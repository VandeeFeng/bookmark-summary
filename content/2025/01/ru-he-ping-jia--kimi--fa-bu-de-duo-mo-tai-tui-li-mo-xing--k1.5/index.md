---
title: 如何评价 Kimi 发布的多模态推理模型 k1.5
date: 2025-01-23
extra:
  source: https://www.fxzhihu.com/question/10114790245/answer/84028353434
  original_title: 如何评价 Kimi 发布的多模态推理模型 k1.5
---
## Summary
**摘要**：
这篇文章主要讨论了Kimi团队在最新的多模态推理模型k1.5方面的工作，重点集中在它们解决模型推理过程中的思考和教训。主要涉及利用长文本输入（Context）和长文本输出（Chain of Thought）的模型优化，以及通过强化学习（RL）训练模型提升性能。文章也提及了团队在实现过程中遇到的关键问题和解决思路，特别是如何让模型通过强化学习进行自我反思和优化，减少犯错并提升长期价值。最终，作者强调了在持续推进AI研究和应用时，注重模型能否像人类一样进行自由思考的必要性。

**要点总结**：
- **技术聚焦**：Kimi团队发布k1.5模型，主要亮点在于对长Chain of Thought的有效性进行的深入探索和复现。
- **成本与性能**：在考量成本与性能的关系中，认识到长文本输出带来的挑战与价值，决定投入资源以提升模型的性能和精度。
- **跨领域启发**：通过观看特定的视频和学习重要文稿，从AlphaGo和LLM的学习过程，以及人类走棋的奖赏制定等多样来源中汲取灵感。
- **强化学习策略**：明确采用强化学习来训练模型，特别是In Context Reinforcement Learning（ICRL）方法，通过模仿人类思考过程，让模型自行搜索和自我校正。
- **长文本探索的技术难以度**：面对长文本输出条件下奖励信号难以准确定义的挑战，提出用原始的长文本作为历史信息，采用奖励信号从模型的自我反思过程中获取。
- **模型自身能力的长远作用**：强调模型自身能力的重要性，假以时日，技术发展中模Sus能实现的前途，对于模型能力的推动是必不可少的，而短期结构化工作可能被取代。
- **强化学习在长文本解释中的应用**：基于奖励信号和自反思，设计强化学习策略鼓励模型进行有用的探索，并通过基于竞争策略的训练手段提升模型在长文本解释方面的表现。
- **创造更多有价值的问题答案**：最终目标是在允许犯错的同时，优化模型性能，系统旨在为AI创造更多情境复杂、结构多元的真实问题，实现多种答案的自适应处理。
## Full Content
Title: 如何评价 Kimi 发布的多模态推理模型 k1.5？ - @Flood Sung | FxZhihu

URL Source: https://www.fxzhihu.com/question/10114790245/answer/84028353434

Markdown Content:
* * *

亲自答一下

这个技术报告是我们的结果，那么相信大家也想知道一些思考过程吧哈哈，所以这里主要想和大家分享一下o1复现的一些关键思考过程，也就是我自己的Long Chain of Thoughts.

2024年9月12号，o1 发布，震撼，效果爆炸，Long CoT的有效让我陷入反思Reflection。

