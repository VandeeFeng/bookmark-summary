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
