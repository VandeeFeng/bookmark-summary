---
title: AI Founder's Bitter Lesson. Chapter 2 - No Power
date: 2025-01-16
extra:
  source: https://lukaspetersson.github.io/blog/2025/power-vertical/
  original_title: AI Founder's Bitter Lesson. Chapter 2 - No Power
---
## Summary
**摘要**：
人工智能开发者的苦涩教训：随着技术发展，普遍性更强的AI产品最终会超越高度垂直化的AI产品，并在多数领域取得主导地位。早期进入市场并不意味着能长期胜出，转向更通用技术的AI方案更具优势。AI垂直应用面临的挑战包括降低的转换成本和缺失战略优势，除非它们能够找到真正独特且不可替代的资源。文章引用内容说明即使是具有专有数据优势的AI垂直产品，也可能无法构建持久的竞争壁垒。

**要点总结**：
1. **性能提升下的度量转化**：随着AI模型性能提高，传统垂直化解决方案将逐渐被更通用的，性能提升的AI产品取代。初始速度快于对手的垂直产品，终将被更好、更全面的通用型AI解决方案超越。
   
2. **市场前景的切换成本**：AI的远程助手产品通过简化工程流程和预安装软件，实现无缝快速上手，较传统垂直产品具有显著优势。转换成本低、易用性高使其更容易在市场中获得竞争优势。
   
3. **市场份额的结构性劣势**：传统垂直化AI解决方案由于缺乏竞争策略，随着AI模型不断优化和改变，较难维持市场地位。仅解决某单一问题的垂直产品，更易被通用型产品替代，而且这类产品并未实现真正的差异化。
   
4. **“角力”资源的独特优势**：AI垂直应用中存在少量情况下，可能依赖于一项真正独特且难以替代的资源作为关键优势，这是独有的差异化因素，可以暂时提供竞争优势。
   
5. **策略转向与资源获得**：AI应用层的开发者应当将更多资源和精力用于寻找和培育那些“角力资源”，以便构建持久的竞争壁垒，抵御未来更具竞争力的通用AI产品的冲击。对此进行深入的策略研究，将是AI相关企业的重点发展方向。
## Full Content
Title: AI Founder's Bitter Lesson. Chapter 2 - No Power

URL Source: https://lukaspetersson.github.io/blog/2025/power-vertical/

Markdown Content:
_tl;dr:_

*   Horizontal AI products will eventually outperform vertical AI products in most verticals. AI verticals were first to market, but who will win in the long run?
*   Switching costs will be low. Horizontal AI will be like a remote co-worker. Onboarding will be like onboarding a new employee - giving them a computer with preinstalled software and access.
*   AI verticals will struggle to find a moat in other ways too. No advantage in any of Helmer’s 7 Powers.
*   … except for the off chance of a true cornered resource - something both absolutely exclusive AND required for the vertical. This will be rare. Most who think they have this through proprietary data misunderstand the requirements. Either it’s not truly exclusive, or not truly required.

