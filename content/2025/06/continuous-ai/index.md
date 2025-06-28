---
title: Continuous AI
date: 2025-06-28
extra:
  source: https://githubnext.com/projects/continuous-ai
  original_title: Continuous AI
---
## Summary
**摘要**：
GitHub Next提出的"Continuous AI"概念旨在将AI自动化无缝集成到软件协作中，类似于持续集成和持续部署（CI/CD）的广泛应用。该概念涵盖利用自动化AI增强软件协作的各项技术，包括持续文档生成、代码质量改进、问题分类、故障分析等任务，并强调这些任务应具备可自动化、可重复、协作性强、可集成和可审计等特性。不同于仅提升个人生产力，Continuous AI更注重团队协作效率，其实现依赖于GitHub Actions和GitHub Models的结合应用，以及相关工具如GenAIScript和llm框架的支持。该项目的长期愿景包括探索软件代理在GitHub上的应用、建立设计原则和模式，并与开源社区共同推进技术的发展。

**要点总结**：
1. **Continuous AI的定义与范畴**：Continuous AI是一个涵盖所有利用自动化AI支持软件协作的技术类别，与CI/CD类似，其目的是通过AI自动化提高协作效率。这包括持续文档生成、代码改进、问题分类等多种任务，这些任务需满足可自动化、可重复及协作性等特征。

2. **团队协作的核心定位**：不同于传统AI工具关注个人效率提升，Continuous AI强调团队协作的优化。其目标是通过自动化文档维护、代码质量检查等任务，减少人工负担，同时确保团队对AI工具的使用拥有完全控制权，实现透明和可审计的协作流程。

3. **技术实现与工具链**：Continuous AI的实现依赖GitHub Actions和GitHub Models的协同工作，结合如GenAIScript或llm等框架，可构建自动化工作流。例如，通过GitHub Actions调用AI模型完成代码生成或问题分类，并以开源社区为依托扩展功能。

4. **长期发展与行业协作**：GitHub Next将Continuous AI视为一个长达30年的技术演进方向，计划通过探索设计原则、与微软研究团队合作（如改进GenAIScript）、整合开源技术等方式推动发展。同时关注行业相关概念（如“AI工程生产力”）的动向，确保技术的前瞻性。
## Full Content
Title: GitHub Next | Continuous AI

URL Source: https://githubnext.com/projects/continuous-ai

Markdown Content:
The application of AI-enriched automation to software collaboration will soon be as seamless, multi-faceted and ubiquitous as Continuous Integration and Continuous Deployment (CI/CD) are today. We call this new frontier Continuous AI.

