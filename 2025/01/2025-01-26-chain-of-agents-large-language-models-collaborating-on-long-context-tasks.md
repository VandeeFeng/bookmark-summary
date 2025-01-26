# Chain of Agents: Large language models collaborating on long-context tasks
- URL: https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/
- Added At: 2025-01-26 11:54:30
- [Link To Text](2025-01-26-chain-of-agents-large-language-models-collaborating-on-long-context-tasks_raw.md)

## Summary
**摘要**：
《链式代理：大型语言模型在长上下文任务中的协作》一文介绍了Chain-of-Agents(CoA)框架，这是用于长上下文任务的多代理协作新模式。通过自然语言处理实现信息聚合和长于多种大型语言模型之间的上下文推理，CoA在问答、总结和代码完成等长上下文任务方面表现出色。它显著提高了与较强基线(如Retrieval Augmented Generation(RAG)、多代理大型语言模型和输入截断模型)相比的表现。CoA的核心优势在于其成本效益、任务和长度无关性及易解释性。

**要点总结**：
- **面临的问题**：通用大型语言模型在处理需要长输入的长上下文任务时存在局限，挑战在于输入长度限制导致无法充分利用全部上下文，影响理解和任务完成。
- **CoA框架**：作者引入了Chain-of-Agents框架，该框架通过逐层协作的方式，利用各代理处理长上下文的不同部分，实现信息聚合和上下文推理。CoA是基于自然语言协作实现的，充分扩展了大型语言模型的信息处理能力，而与传统方法如上下文缩减和窗口扩展有不同的处理方式。
- **输入处理**：CoA采用分阶段的方法，首先通过多个worker代理处理长上下文的不同部分，通过消息传递进行协作，最后由manager代理整合所有信息以生成最终答案。此过程模拟了人类处理长文字的方式，实现逐层协作处理。
- **实验结果**：在多个数据集和六个模型上进行的实验验证了CoA的有效性，显示CoA相比已知的基线处理长上下文任务时表现更优，特别是在问答、摘要和代码完成任务上。
- **性能提升**：CoA能够在多种大型语言模型上实现优异的性能提升，尤其在处理较长输入时，相较于全上下文模型和RAG模型，CoA表现出了显著的提升，改善幅度达到10%以上。

CoA框架为处理长上下文任务提供了一种高效且成本效益高的解决方案，通过合理分配任务级联处理，实现对大型语言模型的优化，适用于多种数据集任务，展现出其独特的性能优势。
