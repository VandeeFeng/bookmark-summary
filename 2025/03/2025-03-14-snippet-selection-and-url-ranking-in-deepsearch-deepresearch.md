# Snippet Selection and URL Ranking in DeepSearch/DeepResearch
- URL: https://jina.ai/news/snippet-selection-and-url-ranking-in-deepsearch-deepresearch/
- Added At: 2025-03-14 05:55:26
- [Link To Text](2025-03-14-snippet-selection-and-url-ranking-in-deepsearch-deepresearch_raw.md)

## Summary
**摘要**：
本文深入探讨了在 DeepSearch/DeepResearch 系统中提高搜索质量的两个关键细节：利用 late-chunking embeddings 进行网页内容片段选择，以及使用 rerankers 对 URL 进行排序。文章指出，尽管 embeddings 和 rerankers 在传统认知中并非 DeepSearch 的核心组成部分，但通过创新应用，它们在片段选择和 URL 排序方面发挥了重要作用。针对长网页内容片段选择问题，文章提出了结合 jina-embeddings-v3 和 late-chunking 的方法，该方法能够有效解决传统 chunking 方法中存在的上下文丢失和边界问题。在 URL 排序方面，文章提出了一种综合考虑频率信号、路径结构、语义相关性、最后更新时间和内容可访问性等因素的排序方法，以引导 LLM 选择最相关的 URL。通过这种方式，DeepSearch 系统能够更有效地利用 LLM 的推理能力，提升搜索结果的质量。文章最后总结了 DeepSearch 的架构，提出了一种双过程理论，将搜索工程分为快速思考、慢速思考和中间思考三个层次，并探讨了 embeddings 和 rerankers 在这种架构中的角色转变。

**要点总结**：

1.  **Late-Chunking Embeddings for Snippet Selection：**
    针对从长网页中选择相关内容片段的问题，传统的将文档分割成小块（chunking）的方法会丢失上下文信息，导致效果不佳。而 "late-chunking"技术首先对整个长文本进行嵌入（embedding），然后再进行分块，从而保留了每个 chunk 的上下文信息，解决了传统 chunking 的问题。结合 `jina-embeddings-v3` 模型，能够更好地选择与查询相关的片段，提高知识提取的准确性。
2.  **URL Ranking Based on Multiple Factors：**
    在 DeepSearch 过程中，系统会收集到大量的 URL，但并非所有 URL 都与搜索目标相关。为了提高效率，需要对 URL 进行排序。文章介绍了一种综合排序方法，考虑了 URL 的多个维度，包括频率信号（URL 在不同来源中出现的次数，以及域名在搜索结果中出现的频率）、路径结构（URL 的层级结构）、语义相关性（URL 与查询的语义相关程度，通过 `jina-reranker-v2-base-multilingual` 模型评估）、最后更新时间（优先考虑最近更新的 URL）和内容可访问性（排除需要登录或付费才能访问的 URL）。
3.  **In-Context Application of Embeddings and Rerankers：**
    文章强调，改进的这两个关键点都是在小规模的"in-context"环境下使用多语言嵌入和rerankers，这与传统的使用这些模型构建预计算索引的方式不同。这种方法更侧重于在LLM的上下文窗口内直接应用这些模型，以实现更精细的控制和优化。
4.  **Dual-Process Theory in Search Engineering：**
    文章提出了一个类似于卡尼曼双过程理论的框架来理解搜索工程的未来发展方向。这个框架包括：快速思考（grep, BM25, SQL，快速的模式匹配）、慢速思考（LLM，需要大量计算的深度上下文理解）和中间思考（embeddings, rerankers，用于过滤、去重和排序等任务）。未来，轻量级的SQL/BM25可能直接与LLM结合，而中间思考模型的角色可能会转变为仅在上下文相关的任务中使用。

