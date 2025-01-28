---
title: Andrej Karpathy's thoughts about deepseek-R1
date: 2025-01-28
extra:
  source: https://readwise.io/reader/shared/01jjnc4z3zwm9d0kzjp1ecrpxm/
  original_title: Andrej Karpathy's thoughts about deepseek-R1
---
## Summary
**摘要**：
这篇文章讨论了深度学习的计算需求，特别是与AI中其他算法相比的极端能源需求，并提出了计算能力作为长期实现智能的上限观点。文章还探讨了数据在深度学习中的作用，指出计算可以创造大量数据，并与强化学习相关。作者指出，生成合成数据并对其排名或筛选等操作等同于执行零至单位优势函数，这实际上是实际上应用了基本的强化学习概念。文章进一步解释了两种主要的深度学习学习类型：模仿学习（例如，预训练和监督微调）和试错学习（强化学习）。文章指出，试错学习远比模仿学习更具颠覆性、更强大，它是深度学习中大部分惊人成果的来源，并列举了AlphaGo作为具体案例。文章还讨论了生成模型的行为如何以不可预测的方式产生策略，这些策略是通过试错学习过程中模型的内部思考和反馈而出现的。此外，讨论了深度搜索或其他AI实体在试错学习过程中发现重新评估假设、回溯尝试新方法等有益策略的能力。

**要点总结**：
- **深度学习的计算需求**：深度学习在计算资源上的需求与其他AI算法相比极其庞大，不过不应低估计算在长期智能实现潜力上的作用。
- **数据生成与计算**：数据在AI中作为独立类别存在，但计算在数据的生成中发挥着关键作用，数据可以通过计算来创造和增强，与此同时强化学习可以看作“合成数据生成”与“强化学习”的等价过程。
- **试错学习与模仿学习**：在AI学习中出现的两种方式：试错学习（强化学习）与模仿学习（预训练、监督微调），其中试错学习更具有颠覆性、创新性和影响力。
- **试错学习的力量**：试错学习的策略和表现，如在AlphaGo等案例中的应用，相较于模仿学习展示出深度学习的核心价值和“啊哈时刻”。
- **资源限制下的创新**：在有限的GPU资源下完成高标准大模型训练的创新演示，强调了数据与算法在资源约束条件下的创新潜力和实际效果。
## Full Content
Title: I don't have too too much to add on top... | annotated by Vandee

URL Source: https://readwise.io/reader/shared/01jjnc4z3zwm9d0kzjp1ecrpxm/

Published Time: 2025-01-27

Markdown Content:
I don't have too too much to add on top of this earlier post on V3 and I think it applies to R1 too (which is the more recent, thinking equivalent).

I will say that Deep Learning has a legendary ravenous appetite for compute, like no other algorithm that has ever been developed in AI. You may not always be utilizing it fully but I would never bet against compute as the upper bound for achievable intelligence in the long run. Not just for an individual final training run, but also for the entire innovation / experimentation engine that silently underlies all the algorithmic innovations.

Data has historically been seen as a separate category from compute, but even data is downstream of compute to a large extent - you can spend compute to create data. Tons of it. You've heard this called synthetic data generation, but less obviously, there is a very deep connection (equivalence even) between "synthetic data generation" and "reinforcement learning". In the trial-and-error learning process in RL, the "trial" is model generating (synthetic) data, which it then learns from based on the "error" (/reward). Conversely, when you generate synthetic data and then rank or filter it in any way, your filter is straight up equivalent to a 0-1 advantage function - congrats you're doing crappy RL.

Last thought. Not sure if this is obvious. There are two major types of learning, in both children and in deep learning. There is 1) imitation learning (watch and repeat, i.e. pretraining, supervised finetuning), and 2) trial-and-error learning (reinforcement learning). My favorite simple example is AlphaGo - 1) is learning by imitating expert players, 2) is reinforcement learning to win the game. Almost every single shocking result of deep learning, and the source of all _magic_ is always 2. 2 is significantly significantly more powerful. 2 is what surprises you. 2 is when the paddle learns to hit the ball behind the blocks in Breakout. 2 is when AlphaGo beats even Lee Sedol. And 2 is the "aha moment" when the DeepSeek (or o1 etc.) discovers that it works well to re-evaluate your assumptions, backtrack, try something else, etc. It's the solving strategies you see this model use in its chain of thought. It's how it goes back and forth thinking to itself. These thoughts are _emergent_ (!!!) and this is actually seriously incredible, impressive and new (as in publicly available and documented etc.). The model could never learn this with 1 (by imitation), because the cognition of the model and the cognition of the human labeler is different. The human would never know to correctly annotate these kinds of solving strategies and what they should even look like. They have to be discovered during reinforcement learning as empirically and statistically useful towards a final outcome.

(Last last thought/reference this time for real is that RL is powerful but RLHF is not. RLHF is not RL. I have a separate rant on that in an earlier tweet

[https://t.co/RMIpFPVpuM](https://t.co/RMIpFPVpuM))

![Image 4](https://pbs.twimg.com/profile_images/1296667294148382721/9Pr6XrPB.jpg)

DeepSeek (Chinese AI co) making it look easy today with an open weights release of a frontier-grade LLM trained on a joke of a budget (2048 GPUs for 2 months, $6M).

For reference, this level of capability is supposed to require clusters of closer to 16K GPUs, the ones being brought up today are more around 100K GPUs. E.g. Llama 3 405B used 30.8M GPU-hours, while DeepSeek-V3 looks to be a stronger model at only 2.8M GPU-hours (~11X less compute). If the model also passes vibe checks (e.g. LLM arena rankings are ongoing, my few quick tests went well so far) it will be a highly impressive display of research and engineering under resource constraints.

Does this mean you don't need large GPU clusters for frontier LLMs? No but you have to ensure that you're not wasteful with what you have, and this looks like a nice demonstration that there's still a lot to get through with both data and algorithms.

Very nice & detailed tech report too, reading through.

[twitter.com/i...](https://twitter.com/i/web/status/1872242657348710721)

