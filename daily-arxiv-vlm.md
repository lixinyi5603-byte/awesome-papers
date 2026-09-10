
<div align="center">

# Daily Arxiv Papers on Efficient Vision & Multimodal Models

![Static Badge](https://img.shields.io/badge/total_papers-20-blue?logo=gitbook)
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
`MLLM` `CLIP`

---
### 2026-09-09
* `compression` `quantization` `efficient-inference` [AgroVisNet: A lightweight Convolutional Network and the BD-PlantDX Expert-Validated Benchmark for Radish, Potato and Pointed Gourd Disease Classification](http://arxiv.org/abs/2609.10469v1)
  > **TL;DR**: Lightweight CNN for plant disease classification using grouped bottleneck residual blocks and attention. Achieves 99.52% accuracy with 290K parameters, 8.7-16.8x smaller than baselines, and quantizes to 0.46MB with only 0.22% accuracy drop.
* `MLLM` `efficient-inference` `token-pruning` [Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs](http://arxiv.org/abs/2609.10355v1)
  > **TL;DR**: Survey of inference-efficiency methods for VideoLLMs, analyzing bottlenecks in frame sampling, modality encoding, and token reduction to reduce computation, memory, and token count for resource-constrained deployment.
* `token-pruning` `MLLM` `efficient-inference` [Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs](http://arxiv.org/abs/2609.10346v1)
  > **TL;DR**: Problem: Fixed visual token pruning strategies underperform on diverse inputs. Method: VIP-Router adaptively selects the best pruning strategy per sample using lightweight routing. Result: Achieves 26.9% relative improvement in average accuracy over fixed strategies.
* `compression` `efficient-inference` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Problem: High cost of iterative retraining in deep active learning. Method: Integrates magnitude pruning into each active learning cycle (Improve & Prune) to get sparse models as a byproduct. Result: Sparse models (up to 95% sparsity) match dense model accuracy.
* `token-pruning` `efficient-inference` `MLLM` [TRACE: Trajectory-robust Admission with Evidence Ordering for Efficient GUI Agents](http://arxiv.org/abs/2609.10297v1)
  > **TL;DR**: Addresses inference cost in GUI agents from accumulating high-resolution screenshots. Proposes a training-free framework for trajectory-robust visual token pruning and ordering, with monotone KV contraction. Achieves effective performance under tight token budgets on six GUI benchmarks.
* `CLIP` `MLLM` [UOT-Gap: A Variational Principle for the Modality Gap in Vision-Language Models via Unbalanced Optimal Transport](http://arxiv.org/abs/2609.10224v1)
  > **TL;DR**: Analyzes the modality gap in VLMs using Unbalanced Optimal Transport. Proposes UOT-Gap, a training-free diagnostic that models embeddings to explain retrieval performance degradation, achieving a mean Spearman correlation of 0.973.
* `compression` `efficient-inference` [LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting](http://arxiv.org/abs/2609.10095v1)
  > **TL;DR**: Prunes redundant primitives in 3D Gaussian Splatting to reduce storage and computational costs. Uses linear increment activation for stable mask training to improve importance ranking. Achieves 3.6x Gaussian reduction over baseline while maintaining rendering quality.
* `efficient-inference` `compression` `MLLM` [Elastoformer: Enabling Dynamic Adaptivity via Elastic Model Transformation](http://arxiv.org/abs/2609.10018v1)
  > **TL;DR**: Problem: Edge AI systems need models that adapt to dynamic resource constraints. Method: Elastoformer, a framework transforming NNs for elastic inference, dynamically switching operational modes at runtime. Result: Achieves up to 85% FLOPs reduction and 76% memory overhead reduction.
* `MLLM` `efficient-inference` `token-pruning` [Beyond Similarity: Foundation Models as an Efficient Backbone for Training-Free Composed Video Retrieval](http://arxiv.org/abs/2609.10008v1)
  > **TL;DR**: Addresses inefficient multimodal video retrieval by proposing an adaptive framework that uses foundation models with selective depth based on query difficulty, achieving up to 93.43 R@1 with efficient token selection and resolution adaptation.
* `quantization` `efficient-inference` [Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs](http://arxiv.org/abs/2609.10439v1)
  > **TL;DR**: FOM-UL enables robust LLM unlearning that withstands post-training quantization. It selectively updates layers to prevent forgotten knowledge from re-emerging after quantization. It maintains stronger utility than baselines under 4-bit and 8-bit PTQ with lower memorization recovery.
* `MLLM` `token-pruning` `efficient-inference` [Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs](http://arxiv.org/abs/2609.10346v1)
  > **TL;DR**: Proposes a sample-adaptive router (VIP-Router) for visual token pruning in MLLMs, selecting the best pruning strategy per input. Achieves 26.9% relative improvement in accuracy on VTC-Bench while adding only 0.017% parameters.
* `compression` `efficient-inference` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Combines active learning's iterative retraining loop with magnitude pruning to find sparse, high-performing subnetworks (winning tickets) at practically no extra cost. Achieves 95% sparsity while matching dense model accuracy, reducing compute for both retraining and acquisition scoring.
* `efficient-inference` `compression` `token-pruning` [Elastoformer: Enabling Dynamic Adaptivity via Elastic Model Transformation](http://arxiv.org/abs/2609.10018v1)
  > **TL;DR**: Problem: Fixed DNNs are inefficient under dynamic edge constraints. Method: Elastoformer transforms networks for real-time elastic inference, switching modes at runtime. Result: Achieves up to 85% FLOPs, 50% latency, and 76% memory reduction.
* `compression` `efficient-inference` [Forward-Free LLM Depth Pruning via Weight Redundancy](http://arxiv.org/abs/2609.09883v1)
  > **TL;DR**: Problem: Forward passes for activation-based LLM depth pruning are costly. Method: Weight-Redundancy Pruning (WRP) estimates inter-layer redundancy directly from weights without forward passes. Result: Outperforms existing forward-free methods and approaches activation-based performance.
* `compression` `efficient-inference` `MLLM` [Modality-Decoupled Federated Learning for Privacy-Preserving Embodied Intelligence in 6G](http://arxiv.org/abs/2609.09591v1)
  > **TL;DR**: Proposes modality-decoupled federated learning for vision-language-action models to address communication inefficiency and privacy. Includes modality-aware communication compression. Reduces per-client uplink payload by 95.6%.
* `compression` `efficient-inference` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Integrates magnitude pruning into active learning cycles to find sparse subnetworks without extra cost. The method yields models with 95% sparsity that match the accuracy of their dense counterparts at each AL iteration.
* `token-pruning` `efficient-inference` `MLLM` [CoGe-GCD: Reframing Generalized Category Discovery with Compositional Generalization](http://arxiv.org/abs/2609.10158v1)
  > **TL;DR**: Addresses compositional generalization in category discovery using token-primitive mapping for structured patch token grouping, reducing token complexity. Achieves improved accuracy with marginal computational overhead.
* `compression` `MLLM` `efficient-inference` [Forward-Free LLM Depth Pruning via Weight Redundancy](http://arxiv.org/abs/2609.09883v1)
  > **TL;DR**: Problem: High cost of forward passes for LLM depth pruning. Method: Forward-free pruning by measuring inter-layer weight redundancy from checkpoints. Result: Outperforms existing forward-free methods and approaches activation-based pruning performance across multiple models and tasks.
* `quantization` `token-pruning` `efficient-inference` [EFQ-Softmax: Exp-Free Quantization for Softmax](http://arxiv.org/abs/2609.09721v1)
  > **TL;DR**: Improves Transformer efficiency by quantizing softmax without exponentiation, directly mapping attention scores to low-bit probabilities. EFQ-Softmax achieves 40.33% latency reduction on A5 vector unit while maintaining Qwen3-VL nine-task mean score at 0.8000.
* `token-pruning` `efficient-inference` `MLLM` [TEFM: Token-Efficient Faithful Modeling for Structured Data](http://arxiv.org/abs/2609.09552v1)
  > **TL;DR**: Proposes TEFM to compress structured data into Behavioral Code tokens for LLMs, achieving token efficiency and faithfulness. Method jointly optimizes code-level and prediction-level fidelity. Achieves competitive accuracy with ~1-2% token retention in clinical/security domains.

