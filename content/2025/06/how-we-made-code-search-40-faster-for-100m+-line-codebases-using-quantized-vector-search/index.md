---
title: How we made code search 40 faster for 100M+ line codebases using quantized vector search
date: 2025-06-27
extra:
  source: https://www.augmentcode.com/blog/repo-scale-100M-line-codebase-quantized-vector-search
  original_title: How we made code search 40 faster for 100M+ line codebases using quantized vector search
---
## Summary
**摘要**：Augment Code团队针对大型代码库（超过1亿行代码）的实时上下文检索性能问题，提出了一种量化向量搜索的解决方案。传统的嵌入向量搜索在处理大型代码库时面临内存占用高（2GB/1亿行）和延迟高（2秒以上）的挑战。通过采用近似最近邻（ANN）算法和量化技术，团队将内存消耗降低8倍（至250MB），搜索延迟减少到200毫秒以内，同时保持99.9%的准确率。该方案实现了无缝的量化索引生成和实时更新机制，当代码库变更时能自动处理新旧索引过渡，确保用户无感知地获得性能提升。这项技术创新不仅解决了大规模代码检索的性能瓶颈，更重要的是保持了AI开发工具在真实工作场景中的实用性。

**要点总结**：
1. **大型代码库的检索性能挑战**：传统嵌入向量搜索在处理1亿行代码时需要2GB内存和2秒以上延迟，无法满足实时交互需求。
2. **量化向量搜索解决方案**：采用近似最近邻（ANN）算法和量化技术，将高维嵌入向量压缩为紧凑的比特向量，实现内存降低8倍（250MB）、延迟<200ms的性能突破。
3. **动态索引更新机制**：创新性地设计索引管道系统，能跟踪代码变更、处理新旧索引共存，并自动回退原始搜索方案确保99.9%准确率。
4. **无缝用户体验设计**：系统自动判断是否使用量化索引（基于代码库大小和索引准备状态），开发者无需手动干预即可获得性能优化。
5. **AI工具实用化的核心洞察**：强调AI软件工程工具必须解决规模化性能问题（响应时间<200ms），才能真正融入开发者的实际工作流。
## Full Content
Title: How we made code search 40% faster for 100M+ line codebases using quantized vector search

URL Source: https://www.augmentcode.com/blog/repo-scale-100M-line-codebase-quantized-vector-search

Published Time: 2025-06-11T20:53:05.660Z

Markdown Content:
_Augment Code is designed to provide the most useful context for working with large codebases. As we took on even bigger codebases, a challenge emerged: our context engine gets great results, but it was running into performance limitations due to the large amount of data to process. We solved this problem by implementing an approximation of context search that shrinks the search space by orders of magnitude while maintaining more than 99.9% fidelity to the exact results. As a result, the latency of real-time features like code completions seamlessly improved by over 40% for our most challenging codebases._

_Here's the hard data: we reduced memory usage by 8x (from 2GB to 250MB for a 100M LOC codebase), cut search latency from 2+ seconds to under 200ms, and maintained 99.9% accuracy on typical queries. For the 0.1% of edge cases—usually involving very recent code changes or extremely rare patterns—we have automatic fallbacks._

Why scale?
----------

A classic puzzle in software engineering is: “What’s the fastest practical way to sort a list?”. The key is that the answer depends on your assumptions and especially on scale. The best approach changes qualitatively every few orders of magnitude. Does the list fit in registers? In cache? In RAM? Does it fit on one machine at all?

Something similar goes for building software. 1,000 lines of code (LOC) is the size of a casual project that fits in one developer’s “working memory”. 10,000 LOC is typical of a concise open-source library but already requires “paging in” various parts of the design to maintain. 100,000 LOC could be a larger open-source effort or prototype product with several collaborators. Mature products maintained by teams frequently reach 1 million LOC; enterprise codebases can easily contain 10 or even 100 million LOC and reflect the work of many different teams separated in time and space. At such scales, coordinating all that work by getting the right understanding to the right people at the right time becomes a constant source of risk, overhead, and frustration.

