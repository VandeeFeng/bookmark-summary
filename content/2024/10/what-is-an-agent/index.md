---
title: What is an agent?
date: 2024-10-22
extra:
  source: https://blog.langchain.dev/what-is-an-agent/
  original_title: What is an agent?
---
## TL;DR
作者认为代理一词并非指一个明确的事物，而是一系列使用大型语言模型（LLM）控制程序流程的事物。可以将代理看做一个谱系，拥有从简单路由系统到复杂自治系统等的多种可能性。还提到了开发过程的工具和平台 LANGGRAPH 和 LANGSMITH，及其在开发过程的重要性。
## Summary
**摘要**

这篇文章探讨了“代理（agent）”的概念及其定义。作者认为代理是一种使用大型语言模型（LLM）来决定应用程序控制流程的系统。然而，代理的定义并非一致，人们对代理的期望也各不相同。因此，作者采用了Andrew Ng的观点，将代理的能力视为一个谱系，而不是一个明确的定义。文章讨论了代理的程度，从简单的路由系统到复杂的自治系统，并强调了代理能力谱系的概念及其在开发过程中的重要性。作者还介绍了LangChain团队为支持代理开发而构建的工具和平台，包括LangGraph和LangSmith。

**要点总结**

1. **代理的定义**: 代理是一种使用大型语言模型（LLM）来决定应用程序控制流程的系统。
2. **代理能力谱系**: 代理的能力可以被视为一个谱系，而不是一个明确的定义，从简单的路由系统到复杂的自治系统。
3. **代理的程度**: 代理可以具有不同的程度，包括路由器、状态机和自治代理。
4. **代理的重要性**: 代理能力谱系的概念在开发过程中至关重要，它可以指导决策，帮助设计和开发更加复杂的代理系统。
5. **新工具和基础设施**: 随着代理能力的增加，需要新的工具和基础设施来支持代理开发，LangChain团队为此构建了LangGraph和LangSmith等工具和平台。
## Full Content
Title: What is an agent?

URL Source: https://blog.langchain.dev/what-is-an-agent/

Published Time: 2024-06-29T01:01:01.000Z

Markdown Content:
_“What is an agent?”_

I get asked this question almost daily. At LangChain, we build tools to help developers build LLM applications, especially those that act as a reasoning engines and interact with external sources of data and computation. This includes systems that are commonly referred to as “agents”.

Everyone seems to have a slightly different definition of what an agent is. My definition is perhaps more technical than most:

💡

An agent is a system that uses an LLM to decide the control flow of an application.

Even here, I’ll admit that my definition is not perfect. People often think of agents as advanced, autonomous, and human-like — but what about a simple system where an LLM routes between two different paths? This fits my technical definition, but not the common perception of what an agent should be capable of. It’s hard to define _exactly_ what an agent is!

That’s why I really liked Andrew Ng’s [tweet last week](https://x.com/AndrewYNg/status/1801295202788983136?ref=blog.langchain.dev). In it he suggests that “rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic.” Just like autonomous vehicles, for example, have levels of autonomy, we can also view agent capabilities as a spectrum. I really agree with this viewpoint and I think Andrew expressed it nicely. In the future, when I get asked about what an agent is, I will instead turn the conversation to discuss what it means to be “agentic”.

What does it mean to be agentic?
--------------------------------

I gave a TED talk last year about LLM systems and used the slide below to talk about the different levels of autonomy present in LLM applications.

![Image 1](https://blog.langchain.dev/content/images/2024/06/Screenshot-2024-06-28-at-7.33.10-PM.png)

A system is more “agentic” the more an LLM decides how the system can behave.

Using an LLM to route inputs into a particular downstream workflow has some small amount of “agentic” behavior. This would fall into the `Router` category in the above diagram.

If you do use multiple LLMs to do multiple routing steps? This would be somewhere between `Router` and `State Machine`.

If one of those steps is then determining whether to continue or finish - effectively allowing the system to run in a loop until finished? That would fall into `State Machine`.

If the system is building tools, remembering those, and then taking those in future steps? That is similar to what the [Voyager paper](https://arxiv.org/abs/2305.16291?ref=blog.langchain.dev) implemented, and is incredibly agentic, falling into the higher `Autonomous Agent` category.

These definitions of “agentic” are still pretty technical. I prefer the more technical definition of “agentic” because I think it’s useful when designing and describing LLM systems.

Why is “agentic” a helpful concept?
-----------------------------------

As with all concepts, it’s worth asking why we even need the concept of “agentic”. What does it help with?

Having an idea of how agentic your system can guide your decision-making during the development process - including building it, running it, interacting with it, evaluating it, and even monitoring it.

The more agentic your system is, the more an orchestration framework will help. If you are designing a complex agentic system, having a framework with the right abstractions for thinking about these concepts can enable faster development. This framework should have first-class support for branching logic and cycles.

The more agentic your system is, the harder it is to run. It will be more and more complex, having some tasks that will take a long time to complete. This means you will want to run jobs as background runs. This also means you want durable execution to handle any errors that occur halfway through.

The more agentic your system is, the more you will want to interact with it while it’s running. You’ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time. You’ll want the ability to modify the state or instructions of the agent at a particular point in time, to nudge it back on track if it’s deviating from the intended path.

The more agentic your system is, the more you will want an evaluation framework built for these types of applications. You’ll want to run evals multiple times, since there is compounding amount of randomness. You’ll want the ability to test not only the final output but also the intermediate steps to test how efficient the agent is behaving.

The more agentic your system is, the more you will want a new type of monitoring framework. You’ll want the ability to drill down into all the steps an agent takes. You’ll also want the ability to query for runs based on steps an agent takes.

Understanding and leveraging the spectrum of agentic capabilities in your system can improve the efficiency and robustness of your development process.

Agentic is new
--------------

One thing that I often think about is what is _actually new_ in all this craze. Do we need new tooling and new infrastructure for the LLM applications people are building? Or will generic tools and infrastructure from pre-LLM days suffice?

To me, the more agentic your application is, the more critical it is to have new tooling and infrastructure. That’s exactly what motivated us to build [LangGraph](https://www.langchain.com/langgraph?ref=blog.langchain.dev), the agent orchestrator to help with building, running, and interacting with agents, and [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.dev), the testing and observability platform for LLM apps. As we move further on the agentic spectrum, the entire ecosystem of supportive tooling needs to be reimagined.

### Join our newsletter

Updates from the LangChain team and community

Enter your email

Processing your application...

Success! Please check your inbox and click the link to confirm your subscription.

Sorry, something went wrong. Please try again.

