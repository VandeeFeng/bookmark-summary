---
title: Seven replies to the viral Apple reasoning paper – and why they fall short
date: 2025-06-15
extra:
  source: https://garymarcus.substack.com/p/seven-replies-to-the-viral-apple
  original_title: Seven replies to the viral Apple reasoning paper – and why they fall short
---
## Summary
**摘要**：
这篇文章讨论了苹果公司发布的一篇关于大语言模型推理局限性的论文引发的广泛争议和七种主要反驳观点。论文指出，当前的大语言模型在复杂推理任务（如汉诺塔问题）中存在显著缺陷，尤其在远离训练数据分布的情况下表现不佳。作者逐一反驳了七种常见的反对意见，包括人类也会犯错、输出令牌长度限制、作者身份质疑、模型规模提升、通过代码解决问题、案例数量不足以及已有认知等观点。文章强调，这些反驳都未能真正解决核心问题，即单纯扩大模型规模不足以实现通用人工智能（AGI），需要结合神经符号系统等其他方法。作者认为苹果论文和SalesForce的最新研究共同表明，当前技术尚无法可靠处理需要复杂推理和算法精度的任务。

**要点总结**：
1. **人类犯错不能成为模型缺陷的借口**：虽然人类在复杂问题和记忆需求上也有困难，但计算机的初衷正是为了弥补人类不足。大语言模型在汉诺塔等基本算法任务上的表现甚至不如现有专有系统，这与AGI应带来的进步背道而驰。关键在于模型无法在远离训练数据的情况下可靠执行算法。

2. **输出令牌长度限制仅是部分解释**：虽然模型输出长度限制可能导致无法完整表达复杂解决方案（如12盘汉诺塔），但这不能解释模型在255步内可解决的8盘汉诺塔上的失败。真正的通用智能系统不应受此限制。

3. **反驳"论文由实习生撰写"的偏见**：尽管第一作者是实习生，但团队包含多位资深研究者，且科学界第一作者往往是初学者的惯例。重要的是论文质量而非作者身份，类比基因图谱发明者本科期间的重要发现。

4. **单纯增加模型规模并非解决方案**：虽然更大模型可能表现更好，但无法预知何种规模足够解决特定问题。苹果研究表明模型可能在简单任务（6盘）表现良好却在稍复杂情况（8盘）崩溃，这种不可预测性令人担忧。

5. **需要神经符号结合的系统**：模型通过编写代码可能解决部分问题，这验证了神经符号AI的重要性。但仅靠下载代码缺乏概念理解，无法应对新问题或动态环境，正如数学考试考察的是理解而非计算结果。
## Full Content
Title: Seven replies to the viral Apple reasoning paper – and why they fall short

URL Source: https://garymarcus.substack.com/p/seven-replies-to-the-viral-apple

Published Time: 2025-06-12T21:25:07+00:00

Markdown Content:
The Apple paper on [limitations in the “reasoning” of Large Reasoning Models](https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf), which raised challenges for the latest scaling hypothesis, has clearly touched a nerve. Tons of media outlets covered it; huge numbers of people on social media are discussing.

M[y own post here laying out the Apple paper in historical and scientific context](https://open.substack.com/pub/garymarcus/p/a-knockout-blow-for-llms?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false)was so popular that well over 150,000 people read it, biggest in this newsletter’s history. _The Guardian_ published an adaptation of my post (“[When billion-dollar AIs break down over puzzles a child can do, it’s time to rethink the hype](https://www.theguardian.com/commentisfree/2025/jun/10/billion-dollar-ai-puzzle-break-down)”) The editor tells me readers spent a long time reading it, notably longer than usual, as if people really wanted to understand the arguments in detail. (The ACM computer science society is reposting the essay, too, and [there is now a French version as well](https://legrandcontinent.eu/fr/2025/06/10/ia-llm-marcus/)).

Tons of GenAI optimists took cracks at the Apple paper (see below), and it is worth considering their arguments. Overall I have seen roughly seven different efforts at rebuttal, ranging from nitpicking and ad hominem to the genuinely clever. Most (not all) are based on grains of truth, but are any of them actually compelling?

Let’s consider.

1.   **Humans have trouble with complex problems and memory demands**. True! But incomplete. We have every right to expect machines to do things we can’t. Cars have more stamina, calculators don’t make arithmetical errors. That’s why we invented computers: to do repetitive calculation without errors. And in many cases (including the Tower of Hanoi, which featured prominently in the paper)) we have existing systems that work perfectly without errors. AGI should be a step forward; in many cases LLMs are a step backwards. And note the bait and switch from “we’re going to build AGI that can revolutionize the world” to “give us some credit, our systems make errors and humans do, too”. The real takeaway from the Apple paper is that LLMs can’t be trusted to run algorithms as complexity and distance from the training distribution grows (just as humans shouldn’t serve as calculators). If we want to get to AGI, we will have to better.

2.   **The Large Reasoning Models (LRMs) couldn’t possibly solve the problem, because the outputs would require too many output tokens** (which is to say the correct answer would be too long for the LRMs to produce). Partial truth, and a clever observation: LRMs (which are enhanced LLMs) have a shortcoming, which is a limit on how long their outputs can be. The correct answer to Tower of Hanoi with 12 moves would be too long for some LRMs to spit out, and the authors should have addressed that. But crucially (i) this objection, clever as it is, doesn’t actually explain the overall pattern of results. The LRMs failed on Tower of Hanoi with 8 discs, where the optimal solution is 255 moves, well within so-called token limits; (ii) well-written symbolic AI systems generally don’t suffer from this problem, and AGI should not either. The length limit on LLM is a bug, and most certainly not a feature. And look, if an LLM can’t reliably execute something as basic as Hanoi, what makes you think it is going to compute military strategy (especially with the fog of war) or molecular biology (with many unknowns) correctly? What the Apple team asked for was way easier than what the real world often demands.

