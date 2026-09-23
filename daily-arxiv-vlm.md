
<div align="center">

# Daily Arxiv Papers on Efficient Vision & Multimodal Models

![Static Badge](https://img.shields.io/badge/total_papers-134-blue?logo=gitbook)
![Static Badge](https://img.shields.io/badge/update-2026.09.22-red?logo=fireship)
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

