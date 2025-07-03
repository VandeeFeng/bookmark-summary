---
title: Writing Code Was Never The Bottleneck
date: 2025-07-03
extra:
  source: https://ordep.dev/posts/writing-code-was-never-the-bottleneck
  original_title: Writing Code Was Never The Bottleneck
---
## Summary
**摘要**：  
文章指出，在软件开发中，编写代码从来不是真正的瓶颈，真正的瓶颈在于代码审查、知识传递、测试、调试以及团队协作与沟通。尽管LLM（大型语言模型）的兴起使代码生成变得快速便捷，但并未减少理解、验证和维护代码的工作量。LLM虽然加快了代码生成的初期速度，但可能导致代码质量下降、维护成本增加，并给代码审查者和团队成员带来更大压力。软件工程的核心挑战仍然是团队间的信任、共享理解和代码质量保证，这些基础问题并未因技术进步而消失。文章强调，理解代码和团队协作仍然是当前软件开发中的主要瓶颈。

**要点总结**：  
1. **真正的开发瓶颈不是编写代码**：软件工程中的主要瓶颈是代码审查、知识传递、测试、调试以及团队协作与沟通，而非单纯编写代码。这些环节需要更多的思考与协调。  
2. **LLM并未解决代码理解与维护的问题**：虽然LLM加快了代码生成速度，但代码的验证、理解和长期维护成本反而增加，尤其是当生成的代码不符合团队规范或引入未知隐患时。  
3. **团队信任与共享理解仍然是关键**：软件开发依赖团队间的协作、共识和知识传递，快速生成的代码可能削弱代码审查的有效性，导致质量不可控。  
4. **LLM无法替代清晰的思考和设计**：尽管LLM提升了原型开发效率，但代码的可维护性和正确性仍然需要人为的深入思考、严格审查和精心设计，这些仍然是开发流程的核心挑战。
## Full Content
Title: Writing Code Was Never The Bottleneck

URL Source: https://ordep.dev/posts/writing-code-was-never-the-bottleneck

Published Time: 2025-06-30T00:00:00+00:00

Markdown Content:
For years, I’ve felt that writing lines of code _was never_ the bottleneck in software engineering.

The actual bottlenecks were, and still are, **code reviews**, **knowledge transfer** through mentoring and pairing, **testing**, **debugging**, and the human overhead of **coordination and communication**. All of this wrapped inside the labyrinth of tickets, planning meetings, and agile rituals.

These processes, meant to drive quality, often slow us down more than the act of writing code itself because they require thought, shared understanding, and sound judgment.

Now, with LLMs making it easy to generate working code faster than ever, a new narrative has emerged: that writing code _was_ the bottleneck, and we’ve finally cracked it.

But that’s **not quite right**.

The marginal cost of adding new software is approaching **zero**, especially with LLMs. But what is the price of _understanding_, _testing_, and _trusting_ that code? **Higher than ever**.

* * *

LLMs shift the workload — they don’t remove it
----------------------------------------------

Tools like Claude can speed up initial implementation. Still, the result is often more code flowing through systems and more pressure on the people responsible for reviewing, integrating, and maintaining it.

This becomes especially clear when:

*   It’s unclear whether the author fully understands what they submitted.
*   The generated code introduces unfamiliar patterns or breaks established conventions.
*   Edge cases and unintended side effects aren’t obvious.

We end up in a situation where code is more straightforward to produce but more complex to verify, which doesn’t necessarily make teams move faster overall.

It’s not a new challenge. Developers have long joked about **“copy-paste engineering”**, but the velocity and scale that LLMs enable have **amplified those copy-paste habits**.

* * *

Understanding code is still the hard part
-----------------------------------------

> _“The biggest cost of code is understanding it — not writing it.”_

LLMs reduce the time it takes to produce code, but they haven’t changed the amount of effort required to reason about behavior, identify subtle bugs, or ensure long-term maintainability. That work can be even more challenging when reviewers struggle to distinguish between generated and handwritten code or understand why a particular solution was chosen.

* * *

Teams still rely on trust and shared context
--------------------------------------------

Software engineering has always been collaborative. It depends on **shared understanding**, **alignment**, and **mentoring**. However, when code is generated faster than it can be discussed or reviewed, teams risk falling into a mode where **quality is assumed rather than ensured**. That creates stress on reviewers and mentors, potentially slowing things down in more subtle ways.

* * *

LLMs are powerful — but they don’t fix the fundamentals
-------------------------------------------------------

There’s real value in faster prototyping, scaffolding, and automation. But LLMs don’t remove the need for **clear thinking**, **careful review**, and **thoughtful design**. If anything, those become even more important as more code gets generated.

Yes, the cost of writing code has indeed dropped. But the cost of making sense of it together as a team **hasn’t**.

**That’s still the bottleneck. Let’s not pretend it isn’t.**

