Title: The Model is the Product

URL Source: https://vintagedata.org/blog/posts/model-is-the-product

Markdown Content:
There were a lot of speculation over the past years about what the next cycle of AI development could be. Agents? Reasoners? Actual multimodality?

I think it's time to call it: the model is the product.

All current factors in research and market development push in this direction.

*   Generalist scaling is stalling. This was the whole message behind the release of GPT-4.5: capacities are growing linearly while compute costs are on a geometric curve. Even with all the efficiency gains in training and infrastructure of the past two years, OpenAI can't deploy this giant model with a remotely affordable pricing.
*   Opinionated training is working _much_ better than expected. The combination of reinforcement learning and reasoning means that models are suddenly learning tasks. It's not machine learning, it's not base model either, it's a secret third thing. It's even tiny models getting suddenly scary good at math. It's coding model no longer just generating code but managing an entire code base by themselves. It's Claude playing Pokemon with very poor contextual information and no dedicated training.
*   Inference cost are in free fall. The recent optimizations from DeepSeek means that all the available GPUs could cover a demand of 10k tokens per day from a frontier model for… the entire earth population. There is nowhere this level of demand. The economics of selling tokens does not work anymore for model providers: they have to move higher up in the value chain.

This is also an uncomfortable direction. All investors have been betting on the application layer. In the next stage of AI evolution, the application layer is likely to be the first to be automated and disrupted.

Shapes of models to come.
-------------------------

Over the past weeks, we have seen two prime example of this new generation of models as a product: OpenAI's DeepResearch and Claude Sonnet 3.7.