因为Long CoT的有效性其实在一年多前就已经知道了，Tim [@周昕宇](https://www.zhihu.com/people/0224c265bcb1f3ce5e711352fa64d547) 很早就验证过 使用很小的模型训练模型做几十位的加减乘除运算，将细粒度的运算过程合成出来变成很长的CoT数据做SFT，就可以获得非常好的效果。我依然记得当时看到那个效果的震撼。我们意识到Long Context的重要性，所以率先考虑把Context搞长，但却对Long CoT这件事情不够重视。其实主要还是考虑了成本问题。Long Context主要做的是长文本输入，有Prefill，有Mooncake加持，成本速度可控，而Long CoT是长文本输出，成本高很多，速度也要慢很多。在这种情况下，把输出搞长就没有成为一个高优选项。

但是，还有什么比Performance更重要呢？成本速度有摩尔定律加持，可以不断下降，只要把performance搞上去，剩下的都不是主要问题。

所以，我们得搞Long CoT，搞o1。

但具体要怎么搞呢？

我们需要先收集一些信息，来反推o1会是怎么做的？RL-LLM会是怎么做的？（对，这里触发了我的搜索API ）

首先我们观察o1官网上的一些例子，我们发现很明显的一些特征：

*   o1可以**犯错**！！！Long CoT和以前的CoT不一样。
*   o1 往往会反复的反思再尝试，有各种but, wait,...
*   o1的思考方法则不局限，可以重述问题，可以联想，可以分治。。。

然后，两个重要的openai的视频出来了，分别是Noam Brown和Hyung Won Chung的：

[https://youtu.be/eaAonE58sLU?si=TUlOyuYF4SkicSrK](https://youtu.be/eaAonE58sLU?si=TUlOyuYF4SkicSrK)[https://youtu.be/kYWUEV\_e2ss?si=bijCga4Xz8jSaqMA](https://youtu.be/kYWUEV_e2ss?si=bijCga4Xz8jSaqMA)我观看了不止一遍，因为他们这些视频并不是近期拍的，但却要等到o1发布了才发出来，说明他们的talk和o1的实现是紧密相连的。

其中，有两张ppt我觉得是至关重要的：

![Image 20](https://picx.zhimg.com/v2-e853fbe6822d95bbeca8ad8bf5c57689_r.jpg?source=2c26e567)

Noam Brown这张，他告诉了我们Test-Time Search的重要性，确实回想起之前的AlphaGo是这么一回事。很多人以为Noam Brown是告诉大家要把AlphaGo的MCTS用到LLM上，那么其实不是，只是说Search很重要。至于应用到LLM上，那么就是：

> 我们需要让模型能够**自行**搜索！

这也让我重新看了一下Richard Sutton的The Bitter Lesson:

[https://www.cs.utexas.edu/~eunsol/courses/data/bitter\_lesson.pdf](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf)

![Image 21](https://picx.zhimg.com/v2-dc022ffc075b31cca34f2a4b8edcabd9_r.jpg?source=2c26e567)

Sutton早就揭示了一切呀。

接下来就是Hyung Won Chung的Don't Teach, Incentivize。这个带来的启发就更大了：

![Image 22](https://picx.zhimg.com/v2-42e8c8432d1986ed53eaed2b3fb6884c_r.jpg?source=2c26e567)

Hyung Won Chung 为什么特别强调这个呢？Structure，什么是Structure？

MCTS是一种structure，A\* 是一种Structure。当我们人为加了点inductive bias进来强求llm按我们要求的格式进行思考，那么这种思考就是结构化的。而基于我们前面对o1的观察，我们就可以把两件事联系在一起了：

> o1没有限制模型如何思考！

这点非常非常关键！因此我们已经可以基于此排除一些带structure的工作了，MCTS就没必要探索，因为一定不work。

特别的：

现在的各种Agentic Workflow就是各种带structure的东西，它一定会限制模型的能力。

所以，其实我们还可以直接得出一个结论：

> Agentic Workflow只有短期价值，没有长期价值！早晚会被模型本身能力取代掉。

All in All 我们就是要训练模型能够像我们人一样思考，自由的思考！

然后，Noam Brown还有一张ppt也蛮重要：

![Image 23](https://picx.zhimg.com/v2-c757ddad625bf4f6ca4a19fd786cad0c_r.jpg?source=2c26e567)

这个非常直接的告诉我们：

> 去做有精确Reward的RL！不要被Reward Model 给限制住了。

之前RLHF相信做过的同学都知道这是一件非常麻烦的事情，因为Human Preference并无法精准的建模，训的Reward Model又很容易reward hacking，lilian weng都专门写了个blog来讲这件事：

[https://lilianweng.github.io/posts/2024-11-28-reward-hacking/](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/)所以，如果reward都不准确的话，那么要做RL就很难work。RL的performance完全取决于reward。

这不禁就回想起以前做robot locomotion，game ai的时候，一堆的reward shaping。

信息到这里就很明显了：

> 做题，做题，还是做题！做有标准答案的题，刷起来！

math和code就是很直接的两个有标准答案的方向，openai也是往这上面刷，那么我们当然就往上面刷呗。

怕context太长，导致遗忘，我们在这里确认一下前面得到的关键信息：

*   **要训练llm通过RL做题，有精确reward**
*   **不要采取结构化的方法，最终会限制住模型的效果，要让模型自己探索思考范式。**
*   **思考包含了搜索过程，允许犯错。**

好了，接下来我们需要解决如何用RL训练LLM通过Long CoT做题这件事。

很多同学可能会想： 那就用PPO呗！

问题没有这么简单。Long CoT对问题的建模产生了很大的变化。

### o1 实际上是 In Context RL with Self-Critique

o1 实际上是把in context rl的完整trajectory当做一条message给训进去了。

如下面的code:

![Image 24](https://picx.zhimg.com/v2-fe256229ecb5e7af2d945f73f3f45316_r.jpg?source=2c26e567)

什么是In Context RL呢？

[In-context Reinforcement Learning with Algorithm Distillation](https://arxiv.org/abs/2210.14215)不了解的同学可以看这边，简单的说就是模型做next token prediction的过程本身就是一个rl探索过程。

模型做一个题，在Long CoT下，实际上在做什么呢？

实际上也在学习做这个题，它输出的整个轨迹就是：

s1,a1,r1,a2,r2,a3,r3,.....

其中a可以认为是一种解决方法，可以看做action，而r就是reward，但这里是模型自己做reflection得到的reward，所以我说它是自带critic/world model的in context rl。

最近有相关blog也终于说了这件事，大家也是可以看看：

[https://blog.ml.cmu.edu/2025/01/08/optimizing-llm-test-time-compute-involves-solving-a-meta-rl-problem/](https://blog.ml.cmu.edu/2025/01/08/optimizing-llm-test-time-compute-involves-solving-a-meta-rl-problem/)但它没有提到self-critique这个问题。

所以这个事情变复杂了呀。

如果把long cot输出建模成in context rl with self-critique，那么我们怎么优化它呢？

首当其冲的问题就是每一句话的value是多少？

然后你会发现这个value已经非常难以估计了。

举个非常简单的例子：计算1+1=？

然后模型输出 1+1=3，不对，1+1=4呢？也不对，因为4-1=3。那么1+1=1呢？ 不对，因1不等于1-1=0..... 哦对了，左手有一颗糖，右手也有一颗糖，左手的糖放到右手，那么我右手有两颗糖，我知道了，1+1=2

你会发现：

> 如果模型不会反思，那么犯错了就是错的，value就会是负值。但如果模型会反思，那么只要知错能改，最终是对的，那么这些错误都不算错误。value就不应该为负。

由此，我们看到Policy会不会反思，其对应的value差异非常大。我们没办法用一个off policy的value 去优化Policy，而对于next token prediction的场景，我们已非常难以去分解step，也不太可能每一个step都去做大规模mc rollout来估计当前value。更进一步的设想一个context 几乎无限长的场景（10M)，比如可以几乎无限悔棋的围棋，那么这个场景已经无限接近非MDP的状态，以至于value难以估计。

这让我想到了人生：

**o1 即 人生。人生就是一条有限的串行轨迹，各种探索，各种犯错，然而除了杀人放火你无法评价某种犯错/挫折的价值会是好还是坏（比如steve jobs可以被自己创立的公司解雇），最终的结局都取决于自己的目标。**

所以，我们可以从逻辑上判断**我们不要训value，不要搞prm了，因为不会准的。**

**所以，看起来用rl训llm通过Long CoT做题这个问题变简单了：**

> **不管模型中间做错了什么，只要不是重复的，那么最后模型做对了，我们就认为这是一个好的探索，值得鼓励。反之，如果模型一顿探索，最后做错了，那么再努力也是错，要惩罚。**

我们把问题变成了Contextual Bandit的问题。那么我们就可以用REINFORCE的变种来做啦。

![Image 25](https://pic1.zhimg.com/v2-a380844f7f9998a3af794e5e6834a6c9_r.jpg?source=2c26e567)

上面这就是最基本的REINFORCE的公式，简单的说就是做对加梯度，做错减梯度。当然，我们需要让训练更稳定，所以可以加KL，加reward的normalization等等一些小trick，具体可以看下paper。但基本的思想就是这么简单。

有了基本思路，那么剩下的就是实操了。但这里其实还有一个重要问题：

**Long CoT是如何变长的？这可能是最关键的事情。**

惊喜的是在我们实际训练的过程中，我们有了重要的发现：

> 模型会随着训练提升performance也不断增加token数！

也就是这是RL训练过程中模型可以自己涌现的！

**Fantastic！**

这个和友商Deepseek的发现几乎是一样的。看到他们直接做了zero-sft的RL，也是挺impressive！

OK，理清了整个思考过程，也是不容易。感觉自己像个AI，哦不，是AI太像人了。

我们的思考还在继续，那么未来呢？

ok，还有o3在前面，还有很多路要走。

AGI确实就是近在眼前的事情，这个Sam Altman没有乱说。

那么ASI呢？

我重新开始思考ASI。其实对于做RL的人来说，从来都不会把AGI作为目标呀，因为AlphaGo，AlphaStar已经验证了RL可以做superhuman的事情了，那么现在不过是把场景搬到了现实世界。

**给AI一个可衡量的目标，然后让其自己去探索，然后通过RL提升模型，仅此而已。**

未来不过是把这个过程不断的复制到更复杂的场景。

比如给AI一本飞机手册，然后让其自己学会模拟驾驶。

比如让AI写出10万+的公众号文章

比如让AI发布一个复制tiktok的app

比如让AI去写一篇文章中Nature

让我们一起期待一下接下来的进展吧！加油！

