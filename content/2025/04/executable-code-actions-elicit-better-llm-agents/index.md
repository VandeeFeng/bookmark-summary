---
title: Executable Code Actions Elicit Better LLM Agents
date: 2025-04-19
extra:
  source: https://readwise.io/reader/shared/01jqgarmq8875pv7d3j09emwe6/
  original_title: Executable Code Actions Elicit Better LLM Agents
---
## Summary
**摘要**：
本文介绍了作者对 Agent 领域一篇重要论文《Executable Code Actions Elicit Better LLM Agents》的解读，该论文是 ReAct 模型的演化版本，被称为 CodeAct。ReAct 模型通过口头表达的方式，简化了复杂的强化学习过程，成为 Agent 项目中简单、有效且稳健的工作流。作者认为 ReAct 的价值不可估量，并强调了学术的魅力在于其成果能以免费论文的形式传播，产生巨大的实际价值。CodeAct 将 ReAct 中固定的 tool 替换为可执行的 Python 代码，利用 Python 库的丰富性，极大地提升了 tool 的数量级和复杂度。CodeAct 建立在 ReAct 的 observation–reasoning–action 工作流之上，使其几乎可以实现 self-debug，并且作者还分享了CodeAct的论文链接和langchain example。

**要点总结**：
1.  ReAct 模型是 Agent 领域的重要创新，它通过口头表达简化了强化学习过程，成为 Agent 项目中被广泛应用的工作流。ReAct通过将复杂的强化学习过程，用自然语言描述的方式表现出来，使得智能体能够像人类一样进行思考和行动，极大地降低了Agent开发的门槛。
2.  CodeAct 是 ReAct 的演进版本，它使用可执行的 Python 代码替换了 ReAct 中固定的 tool。Python 语言拥有丰富的库，CodeAct 能够处理更复杂、更多样化的任务，显著提升 tool 的数量级和复杂度，为 Agent 提供了更强大的能力。
3.  CodeAct 继承了 ReAct 的 observation–reasoning–action 工作流，使 Agent 具备 self-debug 的潜力。这意味着 Agent 可以在执行过程中观察、推理并纠正错误，从而提高其稳定性和可靠性，使其在复杂环境中能够自主学习和适应。
4.  ReAct 模型的价值在于其通过免费论文传播，为 Agent 领域创造了巨大的实际价值。这一方面体现了学术研究的开放性和共享性，另一方面也说明了基础研究对于技术创新和产业发展的重要推动作用。

## Full Content
Title: Twitter thread from @dongxi_nlp | annotated by Vandee

URL Source: https://readwise.io/reader/shared/01jqgarmq8875pv7d3j09emwe6/

Published Time: 2025-03-28

Markdown Content:
「Agent」论文:Executable Code Actions Elicit Better LLM Agents

从 ReAct 到 CodeAct

如果让我在所有 LLM 论文中选择我最喜欢的一篇,2022 年的 ReAct 绝对是前三名之一。

ReAct 大道至简,天才般地将复杂的强化学习(RL)过程,通过口头表达的方式表现出来,至今依然是 Agent 项目中最简单、最有效、最稳健的工作流之一。

如果说 Agent 在各个圈子带动了几百亿美元的投资,那么 ReAct 的价值不可估量。而它,仅仅是作者在 Google 实习期间的成果。这正是学术的魅力——一个价值超过几百亿美元、普通人一学就会的 ReAct,通过一篇免费论文传播出来,产生了巨大的实际价值。

这篇论文是 ReAct 的演化版本,把固定的 tool 替换为可执行的 Python 代码,从而带来更丰富的变化。由于 Python 库的丰富性,CodeAct 在提升 tool 的数量级和复杂度方面有巨大潜力。

尤其是 CodeAct 建立在 ReAct 的 observation–reasoning–action 工作流之上,使得它几乎可以实现 self-debug。这不禁让我想起那个如今无人提及、但去年融资超过 20 亿美元的 Devin。

![Image 1](https://pbs.twimg.com/media/GnJxdxVaYAAmefO.jpg)

* * *

两年前对ReAct的解读:

![Image 2](https://pbs.twimg.com/profile_images/1555109458073747457/JANhY5Zh.jpg)

1/ ReAct: 大语言模型推理,决断和行动的关键

最近大语言模型突破了文字处理任务的限制,向智能coordinator的角色转化。

一个疑问随之而来,“LLM到底如何决断并采取行动来调用不同的api的?”

本条thread读书笔记,通过解读论文ReAct,同时介绍langchain的一个具体例子来试图回答这个问题。

🧵

![Image 3](https://pbs.twimg.com/media/FtJN-V7akAA9_wX.jpg)

* * *

CodeAct论文链接:

[arxiv.org/abs/2402.01030](https://arxiv.org/abs/2402.01030)

* * *

CodeAct langchain example:

[github.com/langchain-ai/l...](https://github.com/langchain-ai/langgraph-codeact)

