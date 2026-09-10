
<div align="center">

# Daily Arxiv Papers on Efficient Vision & Multimodal Models

![Static Badge](https://img.shields.io/badge/total_papers-24-blue?logo=gitbook)
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
`vision-encoder` `visual-perception` `MLLM` `CLIP` `zero-shot` `retrieval`

---
### 2026-09-09
* `MLLM` `visual-perception` `zero-shot` [Spot-the-shift: Evaluating Grounded Image Difference Captioning of Long-term Changes](http://arxiv.org/abs/2609.10356v1)
  > **TL;DR**: Evaluates MLLMs on grounded image difference captioning for long-term scene changes. Proposes benchmark with spatial masks and new protocol. MLLMs struggle with fine-grained multi-image spatial understanding, and synthetic data improves performance without harming generalization.
* `MLLM` `efficient-inference` `token-pruning` [Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs](http://arxiv.org/abs/2609.10355v1)
  > **TL;DR**: Survey of inference-efficiency mechanisms for VideoLLMs to reduce computation, memory, and token count. Covers methods like frame sampling and token reduction across pipeline stages. Compares reported accuracy-cost tradeoffs under shared evaluation protocols.
* `token-pruning` `efficient-inference` `MLLM` [Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs](http://arxiv.org/abs/2609.10346v1)
  > **TL;DR**: Problem: Fixed vision token pruning strategies in MLLMs underutilize sample-wise complementarity. Method: VIP-Router adaptively selects optimal pruning strategy per input using lightweight routing. Result: 26.9% relative improvement in average accuracy on pruning-sensitive benchmarks.
* `compression` `efficient-inference` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Problem: High cost of iterative retraining in deep active learning. Method: Integrate magnitude pruning into each active learning cycle (improve & prune) to get sparse models for free. Result: Sparse models match dense counterparts at 95% sparsity.
* `token-pruning` `efficient-inference` `visual-perception` [TRACE: Trajectory-robust Admission with Evidence Ordering for Efficient GUI Agents](http://arxiv.org/abs/2609.10297v1)
  > **TL;DR**: Problem: GUI agents have high latency from accumulating screenshots. Method: Training-free visual token pruning with trajectory-robust admission and coverage-aware ordering. Result: Effective under tight budgets across six GUI benchmarks.
* `vision-encoder` `CLIP` `zero-shot` [Isotropic Embedding Perturbations for Robust Vision Language Encoders](http://arxiv.org/abs/2609.10292v1)
  > **TL;DR**: Improves vision-language encoder training by introducing Aether, an isotropic embedding perturbation method, which outperforms advanced pixel-level augmentations on multimodal alignment and recognition tasks with consistent gains.
* `CLIP` `retrieval` `visual-perception` [UOT-Gap: A Variational Principle for the Modality Gap in Vision-Language Models via Unbalanced Optimal Transport](http://arxiv.org/abs/2609.10224v1)
  > **TL;DR**: Analyzes modality gap in vision-language models using unbalanced optimal transport. Proposes UOT-Gap as a training-free diagnostic for modality alignment. Achieves mean absolute Spearman correlation of 0.973 for tracking retrieval degradation across datasets.
* `efficient-inference` `vision-encoder` `visual-perception` [ScopeMamba-YOLO: Widening the Perceptual Scope Inward and Outward for Small Object Detection in Remote Sensing Imagery](http://arxiv.org/abs/2609.10156v1)
  > **TL;DR**: Improves small object detection in remote sensing by decoupling contextual modeling from convolution with off-path selective scanning. Achieves 50.8% mAP50 with 3.57M parameters, exceeding YOLOv8s by 10.8 pp with 32% parameters.
* `compression` `efficient-inference` `vision-encoder` [Elastoformer: Enabling Dynamic Adaptivity via Elastic Model Transformation](http://arxiv.org/abs/2609.10018v1)
  > **TL;DR**: Problem: DNNs lack flexibility for dynamic edge constraints. Method: Elastoformer, a framework for elastic inference that adapts computational flow at runtime. Result: Achieves up to 85% FLOPs reduction and 50% latency reduction.
* `efficient-inference` `vision-encoder` `retrieval` [Beyond Similarity: Foundation Models as an Efficient Backbone for Training-Free Composed Video Retrieval](http://arxiv.org/abs/2609.10008v1)
  > **TL;DR**: Proposes an efficient training-free framework for composed video retrieval by adaptively using foundation models, achieving 89.55 R@1 on Dense-WebVid-CoVR with +35% margin over counterparts.
* `efficient-inference` `vision-encoder` `visual-perception` [CLFTv2: Efficient Camera-LiDAR Fusion for Semantic Segmentation via Hierarchical Feature Pyramids](http://arxiv.org/abs/2609.09881v1)
  > **TL;DR**: Efficient semantic segmentation for autonomous driving by replacing global ViT attention with Swin-based hierarchical fusion. Achieves 1.4× fewer GFLOPs and 2.2× higher throughput compared to Mask2Former adaptation while improving VRU recall.
* `MLLM` `visual-perception` `zero-shot` [From Pixels to Hierarchical Sequences: Quadtree Mask Encoding for Vision-Language Binary Change Detection](http://arxiv.org/abs/2609.09876v1)
  > **TL;DR**: Improves dense change detection in MLLMs by encoding binary masks as quadtree sequences with chain-of-thought reasoning, achieving 78.31% F1 and outperforming decoder-based methods.
* `MLLM` `efficient-inference` `visual-perception` [Show-Harness: Just a VLM Agent Can Play Robots](http://arxiv.org/abs/2609.10522v1)
  > **TL;DR**: Problem: Deploying VLMs for robot control is challenging. Method: Show-Harness uses a semantic interface to link VLM intent to robot actions, enabling zero-shot control and efficient fine-tuning. Result: Outperforms representative agentic and VLA paradigms.
* `vision-encoder` `MLLM` `visual-perception` [Can Foundation Models Moderate Online Content? Evaluating Instruction- vs. Example-Driven Policy Operationalization](http://arxiv.org/abs/2609.10410v1)
  > **TL;DR**: Evaluates if Vision-Language Models (VLMs) can moderate online content by comparing instruction- vs example-driven policy guidance. On ModerationBench, VLMs nearly tripled the F1 score (0.60 vs 0.22) of a deployed system.
* `token-pruning` `efficient-inference` `MLLM` [Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs](http://arxiv.org/abs/2609.10346v1)
  > **TL;DR**: Problem: Fixed token pruning strategies for MLLMs fail to exploit sample-wise complementarity. Method: VIP-Router adaptively selects optimal pruning strategy per input. Result: 26.9% relative improvement in accuracy over best fixed strategy baseline.
* `efficient-inference` `MLLM` `visual-perception` [From Symbolic Perception to Logical Deduction: A Framework for Guiding Language Models in Geometric Reasoning](http://arxiv.org/abs/2609.10335v1)
  > **TL;DR**: Replaces computationally intensive multimodal models with a LLM aided by a geometric symbol parser for geometry reasoning, achieving performance comparable to Gemini 2.5 Pro but with clearer, more efficient solutions.
* `compression` `token-pruning` `efficient-inference` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Integrates iterative magnitude pruning into active learning cycles to yield sparse models. Matches dense model accuracy at 95% sparsity, addressing computational bottlenecks in retraining and scoring.
* `MLLM` `visual-perception` `zero-shot` [Beyond Surface Imitation: Contrastive Modeling for Reasoning Path Alignment in Multimodal In-Context Learning](http://arxiv.org/abs/2609.10177v1)
  > **TL;DR**: Problem: Multimodal ICL struggles with reasoning path alignment. Method: Contrastive demonstration modeling with response-conditioned retrieval. Result: Notable gains on VQA tasks.
* `zero-shot` `visual-perception` [A statistical approach to bias in zero-shot learning: the lens of handwriting recognition](http://arxiv.org/abs/2609.10084v1)
  > **TL;DR**: Addresses bias in generalized zero-shot learning for handwriting recognition. Uses a two-stage hierarchical approach with statistical bias correction. Achieves over 20% relative accuracy improvement on unseen classes.
* `compression` `efficient-inference` `vision-encoder` [Elastoformer: Enabling Dynamic Adaptivity via Elastic Model Transformation](http://arxiv.org/abs/2609.10018v1)
  > **TL;DR**: Problem: Fixed DNN architectures cannot adapt to dynamic edge constraints. Method: Elastoformer transforms networks into elastic models with runtime mode switching. Result: Achieves up to 85% FLOPs reduction and 50% latency reduction.
* `compression` `efficient-inference` `vision-encoder` [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](http://arxiv.org/abs/2609.10311v1)
  > **TL;DR**: Integrates magnitude pruning into active learning cycles to obtain sparse models matching dense accuracy at 95% sparsity, addressing computational bottlenecks in retraining and acquisition scoring for image classification.
* `token-pruning` `visual-perception` `vision-encoder` [CoGe-GCD: Reframing Generalized Category Discovery with Compositional Generalization](http://arxiv.org/abs/2609.10158v1)
  > **TL;DR**: Improves Generalized Category Discovery by structuring patch tokens into primitive vocabulary via competitive assignment and information passing. Achieves better accuracy and geometric quality with marginal computational overhead.
* `visual-perception` `zero-shot` `retrieval` [Vague2Detect: Handling Ambiguous Prompts in Knowledge-Based Open-World Detection](http://arxiv.org/abs/2609.09949v1)
  > **TL;DR**: Problem: Open-world object detectors struggle with ambiguous language prompts. Method: Hybrid pipeline using KB retrieval and LLM-generated candidates to guide YOLO-World detections. Result: Improves Vague Prompt Success Rate from 32% to 61% (85% with GPT fallback).
* `quantization` `efficient-inference` `MLLM` [EFQ-Softmax: Exp-Free Quantization for Softmax](http://arxiv.org/abs/2609.09721v1)
  > **TL;DR**: Problem: Softmax quantization creates mismatch in low-bit attention. Method: EFQ-Softmax directly maps attention scores to low-bit probabilities using affine rules. Result: Improves Qwen3-VL nine-task mean from 0.7826 to 0.8000 and reduces kernel latency by 40.33%.

