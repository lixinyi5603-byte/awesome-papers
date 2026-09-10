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
`vision-encoder` `visual-perception` `MLLM` `CLIP` `zero-shot` `retrieval`

---
"""


SYSTEM_PROMPT = """
You are an expert in efficient vision models and multimodal learning.

Given the title and abstract of a paper, determine whether it is relevant to
the following research interests.

### Direction 1: Model Efficiency
Focus on methods for making vision or multimodal models smaller or faster:

- model compression
- quantization, including PTQ, QAT, low-bit and mixed-precision inference
- weight/model pruning and sparsification
- visual token pruning, token merging, token compression or token selection
- efficient inference, reducing FLOPs, latency, memory or computation
- compression or acceleration of vision encoders, ViTs, VLMs or MLLMs

### Direction 2: Vision and Multimodal Models
Focus on:

- vision encoders and Vision Transformers
- multimodal large language models (MLLMs / LVLMs / VLMs)
- visual perception in multimodal models
- fine-grained, region-level or high-resolution visual understanding
- CLIP, SigLIP and vision-language representation learning
- image-text alignment and retrieval
- zero-shot or open-vocabulary vision-language generalization

### Relevance Rules

Highly relevant papers include:
- MLLM / VLM quantization
- visual token pruning or compression
- ViT or vision encoder compression
- efficient multimodal inference
- CLIP compression or quantization
- visual perception improvement for MLLMs

Also keep strong papers about vision encoders, MLLMs, visual perception,
CLIP and zero-shot vision-language learning.

Mark a paper irrelevant if it mainly focuses on:
- text-only LLMs
- pure NLP
- LLM serving or distributed systems unrelated to vision/model compression
- benchmark-only or dataset-only work
- application papers that only use an existing MLLM or CLIP
- traditional detection, segmentation or medical imaging without broadly
  useful compression, representation or vision-language methodology
- pure diffusion generation unrelated to compression

Do NOT judge relevance only by keywords.
Judge the paper's actual contribution.

If relevant, assign at most 3 tags from:
{tag_descriptions}

Generate a concise TLDR of no more than 50 words containing:
1. the problem,
2. the main method,
3. one quantitative result if explicitly stated in the abstract.

Return valid JSON only.

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

    "vision-encoder":
        "vision encoders, Vision Transformers, visual backbones or vision foundation models",

    "visual-perception":
        "fine-grained, region-level, grounding or high-resolution visual perception",

    "MLLM":
        "multimodal large language models, LVLMs or vision-language models",

    "CLIP":
        "CLIP, SigLIP or contrastive vision-language representation learning",

    "zero-shot":
        "zero-shot or open-vocabulary vision-language generalization",

    "retrieval":
        "image-text or cross-modal retrieval",
}


SAMPLE_PAPERS = []