3.   **The paper was written by an intern**. This one, which infuriated me because is a form of ad hominem argument rather than substance, is misguided and only barely true – and utterly lacking in context. It is _true_ that the first author was an intern at Apple, Parshin Shojaee, but (i) she (not _he_ as some fool I won’t name presumed, without spending two seconds of research) also happens to be [a very promising third year Ph.D. student with many paper presentations at leading conferences](https://parshinsh.github.io/), (ii) the article, if you actually read it, makes it clear she shared lead responsibility with [Iman Mirzadeh](https://imirzadeh.me/), who has a Ph.D.; (iii) the paper actually has six authors, not one, and four have Ph.D.s; for good measure one is Yoshua Bengio’s brother [Samy Bengio](https://bengio.abracadoudou.com/), well-known and very distinguished in his own right within the machine learning community; (iv) it is a common practice in many scientific fields to put the junior author first, senior author last, as this paper did; thousands of major articles have done the same (and never been criticized for doing so — it’s a true desperation measure); (v) what really matters is the quality of the work. Alfred Sturtevant was an _undergraduate_ when he invented gene maps.

4.   **Bigger models might to do better**. True, and this is always the case (I have seen one report that o3-pro can do at least one of the problems, at least some of the time; I have not seen a thorough study yet). Bigger models sometimes do better because of genuine improvements in the model, sometimes because of problem-specific training. (From the outside we can never know which). But here’s the thing, we can’t know in advance what model is big enough (if any) for any given problem. And Apple’s result that some pretty large models could succeed at 6 discs, giving the illusion of mastery, but collapse by 8, is ominous. One is left simply having to test everything, all the time, with little guarantees of anything. Some model might be big enough for task T of size S and fail on the next size, or on Task T’ that is slightly different, etc. It all becomes a crapshoot. Not good.

5.   **The systems can solve the puzzles with code.** True in some cases, and a huge win for neurosymbolic AI, given that they can’t reliably solve the puzzles without code, and given that code is symbolic. _Huge_ vindication for what I have been saying all along: we need AI that integrates both neural networks and symbolic algorithms and representations (such as logic, code, knowledge graphs, etc). But also, we need to do so reliably, and in a general way and we haven’t yet crossed that threshold. (Importantly, the point of the Apple paper goal was to see how LRM’s unaided explore a space of solutions via reasoning and backtracking, not see how well it could use preexisting code retrieved from the web.) An analogy: A student might complain about a math exam requiring integration or differentiation by hand, even though math software can produce the correct answer instantly. The teacher’s goal in assigning the problem, though, isn’t finding the answer to that question (presumably the teacher already know the answer), but to assess the student’s conceptual understanding. Do LLM’s _conceptually_ understand Hanoi? That’s what the Apple team was getting at. (Can LLMs download the right code? Sure. But downloading code without conceptual understanding is of less help in the case of new problems, dynamically changing environments, and so on.)

6.   **The paper has only four examples, and at least one of them (Hanoi) isn’t perfect**. I doubt any of them are perfect, but the four together provide converging evidence with dozens of other prior papers (including some of my own), and I am confident many more examples will be uncovered. I already found a couple of analogous failures in algorithm application myself, which I will write about in a few days. Tal Linzen at NYU [just published yet another example](https://x.com/tallinzen/status/1933184078821360084?s=61), with “_models .. able to do the right thing for simple versions of [a language] problem (small grammars, short strings), but [with] accuracy drop[ping] very quickly as the problem becomes more complex_.” Mark my words: in time, we will see scores of papers reinforcing the Apple results.

7.   **The paper is not news; we already knew these models generalize poorly**. True! (I personally have been trying to tell people this for almost thirty years; Subbarao Rao Kambhampati has been trying his best, too). But then why do we think these models are the royal road to AGI? The real news here, aside from the fact that this was a clever study nailing down an important point, is that _people are finally starting to pay attention,_ to (one of the) two biggest Achilles’ Heels of generative AI, and to appreciate its significance. (Tune in to this newsletter on the weekend to hear about the other.) Hilarious, by the way, is hearing both “it’s wrong” and “we knew it all along”, simultaneously. In at least one case I saw a single person say both, minutes apart!

Bottom line? None of the rejoinders are compelling. If people like Sam Altman are sweating, it’s because they should. The Apple paper is yet another clear sign that scaling is not the answer; for once, people are paying attention.

§

The kicker? A Salesforce paper also just posted, that many people missed:

[![Image 1](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7dcc58c-c588-4f54-907e-7d7198090090_1251x1791.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7dcc58c-c588-4f54-907e-7d7198090090_1251x1791.jpeg)

In the “multi-turn” condition, which presumably would require reasoning and algorithmic precision, performance was only 35%.

Talk about convergence evidence. Taking the SalesForce report together with the Apple paper, it’s clear the current tech is not to be trusted.

_**Gary Marcus**, professor emeritus at NYU, and author of The Algebraic Mind and “Deep learning is hitting a wall”, both of which anticipated the correct results, is thrilled to see people finally realize that scaling is not enough to get us to AGI. Now perhaps we can begin to build better AI._