I've read a lot of misunderstandings about DeepResearch, which isn't helped by the multiplication of open and closed clones. OpenAI has not built a wrapper on top of O3. They have [trained an entirely new model](https://cdn.openai.com/deep-research-system-card.pdf), able to perform search internally, without any external calls, prompts or orchestration:

> The model learned the core browsing capabilities (searching, clicking, scrolling, interpreting files) (…) and how to reason to synthetize a large number of websites to find specific pieces of information or write comprehensive reports through reinforcement learning training on these browsing tasks.

DeepResearch is not a standard LLM, nor a standard chatbot. It's a new form of _research language model_, explicitly designed to perform search tasks end to end. The difference is immediately striking to everyone using it seriously: the model generate lengthy reports with consistent structure and underlying source analysis process. In comparison as Hanchung Lee [underlined](https://leehanchung.github.io/blogs/2025/02/26/deep-research/) all the other DeepSearch, including the Perplexity and Google variant, are just your usual models with a few twists:

> Google’s Gemini and Perplexity’s chat assistants also offer “Deep Research” features, but neither has published any literature on how they optimized their models or systems for the task or any substaintial quantitative evaluations (…) We will make an assumption that the fine-tuning work done is non-substantial.

Anthropic has been laying their current vision ever clearer. In December, they introduced a controversial but, to my mind, correct [definition](https://www.anthropic.com/research/building-effective-agents) of agent models. Similarly to DeepSearch, an agent has to perform the targeted tasks internally: they "dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks".

What most agent startups are currently building is not agents, it's workflows, that is "systems where LLMs and tools are orchestrated through predefined code paths." Workflows may still bring some value, especially for vertical adaptations. Yet, to anyone currently working in the big labs it's strikingly obvious that all major progress in autonomous systems will be through redesigning the models in the first place.

We had a very concrete demonstration of this with the release of Claude 3.7, a model primarily trained with complex code use cases in mind. All the workflow adaptation like Devin had a major boost on SWE benchmarks.

To give it another example done at a much smaller scale: at Pleias we're currently working on automating RAG. Current RAG systems are a lot of interconnected yet brittle workflows: routing, chunking reranking, query interpretation, query expansion, source contextualization, search engineering. With the evolving training tech stack, there is a real potential to bundle all theses processes in two separate yet interconnected models, one for data preparation and the other for search/retrieval/report generation. This requires an elaborated synthetic pipeline and entirely new reward functions for reinforcement learning. Actual training, actual research.

What all this all means in practice: displacing complexity. Training anticipates a wide range of actions and edge cases, so that deployment becomes much more simple. But in this process most of the value is now created and, likely in the end, captured by the model trainer. In short, what Claude aims to disrupt and replace the current workflows like this basic "agent" system from llama index:

![Image 1: Llama Index Basic Agent](https://huggingface.co/datasets/Pclanglais/course-material/resolve/main/llama_index.png)

With this:

![Image 2: Claude Agent](https://huggingface.co/datasets/Pclanglais/course-material/resolve/main/claude.png)

Training or being trained on.
-----------------------------

To reassert: the big labs are not advancing with an hidden agenda. While they can be opaque at time, they laying it all in the open: they will bundle, they will go up the application layer and they will attempt to capture most of the value there. And the commercial consequences are quite clear. Naveen Rao, the Gen AI VP of Databricks, [phrased it quite well](https://x.com/NaveenGRao/status/1886544584588619840):

> all closed AI model providers will stop selling APIs in the next 2-3 years. Only open models will be available via APIs (…) Closed model providers are trying to build non-commodity capabilities and they need great UIs to deliver those. It's not just a model anymore, but an app with a UI for a purpose.

So what is happening right now is just a lot of denial. The honeymoon period between model providers and wrappers is over. Things could evolve in both direction:

*   Claude Code and DeepSearch are early technical and product experiments in this direction. You will notice that DeepSearch is not available through an API, only used to create value for the premium subscriptions. Claude Code is a minimalistic terminal integration. Weirdly enough, while Claude 3.7 works perfectly in Claude Code, Cursor struggles with it and I've already seen several high end users cancelling their subscriptions as a result. Actual LLM agents doesn't care about pre-existing workflows: they replace it.
*   The most high profile wrapper are now scrambling to become hybrid AI training companies. They do have some training capacities, though very little advertised. One of Cursor main assets is their small autocompletion model. WindSurf has their internal cheap code model, Codium. Perplexity always relied on home classifiers for routing and recently pivoted to train their own DeepSeek variant for search purposes.
*   For smaller wrappers, not much will change, except likely increased reliance on agnostic inference providers if the big labs entirely let go of this market. I do also expect to see much more focus on UI which is still dramatically underestimated, as even more generalist models are likely to bundle common deployment takss, especially for RAG.

In short the dilemma for most successful wrappers is simple: training or being trained on. What they are doing right now is both free market research for the big labs but, even, as all outputs is ultimately generated through model providers, free data design and generation.

What will happen afterwards is anyone guess. Successful wrappers do have the advantage of knowing their vertical well and accumiulating a lot of precious user feedbacks. Yet, in my experience, it's easier to go down from the model to application layers than building an entirely new training capacities from scratch. Wrappers may not have been helped by their investors either. From what I overheard, there is such a negative polarization against training, they almost have to hide what is going to be their most critical value: neither cursor small nor codium are properly documented at this moment.

Reinforcement learning was not priced in.
-----------------------------------------

This brings me to the actual painful part: currently all AI investments are correlated. Funds are operating under the following assumptions:

*   The real value lay exclusively in an application layer independent from the model layer that is best positioned to disrupt existing market.
*   Model providers will only sell tokens at an ever lowering price, making wrappers in turn more profitable.
*   Close models wrapping will satisfy all the existing demands, even in regulated sectors with long lasting concerns over external dependencies.
*   Building any training capacity is just a waste of time. This does not include only pre-training but all forms of training.

I'm afraid this increasingly look like an adventurous bet and an actual market failure to accurately price the latest technical developments, especially in RL. In the current economic ecosystem, venture funds are meant to find uncorrelated investments. They will not beat S&P500 but that's not what larger institutional investors are looking for: they want to bundle risks, ensure that in a bad year at least some things will work out. Model training is like a textbook perfect example for this: lots of potential for disruption in a context where most western economies are on course for a recession. And yet model trainers can't raise, or at least not in the usual way. Prime Intellect is one of the few new western ai training companies that has a clear potential to become a frontier lab. Yet, despite their achievements including the training of the first decentralized LLM, they struggled to raise more than your usual wrapper.

Beyond that, aside from the big lab, the current training ecosystem is very tiny. You can count all theses companies on your hands: Prime Intellect, Moondream, Arcee, Nous, Pleias, Jina, the HuggingFace pretraining team (actually tiny)… Along with a few more academic actors (Allen AI, Eleuther…) they build and support most of the current open infrastructure for training. In Europe, I know that at least 7-8 LLM projects will integrate the Common Corpus and some of the pretraining tools we developed at Pleias — and the rest will be fineweb, and likely post-training instruction sets from Nous or Arcee.

There is something deeply wrong in the current funding environment. Even OpenAI senses it now. Lately, there was some [felt irritation](https://x.com/khoomeik/status/1892743475843813680) at the lack of "vertical RL" in the current Silicon Valley startup landscape. I believe the message comes straight from Sam Altman and will likely result in some adjustment in the next YC batch but pinpoint to a larger shift: soon the big labs select partners won't be API customers but associated contractors involved in the earlier training stage.

If the model is the product, you cannot necessarily build it alone. Search and code are easy low hanging fruits: major use cases for two years, the market is nearly mature and you can ship a new cursor in a few months. Now many of the most lucrative AI uses cases in the future are not at this advanced stage of development — typically, think about all these rule based system that still rule most of the world economy… Small dedicated teams with a cross-expertise and a high level of focus may be best positioned to tackle this— eventually becoming potential acquihire once the initial ground work is done. We could see the same pipeline in the UI side. Some preferred partner, getting exclusive API access to close specialized models, provided they get on the road for business acquisition.

I haven't mentioned DeepSeek, nor Chinese labs so far. Simply because DeepSeek is already one step further: not model as a product, but as a universal infrastructure layer. Like OpenAI and Anthropic, Lian Wenfeng [lays his plans in the open](https://www.lesswrong.com/posts/kANyEjDDFWkhSKbcK/two-interviews-with-the-founder-of-deepseek):

> We believe that the current stage is an explosion of technological innovation, not an explosion of applications (…) If a complete upstream and downstream industrial ecosystem is formed, then there is no need for us to make applications ourselves. Of course, there is no obstacle for us to make applications if needed, but research and technological innovation will always be our first priority.

At this stage, working only on applications is like "fighting the next wars with last war generals". I'm afraid we're at the point where many in the west are not even aware the last war is over.
