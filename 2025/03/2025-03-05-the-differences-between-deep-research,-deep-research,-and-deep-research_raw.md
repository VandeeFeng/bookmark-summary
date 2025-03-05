Title: The Differences between Deep Research, Deep Research, and Deep Research

URL Source: https://leehanchung.github.io/blogs/2025/02/26/deep-research/

Markdown Content:
A wave of “Deep Research” releases has swept through frontier AI labs recently. Google unveiled its Gemini 1.5 Deep Research in December 2024, OpenAI followed with its Deep Research in February 2025, and Perplexity introduced its own Deep Research shortly after. Meanwhile, DeepSeek, Alibaba’s Qwen, and Elon Musk’s xAI rolled out Search and Deep Search features for their chatbot assistants. Alongside these, dozens of copycat open-source implementations of Deep Research have popped up on GitHub. It seems Deep Research is the Retrieval-Augmented Generation (RAG) of 2025—everything is being rebranded and marketed as “Deep Research” without a clear definition of what it actually entails.

Does this sound familiar? It echoes the hype around RAG in 2023, agents, and agentic RAG in months past. To cut through the clutter, this blog post examines the various flavors of “Deep Research” from a technical implementation perspective.

[Deep Research, Deep Search, or Just Search](https://leehanchung.github.io/blogs/2025/02/26/deep-research/#deep-research-definition)
------------------------------------------------------------------------------------------------------------------------------------

> "”Deep Research uses AI to explore complex topics on your behalf and provide you with findings in a comprehensive, easy-to-read report, and is a first look at how Gemini is getting even better at tackling complex tasks to save you time. “- [Google](https://blog.google/products/gemini/google-gemini-deep-research/)”

> "”Deep research is OpenAI’s next agent that can do work for you independently—you give it a prompt, and ChatGPT will find, analyze, and synthesize hundreds of online sources to create a comprehensive report at the level of a research analyst.” - [OpenAI](https://openai.com/index/introducing-deep-research/)

> "”When you ask a Deep Research question, Perplexity performs dozens of searches, reads hundreds of sources, and reasons through the material to autonomously deliver a comprehensive report.” - [Perplexity](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)”

Stripping away the marketing jargon, here’s the concise definition of Deep Research:

> “Deep research is a report generation system that takes a user query, uses large language models (LLMs) as agents to iteratively search and analyze information, and produce a detailed report as the output.”

In natural language processing (NLP) terms, this is known as `report generation`.

[Implementations](https://leehanchung.github.io/blogs/2025/02/26/deep-research/#implementations)
------------------------------------------------------------------------------------------------

Report generation - or `deep research` - has been a focus of the AI engineering since ChatGPT’s debut. I’ve personally experimented with it during hackathons in early 2023, a time when AI engineering was just taking off. Tools like LangChain, AutoGPT, GPT-Researcher, and prompt engineering, along with countless demos on Twitter and LinkedIn, have drawn significant attention. However, the real challenge lies in the implementation details. Below, we’ll explore common patterns for building report generation systems, highlight their differences, and classify offerings from various vendors.

### [Untrained: Directed Acyclic Graph (DAG)](https://leehanchung.github.io/blogs/2025/02/26/deep-research/#untrained-dag)

Early on, AI engineers discovered that asking an LLM like GPT-3.5 to generate a report from scratch wasn’t practical. Instead, they turned to [Composite Patterns](https://leehanchung.github.io/blogs/2024/10/28/reasoning-prompt-engineering-sampling/#Composites) to chain together multiple LLM calls.

The process typically works like this:

1.  Decompose the user query - sometimes using step back prompting ([Zheng et al, 2023](https://arxiv.org/abs/2310.06117)) - to create a report outline.
2.  For each section, retrieve relevant information from search engines or knowledge bases and summarize it.
3.  Finally, use LLM to stitch the sections into a cohesive report.

A prime example is [GPT-Researcher](https://github.com/assafelovic/gpt-researcher).

![Image 1: alt text](https://leehanchung.github.io/assets/img/2025-02-26/01-dag.png)

Every prompt in this system is meticulously hand-tuned through “prompt engineering.” Evaluation relies on subjective eyeballing of the outputs, resulting in inconsistent report quality. It is beautiful when it worked.

[Untrained: Finite State Machine (FSM)](https://leehanchung.github.io/blogs/2025/02/26/deep-research/#untrained-fsm)
--------------------------------------------------------------------------------------------------------------------

To boost report quality, engineers added complexity to the DAG approach. Rather than a single-pass process, they introduced structural patterns like reflexion ([Shinn et al, 2023](https://arxiv.org/abs/2303.11366)) and self-reflection, where the LLM reviews and refines its own output. This transforms the simple DAG into a finite state machine (FSM), with LLMs partly guiding state transitions.

This illustration from Jina.ai exemplifies the approach:

![Image 2: alt text](https://leehanchung.github.io/assets/img/2025-02-26/02-fsm.png)

Like the DAG method, every prompt is hand-crafted, and evaluations remain subjective. Report quality continues to vary widely as the system is hand tuned.

### [Trained: End to End](https://leehanchung.github.io/blogs/2025/02/26/deep-research/#trained-e2e)

The shortcomings of earlier methods—haphazard prompt engineering and a lack of measurable evaluation metrics—prompted a shift. Stanford’s STORM \[Shao et al, 2024\] addressed these issues by optimizing the system end to end using DSPy ([Khattab et al, 2023](https://arxiv.org/abs/2310.03714)).

![Image 3: alt text](https://leehanchung.github.io/assets/img/2025-02-26/03-storm.png)

The result? STORM generates reports rivaling Wikipedia articles in quality.

### [Trained: Large Reasoning Model](https://leehanchung.github.io/blogs/2025/02/26/deep-research/#trained-lrm)

Advances in LLM reasoning capabilities have made large reasoning models a compelling option for Deep Research. For instance, OpenAI described how it trained its Deep Research model below. Note that OpenAI used [LLM-as-a-judge](https://leehanchung.github.io/blogs/2024/08/11/llm-as-a-judge/) and [evaluation rubrics](https://leehanchung.github.io/blogs/2024/08/11/llm-as-a-judge/#evaluation-criteria) to grade the outputs.

![Image 4: alt text](https://leehanchung.github.io/assets/img/2025-02-26/04-lrm.png)

Google’s Gemini and Perplexity’s chat assistants also offer “Deep Research” features, but neither has published any literature on how they optimized their models or systems for the task or any substaintial quantitative evaluations. However, the product manager of Google’s Deep Research did mention during a [podcast interview](https://www.latent.space/p/gdr) that they “have special access per se. It’s pretty much the same model (Gemini 1.5). We of course have our own, uh, post-training work that we do”. We will make an assumption that the fine-tuning work done is non-substantial. Meanwhile, xAI’s Grok excels at report generation, though it does not seem to search beyond two iterations - few times for the outline sections, and few times per section.

[Competitive Landscape](https://leehanchung.github.io/blogs/2025/02/26/deep-research/#landscape)
------------------------------------------------------------------------------------------------

We’ve developed a conceptual map to evaluate the Deep Research capabilities of various popular services. The vertical axis measures the depth of research, defined by how many iterative cycles a service performs to gather additional information based on prior findings. The horizontal axis assesses the level of training, ranging from hand-tuned systems (e.g., those using manually crafted prompts) on one end to fully trained systems leveraging machine learning techniques on the other. Examples of trained systems include:

```
OpenAI Deep Research: Optimized specifically for research tasks through reinforcement learning.
DeepSeek: Trained for general reasoning and tool use, adaptable to research needs.
Google Gemini: Instruction fine-tuned large language models (LLMs), trained broadly but not specialized for research.
Stanford STORM: A system trained to streamline the entire research process end-to-end.
```

This framework highlights how different services balance iterative research depth with the sophistication of their training approaches, offering a clearer picture of their Deep Research strengths.

![Image 5: alt text](https://leehanchung.github.io/assets/img/2025-02-26/05-quadrants.png)

[Conclusion](https://leehanchung.github.io/blogs/2025/02/26/deep-research/#conclusion)
--------------------------------------------------------------------------------------

The Deep Research landscape is evolving at breakneck speed. Techniques that flopped or weren’t widely available six months ago might now succeed. Naming conventions remain murky, adding to the confusion. Hopefully, this post clarifies the technical distinctions and cuts through the hype.

[References](https://leehanchung.github.io/blogs/2025/02/26/deep-research/#references)
--------------------------------------------------------------------------------------

*   [Yijia Shao, Yucheng Jiang, Theodore A. Kanell, Peter Xu, Omar Khattab, Monica S. Lam (2024) _Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models_. Retrieved from https://arxiv.org/abs/2402.14207](https://arxiv.org/abs/2402.14207)
*   [OpenAI (2025). _Deep Research System Card_. Retrieved from https://cdn.openai.com/deep-research-system-card.pdf](https://cdn.openai.com/deep-research-system-card.pdf)
*   [assafelovic. (2024). GPT Researcher (Version \[latest version\]) \[Computer software\]. GitHub. Retrieved from https://github.com/assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher?tab=readme-ov-file)
*   [Jina AI. (2024). _A practical guide to implementing DeepSearch/DeepResearch._ Retrieved from https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/](https://jina.ai/news/a-practical-guide-to-implementing-deepsearch-deepresearch/)
*   [Latent Space. (2024). _The inventors of deep research._ Retrieved from https://www.latent.space/p/gdr](https://www.latent.space/p/gdr)

```
@article{
    leehanchung,
    author = {Lee, Hanchung},
    title = {The Differences between Deep Research, Deep Research, and Deep Research},
    year = {2025},
    month = {02},
    howpublished = {\url{https://leehanchung.github.io}},
    url = {https://leehanchung.github.io/blogs/2025/02/26/deep-research/}
}
```
