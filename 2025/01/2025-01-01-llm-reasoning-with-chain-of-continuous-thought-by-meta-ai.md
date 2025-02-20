# LLM Reasoning with Chain of Continuous Thought by Meta AI
- URL: https://aipapersacademy.com/chain-of-continuous-thought/
- Added At: 2025-01-01 06:51:56
- [Link To Text](2025-01-01-llm-reasoning-with-chain-of-continuous-thought-by-meta-ai_raw.md)

## Summary
**摘要**：
本文探讨了Meta AI的“训练大型语言模型在连续潜空间中推理”的论文，论文提出了COCONUT方法以打破语言基元推理的约束，允许大型语言模型在连续潜空间中以"Chain of Continuous Thought"的方式推理。COCONUT方法通过在模型的运算中交替使用语言模式和潜空间模式，允许模型在推理过程中使用连续思想。此外，文中指出COCONUT方法优于传统的CoT方法，在处理数学、逻辑推理及规划要求更强的任务时表现更佳。最后，文章介绍了连续推理的优势，尤其是在规划密集型任务中，为未来的AI发展提供了潜在的改进途径。

**要点总结**：
1. **CoT方法回顾**：CoT方法是一种基于语剂逐步展开的推理方式，可以通过模型生成链路的推理过程来得到准确答案。然而，该方法基于语言生成，受限于语言表达能力。
2. **COCONUT方法引入**：COCONUT通过允许模型在连续潜空间中推理，在语言模式与潜空间模式之间进行切换，以连续思想进行推理，无需完全将思想转换为语句，这使得模型能够以更高的效率进行推理。
3. **训练程序**：COCONUT通过多个阶段的训练程序，从零推理逐渐过渡到使用连续思想的推理，利用现有CoT数据，让模型逐步适应并学习如何在连续空间中执行推理。
4. **实验结果**：通过对数学、逻辑推理和规划能力要求更强的三种不同任务的实验，COCONUT方法在准确性上都表现优于CoT方法，特别是在需要规划能力的任务中表现更为出色。
5. **持续性思考与规划能力**：连续推理方法类似于广度优先搜索（BFS）策略，能够有效地提高AI模型在规划密集型任务上的性能，显示了其在规划和决策过程中的应用潜力。
