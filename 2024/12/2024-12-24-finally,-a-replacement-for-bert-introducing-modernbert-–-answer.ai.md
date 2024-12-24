# Finally, a Replacement for BERT: Introducing ModernBERT – Answer.AI
- URL: https://www.answer.ai/posts/2024-12-19-modernbert.html
- Added At: 2024-12-24 05:38:03
- [Link To Text](2024-12-24-finally,-a-replacement-for-bert-introducing-modernbert-–-answer.ai_raw.md)

## Summary
**摘要**：
本文介绍了由Answer.AI和LightOn联合推出的ModernBERT系列模型，这是一个在速度和准确度上均优于BERT及其后继模型的最先进的自编码器模型。ModernBERT包含了近年来大型语言模型（LLMs）研究的多项改进，并且以BERT方式应用于模型中，包括架构更新和训练流程的优化。它是首个在训练数据中包含大量代码的自编码器模型，对比传统模型的512序列长度，ModernBERT的序列长度可达8192，并且具有超过6800万月下载量。

**要点总结**：

1. **速度与准确度的改进**：ModernBERT在保持与BERT基本结构相似的同时，进行优化与创新，实现更快速的处理速度与更高的性能，成为综合考虑实际应用场景的新标准模型。
2. **技术支持与优化**：为了提高在不同GPU上的性能，开发了一种折衷方法，确保ModernBERT在给定硬件限制下有最佳表现。训练数据多样性更高，相比传统的使用Wikipedia和Wikibooks的数据集，ModernBERT采用更丰富的英语文本源，包括网页、代码和科学文章。
3. **开放性与灵活性**：所有训练进度点立即公开，为社区提供基础，可以通过适当的领域定制对模型进行微调。选择代价更低的初始化方式，提高模型的初始化效率，同时采用批处理大小的预热策略来快速提升训练速度。
4. **应用与创新**：ModernBERT的长序列长度和高性能量身适配RAG管道和大型代码搜索等应用，有望开辟新的编程助理领域。引入奖励机制支持社区贡献，对最好的示例进行公开评定与奖励，并提供示例任务引导，鼓励在代码相似性检测等方面的应用开发。
5. **获取与其他资源**：已有两个型号的ModernBERT模型在HuggingFace Hub上发布，供用户直接使用。感兴趣的研究者与开发者还可以访问arXiv提交的论文、模型文档和相关信息，探索和学习更多有关ModernBERT的特点和应用。

这些要点总结共同涵盖了ModernBERT的技术改进、模型利用、社区激励机制以及资源获取方向，以展示其在模型定位、技术支持、开放性编程与创新应用等方面的价值。
