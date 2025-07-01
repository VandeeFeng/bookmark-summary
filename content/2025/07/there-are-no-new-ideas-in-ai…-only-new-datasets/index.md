---
title: There Are No New Ideas in AI… Only New Datasets
date: 2025-07-01
extra:
  source: https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only
  original_title: There Are No New Ideas in AI… Only New Datasets
---
## Summary
**摘要**：  
文章探讨了AI领域近年的快速进步，指出这种进步并非源于全新理论的突破，而是依赖于新数据集的发掘和应用。作者回顾了过去15年AI发展的四大里程碑（深度神经网络、Transformer架构、RLHF和推理模型），发现其核心技术早在几十年前就已存在，关键在于首次大规模应用了新数据源（如ImageNet、互联网文本、人类反馈、验证器数据）。研究认为当前AI的改进更多依赖于数据而非算法创新，并预测未来突破点可能来自未开发的视频或机器人传感器数据。文章质疑了主流研究者过多关注模型优化而非数据获取的现象，引用“苦涩的教训”理论强调数据规模的价值，指出当前模型的性能瓶颈本质上是数据源的限制，而非算法本身。

**要点总结**：  
1. **AI进步的核心驱动力是新数据集而非算法创新**：四大技术里程碑（深度神经网络、Transformer、RLHF、推理模型）的基础理论早已存在，其突破性在于首次规模化应用ImageNet图像数据、互联网文本、人类反馈和可验证程序作为新数据源。  
2. **现有技术可能已达数据利用上限**：研究案例显示，即使开发新型SSM架构也难以超越Transformer在相同数据集上的表现，表明特定数据集包含的信息存在学习上限。  
3. **行业误将资源集中于算法优化**：95%的研究聚焦模型改进，但实际效果边际递减，近期大模型（如GPT-4.5）性能提升有限，反映出当前文本数据潜力接近耗尽。  
4. **未来突破依赖于新数据类型的开发**：未被充分挖掘的YouTube视频数据（含语音/物理/文化信息）和机器人传感器数据可能成为下一代AI训练的“第五数据范式”，但需硬件效率提升作为前提条件。  
5. **“苦涩的教训”理论得到验证**：历史表明计算力和数据规模比精巧算法更能推动AI进步，建议研究者应转向数据获取基础设施而非模型架构的创新。
## Full Content
Title: There Are No New Ideas in AI… Only New Datasets

URL Source: https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only

Published Time: 2025-04-09T21:32:03+00:00

Markdown Content:
Most people know that AI has made unbelievable progress over the last fifteen years– especially in the last five. It might feel like that progress is _*inevitable*_ – although large paradigm-shift-level breakthroughs are uncommon, we march on anyway through a stream of slow & steady progress. In fact, some researchers have recently declared a [“Moore’s Law for AI”](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) where the computer’s ability to do certain things (in this case, certain types of coding tasks) increases exponentially with time:

[![Image 1: Length of asks AIs can do is doubling every 7 months](https://substackcdn.com/image/fetch/$s_!56cS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6c8b571-bdbe-46cc-aa5c-8fd5e5555b01_720x430.png)](https://substackcdn.com/image/fetch/$s_!56cS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6c8b571-bdbe-46cc-aa5c-8fd5e5555b01_720x430.png)

the proposed “Moore’s Law for AI”. (by the way, anyone who thinks they can run an autonomous agent for an hour with no intervention as of April 2025 is fooling themselves)

Although I don’t really agree with this specific framing for a number of reasons, I can’t deny the trend of progress. Every year, our AIs get a little bit smarter, a little bit faster, and a little bit cheaper, with no end in sight.

Most people think that this continuous improvement comes from a steady supply of ideas from the research community across academia – mostly MIT, Stanford, CMU – and industry – mostly Meta, Google, and a handful of Chinese labs, with lots of research done at other places that we’ll never get to learn about.

And we certainly have made a lot of progress due to research, especially on the systems side of things. This is how we’ve made models cheaper in particular. Let me cherry-pick a few notable examples from the last couple years:

- in 2022 Stanford researchers gave us [FlashAttention](https://arxiv.org/abs/2205.14135)), a better way to utilize memory in language models that’s used literally everywhere;

- in 2023 Google researchers developed [speculative decoding](https://arxiv.org/abs/2211.17192), which all model providers use to speed up inference (also developed at [DeepMind](https://arxiv.org/pdf/2302.01318), I believe concurrently?)

- in 2024 a ragtag group of internet fanatics developed [Muon](https://kellerjordan.github.io/posts/muon/), which seems to be a better optimizer than SGD or Adam and may end up as the way we train language models in the future

- in 2025 DeepSeek released [DeepSeek-R1](https://arxiv.org/abs/2501.12948), an open-source model that has equivalent reasoning power to similar closed-source models from AI labs (specifically Google and OpenAI)

So we’re definitely figuring stuff out. And the reality is actually cooler than that: we’re engaged in a decentralized globalized exercise of Science, where findings are shared openly on [ArXiv](https://arxiv.org/) and at conferences and on social media and every month we’re getting incrementally smarter.

If we’re doing so much important research, why do some argue that progress is slowing down? [People are still complaining](https://www.lesswrong.com/posts/4mvphwx5pdsZLMmpY/recent-ai-model-progress-feels-mostly-like-bullshit). The two most recent huge models, [Grok 3](https://x.ai/news/grok-3) and [GPT-4.5](https://openai.com/index/introducing-gpt-4-5/), only obtained a marginal improvement on capabilities of their predecessors. In one particularly salient example, when [language models were evaluated on the latest math olympiad exam](https://arxiv.org/abs/2503.21934v1), they scored only 5%, indicating that [recent announcements may have been overblown](https://cdn.openai.com/o1-system-card-20241205.pdf) when reporting system ability.

And if we try to chronicle the _*big*_ breakthroughs, the real paradigm shifts, they seem to be happening at a different rate. Let me go through a few that come to mind:

1. Deep neural networks: Deep neural networks first took off after the [AlexNet model](https://www.notion.so/There-Are-No-New-Ideas-in-AI-Only-New-Data-1cf5109a45d880e6b0d5d6e3a4ba2fdc?pvs=21) won an image recognition competition in 2012

2. Transformers + LLMs: in 2017 Google proposed transformers in [Attention Is All You Need](https://arxiv.org/abs/1706.03762), which led to [BERT](https://arxiv.org/abs/1810.04805) (Google, 2018) and the original [GPT](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) (OpenAI, 2018)

3. RLHF: first proposed (to my knowledge) in the [InstructGPT paper](https://arxiv.org/abs/2203.02155) from OpenAI in 2022

4. Reasoning: in 2024 OpenAI released O1, which led to DeepSeek R1

If you squint just a little, these four things (DNNs → Transformer LMs → RLHF → Reasoning) summarize everything that’s happened in AI. We had DNNs (mostly image recognition systems), then we had text classifiers, then we had chatbots, now we have reasoning models (whatever those are).

Say we want to make a fifth such breakthrough; it could help to study the four cases we have here. What new research ideas led to these groundbreaking events?

It’s not crazy to argue that **all the underlying mechanisms of these breakthroughs existed in the 1990s,** if not before. We’re applying relatively simple neural network architectures and doing either supervised learning (1 and 2) or reinforcement learning (3 and 4).

Supervised learning via cross-entropy, the main way we pre-train language models, emerged from Claude Shannon’s work in the 1940s.

Reinforcement learning, the main way we post-train language models via RLHF and reasoning training, is slightly newer. It can be traced to the [introduction of policy-gradient methods in 1992](https://people.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf) (and these ideas were certainly around for the first edition of the Sutton & Barto “Reinforcement Learning” textbook in 1998).

Ok, let’s agree for now that these “major breakthroughs” were arguably fresh applications of things that we’d known for a while. First of all – this tells us something about the _*next*_ major breakthrough (that “secret fifth thing” I mentioned above). Our breakthrough is probably not going to come from a completely new idea, rather it’ll be the resurfacing of something we’ve known for a while.

But there’s a missing piece here: each of these four breakthroughs **enabled us to learn from a new data source:**

1. AlexNet and its follow-ups unlocked [ImageNet](http://(https//www.image-net.org/), a large database of class-labeled images that drove fifteen years of progress in computer vision

2. Transformers unlocked training on “The Internet” and a race to download, categorize, and parse all the text on [The Web](https://arxiv.org/abs/2101.00027) (which [it seems](https://www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implications)[we’ve mostly done](https://arxiv.org/abs/2305.16264)[by now](https://arxiv.org/abs/2305.13230))

3. RLHF allowed us to learn from human labels indicating what “good text” is (mostly a vibes thing)

4. Reasoning seems to let us learn from [“verifiers”](http://incompleteideas.net/IncIdeas/KeytoAI.html), things like calculators and compilers that can evaluate the outputs of language models

Remind yourself that each of these milestones marks the first time the respective data source (ImageNet, The Web, Humans, Verifiers) was used at scale. Each milestone was followed by a frenzy of activity: researchers compete to (a) siphon up the remaining useful data from any and all available sources and (b) make better use of the data we have through new tricks to make our systems more efficient and less data-hungry. (I expect we’ll see this trend in reasoning models throughout 2025 and 2026 as researchers compete to find, categorize, and verify everything that might be verified.)

[![Image 2: How to train and validate on Imagenet](https://substackcdn.com/image/fetch/$s_!U_q8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ddd3045-3daa-4adf-8d06-c75b3ac6f436_750x300.jpeg)](https://substackcdn.com/image/fetch/$s_!U_q8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ddd3045-3daa-4adf-8d06-c75b3ac6f436_750x300.jpeg)

Progress in AI may have been inevitable once we gathered [ImageNet](https://www.image-net.org/), at the time the largest public collection of images from the Web

There’s something to be said for the fact that our actual technical innovations may not make a huge difference in these cases. Examine the counterfactual. If we hadn’t invented AlexNet, maybe another architecture would have come along that could handle ImageNet. If we never discovered Transformers, perhaps we would’ve settled with LSTMs or SSMs or found something else entirely to learn from the mass of useful training data we have available on the Web.

This jibes with the theory some people have that nothing matters but data. Some researchers have observed that for all the training techniques, modeling tricks, and hyperparameter tweaks we make, the thing that makes the biggest difference by-and-large is changing the data.

As one salient example, some researchers worked on [developing a new BERT-like model using an architecture other than transformers](https://arxiv.org/abs/2212.10544). They spent a year or so tweaking the architecture in hundreds of different ways, and managed to produce a different type of model (this is a state-space model or “SSM”) that performed about equivalently to the original transformer when trained on the same data.

This discovered equivalence is really profound because it hints that _*there is an upper bound to what we might learn from a given dataset*_. All the training tricks and model upgrades in the world won’t get around the cold hard fact that there is only so much you can learn from a given dataset.

And maybe this apathy to new ideas is what we were supposed to take away from [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html). If data is the only thing that matters, why are 95% of people working on new methods?

The obvious takeaway is that our next paradigm shift isn’t going to come from an improvement to RL or a fancy new type of neural net. It’s going to come when we unlock a source of data that we haven’t accessed before, or haven’t properly harnessed yet.

One obvious source of information that a lot of people are working towards harnessing is video. According to [a random site on the Web](https://www.dexerto.com/entertainment/how-many-videos-are-there-on-youtube-2197264/), about 500 hours of video footage are uploaded to YouTube *per minute*. This is a ridiculous amount of data, much more than is available as text on the entire internet. It’s potentially a much richer source of information too as videos contain not just words but the inflection behind them as well as rich information about physics and culture that just can’t be gleaned from text.

It’s safe to say that as soon as our models get efficient enough, or our computers grow beefy enough, Google is going to start training models on YouTube. They own the thing, after all; it would be silly not to use the data to their advantage.

A final contender for the next “big paradigm” in AI is a data-gathering systems that some way _embodied_– or, in the words of a regular person, robots. We’re currently not able to gather and process information from cameras and sensors in a way that’s amenable to training large models on GPUs. If we could build smarter sensors or scale our computers up until they can handle the massive influx of data from a robot with ease, we might be able to use this data in a beneficial way.

It’s hard to say whether YouTube or robots or something else will be the Next Big Thing for AI. We seem pretty deeply entrenched in the camp of language models right now, but we also seem to be running out of language data pretty quickly. But if we want to make progress in AI, maybe we should stop looking for new ideas, and start looking for new data.

