# Introducing AutoRAG: fully managed Retrieval-Augmented Generation on Cloudflare
- URL: https://blog.cloudflare.com/introducing-autorag-on-cloudflare/
- Added At: 2025-04-10 06:53:12
- [Link To Text](2025-04-10-introducing-autorag-fully-managed-retrieval-augmented-generation-on-cloudflare_raw.md)

## Summary
**摘要**：
文章宣布了Cloudflare上开放测试的AutoRAG，这是一个完全托管的检索增强生成（RAG）管道，旨在简化开发者将上下文感知AI集成到应用程序中的方式。RAG通过从用户自己的数据中检索信息，并将其提供给大型语言模型（LLM）来生成更可靠的响应，从而提高AI响应的准确性。AutoRAG通过自动分块和嵌入数据，将向量存储在Cloudflare的Vectorize数据库中，执行语义检索，并使用Workers AI生成高质量的响应，从而提供端到端的完全托管的RAG管道。AutoRAG持续监视用户的数据源并在后台建立索引，因此用户的AI可以保持最新状态，而无需手动操作。文章还介绍了AutoRAG的工作原理，包括索引和查询过程。索引是将内容转换为向量以进行语义搜索的异步过程，而查询是在用户发送搜索请求时触发的同步过程。此外，文章还提供了一个快速入门指南，展示了如何使用Browser Rendering API抓取网站内容并将其输入到AutoRAG中进行问答。AutoRAG免费启用，但会根据用户对R2、Vectorize、Workers AI和AI Gateway等Cloudflare资源的实际使用情况进行计费。Cloudflare计划在2025年扩展AutoRAG的功能，包括更多数据源集成和更高质量的响应。

**要点总结**：

1.  **AutoRAG 简化了 RAG 流程**：AutoRAG 是一个完全托管的 RAG 管道，它简化了在应用程序中集成上下文感知 AI 的过程，开发者无需手动组合各种工具和服务，如数据存储、向量数据库、嵌入模型和 LLM，即可构建 RAG 管道。它通过自动化数据索引和持续监控，减轻了开发者的维护负担，使他们能够专注于构建更智能的应用程序。
2.  **RAG 提升了 LLM 的准确性**：RAG 是一种通过检索用户自有数据中的相关信息来增强 LLM 回复准确性的方法。它通过将检索到的信息与用户查询相结合，并将其输入到 LLM 中，生成基于用户数据的回复，从而解决了LLM 在处理新信息、专有信息或特定领域信息时可能出现的知识盲区问题。
3.  **AutoRAG 的核心是索引和查询**：AutoRAG 的运作依赖于两个主要过程：索引和查询。索引是一个在后台运行的异步过程，负责将数据转换为向量，以便进行语义搜索。查询是一个在用户发送搜索请求时触发的同步过程，负责检索相关内容并生成 AI 回复。
4.  **Browser Rendering API 扩展了数据源**：Browser Rendering API 允许用户抓取网站内容，并将其用于 AutoRAG 中，从而扩展了 AutoRAG 可以使用的数据源类型。通过 Cloudflare Worker 渲染网页并上传到 R2 存储桶，用户可以将动态网页内容纳入 RAG 流程中。
5.  **AutoRAG 基于 Cloudflare 平台构建**：AutoRAG 构建于 Cloudflare 的开发者平台之上，利用 R2 存储、Vectorize 向量数据库、Workers AI 和 AI Gateway 等服务。用户在使用 AutoRAG 时，需要为这些 Cloudflare 资源的使用付费。

