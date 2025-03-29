---
title: Notes on MCP
date: 2025-03-29
extra:
  source: https://taoofmac.com/space/notes/2025/03/22/1900
  original_title: Notes on MCP
---
## Summary
**摘要**：
作者对Anthropic的MCP（Model Context Protocol）进行了一番体验，但对其印象不佳。作者认为MCP存在不必要的复杂性，其Python SDK充斥着层层包裹的访问器和装饰器，这些可以通过JSON和字典来简化。作者质疑为何需要创建新服务器来暴露现有API，而不是让LLM直接使用现有API。作者认为长期存在的REST和Swagger规范，可以简化为JSON模式，更适合工具定义。此外，作者还对MCP的安全性、访问控制表示担忧，认为过多精力被浪费在为每个API创建新服务器上，而不是利用现有API。MCP的设计是面向连接和有状态的，这使其不太适合API应用。作者认为其设计假定在本地运行大量服务器或使用有足够算力的服务器，这不适合AWS Lambda或Cloudflare Workers等无状态托管环境。作者指出MCP倾向于在模型上下文中塞入过多选项，缺乏设置优先级或展示MCP服务器元数据的清晰方法，导致浪费tokens和模型行为不稳定。作者认为MCP缺少某种形式的“路由”或逐步、选择性地暴露选项的机制。目前作者对MCP并不感冒，更倾向于使用标准工具调用和围绕端点发现的概念。

**要点总结**：
1.  **Pointless Complexity（不必要的复杂性）：** 作者认为 Anthropic 的 MCP 的 Python SDK 存在过度封装的问题，用了太多的 wrappers 、accessors 和 decorators，这些完全可以用简单的 JSON 和字典代替，使得代码库看起来像 Java 或 TypeScript，增加了不必要的复杂性。
2.  **Zero Re-use of Existing API Surfaces（对现有 API 接口的零重复利用）：** 作者质疑为什么不直接让 LLM 使用现有的 API，而是需要通过创建一个新的服务器来包装这些 API。作者认为，已经存在了很长时间的 REST 和 Swagger 规范，完全可以用来生成简化的 JSON schema，从而与通用的工具定义对齐。
3.  **Persistent Connections（持久连接）：** MCP 被设计成一种“通用”的 LLM 接口，但其面向连接和有状态的特性，使其不太适合基于 API 的应用。这种设计似乎假定用户要么在本地运行大量的服务器，要么连接到具有足够计算能力来运行有状态服务器的设备，这与当前 API 的使用方式不太相符，因为现在的 API 通常运行在像 AWS Lambda 或 Cloudflare Workers 这样的无状态托管环境中。
4.  **Too Many Options（过多的选项）：** MCP 倾向于在模型上下文中塞入过多的选项，而且缺乏清晰的方式来设置优先级或展示 MCP 服务器的元数据。这导致模型 API 调用会把 MCP 服务器能做的所有事情都塞进上下文，既浪费 tokens，又导致模型的行为不稳定。

## Full Content
Title: Notes on MCP

URL Source: https://taoofmac.com/space/notes/2025/03/22/1900

Published Time: 2025-03-22T19:00:00+00:00

