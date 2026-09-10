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
You are an expert in model compression and efficient deep learning.

Given a paper title and abstract, determine whether it is relevant to model
lightweighting and efficient inference.

Relevant topics include:
- model compression
- structured or unstructured pruning
- sparsification
- low-rank compression
- parameter reduction
- quantization: PTQ, QAT, low-bit and mixed-precision inference
- weight and activation quantization
- token pruning, token merging, token selection, and token compression
- efficient attention
- efficient inference
- reducing FLOPs, latency, memory, bandwidth, or computational cost
- lightweight model architecture
- compression or acceleration of vision, multimodal, or language models

Give higher priority to papers about:
- quantization
- model pruning
- token pruning / token compression
- joint compression methods
- efficient inference
- lightweight deployment

A paper about MLLMs, VLMs, CLIP, ViTs, or LLMs is relevant only if its main
contribution is directly related to model compression, pruning, quantization,
token reduction, or inference efficiency.

Mark a paper irrelevant if it mainly focuses on:
- model capability improvement without efficiency or compression
- multimodal reasoning or visual perception without lightweighting
- benchmarks, datasets, surveys, or application-only work
- general distributed systems, scheduling, networking, or serving without
  direct model compression or inference-efficiency contributions
- traditional vision or NLP tasks without reusable lightweighting methods
- pure diffusion generation without compression or acceleration

Judge the actual contribution rather than keywords.
When uncertain, prefer precision over recall.

If relevant, assign at most 3 strongly related tags from:
{tag_descriptions}

Generate a TLDR of no more than 50 words containing:
1. the main compression or efficiency problem,
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
}


SAMPLE_PAPERS = []
