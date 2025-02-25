# Long-context GRPO (R1 Reasoning)
- URL: https://unsloth.ai/blog/grpo
- Added At: 2025-02-25 03:17:31
- [Link To Text](2025-02-25-long-context-grpo-(r1-reasoning)_raw.md)

## Summary
**摘要**：
本文介绍了Unsloth团队在长文本GRPO（Generative Reward Policy Optimization，生成式奖励策略优化）推理方面的最新进展，重点在于显著降低VRAM（显存）使用量。通过Unsloth高效GRPO算法，Qwen2.5 (1.5B)模型仅需5GB VRAM即可训练，相比之前的GRPO版本减少了2GB。该算法实现了10倍的上下文长度扩展，同时比其他GRPO LoRA/QLoRA实现（包括使用Flash Attention 2的实现）节省90%的VRAM。对于Llama 3.1 (8B)模型，在20K上下文长度下，使用TRL+FA2的标准GRPO设置需要510.8GB VRAM，而Unsloth的方法仅需54.3GB。Unsloth通过内存高效线性算法、梯度检查点（将中间激活值异步卸载到系统内存）以及与底层推理引擎（vLLM）共享GPU/CUDA内存空间等多种技术来减少VRAM使用。此外，文章还探讨了GRPO的数学原理及实现中发现的问题，包括KL散度的计算方式。最后，文章还介绍了Unsloth在vLLM推理选项方面的更新，包括支持FP8 KV缓存以减少KV缓存空间使用，以及可以直接在vLLM中运行Unsloth动态4bit量化模型。

**要点总结**：

1.  **Unsloth高效GRPO算法显著降低VRAM使用**：Unsloth团队提出的新算法能够在使用更少VRAM的情况下，实现更长的上下文长度，使得在消费级显卡上训练大型语言模型成为可能。该算法通过多种优化手段，包括内存高效线性算法、梯度检查点和内存共享，实现了VRAM使用量的显著降低。
2.  **内存高效线性算法**：通过使用`torch.compile`，该算法在减少内存使用的同时，提高了计算速度，特别是在处理长上下文和多轮生成时，效果更佳。
3.  **梯度检查点技术**：Unsloth利用其智能梯度检查点算法，通过将中间激活值异步卸载到系统内存，进一步节省了VRAM。这种方法虽然会带来约1%的速度损失，但可以大幅降低显存占用。
4.  **GRPO数学原理与实现问题**：文章深入探讨了GRPO的数学原理，特别是KL散度的计算方式，并指出了Hugging Face的TRL GRPO实现中可能存在的偏差。通过实验验证，发现移除detach操作会导致训练崩溃，需要进一步研究。
5.   **vLLM推理优化**：Unsloth实现了与vLLM的集成，允许直接在vLLM中运行动态4bit量化模型，并支持FP8 KV缓存，进一步优化了推理性能和资源利用率。同时，现在可以直接在vLLM中运行Unsloth动态4-bit量化，无需额外操作。
