---
title: You can’t build a moat with AI (redux)
date: 2025-02-22
extra:
  source: https://frontierai.substack.com/p/you-cant-build-a-moat-with-ai-redux
  original_title: You can’t build a moat with AI (redux)
---
## Summary
**摘要**：
文章讨论了在人工智能（AI）领域，尤其是在大型语言模型（LLM）不断发展的情况下，如何建立持久的竞争优势（护城河）。文章指出，仅仅依赖prompt工程或利用最新模型所带来的优势是短暂的，因为这些优势很容易被模仿。文章强调，真正的差异化在于如何利用数据以及如何优化用户体验和工作流程集成。文章认为，AI 应该被视为一种通用工具，就像木匠的锤子一样，重点应该放在如何有效地满足用户需求，并且利用数据来优化产品，例如通过分析用户行为来改进功能和识别bug。此外，深度集成到用户的工作流程中，例如与他们使用的各种工具集成，可以提高产品的粘性。因此，企业应该专注于提供无缝的用户体验和将AI集成到实际的工作流程中，通过深入理解用户需求并利用数据来实现产品的差异化，而不是仅仅依赖于AI本身。

**要点总结**：

1.  **用户体验至关重要**：AI应用不应仅仅是原有应用上添加AI功能，而应该重新思考用户体验，通过AI实现自动化，简化用户操作，将繁琐的工作自动化，提供无缝的体验。持续创新用户体验的团队能够不断保持竞争优势。

2.  **集成和工作流程是关键**：AI应用需要深度集成到企业用户的工作流程中，与他们常用的消息传递工具、文档系统、任务跟踪器等集成，成为他们工作中不可或缺的一部分，从而提高产品的粘性。深度集成能使用户更难切换到竞争对手的产品，因为替换产品需要重新集成所有工作流程。

3.  **数据驱动产品优化**：收集和利用用户数据（包括输入和输出数据）对于理解用户需求、优化产品至关重要。例如，通过分析用户提问的数据，可以了解用户对哪些功能感兴趣，哪些问题回答得不够好，从而改进产品。有效的数据利用是建立长期竞争优势的关键。

4.  **AI是通用工具，重点在于如何使用**：AI已成为一种标准工具，就像木匠的锤子一样，每个应用都应该以某种形式使用AI。差异化不在于是否使用AI，而在于如何有效地理解用户需求，并利用AI来满足这些需求。企业应该关注如何利用AI来解决实际问题，而不是仅仅吹嘘自己使用了AI技术。

## Full Content
Title: You can’t build a moat with AI (redux)

URL Source: https://frontierai.substack.com/p/you-cant-build-a-moat-with-ai-redux

Published Time: 2025-02-20T18:40:39+00:00

Markdown Content:
Last spring, we wrote an article called _[You can’t build a moat with AI](https://frontierai.substack.com/p/you-cant-build-a-moat-with-ai)_. That post argued that prompt engineering, while important, would be difficult to defend over time given how easy it is to experiment with LLMs. As a result, you have to focus on the quality of data your application has access to and your use of that data to differentiate yourself.

Everything we said in that post has held true, but the release of models like DeepSeek R1 and o3-mini have brought the concerns about AI applications’ moats back to the forefront. In the last few weeks, we’ve heard many forms of the question, “If LLMs keep getting cheaper and better, won’t everyone’s application get better? If so, how do you differentiate?” It’s worth it for every application builder to think through this in the more detail.

In short, unless you’re building or hosting foundation models, saying that AI is a differentiating factor is sort of like saying that your choice of database is what differentiated your SaaS product: No one cares.

[![Image 1](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9e64e92-3d60-4b43-bb64-ddf89f442ef5_1792x1024.webp)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9e64e92-3d60-4b43-bb64-ddf89f442ef5_1792x1024.webp)

Source: DALL-E 3.

As a baseline assumption, better models are a rising tide that lifts all boats. It’s generally a good thing for AI applications [when more powerful models come out](https://frontierai.substack.com/p/deepseek-o3-and-ai-applications) because it gives you a more powerful engine to build on, but this isn’t the basis on which you’re going to build a moat. In the immediate frenzy after a new model is released, one team or another might figure out a better way to use that model, but that advantage is going to evaporate extremely quickly. There’s far too much useful content out on the internet for those advantages to last. This is basically the same as the prompt engineering moat we discussed above. In other words, if you’re relying on that as your differentiation, you’re going to get quickly steamrolled by the competition.

Of course, the existence of a good tool isn’t sufficient — how you use the tool matters just as much. Again, you can’t credibly claim that your application is “smarter” than the competition’s, so you’re going to have to look elsewhere for your differentiation. We’ll refer you back to last year’s post for a walkthrough of how you can build a technical moat, but in light of recent model advancements, we’re thinking about this from a product and market perspective.

We think defensibility comes down to three things.

**User experience.** Sprinkling AI on your application for the sake having AI is something that we’ve railed against many times, so we’ll spare you the sanctimony. As we’ve talked about a couple times recently, we believe that most user experiences should be rethought for AI applications. There are many scenarios in which we’ve had to rely on user input previously that we can now infer. In many ways, the whole point of AI applications is that it should feel like magic because something that you previously had to do by hand is now fully automated with believable intelligence. If you’re thinking about taking traditional forms of UX and adding AI to them, that’s an okay starting point but not a defensible moat. On the other hand, if you’re thinking about how you can meet the user where they are, integrate into their workflow, and get tedious busy work out of their hair seamlessly, you’ll find a way to change the UX. Good UX, of course can be copied, but the teams that are capable of innovating once will do it again (see: Snap). In the context of enterprise products, [the focus should be on delivering useful work](https://frontierai.substack.com/p/the-rise-of-ai-work).

**Integration and workflows.** We’re in the business of selling enterprise products, and many of you probably are too. We like to joke that every enterprise company either becomes a database company or an integrations company, and it’s clear that most AI applications companies are going to be integrations-heavy. In the previous paragraph, we touched on the importance of delivering work and snapping into the user’s works — that means that you’ll need to integrate with the customer’s messaging tool, document system, task tracker, and so on. This might sound tedious (and it can be!), but it’s also critical. Products that are able to integrate deeply into a customer’s workflow are incredibly sticky. You’re providing them so much value that they want you to be a part of everything they do — if they’re ever considering replacing you with something else, that product will have to be at least as valuable and justify the cost of re-integrating with everything you work with.

**Data in, data out.** Everything in AI always comes back to data. We talked about the use of data extensively in our previous post. To summarize briefly, simply having data is not enough. The hard part is using the right data at the right time (hint: vector search is not enough). From a business perspective, data _out_ is just as important as data in. At RunLLM, we’re now answering over 100K questions per-month. We can use that data to help our customers in many ways: understanding what features their customers are using, tracking the popularity of different workloads, identifying bugs, and so on. With some labeling, we can also use that content to help ourselves understand what kinds of questions we could do a better job of answering. Not every application is going to do all of those things on day one, but gathering the data over time builds an asset that you will benefit from tremendously in the long run. How you gather that data and how you use it over time will make a huge difference.

Ultimately, our opinion is that AI is no longer an interesting thing to talk about in terms of differentiation. At best, it’s a diminishing advantage, and its worst, it means you’re not planning for the future. Every application should probably be using AI in some form or the other, and the question is how effectively you understand your user’s needs and how effectively you’re able to shape your application to meet those needs. AI has so quickly become mainstream that it should now be considered a standard tool — a carpenter doesn’t brag about their hammer, and you shouldn’t brag about your use of GPT.

#### Discussion about this post