Markdown Content:
[Mar 22nd 2025](https://taoofmac.com/space/notes/2025/03/22/1900) · 2 min read · #agents #ai #anthropic #api #integration #llm #mcp

I’ve been playing with [Anthropic’s MCP](https://docs.anthropic.com/en/docs/agents-and-tools/mcp?utm_source=taoofmac.com&utm_medium=web&utm_campaign=unsolicited_traffic&utm_content=external_link) for a little while now, and I have a few gripes. I understand it is undergoing a kind of [Cambrian explosion](https://www.reddit.com/r/mcp?utm_source=taoofmac.com&utm_medium=web&utm_campaign=unsolicited_traffic&utm_content=external_link) right now, but I am not very impressed with it. Maybe it’s echoes of [TRON](https://www.imdb.com/title/tt0084827?utm_source=taoofmac.com&utm_medium=web&utm_campaign=unsolicited_traffic&utm_content=external_link), but I can’t bring myself to like it.

[Pointless Complexity --------------------](https://taoofmac.com/space/notes/2025/03/22/1900#pointless-complexity)I was looking at [the Python SDK](https://github.com/modelcontextprotocol/python-sdk?utm_source=taoofmac.com&utm_medium=web&utm_campaign=unsolicited_traffic&utm_content=external_link), and all I could see was wrappers inside wrappers into accessors and decorators that could probably be replaced by a few snippets of JSON and a dictionary. I understand that cosplaying as Java developers (or, worse, TypeScript) is a common affliction in modern Python codebases, but I kept wondering exactly why I would need to create a new server to expose an existing API, which leads me to my next point:

[Zero Re-use of Existing API Surfaces ------------------------------------](https://taoofmac.com/space/notes/2025/03/22/1900#zero-re-use-of-existing-api-surfaces)If I want an LLM to use an existing service, why don’t I have the LLM just consume the API directly? Why do I need to create a new server that wraps the existing API? We have had REST and Swagger for a _long_ time now, and it would be a lot easier to just take a Swagger spec and generate a simplified JSON schema from it that aligned with the usual tool definitions. Maybe [FastOpenAPI](https://github.com/mr-fatalyst/fastopenapi?utm_source=taoofmac.com&utm_medium=web&utm_campaign=unsolicited_traffic&utm_content=external_link) would be a good fit for this, at least for some modern APIs.

I also don’t see a lot of emphasis on security, access control, or anything that would make me feel comfortable exposing an MCP server to an LLM. I get that this is a work in progress, but it feels like a lot of effort is being wasted on creating a new server for every API instead of just using the existing ones.

[Persistent Connections ----------------------](https://taoofmac.com/space/notes/2025/03/22/1900#persistent-connections)I get that MCP is being designed to be a kind of “universal” interface for LLMs, but the fact that it is connection-oriented and stateful means that it is not necessarily a good fit for API-based applications.

The design seems to assume you are either running a bunch of servers locally (as subprocesses, which, again, raises a few interesting security issues) or talking to something with enough compute power to run a stateful server, and isn’t really a good fit for the way we use APIs today, considering many are usually run in stateless hosting environments like AWS Lambda or Cloudflare Workers.

At least Anthropic had the good taste to use server-sent events (which is not popular with the SocketIO crowd, of course), but even if I remove the network component, the way local MCP servers are integrated and run as separate processes feels messy and wasteful (and don’t get me started on the overuse of `uv` or `uvx` to pack everything into isolated environments).

> **Update, a week later:** Well, [stateless connections are now possible](https://github.com/modelcontextprotocol/specification/pull/206?utm_source=taoofmac.com&utm_medium=web&utm_campaign=unsolicited_traffic&utm_content=external_link). Let’s see how that works out.

[Too Many Options ----------------](https://taoofmac.com/space/notes/2025/03/22/1900#too-many-options)My limited experimentation quickly surfaced another issue, which is that MCP tends to crowd the model context with too many options. There doesn’t seem to be a clear way to set priorities or a set of good examples to expose MCP server metadata–so your model API calls will just pack all the stuff an MCP server can do and shove it into the context, which is both wasteful of tokens and leads to erratic behavior from models.

I think MCP is missing some form of “routing” or stepwise, selective exposure of options, which would allow you to expose only the relevant options for a given task.

[Conclusion ----------](https://taoofmac.com/space/notes/2025/03/22/1900#conclusion)Right now, I’m not overly excited by MCP over “standard” tool calling. I much prefer [`agents.json`](https://docs.wild-card.ai/agentsjson/introduction?utm_source=taoofmac.com&utm_medium=web&utm_campaign=unsolicited_traffic&utm_content=external_link) and the concepts around endpoint discovery, which feel much more natural if you are working with APIs.

But of course everything around AI and LLMs is in a chaotic state of flux, and I’ve been around for long enough to know that the best ideas often take a while to surface. For now, I will most likely stick to standard tool calling.

