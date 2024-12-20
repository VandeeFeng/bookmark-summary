---
title: Is AI progress slowing down-
date: 2024-12-20
extra:
  source: https://simonwillison.net/2024/Dec/19/is-ai-progress-slowing-down/
  original_title: Is AI progress slowing down-
---
## Summary
**摘要**：
文章《AI进步是否正在放缓？》深入探讨了近来关于人工智能和语言模组（LLMs）的发展停滞的问题。作者Arvind Narayanan、Sayash Kapoor和Benedikt Ströbl指出，从GPT-4发布后的两年以来，最大的进步似乎并不来自大规模的模型扩展。相反，研究者开始聚焦于"推理扩展"（inference scaling），即在进行任务时使用模型做预演，以此增加其用途，从而提升AI能力。这种方法在提高模型效率和降低成本的同时特别适用于具有明确答案的问题，如编程和数学问题。然而，作者也提出此项技术在自然语言生成等问题上难见显著效果，尤其对于训练数据的限制而言。文章指出，广泛依赖行业专家的意见存在潜在偏见，并强调在人工智能应用领域的发展仍落后于理论进步。实际使用的AI应用与现有AI能力的利用程度低下，皆因能力与可靠性的差距所限制。另外，推理模型的可靠性似乎有所增强，这是一个令人欣喜的发展。

**要点总结**：
1. **模型扩展的停滞**：在GPT-4发布后的两年里，人工智能领域的实质性进步并未出自于模型规模的扩展（“调参”），从而引发“模型扩边已失效”的讨论。
2. **推理扩展的兴起**：越来越关注于优化模型在使用时的计算成本与时间（“推理扩展”），尤其是对于具有明确答案的问题，如编程和数学问题，它似乎提供了行之有效的解决策略。
3. **不同问题类型的挑战**：推理扩展在仅适用于问题明确答案的场景（如编程和数学问题）中作用显著。然而，对于写作风格、语言翻译等需要语境理解的问题而言，进展有限，特别是如果问题来源于训练数据的不足效应。
4. **行业专家意见的局限性**：文章反差地指出，不应给行业专家的意见过高的权重，因为这些专家可能为了自身利益提供建议，并在这方面留下偏见。
5. **实际应用的滞后与潜力**：AI的应用开发未能跟上能力增强的步伐，呈现明显的“能力-可靠性缺口”，使得自动化的可能性受到限制。同时，提升可靠性的方法往往需要针对特定应用定制，而非专注于能力增强本身，表达模型能力也表现出持续进步，为人工智能领域带来了希望。
## Full Content
Title: Is AI progress slowing down?

URL Source: https://simonwillison.net/2024/Dec/19/is-ai-progress-slowing-down/

Markdown Content:
**[Is AI progress slowing down?](https://www.aisnakeoil.com/p/is-ai-progress-slowing-down)** ([via](https://bsky.app/profile/randomwalker.bsky.social/post/3ldnu2gntqs24 "@randomwalker.bsky.social")) This piece by Arvind Narayanan, Sayash Kapoor and Benedikt Ströbl is the single most insightful essay about AI and LLMs I've seen in a long time. It's long and worth reading every inch of it - it defies summarization, but I'll try anyway.

The key question they address is the widely discussed issue of whether model scaling has stopped working. Last year it seemed like the secret to ever increasing model capabilities was to keep dumping in more data and parameters and training time, but the lack of a convincing leap forward in the two years since GPT-4 - from any of the big labs - suggests that's no longer the case.

> The new dominant narrative seems to be that model scaling is dead, and “inference scaling”, also known as “test-time compute scaling” is the way forward for improving AI capabilities. The idea is to spend more and more computation when using models to perform a task, such as by having them “think” before responding.

Inference scaling is the trick introduced by OpenAI's o1 and now explored by other models such as Qwen's [QwQ](https://simonwillison.net/2024/Nov/27/qwq/). It's an increasingly practical approach as inference gets more efficient and cost per token continues to [drop through the floor](https://simonwillison.net/tags/llm-pricing/).

But how far can inference scaling take us, especially if it's only effective for certain types of problem?

> The straightforward, intuitive answer to the first question is that inference scaling is useful for problems that have clear correct answers, such as coding or mathematical problem solving. \[...\] In contrast, for tasks such as writing or language translation, it is hard to see how inference scaling can make a big difference, especially if the limitations are due to the training data. For example, if a model works poorly in translating to a low-resource language because it isn’t aware of idiomatic phrases in that language, the model can’t reason its way out of this.

There's a delightfully spicy section about why it's a bad idea to defer to the expertise of industry insiders:

> In short, the reasons why one might give more weight to insiders’ views aren’t very important. On the other hand, there’s a huge and obvious reason why we should probably give less weight to their views, which is that they have an incentive to say things that are in their commercial interests, and have a track record of doing so.

I also enjoyed this note about how we are still potentially years behind in figuring out how to build usable applications that take full advantage of the capabilities we have today:

> The furious debate about whether there is a capability slowdown is ironic, because the link between capability increases and the real-world usefulness of AI is extremely weak. The development of AI-based [applications](https://www.ben-evans.com/benedictevans/2024/4/19/looking-for-ai-use-cases) lags far behind the increase of AI capabilities, so even existing AI capabilities remain greatly underutilized. One reason is the [capability-reliability gap](https://www.aisnakeoil.com/i/147899150/reliability) --- even when a certain capability exists, it may not work reliably enough that you can take the human out of the loop and actually automate the task (imagine a food delivery app that only works 80% of the time). And the methods for improving reliability are often application-dependent and distinct from methods for improving capability. That said, reasoning models also seem to exhibit [reliability improvements](https://youtu.be/iBfQTnA2n2s?si=a-760cPz5ZghJc7w&t=161), which is exciting.

