Title: Explainer: What's R1 & Everything Else?

URL Source: https://timkellogg.me/blog/2025/01/25/r1

Markdown Content:
Sat January 25, 2025

![Image 3: Explainer: What's R1 & Everything Else?](https://cdn.pixabay.com/photo/2022/07/18/11/12/statue-7329573_1280.jpg)Is AI making you dizzy? A lot of industry insiders [are feeling the same](https://x.com/emollick/status/1883248352034521281). R1 just came out a few days ago out of nowhere, and then there’s o1 and o3, but no o2. Gosh! It’s hard to know what’s going on. This post aims to be a guide for recent AI develoments. It’s written for people who feel like they _should_ know what’s going on, but don’t, because it’s insane out there.

Timeline
--------

The last few months:

*   Sept 12, ‘24: [o1-preview](https://openai.com/index/introducing-openai-o1-preview/) launched
*   Dec 5, ‘24: [o1 (full version)](https://openai.com/o1/) launched, along with o1-pro
*   Dec 20, ‘24: [o3](https://techcrunch.com/2024/12/20/openai-announces-new-o3-model/) announced, saturates ARC-AGI, hailed as “AGI”
*   Dec 26, ‘24: [DeepSeek V3](https://api-docs.deepseek.com/news/news1226) launched
*   Jan 20, ‘25: [DeepSeek R1](https://api-docs.deepseek.com/news/news250120) launched, matches o1 but open source
*   Jan 25, ‘25: Hong Kong University [replicates R1 results](https://hkust-nlp.notion.site/simplerl-reason)
*   Jan 25, ‘25: Huggingface announces [open-r1](https://github.com/huggingface/open-r1) to replicate R1, fully open source

Also, for clarity:

*   o1, o3 & R1 are reasoning models
*   DeepSeek V3 is a LLM, a base model. Reasoning models are fine-tuned from base models.
*   ~[ARC-AGI](https://arcprize.org/arc) is a benchmark that’s designed to be simple for humans but excruciatingly difficult for AI. In other words, when AI crushes this benchmark, it’s able to do what humans do.~

EDIT: That’s an incorrect understanding of ARC-AGI (thanks Simon Wilison for pointing that out!). Here’s [what Francois Chollet says](https://bsky.app/profile/fchollet.bsky.social/post/3les3izgdj22j):

> I don’t think people really appreciate how simple ARC-AGI-1 was, and what solving it really means.
> 
> It was designed as the simplest, most basic assessment of fluid intelligence possible. Failure to pass signifies a near-total inability to adapt or problem-solve in unfamiliar situations.

Reasoning & Agents
------------------

Let’s break it down.

Reasoning Models != Agents
--------------------------

Reasoning models are able to “think” before respoding. LLMs think by generating tokens. So we’ve training models to generate a ton of tokens in hopes that they stumble into the right answer. The thing is, [it works](https://arxiv.org/abs/2408.00724v2).

AI Agents are defined by two things:

1.  **Autonomy** (agency) to make decisions and complete a task
2.  Ability to **interact** with the outside world

LLMs & reasoning models alone only generate tokens and therefore have no ability to do either of these things. They need **software** in order to make decisions real and give it interaction abilities.

Agents are a **system of AIs**. They’re models tied together with software to autonomously interact with the world. Maybe hardware too.

Reasoning Is Important
----------------------

Reasoning models get conflated with agents because currently, _**reasoning is the bottleneck**_. We need reasoning to plan tasks, supervise, validate, and generally be smart. We can’t have agents without reasoning, but there will likely be some new challenge once we saturate reasoning benchmarks.

Reasoning Needs To Be Cheap
---------------------------

Agents will run for hours or days, maybe 24/7. That’s the nature of acting autonomously. As such, costs add up. As it stands, R1 costs about **30x less** than o1 and achieves similar performance.

Why R1 Is Important
-------------------

It’s cheap, open source, and has validated what OpenAI is doing with o1 & o3.

There had been some predictions made about how o1 works, based on public documentation, and the R1 public paper corroborates all of this almost entirely. So, **we know how o1 is scaling** into o3, o4, …

It’s also open source, and that means the entire world can run with their ideas. Just notice the condensed timeline in the last week, of people re-creating R1 (some claim for $30). Innovation happens when you can iterate quickly and cheaply, and R1 has triggered such an environment.

Most important, R1 **shut down** some very complex ideas (like [DPO](https://arxiv.org/abs/2305.18290) & [MCTS](https://builtin.com/machine-learning/monte-carlo-tree-search)) and showed that the path forward is simple, basic RL.

AI Trajectory
-------------

Where do we stand? Are we hurtling upwards? Standing still? What are the drivers of change?

Pretraining Scaling Is Out
--------------------------

When GPT-4 hit, there were these dumb scaling laws. Increase data & compute, and you simply get a better model (the [pretraining scaling laws](https://medium.com/@biradarmithilesh/introduction-to-llms-and-the-generative-ai-part-2-llm-pre-training-and-scaling-laws-275a0306c9e2)). These are gone. They’re not dead, per se, but we ran into some bumps with getting access to data but discovered new scaling laws.

(Continue reading)

Inference Time Scaling Laws
---------------------------

This is about **reasoning models**, like o1 & R1. [The longer they think, the better they perform.](https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute)

It wasn’t, however, clear how exactly one should perform _more computation_ in order to achieve better results. The naive assumption was that [Chain of Thought (CoT)](https://www.promptingguide.ai/techniques/cot) could work; you just train the model to do CoT. The trouble with that is finding the fastest path to the answer. [Entropix](https://timkellogg.me/blog/2024/10/10/entropix) was one idea, use the model’s internal signals to find the most efficient path. Also things like [Monte Carlo Tree Search (MCTS)](https://builtin.com/machine-learning/monte-carlo-tree-search) , where you generate many paths but only take one. There were several others.

It turns out **CoT is best**. R1 is just doing simple, single-line chain of thought trained by RL (maybe [entropix](https://timkellogg.me/blog/2024/10/10/entropix) was on to something?). Safe to assume o1 is doing the same.

Down-Sized Models (Scaling Laws??)
----------------------------------

The first signal was GPT-4-turbo, and then GPT-4o, and the Claude series, and all other LLMs. They were all getting smaller and cheaper throughout ‘24.

If generating more tokens is your path to reasoning, then lower latency is what you need. Smaller models compute faster (fewer calculations to make), and thus smaller = smarter.

Reinforcement Learning (Scaling Laws??)
---------------------------------------

R1 used [GRPO (Group Rewards Policy Optimization)](https://bsky.app/profile/timkellogg.me/post/3lgb7jatrks24) to teach the model to do CoT at inference time. It’s just dumb reinforcement learning (RL) with nothing complicated. No complicated verifiers, no external LLMs needed. Just RL with basic reward functions for accuracy & format.

[R1-Zero](https://huggingface.co/deepseek-ai/DeepSeek-R1-Zero) is a version of R1 from DeepSeek that only does GRPO and nothing else. It’s more accurate than R1, but it hops between various languages like English & Chinese at will, which makes it sub-optimal for it’s human users (who aren’t typically polyglots).

_Why does R1-zero jump between languages? [My thought](https://bsky.app/profile/timkellogg.me/post/3lgfvtakxg224) is that different languages express different kinds of concepts more effectively. e.g. the whole “what’s the german word for \[paragraph of text\]?” meme._

Today (Jan 25, ‘25), [someone demonstrated](https://bsky.app/profile/timkellogg.me/post/3lgll2ojkbc2g) that _any reinforcement learning_ would work. They tried [GRPO](https://bsky.app/profile/timkellogg.me/post/3lgb7jatrks24), [PPO](https://arxiv.org/abs/1707.06347), and [PRIME](https://github.com/PRIME-RL/PRIME); they all work just fine. And it turns out that the magic number is 1.5B. If the model is bigger than 1.5B, the inference scaling behavior will spontaneously emerge regardless of which RL approach you use.

_How far will it go?_

Model Distilation (Scaling Laws??)
----------------------------------

R1 distilled from previous checkpoints of itself.

Distillation is when one teacher model generates training data for a student model. Typically it’s assumed that the teacher is a bigger model than the student. R1 used previous checkpoints of the same model to generate training data for Supervised Fine Tuning (SFT). They iterate between SFT & RL to improve the model.

_How far can this go?_

A long time ago (9 days), there was a prediction that GPT5 exists and that GPT4o is just a distillation of it. [This article](https://www.thealgorithmicbridge.com/p/this-rumor-about-gpt-5-changes-everything?r=2cpkgh&utm_medium=ios&triedRedirect=true) theorized that OpenAI and Anthropic have found a cycle to keep creating every greater models by training big models and then distilling, and then using the distilled model to create a larger model. I’d say that the R1 paper largely confirms that that’s possible (and thus likely to be what’s happening).

If so, this may continue for a very long time.

_Note: Evidence suggests that the student can [exceed the teacher](https://bsky.app/profile/timkellogg.me/post/3lfwwlosbus2f) during distilation. It’s unclear how much of this is actually happening. The intuition is that distillation is able to help the student find the signal and more quickly converge. [Model collapse](https://www.nature.com/articles/s41586-024-07566-y) is still top of mind, but it seems to have been a mostly needless fear. Model collapse is certainly always possible, but it’s by no means guaranteed and there are even ways to go the opposite way and have the student exceed the teacher._

‘25 Predictions
---------------

Given the current state of things:

*   Pre-training is hard (but not dead)
*   Inference scaling
*   Downsizing models
*   RL scaling laws
*   Model distilation scaling laws

It seems unlikely that AI is slowing down. One scaling law slowed down and 4 more appeared. This thing is going to accelerate and continue accelerating for the foreseeable future.

Geopolitics: Distealing
-----------------------

_I coined that term, distealing, unauthorized distillation of models. Go ahead, use it, it’s a fun word._

Software is political now and AI is at the center. AI seems to be factored into just about every political axis. Most intersting is China vs. USA.

Strategies:

*   USA: heavily funded, pour money onto the AI fire as fast as possible
*   China: under repressive export controls, pour smarter engineers & researchers into finding cheaper solutions
*   Europe: regulate or open source AI, either is fine

There’s been heavy discussion about if DeepSeek distealed R1 from o1. Given the reproductions of R1, I’m finding it increasingly unlikely that that’s the case. Still, a Chinese lab came out of seemingly nowhere and overtook OpenAI’s best available model. There’s going to be tension.

Also, AI will soon (if not already) increase in abilities at an _**exponential rate**_. The political and geopolitical implications are absolutely massive. If anything, people in AI should pay _more attention_ to politics, and also stay open minded on what policies could be good or bad.

Conclusion
----------

Yes, it’s a dizzying rate of development. The main takeaway is that R1 provides clarity where OpenAI was previously opaque. Thus, the future of AI is more clear, and it seems to be accelerating rapidly.

Discussion
----------

*   [Hacker News](https://news.ycombinator.com/item?id=42827601)
*   [Bluesky](https://bsky.app/profile/timkellogg.me/post/3lgmhnqkpwk2l)
*   [Threads](https://www.threads.net/@kelloggt/post/DFSjmrxui4i?xmt=AQGz5edIpFG3IqJOdJOyVSfE0wJy9f1Cy8-HMgkdv6M4og)
*   [Twitter/X](https://x.com/kellogh/status/1883500950171861221)
*   [LinkedIn](https://www.linkedin.com/posts/tim-kellogg-69802913_explainer-whats-r1-and-everything-else-activity-7289268716951797760-DsX9)
