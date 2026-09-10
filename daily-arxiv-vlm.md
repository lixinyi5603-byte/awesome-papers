
<div align="center">

# Daily Arxiv Papers on Efficient Vision & Multimodal Models

![Static Badge](https://img.shields.io/badge/total_papers-26-blue?logo=gitbook)
![Static Badge](https://img.shields.io/badge/update-2026.09.09-red?logo=fireship)
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
### 2026-09-09
* `compression` `efficient-inference` [AgroVisNet: A lightweight Convolutional Network and the BD-PlantDX Expert-Validated Benchmark for Radish, Potato and Pointed Gourd Disease Classification](http://arxiv.org/abs/2609.10469v1)
  > **TL;DR**: Proposes AgroVisNet, a lightweight CNN with grouped bottleneck residual blocks & attention for plant disease classification, achieving 99.52% accuracy with 290K parameters (8.7-16.8x fewer than baselines) & 0.46MB quantized size. Enables efficient CPU inference (8.4ms/image).
* `compression` `efficient-inference` `token-pruning` [Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs](http://arxiv.org/abs/2609.10355v1)
  > **TL;DR**: Survey on inference-efficiency mechanisms in VideoLLMs, focusing on reducing parameter count, FLOPs, latency, memory, and token count across frame sampling, modality encoding, and token reduction, with concrete efficiency metrics.
* `token-pruning` `efficient-inference` `MLLM` [Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs](http://arxiv.org/abs/2609.10346v1)
  > **TL;DR**: Adaptive visual token pruning for MLLMs via VIP-Router, improving average accuracy by 26.9% over fixed strategies by selecting optimal pruning per sample.
* `compression` `efficient-inference` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Integrates pruning into active learning cycles, achieving 95% sparsity without accuracy loss, reducing retraining and scoring bottlenecks.
* `token-pruning` `efficient-inference` `MLLM` [TRACE: Trajectory-robust Admission with Evidence Ordering for Efficient GUI Agents](http://arxiv.org/abs/2609.10297v1)
  > **TL;DR**: Reduces GUI agent inference cost via training-free visual token pruning and layout-aware evidence ordering, achieving efficient trajectory processing under tight token budgets.
* `compression` `efficient-inference` [LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting](http://arxiv.org/abs/2609.10095v1)
  > **TL;DR**: Stable mask-based pruning for 3D Gaussian Splatting reduces storage overhead. Linear increment activation maintains mid-confidence mask values for stable importance ranking. Achieves 3.6x/1.6x reduction over baselines while improving PSNR (+0.38 dB) on outdoor scenes.
* `efficient-inference` `compression` `quantization` [Elastoformer: Enabling Dynamic Adaptivity via Elastic Model Transformation](http://arxiv.org/abs/2609.10018v1)
  > **TL;DR**: Elastoformer enables dynamic adaptivity for edge inference by transforming standard models into elastic NNs, reducing FLOPs by 85% and latency by 50% while maintaining accuracy.
* `compression` `efficient-inference` [LightMedSeg-ISLES: Stroke Lesion Segmentation with 81x Fewer Parameters than nnU-Net](http://arxiv.org/abs/2609.09634v1)
  > **TL;DR**: Proposes LightMedSeg-ISLES, a 1.26M-parameter pipeline for stroke lesion segmentation that achieves 81.4x parameter reduction and 4.7x fewer FLOPs vs nnU-Net while retaining 97.5% of its Dice score.
* `token-pruning` `efficient-inference` `MLLM` [Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs](http://arxiv.org/abs/2609.10346v1)
  > **TL;DR**: Proposes VIP-Router to adaptively select vision token pruning strategies for MLLMs per input, improving average accuracy by 26.9% and reducing token cost vs fixed strategies.
* `compression` `efficient-inference` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Combines active learning and iterative magnitude pruning to yield 95% sparse models matching dense accuracy, addressing retraining and scoring bottlenecks.
* `compression` `efficient-inference` [RiLM: Parameter-Efficient Language Modeling via Geodesic Decoding](http://arxiv.org/abs/2609.10305v1)
  > **TL;DR**: Eliminates output matrix in small LMs via Riemannian geodesic decoding (shared embedding for I/O), reducing parameters (290k at d=128). Achieves 54.2 PPL on WikiText-2 (2x better than baselines) with hyperbolic manifold.
* `efficient-inference` `compression` [Elastoformer: Enabling Dynamic Adaptivity via Elastic Model Transformation](http://arxiv.org/abs/2609.10018v1)
  > **TL;DR**: Dynamic adaption to variable edge-device constraints via Elastoformer, enabling elastic inference with 85% FLOPs reduction, 50% lower latency, and 76% memory savings versus multiple fixed models for CNNs/ViTs.
* `token-pruning` `efficient-inference` `compression` [Structural Process Supervision for Latent Chain-of-Thought Reasoning](http://arxiv.org/abs/2609.09928v1)
  > **TL;DR**: Compresses chain-of-thought outputs by replacing explicit tokens with compact latent embeddings supervised by learnable prototypes, reducing token length by 50% on GSM8K-Aug while improving accuracy.
* `compression` `efficient-inference` `MLLM` [Forward-Free LLM Depth Pruning via Weight Redundancy](http://arxiv.org/abs/2609.09883v1)
  > **TL;DR**: Proposes Weight-Redundancy Pruning (WRP) for LLMs, eliminating calibration needs by using inter-layer weight similarity for Transformer block removal, matching activation-based pruning performance without forward passes.
* `efficient-inference` `quantization` `compression` [uFlowCSP: Crystal Structure Prediction using Mean flow generative models](http://arxiv.org/abs/2609.09799v1)
  > **TL;DR**: Accelerates crystal structure prediction by learning average probability-flow velocity with MeanFlow, reducing evaluations from thousands to 1-5, achieving 5x-58x speedup and matching/exceeding performance of existing methods.
* `efficient-inference` `compression` `MLLM` [Fine-Tuning a KV Cache Concatenation-Aware Model or Recomputing KV Caches? Why Not Both?](http://arxiv.org/abs/2609.09768v1)
  > **TL;DR**: Reduces KV cache overhead in long-context RAG systems by fine-tuning with KV cache concatenation awareness and selective recomputation, improving RULER score by 9.7 points and reducing TTFT by 80% for 124k-token inputs.
* `compression` `efficient-inference` [Looped GPT-BERT: Trading Parameters for Computation in Small Language Modeling](http://arxiv.org/abs/2609.09691v1)
  > **TL;DR**: Reduces parameters via depth-wise sharing in small LMs, achieving comparable performance on BLiMP/GLUE with 12.18M params vs baselines.
* `quantization` `efficient-inference` [Deep Learning-Based Detection of Electrical Faults and Power Quality Disturbances in Aerospace Power Systems](http://arxiv.org/abs/2609.10479v1)
  > **TL;DR**: Proposes a hardware-aware DL framework for aerospace power fault detection; uses compact ResNet with 8-bit quantization; achieves 95.87% accuracy and 6.90 ms latency on FPGA.
* `compression` `efficient-inference` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Integrates iterative magnitude pruning with active learning (I&P) to obtain sparse models (up to 95% sparsity) matching dense model accuracy, addressing computational bottlenecks in retraining and acquisition scoring.
* `compression` `efficient-inference` `MLLM` [Forward-Free LLM Depth Pruning via Weight Redundancy](http://arxiv.org/abs/2609.09883v1)
  > **TL;DR**: Proposes WRP, a forward-free LLM depth pruning method using weight redundancy analysis, achieving comparable performance to activation-based methods without calibration data or forward passes. Outperforms magnitude pruning across various settings.
* `efficient-inference` `compression` [uFlowCSP: Crystal Structure Prediction using Mean flow generative models](http://arxiv.org/abs/2609.09799v1)
  > **TL;DR**: Accelerates crystal structure prediction (CSP) via MeanFlow-based model reducing inference steps from 1000s to 1-5 evaluations; achieves 5x-58x speedup with equal/better accuracy (83.64% vs 78.34% at 20x fewer evaluations).
* `efficient-inference` `MLLM` [Fine-Tuning a KV Cache Concatenation-Aware Model or Recomputing KV Caches? Why Not Both?](http://arxiv.org/abs/2609.09768v1)
  > **TL;DR**: Reduces TTFT for long-context RAG by fine-tuning with KV cache concatenation-awareness and selective recomputation, improving accuracy by 9.7 points and cutting TTFT by 80%.
* `quantization` `efficient-inference` `MLLM` [EFQ-Softmax: Exp-Free Quantization for Softmax](http://arxiv.org/abs/2609.09721v1)
  > **TL;DR**: EFQ-Softmax enables low-bit probability generation in attention by direct mapping to E2M1 operands, avoiding exp-then-quantize mismatch. Improves Qwen3-8B seven-task mean to 0.6773 (vs. 0.6749) and reduces kernel latency by 40.33% on A5 vector unit.
* `efficient-inference` `quantization` `MLLM` [PELM: Power Efficient On-Device LLM Inference with Speculative Decoding and Dynamic Voltage Frequency Scaling](http://arxiv.org/abs/2609.09662v1)
  > **TL;DR**: Proposes PELM for power-efficient on-device LLM inference using speculative decoding and dynamic voltage frequency scaling, achieving 52.4% energy reduction and 23.1% speedup.
* `compression` `efficient-inference` [LightMedSeg-ISLES: Stroke Lesion Segmentation with 81x Fewer Parameters than nnU-Net](http://arxiv.org/abs/2609.09634v1)
  > **TL;DR**: Proposes LightMedSeg-ISLES for stroke lesion segmentation with 81.4x fewer params than nnU-Net, retaining 97.5% Dice score while reducing FLOPs by 4.7x per patch.
* `token-pruning` `efficient-inference` `MLLM` [TEFM: Token-Efficient Faithful Modeling for Structured Data](http://arxiv.org/abs/2609.09552v1)
  > **TL;DR**: Reduces token consumption by compressing structured data into compact Behavioral Code tokens, achieving ~1-2% token retention while maintaining accuracy and faithfulness in critical domains.

