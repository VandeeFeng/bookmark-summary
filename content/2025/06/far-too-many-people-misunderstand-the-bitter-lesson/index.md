---
title: Far too many people misunderstand the bitter lesson
date: 2025-06-28
extra:
  source: https://www.artfintel.com/p/the-bitter-lesson
  original_title: Far too many people misunderstand the bitter lesson
---
## Summary
**摘要**：
《苦乐教训》一文的核心观点是，长期来看，能有效利用计算资源的算法终将胜过依赖人工知识的算法。这一教训被称为"苦涩"，因为短期内依赖人工知识往往能快速获得成果，但最终会陷入发展瓶颈。文章通过计算机象棋和围棋的历史案例说明，尽管专家系统和启发式方法在特定时期表现优异（如深蓝的国际象棋系统和早期的围棋程序），但最终被基于大规模计算和学习的通用方法（如AlphaGo Zero）超越。作者指出，AI领域的历史规律表明：研究者倾向于构建人工知识系统获得短期成就感，但这会阻碍长期突破；真正的进步来自于利用计算规模的搜索和学习方法。当前大型语言模型的发展也面临类似抉择：专注于特定基准测试的人工优化还是提升模型的通用能力。

**要点总结**：
1. **计算规模的重要性**：算法发展的长期胜出者都是能随计算资源扩展而提升效果的方法，因为计算能力持续呈数量级增长，而其他资源增长有限。历史证明依赖固定人工知识的方法终将被更具扩展性的方法超越。
2. **短期收益与长期代价**：将人工知识（如专家系统、手工特征）融入AI系统能在短期内快速提升性能，这在博弈程序发展史（从深蓝到AlphaGo）中反复验证，但这种改进存在性能天花板，最终阻碍根本性突破。
3. **技术转型的阻力机制**：即使新的范式已证明优越性（如深蓝成功后），旧范式仍会持续多年，这与学术职业周期（博士培养、职称晋升）和组织惯性有关，形成"一个时代结束需要机构重组"的转型模式。
4. **当前AI研发的实践启示**：在大型语言模型竞争中，专注于特定基准测试的短期优化（人工数据/规则）虽能快速提升指标，但投资通用能力（合成数据、混合专家模型等可扩展方法）才是长期制胜关键，NVIDIA硬件发展将为此提供支撑。
## Full Content
Title: The Bitter Lesson

URL Source: https://www.artfintel.com/p/the-bitter-lesson

Published Time: 2025-06-26T15:28:07+00:00

Markdown Content:
[The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) is an excellent essay which is overwhelmingly misunderstood. The point of the bitter lesson is that, over time, methods which scale with compute will outperform methods that do not.

It is not:

*   The idea that we should never incorporate human knowledge

*   The idea that deep learning and scale are all we need (Rich is actually relatively skeptical of deep learning)

