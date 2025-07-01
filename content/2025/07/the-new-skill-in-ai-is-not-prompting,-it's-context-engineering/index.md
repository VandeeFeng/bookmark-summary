---
title: The New Skill in AI is Not Prompting, It's Context Engineering
date: 2025-07-01
extra:
  source: https://www.philschmid.de/context-engineering
  original_title: The New Skill in AI is Not Prompting, It's Context Engineering
---
## Summary
**摘要**：
文章探讨了人工智能领域新兴的"上下文工程"概念，指出随着智能代理（Agents）的兴起，提供高质量上下文信息而非单纯优化提示词（prompting）已成为关键技能。作者将上下文定义为模型生成响应前所能获取的全部信息，包括系统指令、用户提示、对话历史、长期记忆、检索信息、可用工具和输出格式等七个要素。通过对比"廉价演示版"和"魔法版"智能代理的实例分析，阐述了优质上下文如何显著提升AI代理的性能。上下文工程被定义为设计动态系统的学科，强调在正确时间为LLM提供正确信息和工具，其特点包括系统性、动态性、精准性和格式敏感性。文章结论指出，构建强大AI代理的关键在于上下文工程，这需要跨领域协作来确保LLM获得完成任务所需的全部结构化信息。

**要点总结**：
1. **上下文工程取代提示工程的趋势**：在AI领域，关注点正从单纯优化提示词转向更全面的"上下文工程"，即系统性地为LLM提供完成任务所需全部背景信息的学科。Tobi Lutke将其定义为"提供让LLM合理解决任务所需所有上下文的艺术"。

2. **上下文的多元化组成要素**：上下文不仅限于单次提示，而是包含七个关键组成部分：系统指令（定义模型行为）、用户提示（当前任务）、对话历史（短期记忆）、长期记忆（持久知识库）、检索信息（RAG内容）、可用工具（可调用功能）和结构化输出（响应格式要求）。

3. **上下文质量决定Agent效能**：通过企业日程安排场景的对比案例显示，当Agent仅获取基础请求时表现机械，而当补充日历数据、历史邮件、联系人信息和工具权限等上下文后，能生成人性化、高效率的解决方案，证明Agent性能差异主要源自上下文质量而非模型算法。

4. **上下文工程的四大特征**：与静态的提示工程不同，上下文工程具有系统性（预置处理流程）、动态性（实时任务定制）、精准性（按需提供信息工具）和格式敏感性（优化信息呈现方式）的特点，其核心目标是避免"垃圾进垃圾出"的问题。
## Full Content
Title: The New Skill in AI is Not Prompting, It's Context Engineering

URL Source: https://www.philschmid.de/context-engineering

Published Time: 2025-06-30

Markdown Content:
Context Engineering is new term gaining traction in the AI world. The conversation is shifting from "prompt engineering" to a broader, more powerful concept: **Context Engineering**. [Tobi Lutke](https://x.com/tobi/status/1935533422589399127) describes it as "the art of providing all the context for the task to be plausibly solvable by the LLM.” and he is right.

With the rise of Agents it becomes more important what information we load into the “limited working memory”. We are seeing that the main thing that determines whether an Agents succeeds or fails is the quality of the context you give it. Most agent failures are not model failures anyemore, they are context failures.

What is the Context?
--------------------

To understand context engineering, we must first expand our definition of "context." It isn't just the single prompt you send to an LLM. Think of it as everything the model sees before it generates a response.

![Image 1: Context](https://www.philschmid.de/static/blog/context-engineering/context.png)

*   **Instructions / System Prompt:** An initial set of instructions that define the behavior of the model during a conversation, can/should include examples, rules ….
*   **User Prompt:** Immediate task or question from the user.
*   **State / History (short-term Memory):** The current conversation, including user and model responses that have led to this moment.
*   **Long-Term Memory:** Persistent knowledge base, gathered across many prior conversations, containing learned user preferences, summaries of past projects, or facts it has been told to remember for future use.
*   **Retrieved Information (RAG):** External, up-to-date knowledge, relevant information from documents, databases, or APIs to answer specific questions.
*   **Available Tools:** Definitions of all the functions or built-in tools it can call (e.g., check_inventory, send_email).
*   **Structured Output:** Definitions on the format of the model's response, e.g. a JSON object.

Why It Matters: From Cheap Demo to Magical Product
--------------------------------------------------

The secret to building truly effective AI agents has less to do with the complexity of the code you write, and everything to do with the quality of the context you provide.

Building Agents is less about the code you write or framework you use. The difference between a cheap demo and a “magical” agent is about the quality of the context you provide. Imagine an AI assistant is asked to schedule a meeting based on a simple email:

> Hey, just checking if you’re around for a quick sync tomorrow.

**The "Cheap Demo" Agent** has poor context. It sees only the user's request and nothing else. Its code might be perfectly functional—it calls an LLM and gets a response—but the output is unhelpful and robotic:

> Thank you for your message. Tomorrow works for me. May I ask what time you had in mind?

**The "Magical" Agent** is powered by rich context. The code's primary job isn't to figure out _how_ to respond, but to _gather the information_ the LLM needs to full fill its goal. Before calling the LLM, you would extend the context to include

*   Your calendar information (which shows you're fully booked).
*   Your past emails with this person (to determine the appropriate informal tone).
*   Your contact list (to identify them as a key partner).
*   Tools for send_invite or send_email.

Then you can generate a response.

> Hey Jim! Tomorrow’s packed on my end, back-to-back all day. Thursday AM free if that works for you? Sent an invite, lmk if it works.

The magic isn't in a smarter model or a more clever algorithm. It’s in about providing the right context for the right task. This is why context engineering will matter. Agent failures aren't only model failures; they are context failures.

From Prompt to Context Engineering
----------------------------------

What is context engineering? While "prompt engineering" focuses on crafting the perfect set of instructions in a single text string, context engineering is a far broader. Let's put it simply:

> Context Engineering is the discipline of designing and building dynamic systems that provides the right information and tools, in the right format, at the right time, to give a LLM everything it needs to accomplish a task.

Context Engineering is

*   **A System, Not a String:** Context isn't just a static prompt template. It’s the output of a **system** that runs _before_ the main LLM call.
*   **Dynamic:** Created on the fly, tailored to the immediate task. For one request this could be the calendar data for another the emails or a web search.
*   **About the right information, tools at the right time:** The core job is to ensure the model isn’t missing crucial details ("Garbage In, Garbage Out"). This means providing both knowledge (information) and capabilities (tools) only when required and helpful.
*   **where the format matters:** How you present information matters. A concise summary is better than a raw data dump. A clear tool schema is better than a vague instruction.

Conclusion
----------

Building powerful and reliable AI Agents is becoming less about finding a magic prompt or model updates. It is about the engineering of context and providing the right information and tools, in the right format, at the right time. It’s a cross-functional challenge that involves understanding your business use case, defining your outputs, and structuring all the necessary information so that an LLM can “accomplish the task."

Acknowledgements
----------------

This overview was created with the help of deep and manual research, drawing inspiration and information from several excellent resources, including:

*   [Tobi Lutke tweet](https://x.com/tobi/status/1935533422589399127)
*   [Karpathy tweet](https://x.com/karpathy/status/1937902205765607626)
*   [The rise of "context engineering"](https://blog.langchain.com/the-rise-of-context-engineering/)
*   [Own your context window](https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md)
*   [context engineering by Simon Willison](https://simonwillison.net/2025/Jun/27/context-engineering/)
*   [Context Engineering for Agents](https://rlancemartin.github.io/2025/06/23/context_engineering/)