Augment expands the capabilities of engineers and teams by delivering useful software understanding on demand. Among other things, this means being able to determine which specific lines of code out of an entire codebase are relevant to the task a user is working on, in the sub-second time scales required for real-time feedback. Our [indexing and retrieval system](https://www.augmentcode.com/blog/a-real-time-index-for-your-codebase-secure-personal-scalable) is designed to deliver this outcome, and we recently upgraded it to seamlessly support codebases up to 100 million LOC and beyond.

Here’s how we did it.

The challenge
-------------

Modern AI-powered retrieval relies on embeddings, vectors of numerical values generated by LLMs that efficiently represent the semantic content of some piece of context. [Augment’s indexing process](https://www.augmentcode.com/blog/a-real-time-index-for-your-codebase-secure-personal-scalable) generates such embeddings for all Augment users' codebases. Retrieval means searching these embeddings for the vectors which are most similar to a query vector that represents what the user is currently working on. Vector similarity is a simple operation that takes a pair of vectors and produces a single value as output indicating the degree of closeness. The tricky part is scaling it efficiently when computed across a large number of embeddings.

In our experience effective embedding models for code context can require 20+ bytes per LOC to store and 20+ nanoseconds per LOC to search, even after substantial optimization. If we implemented search as a simple loop over all embeddings, a codebase with 100 million LOC would require loading 2 GB of embeddings into RAM and spending 2 seconds of CPU work for every user operation. Smart implementations of caching, cancellation, and parallelization help us mitigate this cost in practice, but simultaneous load from enough users at this scale still risked overwhelming the system and compromising our goal of producing search results within a few hundred milliseconds, the threshold of latency that’s noticeable to a typical user. We knew we needed a way to efficiently narrow the search space.

Our solution
------------

Fortunately, approximate nearest neighbor (ANN) algorithms are a well-studied problem in software engineering. It’s harder than searching a one-dimensionally sorted list, but searching for similar vectors can also be sped up beyond linear time by exploiting the structure of the problem space. Specifically, entries that are closest to each other can also be grouped for the purposes of the search, while entries that are far apart can be quickly ruled out. There are many approaches in the literature but we quickly settled on a cutting-edge approach that leverages quantization— reducing a large embedding vector to a much smaller bit vector that efficiently represents that vector’s general “neighborhood”. By first searching the quantized representation to generate an initial list of candidate embeddings and then searching those candidates using the full embedding similarity computation, we can speed up retrieval by a factor of tens to hundreds while maintaining better than 99.9% parity of results with the original approach in practice.

Defining the algorithm was only the first step, though. It takes time to index the quantized representation we use for ANN search, and codebases are constantly changing, with newly added and deleted content often being especially important to search accurately. To address this challenge, we developed a new indexing pipeline that leverages our content tracking system to produce indexes that match a snapshot of the user's current codebase. Embeddings that are not present in the snapshot are handled as we search, by running the full embedding similarity computation. By smartly tracking changes to codebases we were able to get the best of both worlds: the efficiency of the quantized representation with the precision and flexibility of the original embedding scheme.

The part of this work I’m proudest of is that we’ve created a system that delivers the benefits of ANN search seamlessly and reliably. If a useful quantized index isn’t ready yet, or the codebase is too small to benefit from it, the feature has zero overhead; we just fall back to searching based on embedding similarity alone. If some embeddings are unavailable for any reason, we can produce a quantized index that excludes them. And if the codebase changes, we can use an older quantized index while preparing a new one. Our users never have to know anything or click on anything to get the benefits of ANN quantization. It all happens automatically in the background.

Conclusion
----------

The success of AI for software engineering doesn’t just depend on correct reasoning in a vacuum. It depends on incorporating useful context from dynamically changing codebases as they scale to almost unlimited levels of complexity. Our retrieval system has proven to be a powerful tool for providing this context, and with the introduction of ANN search we’ve ensured that we’ll be able to provide it for even larger and more complex codebases with under 200 milliseconds of additional latency.

The bigger lesson here isn't just about search optimization—it's about keeping AI tools usable at real-world scale. The most sophisticated AI is worthless if developers have to wait seconds for responses. By solving the performance problem invisibly, we've kept the focus where it belongs: on helping developers understand and improve their code.