[](https://githubnext.com/projects/continuous-ai#what-is-continuous-ai)What is Continuous AI?
---------------------------------------------------------------------------------------------

Continuous AI is a label we've identified for **all uses of automated AI to support software collaboration on any platform**. Any use of automated AI to support any software collaboration on any platform anywhere is Continuous AI.

We've chosen the term "Continuous AI” to align with the established concept of Continuous Integration/Continuous Deployment (CI/CD). Just as CI/CD transformed software development by automating integration and deployment, Continuous AI covers the ways in which AI can be used to automate and enhance collaboration workflows.

“Continuous AI” is not a term GitHub owns, nor a technology GitHub builds: it's a term we use to focus our minds, and which we're introducing to the industry. This means Continuous AI is an open-ended set of activities, workloads, examples, recipes, technologies and capabilities; a category, rather than any single tool.

### [](https://githubnext.com/projects/continuous-ai#some-examples-of-continuous-ai)Some examples of Continuous AI

Some Continuous AI happens today in the industry, and more is appearing all the time. Some examples of Continuous AI we're seeing include:

*   **Continuous Documentation**: Continually populate and update documentation, offering suggestions for improvements.

*   **Continuous Code Improvement**: Incrementally improve code comments, tests and other aspects of code e.g. ensuring code comments are up-to-date and relevant.

*   **Continuous Triage**: Label, summarize, and respond to issues using natural language.

*   **Continuous Summarization**: Provide up-to-date summarization of content and recent events in the software projects.

*   **Continuous Fault Analysis**: Watch for failed CI runs and offer explanations of them with contextual insights.

*   **Continuous Quality**: Using LLMs to automatically analyze code quality, suggest improvements, and ensure adherence to coding standards.

*   **Continuous Team Motivation**: Turn PRs and other team activity into poetry, zines, podcasts; provide nudges, or celebrate team achievements.

*   **Continuous Accessibility**: Automatically check and improve the accessibility of code and documentation.

These tasks have characteristics in common:

*   They are **automatable**: They can be performed by AI with a high degree of reliability and accuracy.

*   They are **repetitive**: They involve ongoing tasks that benefit from automation, such as updating documentation or managing issues.

*   They are **collaborative**: They enhance team workflows and improve the overall software development process.

*   They are **integrated**: They can be seamlessly integrated into existing workflows and platforms, such as GitHub.

*   They are **auditable**: They can be monitored and controlled by teams and organizations, ensuring transparency, accountability and utility.

*   There are **many variants**: There are many different ways to implement these tasks, depending on the specific needs of the team or organization.

*   They are **event-triggered**: They can be triggered by events in the software development process, such as code changes, issue creation, or pull requests, and care must be taken to balance rate of triggering with other goals.

### [](https://githubnext.com/projects/continuous-ai#ai-for-collaboration-not-just-individual-productivity)AI for collaboration, not just individual productivity

Continuous AI is about using AI to enhance collaboration in software projects, not just individual productivity. It focuses on automating tasks that benefit teams, such as documentation, code quality, issue management, and team motivation. The goal is to create a more efficient and enjoyable collaborative environment.

Individual productivity is important, but team productivity introduces new opportunities and considerations. For example, AI code generation by individuals can shift burdens to other team members, or to later stages in software projects. Continuous AI is thus partly about the collective impact of AI on software projects.

Teams and organisations must be in control of the Continuous AI they use: the models and automations used, how they are invoked, and how they integrate with their workflows.

### [](https://githubnext.com/projects/continuous-ai#continuous-ai-and-github)Continuous AI and GitHub

On GitHub today, Continuous AI is supported in initial form by the combination of [GitHub Actions](https://github.com/features/actions) and [GitHub Models](https://github.com/features/models). The synergy between these features is at the core of Continuous AI at GitHub.

These two features can be used in combination with LLM programming frameworks such as [GenAIScript](https://microsoft.github.io/genaiscript/), [llm](https://llm.datasette.io/) or [ell](https://github.com/MadcowD/ell). Simple Continuous AI tasks can be built using workflows alone using the [ai-inference action](https://github.com/actions/ai-inference) alone, and the [gh models](https://github.com/github/gh-models) CLI extension is useful for interacting with Models. Together these tools allow developers to create automated workflows that leverage LLMs for tasks like code generation, documentation, and issue management.

In CI/CD, GitHub empowers our customers through GitHub Actions. We expect the same to be true for Continuous AI. Like CI/CD, most Continuous AI technologies will be 3rd party OSS tools and actions. The broader GitHub and OSS communities are a crucial part of Continuous AI at GitHub. Certain capabilities and features of GitHub will support Continuous AI, and GitHub will improve these capabilities over time. Some existing capabilities of the GitHub platform relevant to Continuous AI include integrated authentication, access control, secrets, security scanning, model evals, code search, semantic indexing and code scanning.

We expect Continuous AI to be a story that runs for 30+ years at GitHub, just like CI/CD.

### [](https://githubnext.com/projects/continuous-ai#how-does-continuous-ai-relate-to-agents)How does Continuous AI relate to agents?

One vision for Continuous AI at GitHub is that the GitHub platform can be a good “home” for software agents - that is, for all agent-like things whose main interaction is with software repos and collaboration.

Continuous AI can involve fully autonomous AI agents, but more often centres on scripted “agent-like” AI workflows. Often these workflows are not fully autonomous, but rather involve human oversight and control. They tend to make targeted, reliable use of AI to automate specific tasks in software collaboration, rather than creating fully autonomous agents that operate arbitrarily.

### [](https://githubnext.com/projects/continuous-ai#what-is-the-continuous-ai-project-at-github-next)What is the Continuous AI project at GitHub Next?

The Continuous AI project at GitHub Next is about

*   Introducing the term to the industry.

*   Giving it some meaning by examples, design principles and patterns.

*   Exploring some of what can already be done today on GitHub.

*   Identifying new and existing platform capabilities, opportunities and alignments.

*   Exploring what it means for agents to have their “home” on GitHub.

*   Identifying existing open source Continuous AI technologies in the industry.

*   Nudging existing Continuous AI technologies towards GitHub Models and Actions.

*   Identifying possible [Horizon 2 and 3](https://en.wikipedia.org/wiki/Three_Horizons) manifestations of Continuous AI.

Additionally we are collaborating with Microsoft Research on [GenAIScript](https://microsoft.github.io/genaiscript/), to improve its capabilities for Continuous AI on GitHub, and using it to deliver some of our Continuous AI examples.

Continuous AI has much in common with nascent industry terms such as “AI Engineering Productivity” and “Augmented Engineering” and we are watching closely what other teams in industry are contributing to this space.

### [](https://githubnext.com/projects/continuous-ai#playing-with-continuous-ai-today)Playing with Continuous AI today

Continuous AI is a broad, long-term agenda and will have many manifestations. To play with some Continuous AI on GitHub today, a very simple way is to use [actions/ai-inference](https://github.com/actions/ai-inference) from a GitHub Actions workflow in your favourite repository.

You can also use the [`llm` framework](https://llm.datasette.io/en/stable/) in combination with the [`llm-github-models` extension](https://github.com/tonybaloney/llm-github-models) to create LLM-powered GitHub Actions which use GitHub Models using Unix shell scripting.

Many Continuous AI workflows will need more complex programming. One approach is to start with the [GenAIScript framework](https://microsoft.github.io/genaiscript/), and use it to create [GitHub Actions](https://microsoft.github.io/genaiscript/getting-started/automating-scripts/#github-action). GenAIScript provides a way to create and run AI-powered scripts that can automate various tasks in your GitHub repositories. Some specific examples of Continuous AI are included in the [samples](https://microsoft.github.io/genaiscript/samples/). See also [GitHub Actions with GenAIScript](https://microsoft.github.io/genaiscript/reference/github-actions/) reference material.

Actions programmed with any of the above techniques can be packaged into [GitHub Actions](https://docs.github.com/en/actions/creating-actions) and shared with the community. One example of doing this with GenAIScript is this [issue labeller](https://github.com/pelikhan/action-genai-issue-labeller) which implemented a very simple form of Continuous Triage, using GitHub Models to label issues based on their content via GenAIScript.

Watch this space and the GitHub blogs for more details!

