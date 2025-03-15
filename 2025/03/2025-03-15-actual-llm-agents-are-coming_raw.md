Title: 

URL Source: https://vintagedata.org/blog/posts/designing-llm-agents

Markdown Content:
Actual LLM agents are coming | Vintage Data
===============              

[![Image 1: Vintage Data](https://vintagedata.org/blog/user/themes/quark/images/logo/logo.png)](https://vintagedata.org/blog)

*   [Vintage Data](https://vintagedata.org/blog/)
*   [Posts](https://vintagedata.org/blog/posts)
    *   [Actual LLM agents are coming](https://vintagedata.org/blog/posts/designing-llm-agents)
    *   [The Model is the Product](https://vintagedata.org/blog/posts/model-is-the-product)
    *   [What's the deal with mid-training?](https://vintagedata.org/blog/posts/what-is-mid-training)

Actual LLM agents are coming. They will be trained
==================================================

Agents are everywhere these days. And yet, the most consequential research development in agentic LLM research is almost unnoticed.

In January 2025, OpenAI released [DeepResearch](https://cdn.openai.com/deep-research-system-card.pdf), a specialized variant of O3 for web and document search. Thanks to "reinforcement learning training on these browsing tasks", Deep Research has gained the capacity to plan for a search strategy, cross-reference sources and [niche piece of knowledge](https://florianbrand.de/posts/odr) on queries based on intermediary feedback. Claude Sonnet 3.7 seems to apply successfully the same recipe for code. The model alone outperform existing orchestrations of past models on complex sequences of programming tasks.

In short, as William Brown [puts](https://www.youtube.com/watch?v=JIsgyk0Paic) it, "**LLM agents can work for long multi-step tasks**".

This advancement raises the question of what LLM agents really are. In December, Anthropic [unveiled](https://www.anthropic.com/engineering/building-effective-agents) a new definition: "systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."

In contrast, all the more commons form of agentic system are contrasted as _workflows_, "where LLMs and tools are orchestrated through predefined code paths". The recently hyped Manus AI fits exactly this definition. All my tests over the week-end [show](https://techcrunch.com/2025/03/09/manus-probably-isnt-chinas-second-deepseek-moment/) the same fundamental limitations of workflow systems that were already apparent in the time of AutoGPT, and are [especially striking for search](https://leehanchung.github.io/blogs/2025/02/26/deep-research/):

*   They can't plan and frequently get stuck in the middle of nowhere.
*   They can't memorize and struggle to maintain a task for more than 5-10 minutes.
*   They can't act effectively in the long run. Sequence of actions routinely fail due to a compounded error effect.

This post takes as a starting point an new strong definition of LLM agents. It does its best at summarizing what we know so far, based on a mix of limited information from big labs, emerging reproduction in the open research ecosystem and some personal speculation.

### The bitter lesson of simple LLM agents.

The concept of agents almost entirely clashes with base language models.

In classic agentic research, agents inhabits constrained environments. You're in a maze, you can move in this direction, but not this one. And you cannot fly, nor get under the ground, nor disappear in thin air. You're constrained by physics and, optionally, by the rules of the game. Any actual agents placed in this situation can still enjoy some degree of freedom, as there is more than one way to solve a game. Yet every move have to be conceived under the assumption of winning, getting your final reward. Effective agents gradually memorize past moves and elaborate patterns and heuristics.

This process is called "**search**". It's a very fitting metaphor: the exploratory move of an agent in a maze is a total analog to the clicking patterns of a web user on a search engines. There is a decades-long literature about search: suffice to notice that [Q-star](https://arxiv.org/pdf/2312.10868), the algorithm once rumored to be behind the new O generation of OpenAI model (it's unclear…), is an offshot of [A-Star](https://ieeexplore.ieee.org/document/4082128/), a search algorithm from 1968. One of the best recent example of this process is the [Pokemon training experiment](https://drubinstein.github.io/pokerl/) done by Pufferlib: we see the agents literally searching for the optimal paths, failing, going back and forth.

![Image 2: Pokemon RL experiment by PufferLib](https://drubinstein.github.io/pokerl/assets/mapvid.gif)

Base language models work almost exactly in reverse:

*   Agents are memorizing their environment. Base models don't and can only react to the information available inside their context window.
*   Agents are constrained by bounded rationality. Base models are generating any probable text. While that may result in actually consistent reasoning there is no hard guarantee and models can deviate at any time under pure aesthetic moves.
*   Agents can devise long term strategies. If they well conceived they can plan ahead moves in advance or backtrack. Language models are able to perform single-reasoning task but will quickly [saturate for multi-hop reasoning](https://stochasm.blog/posts/contextualization-machines/). Overall they are bounded by text rules, not physics/game rules.

A simple way of reconciling LLM and agentification would be to simply predefine their output through prepared prompts and rules. This is the approach retained by most agentic LLM systems and bound to hit on the… [Bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) from Richard Sutton. The Bitter Lesson is sometimes mistaken as some kind of guidebook to pretraining language models. It is really primarily about agents and about the temptation of incorporating and harcoding knowledge into the models. If you're seeing a wall, avoid it, move in the other direction. If you're seeing too many walls, backtrack. This is nice in the short term, you'll see immediate improvement and you won't have to run an algorithm forever to see them. In the long run, though, you are bound to always find suboptimal solution or get stuck into unexpected setting:

> We have to learn the bitter lesson that building in how we think we think does not work in the long run. The bitter lesson is based on the historical observations that 1) AI researchers have often tried to build knowledge into their agents, 2) this always helps in the short term, and is personally satisfying to the researcher, but 3) in the long run it plateaus and even inhibits further progress, and 4) breakthrough progress eventually arrives by an opposing approach based on scaling computation by search and learning. The eventual success is tinged with bitterness, and often incompletely digested, because it is success over a favored, human-centric approach.

Now let's transpose this to the way LLMs are currently used in production. Workflows like Manus or your usual LLM wrapper are currently "building knowledge". They guide the model through a series of prepared prompt. It might be the most opportune solution in the short term — after all you don't have to retrain an. It is not the most optimal one. In the end what you create is some kind of hybrid of generative AI and rule-based systems, that is a set of "simple ways to think about the contents of minds, such as simple ways to think about space, objects, multiple agents, or symmetries."

Let's put it clearly. If Manus AI is [unable](https://techcrunch.com/2025/03/09/manus-probably-isnt-chinas-second-deepseek-moment/) to properly book a plane or advise on fighting a tiger bare-handed, it's not because it is badly conceived. It has just been bitten by the bitter lesson. Prompts can't scale. Hardcoded rules can't scale. You need to design systems, from the ground up, that can search, that can plan and that can act. You need to design actual LLM agents.

### RL+Reasoning: the winning recipe

Again a hard question. There is little in the open. Anthropic, OpenAI, DeepMind and a handful of other labs know. So far we have to make do with few official informations, informal rumors and some limited open research attempts.

*   Similarly to classic agents, LLM agents are trained with reinforcement learning. There is a maze: all the potential words that can be written about something . There is a final way out or "reward". The process to check a reward has been attained is called a **verifier** — which are the entire purposes of William Brown new library verifiers. Verifiers are currently preferably done on formal outcomes, like math equations or programming sequences. Yet, as Kalomaze [showed](https://kalomaze.bearblog.dev/grpo-judge-experiments-findings-and-empirical-observations/), it is perfectly possible to build verifiers around non-strictly verifiable outputs, by training ad-hoc classifier. A major change that we have in this concern : language models are better are evaluating than creating. So even with small LLM-as-judge you can get a significant jump in performance and overall reward design.
*   LLM agents are trained through **drafts**, entire texts being generated and evaluated. This is not a straightforward choice as research initially focus on expanding search to the entire token sequence. Computation constraints have been a major factor as well as the recent breakthroughs in developing "reasoning" models — which could maybe be more aptly called drafting models. A typical training sequence of a reasoning model involves letting the model come up with its own logical sequence, under the assumption that the one yielding a good answer are more correct. This can yield counter-intuitive outcome (the best example being the DeepSeek R0 model doing occasional language switching between English and Chinese). Yet in a typical bitter lesson way, RL only cares about whatever works, not hesitating to take non-orhodox or unplanned shortcuts if needs be. Similarly to the classic agent lost in the maze, a language model has to find its way out through a pure reasoning exercise. No predefined prompting, no directions, just rewards and way to get them: the bitter solution to the bitter lesson.
*   LLM drafts are pre-defined into structured data sections to ease reward verification and to some extent, the overall reasoning process. This is a form of **rubric engineering** that can be either managed directly as a reward function or, as I think in more common in big labs training settings, by some initial phase of post-training.
*   LLM agents usually require being trained on a large amount of drafts and in multi-steps. This is typically what is happening for search: we do not evaluate the result of a search in one go but the ability of the model to access a resource, get a result, elaborate on it, get another resource, elaborate on it, change plan, backtrack etc. For this reason the preferred method for traiing LLM agents is now **GRPO** from DeepSeek, especially in combination with text generation from vllm. A few weeks ago I released a viral code notebook based on William Brown work that managed to fit GRPO on one A100 GPU made available through Google Colab. The lowering of compute requirement is a major factor that will ensure the democratization of RL and agentic design in the years to come.

### Wait… How do you scale that?

Here is for the fundamental building blocks. Now from this to OpenAI DeepResearch and the other emerging agents able to process long sequence of actions there is a distance. Allow me to speculate a bit.

Open RL/reasoning research has mostly focused on math since it turned out we have large collections of math exercises, some of them bundled in Common Crawl and extracted by HuggingFace with classifiers (that's FineMath). For many domains and, more specifically, search, we don't have the data. Because we need actual action sequences: logs, clicks, patterns. I used to work on log analysis in a not so remote past. Models (still using Markov chains, but, hey, this field changed fast…) were still routinely trained on AOL leaked data from the late 1990s (!). There is at least one critical open set recently added in the field: Wikipedia clickstream, an anomyzed set of paths from one Wikipedia article to another. Now let me ask you a simple question: is this set on HuggingFace? No. In fact, there is almost no actually agentic data on HuggingFace, in the sense that it would empower planning capacities. The entire field is still operating under the assumption LLM models are to be orchestrated with custom rule-based systems. I'm not sure that OpenAI or Anthropic have this data in enough quantity either. This is at least one area where legacy tech companies hold a strong leverage and there is no easy substitute: you can't buy the gigantic collection of Google user queries (unless it has been leaked somewhat on the dark web).

There is a way around: generating the data directly through **emulations** or "simulation". Classic RL models do not need past examples. They extrapolate the constraints and overreaching strategies through extensive and repeated search. Once transposed to search, a typical reinforcement learning approach would not be dissimilar to game RL: let the model travel freely and reward whenever it hits the right answer. This could be a very long travel. Like you need to locate the one very specific chemistry experiment stored in a forgotten soviet paper from the 1960s. Per pure brute force, maybe enforcing some language query variation, the model finally stumble on the right find. And then if can agregate all the factors that lead to that which might make this find more likely in the future.

Let's do some arithmetic. In a typical RL design, let's say GRPO, you can have 16 concurrent drafts — and I would not be surprised in models trained in big labs used a much higher iteration of drafts. Each of one may successively browse at least 100 different pages. That's 2,000 potential queries and this is just… one step. A complex RL training sequence would take maybe hundred of thousands steps (one of the reason I think it's now verging on mid-training) and various examples, especially for something as complex as generalist search capacities. What you're looking at is one training sequence requiring hundreds of millions of individual connexions — and maybe ddos some preferred academic sources in the process. This is… not optimal. Broadband, rather than actual compute, becomes your primary constraints.

Game RL faces a similar constraints. And that's why state of the art methods like Pufferlib [wrap](https://arxiv.org/pdf/2406.12905v1) "environments to look like Atari from the perspective of learning libraries, without any loss of generality": RL models just need to see what they need to use. Once applied to search, this could involve leveraging the big common crawl dumps and sending the data as if it were processed through the web, with urls, api calls and other typical http artifact. All the while the data is already there, stored in local dataframes with fast querying capacities.

So my expectation is that a typical LLM RL agent for search could be trained in this way:

*   Creating a large emulation of web search with a fixed dataset continuously "translated" back to the model.
*   Pre-cooling the model with some form of light SFT (like the SFT-RL-SFT-RL steps from DeepSeek), maybe on whatever existing search patterns that could be found. Overall idea is to pre-format the reasoning and output and speed up actual RL training — some form of pre-defined rubric engineering.
*   Preparing more or less complex queries with associated outcomes as **verifiers**. My only guess is that it involves some complex synthetic pipeline with backtranslation from existing resource, or maybe just very costly annotations from phd-level annotators.
*   Actual training in multi-step RL. The model is submitted a query, initiate a search, is sent results, can browse a page or rephrase results, all of it done in multi-step. From the perspective of the model it is as if it were actually browsing the web but all this data exchange in prepared i the background by the search emulator.
*   Maybe once the model is good enough at search, re-doing another round of RL and SFT this time more focused on writing the final synthesis. Once more I'm expecting it involves some complex synthetic pipeline where the output is becoming the input: original long reports, cuts down into little pieces and some reasoning involved to tie them up again.

### You won't prompt an agent

Finally we have an actual agent model. What does it change in practice with regard to standard workflows or model orchestrations? Just better quality overall? Or a completely different paradigm?

Let's journey back to the Anthropic definition: LLM agents "dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks". I'm going to take once more one of the use cases I'm more familiar with: search.

There have been lots of speculations about the death of RAG and its replacement by direct LLM use with long context. This did not happen for multiple reasons: long context is computationally costly, not that accurate beyond relatively trivial lookups and yield little traceability of inputs. Actual agentic search LLM will not kill RAG. What can realistically happen is automating it to a large extent and bundle all the complexity of vector stores, routing, reranking. A typical search process could happen in the way:

*   Query is analyzed, decomposed and some assumptions are made about the user intent.
*   The user might be immediately prompted back if the query is unclear (OpenAI DeepResearch already does it).
*   The model can afterwards either proceed with a generalist search or, if appropriate, immediately proceeds to more specialized research sources. The model has memorized standard API schemes and can call them directly. To save up on inference time, the models could preferably rely on the existing "emulated" versions of the web: APIs, sitemaps and the large ecosystem of the web of data.
*   Search sequences are learned and trained. The model can give up on a bad direction. Or it can take an alternative path like a professional knowledge worker would do. Some of the most impressive results I've been seeing with OpenAI DeepResearch testify of this capacity: badly indexed sources are correctly located through a series of internal deduction.
*   The steps and processes are logged as internal reasoning traces and provide some level of explainability.

In short, the search process is directly engineered. The LLM agent takes the search infrastructure as it is and tries to game its way through way to the best of its ability. There is no immediate need for additional data preparation. There is no need either to train users to interact with generative AI system. As Tim Berners-Lee [underlined](https://www.w3.org/DesignIssues/RealUserAgent.html) more than a decade ago "One way to think about \[agent\] is that the program does, in each instance, exactly what the user would want it to do if asked specifically. "

Now, to get a clearer view of actual LLM agents put in production, you can start to transpose this approach to other domains. An actual network engineering agents would similarly be able to interact directly with the existing infra to generate device configurations based on requirements (routers, switches, firewalls), analyze network topologies and suggest optimizations or parse error logs to identify root causes of network issues. An actual financial agent would be trained to provide seamless and accurate translation of the competing data standards (like ISO 20022 to MT103). None of theses things are currently doable with a set of system prompts.

Currently the only actors able to develop actual LLM agents are the big labs. They hold all the cards: the know-how, some of the data (or at least the synthetic recipe to make them) and overall vision of turning their models into products. I'm not sure such a technological concentration is a good things, though it has been considerably helped by the reluctance of the funding ecosystem to consider actual model training as an actual source of disruption and value creation in the long run.

I generally don't like to overhype things. Yet, given the large potential of disruption and value capture, I do believe it's becoming fast critical to democratize the training and deployment of actual LLM agents. So opening verifiers, GRPO training sample and, maybe soon, complex synthetic pipelines and emulators.

2025, the year of agents? It could still be. Let's see what we make of it.

[Grav](http://getgrav.org/) was with by [Trilby Media](https://trilby.media/).

[](https://vintagedata.org/blog)

*   [Vintage Data](https://vintagedata.org/blog/)
*   [Posts](https://vintagedata.org/blog/posts)
    *   [Actual LLM agents are coming](https://vintagedata.org/blog/posts/designing-llm-agents)
    *   [The Model is the Product](https://vintagedata.org/blog/posts/model-is-the-product)
    *   [What's the deal with mid-training?](https://vintagedata.org/blog/posts/what-is-mid-training)
