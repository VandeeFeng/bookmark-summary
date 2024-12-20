# The Ultimate Guide to Chain of Thoughts (CoT): Part 1
- URL: https://learnprompting.org/blog/guide-to-chain-of-thought-part-one
- Added At: 2024-12-20 14:06:47
- [Link To Text](2024-12-20-the-ultimate-guide-to-chain-of-thoughts-(cot)-part-1_raw.md)

## Summary
**摘要**：
本文主要讲解了Chain-of-Thought（这里的简称被称作CoT）推理策略在大型语言模型（LLMs）中的关键作用以及其对LLMs推理能力的重要性。LLMs通过被命名为“CoT”的策略实现了解决问题、推理和多步骤任务生成等各种复杂任务的能力提升，这种技术使得模型在数学问题解决、逻辑推理、复杂语言生成任务等领域更加准确。随后，文章详细介绍了标准CoT、零样本CoT、自一致性、自动化CoT（Auto-CoT）、表格化CoT（Tab-CoT）等CoT策略的版本，并阐述了它们如何使CoT技术在各个领域变革。本文同样讨论了CoT策略的多样性和路径拓展，如对比式CoT、决策树结构化思考（即Tree-of-Thoughts ToT）以及结构化思考图（Graph of Thoughts GoT）的概念。此外，讨论了编程性思考促进策略（Programs of thoughts PoT），支持LLMs通过与外部语言解释器的交互（例如Python）来解决复杂问题。最后，文章引导读者理解为何掌握CoT技巧对AI工程师至关重要，这将直接影响AI系统的可解释性和可理解性。

**要点总结**：
- **CoT推理策略**：CLMs在处理复杂任务时提出断链性问题并将其分解为多个步骤。
- **标准CoT**：借助用户输入的数个示例，此方法允许LLMs系统逐个解决问题，然后组合得出答案。
- **零样本CoT**：通过任务特有的提示词“让我们一步一步思考”，此方法无需示例即可回答问题，主要适用于算术、符号推理和逻辑推理任务。
- **自一致性**：通过向LMM提问多次，收集并聚合多个回答，确保结果的一致性，降低算法不完全推理的风险。
- **自动化CoT（Auto-CoT）**：利用算法自动生成推理步骤，进一步自动化后零样本CoT过程。
- **表格化CoT（Tab-CoT）**：通过在表格中显式建模推理过程，提高输出的清晰度与结构化。
- **对比式CoT**：通过提供正确与错误的推理示例，训练模型识别问题避免滥推。
- **决策树结构化思考（Tree-of-Thoughts ToT）**：鼓励LLMs通过多个思维链发展逻辑推理，相似于决策树。
- **结构化思考图（Graph of Thoughts GoT）**：巩固CoT概念，通过建模信息网络为LLMs提供更为动态的推理框架。
- **编程性思考促进策略（Programs of thoughts PoT）**：编码生成的数学表达式并执行，解决复杂数学表达式和迭代数值计算。
- **在AI领域的应用**：掌握CoT技巧对AI工程师凸显了对构建可解释、准确、适应性强的AI系统的价值。
