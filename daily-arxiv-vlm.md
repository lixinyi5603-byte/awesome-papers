
<div align="center">

# Daily Arxiv Papers on Efficient Vision & Multimodal Models

![Static Badge](https://img.shields.io/badge/total_papers-25-blue?logo=gitbook)
![Static Badge](https://img.shields.io/badge/update-2026.09.10-red?logo=fireship)
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
### 2026-09-10
* `quantization` `efficient-inference` `MLLM` [OmniKVQuant: KV Cache Quantization for Omni-LLMs](http://arxiv.org/abs/2609.11582v1)
  > **TL;DR**: 2-bit KV cache quantization for Omni-LLMs via temporal windowed key range and modality-specific value rotation, preserving performance on 7 audio-visual benchmarks.
* `compression` `efficient-inference` [LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation](http://arxiv.org/abs/2609.11739v1)
  > **TL;DR**: Reduces LLM output sequence length by selecting task-aware low-rank adaptation subspaces, cutting tokens by up to 39.84% while updating only 0.24-0.28% of params.
* `compression` `efficient-inference` `MLLM` [X-AuT: Progressive Audio-Encoder Compression for Speech LLMs with Cross-Scale Distillation](http://arxiv.org/abs/2609.11412v1)
  > **TL;DR**: Progressive audio-encoder compression for speech LLMs via cross-scale distillation, reducing parameters by 20.7% (18→14 layers) while lowering error from 5.61% to 5.75%.
* `compression` `efficient-inference` [X-RACE: XAI-assisted Recurrent neural network Attribution for Channel Estimation](http://arxiv.org/abs/2609.11211v1)
  > **TL;DR**: Efficient LSTM for channel estimation via XAI-assisted pruning of input subcarriers and hidden units, reducing inference complexity by 44.1% while maintaining BER performance.
* `compression` `efficient-inference` `token-pruning` [LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation](http://arxiv.org/abs/2609.11739v1)
  > **TL;DR**: Reduces LLM output length via task-aware low-rank adaptation (0.24-0.28% params), cutting Pythia-2.8B tokens by 39.84% without preference loss.
* `quantization` `efficient-inference` `MLLM` [Why Does Post-Training Quantization Work?](http://arxiv.org/abs/2609.11716v1)
  > **TL;DR**: Explains why PTQ works for LLMs despite error accumulation, identifying error cancellation between layers and LM-head geometry as key mechanisms enabling low-bit (e.g., INT8/INT4) quantization without significant performance loss.
* `compression` `efficient-inference` `MLLM` [LILA: Calibration-Free Structured Pruning of Large Language Models via Latent Spectral Geometry](http://arxiv.org/abs/2609.11163v1)
  > **TL;DR**: Calibration-free structured pruning of LLMs via spectral geometry, achieving 25% sparsity without training or calibration data, surpassing PruneNet by 1.57pp in zero-shot accuracy on LLaMA-2-7B.
* `compression` `efficient-inference` `MLLM` [EMMI: Edge Multi-Modal Intelligence for Communication-Efficient MLLM Inference via Fused Representation Compression](http://arxiv.org/abs/2609.11058v1)
  > **TL;DR**: Efficient MLLM inference via fused multimodal compression; modality-specific encoding and learned compression reduce comms by 32x, achieving 3.4x latency reduction for edge deployment.

### 2026-09-09
* `compression` `quantization` `efficient-inference` [AgroVisNet: A lightweight Convolutional Network and the BD-PlantDX Expert-Validated Benchmark for Radish, Potato and Pointed Gourd Disease Classification](http://arxiv.org/abs/2609.10469v1)
  > **TL;DR**: Proposes a lightweight CNN (AgroVisNet) for plant disease classification, achieving 99.52% accuracy with only 290K parameters. Quantized to 0.46 MB (INT8) with minimal accuracy drop (0.22%), and runs in 8.40 ms per image on CPU.
* `token-pruning` `efficient-inference` `MLLM` [Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs](http://arxiv.org/abs/2609.10346v1)
  > **TL;DR**: Sample-adaptive vision token pruning for MLLMs using VIP-Router, dynamically selecting pruning strategies per input, improving accuracy by 26.9% with minimal overhead (0.017% params).
* `compression` `efficient-inference` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Integrates magnitude pruning into active learning cycles to obtain sparse models (95% sparsity) matching dense model accuracy, reducing retraining and scoring costs.
* `token-pruning` `efficient-inference` `MLLM` [TRACE: Trajectory-robust Admission with Evidence Ordering for Efficient GUI Agents](http://arxiv.org/abs/2609.10297v1)
  > **TL;DR**: Training-free visual token pruning for GUI agents reduces memory and latency. Utilizes layout prior, relevance, and novelty to rank tokens, preserving coverage under tight budgets. Achieves up to 40% reduction in inference costs.
* `compression` `efficient-inference` [LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting](http://arxiv.org/abs/2609.10095v1)
  > **TL;DR**: Problem: storage overhead in 3D Gaussian Splatting. Method: replace Gumbel-Sigmoid with linear increment activation for stable pruning. Result: 3.6x Gaussian reduction on Mip-NeRF 360 while maintaining rendering quality.
* `compression` `efficient-inference` [Elastoformer: Enabling Dynamic Adaptivity via Elastic Model Transformation](http://arxiv.org/abs/2609.10018v1)
  > **TL;DR**: Dynamic adaption for edge AI via elastic model transformation, enabling real-time switching to reduce FLOPs by 85%, latency by 50%, and memory by 76%.
* `compression` `efficient-inference` [LightMedSeg-ISLES: Stroke Lesion Segmentation with 81x Fewer Parameters than nnU-Net](http://arxiv.org/abs/2609.09634v1)
  > **TL;DR**: Reduces model size for stroke lesion segmentation with 81x fewer params than nnU-Net, achieving 97.5% Dice at 1.26M params and 4.7x fewer FLOPs.
* `token-pruning` `efficient-inference` `MLLM` [Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs](http://arxiv.org/abs/2609.10346v1)
  > **TL;DR**: Adaptive visual token pruning (VIP-Router) for MLLMs selects optimal pruning strategies per input, outperforming fixed pruning by 26.9% accuracy improvement while reducing tokens dynamically.
* `compression` `efficient-inference` [Elastoformer: Enabling Dynamic Adaptivity via Elastic Model Transformation](http://arxiv.org/abs/2609.10018v1)
  > **TL;DR**: Proposes Elastoformer for dynamic model adaptation in edgeAI, reducing FLOPs by 85%, latency by 50%, and memory by 76% via elastic inference without multiple models.
* `compression` `efficient-inference` [Forward-Free LLM Depth Pruning via Weight Redundancy](http://arxiv.org/abs/2609.09883v1)
  > **TL;DR**: Depth pruning for LLMs using weight redundancy analysis (WRP) to remove Transformer blocks without forward passes. Achieves performance close to activation-based methods by measuring inter-layer weight similarity and projection scales.
* `compression` `efficient-inference` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Integrates iterative magnitude pruning into active learning cycles, yielding 95% sparse models matching dense accuracy, reducing retraining and scoring costs.
* `compression` `efficient-inference` [Forward-Free LLM Depth Pruning via Weight Redundancy](http://arxiv.org/abs/2609.09883v1)
  > **TL;DR**: Proposes Weight-Redundancy Pruning (WRP), a forward-free LLM depth pruning method using inter-layer weight similarity and projection scales to remove redundant Transformer blocks, matching activation-based methods without calibration data.
* `quantization` `efficient-inference` [When Does Low-Bit Quantization Preserve the Decisions of Vector Search?](http://arxiv.org/abs/2609.09854v1)
  > **TL;DR**: Analyzes low-bit quantization's impact on vector search decisions, focusing on comparison-level failures and exact margins. Derives bounds for quantization-induced decision flips and validates correlation gains. Applies to multiple quantization methods.
* `quantization` `efficient-inference` `MLLM` [EFQ-Softmax: Exp-Free Quantization for Softmax](http://arxiv.org/abs/2609.09721v1)
  > **TL;DR**: EFQ-Softmap enables low-bit softmax probability generation (FP8/FP4) by directly mapping scores to E2M1 operands, improving Qwen3-8B accuracy by 0.38% and reducing latency by 40% for 16K-128K sequences.
* `efficient-inference` `token-pruning` [PELM: Power Efficient On-Device LLM Inference with Speculative Decoding and Dynamic Voltage Frequency Scaling](http://arxiv.org/abs/2609.09662v1)
  > **TL;DR**: Efficient on-device LLM inference via speculative decoding and dynamic voltage scaling, reducing energy by 52.4% while maintaining quality.
* `compression` `quantization` `efficient-inference` [LightMedSeg-ISLES: Stroke Lesion Segmentation with 81x Fewer Parameters than nnU-Net](http://arxiv.org/abs/2609.09634v1)
  > **TL;DR**: Stroke lesion segmentation model LightMedSeg-ISLES reduces parameters 81.4x (1.26M vs 102.35M) and FLOPs 4.7x vs nnU-Net while retaining 97.5% Dice (0.618 vs 0.634) and improving lesion-wise F1 by 0.055.
* `token-pruning` `efficient-inference` `MLLM` [TEFM: Token-Efficient Faithful Modeling for Structured Data](http://arxiv.org/abs/2609.09552v1)
  > **TL;DR**: Reduces token consumption in LLMs for structured data by compressing inputs into Behavioral Code tokens, achieving ~1-2% token retention with minimal accuracy loss.

