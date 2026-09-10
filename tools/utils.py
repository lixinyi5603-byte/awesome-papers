# Static strings and sample data used by the fetcher


README_HEADER = """
<div align="center">

# Daily Arxiv Papers on Efficient Vision & Multimodal Models

![Static Badge](https://img.shields.io/badge/total_papers-{papers}-blue?logo=gitbook)
![Static Badge](https://img.shields.io/badge/update-{update}-red?logo=fireship)
[![Static Badge](https://img.shields.io/badge/arXiv-cs.CV-green)](https://arxiv.org/list/cs.CV/recent)
[![Static Badge](https://img.shields.io/badge/arXiv-cs.LG-green)](https://arxiv.org/list/cs.LG/recent)
[![Static Badge](https://img.shields.io/badge/arXiv-cs.AI-green)](https://arxiv.org/list/cs.AI/recent)

`Fetch from arXiv` → `LLM Filter` → `GitHub Workflow Update`

</div>

**🎯 Research Focus**:
Model Compression · Quantization · Token Pruning · Vision Encoder ·
Multimodal Large Language Models · Visual Perception · CLIP

**🔖 TAGS**:
`compression` `quantization` `token-pruning` `efficient-inference`
`MLLM` `CLIP`

---
"""


SYSTEM_PROMPT = """
You are an expert in model compression, multimodal large language models,
vision-language models, and CLIP-like models.

Given a paper title and abstract, determine whether it is relevant to the
following research scope.

Relevant topics:
- model compression, pruning, sparsification, low-rank compression
- quantization: PTQ, QAT, low-bit and mixed-precision inference
- token pruning, token merging, token compression, token selection
- efficient inference: reducing FLOPs, latency, memory, or computation
- MLLMs / LVLMs / VLMs
- CLIP and contrastive vision-language models
- multimodal representation, alignment, fusion, and visual token processing
- fine-grained, region-level, or high-resolution visual understanding

Give higher priority to papers combining model efficiency with multimodal or
vision-language models, such as MLLM quantization, visual token pruning,
multimodal model compression, and efficient VLM/MLLM inference.

Mark a paper irrelevant if it mainly focuses on:
- text-only LLMs or pure NLP
- general LLM serving, scheduling, networking, or distributed systems unrelated
  to multimodal models or compression
- benchmark-only, dataset-only, survey, or application-only work
- traditional detection, segmentation, tracking, medical imaging, autonomous
  driving, or remote sensing without broadly useful compression or multimodal methods
- image-text retrieval or zero-shot recognition
- pure diffusion generation

Judge the paper by its actual contribution, not by keyword matching alone.
When uncertain, prefer precision over recall.

If relevant, assign at most 3 strongly related tags from:
{tag_descriptions}

Generate a TLDR of no more than 50 words containing:
1. the main problem,
2. the key method,
3. one quantitative result if explicitly stated in the abstract.

Return JSON only.

Relevant:
{"relevant": true, "tags": ["tag1", "tag2"], "tldr": "..."}

Irrelevant:
{"relevant": false}
"""


USER_PROMPT = """
Title: {title}

Abstract:
{abstract}
"""


TAGS = {
    "compression":
        "model compression, pruning, sparsification or parameter reduction",

    "quantization":
        "PTQ, QAT, low-bit, weight/activation or mixed-precision quantization",

    "token-pruning":
        "visual token pruning, token merging, token selection or token compression",

    "efficient-inference":
        "reducing inference FLOPs, latency, memory or computational cost",

    "MLLM":
        "multimodal large language models, LVLMs or vision-language models",

    "CLIP":
        "CLIP, SigLIP or contrastive vision-language representation learning",
}


SAMPLE_PAPERS = []
