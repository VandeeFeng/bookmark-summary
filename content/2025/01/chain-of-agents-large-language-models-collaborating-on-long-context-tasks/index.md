---
title: Chain of Agents- Large language models collaborating on long-context tasks
date: 2025-01-26
extra:
  source: https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/
  original_title: Chain of Agents- Large language models collaborating on long-context tasks
---
## Summary
**摘要**：
《链式代理：大型语言模型在长上下文任务中的协作》一文介绍了Chain-of-Agents(CoA)框架，这是用于长上下文任务的多代理协作新模式。通过自然语言处理实现信息聚合和长于多种大型语言模型之间的上下文推理，CoA在问答、总结和代码完成等长上下文任务方面表现出色。它显著提高了与较强基线(如Retrieval Augmented Generation(RAG)、多代理大型语言模型和输入截断模型)相比的表现。CoA的核心优势在于其成本效益、任务和长度无关性及易解释性。

**要点总结**：
- **面临的问题**：通用大型语言模型在处理需要长输入的长上下文任务时存在局限，挑战在于输入长度限制导致无法充分利用全部上下文，影响理解和任务完成。
- **CoA框架**：作者引入了Chain-of-Agents框架，该框架通过逐层协作的方式，利用各代理处理长上下文的不同部分，实现信息聚合和上下文推理。CoA是基于自然语言协作实现的，充分扩展了大型语言模型的信息处理能力，而与传统方法如上下文缩减和窗口扩展有不同的处理方式。
- **输入处理**：CoA采用分阶段的方法，首先通过多个worker代理处理长上下文的不同部分，通过消息传递进行协作，最后由manager代理整合所有信息以生成最终答案。此过程模拟了人类处理长文字的方式，实现逐层协作处理。
- **实验结果**：在多个数据集和六个模型上进行的实验验证了CoA的有效性，显示CoA相比已知的基线处理长上下文任务时表现更优，特别是在问答、摘要和代码完成任务上。
- **性能提升**：CoA能够在多种大型语言模型上实现优异的性能提升，尤其在处理较长输入时，相较于全上下文模型和RAG模型，CoA表现出了显著的提升，改善幅度达到10%以上。

CoA框架为处理长上下文任务提供了一种高效且成本效益高的解决方案，通过合理分配任务级联处理，实现对大型语言模型的优化，适用于多种数据集任务，展现出其独特的性能优势。
## Full Content
Title: Chain of Agents: Large language models collaborating on long-context tasks

URL Source: https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/

Markdown Content:
Over the past few years large language models (LLMs) have shown remarkable capabilities on various tasks, such as reasoning, knowledge retrieval, and generation. However, it is still challenging for LLMs to solve tasks that require long inputs, because they typically have limitations on input length, and hence, cannot utilize the full context. This issue hinders long context tasks, such as long summarization, question answering, and code completion.

