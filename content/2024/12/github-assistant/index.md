---
title: github-assistant
date: 2024-12-27
extra:
  source: https://medium.com/relta/github-assistant-49ae388ad758
  original_title: github-assistant
---
## Summary
**摘要**：
github-assistant是一个由Relta、assistant-ui、dlt和LangGraph集成的GitHub API查询工具。它在10天内构建完成，能够以自然语言形式从GitHub仓库中查询结构化数据，并已预加载了一些流行开源项目的数据。这个工具基于Relta的语义层，能指导模型产生准确结果，并优于ChatGPT在某些查询方面。语义层通过预定义的指标（维度和度量）生成SQL，使得对于某些ChatGPT会虚构答案的问题，github-assistant仍能提供正确答案。程序架构包括前端助手、Relta中的语义层建模、dlt加载GitHub API数据、LangGraph作为代理框架，以及其他后端组件。此工具通过前端代理直接与用户交互，解答简单问题或调用Relta API获取数据查询的细节。语义层代理会根据用户反馈修改和创建SQL，Text-to-SQL代理则基于语义层生成SQL、执行并优化查询以获取结果答案。程序使用了Vercel、FastAPI、PostgreSQL等来部署各种组件和存储状态。

**要点总结**：
1. **集成工具**： github-assistant利用多种技术如assistant-ui、Relta、dlt和LangGraph，实现了用自然语言从GitHub仓库中查询数据的功能。
2. **语义层实现**： Relta提供了一个语义层，通过预建的指标和维度生成SQL，帮助程序理解和处理数据查询，解决了语法错误和代码生疏问题。
3. **性能和优化**： Relta规划未来将根据性能反馈和用户反馈调整优化语义层，通过自动代码生成和错误检测提高整体效率和准确性。
4. **大规模数据查询支持**： github-assistant支持处理大规模数据，并提供数据加载工具dlt来提取GitHub API内的数据。
5. **可视化组件整合**： 通过与助理UI集成，github-assistant能够生成动态可视化图表，在用户数据查询后用shadcn Charts展示结果。

**注解**：
- 该工具旨在简化数据开发工具（Datanames）的使用，使开发者能以普通英语查询和操作GitHub API内的结构化数据。
- 通过前端代理、内部SQL代理以及文本转SQL代理，github-assistant实现了一套过程，从用户交互到SQL执行和结果返回。
- Relta语义层是连接用户需求和实际数据处理的关键，使用DuckDB构建和维护视图，有效隔离和细化数据模型，集中于业务指标。
- 助理UI提供可视化图表的生成和展示，增强用户对数据的解读。
- 未来工作包括对GitHub数据的深入发掘、提高代理调用效率（转向本地运行机器学习模型）、支持图表存储至Dashboards等扩展功能。
## Full Content
Title: github-assistant - Relta - Medium

URL Source: https://medium.com/relta/github-assistant-49ae388ad758

Published Time: 2024-12-16T07:37:59.838Z