The entire point of the essay is that, in the last 5 decades, we have seen massive increases in the amount of compute available to us as an industry and we expect to continue to see [massive increases](https://openai.com/index/announcing-the-stargate-project/) in the amount of compute available to AI research. Methods which take advantage of compute will benefit, and those that do not will suffer.

The reason the lesson is bitter is that it is often much easier and quicker to get results by incorporating human knowledge.

If you’re training an autocomplete system in 1995, you’re probably not going to get very far with next token prediction, and instead, handcoded, or statistically generated rules will do better. In 2005, N-gram models are optimal. It isn’t until the mid 2010s that we start to see deep learning dominate in NLP, and not until the late 2010s that self supervised learning becomes dominant. At each point along the way, incorporating human knowledge has been advantageous, and has been a way that you can get an advantage over your competition. But in the long term, it’s a dead end. Methods which take advantage of more compute outperform over a sufficiently long time frame. Compute is the only parameter which we can expect to increase by several orders of magnitude. Much as I wish it were otherwise, it’s unlikely that we’ll see 1000x the number of tokens we have now. But in compute, that’s almost certain.

The canonical example is computer chess. Before [Deep Blue](https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)) expert systems were largely used. Deep Blue showed that leveraging compute to perform extensive searches against a hand coded value function[1](https://www.artfintel.com/p/the-bitter-lesson#footnote-1-166870478) performed extremely well. Deep Blue was a massive win for the “scale compute”/computer search crowd, as it was much more based on scale than human heuristics, but it required an evaluation function with 8000 custom chess features created by human experts, and the evaluation function weighted them using hand selected weights. One measure of the generality of the system is how easy it would be to extend it to a different scenario. To extend Deep Blue to work in Go would be extremely challenging, as one would need to come up with a proper evaluation function by creating another 8000 custom Go features.

Computer Go is another example where human knowledge fell short. [AlphaGo Zero](https://arxiv.org/abs/1712.01815) evaluated against the then state of the art Go bots, which included [Pachi](https://pasky.or.cz/go/pachi-tr.pdf), [GnuGo](https://www.moderndescartes.com/essays/gnugo_to_agz/), and [CrazyStone](https://en.wikipedia.org/wiki/Crazy_Stone_(software)). Pachi and CrazyStone did MCTS with heuristic value functions, and GnuGo was an expert system, with a hand created decision tree to select moves. They were good at the time! But they were all ultimately dead ends. As Rich states in the article:

> The bitter lesson is based on the historical observations that
> 
> 
> 1) AI researchers have often tried to build knowledge into their agents,
> 
> 
> 2) this always helps in the short term, and is personally satisfying to the researcher, but
> 
> 
> 3) in the long run it plateaus and even inhibits further progress, and
> 
> 
> 4) breakthrough progress eventually arrives by an opposing approach based on scaling computation by search and learning.
> 
> 
> The eventual success is tinged with bitterness, and often incompletely digested, because it is success over a favored, human-centric approach.

If you look at [GnuGo’s code](https://github.com/lungzeeyim/GNUgo), it was a lot of hard work by a lot of people, and was dramatically worse than what was possible. What’s surprising is that, while GnuGo [began in 1989](https://www.gnu.org/software/gnugo/devel.html), released continued until 2009, so the authors were undoubtedly aware of Deep Blue and the stunning victory that scaled search had, yet they continued to push forward with their expert system. Brian Lee, a former Google Brain researcher who [replicated AlphaGo within Brain](https://github.com/tensorflow/MiniGo), offers a [compelling explanation](https://www.moderndescartes.com/essays/gnugo_to_agz/) for why:

> I offer another point: that these stages [of the Bitter Lesson] happen over the span of a decade or so. Over this decade, PhDs are minted, career identities built, promotion criteria set, culture defined, and org charts annealed. Much in the way that science progresses one funeral at a time, progress on difficult problems progresses one organization shutdown at a time.

Consider another scenario. You work at a LLM lab, and have to make your benchmark numbers bigger than your competition or you get fired. You have the immediate temptation to include human knowledge, which in this case might be specialized datasets for a specific benchmark.

A better approach would be to make the model _generally_ stronger. Focusing on methods that scale with compute as a filter is a strong bet to make, as Jensen Huang is doing his best to give you multiple orders of magnitude more FLOPS. Methods like test time compute, synthetic data, or MoE models are great examples. But the problem with this approach, which when I write it down seems obvious, is that in the moment, it feels _indulgent_. We _don’t have time_ for proper science, we have to beat the other labs on LiveCodeBench. That is the bitter lesson: DeepSeek focuses on general improvements, gets them working, scales them to 3.8e25 FLOPS, and is SOTA.

*   [What comes next, by Nathan Lambert (Interconnects)](https://substack.com/home/post/p-166556899), discussing, among other aspects, how excellent O3 is.

*   [Undertrained tokens in R1](https://substack.com/home/post/p-158907079?source=queue), by .

*   The [Deep Blue paper](https://x.com/finbarrtimbers/status/1938115342427165035), which is worth reading.

[1](https://www.artfintel.com/p/the-bitter-lesson#footnote-anchor-1-166870478)

Deep Blue is fascinating for a variety of reasons, including the fact that they had custom “chess chips” made to encode the evaluation function in hardware.

