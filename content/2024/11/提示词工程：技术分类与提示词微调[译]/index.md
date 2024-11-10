---
title: 提示词工程：技术分类与提示词微调[译]
date: 2024-11-10
extra:
  source: https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning
  original_title: 提示词工程：技术分类与提示词微调[译]
---
## Summary
**摘要**：
这篇文章提供了对提示词工程技术的全面概览，包括明确的技术分类、提示词微调和评估的方法。目前的提示词工程技术分为三个大类：单一提示词技术、组合多个提示词的技术和将大型语言模型与外部工具结合的技术。技术具体包括零样本学习、少样本学习、链式思维提示、程序辅助语言生成、投票、分而治之方法、自我评价等。文章深入分析了各种技术工作原理和应用，同时强调了提示词调整和评估的重要性。简而言之，文章围绕技术分类、具体技术原理与应用、以及提高提示词有效性的策略提供了综合性的指导。

**要点总结**：
1. **提示词工程技术**：专注于优化启发式反馈机制，提高大语言模型的性能。
  
2. **技术分类**：分为单一提示词技术、组合多提示词技术与大型语言模型结合外部工具的应用三类。
  
3. **任务挑战**：缺乏明确技术分类、作者针对性技术和方法之间的个性化融合。
  
4. **常见规则**：编写清晰指导语句、具体化说明、使用标签/分隔符、结构化输出要求等。
  
5. **标准化分类**：提供一种建议的分类系统，帮助理解和应用提示词工程技术。
  
6. **技术详解**：零样本学习、少样本学习、链式思维提示、程序辅助语言生成、投票方法、分而治之策略、自我评价机制等详细讲解。
  
7. **创新技术**：提出投票、分而治好方法、基于策略模型的定向刺激提示、编制知识提示、提示链、由简到繁提示、表链提示、思维树等新技术。
  
8. **反思与外部工具结合**：反思框架以及与检索增强生成、ReAct等外部工具的集成方法。
  
9. **提示词调整与评估**：将提示词作为数据科学流程进行调整，以确保最佳性能。
  
10. **结语**：总结了方法原理、应用案例和优化策略，鼓励实践者根据具体需求灵活使用和调整技术。
## Full Content
Title: 提示词工程：技术分类与提示词微调[译]

URL Source: https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning

Markdown Content:
作为一个新兴的研究领域，提示词工程尚未有明确的技术分类。当你查看各种讨论这些技术的文章和网站时，你会发现它们风格各异，且缺乏系统性。因此，实践者通常会采用最简单的方法。在本文中，我将为提示词工程技术提供一个概览，并提出一个清晰的分类，这将帮助你更好地理解这些概念并有效应用它们。此外，我还将探讨如何将提示词工程作为一个数据 [科学](https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning#)过程进行，其中包括提示词微调和评估。

![Image 1](https://miro.medium.com/v2/resize:fit:700/1*5eD88098w6J3RNwgja9Aeg.png)

大语言模型的挑战

尽管许多研究人员不断努力，但大语言模型仍然存在一些问题。其主要挑战包括：

*   **引用资源。** 大语言模型可以生成看似非常可信并引用外部资源的内容，但要记住，它们无法访问互联网或引用真实资源。
    
*   **偏见。** 大语言模型可能会在回答中表现出偏见，往往会生成带有刻板印象或偏见的内容。
    
*   **幻觉。** 当面对无法回答的问题时，大语言模型有时会“幻觉”出错误的信息。
    
*   **[数学](https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning#)和常识问题。** 尽管大语言模型具有先进的能力，但它们在解决一些简单的数学或常识问题时仍然存在困难。
    
*   **提示词攻击。** 大语言模型可能会被用户操纵或“攻击”，使其忽略开发者的指令并生成特定的内容。
    

大多数提示词工程技术主要针对幻觉问题，以及解决数学和常识任务的挑战。虽然也有一些技术专门用于减轻提示词攻击，但这部分内容需要另行讨论。

**常见规则**
--------

在讨论具体技术之前，让我们先谈谈一些提示词的常见规则，这些规则将帮助你编写清晰而具体的指令：

1.  准确说明具体要求（写作、总结、提取信息），
    
2.  避免告诉模型不该做什么，而是直接说明该做什么，
    
3.  具体化：不要说“用几句话”，而要说“用2-3句话”，
    
4.  添加标签或分隔符，使提示词更加结构化，
    
5.  如果需要，要求结构化输出（如JSON、HTML），
    
6.  要求模型验证是否满足条件（例如，“如果你不知道答案，就说‘没有信息’”），
    
7.  让模型先解释然后再给出答案（否则模型可能会试图为错误的答案辩护）。
    

**分类**
------

![Image 2](https://miro.medium.com/v2/resize:fit:700/1*Mq65ILt6P0p8n_ylGtkm1A.png)

我对提示词工程技术分类的建议

目前的大多数技术可以分为三类：

*   **单一提示词技术** 旨在优化单一提示词的响应，
    
*   其次是 **组合多个提示词的技术**。它们的共同点是通过多次调用一个模型（或多个模型）来解决任务，
    
*   最后，有一类方法将大型语言模型 **与外部工具结合**。
    

**单一提示词技术**
-----------

![Image 3](https://miro.medium.com/v2/resize:fit:700/1*wftLuvbBR58m_-LkMunbgQ.png)

输入输出或单一提示词技术

这些技术旨在通过单一提示词解决任务。

*   零样本学习，
    
*   少样本学习，
    
*   链式思维提示，
    
*   程序辅助语言生成。
    

让我们逐一探讨这些技术。

**零样本提示**

这是最简单的技术，使用自然语言指令即可完成。

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*qy3a2I6tPEbR3ASaM4z4vw.png)

一次性学习。示例来自 [promptingguide.ai](http://promptingguide.ai/)

**少样本提示**

LLM 在一次性学习方面表现出色，但在应对复杂任务时可能仍然会遇到挑战。少样本学习的核心思想是为模型展示类似任务的正确示例 ([Brown 等人, 2020](https://arxiv.org/abs/2005.14165))。

![Image 5](https://miro.medium.com/v2/resize:fit:700/1*4gE37XARckC1j_h9ldc2Bw.png)

少样本学习。示例来自 [promptingguide.ai](http://promptingguide.ai/)

在 [Min 等人 (2022)](https://arxiv.org/abs/2202.12837) 的研究中，展示了演示标签的不准确性对多种分类和选择任务的影响较小。更为关键的是，确保演示包含了标签空间的示例、输入测试的分布以及序列的整体格式。

**链式思维提示 (CoT)**

链式思维提示通过中间推理步骤，赋予模型复杂的推理能力。这种技术旨在让模型逐步推理每一个步骤。

![Image 6](https://miro.medium.com/v2/resize:fit:700/1*ZeCxbNj-VXyG9El5pwSjZQ.png)

零样本、少样本和链式思维提示技术。示例来自 [Kojima 等人 (2022)](https://arxiv.org/abs/2205.11916)。

链式思维提示（CoT）可以与零样本学习或少样本学习结合使用。零样本链式思维提示的核心思想是引导模型逐步推理，从而得出解决方案。该方法的作者 ([Kojima 等人, 2022)](https://arxiv.org/abs/2205.11916)) 证明了零样本链式思维提示在算术、符号和其他逻辑推理任务上，显著优于零样本大语言模型的表现。

如果选择少样本链式思维提示，必须确保示例的多样性，并附带详细的解释 ([Wei 等人, 2022)](https://arxiv.org/abs/2201.11903))。这种方法在算术、常识和符号推理任务上的表现提升非常显著。

**程序辅助语言模型 (PAL)**

程序辅助语言模型是一种通过将解释以自然语言和代码的形式呈现，从而扩展链式思维提示的方法 ([Gao 等人, 2022)](https://arxiv.org/abs/2211.10435))。

![Image 7](https://miro.medium.com/v2/resize:fit:700/1*cKINqTfoTPjIOdu6CnRLVA.png)

程序辅助语言提示。示例来自 [Gao 等人, 2022)](https://arxiv.org/abs/2211.10435)。

该技术可以通过 [LangChain PALChain](https://api.python.langchain.com/en/latest/pal_chain/langchain_experimental.pal_chain.base.PALChain.html) 类来实现。

**多组提示词技术**
-----------

下一组提示词基于不同策略来组合一个或几个模型的提示词：

1.  **投票。** 这种方法的思路是通过投票来获得正确的答案。技术：自我一致性。
    
2.  **分而治之。** 这一组提示词基于将复杂任务分解为多个提示词来完成。技术：定向刺激，生成知识，提示链，表格链，以及从最少到最多的提示法。
    
3.  **自我评价。** 这种方法建议在框架中加入一个检查输出是否符合指令的步骤。技术：反思，思维树。
    

**自我一致性（SC）**

自我一致性基于这样一个直觉，即“一个复杂的推理问题通常允许多种不同的思考方式，最终得出唯一正确的答案” ([Wang et al. (2022](https://arxiv.org/abs/2203.11171))).

![Image 8](https://miro.medium.com/v2/resize:fit:700/1*Ck4QA5__hCgRuftPSppu6w.png)

自我一致性提示技术

它多次提出相同的链式推理提示词，从而生成一组不同的推理路径，然后通过投票选择最一致的答案。

![Image 9](https://miro.medium.com/v2/resize:fit:700/1*xrgSrsjOdoSnGxSLwzPaFQ.png)

来自 [Wang et al. (2022](https://arxiv.org/abs/2203.11171)) 的自我一致性提示法示例

在 [Wang et al. (2022](https://arxiv.org/abs/2203.11171)) 中，自我一致性在算术和常识任务中的应用在常见基准测试中提高了4%–18%的表现。

**定向刺激提示（Directional Stimulus Prompting, DSP）**
-----------------------------------------------

下一个结合提示词的概念是“分而治之”。在 DSP 中，我们有两个步骤：首先生成刺激（例如，关键词），然后使用这些刺激来提高响应的质量。

定向刺激提示由 [Li 等人 (2023)](https://arxiv.org/abs/2302.11520) 提出，主要用于摘要生成、对话生成和链式思维推理任务。该方法涉及两个模型：

*   一个可调的小型策略语言模型，用于生成刺激（提示）。
    
*   一个冻结的大型黑箱语言模型，根据问题和前一步生成的刺激来生成总结。
    

![Image 10](https://miro.medium.com/v2/resize:fit:700/1*8FE1G2c8YfKCqCFMlHgZkw.png)

定向刺激提示示意图

策略模型可以通过监督微调和基于大型语言模型输出的离线或在线奖励进行强化学习来优化，例如：

![Image 11](https://miro.medium.com/v2/resize:fit:700/1*2W_gUmz_v0zpkC8lrupvLw.png)

在 DSP 框架中 [Li 等人 (2023)](https://arxiv.org/abs/2302.11520) ，我们学习了一个小型可调策略模型，以生成定向刺激（此处为关键词），为大型语言模型提供特定的输入指导，从而实现目标。

**生成知识提示 (Generated Knowledge Prompting, GK)**

在“分而治之”概念下，另一个提示技术是由 [Liu 等人 (2022)](https://arxiv.org/pdf/2110.08387.pdf) 提出的生成知识提示。其核心思想是先通过独立的提示生成知识，然后利用这些知识来获取更优质的响应。

生成知识提示包括两个阶段：

*   **知识生成**：使用少样本学习示例从语言模型中生成与问题相关的知识陈述，
    
*   **知识整合**：利用第二个语言模型对每个知识陈述进行预测，并选择置信度最高的预测。
    

![Image 12](https://miro.medium.com/v2/resize:fit:667/1*yle11EBNK9SIntuAN0sgUw.png)

生成知识提示示意图

该方法无需依赖任务特定的监督来整合知识，也无需访问结构化的知识库，但它显著提升了大规模最先进模型在常识推理任务上的表现。

![Image 13](https://miro.medium.com/v2/resize:fit:700/1*DQJ8bj0WlEPywSS7wjdLww.png)

QASC 中由 [Liu 等人 (2022)](https://arxiv.org/pdf/2110.08387.pdf) 提出的少样本知识生成提示词示例

**提示链**

提示链是一种简单却强大的技术，你可以将任务拆分为多个子问题，并逐一提示模型进行处理。

![Image 14](https://miro.medium.com/v2/resize:fit:700/1*V6mBYqyGeoNTkx6Lq2cHaw.png)

提示链示意图

提示链在处理复杂任务时特别有用，当一个大语言模型面对一个非常详细的提示时，可能会难以处理。提示链还可以提升大语言模型应用的透明度、可控性和可靠性。

![Image 15](https://miro.medium.com/v2/resize:fit:700/1*f3Z-3SJBEU561YbBcw1gZg.png)

来自 [txt.cohere.com](http://txt.cohere.com/) 的提示链示例

**由简到繁提示**

由简到繁提示更进一步，增加了一个步骤，即模型需要决定如何将任务拆分为多个子问题。

![Image 16](https://miro.medium.com/v2/resize:fit:700/1*H574wa9Fd25FUuJrM0iLYg.png)

由简到繁提示的示意图

[Zhou 等人 (2022)](https://arxiv.org/pdf/2205.10625.pdf) 的实验结果表明，由简到繁提示在符号操作、组合泛化和 [数学](https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning#)推理相关的任务中表现优异。

![Image 17](https://miro.medium.com/v2/resize:fit:700/1*Qidvz-03gcE0G7zdfWtARg.png)

来自 [Zhou 等人 (2022)](https://arxiv.org/pdf/2205.10625.pdf) 的由简到繁提示示例

**表链提示**

在最近的研究中（[Wang et al. (2024)](https://arxiv.org/pdf/2401.04398.pdf)），提出了一种新方法，将表格数据明确纳入推理链，作为中间思维的代理。

![Image 18](https://miro.medium.com/v2/resize:fit:699/1*X9iw04YS4sey7aVoMO2Oqw.png)

表格链提示的示意图

该算法包括两个循环步骤：

1.  **动态计划**：在此步骤中，大语言模型（LLM）根据输入查询和之前操作的历史记录（操作链）从操作库中选择下一个操作，
    
2.  **论据生成**：涉及为前一步选择的操作（如新列名）生成论据，并使用编程语言执行操作，生成相应的中间表格。
    

![Image 19](https://miro.medium.com/v2/resize:fit:700/1*q4V3pnRiYHRycLbqlvR5Xw.png)

表格链提示的示例及其对比 [Wang et al. (2024)](https://arxiv.org/pdf/2401.04398.pdf)

接下来的两种方法实现了自我检查的概念——框架中设置了一个步骤来检查解决方案。可以在[此链接](https://github.com/run-llama/llama-hub/blob/main/llama_hub/llama_packs/tables/chain_of_table/chain_of_table.ipynb)找到表格链实现的示例。

**思维树（ToT）**

思维树在链式思维方法的基础上进行了扩展，允许模型探索多个推理步骤并自行评估选项。

要实现思维树技术，我们必须解决四个问题：

1.  如何将中间过程分解为思维步骤，
    
2.  如何从每个状态生成潜在的思维，
    
3.  如何使用启发式方法评估状态（通过状态评估提示），
    
4.  使用何种搜索算法（[Yao et al. (2023)](https://arxiv.org/abs/2305.10601)）
    

![Image 20](https://miro.medium.com/v2/resize:fit:700/1*IUa-dv86KwXz3qVccJWudQ.png)

Tree-of-Thoughts 提示技巧

**输入提示词**应包括解决问题的中间步骤描述，以及采样的想法或生成这些想法的指示。**状态评估器提示词**则应提供选择下一步提示词的指示。

![Image 21](https://miro.medium.com/v2/resize:fit:700/1*29HOrzWcwME6jGJnpucMVA.png)

24 点游戏的 Tree-of-Thought 示例，来源于 [Yao 等人 (2023)](https://arxiv.org/abs/2305.10601)。

[Yao 等人 (2023)](https://arxiv.org/abs/2305.10601) 的实验展示了 Tree-of-Thought 技术在需要复杂规划或搜索的任务中的成功应用。LangCh [ai](https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning#)n 已在 [langchain\_experimental.tot.base.ToTChain 类](https://api.python.langchain.com/en/latest/tot/langchain_experimental.tot.base.ToTChain.html) 中实现了 Tree-of-Thought 技术。

**反思**

反思是一个通过语言反馈强化语言 [智能体](https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning#)的框架。反思智能体会对任务反馈信号进行口头反思，并将其反思文本保存在情景记忆缓冲区中，以便在后续试验中做出更好的决策 ([Shinn 等人 (2023))](https://arxiv.org/pdf/2303.11366.pdf)。

AI-driven creativity enhancement tools

![Image 22](https://miro.medium.com/v2/resize:fit:536/1*izLleO5MufRYPZ9-nR-qJQ.png)

反思框架的示意图，来自 [Shinn 等人 (2023)](https://arxiv.org/pdf/2303.11366.pdf)。

反思框架由三个独立的模型组成：

*   **执行者**：一个基于状态观察生成文本和动作的大语言模型（使用 CoT 和 ReAct 技术），
    
*   **评估者**：一个对执行者生成的输出进行评分的大语言模型，
    
*   **自我反思**：一个生成口头强化提示以帮助执行者自我改进的大语言模型。
    

![Image 23](https://miro.medium.com/v2/resize:fit:700/1*QDMt7kX1Y8QlT4NFlNHQdg.png)

[Shinn 等人 (2023)](https://arxiv.org/pdf/2303.11366.pdf) 中不同任务的 Reflexion 示例

Reflexion 在需要顺序决策、编程和语言推理的任务中表现出色。

可以通过[链接](https://github.com/noahshinn/reflexion)查看具体实现。

**结合外部工具的大语言模型框架**
------------------

在本节中，我将介绍两种方法——检索增强生成和ReAct。

**检索增强生成 (RAG)**

RAG结合了信息检索组件和文本生成模型：

*   **检索**。在检索阶段，系统通常使用向量搜索来查找可能回答问题的相关文档，
    
*   **生成**。然后，将这些相关文档与初始问题一起作为上下文传递给大语言模型（[Lewis et al. (2021)](https://arxiv.org/pdf/2005.11401.pdf)）。
    

在大多数情况下，RAG采用序列方式操作，即检索到的_k_篇文档用于生成回答用户查询的所有Token。

![Image 24](https://miro.medium.com/v2/resize:fit:700/1*TlL6tf8Ng0wQL6iJNMDfeA.png)

RAG架构示意图

尽管RAG中的语言模型可以进行微调，但实际应用中很少这样做，因为预训练的大语言模型已经足够强大，可以直接使用，而微调成本又过高。此外，RAG中的内部知识可以以高效的方式进行修改，无需重新训练整个模型。

![Image 25](https://miro.medium.com/v2/resize:fit:700/0*Jw8U0je9NUf_DJdI)

[来自deepset.ai](http://xn--deepset-295on32q.ai/)的RAG流程示例

RAG生成的响应更加事实准确、具体且多样化，并在事实验证方面取得了更好的效果。

**ReAct**

[Yao et al. (2022)](https://arxiv.org/abs/2210.03629) 引入了一种名为ReAct的框架，在此框架中，大语言模型交替生成_推理轨迹_和_任务特定的行动_：推理轨迹帮助模型推导、跟踪和更新行动计划，并处理例外情况，而行动则使模型能够与知识库或环境等外部资源交互并收集更多信息。

![Image 26](https://miro.medium.com/v2/resize:fit:700/1*XB4r7h0Xt2_NTmVxQB5NqQ.png)

ReAct架构示意图

ReAct 框架能够从可用工具（如搜索引擎、计算器、SQL  [智能体](https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning#)）中进行选择，应用这些工具并分析结果，从而决定下一步行动。

![Image 27](https://miro.medium.com/v2/resize:fit:582/1*tH2b4ttH3vdybx4zIUTW0A.png)

[Yao 等人（2022）](https://arxiv.org/abs/2210.03629) 提供的 ReAct 示例

ReAct 通过与 Wikipedia API 的交互，生成比没有推理轨迹的基线更易于解释的任务解决路径，从而克服了链式思维推理中常见的幻觉和错误传播问题 ([Yao 等人, 2022](https://arxiv.org/abs/2210.03629))。

查看通过 Langch [ai](https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning#)n 工具实现的 [ReAct 示例](https://python.langchain.com/docs/modules/agents/agent_types/react/)。

**提示词调整与评估**
------------

提示词工程技术的选择在很大程度上取决于您对大语言模型的应用需求和可用资源。如果您曾经尝试过提示词，您会发现大语言模型对人工生成的提示词非常敏感，即使是最微小的变化也可能影响结果，这些变化往往是不理想的且具有主观性。

无论您选择哪种提示词技术，如果您正在构建应用程序，将提示词工程视为数据科学过程非常重要。这意味着需要创建一个测试集，选择适当的度量标准，调整提示词并评估其对测试集的影响。

![Image 28](https://miro.medium.com/v2/resize:fit:516/1*6IKahQpMeakA7JL5kSKPtg.png)

将提示词工程视为数据科学过程

测试提示词的度量标准在很大程度上取决于具体应用，但以下是一些指南（来自[数据科学峰会2023](http://dssconf.pl/)）：

![Image 29](https://miro.medium.com/v2/resize:fit:700/1*USUsrDR0d-n9fvLBxpbbng.png)

测试提示词的度量标准（来自[数据科学峰会2023](http://dssconf.pl/)）

1.  **准确性和相关性**：
    

*   生成的答案在事实上的准确性，
    
*   生成的答案与问题的相关性。
    

2.  **检索**—主要应用于RAG和ReAct管道，但也适用于生成知识和方向性刺激提示词：
    

*   精确度——检索到的文档的相关性，
    
*   召回率——是否检索到所有相关文档。
    

3.  **内部思维**：
    

*   智能体和工具选择的准确性——针对ReAct，
    
*   工具论点提取——是否从上下文中正确 [检索](https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning#)并转换论点——针对ReAct，
    
*   在长时间对话中记住事实——针对ReAct，
    
*   正确的逻辑步骤——针对ReAct和链式思维提示词。
    

4.  **非功能性**：
    

*   答案的风格和语气，
    
*   避免偏见，
    
*   遵循规范与安全检查，
    
*   提示词注入测试。
    

根据您的使用案例，选择适当的度量标准，并跟踪提示词变化对测试集的影响，确保任何更改不会降低响应质量。

**总结**
------

我并不声称已经涵盖了所有现有的技术——这些技术实在太多了，很快可能会有人出版整本教科书。但如果你读到了这里，你会发现所有这些技术的概念都非常普遍且直观。我可以将编 [写](https://baoyu.io/translations/prompt-engineering/prompt-engineering-classification-of-techniques-and-prompt-tuning#)一个好的提示词的所有规则总结为以下几点：

1.  清晰且准确，避免让模型猜测你的意图，
    
2.  使用分隔符或标签来增强提示词的结构性，
    
3.  通过展示示例和添加解释来帮助模型理解，
    
4.  要求模型以迭代的方式思考，并解释其解决方案，
    
5.  如果提示词比较复杂，考虑将其分解为多个子任务，
    
6.  尝试多次重复使用相同的提示词，
    
7.  考虑增加一个模型自我检查的步骤，
    
8.  如果需要，将你的大语言模型与外部工具结合使用，
    
9.  将提示词调整视为一个迭代且需要评估的数据科学过程。
    

就这样！感谢你坚持到这里，祝你提示词编写顺利！

