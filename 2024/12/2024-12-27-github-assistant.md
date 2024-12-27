# github-assistant
- URL: https://medium.com/relta/github-assistant-49ae388ad758
- Added At: 2024-12-27 05:05:33
- [Link To Text](2024-12-27-github-assistant_raw.md)

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