Markdown Content:
[![Image 22: Amir Zohrenejad](https://miro.medium.com/v2/resize:fill:44:44/0*g4-ZrF2WQmSCiCnF.jpg)](https://medium.com/@aazo11?source=post_page---byline--49ae388ad758--------------------------------)

[![Image 23: Relta](https://miro.medium.com/v2/resize:fill:24:24/1*URC8pi1t0j1l_yNoOu1OTQ.png)](https://medium.com/relta?source=post_page---byline--49ae388ad758--------------------------------)

[github-assistant](https://github-assistant.com/) answers questions from repository data available through the GitHub API. It was built in only 10 days using [Relta](https://www.relta.dev/), [assistant-ui](https://www.assistant-ui.com/), [dlt](https://dlthub.com/) and [LangGraph](https://www.langchain.com/langgraph). This is exciting. It shows that LLMs and data devtools have matured. With the right tools and without much effort, developers can let users query structured data in plain English.

This technology will enable new scenarios for users in the near future: search engines will answer questions from publicly available relational datasets such as the GitHub API. SaaS developers will embed conversational analytics into their products. AI agents will query and act on SQL data in their execution flows.

![Image 24](https://miro.medium.com/v2/resize:fit:267/1*wUZiI2Mg2cncuMWWXIiBgQ.png)

Results
-------

github-assistant currently loads Issues, Pull Requests, Stars, and Commits from GitHub. We have pre-loaded this data for a few popular open-source repos. You can load data for any open-source repo as well. Relta’s [semantic layer](https://github.com/reltadev/github-assistant/tree/main/server-poc/semantic_layer) acts as a guardrail to guide the model to correct results. Even with its current minimal [semantic layer](https://github.com/reltadev/github-assistant/tree/main/server-poc/semantic_layer) setup, the tool outperforms ChatGPT in a number of query types.

**Hallucinations**

The semantic layer provides tight guardrails in the form of pre-defined metrics (with dimensions and measures) to generate SQL from the relational data. As a result, github-assistant provides accurate results for some questions where ChatGPT would hallucinate.

The correct answer to the question above with the underlying calculation from github-assistant.

**Data availability**

ChatGPT only has access to data that it can crawl from GitHub webpages. This leaves a whole lot of data and insights inaccessible, even though they can be accessed from the GitHub API. The example below illustrates this for commit data on a repository.

Architecture
------------

[github-assistant](https://github.com/reltadev/github-assistant) is built on the following:

1.  [assistant-ui](https://www.assistant-ui.com/) on the front-end
2.  [Relta](https://www.relta.dev/) for semantic layer creation, refinement and text-to-sql
3.  [dlt](https://dlthub.com/) for loading data from the GitHub API
4.  [LangGraph](https://www.langchain.com/langgraph) as the agent framework (with LangSmith used for observability)

![Image 25](https://miro.medium.com/v2/resize:fit:700/0*QrMsc8nka5jfHR_I)

We use Vercel, FastAPI and and PostgreSQL on RDS and ECS + ECR for app hosting and state storage in various parts of the solution. The LLM used is OpenAI gpt-4o.

Meet the Agents
---------------

The heavy lifting of github-assistant is powered by three agents:

1.  **Front-end agent —** Communication with the user, directly answering simple questions (“What can you do?”) or calling Relta’s API for questions about data, as well as choosing the graph type and title for the query results.
2.  **Semantic-layer agent —** an agent within Relta which creates the first draft semantic layer from the DDL and sample questions. The agent suggests modifications to the semantic layer based on user feedback and automatically raises PRs on the repo.
3.  **Text-to-SQL agent —** an agent within Relta which uses the the semantic layer to generate SQL, execute it, repair if necessary and return the result or answer.

Loading the data with dlt
-------------------------

github-assistant uses dlt and its [verified sources](https://dlthub.com/docs/dlt-ecosystem/verified-sources/) to set up data pipelines to load the data from the GitHub graphql API. We made minimal changes to the dlt GitHub connector. Most of our work on the data pipelines was to create and persist logic around pipeline state.

With the rich set of source connectors in dlt, solutions such as shopify-assistant, googleads-assistant, asana-assistant can all be spun up using the same blueprint as github-assistant.

Relta’s Semantic Layer
----------------------

Semantic layers are not new. However, most software developers are not familiar with them and building one has been a manual iterative process. Relta simplifies this. The existing semantic layer was put together in less than an hour using questions we drafted for the data. Relta creates Views on a DuckDB instance based on this semantic layer and materializes these views by loading the raw data into DuckDB. This creates isolated databases where the data is modeled around the business metrics instead.

Based on performance and user feedback [Relta](https://relta.dev/) will propose changes to the semantic layer and automatically raise PRs on the repo which we will deploy to improve performance.

![Image 26](https://miro.medium.com/v2/resize:fit:700/1*CIgUiLnqvTxUve_kCGMtEg.png)

Relta semantic layer builder

We believe in the future producers of data will create and publish semantic layers together with their datasets that can be used by downstream application developers to set up natural language interfaces such as github-assistant from their data.

Generative Chart UIs powered by assistant-ui
--------------------------------------------

[assistant-ui](https://www.assistant-ui.com/) powers dynamic visualizations in github-assistant. After Relta returns SQL results, assistant-ui’s agent selects the appropriate chart type and generates a chart title. The results are then streamed to the client and displayed using [shadcn Charts](https://ui.shadcn.com/charts).

Next Steps
----------

We plan on continuing the work on github-assistant in a few ways:

1.  We are just scratching the surface of GitHub data. We want to crowd-source end user questions to add additional parts of the data to the semantic layer.
2.  Some of the LLM calls by the agents are for simple tasks (such as metric selection). We want to optimize LLM usage by moving these to small, locally run LLMs. We believe in local first and want to experiment with pushing everything to the browser.
3.  We want to support saving generated charts to dashboards.

If you are interested in contributing or learning more about Relta or assistant-ui we would to chat with you. Please reach out to amir \[at\] relta.dev or simon \[at\] assistant-ui.com

