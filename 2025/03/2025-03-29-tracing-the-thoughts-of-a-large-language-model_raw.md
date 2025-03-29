Title: Tracing the thoughts of a large language model

URL Source: https://simonwillison.net/2025/Mar/27/tracing-the-thoughts-of-a-large-language-model/

Markdown Content:
**[Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)**. In a follow-up to the research that brought us the [delightful Golden Gate Claude](https://simonwillison.net/2024/May/24/golden-gate-claude/) last year, Anthropic have published two new papers about LLM interpretability:

*   [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) extends last year's interpretable features into [attribution graphs](https://transformer-circuits.pub/2025/attribution-graphs/methods.html#graphs), which can "trace the chain of intermediate steps that a model uses to transform a specific input prompt into an output response".
*   [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) uses that methodology to investigate Claude 3.5 Haiku in a bunch of different ways. [Multilingual Circuits](https://transformer-circuits.pub/2025/attribution-graphs/biology.html#dives-multilingual) for example shows that the same prompt in three different languages uses similar circuits for each one, hinting at an intriguing level of generalization.

To my own personal delight, neither of these papers are published as PDFs. They're both presented as glorious mobile friendly HTML pages with linkable sections and even some inline interactive diagrams. More of this please!

[![Image 1: Screenshot of a multilingual language model visualization showing antonym prediction across three languages. Left panel shows English with prompt "The opposite of 'small' is'" predicting "large". Middle panel shows Chinese prompt "小"的反义词是" predicting "大 (zh: big)". Right panel shows French prompt "Le contraire de "petit" est" predicting "grand (fr: big)". Above shows activation analysis with token predictions and highlighted instances of "contraire" in French text.](https://static.simonwillison.net/static/2025/anthropic-diagrams.jpg)](https://transformer-circuits.pub/2025/attribution-graphs/biology.html#dives-multilingual)
