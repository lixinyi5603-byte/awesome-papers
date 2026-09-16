
<div align="center">

# Daily Arxiv Papers on Efficient Vision & Multimodal Models

![Static Badge](https://img.shields.io/badge/total_papers-48-blue?logo=gitbook)
![Static Badge](https://img.shields.io/badge/update-2026.09.15-red?logo=fireship)
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
### 2026-09-15
* `token-pruning` `efficient-inference` `MLLM` [BrainFocus: EEG-Guided ROI Selection for Efficient Vision-Language Models](http://arxiv.org/abs/2609.17443v1)
  > **TL;DR**: Reduces VLM inference cost via EEG-guided ROI selection, cutting input tokens by 23.2%-39.4% and FLOPs by 23.2%-39.5% while improving accuracy.
* `token-pruning` `efficient-inference` `MLLM` [StackTok: Accelerating VLMs Inference with Budget-Adaptive Visual Token Selection](http://arxiv.org/abs/2609.16841v1)
  > **TL;DR**: Reduces VLM inference cost via budget-adaptive visual token selection, achieving 95.26% full-token performance with 5.6% tokens (160/2880) in LLaVA-NeXT-7B.
* `token-pruning` `efficient-inference` `MLLM` [VideoMM: Adaptive Macro-Micro Inference for Efficient Video MLLMs](http://arxiv.org/abs/2609.16722v1)
  > **TL;DR**: Addresses video MLLM inefficiency by decoupling selection from reasoning, using macro proxies for token pruning and micro tokens for detailed reasoning. Achieves 6.13× speedup and 7.4% accuracy gain over baselines.
* `quantization` `compression` `MLLM` [Efficient Quantization-Aware Distillation with Cross-Modal Alignment for Edge Vision-Language Models](http://arxiv.org/abs/2609.16689v1)
  > **TL;DR**: Quantization-aware distillation for edge VLMs, using QAT within a unified teacher-anchored framework with cross-attention adapters. Achieves efficient deployment while improving non-RGB modality performance.
* `quantization` `token-pruning` `efficient-inference` [Channel-Wise and Token-Aware Post-Training Quantization for Visual State Space Duality](http://arxiv.org/abs/2609.16656v1)
  > **TL;DR**: Addressing activation quantization bottleneck in VSSD models via channel-wise token-balanced output-aware clipping (CTOAC), achieving strong robustness at low-bit settings (precision not specified). COCO/ADE20K task performance preserved with 1.42x speedup on RTX 4090 over FP32.
* `efficient-inference` `quantization` [JustFit: 200K-Token LLM Serving on a 24 GiB Laptop with Just-in-Time State Management](http://arxiv.org/abs/2609.17475v1)
  > **TL;DR**: Efficient LLM serving on laptops via JustFit runtime with compressed KV execution (MXFP4). Achieves 6.93x context increase (212,992 tokens) and 19.11 tokens/s throughput.
* `efficient-inference` `compression` `MLLM` [FlexEE: Self-Speculative and KV-Compatible Early Exiting for Offloading-Aware LLM Inference](http://arxiv.org/abs/2609.17008v1)
  > **TL;DR**: Reduces LLM inference cost via early exiting, self-speculative decoding, and KV-cache optimization, achieving 1.27-3.16x speedup on Llama2-7B with layer reduction.
* `token-pruning` `efficient-inference` `MLLM` [StackTok: Accelerating VLMs Inference with Budget-Adaptive Visual Token Selection](http://arxiv.org/abs/2609.16841v1)
  > **TL;DR**: Efficiency problem: High-resolution images increase visual tokens in VLMs. Method: Budget-adaptive token selection (StackTok) balances query relevance and visual coverage without retraining. Result: Retains 95.26% performance with only 5.6% (160/2880) tokens on LLaVA-NeXT-7B.
* `token-pruning` `efficient-inference` `MLLM` [VideoMM: Adaptive Macro-Micro Inference for Efficient Video MLLMs](http://arxiv.org/abs/2609.16722v1)
  > **TL;DR**: Addresses token explosion in video MLLMs via adaptive macro-micro inference, decoupling selection (low-cost macro proxy) from reasoning (high-fidelity micro tokens). Achieves 6.13× speedup over full-context baselines with 7.4% accuracy gain on LongVideoBench.
* `token-pruning` `efficient-inference` [Protocol-Preserving Context Trimming for Agentic Workflows: Benefits, Failure Regimes, and Budget Guardrails](http://arxiv.org/abs/2609.16461v1)
  > **TL;DR**: Protocol-preserving context trimming for LLM agentic workflows reduces token usage (56% savings) while maintaining high task success (96.0%) and protocol adherence (96.3%), outperforming conventional methods by selectively preserving critical state.
* `efficient-inference` `token-pruning` [Early-Bird Decoding: Accelerating Diffusion LLMs with Learnable Block Sizes and Parallel Sampling](http://arxiv.org/abs/2609.16450v1)
  > **TL;DR**: Accelerates diffusion LLM inference by adaptively grouping low-entropy tokens into variable-length blocks for parallel decoding, achieving up to 18.76x higher throughput without modifying pretrained weights.

### 2026-09-14
* `quantization` `efficient-inference` [VC-Attention: Value Smoothing and Softmax Casting for Low-bit Attention](http://arxiv.org/abs/2609.15810v1)
  > **TL;DR**: Addressing outliers and softmax bottleneck in low-bit attention for efficient deployment. Uses value smoothing with online clustering and ExpCast-FP8 for fused probability casting. Achieves 1.46-1.59x speedup over BF16 FlashAttention-4 on datacenter GPUs.
* `token-pruning` `efficient-inference` `MLLM` [Don't Send What You Don't Need: Question-Guided Token Pruning as a Privacy Defense for Vision-Language Models](http://arxiv.org/abs/2609.15671v1)
  > **TL;DR**: Privacy-aware VLMs with question-guided token pruning (40% tokens retained) for efficient transmission, using Dynamic Threshold Predictor; reduces privacy attack success from 0.99 to 0.76-0.79 while maintaining VQA accuracy.
* `token-pruning` `efficient-inference` `MLLM` [MarKey: Marginal Utility Guided Greedy Keyframe Selection for Long Video Understanding](http://arxiv.org/abs/2609.15408v1)
  > **TL;DR**: Efficient video understanding via subset-aware greedy keyframe selection (MarKey) to reduce redundant frames, achieving robust gains in multimodal LLMs across diverse benchmarks.
* `compression` `efficient-inference` `token-pruning` [SparseTalk - Sparsifying 3D Gaussian Language Fields for Efficient 3D Visual Question Answering](http://arxiv.org/abs/2609.15137v1)
  > **TL;DR**: Reduces dense 3D Gaussian language fields via sparsification for efficient VQA. Uses object-based token selection, cutting input from 32K to 256 tokens (0.8% original size) with 125x memory reduction while retaining performance, showing field redundancy.
* `token-pruning` `quantization` `MLLM` [AdaVSkip: Adaptive Visual Token Skipping Across Layers For Efficient MLLMs Inference](http://arxiv.org/abs/2609.15131v1)
  > **TL;DR**: AdaVSkip reduces MLLM computation by adaptively skipping visual tokens across layers via lightweight routers, achieving 53.2% FLOPs reduction and preserving performance. Combine with token compression for 91.2% FLOPs reduction.

### 2026-09-13
* `compression` `efficient-inference` [Sparsity-Adaptive Sharpness-Aware Minimization](http://arxiv.org/abs/2609.14274v1)
  > **TL;DR**: Improves corruption robustness of pruned models at 80-90% sparsity via sparsity-adaptive SAM and MWH, enhancing clean accuracy and inference throughput.
* `quantization` `efficient-inference` [WaterKron and FlipFlop Hessian: Information-Theoretically Grounded Quantization with Kronecker-factored Hessians](http://arxiv.org/abs/2609.14706v1)
  > **TL;DR**: Proposes WaterKron for PTQ with Kronecker-factored Hessians, using two-sided GPTQ and entropy coding. Derives distortion penalty, leading to optimal FlipFlop Hessian. Improves KL divergence and perplexity.

### 2026-09-11
* `quantization` `efficient-inference` [Attention Quantization for Tabular Foundation Models](http://arxiv.org/abs/2609.13031v1)
  > **TL;DR**: Quantizes attention computation (queries, keys, values) to FP8 in tabular foundation models, achieving 1.7x speedup with no accuracy loss via aligned training-test quantization.
* `compression` `efficient-inference` [Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents](http://arxiv.org/abs/2609.12896v1)
  > **TL;DR**: Addresses LoRA storage and routing overhead in LLM agents via BQ-LoRA, which balances trajectory updates and compresses gradients under fixed-rank constraints, achieving efficient low-rank adaptation without distorting decision distributions.
* `quantization` `efficient-inference` `MLLM` [Quality-Constrained Routing over a Fixed Pool of Quantized Mixture-of-Experts Instances](http://arxiv.org/abs/2609.12550v1)
  > **TL;DR**: Proposes quality-aware routing for quantized MoE models (W2/W3/W4) using Fragility-Weighted Perplexity (FWP) to balance quality vs. throughput, achieving 2.5% better efficiency than baselines with mean ΔNLL of 0.0513 at W4.
* `compression` `efficient-inference` [Theoretical Guarantees for One-Shot Magnitude Pruning and Compute-Adaptive Early Exit](http://arxiv.org/abs/2609.12337v1)
  > **TL;DR**: Studies one-shot magnitude pruning and early exits for compute reduction; proves theoretical guarantees for pruning efficiency and shows decay of generalization error with compute gap. Theoretical and empirical results support scaling laws.
* `compression` `quantization` `efficient-inference` [ESTS at WMT26: Routing-Informed Expert Pruning for Model Compression](http://arxiv.org/abs/2609.12310v1)
  > **TL;DR**: Combines expert pruning (1. routing-informed selection, 2. cross-lingual divergence) with MXFP4 quantization on GPT-OSS-20B, yielding models from 4.186B to 7.770B params and 4.55-6.33GiB sizes while maintaining translation quality.

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

