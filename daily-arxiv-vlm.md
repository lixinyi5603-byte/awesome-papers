
<div align="center">

# Daily Arxiv Papers on Efficient Vision & Multimodal Models

![Static Badge](https://img.shields.io/badge/total_papers-448-blue?logo=gitbook)
![Static Badge](https://img.shields.io/badge/update-2026.10.06-red?logo=fireship)
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
### 2026-10-06
* `efficient-inference` `token-pruning` [Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation](http://arxiv.org/abs/2610.08772v1)
  > **TL;DR**: Reduces quadratic attention cost in Diffusion Transformers via backend-agnostic sparse attention, eliminating artifacts while achieving 4.52x speedup in attention computation.
* `quantization` `efficient-inference` [Test-Time Adaptation of Quantized ViTs via Single-Pass Quantizer-Aligned Recalibration](http://arxiv.org/abs/2610.08358v1)
  > **TL;DR**: Proposes QuAR, a test-time adaptation method for quantized ViTs without backprop or parameter updates, aligning activation ranges to mitigate distribution shift. Works at 3-8 bits, improving ImageNet-C accuracy by 2.28-4.00 points with 46% lower latency.
* `token-pruning` `efficient-inference` `MLLM` [DIPrune: Task-Aware Token Pruning with Dual Importance for Efficient Multimodal Language Models](http://arxiv.org/abs/2610.08341v1)
  > **TL;DR**: Task-aware token pruning for MLLMs using dual importance scoring (intra-layer saliency & inter-layer gradient dynamics) to cut computational cost while minimizing semantic loss. Achieves SOTA on LLaVA/Qwen-VL.
* `token-pruning` `efficient-inference` `MLLM` [VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models](http://arxiv.org/abs/2610.08133v1)
  > **TL;DR**: Action-Consistent Learning prunes 87.5% of visual tokens in VLAs via action-level supervision, boosting speed 1.5x without model updates.
* `compression` `efficient-inference` [Two Halves are More than One: Phase-wise Velocity Distillation for Fast and High-Quality Image Generation](http://arxiv.org/abs/2610.08070v1)
  > **TL;DR**: Reduces diffusion model inference cost by partitioning generation into coarse and fine phases with half-sized experts, cutting parameters by ~50% and VRAM by ~47%, while achieving FID 1.48 on ImageNet 256x256.
* `token-pruning` `efficient-inference` `MLLM` [VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs](http://arxiv.org/abs/2610.07987v1)
  > **TL;DR**: Enables elastic visual representation in MLLMs via gated spatial pooling and granularity routing, saving 43% tokens while retaining 98.9% performance, boosting throughput 2.3x with 54.4% lower TTFT.
* `token-pruning` `efficient-inference` `MLLM` [Decide Before You Look: Learning Which Retrieved Memories Deserve Pixels](http://arxiv.org/abs/2610.07984v1)
  > **TL;DR**: Predicts which retrieved images need full-resolution pixels for QA using thumbnails, pruning 77-89% visual tokens (11-23% usage) with no accuracy drop, enabling 2.9x faster inference vs full processing.
* `token-pruning` `efficient-inference` [Later Is Better: Token Reduction for ViTs Under Distribution Shift](http://arxiv.org/abs/2610.07758v1)
  > **TL;DR**: Improves out-of-distribution accuracy for token-reduced ViTs via a late-concentrated power-law schedule. Retains 26% compute (+1.17pp accuracy) on ImageNet-C with DeiT-S, outperforming flat schedules. Works across multiple pruning methods and domains.
* `token-pruning` `compression` `MLLM` [Foveated Compression: Selective High-Resolution Preservation for Token-Efficient VLMs](http://arxiv.org/abs/2610.07729v1)
  > **TL;DR**: Proposes Foveated Compression for VLMs, selectively preserving high-resolution tokens at 11.11-20.99% of visual tokens, with learned selection outperforming random allocation (69.61 macro accuracy) but below oracle (82.73).
* `compression` `efficient-inference` [MemFLoRA: Memory-Floor LoRA for CNN Adaptation at the Edge](http://arxiv.org/abs/2610.08669v1)
  > **TL;DR**: Reduces CNN adaptation memory via Memory-Floor LoRA, freezing down-projection and minimizing activation state, cutting saved-activation by 98.5-98.7% and peak training memory by 94.9-97.3% compared to full fine-tuning.
* `compression` `efficient-inference` [Micro Neural Policies for Safe Real-Time Robotic Control](http://arxiv.org/abs/2610.08541v1)
  > **TL;DR**: Compresses neural policies for robotic control via ES and SMC, reducing memory to 0.5-7.5 kB while maintaining real-time performance (<25 ns jitter).
* `quantization` `efficient-inference` `compression` [Test-Time Adaptation of Quantized ViTs via Single-Pass Quantizer-Aligned Recalibration](http://arxiv.org/abs/2610.08358v1)
  > **TL;DR**: Test-time adaptation for quantized ViTs via Quantizer-Aligned Recalibration (QuAR), a backprop-free method recalibrating activations for 3-8 bit weights/activations, improving ImageNet-C accuracy by 2.28 points at 8 bits with 46% lower latency.
* `quantization` `efficient-inference` `MLLM` [OSFP4: Joint Optimization of Diagonal Smoothing and Block Scales for NVFP4 Quantization](http://arxiv.org/abs/2610.08231v1)
  > **TL;DR**: Optimizes NVFP4 quantization for LLMs via joint diagonal smoothing & block scale optimization, preserving 94-97% throughput while minimizing quantization error.
* `compression` `efficient-inference` `token-pruning` [Compact Robot Policies Need Fine-Grained Visual Representations](http://arxiv.org/abs/2610.08183v1)
  > **TL;DR**: Compact robot policy (48.9M params) uses pretrained, compressed representations and token pruning (48 tokens vs all patches) to match larger systems (40.9-163.6x), achieving 97.0% on LIBERO with 19.8% drop if encoder is frozen.
* `token-pruning` `efficient-inference` `MLLM` [VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs](http://arxiv.org/abs/2610.07987v1)
  > **TL;DR**: Adaptive visual token compression for MLLMs via gated spatial pooling and granularity routing, saving 43% tokens while retaining 98.9% performance, achieving 2.3x throughput gain.
* `token-pruning` `efficient-inference` `MLLM` [Decide Before You Look: Learning Which Retrieved Memories Deserve Pixels](http://arxiv.org/abs/2610.07984v1)
  > **TL;DR**: Problem: reduce unnecessary visual token processing in multimodal QA. Method: PixelTriage predicts useful images before full processing. Efficiency: 11-23% visual tokens used. Result: 2.9x faster inference on DMV with no accuracy drop.
* `efficient-inference` `compression` [Hybrid Latent Attention for Looped Language Models](http://arxiv.org/abs/2610.07940v1)
  > **TL;DR**: Reduces KV cache size in looped language models by compressing old tokens to latents, shrinking cache 10.7x per token, improving throughput 2.5-7.4x, and retaining 97% accuracy. (Ouro looped models, 1.4B and 2.6B parameters)
* `token-pruning` `efficient-inference` [ReFold: Training-Free Reversible Inter-Turn Context Folding for Long-Horizon Agents](http://arxiv.org/abs/2610.07863v1)
  > **TL;DR**: Reduces long-horizon agent token consumption via reversible inter-turn context folding, cutting tokens by 2.5x and KV-cache memory by 50% without degrading task success.
* `token-pruning` `efficient-inference` [Later Is Better: Token Reduction for ViTs Under Distribution Shift](http://arxiv.org/abs/2610.07758v1)
  > **TL;DR**: Token reduction for ViTs under distribution shift via late-concentrated power-law schedule, maintaining accuracy at 26% compute reduction (+1.17pp on ImageNet-C with DeiT-S).
* `compression` `efficient-inference` [VALSE: Vertical Adaptive Layer Skipping for Efficient Inference in Large Language Models](http://arxiv.org/abs/2610.07606v1)
  > **TL;DR**: Efficient inference in LLMs via adaptive layer skipping, reducing FLOPs by selectively activating only necessary layers based on input difficulty, with theoretical guarantees on function space approximation and FLOPs savings.
* `compression` `efficient-inference` [MemFLoRA: Memory-Floor LoRA for CNN Adaptation at the Edge](http://arxiv.org/abs/2610.08669v1)
  > **TL;DR**: Memory-Floor LoRA (MemFLoRA) reduces activation-memory during CNN adaptation by freezing down-projection and training scale-matched up-projection, achieving 98.5-98.7% reduction in saved-activation memory.
* `quantization` `compression` `efficient-inference` [SSR: Sparse Segment Reduction for Ternary GEMM Acceleration](http://arxiv.org/abs/2610.08403v1)
  > **TL;DR**: Proposes SSR for ternary (INT2) LLM acceleration via optimized sparsity structures, achieving 2.1-11.3x GEMM speedup over RSR++ and 3.5-6.3x end-to-end speedup on Llama-3 1B with 45-95% sparsity.
* `token-pruning` `efficient-inference` `MLLM` [DIPrune: Task-Aware Token Pruning with Dual Importance for Efficient Multimodal Language Models](http://arxiv.org/abs/2610.08341v1)
  > **TL;DR**: Task-aware token pruning for MLLMs using dual importance scoring, achieves SOTA results on LLaVA and Qwen-VL by minimizing task loss distortion.
* `compression` `token-pruning` `efficient-inference` [Compact Robot Policies Need Fine-Grained Visual Representations](http://arxiv.org/abs/2610.08183v1)
  > **TL;DR**: Efficient robot policy by compressing visual representations using 48 tokens per view (token pruning) and pretraining, matching performance of larger models with 48.9M params, achieving 97.0% on LIBERO.
* `quantization` `compression` `efficient-inference` [Align, Then Correct: Training-Free Two-Stage Low-Rank Compensation for Extremely Quantized Large Language Models](http://arxiv.org/abs/2610.08164v1)
  > **TL;DR**: Proposes a training-free low-rank compensation method for extreme-weight-quantized LLMs (2-bit). It uses a two-stage closed-form adaptation (asymmetric alignment + natural-gradient step) to recover accuracy, e.g., reducing WikiText-2 perplexity from 12.43 to 10.26 on Qwen3-8B under QuIP#.
* `quantization` `efficient-inference` [ApexQuant: Data-Free Elastic Quantization by Residual Re-Isotropization](http://arxiv.org/abs/2610.07904v1)
  > **TL;DR**: Data-free elastic quantization by residual re-quantization, achieving near full-precision accuracy at 4 bits and best 2-bit results without calibration, via recursive error re-isotropization.
* `compression` `efficient-inference` `token-pruning` [ReFold: Training-Free Reversible Inter-Turn Context Folding for Long-Horizon Agents](http://arxiv.org/abs/2610.07863v1)
  > **TL;DR**: Reduces token consumption in long-horizon LLM agents by training-free reversible context folding, achieving 2.5x token reduction and 1.7x faster inference.
* `quantization` `efficient-inference` [Lost in the bf16 Cast: Exporting Ternary Language Models Can Revert Most Low-Learning-Rate Code Changes](http://arxiv.org/abs/2610.07853v1)
  > **TL;DR**: Audits ternary model export pipelines revealing bf16 casting issues causing accuracy drops; proposes two remedies to preserve accuracy (Falcon-E-1B-Base GSM8K accuracy recovers from 0.78% to ~58.79%).
* `quantization` `efficient-inference` `MLLM` [TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](http://arxiv.org/abs/2610.07767v1)
  > **TL;DR**: Efficient FP4 RL quantization for MoE LLMs via rollout-guided QAT, reducing train-rollout discrepancy, achieving joint FP4 weight/activation + KV-cache with 5.4x rollout speedup vs. BF16.

### 2026-10-05
* `token-pruning` `efficient-inference` `compression` [Less Context, Better Geometry: Masked Geometric Encoder for Robust 3D Foundation Models](http://arxiv.org/abs/2610.06813v1)
  > **TL;DR**: Proposes a Masked Geometric Encoder (MGE) for 3D foundation models, reducing quadratic attention complexity via token dropping and adaptive merging. Achieves inference speedup with better occlusion handling.
* `compression` `token-pruning` `efficient-inference` [MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers](http://arxiv.org/abs/2610.06801v1)
  > **TL;DR**: Reduces diffusion transformer latency via sparse attention with token grouping and KV selection, achieving 1.8-2.32x speedups in video/3D generation without quality loss.
* `token-pruning` `efficient-inference` [Video Encoders Built on Image Representations](http://arxiv.org/abs/2610.06616v1)
  > **TL;DR**: Proposes a compact video encoder by selecting relevant visual tokens (28%-35% of full tokens) across frames, achieving 62.75 benchmark score with 1,535 tokens and 2.16x speedup on Qwen3-VL-8B.
* `quantization` `efficient-inference` `MLLM` [CentriQ: Calibration-Free Quantization of Diffusion Transformers via Exact Mean Centering](http://arxiv.org/abs/2610.06260v1)
  > **TL;DR**: Quantizes diffusion transformers to 4-bit weights and activations via exact mean centering, avoiding calibration; matches SVDQuant at 4-bit and achieves usable quality at 2-bit.
* `token-pruning` `efficient-inference` [Level-of-Token Diffusion](http://arxiv.org/abs/2610.05816v1)
  > **TL;DR**: Efficient diffusion models via adaptive token allocation (LoT layout) for reduced computation, using multiresolution tokens for detail-aware processing, achieving speedups with quality-efficiency tradeoffs based on token budget.
* `quantization` `compression` `efficient-inference` [Paradee: Distilling Kokoro-82M into an 8M-Parameter Single-Voice Text-to-Speech Model](http://arxiv.org/abs/2610.06817v1)
  > **TL;DR**: Distills 82M TTS model into 8M params via layer narrowing & separate training, quantized to INT8, achieving 8.5MB size, 25x real-time CPU inference, with UTMOS score 4.41 (vs teacher 4.52).
* `token-pruning` `efficient-inference` [MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers](http://arxiv.org/abs/2610.06801v1)
  > **TL;DR**: Proposes Meta-Cached Sparse Attention (MC-Sparse) to reduce diffusion transformer latency by selecting key-value tokens & query grouping, achieving 1.8-2.32x speedup with negligible quality loss.
* `quantization` `efficient-inference` `token-pruning` [Quantifying the Stability of Multi-Step Reasoning via Error Amplification](http://arxiv.org/abs/2610.06404v1)
  > **TL;DR**: Analyzes stability of multi-step reasoning via Jacobian norms, proposes chain-of-thought length compression and quantization-aware training. Achieves 8.2% improvement for long inputs and 3-8x stability reduction via Jacobian regularization.
* `quantization` `efficient-inference` `compression` [CentriQ: Calibration-Free Quantization of Diffusion Transformers via Exact Mean Centering](http://arxiv.org/abs/2610.06260v1)
  > **TL;DR**: Proposes CentriQ for 4/2-bit weight-activation quantization of diffusion transformers via exact mean centering and closed-form per-token scaling without calibration; matches calibrated SVDQuant at 4 bits and retains usable quality at 2-bit activations.
* `quantization` `compression` `efficient-inference` [Differentiable Bit-Widths: Co-optimizing Pruning and Quantization via SVD for Ultra-Efficient LLM Compression](http://arxiv.org/abs/2610.06026v1)
  > **TL;DR**: Co-optimizes pruning and quantization via differentiable bit-width learning for LLMs, achieving 1.61-bit ultra-efficient compression with superior performance to decoupled methods.
* `token-pruning` `efficient-inference` [Level-of-Token Diffusion](http://arxiv.org/abs/2610.05816v1)
  > **TL;DR**: Introduces Level-of-Token Diffusion (LoT) for efficient diffusion models, using adaptive multi-resolution tokens to reduce computation where less detail is needed, achieving significant speedups depending on token budget.
* `compression` `quantization` `efficient-inference` [Paradee: Distilling Kokoro-82M into an 8M-Parameter Single-Voice Text-to-Speech Model](http://arxiv.org/abs/2610.06817v1)
  > **TL;DR**: Distills an 82M TTS model into an 8M-param model, quantized to INT8 (8.5MB), achieving 25x real-time speed on CPU with minimal quality drop (UTMOS 4.41 vs 4.52).
* `compression` `quantization` `efficient-inference` [Co-Optimizing Graph Sparsification and Approximate Computing for Energy-Efficient FPGA-Based GCN Inference](http://arxiv.org/abs/2610.06138v1)
  > **TL;DR**: Co-optimizes graph sparsification and 8-bit quantization for GCNs on FPGAs, achieving 9.88× speedup with 86.6% accuracy on Amazon Photo at <1W power.
* `quantization` `compression` `efficient-inference` [StagQ: Constraint-Driven Multi-Precision Weight Quantization for LLMs](http://arxiv.org/abs/2610.05977v1)
  > **TL;DR**: Multi-precision weight quantization for LLMs with 2-bit group-wise base + 1-bit refinements, achieving 2-4 bit precision and 3.1-7.0 MMLU points improvement on Llama-3.1-8B.
* `quantization` `efficient-inference` `MLLM` [Beyond In-Distribution Preservation: Recovering Generalization in Quantized VLAs via Vulnerability-Oriented Tuning](http://arxiv.org/abs/2610.05745v1)
  > **TL;DR**: Addresses robustness loss in quantized Vision-Language-Action models via selective vulnerability-aware tuning (PIVOT-Q), achieving recovery with 7.4% of full distillation budget.

### 2026-10-04
* `token-pruning` `efficient-inference` [Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training](http://arxiv.org/abs/2610.05416v1)
  > **TL;DR**: Proposes Prism, a dynamic sparse attention method for joint video-audio generation training, reducing redundant tokens via spatiotemporal macro-zones and hybrid block selection, achieving 2.5× training speedup over full attention.
* `compression` `efficient-inference` [Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting](http://arxiv.org/abs/2610.05289v1)
  > **TL;DR**: Mobile-4DGS reduces storage and computational overhead for real-time 3D Gaussian Splatting on mobile devices via Monte Carlo Specular Energy Aggregator for compact appearance and Multi-View Alpha-Based Densification for primitive pruning, achieving efficient inference.
* `token-pruning` `efficient-inference` `MLLM` [When and What to Prune? Stage-Aware Visual Token Pruning for Efficient VLA](http://arxiv.org/abs/2610.05273v1)
  > **TL;DR**: Stage-aware visual token pruning for VLA models, using adaptive layer selection and dual-path pruning to remove 87.5% of tokens while maintaining task success, achieving 1.718x speedup.
* `compression` `efficient-inference` [TIRMamba: A Thermal-Prior-Modulated State-Space Network for Sub-Million-Parameter Infrared Image Super-Resolution](http://arxiv.org/abs/2610.05182v1)
  > **TL;DR**: Efficient infrared super-resolution with sub-million parameter network, achieving 29-40x fewer parameters and 2.8-9.4x lower latency compared to state-of-the-art.
* `compression` `token-pruning` `efficient-inference` [LightVLN: Efficient Aerial Vision-and-Language Navigation with Compact Memory and History-Guided Local Aggregation](http://arxiv.org/abs/2610.05024v1)
  > **TL;DR**: Efficient aerial VLN by compressing history to 1 token per frame and reducing current observation from 256 to 32 tokens, achieving 14.61Hz inference with a 0.5B backbone.
* `compression` `efficient-inference` [Task-Aware Joint Pruning and Distillation for Efficient Audio Deepfake Detection](http://arxiv.org/abs/2610.05264v1)
  > **TL;DR**: Compresses SSL-based audio deepfake detectors via joint pruning & distillation, reducing model to 31.9M params (6.3x FLOPs reduction) with only 1.30% performance drop.
* `compression` `efficient-inference` [LiFT: Loop Flow Transformers](http://arxiv.org/abs/2610.05538v1)
  > **TL;DR**: Reduces computation in generative models by looping a shared Diffusion Transformer core, achieving 52% fewer inference FLOPs and 60% fewer parameters than baseline while improving FID by 3.34.
* `token-pruning` `quantization` `efficient-inference` [Underscoring the Problem: Why Softpick Fails at Initialization](http://arxiv.org/abs/2610.05488v1)
  > **TL;DR**: Addresses high activation dynamic range in low-precision inference via Softpick's rectified attention, separating denominator terms. Enables training from scratch (230M params) with fewer dead heads and reliable passkey retrieval.
* `quantization` `efficient-inference` `MLLM` [Understanding the Weight Averaging Mechanism in LLM Training for Post-Training Quantization](http://arxiv.org/abs/2610.05329v1)
  > **TL;DR**: Analyzes weight averaging in LLM pretraining to improve post-training quantization robustness, demonstrating better stability for coarser quantization (e.g., INT8). Achieves Pareto-optimal trade-off between accuracy and quantization robustness.
* `efficient-inference` `quantization` `MLLM` [Robust Parameter-Efficient LLM Adaptation on Analog Hardware](http://arxiv.org/abs/2610.05318v1)
  > **TL;DR**: Efficient LLM adaptation for analog hardware using LoRA with input reshaping and update accumulation. Reduces MVM errors and preserves updates with only 20 conductance states. Improves fine-tuning under noise and finite-resolution programming.
* `quantization` `efficient-inference` `compression` [Loopy: Low-Bit Quantization Framework for Looped Language Models](http://arxiv.org/abs/2610.05265v1)
  > **TL;DR**: PTQ framework for looped LMs using depth-aware quantization of shared recurrent core via channel scaling & orthogonal rotations at target deployment depth. W4A4 reduces perplexity by 36.5% vs SpinQuant on Ouro-1.4B.

### 2026-10-03
* `compression` `token-pruning` `efficient-inference` [Investigating Spatiotemporal Redundancy in Video Transformer for Collision Anticipation](http://arxiv.org/abs/2610.04727v1)
  > **TL;DR**: Reduces video transformer computation via temporal token merging (50% FLOPs reduction to 178.5 GFLOPs) and MLP pruning, achieving 1.76x speedup with minimal mAP drop (0.7478 to 0.7443).
* `token-pruning` `efficient-inference` `MLLM` [FLASHSWIN: Unlocking Large Windows and Dense Tokens in Swin Vision Transformers with Memory Efficient Attention](http://arxiv.org/abs/2610.04664v1)
  > **TL;DR**: Improves attention efficiency in Swin ViTs via FlashAttention, reducing per-window memory from O(M^4) to O(M^2), enabling larger windows (M=32) and dense tokens (p=2) with 12.4GB memory, achieving +1.3% ImageNet accuracy over SwinV2-T.
* `quantization` `efficient-inference` `compression` [RPFQ-ViT: Rotated Phase-Frame Quantization for Extremely Low-Bit Weights in Vision Transformers](http://arxiv.org/abs/2610.04457v1)
  > **TL;DR**: RPFQ-ViT proposes rotated phase-frame quantization for extremely low-bit ViTs, achieving 79.33% Top-1 on ImageNet with W2/A4, reducing model size by 5.4-7.1× and latency by 1.4-1.6×.
* `token-pruning` `efficient-inference` `MLLM` [Rethinking Long-Video Efficiency: A Joint Allocation Perspective on Frames, Pixels, and Front-End Latency](http://arxiv.org/abs/2610.04318v1)
  > **TL;DR**: Efficient long-video understanding by trading per-frame resolution for denser temporal coverage, combining dense low-res and sparse high-res frames (LoHi), reducing front-end latency by 7x and improving accuracy by 10.6pp at matched token budget.
* `token-pruning` `efficient-inference` `MLLM` [FlashGaze: Training-Free Multi-Scale Patch Pruning For Efficient Video Understanding](http://arxiv.org/abs/2610.04225v1)
  > **TL;DR**: Training-free visual token pruning for efficient video understanding in MLLMs via pixel-space spatiotemporal redundancy reduction, achieving 5.4x ViT speedup and 17x prefill speedup with 98% accuracy retention.
* `compression` `efficient-inference` `MLLM` [More Value per Key: Asymmetric Sparse Attention for Faster LLM Decoding](http://arxiv.org/abs/2610.04753v1)
  > **TL;DR**: Reduces LLM decoding cost by asymmetric sparse attention (SAGA), decoupling key/value heads with top-N sparsity. Achieves 2x speedup over full-attention GQA baseline at long contexts with 1.5B params.
* `token-pruning` `efficient-inference` [LatentIndex: Cross-Layer Sharing with Layer-Specific Selection for Sparse Attention](http://arxiv.org/abs/2610.04635v1)
  > **TL;DR**: Efficient sparse attention via cross-layer index sharing with layer-specific selection. LatentIndex shares latent caches, reducing indexer-cache storage by 61.1% and achieving 2.30-2.72x decode speedups over DSA.
* `compression` `efficient-inference` `MLLM` [InferOpt: Constrained Multi-Objective Search for LLM Inference Configurations](http://arxiv.org/abs/2610.04473v1)
  > **TL;DR**: Efficient LLM inference via constrained multi-objective search for layer-wise configurations. InferOpt optimizes KV cache (reducing by 64.4%) and MoE expert routing (43.0% fewer token-expert pairs) while maintaining performance.
* `efficient-inference` `compression` [MOIRA: Mass-Oriented Indexing with Ragged Attention for Long-Context Decoding](http://arxiv.org/abs/2610.04313v1)
  > **TL;DR**: Reduces KV cache memory bandwidth in long-context decoding via adaptive sparse attention (coverage rule γ=0.99, 70% page reduction), cutting time per token by 2.2-2.5× vs dense.
* `compression` `efficient-inference` [FTD-GNO: Memory-Efficient Graph Neural Operators through Functional Tensor Decomposition of the Kernel](http://arxiv.org/abs/2610.04212v1)
  > **TL;DR**: Reduces memory overhead in Graph Neural Operators via functional tensor decomposition, achieving lower peak memory and shorter training times without full kernel materialization.
* `quantization` `compression` `efficient-inference` [BARQ: Balanced Codebook Refinement for Low-Bit LLM Quantization](http://arxiv.org/abs/2610.04490v1)
  > **TL;DR**: Improves LLM weight quantization via balanced fitting of codebooks using entropically regularized optimal transport. BARQ achieves lower perplexity and higher accuracy at comparable low-bit budgets vs. baselines.
* `quantization` `efficient-inference` [Saying, Not Knowing: Aggressively GGUF-Quantized Small Language Models Still Write Rare Words They Can No Longer Define](http://arxiv.org/abs/2610.04403v1)
  > **TL;DR**: Assesses rare word semantics loss in aggressively GGUF-quantized SLMs (down to ~2.6b Q2_K), finding sub-2B models lose 20-67% definition accuracy versus 3B+ robustness; Q4_K_M stays clean at >=1B params. Exposes semantic dissociation risks in ultra-low-bit deployment.

### 2026-10-02
* `token-pruning` `efficient-inference` `MLLM` [From Patching to Pruning Visual Computation in Vision Language Models](http://arxiv.org/abs/2610.03389v1)
  > **TL;DR**: Prunes visual computation in VLMs via activation patching without token removal, reduces 55% FLOPs at 3% accuracy drop (94% retained), showing non-uniform visual processing across layers.
* `quantization` `efficient-inference` [VisionMX: Unlocking Microscaling Post-Training Quantization for Vision Models](http://arxiv.org/abs/2610.03218v1)
  > **TL;DR**: Explores microscaling (MX) post-training quantization for vision models, identifying error sources and proposing optimizations (bounded weight rounding, foldable affine correction). Handles MX formats, achieving performance recovery in MX-sensitive architectures.
* `quantization` `efficient-inference` `MLLM` [CHASE-VLA: Post-Training Quantization Framework for Vision-Language-Action Models with Chunk-Aware Scale Estimation](http://arxiv.org/abs/2610.02666v1)
  > **TL;DR**: PTQ for VLA models via chunk-aware scale estimation, enabling W4A4 quantization of MLP & attention layers, restoring FP16 performance with 73.4% weight storage reduction and 70.9% memory traffic savings on π0.5.
* `efficient-inference` `compression` `token-pruning` [SpectralCache: Accelerating Diffusion-Based World Models via Spectral Feature Caching](http://arxiv.org/abs/2610.02660v1)
  > **TL;DR**: Reduces diffusion model inference overhead via spectral feature caching by reusing stable singular subspaces and skipping backbone evaluations, achieving 5.22x speedup on HunyuanWorld-Voyager-13B.
* `compression` `efficient-inference` `quantization` [Preserving Mathematical Reasoning in Compressed Diffusion Language Models via Trajectory-Aware Low-Rank Approximation](http://arxiv.org/abs/2610.03326v1)
  > **TL;DR**: Preserves mathematical reasoning in compressed diffusion LLMs via trajectory-aware low-rank approximation. Proposes Traj-MC for efficient calibration, improving reconstruction and reasoning under compression. Achieves better reasoning preservation than clean calibration on benchmarks.
* `compression` `efficient-inference` [KV$^2$: A Self-Refining KV Cache](http://arxiv.org/abs/2610.03198v1)
  > **TL;DR**: Compresses KV cache in long-context models by selective token reconstruction, achieving 40% better score at 2% cache budget with lower runtime and memory.
* `quantization` `compression` `efficient-inference` [Tailoring the Quantization Space for 1-Bit KV Cache Compression](http://arxiv.org/abs/2610.03027v1)
  > **TL;DR**: 1-bit KV cache compression via query-guided and covariance-aware vector quantization (TaSQ), enabling 14x larger batch size and 1.87x higher throughput vs. BF16 baseline.
* `compression` `efficient-inference` `MLLM` [Dynamic Expert Pruning for Multi-Agent Systems](http://arxiv.org/abs/2610.02951v1)
  > **TL;DR**: Dynamic expert pruning for Mixture-of-Experts models in multi-agent systems, using per-request masks from lightweight predictors, avoids static pruning inefficiencies, enabling sparser and more efficient serving without retraining, while maintaining accuracy.
* `compression` `efficient-inference` [DyRA: Dynamic Residual Approximation for Efficient Matrix Multiplication in DNNs](http://arxiv.org/abs/2610.02882v1)
  > **TL;DR**: Problem: High cost of dense matrix multiplication in DNNs. Method: Dynamic residual approximation (DyRA) for output-aware structured matrix approximation. Result: 1.5× GPU speedup for DINOv3 with 3× less accuracy drop vs baselines.
* `compression` `efficient-inference` [iS-KV: Online Low-Rank KV Cache Compression via Block-Incremental SVD](http://arxiv.org/abs/2610.02815v1)
  > **TL;DR**: Reduces KV-cache memory via online low-rank compression (block-incremental SVD), achieving 82.6% accuracy at 4.06x compression on DeepSeek-R1-Distill-Llama-8B.
* `quantization` `efficient-inference` `MLLM` [BitNest: Bit-Nested Speculative Decoding for Memory-Efficient LLM Inference Acceleration](http://arxiv.org/abs/2610.02800v1)
  > **TL;DR**: Memory-efficient LLM inference by embedding low-precision draft directly into higher-precision target via bit-nested speculative decoding, achieving 1.48--1.61x speedup over FP16 decoding with 95.2% acceptance rate.
* `quantization` `efficient-inference` [16-bit Precision of Convolutional Neural Networks on Microcontroller Units for 8-bit Costs](http://arxiv.org/abs/2610.03402v1)
  > **TL;DR**: Efficient 16-bit quantization (W16A16) for MCUs matches 8-bit costs in speed/energy while reducing quantization errors 10x, validated on Armv7E-M.
* `token-pruning` `efficient-inference` `MLLM` [From Patching to Pruning Visual Computation in Vision Language Models](http://arxiv.org/abs/2610.03389v1)
  > **TL;DR**: Proposes Patch-to-Prune (P2P) for efficient VLMs by bypassing unnecessary visual token computations without modifying weights or removing tokens. Maintains 94% accuracy at 3% tolerance while reducing FLOPs by 55%.
* `compression` `efficient-inference` [Exploring the Trade-Off Between Structured Pruning and Fault Tolerance in Deep Neural Networks for Space Applications](http://arxiv.org/abs/2610.03117v1)
  > **TL;DR**: Investigates structured pruning impact on model robustness to bit-flips for space applications; shows shorter execution time offsets increased fault sensitivity, enabling energy/latency savings.
* `quantization` `compression` `efficient-inference` [Tailoring the Quantization Space for 1-Bit KV Cache Compression](http://arxiv.org/abs/2610.03027v1)
  > **TL;DR**: Efficient 1-bit KV cache compression for LLMs via query-guided vector quantization (TaSQ), achieving 1.87× throughput gain and 14× batch size increase over BF16 baseline.
* `token-pruning` `compression` `efficient-inference` [SlimKV: Joint Token-Feature KV Cache Compression with Reconstruction-Free Beacon Attention](http://arxiv.org/abs/2610.02953v1)
  > **TL;DR**: Compresses KV-cache memory in LLMs via joint token-feature compression with beacon attention, achieving 16x/32x compression with 96% accuracy retention and up to 3.38x decoding speedup at 128K length.
* `compression` `efficient-inference` `token-pruning` [Dynamic Expert Pruning for Multi-Agent Systems](http://arxiv.org/abs/2610.02951v1)
  > **TL;DR**: Memory-inefficient MoE models due to resident experts. Dynamic Expert Pruning (DEP) uses prompts to generate per-request masks, reducing footprint. Achieves higher accuracy than static pruning, especially when few experts are retained.
* `compression` `quantization` `efficient-inference` [DyRA: Dynamic Residual Approximation for Efficient Matrix Multiplication in DNNs](http://arxiv.org/abs/2610.02882v1)
  > **TL;DR**: Efficient matrix multiplication via dynamic residual approximation and low-rank output error correction, reducing GPU inference time 1.5× for DINOv3 with 3× less accuracy drop.

### 2026-10-01
* `token-pruning` `efficient-inference` [Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens](http://arxiv.org/abs/2610.01939v1)
  > **TL;DR**: Reducing token overhead in VLM robot agents; feedback-driven selective observation reduces LLM calls by 49% and tokens by 65% with improved success rate (63.1% to 71.7%).
* `token-pruning` `efficient-inference` `MLLM` [VETO: Video Efficient Token Optimization for Vision Language Models](http://arxiv.org/abs/2610.01785v1)
  > **TL;DR**: Reduces visual token redundancy in VLMs via dual-axis compression (spatial merging + temporal redundancy pruning) with a training-optional plugin, achieving 45% faster inference and 55.7% accuracy at 10% token budget.
* `compression` `efficient-inference` `MLLM` [MWOP: Modality-aware Width-wise Operation Pruning for Efficient MLLMs](http://arxiv.org/abs/2610.01434v1)
  > **TL;DR**: Efficient MLLM inference via modality-aware operation pruning (V2V, T2V, T2T paths and FFN channels). Achieves 1.6x prefill speedup on LLaVA-7B with 99.7% performance retention.
* `quantization` `efficient-inference` [Joint Branch-Space Transform Coding for Diffusion Activation Quantization with Classifier-Free Guidance](http://arxiv.org/abs/2610.00930v1)
  > **TL;DR**: Improves diffusion model activation quantization by exploiting CFG branch correlations via branch-space transform coding (GCBT), enabling fixed-bit PTQ with statistically significant fidelity gains.
* `token-pruning` `efficient-inference` `MLLM` [VETO: Video Efficient Token Optimization for Vision Language Models](http://arxiv.org/abs/2610.01785v1)
  > **TL;DR**: Addresses quadratic visual token cost in VLMs via dual-axis token compression (intra-frame merging + inter-frame redundancy reduction), achieving 45% faster inference and 55.7% accuracy under 10% token budget.
* `token-pruning` `efficient-inference` `compression` [TopK-Guided: Adaptive, Budget-Aware Activation Sparsity for Efficient LLM Inference](http://arxiv.org/abs/2610.01763v1)
  > **TL;DR**: Efficient LLM inference via adaptive sparsity, combining token-level budget control with block-level sensitivity for improved accuracy over TEAL/WINA at high sparsity.
* `compression` `efficient-inference` `MLLM` [MWOP: Modality-aware Width-wise Operation Pruning for Efficient MLLMs](http://arxiv.org/abs/2610.01434v1)
  > **TL;DR**: Proposes MWOP for pruning modality-aware attention paths and FFN channels in MLLMs, achieving 1.6x prefill speedup with 99.7% performance retention on LLaVA-OneVision-7B.
* `compression` `token-pruning` `efficient-inference` [ITC-MoE: Importance-guided Token-aware Compression for MoE Diffusion Language Models](http://arxiv.org/abs/2610.01296v1)
  > **TL;DR**: Compresses MoE diffusion models via importance-guided token-aware low-rank factorization and routing adaptation, achieving 30% compression and 7.22x speedup while maintaining 96.33% accuracy.
* `efficient-inference` `token-pruning` [HHR: Hierarchical Hash Retrieval for Efficient LLM Generation](http://arxiv.org/abs/2610.01230v1)
  > **TL;DR**: Addresses efficient long-context inference in LLMs via hierarchical hash retrieval to reduce false positives/negatives, achieving up to 3.3x decoding speedup for Llama-3.1-8B at 128K context length.
* `quantization` `efficient-inference` [The Devil Is in the Reconstruction Loss Scale: Rethinking Optimization in LLM Quantization](http://arxiv.org/abs/2610.00983v1)
  > **TL;DR**: Analyzes optimization imbalance in LLM PTQ due to MSE loss scale, proposes RMSE variants for gradient normalization, achieving better INT4 quantization via stage-decoupled optimization.
* `efficient-inference` `compression` [Decoding Looped Transformers Better for (Almost) Free](http://arxiv.org/abs/2610.02185v1)
  > **TL;DR**: Improves decoding efficiency in looped Transformers via contrastive decoding (LoopCD), reducing FLOPs by 22.5-48.2% while maintaining performance.
* `compression` `efficient-inference` [LAST: Looped Audio Spectrogram Transformer](http://arxiv.org/abs/2610.01926v1)
  > **TL;DR**: Reduces transformer computational cost by reusing blocks to refine class token, cutting 49.4% parameters and 42% FLOPs while improving AudioSet mAP by 2.1%.
* `quantization` `efficient-inference` [Stochastic Rounding in Low-Precision Transformer Inference: A Variable-Precision Emulation Study of a Small GPT-2](http://arxiv.org/abs/2610.01889v1)
  > **TL;DR**: Compares stochastic vs. nearest rounding for low-precision transformer inference, finding MLPs favor stochastic rounding (1.15x perplexity at 6-bit) while heads prefer nearest, achieving 1.10x perplexity in mixed-precision.
* `compression` `efficient-inference` [CrossGMN: Graph Metanetworks for Cross-Architecture Weight-Space Transformations](http://arxiv.org/abs/2610.01649v1)
  > **TL;DR**: Focuses on model compression via cross-architecture weight-space transformations. Key method: CrossGMN, a graph metanetwork for equivariant weight transformations. Results: speeds up distillation by up to 8.89x and transfers across datasets without retraining (3.78x).
* `compression` `efficient-inference` `quantization` [QK-Wanda: Coupling Queries and Keys for Unstructured Pruning](http://arxiv.org/abs/2610.01554v1)
  > **TL;DR**: Couples query-key weights for unstructured pruning, reducing reconstruction error by 60% at 50% sparsity and 45% at 80%, while increasing zero-shot accuracy by 5.94 percentage points at 80% sparsity on Llama 2 70B.
* `quantization` `compression` `efficient-inference` [FedFit: Federated Fine-Tuning of LLMs via Vector-Bank Parameterization and Quantization](http://arxiv.org/abs/2610.01537v1)
  > **TL;DR**: FedFit reduces federated LLM fine-tuning communication overhead via vector-bank parameterization and quantization, achieving 100x higher compression ratios than standard federated LoRA while maintaining perplexity.

### 2026-09-29
* `compression` `efficient-inference` [TSGL: Teacher-Student Graph Learning for 3DGS Compression](http://arxiv.org/abs/2609.38635v1)
  > **TL;DR**: Compresses 3DGS models by 27x-33x using Teacher-Student Graph Learning and Graph Fourier Transform, reducing file sizes with <0.6dB PSNR loss.
* `efficient-inference` `token-pruning` `compression` [$S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient](http://arxiv.org/abs/2609.37976v1)
  > **TL;DR**: Proposes $S^3$ to improve reasoning efficiency in LLMs by leveraging null-space components, reducing token overhead by 27.4% while increasing accuracy by 1.0pp.
* `token-pruning` `efficient-inference` `MLLM` [TReVS: Integrating Textual Relevance and Visual Saliency for Efficient Vision-Language Model Token Pruning](http://arxiv.org/abs/2609.37581v1)
  > **TL;DR**: Efficient visual token pruning via text-visual joint saliency and high-variance attention, pruning 94.4% tokens while retaining 92.8% performance in LLaVA-1.5-7B.
* `token-pruning` `efficient-inference` `MLLM` [ResComEmb: Effective and Efficient Multimodal Embedding via Residual Homogeneity Compression](http://arxiv.org/abs/2609.37225v1)
  > **TL;DR**: Problem: High storage and interaction costs from long visual token sequences in MLLMs. Solution: Residual Homogeneity Compression (RHC) module under visual token budgets. Result: Outperforms ColQwen2.5 in document retrieval using only 37.5% visual tokens.
* `token-pruning` `efficient-inference` `MLLM` [EviViT: Evidence-Adaptive Vision Transformers for Fine-Grained Perception](http://arxiv.org/abs/2609.37123v1)
  > **TL;DR**: Reduces visual tokens via evidence-adaptive token allocation for fine-grained perception in ViTs, achieving higher accuracy with fewer tokens than global-only processing.
* `quantization` `compression` `MLLM` [Task-Oriented Visual Feature Compression via Residual Vector Quantization for Device-Edge Multimodal Inference](http://arxiv.org/abs/2609.37090v1)
  > **TL;DR**: Reduces visual payload by 53.6% for device-edge LMM inference via query-guided feature aggregation and residual vector quantization.
* `token-pruning` `efficient-inference` `MLLM` [OmniRoute: Mapping Temporal Semantic Evidence to Audio-Visual Token Budgets for Efficient Omnimodal Large Language Models](http://arxiv.org/abs/2609.37052v1)
  > **TL;DR**: Proposes OmniRoute for token-level compression in audio-visual LLMs, dynamically adjusting token budgets based on temporal semantic relevance. Reduces prefill latency with training-free token selection and merging, achieving better efficiency-performance trade-off on 4 benchmarks.
* `token-pruning` `efficient-inference` `MLLM` [GleanVID: Complementary Token Selection for Efficient Video Large Language Models](http://arxiv.org/abs/2609.37042v1)
  > **TL;DR**: Efficient VideoLLMs via complementary token selection. GleanVID selects tokens across frames to preserve informative & complementary evidence within a 25% token budget, reducing prefill latency by 44.7% while retaining 98.6% of Qwen3-VL's performance.
* `compression` `efficient-inference` `token-pruning` [UltraMatch: Transport Path Routing for Ultra-Fast and Memory-Efficient Image Matching](http://arxiv.org/abs/2609.36980v1)
  > **TL;DR**: Dense token-level matching is expensive. UltraMatch routes only a few paths, uses sparse Dual-Softmax and tiny fine matching head. 1.67x faster than SuperPoint+LightGlue, 0.44 GiB memory, scales to 6K resolution.
* `quantization` `efficient-inference` [Chinese-Jev: Bringing System One Model to Chinese-Language Tasks](http://arxiv.org/abs/2609.36965v1)
  > **TL;DR**: INT8-quantized Chinese-Jev model achieves 1.0s latency per decision on mobile devices, offering 20.3x speedup over baseline while maintaining accuracy.
* `token-pruning` `efficient-inference` `MLLM` [Representation Dynamics Reveal Semantic Saliency and Similarity for Visual Token Pruning in MLLMs](http://arxiv.org/abs/2609.36916v2)
  > **TL;DR**: Reduces MLLM inference latency via visual token pruning using layer-dependent update magnitudes & direction similarities, preserving 91.9% performance with 5.6% tokens and 7.8x speedup.
* `compression` `efficient-inference` [Does the VGGT Family Need All Its Layers?](http://arxiv.org/abs/2609.36842v1)
  > **TL;DR**: Identifies redundant layers in VGGT models with structured pruning, reducing parameters by 44% without accuracy drop, using layer degradation analysis and linear calibration.
* `compression` `token-pruning` `efficient-inference` [NesTok: Nested Self-Aligned 1D Tokenizer for Autoregressive Image Generation](http://arxiv.org/abs/2609.36756v2)
  > **TL;DR**: NesTok introduces cross-length training for 1D variable-length visual tokenizers, improving reconstruction and generation efficiency. Achieves rFID 0.98 on ImageNet.
* `token-pruning` `efficient-inference` `MLLM` [FocusVTC: Efficient and High-Performance Visual Text Compression with Adaptive Resolution](http://arxiv.org/abs/2609.36651v1)
  > **TL;DR**: Efficient visual text compression via adaptive resolution and selective region enhancement. Achieves 2.9x input compression (72 DPI) with 87.4 score vs. 57.5 for baseline.
* `quantization` `compression` `efficient-inference` [ShamAN-Q: Shampoo Augmented NanoQuant for Sub-1-bit LLM Weights](http://arxiv.org/abs/2609.38521v1)
  > **TL;DR**: Sub-1-bit post-training quantization (PTQ) method (0.8-1 bpw) for LLMs using curvature-aware reconstruction with Fisher information, improving WikiText-2 perplexity from 27.56 to 22.96 at 1 bpw (0.6B model).
* `quantization` `compression` `efficient-inference` [Security-Enhanced Seed-Based Weight Quantization for Large Language Models](http://arxiv.org/abs/2609.38477v1)
  > **TL;DR**: Security-enhanced seed-based weight quantization for LLMs with non-uniform bit allocation (down to 4-bit), achieving better perplexity than SeedLM at same bit-rate while providing security benefits against bit-flip attacks.
* `quantization` `efficient-inference` `MLLM` [STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization](http://arxiv.org/abs/2609.38169v1)
  > **TL;DR**: Addresses memory bottleneck in linear attention's recurrent states via spatial-temporal PTQ (STEPQuant), allocating precision by error magnitude and memory lifetime. Achieves FP32 accuracy with 6-bit and outperforms INT8 with 4-bit, reducing serving memory by 68.7%.
* `quantization` `efficient-inference` [LeapQuant: Efficient Linear Attention with Accurate Recurrent State Quantization](http://arxiv.org/abs/2609.38166v1)
  > **TL;DR**: Solves error accumulation & outliers in 8-bit recurrent state quantization for LLM linear attention via per-window quantization & compensator tokens, achieving 2.05-3.7x kernel speedups with FP32 accuracy.
* `token-pruning` `compression` `efficient-inference` [KV-Kaizen: Learning Context-Adaptive Cache Compression Choices](http://arxiv.org/abs/2609.37988v2)
  > **TL;DR**: Proposes KV-Kaizen for LLM KV cache compression via adaptive depth, precision (fewer bits), and rank reduction. Achieves 32x smaller cache on 14B model with no accuracy loss.
* `efficient-inference` `compression` [$S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient](http://arxiv.org/abs/2609.37976v1)
  > **TL;DR**: Reduces token cost in reasoning LLMs by null-space optimization, achieving 27.4% fewer tokens and +1.0% accuracy.
* `compression` `efficient-inference` `MLLM` [DIET: Deletion-response Expert Trimming for Video Diffusion Transformers](http://arxiv.org/abs/2609.37829v1)
  > **TL;DR**: Prunes 50% MoE experts in video diffusion transformers via deletion-response signatures, reducing model size from 57GB to 30GB while improving VBench score (0.7941 to 0.8115) without fine-tuning.
* `token-pruning` `efficient-inference` `MLLM` [FOCUS: Training-Free Decision-Preserving Context Compression for LLM Agents](http://arxiv.org/abs/2609.37590v1)
  > **TL;DR**: Problem: quadratic inference cost from growing LLM agent histories. Method: training-free causal decision-preserving context compression. Result: 48% context reduction, 73% dependency cut, and 8.9% task success improvement.
* `token-pruning` `efficient-inference` `MLLM` [TReVS: Integrating Textual Relevance and Visual Saliency for Efficient Vision-Language Model Token Pruning](http://arxiv.org/abs/2609.37581v1)
  > **TL;DR**: Efficient visual token pruning in VLMs by integrating text relevance with visual saliency and high-variance attention heads, achieving 92.8% performance retention with 94.4% tokens pruned.
* `compression` `efficient-inference` `token-pruning` [Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings](http://arxiv.org/abs/2609.37272v1)
  > **TL;DR**: Improves token merging by preserving task-relevant null-space residuals, achieving +31.51 mIoU under strong compression.
* `token-pruning` `efficient-inference` `MLLM` [ResComEmb: Effective and Efficient Multimodal Embedding via Residual Homogeneity Compression](http://arxiv.org/abs/2609.37225v1)
  > **TL;DR**: Addresses visual token redundancy in MLLMs via Residual Homogeneity Compression, reducing token budget by 62.5% while improving retrieval performance.
* `compression` `efficient-inference` `MLLM` [IronLLM: Forging Compact Edge-Native Language Models for Real-Time Embodied Intelligence](http://arxiv.org/abs/2609.36860v1)
  > **TL;DR**: Efficient on-device LLM with 654M params, using hybrid attention and lightweight KV-cache design for 1.48x decoding speedup, optimized for low-latency with simplified components.
* `compression` `efficient-inference` `MLLM` [ARC-KV: Amortizing Anchor Search for Reconstruction-Based KV Cache Compaction](http://arxiv.org/abs/2609.36835v1)
  > **TL;DR**: KV cache compression for LLMs. ARC-KV amortizes anchor selection via a learned indexer, enabling reusable context-specific compaction. At 10% KV retention, improves accuracy by 0.0065 and reduces compaction time 25x vs baseline (37.3s vs 959.8s).
* `quantization` `MLLM` `efficient-inference` [Calibrate the Decisions That Change the Future: On-Policy Post-Training Quantization for Multimodal Large Language Models](http://arxiv.org/abs/2609.36828v1)
  > **TL;DR**: Proposes OnPTQ for MLLMs, combining decision-consequence risk for autoregressive-aware PTQ, improving downstream performance in low-bit settings (specific bit-widths not stated) with fewer correctness flips versus FP16.
* `token-pruning` `efficient-inference` [Aperture: Merge-Consistent Rotary States for Compressed Tokens](http://arxiv.org/abs/2609.36781v1)
  > **TL;DR**: Proposes Aperture for merge-consistent rotary states in token compression, addressing positional information loss during merging. Achieves 65.63% accuracy in video QA vs 67.12% for baseline merging.
* `token-pruning` `compression` `efficient-inference` [NesTok: Nested Self-Aligned 1D Tokenizer for Autoregressive Image Generation](http://arxiv.org/abs/2609.36756v2)
  > **TL;DR**: Dynamic visual tokenizer with cross-length training for adaptive compression, improves rFID to 0.98 on ImageNet, enabling flexible trade-offs between quality and computational cost.
* `token-pruning` `efficient-inference` `MLLM` [FocusVTC: Efficient and High-Performance Visual Text Compression with Adaptive Resolution](http://arxiv.org/abs/2609.36651v1)
  > **TL;DR**: Efficient visual text compression via adaptive resolution, combining low-DPI global views with selective enhancement, achieving 2.9x input compression and 2.79x speedup while improving performance.
* `quantization` `efficient-inference` `MLLM` [Bits Under ZK-LLM: Evaluating Zero-Knowledge-Friendly Quantization for Verifiable Private LLM Inference](http://arxiv.org/abs/2609.36437v1)
  > **TL;DR**: Evaluates ZK-friendly quantization for private LLM inference, analyzing weight/activation precision and nonlinear lookup tables. Identifies RMSNorm as a bottleneck and shows operator-aware precision selection improves efficiency. Achieves near-baseline utility with selective precision increase.
* `quantization` `compression` `efficient-inference` [JARQ: Joint Alternating Refinement for Quantization](http://arxiv.org/abs/2609.38599v1)
  > **TL;DR**: Improves group-wise post-training quantization in LLMs by alternating joint scale refinement and code adjustments, maintaining bit-width. Cuts 3-bit RTN perplexity by up to 36%.
* `quantization` `compression` `efficient-inference` [ShamAN-Q: Shampoo Augmented NanoQuant for Sub-1-bit LLM Weights](http://arxiv.org/abs/2609.38521v1)
  > **TL;DR**: ShamAN-Q introduces sub-1-bit PTQ for LLMs using dense curvature metrics via Shampoo optimizer, achieving 0.8–1 bpw with improved perplexity (e.g., 14.29 to 13.80 on Qwen3-Base 4B) and matching/exceeding prior quantization methods.
* `quantization` `compression` `efficient-inference` [Security-Enhanced Seed-Based Weight Quantization for Large Language Models](http://arxiv.org/abs/2609.38477v1)
  > **TL;DR**: Non-uniform weight sensitivity-aware seed-based compression for LLMs with deterministic bit-allocation (4-bit/weight), matching SeedLM perplexity with fewer bits and reducing accuracy loss, implemented in ASIC with minimal overhead.
* `quantization` `efficient-inference` `MLLM` [STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization](http://arxiv.org/abs/2609.38169v1)
  > **TL;DR**: Quantizes Delta-rule recurrent states via spatial-temporal precision allocation, reducing serving memory by 68.7% at 6-bit while matching FP32 accuracy, and outperforms INT8 at 4-bit.
* `quantization` `efficient-inference` `MLLM` [LeapQuant: Efficient Linear Attention with Accurate Recurrent State Quantization](http://arxiv.org/abs/2609.38166v1)
  > **TL;DR**: Efficient 8-bit quantization of recurrent state in linear attention LLMs via per-window quantization with high-precision compensator tokens, achieving 1.47× end-to-end speedup with FP32 accuracy.
* `quantization` `efficient-inference` `MLLM` [WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms](http://arxiv.org/abs/2609.38121v1)
  > **TL;DR**: KV cache quantization bottleneck addressed via data-adaptive WUSH-KV with calibrated transforms, achieving near-optimal INT2 quantizer performance (2-bit) with lowest perplexity, outperforming OSCAR transform.
* `compression` `efficient-inference` `quantization` [Mira: Memory-Efficient MoE Inference Using Adaptive Caching and Predictive Expert Staging](http://arxiv.org/abs/2609.38090v1)
  > **TL;DR**: Memory-efficient MoE inference via predictive expert staging and tailored quantization, achieving 5.71x speedup on GPU with optimized cache and compression.
* `efficient-inference` `token-pruning` `MLLM` [$S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient](http://arxiv.org/abs/2609.37976v1)
  > **TL;DR**: Proposes $S^3$ to reduce LLM token cost by operating in null-space, achieving 27.4% token reduction and +1.0% accuracy on reasoning tasks.
* `quantization` `compression` `efficient-inference` [Behavioral Capacity Certificates for Quantized Language Models](http://arxiv.org/abs/2609.37887v1)
  > **TL;DR**: Proposes Behavioral Capacity Certificates (BCC) for quantized language models, enabling efficient bit-width selection (mixed-precision) and weight pruning/sparsity while preserving model behavior. Achieves lower NLL and higher prediction agreement on GPT-2 and other models at equal cache memory.
* `token-pruning` `efficient-inference` [Retrieval Capacity of Self-Attention Under Competition](http://arxiv.org/abs/2609.37879v1)
  > **TL;DR**: Studies effective token pruning in language models via self-attention, keeping only top-attention tokens. Achieves close to full-attention NLL with small token sets, outperforming random selection.
* `quantization` `efficient-inference` [Delta-Matching: Closing the Final Gap of Native 8-bit Training for LLMs](http://arxiv.org/abs/2609.37852v1)
  > **TL;DR**: Enables fully native 8-bit FP8 LLM training via Delta-Matching, mitigating optimization errors in attention-core matmuls, matching BF16/FP32 performance across scales.
* `quantization` `efficient-inference` [Scale Sensitivity in Low-Bit Post-Training Quantization: Curvature of the Quantization Error Landscape](http://arxiv.org/abs/2609.37416v1)
  > **TL;DR**: Analyzes scale sensitivity in PTQ via Gaussian weight analysis, proving curvature decay with bit-width. Validated on GPTQ for LLMs, showing strong sensitivity at 2-3 bits and Hadamard processing matching optimal scale at ≥3 bits.
* `compression` `efficient-inference` [vSkipper: Translating Dynamic Layer Skipping into LLM Serving Gains](http://arxiv.org/abs/2609.37062v1)
  > **TL;DR**: Dynamic layer skipping in LLM serving reduces computation but lacks efficient integration with modern engines. vSkipper virtualizes skipping to preserve serving features, achieving 36.8% lower latency on GSM8K and 11.3% higher throughput under saturation without quality loss, using FlexiDepth's 8/32 layer skipping.
* `token-pruning` `efficient-inference` `MLLM` [GleanVID: Complementary Token Selection for Efficient Video Large Language Models](http://arxiv.org/abs/2609.37042v1)
  > **TL;DR**: Reduces VideoLLM inference overhead via complementary token selection, preserving 98.6% Qwen3-VL performance with 25% tokens and cutting prefill latency by 44.7%.
* `quantization` `efficient-inference` `compression` [QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching](http://arxiv.org/abs/2609.36760v2)
  > **TL;DR**: Proposes QuantMLA for INT4/INT2 KV cache quantization in Multi-Head Latent Attention, with path-specific error analysis and function-aligned transformations. Achieves 3.59x cache compression at 128K context with minimal accuracy drop.
* `quantization` `efficient-inference` `MLLM` [Replay the Curvature: Accurate and Scalable NVFP4 Quantization for Large Language Model Inference](http://arxiv.org/abs/2609.36654v1)
  > **TL;DR**: Proposes NVFP4 (4-bit) quantization for LLMs with Schur Replay scale-selection to reduce weight storage and memory traffic, achieving up to 100.84% BF16 accuracy recovery on 397B model with 15.17x speedup.

### 2026-09-28
* `compression` `efficient-inference` `token-pruning` [ReSS: Residual-Restoring Sparse Attention for 3D Vision Transformers](http://arxiv.org/abs/2609.35593v1)
  > **TL;DR**: Problem: high computation in 3D vision transformers due to global attention. Method: residual-restoring sparse attention (ReSS) by minimizing drift in residual stream. Result: preserves dense performance better than prior methods at up to 70% sparsity.
* `quantization` `token-pruning` `efficient-inference` [EdgeVLN: Runtime-Aware Deployment Ready Quantized Vision Language Navigation Model](http://arxiv.org/abs/2609.35570v1)
  > **TL;DR**: Proposes EdgeVLN, a quantized VLN model with 4-bit weight quantization and memory-token pruning, achieving 58.02% success rate on R2R VLN-CE with 11.35GB memory usage and 13.3x energy reduction on Jetson Orin.
* `token-pruning` `efficient-inference` `MLLM` [Rethinking Visual Token Compression for Video Large Language Models: A Simple Yet Strong Baseline](http://arxiv.org/abs/2609.35394v1)
  > **TL;DR**: Video LLM visual token compression problem addressed by SimpleCluster, a training-free position-aware cross-frame clustering method. Achieves competitive performance at low retention rates (e.g., 1%) by preserving feature-space structure.
* `token-pruning` `compression` `efficient-inference` [Beyond Selection: Token Parameterization for Extreme Visual Token Compression](http://arxiv.org/abs/2609.35232v1)
  > **TL;DR**: Extreme visual token compression via basis transformation and structured truncation. Braco method achieves 23x-144x compression with 95.2% accuracy and 84.2%-86.7% FLOPs reduction.
* `efficient-inference` `token-pruning` `MLLM` [Still There, No Longer Seen: Exposing Compression-Induced Risk in Large Vision-Language Models](http://arxiv.org/abs/2609.35002v1)
  > **TL;DR**: Analyzes compression-induced adversarial failures in LVLMs, proposes CIRA attack (20.35% CSFR) targeting token compression, and evaluates defenses for visual token pruning.
* `token-pruning` `efficient-inference` `MLLM` [SPIDER: Multi-Layer Semantic Token Pruning and Adaptive Sub-Layer Skipping in Multimodal Large Language Models](http://arxiv.org/abs/2609.34977v1)
  > **TL;DR**: Reduces data and computational redundancy in MLLMs via multi-layer semantic visual token pruning and adaptive sub-layer skipping, achieving 79% FLOPs reduction while retaining 96% performance on LLaVA-NeXT-7B.
* `token-pruning` `efficient-inference` `MLLM` [Just MLPs: Efficient Visual State Reconstruction for Multimodal Language Models](http://arxiv.org/abs/2609.34972v1)
  > **TL;DR**: Reduces MLLM computational cost by replacing Transformer evolution of visual tokens with lightweight low-rank adapters, preserving all tokens while achieving higher accuracy than pruning baselines at comparable/lower compute.
* `token-pruning` `efficient-inference` `MLLM` [Resolution as a First-Class Decision: Task-Conditioned Routing for Efficient Multimodal Large Language Models](http://arxiv.org/abs/2609.34942v1)
  > **TL;DR**: Addresses MLLM inefficiency from high-resolution visual tokens via task-conditioned routing, reducing FLOPs by 40.9% and latency by 53.7% while maintaining performance.
* `quantization` `efficient-inference` `MLLM` [SubRot: Signed Gradient Subspace Calibration for VLM Rotation Quantization](http://arxiv.org/abs/2609.34884v1)
  > **TL;DR**: Proposes SubRot for VLM rotation quantization via signed gradient subspace calibration, achieving 1.4pp improvement over FlatQuant at W4A6/4, with <1.4pp drop vs FP16 at W4A4.
* `quantization` `token-pruning` `MLLM` [P4Q: Co-designing Token Pruning and Quantization for Vision-Language Model Acceleration](http://arxiv.org/abs/2609.34867v1)
  > **TL;DR**: Co-designed token pruning and quantization to accelerate VLMs, combining quantization-aware token selection and pruning-aware quantization calibration for 2.8x speedup while maintaining accuracy on LLaVA-NeXT.
* `token-pruning` `efficient-inference` `MLLM` [When Text Matters: Design Principles for Visual Token Pruning in Vision-Language Model](http://arxiv.org/abs/2609.34861v1)
  > **TL;DR**: Improves visual token pruning in VLMs by separating vision-guided pruning from deferred text-guided reselection, achieving 11.10-16.84% better performance recovery at 80-90% pruning with comparable latency.
* `token-pruning` `efficient-inference` `MLLM` [From Perception to Integration: Revisiting the Internal Dynamics of Reasoning in Vision-Language Models](http://arxiv.org/abs/2609.34809v1)
  > **TL;DR**: Reduces reasoning tokens in VLMs by 79.1% via early stopping with a readiness detector, improving accuracy by 3.13 points.
* `quantization` `MLLM` `efficient-inference` [Beyond Reconstruction Loss in Post-Training Quantization: Balanced Fitting for Large Vision-Language Models](http://arxiv.org/abs/2609.34765v1)
  > **TL;DR**: Proposes Balanced Fitting for PTQ in LVLMs, balancing precision and regularization via layer-/component-wise quantization effects. Achieves better downstream performance than prior methods under weight-only and weight-activation quantization.
* `quantization` `efficient-inference` `compression` [GLF-Q: Global-Local Feature-based Quantization for Vision Transformers](http://arxiv.org/abs/2609.34564v1)
  > **TL;DR**: Addresses low-bit PTQ accuracy drop in ViTs via Global-Local Feature alignment and offline Hadamard transforms. Achieves SOTA at 3-bit, improving classification and maintaining robustness, with 8-bit GPU speedups.
* `token-pruning` `efficient-inference` `MLLM` [ACPruner: Visual Token Pruning as Biased Attention Coverage Maximization in LVLMs](http://arxiv.org/abs/2609.34558v1)
  > **TL;DR**: Visual token pruning for efficient LVLM inference via biased attention coverage maximization, achieving strong performance with 30-50% token removal and substantial speedups in models like LLaVA-7B/13B.
* `token-pruning` `efficient-inference` `MLLM` [MiCo: Mutual Information Coverage Optimization through Semantic Erasure Modeling for Efficient MLLM Inference](http://arxiv.org/abs/2609.34330v1)
  > **TL;DR**: Token pruning for efficient MLLM inference via mutual information coverage optimization. Semantic erasure model & greedy submodular coverage optimization. Retains 97.5% performance with 5.6% visual tokens & 3.8x speedup on LLaVA-NEXT-13B.
* `token-pruning` `efficient-inference` `compression` [DORA: Dynamic Online Reinforcement Agent for Token Pruning in Vision Transformers](http://arxiv.org/abs/2609.34325v1)
  > **TL;DR**: Online token pruning via reinforcement learning for ViTs, dynamically pruning input-adaptive tokens with FlashAttention, reducing FLOPs by 38.4% on DeiT-Base at <1% accuracy drop.
* `token-pruning` `efficient-inference` `MLLM` [Text-Vision Synergistic Token Caching: A Training-Free Framework for Efficient Vision-Language-Action Inference](http://arxiv.org/abs/2609.34319v1)
  > **TL;DR**: Efficient vision-language-action inference via text-vision synergistic token caching, improving task success by 14.5% at 12.5% retention while reducing FLOPs by 2.45x.
* `token-pruning` `MLLM` `efficient-inference` [SCOPD: Sparse-Context On-Policy Self-Distillation for Efficient Vision-Language Models](http://arxiv.org/abs/2609.34044v1)
  > **TL;DR**: Improves performance of VLMs with token pruning (10% retention) via sparse-context self-distillation, raising accuracy from 86.37% to 92.43%.
* `quantization` `efficient-inference` `MLLM` [IMC-CLINIC: Coupled Loss-Informed Newton Iterations for Clipping in Analog In-Memory Computing](http://arxiv.org/abs/2609.35586v1)
  > **TL;DR**: Optimizing clipping in analog IMC for LLMs to jointly handle operand and ADC quantization errors, improving accuracy by 6.5-11.5 points over baselines while cutting calibration time 10-12x.
* `quantization` `compression` `efficient-inference` [The Hidden Ratio in Adam: Stable Structure, Compression, and Sign Dynamics](http://arxiv.org/abs/2609.35392v1)
  > **TL;DR**: Efficient Adam optimization via a transformed ratio with stable distribution. Replaces second moment with 4-bit codebook, achieving comparable performance to full-precision Adam.
* `token-pruning` `efficient-inference` `MLLM` [SPIDER: Multi-Layer Semantic Token Pruning and Adaptive Sub-Layer Skipping in Multimodal Large Language Models](http://arxiv.org/abs/2609.34977v1)
  > **TL;DR**: Addresses efficiency in MLLMs via multi-layer semantic visual token pruning & adaptive sub-layer skipping (SPIDER), reducing FLOPs by 79% while preserving 96% performance on LLaVA-NeXT-7B.
* `token-pruning` `efficient-inference` `MLLM` [Just MLPs: Efficient Visual State Reconstruction for Multimodal Language Models](http://arxiv.org/abs/2609.34972v1)
  > **TL;DR**: Reduces computation in MLLMs via lightweight low-rank adapters to avoid token pruning, maintaining all visual tokens with 95% accuracy at lower FLOPs.
* `quantization` `efficient-inference` [From Attention Sensitivity to Layer Role: Revisiting Mixed-Precision Quantization of Transformers](http://arxiv.org/abs/2609.34866v1)
  > **TL;DR**: Proposes mixed-precision quantization for Transformers using joint QKV attention block objectives. Achieves 3-bit quantization with 77-90% recovery of GPTQ gap (Mistral-7B), later improved to 4.5 bits avg at 3.56x compression.
* `token-pruning` `efficient-inference` `MLLM` [OmniTide: Co-Designing Algorithms and Systems for Efficient On-Device Omni-LLM Streaming](http://arxiv.org/abs/2609.34653v1)
  > **TL;DR**: Efficient on-device omni-modal streaming faces KV cache growth. OmniTide retains critical context with unit-based retention (OmniPick) and dynamically compacts tokens (OmniPage), achieving 12.72× kernel speedups, 2.40× lower latency, and 18.0% accuracy gain over baselines.
* `quantization` `efficient-inference` `MLLM` [DPS: Dual-Mode Precision LLM Serving with Semi-Unified Memory](http://arxiv.org/abs/2609.34380v1)
  > **TL;DR**: Dual-mode LLM serving switches between FP16 and lower-precision weights to repurpose memory for KV cache, improving throughput 2.1-3.3x while maintaining accuracy.
* `quantization` `efficient-inference` `MLLM` [QuantaSpike: Short-Window Spike-Driven Quantization for Large Language Models](http://arxiv.org/abs/2609.34259v1)
  > **TL;DR**: Proposes QuantaSpike for energy-efficient LLM inference via short-window spike-driven quantization with Logarithmic Ternary Integrate-and-Fire neurons. Achieves 80% energy reduction on OPT models and 67.1% on Llama-2 compared to SpikeQuant, maintaining close to FP16 accuracy with 4-step firing windows.
* `compression` `quantization` `efficient-inference` [EntroPack: Fast and Accurate Entropy-Coded Weight Compression at Arbitrary Bitrates](http://arxiv.org/abs/2609.34185v1)
  > **TL;DR**: Proposes EntroPack for entropy-coded weight compression at arbitrary bitrates using E_8 lattice quantization, achieving 24% lower L2 weight error than NF4 at 4 bits/param.
* `compression` `efficient-inference` [CASS: Contribution-Aware Structured Sparsity for Model Merging](http://arxiv.org/abs/2609.34184v1)
  > **TL;DR**: Structured sparsity for model merging via contribution-aware masks, reducing parameter interference; improves merging baselines across vision and language benchmarks
* `compression` `efficient-inference` `MLLM` [SlimWise: Decoupling Expert Pruning Across Prefill and Decode for Efficient MoE Serving](http://arxiv.org/abs/2609.34117v1)
  > **TL;DR**: Expert pruning for MoE models, decoupling pruning during prefill and decode phases. SlimWise achieves 1.81x decode throughput at 50% expert pruning with minimal accuracy loss by reusing prefill KV cache and distillation.
* `compression` `efficient-inference` [MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference](http://arxiv.org/abs/2609.34077v1)
  > **TL;DR**: Reduces MoE inference memory by 23.7% via masked co-adaptive fine-tuning that limits expert access per layer.
* `token-pruning` `efficient-inference` [SANTA++: Sampling Attention through Representative Keys](http://arxiv.org/abs/2609.35629v1)
  > **TL;DR**: Reduces KV cache memory reads via stochastic attention with representative key sampling, achieving 16-22% reads of dense attention with 94-99% score retention, 1.69x speedup at 32K context.
* `compression` `efficient-inference` `MLLM` [Cartridges++: KV Cache Compression without Off-Context Derailment](http://arxiv.org/abs/2609.35621v1)
  > **TL;DR**: Compresses KV cache for LLMs via distillation, improves off-context query handling with router/data-mixing variants, reduces memory footprint.
* `compression` `efficient-inference` [Output-aware Residual Stream Pruning for Large Language Models](http://arxiv.org/abs/2609.35579v1)
  > **TL;DR**: Fixes blind post-pruning sensitivity in LLMs by optimizing a spectral upper bound of output KL divergence, achieving better perplexity and task performance vs. activation-only pruning.
* `quantization` `efficient-inference` `MLLM` [Tetra: Serving Leech-Lattice Quantized LLMs at 2.7 Bits per Parameter](http://arxiv.org/abs/2609.35465v1)
  > **TL;DR**: Proposes Tetra, a Leech-lattice quantization method for LLMs achieving 2.7 bits/weight via a trellis-coded codebook and 4-bit fallback, enabling 57.2-113.8 tokens/sec at <3 points MMLU drop vs FP16.
* `quantization` `compression` [The Hidden Ratio in Adam: Stable Structure, Compression, and Sign Dynamics](http://arxiv.org/abs/2609.35392v1)
  > **TL;DR**: Proposes a compressible state reparameterization of Adam optimizer using a stable ratio structure, enabling 4-bit storage of second-moment state without performance loss.
* `quantization` `efficient-inference` [Fiona: Accelerating FHE Inference with Packing-Aware Ternary Weights](http://arxiv.org/abs/2609.35352v1)
  > **TL;DR**: Accelerates FHE inference via packing-aware ternary (2-bit) weight quantization, reducing PMult ops by 53.4-79.5% and speeding up encrypted inference by up to 2.38x with <1% accuracy drop.
* `token-pruning` `compression` `efficient-inference` [Beyond Selection: Token Parameterization for Extreme Visual Token Compression](http://arxiv.org/abs/2609.35232v1)
  > **TL;DR**: Extreme visual token compression via basis truncation and learned spatial residuals, achieving 95.2% accuracy at 23x–144x compression with 84.2%–86.7% FLOPs reduction and 36% speedup.
* `compression` `efficient-inference` [Sub-Model Short-Term Memory Convolutions for Keyword Spotting Systems on Device](http://arxiv.org/abs/2609.35005v1)
  > **TL;DR**: Reduces computational cost in keyword spotting with Short-Term Memory Convolutions, achieving 46-82% fewer operations while maintaining 93.8% accuracy.
* `quantization` `efficient-inference` `compression` [From Attention Sensitivity to Layer Role: Revisiting Mixed-Precision Quantization of Transformers](http://arxiv.org/abs/2609.34866v1)
  > **TL;DR**: Proposes JAB for mixed-precision quantization of Transformers by jointly optimizing Q,K,V weights in attention layers, achieving 3-bit quantization recovering 77-90% of full precision performance, with 96.4% weights at 4.5 bits on full Mistral-7B at 3.56x compression.
* `token-pruning` `efficient-inference` `MLLM` [When Text Matters: Design Principles for Visual Token Pruning in Vision-Language Model](http://arxiv.org/abs/2609.34861v1)
  > **TL;DR**: Visual token pruning for VLMs with deferred text-guided reselection, achieving 11.10% and 16.84% better performance recovery at 80% and 90% pruning rates.
* `quantization` `MLLM` `efficient-inference` [Beyond Reconstruction Loss in Post-Training Quantization: Balanced Fitting for Large Vision-Language Models](http://arxiv.org/abs/2609.34765v1)
  > **TL;DR**: Proposes a balanced PTQ method for LVLMs, combining fine-grained fitting with quantization regularization, outperforming prior PTQ in weight-only and weight-activation setups without clear reconstruction-loss-DT performance correlation.
* `quantization` `compression` `efficient-inference` [QuantForge: Discovering Residual Decompositions for MXFP4 Post-Training Quantization](http://arxiv.org/abs/2609.34680v1)
  > **TL;DR**: Presents QuantForge for discovering MXFP4 W4A4 PTQ decompositions, shaping attention/MLP paths residuals. Achieves best fit (0.093) on 7 tasks at 32B scale.
* `token-pruning` `efficient-inference` `MLLM` [OmniTide: Co-Designing Algorithms and Systems for Efficient On-Device Omni-LLM Streaming](http://arxiv.org/abs/2609.34653v1)
  > **TL;DR**: Addresses KV cache memory bottleneck in on-device omni-modal LLMs via modality-aware token pruning (OmniPick) and memory-optimized cache partitioning (OmniPage), achieving 12.72× kernel speedups and 26.7% KV span reduction.
* `compression` `efficient-inference` [When Can Attention Heads Be Statically Defined?](http://arxiv.org/abs/2609.34650v1)
  > **TL;DR**: Reduces training cost by freezing attention heads with low variance, storing patterns linearly (vs quadratic). Replacing 25% heads speeds updates 1.056x at 124M params with minimal perplexity impact (0.77%).
* `token-pruning` `efficient-inference` `compression` [X-MoD: Practical Scaling Laws for Sparse-Depth Routing Beyond Mixture-of-Depths](http://arxiv.org/abs/2609.34212v1)
  > **TL;DR**: X-MoD improves sparse-depth routing in Transformers by decoupling token sparsity from anchor stride, enabling scalable conditional computation. Reduces active computation while maintaining performance, validated via pretraining sweeps and scaling laws.
* `compression` `quantization` `efficient-inference` [EntroPack: Fast and Accurate Entropy-Coded Weight Compression at Arbitrary Bitrates](http://arxiv.org/abs/2609.34185v1)
  > **TL;DR**: Efficient weight compression via entropy-coded E8 lattice quantization with flexible bitrates (e.g., 4 bits/param), achieving 24% lower L2 weight error than NF4 at similar storage rates with fast GPU decoding.
* `compression` `efficient-inference` `MLLM` [SlimWise: Decoupling Expert Pruning Across Prefill and Decode for Efficient MoE Serving](http://arxiv.org/abs/2609.34117v1)
  > **TL;DR**: Prunes experts for efficient MoE serving by decoupling prefill and decode phases, reusing KV caches without conversion. Achieves 1.81x decode throughput at 50% expert pruning with minimal accuracy loss.
* `compression` `efficient-inference` [MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference](http://arxiv.org/abs/2609.34077v1)
  > **TL;DR**: Memory-efficient MoE inference via masked co-adaptive fine-tuning, reduces expert fetches per token by 23.7% & lowers time per output token by up to 16.4%, accuracy maintained.

### 2026-09-27
* `quantization` `efficient-inference` [Chameleon: Dynamic Format Adapter for Efficient Diffusion](http://arxiv.org/abs/2609.33496v1)
  > **TL;DR**: Dynamic format adapter selects optimal per-channel & per-timestep bit format for diffusion model PTQ, achieving best FID at W4A8 with CLIP within 0.24 of FP16.
* `quantization` `efficient-inference` `compression` [PulseQuant: Propagation-Guided Subspace Correction for 4-Bit Video Diffusion Transformers](http://arxiv.org/abs/2609.33384v1)
  > **TL;DR**: Quantization errors in video diffusion transformers propagate unpredictably. PulseQuant combines trajectory sensitivity and activation geometry for 4-bit PTQ, using propagation-aware calibration and subspace correction. Improves key metrics while preserving 4-bit weights.
* `compression` `efficient-inference` [LoopTrack: A Simple Baseline for Parameter-Efficient Transformer Tracking](http://arxiv.org/abs/2609.33306v1)
  > **TL;DR**: Parameter-efficient Transformer tracking via looped, shared blocks for feature interaction, reducing parameters (3.4M and 6.4M variants), achieving 66.2-69.3% SUC on LaSOT.
* `quantization` `compression` `efficient-inference` [Q-WAM: 4-Bit Quantization of World Action Models with Action-Subspace Protection](http://arxiv.org/abs/2609.33269v1)
  > **TL;DR**: Q-WAM enables 4-bit weight-activation quantization for World Action Models via Action-Subspace Protection (ASP), maintaining action precision with 16-bit sensitive channels. Achieves 89.6--93.0% success rate on RoboTwin 2.0, 3.1--3.4x memory reduction.
* `token-pruning` `efficient-inference` `compression` [Scope-WM: Scoped Computation for Efficient Visual World Models](http://arxiv.org/abs/2609.33218v1)
  > **TL;DR**: Reduces visual world model latency and memory via action-conditioned token selection, achieving 6.97× planning speedup and 18.1% memory usage versus dense models.
* `compression` `efficient-inference` `MLLM` [Query, Align, and Distill: Navigation-Aware Cross-Modal Interaction for Efficient Vision-and-Language Navigation](http://arxiv.org/abs/2609.33097v1)
  > **TL;DR**: Efficient Vision-and-Language Navigation via distillation and token-adaptive objective, reducing parameters by 93.65% while matching teacher performance.
* `compression` `efficient-inference` `MLLM` [GroupMask: Layer-Adaptive Group-wise Sparsity for Semi-Structured LLM Pruning](http://arxiv.org/abs/2609.33977v1)
  > **TL;DR**: Proposes GroupMask for layer-adaptive group-wise sparsity in LLM pruning, achieving 50% sparsity on LLaMA-2-7B, reducing perplexity from 10.02 to 8.30.
* `token-pruning` `efficient-inference` [On the Token Value Inequality in Efficient Reasoning](http://arxiv.org/abs/2609.33970v1)
  > **TL;DR**: Addresses token inefficiency in CoT reasoning by identifying and pruning low-value tokens with normalized log probability signals, reducing token usage by 76% while maintaining reasoning quality.
* `quantization` `efficient-inference` `compression` [Quantization Error Is Spectrally Flat: A Single Random Probe Is a Calibrated, Data-Free Sensitivity Estimator, with Application to Budget-Targeted Mixed-Precision Quantization](http://arxiv.org/abs/2609.33923v1)
  > **TL;DR**: Proposes a data-free mixed-precision quantization method using a single random Gaussian probe to estimate per-tensor sensitivity, enabling budget-targeted bit allocation (2-bit to 8-bit), achieving 3.5-13.6% lower perplexity than uniform 4-bit models.
* `quantization` `efficient-inference` `compression` [Transformer-based Neural Beamforming for Real-Time Speech Enhancement on Smart Low-Power Hearable Devices](http://arxiv.org/abs/2609.33755v1)
  > **TL;DR**: Optimizes real-time neural beamforming for hearables using mixed-precision (float32, int8, float16) to achieve 15ms latency with 45.9mW power, while maintaining 97.65% STOI.
* `compression` `efficient-inference` [One Latent, Many Tokens: Jointly Learning Compressed Embeddings for Efficient Language Diffusion](http://arxiv.org/abs/2609.33698v1)
  > **TL;DR**: Problem: high cost of diffusion language models. Method: jointly trains compressor, flow matching, and decoder for structured compressed embeddings. Compression rate: 0.5x. Result: 34.52 Gen-PPL and 2.3x throughput over ELF.
* `compression` `efficient-inference` `token-pruning` [EAT: Expert Account Tracker for Efficient MoE Inference](http://arxiv.org/abs/2609.33614v1)
  > **TL;DR**: Proposes Expert Account Tracker (EAT) for efficient MoE inference by dynamically selecting important experts, reducing activated experts by 25%, improving token generation speed.
* `quantization` `efficient-inference` `MLLM` [JustQuant: You Don't Need Smoothing, SVD, or Rotation for 4-Bit Activation Quantization](http://arxiv.org/abs/2609.33601v1)
  > **TL;DR**: Proposes JustQuant for 4-bit activation quantization via multi-level supervision (Theseus QAD), avoiding complex PTQ operators. Achieves better quantization quality on diffusion and LLMs.
* `quantization` `compression` `efficient-inference` [TerMeZO: Ternary Sparse Zeroth-Order Optimization for Fine-tuning BitNet Models at the Edge](http://arxiv.org/abs/2609.33548v1)
  > **TL;DR**: Ternary sparse fine-tuning for BitNet (ternary weights, 8-bit activations) via zeroth-order optimization, reducing memory footprint. Achieves better performance than full-parameter fine-tuning while lowering memory usage.
* `quantization` `efficient-inference` [Chameleon: Dynamic Format Adapter for Efficient Diffusion](http://arxiv.org/abs/2609.33496v1)
  > **TL;DR**: Dynamic format adapter for diffusion PTQ, selecting per-channel weight (4-8b) and per-layer-activation (8b) formats based on data distribution. Achieves best FID in SDXL/PixArt at W4A8, CLIP within 0.24 of FP16.
* `efficient-inference` `token-pruning` `MLLM` [Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs](http://arxiv.org/abs/2609.33477v1)
  > **TL;DR**: Improves hybrid LLM inference efficiency via suffix replay for prefix caching, reducing median TTFT by 15-70% and cutting storage to 0.36-0.51x of baseline.
* `token-pruning` `efficient-inference` `MLLM` [CoViST: Visual Token Compression via Composable States](http://arxiv.org/abs/2609.33397v1)
  > **TL;DR**: Visual token compression for VLMs via composable states (position + weights + metadata), retaining 99.9% performance at 192 tokens, and 98.1% at 64 tokens.
* `token-pruning` `efficient-inference` [Scope-WM: Scoped Computation for Efficient Visual World Models](http://arxiv.org/abs/2609.33218v1)
  > **TL;DR**: Reduces GPU memory (18.1%) and planning time (14.3%) via action-conditioned token selection and sparse dynamics prediction in visual world models.
* `compression` `efficient-inference` `MLLM` [Query, Align, and Distill: Navigation-Aware Cross-Modal Interaction for Efficient Vision-and-Language Navigation](http://arxiv.org/abs/2609.33097v1)
  > **TL;DR**: Compresses vision-and-language navigation models by 93.65% via distillation from a teacher that explicitly selects navigable evidence tokens and transfers attention locations, nearly matching teacher performance.
* `compression` `efficient-inference` `MLLM` [GroupMask: Layer-Adaptive Group-wise Sparsity for Semi-Structured LLM Pruning](http://arxiv.org/abs/2609.33977v1)
  > **TL;DR**: Semi-structured LLM pruning via layer-adaptive group-wise sparsity with GroupMask, achieving 50% sparsity, reducing WikiText-2 perplexity from 10.02 to 8.30.
* `quantization` `efficient-inference` `MLLM` [Optimizing the Phi-2 Small Language Model for Real-time Chatbot Applications Using Parameter-Efficient Fine-Tuning (PEFT) with QLoRA Quantization](http://arxiv.org/abs/2609.33927v1)
  > **TL;DR**: Enhances Phi-2 SLMs via PEFT with 4-bit QLoRA, reducing memory usage for mobile/edge deployment, maintaining accuracy with 4-bit quantization, and showing improved ROUGE scores for summarization.
* `quantization` `efficient-inference` [Quantization Error Is Spectrally Flat: A Single Random Probe Is a Calibrated, Data-Free Sensitivity Estimator, with Application to Budget-Targeted Mixed-Precision Quantization](http://arxiv.org/abs/2609.33923v1)
  > **TL;DR**: Proposes a data-free sensitive estimator for mixed-precision quantization using random Gaussian probes, achieving 3.5-13.6% lower perplexity than 4-bit uniform quantization on MoE models without calibration data.
* `compression` `efficient-inference` `token-pruning` [Where Activation Sparsity and KV-Cache Sparsity Cross in LLM Decoding](http://arxiv.org/abs/2609.33889v1)
  > **TL;DR**: Efficient LLM decoding via KV-cache sparsity and activation sparsity, achieving 14-26% speedup under matched perplexity budgets.
* `efficient-inference` `compression` `token-pruning` [PQ-HSA: Reusing Product-Quantized Scores for Hybrid Sparse-Approximate Attention](http://arxiv.org/abs/2609.33746v1)
  > **TL;DR**: Proposes PQ-HSA for efficient long-context attention by reusing quantized scores to reduce KV cache access, achieving 1.6x speedup at 128K context with minimal accuracy drop.
* `quantization` `efficient-inference` [Pretraining Transformers with Quantized Softmax in Attention](http://arxiv.org/abs/2609.33591v1)
  > **TL;DR**: Efficient attention via quantized softmax in Transformers using K-interval approximation (K=4 to 16), minimizing loss gap to +0.004 nats at K=16 with pretraining-compatible backward rules.
* `quantization` `efficient-inference` `MLLM` [Approximating Softmax in Pretrained LLMs: Model Sensitivity and Kernel Acceleration](http://arxiv.org/abs/2609.33586v1)
  > **TL;DR**: Efficient softmax approximation for LLMs with logarithmic weight representation (Rowmax-PoT) speeds FP8 attention (12.4-25.8% faster at 8K), reduces energy by 8.4% at 16K, with minimal perplexity increase (0.091-0.492%).
* `quantization` `compression` `efficient-inference` [TerMeZO: Ternary Sparse Zeroth-Order Optimization for Fine-tuning BitNet Models at the Edge](http://arxiv.org/abs/2609.33548v1)
  > **TL;DR**: Fine-tuning ternary (-1,0,1) BitNet models with reduced memory via sparse zeroth-order optimization. TerMeZO leverages ternary structure for weight selection, matching MeZO performance with lower memory. Tested on 1B-3B models.
* `quantization` `efficient-inference` `MLLM` [Chameleon: Dynamic Format Adapter for Efficient Diffusion](http://arxiv.org/abs/2609.33496v1)
  > **TL;DR**: Proposes Chameleon, a PTQ framework for diffusion models that dynamically selects the best numerical format per weight channel and activation tensor, achieving 4-bit weights (W4A8) with minimal FID degradation on SDXL and SDXL-Turbo, outperforming fixed-format PTQ methods.
* `token-pruning` `efficient-inference` `MLLM` [When to Evict, Not What to Keep: Draft-Guided Eviction for Training-Free KV-Cache Compression](http://arxiv.org/abs/2609.33334v1)
  > **TL;DR**: Proposes Draft-Guided Eviction (DGE) for KV-cache compression by deferring eviction until drafting first k=2 tokens, improving over prior methods with 44.2 on LongBench (vs 44.3 FullKV).
* `compression` `efficient-inference` [SketchSSM: Write to the Full State, Read from a Compact Sketch](http://arxiv.org/abs/2609.33051v1)
  > **TL;DR**: Reduces state-access traffic in hybrid-attention models via compact sketch-based state reads, cutting traffic by ~10x while preserving accuracy, achieving 7.78x kernel speedup on Mamba-2.

### 2026-09-26
* `token-pruning` `efficient-inference` [Improving Video Sparse Attention with Fine-grained Router and Sparse Rebasing](http://arxiv.org/abs/2609.32882v1)
  > **TL;DR**: Reduces video attention computation via fine-grained router and sparse rebasing, achieving 8.9x speedup in attention and 4.62x end-to-end generation while maintaining quality.
* `compression` `token-pruning` `MLLM` [OmniMoE-VL: A Sparse Vision-Language Model with Coupled Visual-Depth Routing](http://arxiv.org/abs/2609.32780v1)
  > **TL;DR**: Sparse VLM with visual-depth routing for question-dependent token selection, achieves 85.9 score with 9B activated params (28B total).
* `token-pruning` `efficient-inference` `MLLM` [Refinement Symmetry in Multimodal Transformers](http://arxiv.org/abs/2609.32669v1)
  > **TL;DR**: Addresses token inefficiency in multimodal transformers via refinement symmetry, using linear mass factors and measure weighting. Tests on Qwen2.5-Omni-7B show reduced drift and 1.04% accuracy gain with token merging.
* `quantization` `efficient-inference` [DraftAttention2: Fast Video Diffusion with Low-Resolution-Guided Mixed-Precision Attention](http://arxiv.org/abs/2609.32628v1)
  > **TL;DR**: Proposes DraftAttention2, a mixed-precision attention method for efficient video diffusion, using 4- and 8-bit quantization guided by low-resolution draft attention to skip or reduce precision in less important blocks, achieving better quality-efficiency trade-off with significant acceleration.
* `compression` `efficient-inference` [RIPE-MambaSpike: Resolution-Independent Spiking-State-Space Interfaces for Parameter-Efficient Event-Based Vision](http://arxiv.org/abs/2609.32537v1)
  > **TL;DR**: Reduces parameter cost in spiking-Mamba hybrids from 36.25M to 0.870M via hierarchical multi-resolution bridge, achieving 45.7% accuracy on DailyDVS-200 with 3.0-15.1x fewer params than dense ANNs.
* `token-pruning` `MLLM` `efficient-inference` [Fewer Tokens, More Self-Teaching: On-Policy Self-Distillation for Extreme Visual Token Reduction](http://arxiv.org/abs/2609.32353v1)
  > **TL;DR**: Focus on extreme visual token reduction (5% retention) for MLLMs via on-policy self-distillation (LT-OPD) with curriculum learning. Achieves 82.3% retained performance, 85.2% KV-cache reduction, and 85.4% prefill FLOPs savings.
* `token-pruning` `efficient-inference` `MLLM` [KeyRec: Bounded Visual Memory for Streaming and Long-Video Understanding](http://arxiv.org/abs/2609.32182v1)
  > **TL;DR**: Proposes KeyRec, a training-free visual token pruning method for long-video VLMs, retaining 10% tokens while outperforming baselines by 2.21-18.37 pts on real-time questions.
* `compression` `efficient-inference` [PruneForget: Joint Unlearning and Pruning of Vision Models](http://arxiv.org/abs/2609.32162v1)
  > **TL;DR**: Joint unlearning and pruning for vision models to improve efficiency; uses unlearn set to guide pruning; achieves compaction and unlearning with negligible performance drop.
* `token-pruning` `efficient-inference` [Beyond Token Savings: A Systematic Study of Context Compression in LLM Agents](http://arxiv.org/abs/2609.32961v1)
  > **TL;DR**: Examines token compression in LLM agents, revealing that fewer tokens need not mean faster execution (20-80% longer with 1/3 tokens). Systematically evaluates effects on task success, latency, and cost across models.
* `quantization` `efficient-inference` [Precision As You Need: Stochastic Computing Is a Dense Adaptive Quantizer](http://arxiv.org/abs/2609.32922v1)
  > **TL;DR**: Proposes stochastic computing as a dense adaptive quantizer for vision transformers, enabling per-row mixed-precision inference with dynamic bit-stream lengths (L) competing with INT quantization. Matches accuracy at lower average stream lengths.
* `quantization` `efficient-inference` [Logic Gate Networks and Lookup Table Networks as Lightweight Hardware Classifiers for Inter-patient ECG Arrhythmia Classification](http://arxiv.org/abs/2609.32854v1)
  > **TL;DR**: Proposes Logic Gate Networks and Lookup Table Networks for low-power ECG classification, achieving 94.41% accuracy with 2.89k-6.17k FLOPs and only 0.46 nJ energy per inference.
* `quantization` `efficient-inference` `token-pruning` [DraftAttention2: Fast Video Diffusion with Low-Resolution-Guided Mixed-Precision Attention](http://arxiv.org/abs/2609.32628v1)
  > **TL;DR**: Fast video diffusion via mixed-precision attention (INT4/INT8) and token pruning guided by low-resolution drafts, improving efficiency with configurable budgets and fused kernels, achieving superior quality-speed trade-off in few-step generation.
* `quantization` `efficient-inference` `MLLM` [PrismQuant: Optimal Null-Space Rotations for Grouped Quantizers](http://arxiv.org/abs/2609.32429v1)
  > **TL;DR**: PrismQuant optimizes INT4 grouped quantization via Ky Fan trace maximization for alignment, achieving W4A4KV4 on Llama-3.1-70B with 72.46% zero-shot accuracy, 1.51x prefill speedup, and 56.34% lower memory.
* `compression` `efficient-inference` [Fracast-0: Fractal Weight Sharing for a Time Series Foundation Model with Only 85K Parameters](http://arxiv.org/abs/2609.32209v1)
  > **TL;DR**: Reduces parameter count in time series foundation models via fractal weight sharing and scale conditioning, achieving 85K parameters with 42% fewer params than TinyCast while maintaining competitive accuracy (MASE 0.808).
* `token-pruning` `efficient-inference` `MLLM` [KeyRec: Bounded Visual Memory for Streaming and Long-Video Understanding](http://arxiv.org/abs/2609.32182v1)
  > **TL;DR**: Long-video VLMs face high token costs. KeyRec selects and manages visual tokens with bounded memory, reducing decoder-facing tokens to 10% while improving performance by 2.21–18.37 points.
* `efficient-inference` `MLLM` [Empowering Hybrid Attention Models on NPUs](http://arxiv.org/abs/2609.32114v1)
  > **TL;DR**: Addresses memory and computational inefficiency of hybrid attention LLMs on edge NPUs via dataflow reorganization at core, operator, and tensor levels, achieving 2.03x faster latency and 36.14x energy reduction.
* `compression` `efficient-inference` `quantization` [Logic Gate Networks and Lookup Table Networks as Lightweight Hardware Classifiers for Inter-patient ECG Arrhythmia Classification](http://arxiv.org/abs/2609.32854v1)
  > **TL;DR**: Proposes lightweight binary logic gate (LGN) and lookup table (LUTN) networks for ECG classification, achieving 94.41% accuracy with only 2.89k-6.17k FLOPs (3-6 orders lower than SOTA) and 0.46nJ energy consumption per inference.
* `compression` `token-pruning` `efficient-inference` [UniCache: Task- and Type-Aware KV Cache Compression for Unified Multimodal Models](http://arxiv.org/abs/2609.32831v1)
  > **TL;DR**: Efficient KV cache compression for multimodal models via task- and type-aware policies, achieving 5x compression for understanding/editing and 2.5x for generation with negligible quality loss.
* `token-pruning` `efficient-inference` `MLLM` [OmniMoE-VL: A Sparse Vision-Language Model with Coupled Visual-Depth Routing](http://arxiv.org/abs/2609.32780v1)
  > **TL;DR**: OmniMoE-VL introduces a coupled visual-depth routed projector for VLMs, selecting sparse visual depths and reusing global preferences to guide patch fusion and visual injection, reducing activated parameters to 9B while achieving 85.9 average score on 8 benchmarks.
* `token-pruning` `efficient-inference` `MLLM` [Distance-KV: Exploiting Relative Distance for Efficient Long-Context Inference](http://arxiv.org/abs/2609.32663v1)
  > **TL;DR**: Efficient long-context LLM inference via static KV cache pruning based on relative distance, reducing KV cache memory by 65.4% and achieving 1.66x speedup at 128K context length.
* `quantization` `efficient-inference` `MLLM` [Quantization-Aware Pre-Training with Constrained Empirical Weight Distribution](http://arxiv.org/abs/2609.32659v1)
  > **TL;DR**: Proposes Constrained Empirical Weight Distribution (CEWT) to suppress rounding boundary weight oscillation in Quantization-Aware Pre-Training (QAPT), achieving 2.5 average perplexity reduction for 1-bit quantized LLaMA/GPT models without hyperparameters or memory overhead.
* `compression` `efficient-inference` [Stabilizing the Dynamic Low-Rank Training](http://arxiv.org/abs/2609.32615v1)
  > **TL;DR**: Stabilizes dynamic low-rank training (DLRT) with gradient flow analysis, achieving efficient subnetworks through compensation buffer and adaptive rank control; maintains SuperGLUE performance with only 2.8% parameter overhead.
* `quantization` `efficient-inference` `MLLM` [PrismQuant: Optimal Null-Space Rotations for Grouped Quantizers](http://arxiv.org/abs/2609.32429v1)
  > **TL;DR**: Optimizes grouped INT4 quantization by aligning activation eigenspace with group subspace via optimal rotation, achieving 3.85 perplexity on Llama-70B (W4A4KV4) and 1.22x decode speedup with 56.34% lower memory.
* `token-pruning` `efficient-inference` `MLLM` [Fewer Tokens, More Self-Teaching: On-Policy Self-Distillation for Extreme Visual Token Reduction](http://arxiv.org/abs/2609.32353v1)
  > **TL;DR**: Proposes LT-OPD for extreme visual token reduction in MLLMs via on-policy self-distillation and budget-level curriculum. Achieves 82.3% retained performance under 5% token retention, reducing KV-cache usage by 85.2% and prefill FLOPs by 85.4%.
* `compression` `efficient-inference` [DP-Rec: Towards Dynamic Patching for Efficient Long-Sequence Recommendation](http://arxiv.org/abs/2609.32215v1)
  > **TL;DR**: Dynamic patching method DP-Rec compresses long user sequences into informative latent vectors via contrastive entropy surprise, reducing computational overhead while maintaining accuracy for recommendation systems.
* `compression` `token-pruning` `efficient-inference` [DegreeSpar: Structured Degree Sparsity for Efficient Secure Transformer Inference](http://arxiv.org/abs/2609.32204v1)
  > **TL;DR**: Structured polynomial degree sparsification (DegreeSpar) for secure Transformer inference, combining token pruning and model pruning, achieves 2.29x-6.63x speedup with BERT/SST-2 accuracy of 92.68% at 110.55s.

### 2026-09-25
* `token-pruning` `compression` `efficient-inference` [Where Compute Matters: Heterogeneous Attention for Efficient Video Diffusion](http://arxiv.org/abs/2609.31050v1)
  > **TL;DR**: Adaptive token pruning for video diffusion models using heterogeneous attention, routing only 20% tokens to dense attention while maintaining quality.
* `compression` `efficient-inference` [Training-Free Bottleneck Width Planning for Convolutional Autoencoders](http://arxiv.org/abs/2609.30755v1)
  > **TL;DR**: Training-free method (MS-SRD) plans bottleneck width for autoencoders using spectral analysis, achieving 0.84% error in latent-size prediction at NMSE ≤ 0.01, and matching deployment widths without training.
* `efficient-inference` `token-pruning` `quantization` [DeepEdu-v1: Efficient and Scalable Agentic LLMs for Vietnamese Education](http://arxiv.org/abs/2609.31568v1)
  > **TL;DR**: Addresses long-context inference inefficiency and KV cache overhead in LLMs for education; uses token selection at cluster granularity (x7.7 fewer retrievals) and PTQ (AWQ/GPTQ) for weights; reduces prefill latency by 35% and improves accuracy to 79.5%.
* `compression` `efficient-inference` `MLLM` [ActKV: Efficient LLM Agents through Action-Guided KV Cache Management](http://arxiv.org/abs/2609.31395v1)
  > **TL;DR**: Reduces KV cache memory in agentic LLMs by prioritizing action-critical entries, achieving 25.98% peak memory with 98.53% accuracy, and 3.97X token throughput.
* `quantization` `efficient-inference` [The Right Information Extraction Pipeline Depends on the Document: Accuracy-Energy Trade-offs for Small, Local Models](http://arxiv.org/abs/2609.31341v1)
  > **TL;DR**: Studies energy-accuracy trade-offs for on-premise document processing using small models (≤8B params). FP8 quantization saves 27-32% energy in single-request settings, while batching reduces energy by 38-85% per page.
* `quantization` `efficient-inference` `compression` [Softmax Reparameterization for Output-Head Quantization](http://arxiv.org/abs/2609.31291v1)
  > **TL;DR**: Proposes softmax reparameterization for post-training quantization of output heads in small LMs, achieving W4 (INT4) quantization with KL divergence reduced from 0.936 to 0.256 on Phi-4-mini, and 10.8% lower latency while preserving model accuracy.
* `compression` `efficient-inference` `token-pruning` [Acoustic-to-Text KV Compression for Full-Duplex Speech Models](http://arxiv.org/abs/2609.31224v1)
  > **TL;DR**: Reduces KV cache memory in full-duplex speech models by 64.6% via acoustic-to-text compression and eviction of older states, keeping recent context and transcripts for efficient streaming.
* `quantization` `efficient-inference` `compression` [Teacher-Anchored Selection of Post-Training Quantized Models under Domain Shift](http://arxiv.org/abs/2609.31155v1)
  > **TL;DR**: Proposes teacher-anchored selection for domain-shifted post-training quantized models, focusing on 8-bit unclipped configurations. Method reduces regret with minimal labels, outperforming confidence-based estimators across 134 model families.
* `quantization` `efficient-inference` `MLLM` [G$^2$PTQ: Improving LLM Post-Training Quantization with Generalized Gradient Compensation](http://arxiv.org/abs/2609.31009v1)
  > **TL;DR**: Proposes G²PTQ for improved PTQ of LLMs via globally supervised block-wise optimization with dynamic gradient & Hessian updates. Achieves better alignment with full-precision models across various bit-widths.
* `token-pruning` `efficient-inference` `MLLM` [Skip the Talk, Re-Focus on Vision: Latent Reasoning for Reasoning Segmentation in Multimodal Large Language Models](http://arxiv.org/abs/2609.30783v1)
  > **TL;DR**: Reduces reasoning tokens in MLLMs for segmentation by replacing explicit CoT with compact learnable latent tokens, achieving 16x token reduction and +4.9% gIoU on ReasonSeg.
* `token-pruning` `efficient-inference` [Selective Amortization of Full-Budget Counterfactual Reasoning for Visual Token Communication](http://arxiv.org/abs/2609.30756v1)
  > **TL;DR**: Optimizes visual token communication by selectively evaluating the most informative tokens, reducing encoder computation. ACV-Gate combines terminal-value learning with selective refinement, achieving 27.6% fewer evaluations and 0.636 dB PSNR gain at 0.20 bpp.
* `compression` `quantization` `efficient-inference` [Weight Pair Encoding: Inducing a Smaller Grammar in Neural Network Weights](http://arxiv.org/abs/2609.31564v1)
  > **TL;DR**: Weight Pair Encoding compresses neural network weights by applying grammar-based compression techniques (Re-Pair, int8 quantization) within training, achieving 0.38-0.43x grammar size reduction vs int8 QAT at 1.1-1.9 accuracy cost on ViT models.
* `quantization` `compression` [Generalization behavior of OPTQ and the role of regularization](http://arxiv.org/abs/2609.31560v1)
  > **TL;DR**: Studies quantization via OPTQ and stochastic OPTQ, focusing on generalization bounds and regularization role in minimizing squared quantization error. Proves bounds for generalization error and recommends new λ setting, with favorable experimental results.
* `compression` `efficient-inference` [Scaffold: Support Graph Theory Based Sparsification for Graph Neural Networks](http://arxiv.org/abs/2609.31466v1)
  > **TL;DR**: Reduces GNN computational cost via topology-aware graph sparsification, preserving key edges (10%-50% retained) while maintaining accuracy, cutting memory by >50% and improving training speed.
* `quantization` `efficient-inference` `MLLM` [Towards Understanding LLM-Based Log Anomaly Detection: An Empirical Study of Performance, Efficiency, and Robustness](http://arxiv.org/abs/2609.31371v1)
  > **TL;DR**: Analyzes efficiency vs. accuracy trade-offs in LLM-based log anomaly detection; low-bit quantization preserves accuracy with lower compute costs; empirical results show varying computational costs for models with similar accuracy.
* `quantization` `compression` `efficient-inference` [Softmax Reparameterization for Output-Head Quantization](http://arxiv.org/abs/2609.31291v1)
  > **TL;DR**: Post-training method for output head quantization via softmax reparameterization, enabling W4 and W2 quantization with 10.8% latency reduction, reducing AW-MSE KL from 0.936 to 0.256.
* `quantization` `efficient-inference` `compression` [Teacher-Anchored Selection of Post-Training Quantized Models under Domain Shift](http://arxiv.org/abs/2609.31155v1)
  > **TL;DR**: Selects optimal quantized models (e.g., 8-bit) under domain shift via teacher-anchored selection, reducing label dependency. Achieves 8-bit per-channel quantization with improved selection stability, reducing mean regret at low label budgets.
* `compression` `efficient-inference` [KuaFu: Compressing Long User Behavior into Understanding at Billion Scale](http://arxiv.org/abs/2609.31045v1)
  > **TL;DR**: Compresses long user behavior sequences (10x-20x) into 2-4 tokens (128-256 width) per item, improving throughput 37%-350% and reducing GPUs by 190 while maintaining downstream task performance.
* `quantization` `efficient-inference` [Low-Bit Recurrent States in Hybrid Language Models](http://arxiv.org/abs/2609.30950v1)
  > **TL;DR**: Quantizes recurrent states in hybrid LMs with mixed-precision bit allocation (4-6 bits), using distortion weights and range normalization, reducing negative log-likelihood by 3.3-27.9x vs baselines at 4 bits with minimal FP32 gap at 6 bits.
* `quantization` `efficient-inference` [The KV Cache Is the New Memory Wall](http://arxiv.org/abs/2609.30854v1)
  > **TL;DR**: Addresses KV cache memory bottleneck in LLM inference with techniques including quantization to cut bandwidth, especially impactful at <4-bit precision, achieving bandwidth savings near theoretical limits at long contexts.
* `quantization` `efficient-inference` `compression` [Quantizing Looped Transformers: Feedback Exposure and Calibration Blindness](http://arxiv.org/abs/2609.30820v1)
  > **TL;DR**: Low-bit INT4 quantization of looped transformers suffers from feedback exposure and calibration blindness. Accumulating Hessian across steps recovers bf16 accuracy on Huginn-3.5B.
* `token-pruning` `efficient-inference` [Beyond Mean Attention: Diversity-Aware, Layer-Wise Scoring for KV Cache Eviction](http://arxiv.org/abs/2609.30738v1)
  > **TL;DR**: Efficient KV cache eviction using diversity-aware layer-wise scoring to reduce memory footprint, improving performance by +1.1 to +13.2 on Mistral-7B at budgets of 32-128 entries per layer.
* `compression` `efficient-inference` [Input-Layer Starvation: Why Per-Layer Pruning Breaks IoT Intrusion Detectors](http://arxiv.org/abs/2609.30729v1)
  > **TL;DR**: Input-layer pruning causes severe class-level failures in IoT intrusion detectors. Uniform layer-wise pruning at 80% sparsity drops macro-F1 by half (0.542 to 0.271). Protecting first-layer weights prevents collapse (loss 0.013) and maintains performance.
* `quantization` `efficient-inference` `MLLM` [LUMO (Lightweight Unified Multilingual Orchestrator): A Privacy Preserving Offline Voice Assistant](http://arxiv.org/abs/2609.30692v1)
  > **TL;DR**: Offline voice assistant LUMO uses 4-bit GGUF quantization for LLM, achieving 6.8% WER, 2.0-4.0s latency, and 9.0W power on Raspberry Pi 5.

### 2026-09-24
* `compression` `quantization` `efficient-inference` [Towards Practical Compression of 3D Gaussian Splatting](http://arxiv.org/abs/2609.30245v1)
  > **TL;DR**: Addresses high storage in 3D Gaussian Splatting via anchor-wise causal factorization and adaptive Gaussian pruning; introduces quantization-aware training and integer inference for cross-platform consistency; achieves state-of-the-art compression performance.
* `efficient-inference` `compression` [Accelerating Video Diffusion via Training-Free Trajectory Routing](http://arxiv.org/abs/2609.30096v1)
  > **TL;DR**: Efficient video diffusion via training-free trajectory routing, using large/small model switching based on relative disagreement scores, achieving 1.95x-2.73x speedups.
* `quantization` `compression` `efficient-inference` [AERIAL: Adversarial Evaluation of Robustness in Accuracy-Preserving Low-Precision EEG Decoders](http://arxiv.org/abs/2609.30037v1)
  > **TL;DR**: Evaluates robustness impact of INT8 quantization (PTQ/QAT) and 50% pruning on EEG decoders. Pruning reduces adversarial transfer efficiency, while PTQ maintains 95-98% prediction consistency with FP32.
* `quantization` `MLLM` `efficient-inference` [GHOST-Q: Towards Studying Grounding Hallucinations Overlooked Under Same-score TradeOffs in Quantized VLMS](http://arxiv.org/abs/2609.29999v1)
  > **TL;DR**: Evaluates INT8 and NF4 quantized VLMs (8B params) on grounding hallucinations, showing same accuracy but shifts in failures, with 10/36 significant effects in hallucination-sensitive tasks.
* `token-pruning` `efficient-inference` [When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression](http://arxiv.org/abs/2609.29875v1)
  > **TL;DR**: Compresses long-horizon agent reasoning history via Interaction Aware Compression (ICLR), reducing input/output/cache tokens by up to 33.3% while preserving task performance (reward 0.699→0.718).
* `compression` `efficient-inference` [Dense Coverage, Sparse Refinement: Byte-Constrained Cooperative Perception](http://arxiv.org/abs/2609.29456v1)
  > **TL;DR**: Efficient BEV feature compression for collaborative perception via coverage-refinement design with task-aware benefit selection. Achieves 0.60 AP@0.7 at 1.87 KB per agent vs 0.52 at 4.61 KB.
* `token-pruning` `efficient-inference` `MLLM` [Exploiting answer-invariant redundancies in satellite imagery for efficient VLM inference on edge](http://arxiv.org/abs/2609.29029v1)
  > **TL;DR**: Finds answer-invariant redundant tokens (AITR) in satellite VLM inference; prunes tiles & tokens via query-conditioned pruning & elastic prefill in LLaVA. Reduces energy 78%, latency 69%, ups accuracy to 73%.
* `quantization` `MLLM` `efficient-inference` [GHOST-Q: Towards Studying Grounding Hallucinations Overlooked Under Same-score TradeOffs in Quantized VLMS](http://arxiv.org/abs/2609.29999v1)
  > **TL;DR**: Evaluates PTQ effects on VLMs' grounding behavior under INT8/NF4, showing preserved accuracy but altered hallucinations and latency, with 10/36 significant paired effects on hallucination-sensitive tasks.
* `token-pruning` `efficient-inference` [When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression](http://arxiv.org/abs/2609.29875v1)
  > **TL;DR**: Reduces context length and inference cost in long-horizon agents by pruning historical reasoning. Uses Interaction Aware Compression for Long Horizon Reasoning (ICLR) to rank and remove reasoning blocks. Reduces input, output, and cache read tokens by 25.5%, 14.4%, and 33.3% while improving reward.
* `compression` `efficient-inference` [Less is More: Encoder-only Audio-Visual Segmentation](http://arxiv.org/abs/2609.29121v1)
  > **TL;DR**: Reducing redundant components in AVSS model for efficiency. Proposes encoder-only architecture (EASE), achieves 365 FPS (3x speedup over SotA) with comparable accuracy.
* `quantization` `compression` `efficient-inference` [AERIAL: Adversarial Evaluation of Robustness in Accuracy-Preserving Low-Precision EEG Decoders](http://arxiv.org/abs/2609.30037v1)
  > **TL;DR**: Analyzes EEG model robustness under accuracy-preserving INT8 PTQ/QAT and 50% pruning. Finds no direct robustness improvement, but PTQ maintains higher adversarial transfer (0.994/0.997) vs pruning. Validated with TensorRT deployment.
* `quantization` `MLLM` `efficient-inference` [GHOST-Q: Towards Studying Grounding Hallucinations Overlooked Under Same-score TradeOffs in Quantized VLMS](http://arxiv.org/abs/2609.29999v1)
  > **TL;DR**: Analyzes hallucination issues in INT8/NF4 VLMs, showing FP16 accuracy preserved but 10/36 grounding effects significant, with A100 profiling revealing latency-memory tradeoffs.
* `quantization` `efficient-inference` [Does per-frame early exit pay? A compute-matched study of dynamic depth for on-device speech enhancement](http://arxiv.org/abs/2609.29867v1)
  > **TL;DR**: Optimizes dynamic depth speech enhancement for on-device int8 inference, achieving 0.11 higher PESQ at equivalent compute or 30% less compute for same PESQ, with minimal latency overhead.
* `quantization` `compression` `efficient-inference` [Beyond Model Size: Redesigning LiSenNet for embedded speech enhancement](http://arxiv.org/abs/2609.29866v1)
  > **TL;DR**: Optimizes speech enhancement model for microcontroller NPUs via operator reformulation and int8 quantization, achieving PESQ 3.01 (vs 2.93 baseline) with 4.83ms latency per 16ms input.
* `quantization` `token-pruning` `efficient-inference` [FlashLoop: Fast and Memory-Efficient Looped Transformers via Lazy Updates](http://arxiv.org/abs/2609.29812v1)
  > **TL;DR**: Reduces redundancy in looped transformers via token-sparse updates and KV-residual quantization (low-bit) + sparse attention, achieving 6x memory reduction and 1.64x speedup.
* `compression` `efficient-inference` `MLLM` [Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs](http://arxiv.org/abs/2609.29382v1)
  > **TL;DR**: Efficient compute allocation for VLAs via decoupled early exits and KV cache synthesis, reducing latency by 79.2% and FLOPs by 31.8% while improving success rate.
* `compression` `efficient-inference` [TinyCardioUNet: IMU-to-ECG Translation with Graph-Encoded Inter-Axis Dependencies and Tensor Decomposition-Based Parameter Reduction](http://arxiv.org/abs/2609.29322v1)
  > **TL;DR**: Proposes a lightweight TinyCardioUNet for IMU-to-ECG translation using tensor decomposition for parameter reduction (36.0k parameters) and achieves RMSE 0.098.
* `token-pruning` `efficient-inference` `MLLM` [Exploiting answer-invariant redundancies in satellite imagery for efficient VLM inference on edge](http://arxiv.org/abs/2609.29029v1)
  > **TL;DR**: Efficient VLM inference by pruning answer-invariant tokens in satellite imagery. Proposes Rift for query-conditioned tile pruning and elastic prefill. 78% energy and 69% latency reduction for LLaVA-1.5 7B.
* `compression` `efficient-inference` [Automatic Rank Allocation for Low-Rank Adaptation in Large Language Models via lp Regularization](http://arxiv.org/abs/2609.28998v1)
  > **TL;DR**: Automates rank allocation in LoRA for LLMs via ℓp regularization, optimizing efficiency without manual tuning, achieving competitive performance on NLP tasks.
* `quantization` `efficient-inference` [Same Bit Width, Different Outcomes: Post-Training Quantization of Text-to-Speech Across Architectures](http://arxiv.org/abs/2609.28974v1)
  > **TL;DR**: Evaluates PTQ across TTS architectures, identifying model-specific sensitive components. 4-bit weights reduce UTMOS by 2.8 on Supertonic, with per-layer GPTQ restoring near-original quality. 4-bit kernels achieve 0.6x fp32 latency on Mac mini.

### 2026-09-23
* `compression` `efficient-inference` [LightMIS: Ultra-Lightweight Medical Image Segmentation Without a Stage-Wise Decoder](http://arxiv.org/abs/2609.28327v1)
  > **TL;DR**: Ultra-lightweight medical image segmentation model (LightMIS) reduces parameters by 90-99.6% and FLOPs by 82.5-96.1% via Scale-Aligned Projection and Adaptive Fusion Cascade, achieving 0.131M params and 0.575GFLOPs for a 3x256x256 input.
* `quantization` `efficient-inference` [RAMP: Robust Adaptive Mixed-Precision Quantization for Edge CPU Vision Models](http://arxiv.org/abs/2609.28262v1)
  > **TL;DR**: Proposes RAMP, a robust adaptive mixed-precision quantization method for edge CPU vision models, using Jensen-Shannon Divergence and K-Means clustering for layer-wise INT8 quantization. Achieves near-lossless accuracy with a mean 1.81× speed-up over full-precision models.
* `token-pruning` `efficient-inference` `compression` [Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces](http://arxiv.org/abs/2609.27988v1)
  > **TL;DR**: Develops a low-rank spectral pullback network (SPN) for task-sensitive token pruning, reducing depth error by 25% at 0.5 prune ratio with a 310K-parameter importance head.
* `quantization` `compression` `efficient-inference` [MicroQonv: Reshaping Convolution Tensors for Efficient Microscaling in Training and Inference](http://arxiv.org/abs/2609.28358v1)
  > **TL;DR**: Efficient microscaling quantization for conv layers via modified im2col + single quantization pass, reducing memory movement by ×7.53 and enabling 4-bit quantization with minimal accuracy loss.
* `compression` `token-pruning` `efficient-inference` [Stable Geometry with Divergent Task Evidence for Efficient Long-Horizon Agent Compression](http://arxiv.org/abs/2609.27332v1)
  > **TL;DR**: Efficient agent history compression via evidence-preserving token pruning. Geometry Guided Evidence Preserving Memory (GEM) reduces token usage by 21.4% (2.69M to 2.11M) while maintaining task reward by prioritizing task evidence over geometric redundancy.
* `compression` `efficient-inference` `MLLM` [KITE: KV-Invariant Transformer Expansion for Efficient Agentic LLM Scaling](http://arxiv.org/abs/2609.27294v1)
  > **TL;DR**: Reduces LLM inference costs via KV-invariant expansion, saving 6.7-31.6% inference cost at 2.15B active parameters using a two-tower decoder for efficient KV generation.
* `token-pruning` `efficient-inference` [DRSR: Learning Set-Level Deletion Risk for Efficient Long-Horizon Agents](http://arxiv.org/abs/2609.27276v1)
  > **TL;DR**: Problem: agent-history compression for efficient long-horizon agents. Method: Direct Relational Set-Risk Pruning (DRSR) for structured token deletion. Result: 20.82% fewer tokens while improving reward from 0.699 to 0.802.
* `quantization` `efficient-inference` [Predicting Quantization Price for Selecting PTQ Configurations Before Deployment](http://arxiv.org/abs/2609.28270v1)
  > **TL;DR**: Proposes a price-guided selection method for PTQ configurations to predict and minimize output-distribution drift before deployment, using error covariance and downstream curvature to optimize bit allocation and quantization parameters.
* `quantization` `efficient-inference` [RAMP: Robust Adaptive Mixed-Precision Quantization for Edge CPU Vision Models](http://arxiv.org/abs/2609.28262v1)
  > **TL;DR**: Proposes RAMP for mixed-precision INT8 quantization on edge CPUs using Jensen-Shannon Divergence for layer-wise sensitivity analysis, achieving near-lossless accuracy with 1.81x speed-up.
* `compression` `efficient-inference` [Tensor Decomposition of Transformer Key-Value Caches: Spectral Structure and Format Comparison](http://arxiv.org/abs/2609.28029v1)
  > **TL;DR**: Analyzes key-value cache as tensor, applies Tucker decomposition for 2-5x compression, achieves lowest error for values, identifies full-rank modes to leave uncompressed, post-RoPE keys lose 41-64% compressibility.
* `token-pruning` `efficient-inference` `compression` [Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces](http://arxiv.org/abs/2609.27988v1)
  > **TL;DR**: Proposes task-induced metrics for ViT feature spaces, enabling token pruning via a 310K-parameter importance head, reducing depth error by 25% at prune ratio 0.5.
* `compression` `efficient-inference` [Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery](http://arxiv.org/abs/2609.27980v1)
  > **TL;DR**: Prunes Whisper encoder by removing 6 layers (18.5%) based on WER sensitivity, achieving 20.1% WER post-distillation (vs 18.2% baseline) without custom inference code.
* `compression` `efficient-inference` [Attention Routing Stabilizes Early: Working-Set Inference for Recurrent Language Models](http://arxiv.org/abs/2609.27373v1)
  > **TL;DR**: Reduces recurrent LM inference cost by exploiting early attention stabilization; reuses sparse working-set context to limit computation; achieves 1.76× speedup at 4K context without losing performance.
* `efficient-inference` `compression` `quantization` [KITE: KV-Invariant Transformer Expansion for Efficient Agentic LLM Scaling](http://arxiv.org/abs/2609.27294v1)
  > **TL;DR**: Efficient agentic LLM scaling via KV-invariant expansion, reducing inference cost by 31.6% for a 67B MoE model with 2.15B active parameters per token.
* `compression` `efficient-inference` [NGN: Learning Neural Network Size as a Differentiable Count](http://arxiv.org/abs/2609.27291v1)
  > **TL;DR**: Problem: selecting optimal model size before training. Method: differentiable learning of structural component counts via learnable boundary; post-deployment discarding of unused components. Key result: learned prefixes perform similarly to fixed-size models of same size.
* `compression` `quantization` `efficient-inference` [Reliable Federated TinyML Deployment for IoT Security](http://arxiv.org/abs/2609.27202v1)
  > **TL;DR**: Federated TinyML for IoT security combines knowledge distillation, pruning, and quantization to reduce model size for resource-constrained devices, achieving 93.85% Attack Recall with stable training.

### 2026-09-22
* `token-pruning` `efficient-inference` [GTR: Gated Token Recurrence for Efficient Dense Prediction](http://arxiv.org/abs/2609.26590v1)
  > **TL;DR**: Proposes GTR, a softmax-free recurrent vision backbone with gated linear attention for efficient dense prediction, achieving 1.908ms latency with FP16 execution on RTX 4090 and 4x speedup in kernel benchmark.
* `token-pruning` `efficient-inference` `MLLM` [From Token Importance to Conditional Removability: Rethinking Visual Token Pruning in Multimodal Large Language Models](http://arxiv.org/abs/2609.26484v1)
  > **TL;DR**: Conditional token removability (not just importance) for visual token pruning in MLLMs; CoRePrune framework with perturbation-aware pruning and set-conditioned refinement; achieves 90.3% dense-model performance with 128 visual tokens (51% prefill time reduction).
* `quantization` `efficient-inference` [PP-Net: A Hybrid Physical-Prior Neural Network for Scattered Light Removal in Biomedical Images on Embedded Devices](http://arxiv.org/abs/2609.26474v1)
  > **TL;DR**: Proposes PP-Net for biomedical scattered light removal, optimized for embedded devices with INT8 quantization, achieving 200 ms latency per 512x512 image.
* `quantization` `token-pruning` `efficient-inference` [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](http://arxiv.org/abs/2609.26425v1)
  > **TL;DR**: 2-bit KV cache quantization for world models, QuantWM uses sensitivity-aware clustering and attention compensation to reduce flickering, achieving 6.20x memory compression with better quality than prior methods.
* `token-pruning` `efficient-inference` `MLLM` [Shallow to Deep: Aligning Token Pruning with Stage-wise Roles in LVLMs](http://arxiv.org/abs/2609.25635v1)
  > **TL;DR**: Reduces visual token redundancy in LVLMs via hierarchical pruning: spectral analysis (shallow), Gaussian-smoothed attention (intermediate), and stability-adaptive triggering (deep). Achieves 94.4% token reduction (+2.1% accuracy) and 3.9x speed-up on LLaVA-NeXT-7B.
* `quantization` `efficient-inference` `MLLM` [Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning](http://arxiv.org/abs/2609.26708v1)
  > **TL;DR**: Addresses reasoning degradation in sub-3-bit quantized models via on-policy distillation (OPD), improving BF16 performance retention from 35% to 70% on MATH-500 at 2.79/1.88 effective bits.
* `quantization` `efficient-inference` [PP-Net: A Hybrid Physical-Prior Neural Network for Scattered Light Removal in Biomedical Images on Embedded Devices](http://arxiv.org/abs/2609.26474v1)
  > **TL;DR**: Proposes PP-Net for scattered light removal in biomedical images, optimized for embedded devices with INT8 quantization, achieving ~200 ms inference latency per 512x512 image.
* `quantization` `efficient-inference` `MLLM` [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](http://arxiv.org/abs/2609.26425v1)
  > **TL;DR**: 2-bit KV cache quantization for video generation, using sensitivity-aware clustering and attention compensation to reduce visual degradation. Achieves 6.20x memory compression with improved temporal consistency.
* `token-pruning` `efficient-inference` [CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference](http://arxiv.org/abs/2609.26300v1)
  > **TL;DR**: KV cache bottleneck in LLM long-context inference. CompKV selects tokens based on compensation error impact, optimizing selection for mean compensation. Up to 6.85× speedup in self-attention over full attention.
* `compression` `efficient-inference` `MLLM` [You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs](http://arxiv.org/abs/2609.25809v1)
  > **TL;DR**: Performs dynamic expert pruning in fine-grained MoE LLMs, showing 66% expert pruning retains 98.8% unpruned performance, achieving 1.2-1.7x speedup.
* `compression` `efficient-inference` `MLLM` [Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference](http://arxiv.org/abs/2609.25537v1)
  > **TL;DR**: Compresses long LLM contexts into answer-aligned memory embeddings, reducing KV cache and GPU memory by 50% via query-guided selection and answer distillation, cutting inference time by 20%.
* `quantization` `MLLM` `efficient-inference` [Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning](http://arxiv.org/abs/2609.26708v1)
  > **TL;DR**: On-policy distillation addresses quantization-amplified exposure bias for sub-3-bit models, combining QAD and OPD to retain 70% of BF16 performance on MATH-500 and 91% on HumanEval at 1.88-2.79 bits.
* `token-pruning` `efficient-inference` [GTR: Gated Token Recurrence for Efficient Dense Prediction](http://arxiv.org/abs/2609.26590v1)
  > **TL;DR**: Proposes GTR, a softmax-free recurrent vision backbone for efficient dense prediction, reducing quadratic attention cost. Achieves 1.908ms latency on RTX 4090 with FP16 inference.
* `quantization` `efficient-inference` [PP-Net: A Hybrid Physical-Prior Neural Network for Scattered Light Removal in Biomedical Images on Embedded Devices](http://arxiv.org/abs/2609.26474v1)
  > **TL;DR**: PP-Net addresses efficient scattered light removal for biomedical images on embedded devices with INT8 quantization, achieving 200ms latency per 512x512 image.
* `quantization` `efficient-inference` `MLLM` [Disaggregated Quantization: Specializing LLM Prefill and Decode](http://arxiv.org/abs/2609.26333v1)
  > **TL;DR**: Optimizes LLM prefill and decode phases via disaggregated quantization (DQ), specializing compute formats and weights. Achieves 1.78x speedup at 8K prompt length with 2-3-bit decode, improving accuracy by 32.5 points on MMLU-Pro with NVFP4 prefiller.
* `token-pruning` `efficient-inference` `MLLM` [CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference](http://arxiv.org/abs/2609.26300v1)
  > **TL;DR**: Optimizes KV cache selection for long-context LLM inference by jointly considering token importance and compensation error, achieving 6.85× speedup over full attention via block-based token pruning.
* `compression` `efficient-inference` [GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression](http://arxiv.org/abs/2609.25963v1)
  > **TL;DR**: Solves transformer layer redundancy via geometry-preserving cross-layer factorization, achieving efficient structured sparsity without retraining, outperforming independent decompositions.
* `quantization` `efficient-inference` `MLLM` [Beyond Scalar Sensitivity: Activation-Aware Mixed-Precision LLM Quantization with Cross-Layer Refinement](http://arxiv.org/abs/2609.25916v1)
  > **TL;DR**: Addresses unreliable scalar proxies in mixed-precision LLM quantization by proposing CASA, an activation-aware, cross-layer method. Achieves lower perplexity at <3 bits/weight, with gains tied to condition numbers.
* `compression` `efficient-inference` `token-pruning` [You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs](http://arxiv.org/abs/2609.25809v1)
  > **TL;DR**: Fine-grained MoE LLMs enable dynamic expert pruning; retaining 2/3 of experts preserves 98.8% performance with 1.2-1.7x speedup, showing high expert redundancy.
* `quantization` `efficient-inference` `token-pruning` [Latest Exact Match Attention](http://arxiv.org/abs/2609.25802v1)
  > **TL;DR**: LEMA binarizes queries and keys in transformers for exact-match attention, reducing compute via binary ops (1-bit), enabling constant-time token retrieval, and matching half-sized softmax transformers' performance while maintaining inference speed.

### 2026-09-21
* `token-pruning` `efficient-inference` `MLLM` [SLICEChat: Progressive In-Encoder Token Pruning for Whole-Slide Pathology Language Models](http://arxiv.org/abs/2609.24894v1)
  > **TL;DR**: Efficient pathology MLLM with in-encoder token pruning via hybrid Mamba-Transformer encoder and language-supervised pruning, achieves 59.09-79.84% accuracy with competitive latency on gigapixel WSIs.
* `quantization` `efficient-inference` `MLLM` [SPHQuant: Efficient extreme low bit weight quantization for Vision-Language Models](http://arxiv.org/abs/2609.24875v1)
  > **TL;DR**: Proposes SPHQuant for extreme low-bit weight-only quantization of VLMs, using spherical decomposition and radius-direction isolation to handle outliers at 2-3 bits, improving decode throughput by 30.3% over QTIP.
* `compression` `efficient-inference` [DTKDP: A Dual Teacher Knowledge Distillation and Pruning Framework for Lightweight Oriented SAR Ship Detection](http://arxiv.org/abs/2609.24872v1)
  > **TL;DR**: Lightweight SAR ship detection via dual-teacher knowledge distillation and pruning, reducing Oriented R-CNN parameters by 87.5-91.8% and FLOPs by 75.6-79.9%, with minimal accuracy drop (0.65% improvement to 2.38% decrease).
* `quantization` `token-pruning` `MLLM` [ME-VLM:A Unified VLM for Embodied Cognition and Agent Coordination](http://arxiv.org/abs/2609.24526v1)
  > **TL;DR**: Combines visual token compression and W4A8 quantization for efficient deployment of a 4B model, reducing prefill latency from 400ms to 188ms on edge devices.
* `token-pruning` `efficient-inference` `MLLM` [VPRune: Efficient Training-free Pre-LLM Visual Token Pruning](http://arxiv.org/abs/2609.24485v1)
  > **TL;DR**: Training-free pre-LLM visual token pruning via diversity selection, token recycling, and position restoration reduces LVLM inference cost by 40% with minimal performance drop on FastVLM-1.5B.
* `quantization` `efficient-inference` `MLLM` [When Quantization Preserves Accuracy but Not Evidence: Explanation-Aware Post-Training Quantization for Medical LLMs](http://arxiv.org/abs/2609.24799v1)
  > **TL;DR**: Proposes explanation-aware PTQ to preserve rationale-quality in medical LLMs. Uses offline faithfulness cache & answer-supporting evidence tokens. W4A4KV4 quantization on 7B-8B LLMs better preserves rationale-to-answer support than accuracy-only baselines.
* `quantization` `compression` `efficient-inference` [NPU Accelerator: Quantized Real-Time Vehicle Detection on PYNQ-Z1 Using FINN](http://arxiv.org/abs/2609.24757v1)
  > **TL;DR**: Real-time vehicle detection via QAT, LP-YOLO Slim, with 4-bit weights and 2-bit activations, achieving 35.66 FPS, 12.25 FPS/W, and 0.594 mAP@0.5 on a PYNQ-Z1 board.
* `quantization` `compression` `efficient-inference` [QLoRA Fine-Tuning of Ministral LLM for Sequence-to-Function Protein Annotation](http://arxiv.org/abs/2609.24538v1)
  > **TL;DR**: Applies 4-bit QLoRA fine-tuning to Ministral 3 (3B) for protein annotation, reducing memory and compute costs while maintaining functional accuracy.
* `token-pruning` `efficient-inference` `MLLM` [VPRune: Efficient Training-free Pre-LLM Visual Token Pruning](http://arxiv.org/abs/2609.24485v1)
  > **TL;DR**: Efficient visual token pruning for LVLMs with diversity selection, token recycling, and position restoration, reducing inference latency on FastVLM-1.5B without retraining.
* `quantization` `efficient-inference` `MLLM` [FoldQuantVLA: Native Low-Bit Quantization of Vision-Language-Action Models via Consistent Folding](http://arxiv.org/abs/2609.24433v1)
  > **TL;DR**: Quantizes vision-language-action models to W4A4 & W8A8 via channel scaling, block Hadamard transforms, and per-token quantization, achieving 1.2-1.52x speedups on NVIDIA GPUs with 92.5% task success rate.
* `token-pruning` `efficient-inference` `MLLM` [ARM: Attention with Routed-Memory for Learnable Sparse Control](http://arxiv.org/abs/2609.24417v1)
  > **TL;DR**: KV cache memory issue in LLMs, learnable sparse memory with Gumbel-Softmax routing, reduces memory and latency while maintaining performance.
* `compression` `efficient-inference` [Artificial Structure Function Search: Preserving Artificial Functional Connectivity for Structured Pruning](http://arxiv.org/abs/2609.24401v1)
  > **TL;DR**: Structured pruning via Principle Gradient Importance for preserving functional connectivity, achieving 70% parameter reduction without re-training.
* `quantization` `efficient-inference` [The Undetected Damage of Quantization on Retrieval and How to Fix It](http://arxiv.org/abs/2609.24322v1)
  > **TL;DR**: Quantization alters 14-46% of top-1 retrieval results despite intact classification accuracy. Method: gap-based bit allocation for trusted queries. Recovers 0.75-bit benefit at half cost, with some inputs routed to full precision.
* `quantization` `compression` `efficient-inference` [KV-COBRA: KV Cache Compression via Co-Optimized Bit-Rank Allocation](http://arxiv.org/abs/2609.24298v1)
  > **TL;DR**: KV cache compression via co-optimized bit-rank allocation per attention head; combines low-rank projection and scalar quantization to minimize distortion. Achieves best accuracy at 0.5-4 bits per dimension vs. uniform allocation.
* `quantization` `efficient-inference` [vla.simd: Efficient CPU Inference for Language-Conditioned Manipulation](http://arxiv.org/abs/2609.24274v1)
  > **TL;DR**: The paper presents vla.simd, a CPU inference engine for language-conditioned policies, achieving 1.4× speedup over PyTorch, with IMPACT policy delivering 81.2 actions/s in int8 on Raspberry Pi 5.
* `compression` `quantization` `efficient-inference` [LEAP-NBV: Lightweight Edge Active-Perception for Foundation-Model Next-Best-View Planning](http://arxiv.org/abs/2609.23974v1)
  > **TL;DR**: Efficient edge deployment of foundation models via model distillation (32M student) and FP16 quantization, achieving 2.0x speedup and 3.0x lower energy with 12 ms latency for HMR.
* `token-pruning` `efficient-inference` `MLLM` [ARM: Attention with Routed-Memory for Learnable Sparse Control](http://arxiv.org/abs/2609.24417v1)
  > **TL;DR**: Efficient KV caching for LLMs via learnable sparse routing, avoiding hard eviction, reduces memory and latency; achieves superior performance on long-context reasoning benchmarks.
* `compression` `efficient-inference` [Artificial Structure Function Search: Preserving Artificial Functional Connectivity for Structured Pruning](http://arxiv.org/abs/2609.24401v1)
  > **TL;DR**: Proposes ASF-S for structured pruning via Principle Gradient Importance (PGI), preserving Artificial Functional Connectivity, achieves 70% parameter reduction without re-training pruned layers.
* `quantization` `efficient-inference` [NAVIR: Neuromorphic Audio-Visual Speech Recognition for Robust Human-Robot Interaction on Edge Hardware](http://arxiv.org/abs/2609.24391v1)
  > **TL;DR**: Efficient audio-visual speech recognition for edge devices via quantization-aware training and factorized modules, achieving 14.0% WER under noise with on-board energy savings over 100x compared to GPU.
* `compression` `efficient-inference` [Prescriptive SVD-Inspired Attention via Spectral Energy Retention](http://arxiv.org/abs/2609.24370v1)
  > **TL;DR**: Reduces self-attention complexity via spectral energy retention, pruning 24.5-53.7% of score directions, cutting 2.6-4.3% parameters and 2.8-5.4% MACs with negligible accuracy change.
* `quantization` `efficient-inference` [The Undetected Damage of Quantization on Retrieval and How to Fix It](http://arxiv.org/abs/2609.24322v1)
  > **TL;DR**: Quantization alters retrieval results; propose a gap-based method to decide trustworthiness and allocate extra bits, recovering up to three-quarters of a bit's benefit for half the cost.
* `compression` `quantization` `efficient-inference` [KV-COBRA: KV Cache Compression via Co-Optimized Bit-Rank Allocation](http://arxiv.org/abs/2609.24298v1)
  > **TL;DR**: Optimizes KV-cache compression by co-optimizing rank and bit-width per attention head via quantization and low-rank projection, achieves best accuracy at 0.5-4 bits per dimension with minimal overhead.
* `quantization` `compression` `efficient-inference` [Q-DEQ: Discrete Solving and Quantization for Deep Equilibrium Models in Time Series Forecasting under Edge Deployment Coding Constraints](http://arxiv.org/abs/2609.24042v1)
  > **TL;DR**: Proposes Q-DEQ for efficient deep equilibrium models via discrete solving and W8A8 quantization, reducing parameters by 1.8-3.8x and static weight storage by 4.3-12.8x with minor MSE impact.

### 2026-09-20
* `compression` `efficient-inference` [VGGT-Prime: Compute-Adaptive Mixture-of-Heads for Efficient Visual Geometry Transformers](http://arxiv.org/abs/2609.23733v1)
  > **TL;DR**: Reduces architectural redundancy in visual geometry transformers via compute-adaptive mixture-of-heads, achieving 8x speedup, complementary to token merging for 14x total speedup.
* `token-pruning` `efficient-inference` `MLLM` [Layer-Aware Position Embeddings for Visual Token Pruning in Multimodal Large Language Models](http://arxiv.org/abs/2609.23715v1)
  > **TL;DR**: Reduces MLLM inference cost via visual token pruning with layer-aware position embeddings, switching between sparse/continuous embeddings per layer, improving multimodal performance while pruning.
* `compression` `efficient-inference` [LiteTex-GS: Fast and Lightweight Texturing for Gaussian Splatting](http://arxiv.org/abs/2609.23380v1)
  > **TL;DR**: Addresses high memory and computational costs in Gaussian Splatting via compact texturing and contribution-aware pruning, reducing parameters and training time while maintaining rendering quality.
* `token-pruning` `efficient-inference` [RegVGGT: Sustainable Visual Geometry Grounding for Streaming via Regulated Memory](http://arxiv.org/abs/2609.23286v1)
  > **TL;DR**: Addresses GPU memory inflation in streaming 3D reconstruction by regulating token updates, admitting only 1% tokens per frame, enabling thousand-frame processing on consumer GPUs with minimal quality loss.
* `quantization` `compression` `efficient-inference` [On the Efficiency-Safety Dilemma in Large Reasoning Models](http://arxiv.org/abs/2609.23587v1)
  > **TL;DR**: Explores the trade-off between efficiency (quantization/pruning) and adversarial robustness in large reasoning models, finding joint quantization-pruning optimal for balance. INT8/INT4 quantization studied, showing superficial safety gains but actual reasoning capability loss.
* `quantization` `efficient-inference` [ARID: A Deployable Edge AI System for Structured Information Extraction from Industrial Maintenance Work Orders](http://arxiv.org/abs/2609.23582v1)
  > **TL;DR**: Efficient structured information extraction on edge devices using 4-bit inference, achieving 82.9% token-F1 on Jetson Orin NX with 5,310 ms P50 latency at 12.5 W.
* `efficient-inference` `token-pruning` `MLLM` [ValueDiff: Value-Geometric KV Cache Eviction for Sink-Suppressed LLMs](http://arxiv.org/abs/2609.23314v1)
  > **TL;DR**: KV cache eviction for efficient LLM inference via value-vector dispersion ranking, achieving 92% retention at 4k budget on LongBench with sink-suppressed models.
* `quantization` `compression` `efficient-inference` [Global Ranks Survive, Selected Heads Shift: BOS-Sink Topology under 4-bit Weight-Only Quantization](http://arxiv.org/abs/2609.23585v1)
  > **TL;DR**: Analyzes 4-bit NF4 weight-only PTQ for LMs, showing global rank preservation (ρₛ≥0.980) but top-k head selection shifts (Jaccard 0.619-0.793), with layerwise drift up to 7.9x, highlighting need for post-quantization revalidation in sink-aware deployment.
* `quantization` `efficient-inference` [ARID: A Deployable Edge AI System for Structured Information Extraction from Industrial Maintenance Work Orders](http://arxiv.org/abs/2609.23582v1)
  > **TL;DR**: Deploys 4-bit inference for structured information extraction on edge devices (Jetson Orin NX), achieving 82.9% token-F1 at 5,310ms P50 latency with 12.5W power.
* `token-pruning` `efficient-inference` [ValueDiff: Value-Geometric KV Cache Eviction for Sink-Suppressed LLMs](http://arxiv.org/abs/2609.23314v1)
  > **TL;DR**: Key-value cache eviction in LLMs with value-geometric scores, achieving 88-99% dense retention at 2k token budget, outperforming prior methods by up to 20 points.

### 2026-09-19
* `compression` `efficient-inference` `quantization` [SparkDiffusion: Mitigating the High-Sparsity Trap --- A Unified Framework for up to $265\times$ Single-GPU Acceleration of Visual Generation](http://arxiv.org/abs/2609.23153v1)
  > **TL;DR**: Addresses high-sparsity trap in video diffusion transformers with sparse warm-up, distillation, and FP8 quantization, achieving 97% sparsity and 265x speedup for 720P generation.
* `token-pruning` `efficient-inference` `MLLM` [MM-ContextFold: Context Folding for Multimodal Agentic Retrieval](http://arxiv.org/abs/2609.23121v1)
  > **TL;DR**: Reduces context explosion in multimodal agentic retrieval by discarding redundant raw images after textualization, improving accuracy by 6.3% and cutting context length by 27.5%.
* `compression` `efficient-inference` [Compressing 3D Gaussian Splatting via Cross-Representation Priors](http://arxiv.org/abs/2609.23005v1)
  > **TL;DR**: Problem: High storage costs in 3D Gaussian Splatting. Method: Cross-representation priors optimize anchor-level entropy modeling. Result: 30% bitrate reduction vs. baselines while preserving rendering quality.
* `token-pruning` `efficient-inference` `MLLM` [MM-ContextFold: Context Folding for Multimodal Agentic Retrieval](http://arxiv.org/abs/2609.23121v1)
  > **TL;DR**: Reduces multimodal context explosion by dynamically loading and discarding visual tokens, retaining only textual summaries; cuts working context length by 27.5% while improving accuracy by 6.3%.
* `efficient-inference` `token-pruning` [Block-Sparse Attention with Semantic-Geometric Decoupled Routing](http://arxiv.org/abs/2609.22884v1)
  > **TL;DR**: Efficient block-sparse attention for long-context LLMs with semantic-geometric decoupled routing; achieves 5.03x speedup over FlashAttn at 128K context length.
* `quantization` `efficient-inference` `MLLM` [Towards Full Pipeline FP8 Reinforcement Learning for LLMs](http://arxiv.org/abs/2609.22870v1)
  > **TL;DR**: Addresses FP8 training instability in LLM reinforcement learning by proposing Calibrated Clipping to align FP8 bounds with BF16 distributions, restoring performance comparable to BF16 baseline.
* `quantization` `efficient-inference` [Real-Time Plasma State Prediction via FPGA-Accelerated Quantized Recurrent Probabilistic Neural Networks](http://arxiv.org/abs/2609.23141v1)
  > **TL;DR**: FPGA-accelerated real-time plasma state prediction using quantized RPNN via QKeras, achieving sub-10μs latency with resource-efficient deployment on Xilinx Alveo U50.
* `quantization` `efficient-inference` [Perplexity Cost Understates What Activation Quantisation Breaks](http://arxiv.org/abs/2609.23125v1)
  > **TL;DR**: Analyzes activation quantization impact on perplexity vs. specific tasks, showing retrieval degrades faster than induction; proposes rotation-based quantization, achieving 0.968 induction accuracy at 4 bits.
* `quantization` `efficient-inference` `MLLM` [Towards Full Pipeline FP8 Reinforcement Learning for LLMs](http://arxiv.org/abs/2609.22870v1)
  > **TL;DR**: Fixes FP8 RL training instability in LLMs by aligning clipping bounds with BF16 distributions, achieving stable performance comparable to BF16 baselines for models up to 32B.

### 2026-09-18
* `quantization` `efficient-inference` [ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](http://arxiv.org/abs/2609.21712v1)
  > **TL;DR**: Proposes W8A8 quantization for a real-time autonomous-driving world model, achieving 107.7× speedup over original teacher model while retaining 90% PSNR.
* `quantization` `efficient-inference` [Quantization-Aware Kalman Estimation for Diffusion Sampling](http://arxiv.org/abs/2609.21407v1)
  > **TL;DR**: Addresses sampling errors in W4A4 quantized diffusion models with a plug-and-play Kalman estimator (QuAKE) for trajectory-aware correction, reducing distributional discrepancy.
* `compression` `efficient-inference` [Accelerating Dense LLMs via L0-regularized Mixture-of-Experts](http://arxiv.org/abs/2609.21672v1)
  > **TL;DR**: L0-regularized Mixture-of-Experts (L0-MoE) reduces dense LLM inference cost by 2.5x via sparsity and dynamic batching without performance loss.
* `quantization` `efficient-inference` `MLLM` [SpecQuant: Speculative Decoding with Multi-Parent Quantization for Adaptive LLM Inference](http://arxiv.org/abs/2609.21704v1)
  > **TL;DR**: Combines speculative decoding with multi-parent INT4/FP8/FP16 quantization for adaptive LLM inference, achieving 35-43% speedups without >2% accuracy drop on Qwen2.5 models.
* `quantization` `efficient-inference` `MLLM` [Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals](http://arxiv.org/abs/2609.21450v1)
  > **TL;DR**: LLM W4A4 quantization challenge from activation outliers solved via error decomposition into weight compensation and orthogonal residuals, using Hadamard rotation and scaling. Achieves competitive results on Llama/Mistral models without backprop.
* `efficient-inference` `compression` [TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching](http://arxiv.org/abs/2609.21172v1)
  > **TL;DR**: Reduces KV-cache memory bottleneck in mobile LLMs via predictive multi-tier caching (exact, low-rank, flash-offloaded tiers), achieving 12.5-34% RAM reduction and 17.6x prefill throughput improvement while maintaining accuracy.

### 2026-09-17
* `compression` `efficient-inference` [PhGS: Post-Hoc Pruning and Refinement of Single-View Feed-Forward 3D Gaussian Reconstructions](http://arxiv.org/abs/2609.20623v1)
  > **TL;DR**: Reduces spatial redundancy in single-view 3D Gaussian Splatting via post-hoc pruning and recurrent refinement, achieving high memory reduction while preserving rendering fidelity without retraining.
* `quantization` `compression` `efficient-inference` [Cross-Architecture Foundation-Model Distillation for Edge Flood Segmentation](http://arxiv.org/abs/2609.20441v1)
  > **TL;DR**: Distills 300M Prithvi-EO-2.0 into 0.7M EfficientViT-B0 for edge deployment; uses quantization-aware training to achieve INT8 (1.5MB) with 5.57ms/image and 14MB memory on Jetson Xavier NX.
* `compression` `efficient-inference` [A Smaller Transformer in Your Transformer](http://arxiv.org/abs/2609.20100v1)
  > **TL;DR**: Reduces Transformer depthwise redundancy by fusing contiguous layers into surrogate layers (TWT), halving depth while maintaining performance, reducing parameters and compute without degradation.
* `token-pruning` `MLLM` `efficient-inference` [QCPruner: Query-Conditioned Population Coverage for Visual Token Pruning](http://arxiv.org/abs/2609.19990v1)
  > **TL;DR**: Efficient token pruning for MLLMs with query-conditioned utility weighting, retaining 96.1% performance at 32/576 tokens on LLaVA-1.5-7B.
* `token-pruning` `efficient-inference` `MLLM` [Region-Level Policy Optimization for Fine-grained MLLM Perception](http://arxiv.org/abs/2609.19745v1)
  > **TL;DR**: Proposes Vision-RL2 for MLLM token efficiency, using reinforcement learning to optimize region proposals and prune background tokens, achieving ~4x fewer visual tokens without accuracy loss.
* `efficient-inference` `token-pruning` [Understanding and Exploiting Diagonal Attention Sparsity in Autoregressive Image Generation](http://arxiv.org/abs/2609.19702v1)
  > **TL;DR**: Reduces attention computation in autoregressive image generation by exploiting diagonal sparsity, achieving 3.1x throughput with <2% quality drop.
* `quantization` `efficient-inference` `MLLM` [MiX: Micro-Inverted-Scaling for End-to-End Low-Bit Vision-Language Model Acceleration](http://arxiv.org/abs/2609.19683v1)
  > **TL;DR**: Proposes Micro-Inverted-Scaling (MiX) for end-to-end 4.5-bit VLM quantization, handling outliers via shared mantissa grouping, achieving 2.3-4.5x speedup and 1.4-2.9x energy reduction vs. prior work while maintaining accuracy.
* `quantization` `compression` `efficient-inference` [Cross-Architecture Foundation-Model Distillation for Edge Flood Segmentation](http://arxiv.org/abs/2609.20441v1)
  > **TL;DR**: Distills a 300M Prithvi-EO-2.0 teacher to a 0.7M EfficientViT-B0 student, then quantizes to INT8 (1.5MB), achieving 5.57ms inference per 512x512 image on Jetson Xavier NX.

### 2026-09-16
* `compression` `efficient-inference` [PULSE: Unlocking Practical Image Compression on Single-Thread CPU](http://arxiv.org/abs/2609.18602v1)
  > **TL;DR**: Proposes PULSE, a practical image codec for CPU-constrained devices with a low-complexity neural receiver (5.2 kMAC/pixel) and efficient entropy coding, decoding 1080p images in 126 ms on a single CPU thread, matching HM compression performance.
* `token-pruning` `efficient-inference` [Decoder-Agnostic Token Merging for Vision Transformers: A Systematic Study of G2TM](http://arxiv.org/abs/2609.18279v1)
  > **TL;DR**: Proposes Graph-Guided Token Merging (G2TM) for Vision Transformers, systematically evaluating across various decoders. Reduces GFLOPs by 22-47% and increases throughput by 74% on ADE20K, with minimal accuracy drop.
* `compression` `efficient-inference` [Unified Response Geometry for Structured Pruning](http://arxiv.org/abs/2609.18239v1)
  > **TL;DR**: Proposes structured pruning via joint response capacity selection, achieving 67.7% Top-1 accuracy on ImageNet ResNet-50 at 40% pruning without fine-tuning.
* `token-pruning` `efficient-inference` `compression` [Position Anchor Tuning: Towards Efficient Adaptation of Pre-Trained Point Cloud Transformers](http://arxiv.org/abs/2609.18056v1)
  > **TL;DR**: Improves inference efficiency of point cloud transformers via token aggregation-expansion pairs (TAM-TEM), reducing computation-heavy MHA/FFN blocks. Achieves comparable performance with lower computational overhead and fewer trainable parameters.
* `efficient-inference` `token-pruning` `MLLM` [rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model Inference](http://arxiv.org/abs/2609.19104v1)
  > **TL;DR**: Reduces VLA model latency by reusing visual tokens and neuron activations via dual-phase cache, maintaining success rates while achieving 1.29-1.42x speedup on robotic tasks.
* `compression` `efficient-inference` [Higher-order pruning of experts in mixture-of-experts language models](http://arxiv.org/abs/2609.18916v1)
  > **TL;DR**: Problem: MoE model parameter reduction in 122B-scale models. Method: Higher-order expert pruning (HOPE) preserves cooperative interactions. Result: At 50% pruning rate, HOPE achieves 1.58 avg rank (vs 2.42 baseline) with +6.1% gain on agentic coding.
* `quantization` `efficient-inference` `compression` [The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](http://arxiv.org/abs/2609.18063v1)
  > **TL;DR**: Efficient serving of 35B MoEs via SSD offloading with trained routing prediction and 4-bit quantization, achieving 20tok/s with 3GiB peak memory, close to fp16 accuracy.
* `compression` `efficient-inference` [Higher-order pruning of experts in mixture-of-experts language models](http://arxiv.org/abs/2609.18916v1)
  > **TL;DR**: Prunes Mixture-of-Experts models via second-order objective (HOPE) preserving expert cooperation. Achieves best rank (1.58) at 50% pruning, +6.1% gain on agentic coding.
* `quantization` `efficient-inference` `compression` [Colla-Q: Toward Collaborative Experts in MoE Quantization via Minimax Precision Balancing](http://arxiv.org/abs/2609.18131v1)
  > **TL;DR**: Quantization of MoE models with activation-entropy-based bit allocation to balance expert performance, maintaining robustness and reducing calibration dataset dependence.
* `quantization` `efficient-inference` [A Calibrated Instrument for Measuring How Inference Optimizations Affect Output Quality](http://arxiv.org/abs/2609.18005v1)
  > **TL;DR**: Proposes a calibrated method to measure quality impact of LLM optimizations. Tests 4-bit and 3-bit quantization, showing 4-bit matches 16-bit baseline, while 3-bit loses 0.5-1.1 points across domains. Also compares early-exit methods, revealing domain-dependent quality drops.

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

