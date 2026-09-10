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
`MLLM`

---
"""
SYSTEM_PROMPT = """
You are an expert in post-training quantization, model compression, and token pruning.

Given a paper title and abstract, determine whether it is relevant to efficient
and lightweight deep learning models.

Primary focus:
- post-training quantization (PTQ)
- low-bit quantization, especially INT8 / INT4 / INT3 / INT2
- weight-only and weight-activation quantization
- mixed-precision quantization
- quantization calibration, smoothing, rotation, reconstruction, and outlier handling
- quantization error, sensitivity analysis, and bit allocation
- practical low-bit inference and deployment

Secondary focus:
- model compression
- structured or unstructured pruning
- sparsification
- low-rank compression
- parameter reduction
- token pruning
- visual token pruning
- token dropping, selection, merging, or compression
- efficient inference methods that reduce FLOPs, latency, or memory

Give highest priority to papers that combine these directions, such as:
- quantization + model pruning
- quantization + token pruning
- quantization-aware token selection
- joint low-bit quantization and compression
- pruning or token reduction designed for low-bit deployment

Papers on LLMs, VLMs, MLLMs, ViTs, or other foundation models are relevant
only when their main contribution is directly related to quantization,
compression, pruning, token reduction, or inference efficiency.

Mark a paper irrelevant if it mainly focuses on:
- model capability improvement without efficiency or compression
- reasoning, perception, alignment, or multimodal modeling without lightweighting
- benchmarks, datasets, surveys, or application-only work
- general serving, scheduling, networking, or distributed systems without
  direct compression or low-bit inference contributions

Judge the actual contribution rather than keywords.
When uncertain, prefer precision over recall.

If relevant, assign at most 3 strongly related tags from:
{tag_descriptions}

Generate a TLDR of no more than 50 words containing:
1. the main efficiency or compression problem,
2. the key method,
3. the bit-width or compression setting if available,
4. one quantitative result if explicitly stated in the abstract.

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
}


SAMPLE_PAPERS = []
