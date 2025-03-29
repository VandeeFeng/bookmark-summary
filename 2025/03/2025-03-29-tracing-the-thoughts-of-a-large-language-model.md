# Tracing the thoughts of a large language model
- URL: https://simonwillison.net/2025/Mar/27/tracing-the-thoughts-of-a-large-language-model/
- Added At: 2025-03-29 06:37:13
- [Link To Text](2025-03-29-tracing-the-thoughts-of-a-large-language-model_raw.md)

## Summary
**摘要**：
Anthropic发布了两篇关于大型语言模型（LLM）可解释性的新论文，延续了去年Golden Gate Claude的研究。第一篇论文《Circuit Tracing: Revealing Computational Graphs in Language Models》将去年的可解释特征扩展到归因图，可以追踪模型将特定输入提示转换为输出响应的中间步骤链。第二篇论文《On the Biology of a Large Language Model》利用该方法，从多种角度研究Claude 3.5 Haiku。例如，多语言电路展示了用三种不同语言的相同提示，使用了相似的电路，暗示了一种有趣的泛化水平。这两篇论文均以移动友好的HTML页面形式呈现，包含可链接的部分，甚至还有一些内联交互式图表。其中一个例子是多语言语言模型可视化，展示了三种语言的近义词预测，激活分析突出显示了法语文本中的“contraire”实例。

**要点总结**：
1.  **扩展可解释特征到归因图：** 《Circuit Tracing》论文的核心是扩展了去年的研究成果，引入了“归因图”的概念。归因图能够追踪语言模型处理输入提示并生成输出响应时所经历的中间步骤，揭示了模型内部的计算过程。
2.  **研究Claude 3.5 Haiku的内部机制：** 《On the Biology of a Large Language Model》论文运用“Circuit Tracing”中的方法，对Claude 3.5 Haiku模型进行了深入研究，从多个角度探索其工作原理，试图理解LLM的内部生物学。
3.  **多语言电路的相似性：** 通过研究多语言电路，论文发现，对于同一种提示，即使使用不同的语言，模型也会使用相似的电路进行处理。这表明LLM在不同语言之间存在着某种程度的泛化能力，它们能够理解不同语言表达的相同含义。
4.  **论文呈现形式的创新：** 这两篇论文没有采用传统的PDF格式，而是使用了移动友好的HTML页面，这种形式更便于阅读和分享，并且还包含了可链接的部分和内联交互式图表，增强了用户的阅读体验。

