# Notes on MCP
- URL: https://taoofmac.com/space/notes/2025/03/22/1900
- Added At: 2025-03-29 06:17:36
- [Link To Text](2025-03-29-notes-on-mcp_raw.md)

## Summary
**摘要**：
作者对Anthropic的MCP（Model Context Protocol）进行了一番体验，但对其印象不佳。作者认为MCP存在不必要的复杂性，其Python SDK充斥着层层包裹的访问器和装饰器，这些可以通过JSON和字典来简化。作者质疑为何需要创建新服务器来暴露现有API，而不是让LLM直接使用现有API。作者认为长期存在的REST和Swagger规范，可以简化为JSON模式，更适合工具定义。此外，作者还对MCP的安全性、访问控制表示担忧，认为过多精力被浪费在为每个API创建新服务器上，而不是利用现有API。MCP的设计是面向连接和有状态的，这使其不太适合API应用。作者认为其设计假定在本地运行大量服务器或使用有足够算力的服务器，这不适合AWS Lambda或Cloudflare Workers等无状态托管环境。作者指出MCP倾向于在模型上下文中塞入过多选项，缺乏设置优先级或展示MCP服务器元数据的清晰方法，导致浪费tokens和模型行为不稳定。作者认为MCP缺少某种形式的“路由”或逐步、选择性地暴露选项的机制。目前作者对MCP并不感冒，更倾向于使用标准工具调用和围绕端点发现的概念。

**要点总结**：
1.  **Pointless Complexity（不必要的复杂性）：** 作者认为 Anthropic 的 MCP 的 Python SDK 存在过度封装的问题，用了太多的 wrappers 、accessors 和 decorators，这些完全可以用简单的 JSON 和字典代替，使得代码库看起来像 Java 或 TypeScript，增加了不必要的复杂性。
2.  **Zero Re-use of Existing API Surfaces（对现有 API 接口的零重复利用）：** 作者质疑为什么不直接让 LLM 使用现有的 API，而是需要通过创建一个新的服务器来包装这些 API。作者认为，已经存在了很长时间的 REST 和 Swagger 规范，完全可以用来生成简化的 JSON schema，从而与通用的工具定义对齐。
3.  **Persistent Connections（持久连接）：** MCP 被设计成一种“通用”的 LLM 接口，但其面向连接和有状态的特性，使其不太适合基于 API 的应用。这种设计似乎假定用户要么在本地运行大量的服务器，要么连接到具有足够计算能力来运行有状态服务器的设备，这与当前 API 的使用方式不太相符，因为现在的 API 通常运行在像 AWS Lambda 或 Cloudflare Workers 这样的无状态托管环境中。
4.  **Too Many Options（过多的选项）：** MCP 倾向于在模型上下文中塞入过多的选项，而且缺乏清晰的方式来设置优先级或展示 MCP 服务器的元数据。这导致模型 API 调用会把 MCP 服务器能做的所有事情都塞进上下文，既浪费 tokens，又导致模型的行为不稳定。