To mitigate this, at [NeurIPS 2024](https://neurips.cc/Conferences/2024) we introduced [Chain-of-Agents](https://openreview.net/pdf?id=LuCLf4BJsr) (CoA), a novel framework that harnesses multi-agent collaboration through natural language to enable information aggregation and context reasoning across various LLMs over long-context tasks. We perform a comprehensive evaluation of CoA on a wide range of long-context tasks, including question answering, summarization, and code completion. We demonstrate significant improvements (up to 10%) over strong baselines: [retrieval augmented generation](https://cloud.google.com/use-cases/retrieval-augmented-generation) (RAG), multi-agent LLMs, and LLMs that have had their inputs truncated once the context window is full (called “full-context”).

A simple but effective approach to improve long-context understanding
---------------------------------------------------------------------

Previous studies have mainly explored two major directions: _input reduction_ and _window extension_. Input reduction reduces the length of the input context — for example, by directly truncating the input — before feeding to downstream LLMs. RAG extends this direction by breaking the input into chunks and then retrieving answers to the most relevant chunks based on embedding similarity. However, because of low retrieval accuracy, LLMs could receive an incomplete context for solving the task, hurting performance. Window extension extends the context window of LLMs via fine-tuning, training the model to consume longer inputs. For example, [Gemini](https://gemini.google.com/) is able to directly process 2M tokens for each input. However, when the window becomes longer even than their extended input capacities, such LLMs still struggle to focus on the needed information to solve the task and suffer from ineffective context utilization. This long context approach is further complicated by the fact that the cost increases quadratically with length due to the design of the [transformer architecture](https://research.google/blog/transformer-a-novel-neural-network-architecture-for-language-understanding/) that underlies most LLMs.

Motivated by the aforementioned challenges, we designed CoA with inspiration from the way people interleave reading and processing of long contexts under our own limited working memory constraints. Whereas input reduction approaches need to start processing over shorter inputs (“read-then-process”), CoA breaks the input into chunks and then assigns workers to process each chunk sequentially before reading all of the input (“interleaved read-process”). Further, in contrast to context extension, CoA leverages the capacity of LLMs to communicate between agents rather than trying to feed a large number of tokens into the LLM. CoA is also compute cost–effective, significantly improving over full-context approaches, in particular, by reducing time complexity from _n_2 to _nk_, where _n_ is the number of input tokens and _k_ is the context limit of the LLM.

A novel approach to input processing
------------------------------------

CoA contains two stages. In the first, a series of worker agents in charge of different chunks of long context collaborate and aggregate supporting data that can be used to answer the given query. To this end, the workers read and process sequentially, each receiving the message from the previous worker and transferring the useful updated information to the next. In the second stage, the manager agent receives the complete evidence from the last worker agent and generates the final response. Here is a motivating example:

_Question:_ “Who is the grandchild of A?”

_Source input, separated into chunks:_ \[1\],\[2\],\[3\],\[4\]

_Supporting data from each chunk:_

\[1\] – A’s spouse is D

\[2\] – A’s child is B

\[3\] – No additional evidence

\[4\] – B’s child is C

_Question:_ “Who is the grandchild of A?”

_Workers assess their chunk and perform a relevant task:_

\[1\] – topic exploration: A’s spouse is D

\[2\] – answer first hop: A’s child is B

\[3\] – forward previous evidence: A’s child is B

\[4\] – complete reasoning: A’s child is B, B’s child is C. Thus, A’s grandchild is C

_Manager:_ “It is C.”

### Stage 1: Worker agent: Segment comprehension and chain-communication

In Stage 1, CoA contains a sequence of worker agents. Each worker receives an heuristically concatenated portion from the source text, the query, instructions for a specific task assigned to that agent, and the message passed from the previous agent. This communication chain is unidirectional, passing from each worker to the next in sequential order. The worker agents process each concatenated block and outputs a message for the next worker.

### Stage 2: Manager agent: Information integration and response generation

In Stage 2, after multiple steps of information extraction and comprehension by worker agents, the manager agent produces the final solution. While worker agents extract relevant information in a long-context source, the manager agent synthesizes relevant information accumulated by the end of ‘’worker–agent chain'' to generate the final answer. Specifically, given the instruction for manager and query, the manager agent assesses the accumulated knowledge from the last worker to generate the final answer.

Experiments
-----------

To illustrate the utility of this approach, we conduct intensive experiments on nine datasets, including question answering, summarization, and code completion tasks with six LLMs, [PaLM 2](https://ai.google/discover/palm2/) (Text Bison and Text Unicorn), [Gemini](https://gemini.google.com/) (Ultra), and [Claude 3](https://claude.ai/) (Haiku, Sonnet, and Opus) models. We compare CoA with two strong baselines chosen from input reduction and window extension approaches, respectively: (i) RAG, which uses a state-of-the-art retriever to obtain the most relevant information to feed into the LLM, and (ii) Full-Context, which feeds all input into the LLM until reaching the window limit.

### Comparison with a RAG model

The figures show the results on question answering, summarization, and code completion tasks for three models on eight different datasets, including HotpotQA, MuSiQue, RepoBench-P(RepoB) from [LongBench](https://aclanthology.org/2024.acl-long.172.pdf), and NarrativeQA (NQA), Qasper, QuALITY, QMSum, GovReport from [SCROLLS](https://www.scrolls-benchmark.com/). CoA (8k) (where “8k” refers to the length of input for the LLM) outperforms Full-Context (8k) by a large margin on all datasets. It also outperforms the RAG (8k) model for all eight datasets.

### Multi-agent collaboration in CoA enables complex reasoning over long context

Below we present a comparison of outputs from RAG and CoA for a question on the [HotpotQA dataset](https://hotpotqa.github.io/). To find the correct answer, RAG retrieves text chunks with high semantic similarity with the query. However, conducting multi-hop reasoning is challenging as the critical first-hop answer often lacks semantic relevance to the query. In contrast, CoA operates differently: the first agent explores related topics without knowing the query’s answer, aiding subsequent inference. The second agent, also unaware of the answer, broadens the topic scope by incorporating new information. The third agent finally discovers the answer, synthesizing information from earlier agents and new data to complete the reasoning chain. This collaborative approach highlights CoA’s ability to facilitate complex reasoning across long context tasks.

### Comparison with long context LLMs

The figure below shows the comparison with long context LLMs on [NarrativeQA](https://arxiv.org/abs/1712.07040) and [BookSum](https://arxiv.org/abs/2105.08209). CoA (8k) significantly outperforms RAG (8k) and Full-Context (200k) baselines with three Claude 3 (Haiku, Sonnet, and Opus) models as backbones, even though the context limit of the latter is 200k.

### Greater improvement for long context models with longer inputs

We compare the performance of CoA and Full-Context with [Claude 3](https://claude.ai/) on [BookSum](https://arxiv.org/abs/2105.08209). As shown in Figure, CoA can outperform the Full-Context baseline by a large margin on various source lengths. It is worth noting that, when the length of the sample increases, the performance even increases for CoA, and the improvement over Full-Context (200k) baseline becomes more significant. The improvement of CoA reaches around 100% when the length is larger than 400k. Thus, we can conclude that 1) CoA can still enhance the LLM performance even though the model has a very long context window limit; and 2) CoA delivers more performance gains when the input is longer.

Conclusion
----------

In this paper, we propose Chain-of-Agents (CoA), a multi-agent LLM collaboration framework for solving long context tasks. It is a training-free, task- and length-agnostic, interpretable, and cost-effective framework. Experiments show that Chain-of-Agents outperforms RAG and long context LLMs by a large margin, despite its simple design. Analysis shows that by integrating information aggregation and context reasoning, CoA performs better on longer samples.