AI history teaches us a clear pattern: solutions that try to overcome model limitations through domain knowledge eventually lose to more general approaches that leverage compute power. In [chapter 1](https://lukaspetersson.com/blog/2025/bitter-vertical/), we saw this pattern emerging again as companies build vertical products with constrained AI, rather than embracing more flexible solutions that improve with each model release. But having better performance isn’t enough to win markets. This chapter examines the adoption of vertical and horizontal products through the lens of Hamilton Helmer’s 7 Powers framework. We’ll see that products built as vertical workflows lack the strategic advantages needed to maintain their market position once horizontal alternatives become viable. However, there’s one critical exception that suggests a clear strategy for founders building in the AI application layer.

As chapter 1 showed, products that use more capable models with fewer constraints will eventually achieve better performance. Yet solutions based on current models (which use engineering effort to reduce mistakes by introducing human bias) will likely reach the market first. To be clear, this post discusses the scenario where we enter the green area of Figure 1 and whether AI verticals can maintain their market share as more performant horizontal agents become available.

 ![Image 7](https://lukaspetersson.com/assets/img/comp_easy.png)

_Figure 1, performance trajectory comparison between vertical and horizontal AI products over time, showing three distinct phases: traditional software dominance, vertical AI market entry, and horizontal AI advancement with improved models._

Of course, Figure 1 is simplistic. These curves look different depending on the difficulty of the problem. Most problems which AI has potential to solve are so hard that AI verticals will never reach acceptable performance, as illustrated in Figure 2. These problems are largely out of scope and not attempted by any startups today. So even if they make up the majority of potential AI applications, they represent a minority among today’s AI applications.

 ![Image 8](https://lukaspetersson.com/assets/img/comp_hard.png)

_Figure 2, unlike Figure 1, this shows a harder problem where vertical AI products never reach adequate performance levels, even as horizontal AI achieves superior results with improved models._

For problems simple enough to be solved by current constrained approaches (Figure 1), the question becomes: can AI verticals maintain their lead when better solutions arrive?

To paint the picture of the battlefield: Vertical AI is easy to recognize, as it is what most startups in the AI application layer build today. Chapter 1 went into details of the definitions here, but in short, they achieve more reliability by constraining the AI in predefined workflows. On the other hand, horizontal AI will be like a remote co-worker. Imagine ChatGPT, but it can take actions on a computer in the background, using traditional (non AI) software to complete tasks. Onboarding will be like onboarding a new employee - the computer would have the same pre-installed software and account access as you would give a new employee, and you would communicate instructions in natural language. There will be no need to give it all possible sources of data for the task because it can autonomously navigate and find the data it needs. Furthermore, we will assume that this horizontal AI will be built by an AI lab (OpenAI, Anthropic, etc.), as chapter 4 discusses why this is likely.

Note that I am referring to the horizontal agent in an anthropomorphic way, but it does not need to be as smart as a human to perform most of these tasks. This is not ASI. It will, however, be smart enough to write its own software when it cannot find available alternatives to interact with. I think this is realistic to expect in relatively short timelines because coding is precisely the area where we see the most progress in AI models.

Of course, there is a discussion to be had whether this will happen, and if so, when (chapter 3). But I have met a surprising number of founders who believe this will happen, and still think their AI vertical can survive this competition.

I personally lost to this competition once. When OpenAI released ChatGPT in November 2022, I wanted to use it to explain scientific papers. However, it couldn’t handle long inputs (longer inputs require more compute, which OpenAI limited to manage costs). When the GPT-3.5 API became available, I built AcademicGPT, a vertical AI product that solved this limitation by breaking the task into multiple API calls. The product got paying subscribers, but when GPT-4 launched with support for longer inputs, my engineering work became obsolete. The less biased, horizontal product suddenly produced better results than my carefully engineered solution with human bias.

I was not alone. Jared, partner at YC, noted in the Lightcone podcast: “that first wave of LLM apps mostly did get crushed by the next wave of GPTs.” Of course, these were much thinner wrappers than the vertical AI products of today. AcademicGPT only solved for one thing, input length, but the startups that create sophisticated AI vertical products solve for several things. This might extend their lifespan, but one by one, AI models will solve them out of the box, just as input length was solved when GPT-4’s context window increased. As we saw in chapter 1, as models get better, they will eventually find themselves competing with a horizontal solution that is better in every aspect.

Hamilton Helmer’s 7 Powers provides a nice framework for analyzing if they can stand this competition. This framework identifies seven lasting sources of competitive advantage: Scale Economies, Network Economies, Counter-Positioning, Switching Costs, Branding, Cornered Resource, and Process Power.

### **Switching Cost**

_Customer retention through perceived losses and barriers associated with changing providers. This makes customers more likely to stay with the current provider even if alternatives exist._

**Integration/UX**

Users might have grown used to the UI of the vertical AI product, but this is unlikely to be a barrier because of the simple nature of onboarding horizontal AI. It will be like onboarding a new employee, which you have done many times before. Or as Leopold Aschenbrenner [put it](https://situational-awareness.ai/): “The drop-in remote worker will be dramatically easier to integrate—just, well, drop them in to automate all the jobs that could be done remotely.”

Furthermore, the remote co-worker will evolve from an existing horizontal AI product which you are already used to. Most people will already be familiar with the UI of ChatGPT. As a last point, horizontal AI products will be able to greatly benefit from being able to seamlessly share context across tasks.

Dialog in natural language seems to be the best UI, as it is the one we have chosen in most of our daily interactions. However, there are some areas where a computer UI is more convenient. Of course, traditional software like Excel still exists and can be used to interact with the horizontal agent in these cases, but I am open to the possibility that there is a niche where neither traditional software nor natural language dialog is optimal. AI verticals that operate in such a niche (and innovate this UI) would find switching cost barriers. However, their moat would not be AI-related; non-AI versions (which the horizontal AI could use) would be equally valuable.

**Sales**

Sales will not be a barrier if the horizontal product evolves from a product you already have. Many companies have already gone through procurement of ChatGPT, and this is only increasing.

**Price**

The closest thing we have today to the horizontal AI product we are dealing with is Claude Computer-use, which is very expensive to run because of repeated calls to big LLM models with high resolution images. AI verticals often optimize this by limiting the input to only include what (they think) is relevant. But the cost of running models has been on a steep downward trajectory. Because of competition between the AI labs, I expect this to continue. Furthermore, having a single product for many verticals instead of licensing many will save cost.

### **Counter Positioning**

_Novel business approach that established players find difficult or impossible to replicate. This creates a unique market position that competitors cannot effectively challenge._

At first glance, vertical products might seem to have counter positioning through their ability to tailor solutions to specific customers. But this advantage only exists if it actually makes your product better than the competition, which it is not in the scenario we are examining. See chapter 1 for more details.

In fact, the situation demonstrates counter positioning advantages in the other direction. Horizontal solutions scale naturally with each model improvement, while vertical products face a dilemma: either maintain their constraints and fall behind in performance, or adopt the better models and lose their differentiation.

### **Scale Economy**

_Production costs per unit progressively reduce as business operations expand in scale. This advantage allows companies to become more cost-efficient as they grow larger._

Scale Economies are equally available to both approaches. Vertical products scale efficiently like traditional SaaS businesses. But horizontal solutions share this advantage and can push prices down faster by spreading R&D cost of model development across users from many different verticals.

### **Network Economy**

_Product or service value for each user rises with expansion of the total customer network. Each new user adds value for all existing users, creating a self-reinforcing growth cycle._

Network Economies tell a similar story to Scale Economies. Both vertical and horizontal products gather user data to improve their product. However, horizontal solutions have an inherent advantage - they can use the data to train better models, creating a broader feedback loop that improves performance across all use cases.

### **Brand Power**

_Long-lasting perception of enhanced value based on the company’s historical performance and reputation. A strong brand creates customer loyalty and allows for premium pricing._

Brand power is typically out of reach for companies at this scale. See Figure 3. It could be argued that OpenAI and/or Google has it, but no startup doing vertical AI will.

### **Process Power**

_Organizational capabilities that require significant time and effort for competitors to match. These are often complex internal systems or procedures that create operational excellence._

Similarly, process power is typically out of reach for companies at this scale. See Figure 3.

 ![Image 9](https://lukaspetersson.com/assets/img/power_stages.png)

_Figure 3, the three phases of business growth and the Powers most often found at each stage._

### **Cornered Resource**

_Special access to valuable assets under favorable conditions that create competitive advantage. This could include exclusive rights, patents, or data._

So far, no power has been able to challenge AI verticals in their competition with horizontal AI co-workers. However, a cornered resource breaks this pattern. Such a resource will be very rare. The resource has to be truly exclusive—that is, it should not be available for sale at any price. It also has to be truly required to operate in that vertical, meaning without it, your product cannot succeed regardless of other factors. There will be very few verticals that find such a resource. I think several AI verticals believe they have this advantage through some data, but in reality, they don’t. The data is either not truly required or not exclusively held. However, some will find such a resource. For example, they might have a dataset that could only be gathered during a rare event. As long as they maintain control of it, the superior intelligence of horizontal AI won’t matter.

In conclusion, in the scenario where a vertical AI product was first to market but now faces competition from a superior solution based on horizontal AI, almost all vertical AI solutions will struggle to find a barrier. By examining Helmer’s 7 powers, we see that having a cornered resource might be the only moat AI verticals can have. This suggests that AI founders in the applications layer should perhaps spend much more time trying to acquire such a resource than anything else, as we will discuss further in chapter 4. Verticals that don’t create a barrier will be overtaken by horizontal solutions once they become competitive. This happened to me with AcademicGPT. AcademicGPT solved just one problem which horizontal solutions couldn’t solve at the time, but this will be the fate for more sophisticated AI verticals that solve multiple ones. It will just take slightly longer. However, the elephant in the room is the assumption that the timeline for a remote co-worker is short. This brings us to chapter 3, where we’ll explore how the AI application layer is likely to evolve. We’ll make concrete predictions and investigate the potential obstacles to this transition - including model stagnation, regulatory challenges, trust issues, and economic barriers.

