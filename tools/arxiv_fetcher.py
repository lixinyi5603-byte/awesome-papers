from __future__ import annotations

from datetime import datetime, timedelta
from typing import Iterable, List

import arxiv

from config import logger


def _ensure_list(categories: Iterable[str] | str) -> list[str]:
    return [categories] if isinstance(categories, str) else list(categories)


def fetch_arxiv_papers(
    categories: Iterable[str] | str,
    start_date: str,
    end_date: str | None = None,
) -> List[dict]:
    """
    Fetch papers from arXiv within a date window.

    Args:
        categories:
            e.g. ["cs.CV", "cs.AI", "cs.LG"] or "cs.CV"
        start_date:
            YYYYMMDD
        end_date:
            YYYYMMDD. If None, equals start_date.

    Returns:
        List of dicts with:
        title, link, abstract, authors, categories, id
    """

    cats = _ensure_list(categories)
    end = end_date or start_date

    logger.info(
        f"Fetching arXiv papers for {cats} from {start_date} to {end}"
    )

    # ------------------------------------------------------------------
    # Correctly calculate the day after end_date.
    # Do NOT use int(end) + 1 because dates such as 20260930 would
    # incorrectly become 20260931.
    # ------------------------------------------------------------------

    end_next = (
        datetime.strptime(end, "%Y%m%d") + timedelta(days=1)
    ).strftime("%Y%m%d")

    # ------------------------------------------------------------------
    # Combine categories into ONE arXiv query.
    #
    # Example:
    # (cat:cs.CV OR cat:cs.AI OR cat:cs.LG)
    # AND submittedDate:[... TO ...]
    #
    # This avoids making three independent searches.
    # ------------------------------------------------------------------

    category_query = " OR ".join(f"cat:{cat}" for cat in cats)

    query = (
        f"({category_query}) "
        f"AND submittedDate:[{start_date}0000 TO {end_next}0000]"
    )

    search = arxiv.Search(
        query=query,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
        max_results=5000,
    )

    logger.debug(f"Search: {search}")

    # ------------------------------------------------------------------
    # Slow down requests to reduce the chance of HTTP 429.
    #
    # page_size=100:
    #   Smaller pages are generally more reliable.
    #
    # delay_seconds=10:
    #   Wait at least 10 seconds between API page requests.
    #
    # num_retries=5:
    #   Let the arxiv package retry failed requests.
    # ------------------------------------------------------------------

    client = arxiv.Client(
        page_size=100,
        delay_seconds=10.0,
        num_retries=5,
    )

    papers: list[dict] = []

    # Used to avoid duplicate papers.
    # A paper may belong to multiple categories.
    seen_ids: set[str] = set()

    try:
        results = client.results(search)

        for r in results:

            paper_id = r.entry_id

            if paper_id in seen_ids:
                continue

            seen_ids.add(paper_id)

            logger.debug(f"Found paper: {r.title}")

            papers.append(
                {
                    "title": r.title,
                    "link": r.entry_id,
                    "abstract": r.summary,
                    "authors": [a.name for a in r.authors],
                    "categories": r.categories,
                    "id": r.entry_id,
                }
            )

    except Exception as exc:
        # Important:
        # Do not silently pretend that "0 papers" means success.
        logger.error(
            f"Failed to fetch arXiv papers after retries: {exc}"
        )

        # Let GitHub Actions fail.
        # This prevents the current date from being incorrectly marked
        # as successfully processed.
        raise

    logger.info(f"Fetched {len(papers)} papers total")

    return papers