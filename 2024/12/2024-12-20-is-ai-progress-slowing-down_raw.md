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
