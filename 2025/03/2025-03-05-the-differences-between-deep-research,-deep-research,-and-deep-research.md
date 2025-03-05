# The Differences between Deep Research, Deep Research, and Deep Research
- URL: https://leehanchung.github.io/blogs/2025/02/26/deep-research/
- Added At: 2025-03-05 16:16:51
- [Link To Text](2025-03-05-the-differences-between-deep-research,-deep-research,-and-deep-research_raw.md)

## Summary
**摘要**：
近期，各AI实验室纷纷推出“Deep Research”功能，如Google的Gemini 1.5、OpenAI的Deep Research和Perplexity的Deep Research。同时，DeepSeek、阿里巴巴的Qwen和Elon Musk的xAI也为其聊天机器人助手推出了搜索和深度搜索功能。此外，GitHub上还涌现了大量模仿Deep Research的开源实现。这种现象类似于2023年的RAG热潮，许多事物都被重新命名并宣传为“Deep Research”，但对其具体含义没有明确定义。为明确“Deep Research”的具体技术实现，文章从技术角度分析了各种“Deep Research”的实现方法。Deep Research是一种报告生成系统，它接受用户查询，并使用大型语言模型（LLM）作为代理来迭代地搜索和分析信息，并生成详细的报告作为输出。自ChatGPT问世以来，报告生成一直是AI工程的重点。文章探讨了构建报告生成系统的常见模式，突出了它们的差异，并对各供应商的产品进行了分类，包括非训练的DAG、非训练的FSM、训练的端到端模型和训练的大型推理模型，最后对Deep Research 的能力进行了评估。

**要点总结**：
1.  **Deep Research的定义**：Deep Research是一种报告生成系统，它接受用户查询，使用大型语言模型（LLM）作为代理迭代地搜索和分析信息，并生成详细的报告作为输出。在自然语言处理（NLP）中，这被称为报告生成。

2.  **非训练的DAG方法**：早期的AI工程师发现，直接让LLM生成报告不切实际，因此他们使用复合模式将多个LLM调用链接在一起。流程通常是首先分解用户查询以创建报告大纲，然后从搜索引擎或知识库检索相关信息并进行总结，最后使用LLM将各个部分缝合成一个连贯的报告。

3.  **非训练的FSM方法**：为了提高报告质量，工程师们在DAG方法中增加了复杂性。他们引入了诸如reflexion和self-reflection之类的结构模式，LLM可以审查和改进自己的输出。这会将简单的DAG转换为有限状态机（FSM），其中LLM可以部分指导状态转换。与DAG方法一样，每个prompt都是手工制作的，并且评估仍然是主观的。

4.  **训练的端到端方法**：由于早期方法存在prompt工程随意和缺乏可衡量的评估指标等缺点，因此出现了一个转变。Stanford的STORM通过使用DSPy端到端地优化系统来解决这些问题。STORM生成的报告在质量上可以与Wikipedia的文章相媲美。

5.  **训练的大型推理模型**：LLM推理能力的进步使大型推理模型成为Deep Research的一个引人注目的选择。OpenAI介绍了其如何训练其Deep Research模型。Google的Gemini和Perplexity的聊天助手也提供“Deep Research”功能，但没有公布关于如何优化模型或系统的文献或任何有价值的定量评估。xAI的Grok擅长生成报告，尽管它似乎没有搜索超过两次迭代。
