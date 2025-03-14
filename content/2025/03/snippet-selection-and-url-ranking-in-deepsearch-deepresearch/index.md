---
title: Snippet Selection and URL Ranking in DeepSearch/DeepResearch
date: 2025-03-14
extra:
  source: https://jina.ai/news/snippet-selection-and-url-ranking-in-deepsearch-deepresearch/
  original_title: Snippet Selection and URL Ranking in DeepSearch/DeepResearch
---
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

## Full Content
Title: Snippet Selection and URL Ranking in DeepSearch/DeepResearch

URL Source: https://jina.ai/news/snippet-selection-and-url-ranking-in-deepsearch-deepresearch/

Published Time: 2025-03-12T14:20:43.000+01:00

Markdown Content:
[A Practical Guide to Implementing DeepSearch/DeepResearch QPS out, depth in. DeepSearch is the new norm. Find answers through read-search-reason loops. Learn what it is and how to build it. ![Image 1](https://jina-ai-gmbh.ghost.io/content/images/icon/favicon-128x128-22.png)Han Xiao ![Image 2](https://jina-ai-gmbh.ghost.io/content/images/thumbnail/a-practical-guide-to-implementing-deepsearch-deepresearch-1.webp)](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch)

If you've already read our DeepSearch/DeepResearch implementation guide, let's dive deeper into some details that can _greatly_ improve quality. In this post, we'll focus on two key challenges: **using** [**late-chunking**](https://jina.ai/news/late-chunking-in-long-context-embedding-models) **embeddings for snippet selection from lengthy webpages** and **using rerankers to prioritize URLs before crawling.**

Some might recall our previous conclusion stating that "embeddings were only useful for query deduplication like STS tasks (semantic textual similarity), while rerankers weren't even part of our original DeepSearch implementation." Well, it turns out both are still quite valuable - just not in the conventional way one might expect. We've always followed the _leanest_ possible path. We don't add components just to justify their existence or our value as an embedding & reranker provider. **We're based - about what search really needs at its foundation.**

So after weeks iterations, we've discovered uncommon yet effective uses for both in DeepSearch/DeepResearch systems. By applying them, we've significantly improved the quality of [Jina DeepSearch](https://search.jina.ai/) (feel free to try it). We'd like to share these insights with fellow practitioners working in this space.

[](https://jina.ai/news/snippet-selection-and-url-ranking-in-deepsearch-deepresearch/#select-snippet-from-long-content "Select Snippet From Long Content")Select Snippet From Long Content
--------------------------------------------------------------------------------------------------------------------------------

The problem is this: after [using Jina Reader to read webpage content](https://jina.ai/reader), we need to add it as a knowledge item to the agent's context for reasoning. While dumping the full content into the LLM's context is the simplest way, it's not optimal when considering token costs and generation speed. In practice, we need to identify which parts of the content are most relevant to the question and selectively add only those parts as knowledge to the agent's context.

💡

We're talking about the cases where content remains too lengthy even after Jina Reader's markdown cleaning. This occurs often with long pages like GitHub issues, Reddit threads, forum discussions, and blog posts (including many of our own from jina.ai/news).

LLM-based filtering has the same cost and latency issues, so let's find solutions of smaller models: we need smaller and cheaper, **yet still multilingual models** – a crucial factor since we can't guarantee either the query or the documents will always be in English.

We have a question on one side (either the original query or a gap question) and a large markdown content on the other side, where most content is irrelevant. We need to select the most relevant snippets for the query. This resembles the chunking problem the RAG community has grappled with since 2023 - retrieving only relevant chunks using retriever models to place in the context window for summarization. However, there are two key differences in our case:

1.  Limited chunks from limited number of documents. If each chunk contains roughly 500 tokens, then a typical long web document has around 200,000 tokens (p50) to 1,000,000 tokens (p99), and we use Jina Reader to fetch 4-5 URLs each step, this would yield approximately hundreds of chunks - meaning hundreds of embedding vectors and hundreds of cosine similarities. This is easily manageable with in-memory JavaScript without a vector database.
2.  We need consecutive chunks to form effective knowledge snippets. We can't accept snippets combining scattered sentences like `[1-2, 6-7, 9, 14, 17, ...].` A more useful knowledge snippet would follow patterns like `[3-15, 17-24, ...]` - always maintaining consecutive text. This makes it easier for the LLM to copy and cite from the knowledge source and reduces hallucination.

The rest is all the caveats practitioners complained about: each chunk can't be too long since embedding models can't handle long context well; chunking introduces context loss and makes chunk embeddings i.i.d; and how to even find the best boundary cues that maintain both readability and semantics? If you know what we're talking about, then you've likely been haunted by these issues in your RAG implementations.

But long story short - **late-chunking with [jina-embeddings-v3](https://jina.ai/?sui&model=jina-embeddings-v3) beautifully solves all three problems.** Late chunking maintains the context info for each chunk, is [insensitive to boundary cues](https://jina.ai/news/what-late-chunking-really-is-and-what-its-not-part-ii#late-chunking-is-resilient-to-poor-boundary-cues), and [jina-embeddings-v3](https://jina.ai/?sui&model=jina-embeddings-v3) itself is SOTA in _asymmetric_ multilingual retrieval tasks. Interested readers can follow our blog posts or papers for details, but here's the overall implementation.

![Image 3: Flow chart for "Snippet Selection with Late Chunking" outlining steps 1-5, including embedding with Jina and similarity scori](https://jina-ai-gmbh.ghost.io/content/images/2025/03/Untitled-design--14-.svg)

This diagram illustrates the snippet selection algorithm, which works similarly to `Conv1D`. The process begins by splitting a long document into fixed-length chunks, which are then embedded with [jina-embeddings-v3](https://jina.ai/?sui&model=jina-embeddings-v3) with late-chunking toggle on. After calculating similarity scores between each chunk and the query, a sliding window moves across the similarity scores to find the window with the highest average value.

[What Late Chunking Really Is & What It’s Not: Part II Part 2 of our exploration of Late Chunking, a deep dive into why it is the best method for chunk embeddings and improving search/RAG performance. ![Image 4](https://jina-ai-gmbh.ghost.io/content/images/icon/favicon-128x128-23.png)Jina AIHan Xiao ![Image 5](https://jina-ai-gmbh.ghost.io/content/images/thumbnail/what-late-chunking-really-is-and-what-its-not-part-ii.webp)](https://jina.ai/news/what-late-chunking-really-is-and-what-its-not-part-ii)

[jina-embeddings-v3: Multilingual Embeddings With Task LoRA We introduce jina-embeddings-v3, a novel text embedding model with 570 million parameters, achieves state-of-the-art performance on multilingual data and long-context retrieval tasks, supporting context lengths of up to 8192 tokens. The model includes a set of task-specific Low-Rank Adaptation (LoRA) adapters to generate high-quality embeddings for query-document retrieval, clustering, classification, and text matching. Evaluation on the MTEB benchmark shows that jina-embeddings-v3 outperforms the latest proprietary embeddings from OpenAI and Cohere on English tasks, while achieving superior performance compared to multilingual-e5-large-instruct across all multilingual tasks. With a default output dimension of 1024, users can flexibly reduce the embedding dimensions to as low as 32 without compromising performance, enabled by Matryoshka Representation Learning. ![Image 6](https://jina-ai-gmbh.ghost.io/content/images/icon/apple-touch-icon-9.png)arXiv.orgSaba Sturua ![Image 7](https://jina-ai-gmbh.ghost.io/content/images/thumbnail/arxiv-logo-fb-5.png)](https://arxiv.org/abs/2409.10173)

[Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models Many use cases require retrieving smaller portions of text, and dense vector-based retrieval systems often perform better with shorter text segments, as the semantics are less likely to be over-compressed in the embeddings. Consequently, practitioners often split text documents into smaller chunks and encode them separately. However, chunk embeddings created in this way can lose contextual information from surrounding chunks, resulting in sub-optimal representations. In this paper, we introduce a novel method called late chunking, which leverages long context embedding models to first embed all tokens of the long text, with chunking applied after the transformer model and just before mean pooling - hence the term late in its naming. The resulting chunk embeddings capture the full contextual information, leading to superior results across various retrieval tasks. The method is generic enough to be applied to a wide range of long-context embedding models and works without additional training. To further increase the effectiveness of late chunking, we propose a dedicated fine-tuning approach for embedding models. ![Image 8](https://jina-ai-gmbh.ghost.io/content/images/icon/apple-touch-icon-10.png)arXiv.orgMichael Günther ![Image 9](https://jina-ai-gmbh.ghost.io/content/images/thumbnail/arxiv-logo-fb-6.png)](https://arxiv.org/abs/2409.04701)

```
function cherryPick(question, longContext, options) {
  if (longContext.length < options.snippetLength * options.numSnippets)
    return longContext;
  
  const chunks = splitIntoChunks(longContext, options.chunkSize);
  
  const chunkEmbeddings = getEmbeddings(chunks, "retrieval.passage");
  const questionEmbedding = getEmbeddings([question], "retrieval.query")[0];
  
  const similarities = chunkEmbeddings.map(embed => 
    cosineSimilarity(questionEmbedding, embed));
  
  const chunksPerSnippet = Math.ceil(options.snippetLength / options.chunkSize);
  const snippets = [];
  const similaritiesCopy = [...similarities];
  
  for (let i = 0; i < options.numSnippets; i++) {
    let bestStartIndex = 0;
    let bestScore = -Infinity;
    
    for (let j = 0; j <= similarities.length - chunksPerSnippet; j++) {
      const windowScores = similaritiesCopy.slice(j, j + chunksPerSnippet);
      const windowScore = average(windowScores);
      
      if (windowScore > bestScore) {
        bestScore = windowScore;
        bestStartIndex = j;
      }
    }
    
    const startIndex = bestStartIndex * options.chunkSize;
    const endIndex = Math.min(startIndex + options.snippetLength, longContext.length);
    snippets.push(longContext.substring(startIndex, endIndex));
    
    for (let k = bestStartIndex; k < bestStartIndex + chunksPerSnippet; k++)
      similaritiesCopy[k] = -Infinity;
  }
  
  return snippets.join("\n\n");
}
```

Using late chunking and Conv1D-like mean pooling for selecting the best snippet w.r.t. the question.

Make sure you call Jina Embeddings API with retrieval `task` , `late_chunking` and `truncate` set as bellow:

```
await axios.post(
  'https://api.jina.ai/v1/embeddings',
  {
    model: "jina-embeddings-v3",
    task: "retrieval.passage",
    late_chunking: true,
    input: chunks,
    truncate: true
  }, 
  { headers }); 
```

For embedding question, make sure to change `task` to `retrieval.query` and toggle off `late_chunking`

The full implementation can be found on Github:

[node-DeepResearch/src/tools/jina-latechunk.ts at main · jina-ai/node-DeepResearch Keep searching, reading webpages, reasoning until it finds the answer (or exceeding the token budget) - jina-ai/node-DeepResearch ![Image 10](https://jina-ai-gmbh.ghost.io/content/images/icon/pinned-octocat-093da3e6fa40-5.svg)GitHubjina-ai ![Image 11](https://jina-ai-gmbh.ghost.io/content/images/thumbnail/0921e515-0139-4540-bca4-52042b49328c-2)](https://github.com/jina-ai/node-DeepResearch/blob/main/src/tools/jina-latechunk.ts)

[](https://jina.ai/news/snippet-selection-and-url-ranking-in-deepsearch-deepresearch/#rank-url-for-next-read "Rank URL for Next Read")Rank URL for Next Read
--------------------------------------------------------------------------------------------------------------------------------

The problem is this: during a DeepSearch session, you'll likely collect a lot of URLs from search engine result pages (SERP) and discover even more every time you read individual webpages (those on-page links). The total count of unique URLs can easily reach the hundreds. Again, simply dumping all URLs directly into the LLM's context is inefficient - it wastes valuable context-length and more problematically, **we found LLMs essentially pick URLs at random.** It's crucial to guide the LLM toward URLs that have the highest probability of containing the answer you need.

```
curl https://r.jina.ai/https://example.com \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Retain-Images: none" \
  -H "X-Md-Link-Style: discarded" \
  -H "X-Timeout: 20" \
  -H "X-With-Links-Summary: all"
```

Best option for using Jina Reader to crawl a page in DeepSearch. This will collect all on-page links in a separate `links` field, and removing them from the `content` field.

Think of this problem as an in-context PageRank where we need to weight hundreds of URLs during a session. We rank URLs based on multiple factors that combine last update time, domain frequency, path structure, and most importantly, semantic relevance to the query to create a composite score. Remember we can only use the information that's available _before_ actually visiting the URL:

![Image 12: Infographic detailing a URL ranking system in deep search, including updated time, frequency signals, path structure, and opt](https://jina-ai-gmbh.ghost.io/content/images/2025/03/url-ranking-illustration--2-.svg)

**Frequency Signals**: URLs that appear multiple times across different sources receive additional weight. URLs from domains that appear frequently in search results receive a boost, as popular domains often contain authoritative content.

**Path Structure**: We analyze URL paths to identify content clusters. URLs within common path hierarchies receive higher scores, with a decay factor applied to deeper paths.

**Semantic Relevance**: We use [jina-reranker-v2-base-multilingual](https://jina.ai/?sui&model=jina-reranker-v2-base-multilingual) to assess the semantic relevance between the question and the textual info of each URL, which is [a classic reranking problem](https://jina.ai/reranker/#what_reranker). The textual info of each URL comes from:

*   Title & snippets from SERP API results (`https://s.jina.ai/` with `'X-Respond-With': 'no-content'`)
*   Anchor text of on-page URLs (`https://r.jina.ai` with `'X-With-Links-Summary': 'all'`)

**Last Updated Time**: Some DeepSearch queries are time-sensitive, so recently updated URLs are more valuable than older ones. Without being a major search engine like Google, reliably determining last update time is challenging. We've implemented a multi-layered approach that combines the following signal and provide a confidence-scored timestamp that prioritize fresher content when needed.

*   SERP API filters (such as s.jina.ai's `tbs` parameter for filtering by recency)
*   HTTP header analysis (Last-Modified, ETag)
*   Metadata extraction (meta tags, Schema.org timestamps)
*   Content pattern recognition (visible dates in HTML)
*   CMS-specific indicators for platforms like WordPress, Drupal, and Ghost

**Gated Content:** Some content on social media platforms is gated or simply behind paywalls, and without logging in or violating their ToS, there's no legitimate way to fetch this content. We should actively maintain a list of problematic URLs and hostnames to lower their rankings, preventing wasted time on unaccessible content.

**Domain Diversity:** In some cases, the highest-weighted URLs all come from the same hostnames, which can trap DeepSearch in a local optimum and reduce the final quality of results. Check the above examples where all top URLs are from StackOverflow. To improve diversity, we can implement an explore-exploit approach by selecting the top-k highest-ranked URLs from each hostname.

The full implementation of ranking URLs can be found on our Github.

[node-DeepResearch/src/utils/url-tools.ts at main · jina-ai/node-DeepResearch Keep searching, reading webpages, reasoning until it finds the answer (or exceeding the token budget) - jina-ai/node-DeepResearch ![Image 13](https://jina-ai-gmbh.ghost.io/content/images/icon/pinned-octocat-093da3e6fa40-6.svg)GitHubjina-ai ![Image 14](https://jina-ai-gmbh.ghost.io/content/images/thumbnail/0921e515-0139-4540-bca4-52042b49328c-3)](https://github.com/jina-ai/node-DeepResearch/blob/main/src/utils/url-tools.ts#L192)

```
<action-visit>
- Crawl and read full content from URLs, you can get the fulltext, last updated datetime etc of any URL.  
- Must check URLs mentioned in <question> if any
- Choose and visit relevant URLs below for more knowledge. higher weight suggests more relevant:
<url-list>
  + weight: 0.20 "https://huggingface.co/docs/datasets/en/loading": "Load - Hugging FaceThis saves time because instead of waiting for the Dataset builder download to time out, Datasets will look directly in the cache. Set the environment ...Some datasets may have more than one version based on Git tags, branches, or commits. Use the revision parameter to specify the dataset version you want to load ..."
  + weight: 0.20 "https://huggingface.co/docs/datasets/en/index": "Datasets - Hugging Face🤗 Datasets is a library for easily accessing and sharing datasets for Audio, Computer Vision, and Natural Language Processing (NLP) tasks. Load a dataset in a ..."
  + weight: 0.17 "https://github.com/huggingface/datasets/issues/7175": "[FSTimeoutError] load_dataset · Issue #7175 · huggingface/datasetsWhen using load_dataset to load HuggingFaceM4/VQAv2, I am getting FSTimeoutError. Error TimeoutError: The above exception was the direct cause of the following ..."
  + weight: 0.15 "https://github.com/huggingface/datasets/issues/6465": "`load_dataset` uses out-of-date cache instead of re-downloading a ...When a dataset is updated on the hub, using load_dataset will load the locally cached dataset instead of re-downloading the updated dataset."
  + weight: 0.12 "https://stackoverflow.com/questions/76923802/hugging-face-http-request-on-data-from-parquet-format-when-the-only-way-to-get-i": "Hugging face HTTP request on data from parquet format when the ...I've had to get the data from their data viewer using the parquet option. But when I try to run it, there is some sort of HTTP error. I've tried downloading ..."
</url-list>
</action-visit>
```

Remember to put URL weights in the agent's context and instruct LLMs to respect the weights.

[](https://jina.ai/news/snippet-selection-and-url-ranking-in-deepsearch-deepresearch/#conclusion "Conclusion")Conclusion
------------------------------------------------------------------------------------------------------------------------

Since our DeepSearch release on February 2nd 2025, we've discovered two implementation details that greatly improved quality. In both cases, multilingual embeddings and rerankers are used in an _"in-context"_ manner - operating at a much smaller scale than the traditional pre-computed indices these models typically require.

This points to a polarization in search engineering future. Consider a framework analogous to Kahneman's dual-process theory:

*   Fast-think (grep, BM25, SQL): Quick, rule-governed pattern matching with minimal computational demands.
*   Slow-think (LLM): Comprehensive reasoning with deep contextual understanding, requiring significant computation.
*   Mid-think (embeddings, rerankers): Caught in limbo? Too "advanced"/semantic for simple pattern matching yet lacking true reasoning capabilities to achieve best precision@1.

As a consequence, we may be witnessing the popularity of a bifurcated architecture where lightweight, efficient SQL/BM25 handles content retrieval on the left hand side, feeding _directly_ into LLMs for deep processing on the right hand side. The remaining role for mid-think models shifts to in-context tasks only such as filtering, deduplication, and sorting where full reasoning would be inefficient.

Nevertheless, selecting critical snippets and ranking URLs remain fundamental components with direct impact on DeepSearch/DeepResearch system quality. We hope our insights spark improvements in your own implementations.

Query expansion continues to be another crucial quality determinant. We're actively evaluating multiple approaches—ranging from basic prompt-based rewrites to small language models and reasoning-based methods. Look for our upcoming findings on this front soon. Stay tuned.

