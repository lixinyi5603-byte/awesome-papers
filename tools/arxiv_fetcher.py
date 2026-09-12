from __future__ import annotations

import time
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

    # Correctly calculate the next day.
    end_next = (
        datetime.strptime(end, "%Y%m%d") + timedelta(days=1)
    ).strftime("%Y%m%d")

    # Slow down API requests to reduce HTTP 429.
    client = arxiv.Client(
        page_size=100,
        delay_seconds=15.0,
        num_retries=5,
    )

    papers: list[dict] = []
    seen_ids: set[str] = set()

    # Query each category separately.
    # This is more reliable than combining several categories with OR.
    for index, cat in enumerate(cats):
        query = (
            f"cat:{cat} AND "
            f"submittedDate:[{start_date}0000 TO {end_next}0000]"
        )

        search = arxiv.Search(
            query=query,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
            max_results=5000,
        )

        logger.debug(f"Search: {search}")

        try:
            results = list(client.results(search))
        except Exception as exc:
            logger.error(
                f"Failed to fetch category {cat} after retries: {exc}"
            )

            # Do not treat API failure as "0 papers".
            # Let GitHub Actions fail so this date can be retried later.
            raise

        logger.info(
            f"Fetched {len(results)} papers from category {cat}"
        )

        for r in results:
            paper_id = r.entry_id

            # A paper may belong to multiple categories.
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

        # Additional pause between different category queries.
        # No need to sleep after the final category.
        if index < len(cats) - 1:
            logger.info(
                "Waiting 15 seconds before fetching the next category..."
            )
            time.sleep(15)

    logger.info(
        f"Fetched {len(papers)} unique papers total"
    )

    return papers