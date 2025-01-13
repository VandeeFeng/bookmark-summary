---
title: AI founders will learn The Bitter Lesson
date: 2025-01-13
extra:
  source: https://lukaspetersson.github.io/blog/2025/bitter-vertical/
  original_title: AI founders will learn The Bitter Lesson
---
## Summary
**摘要**：
本文为AI领域的探讨，特别关注于初创企业、AI研究者在过去多次重复的错误以及AI创始人们需要学习的历史教训。AI在历史上的发展证明了，通用性方法最终总是胜出，并有显著的优势。在AI应用领域的创始人现在正在重复过去AI研究者犯过的相似错误。随着更好的AI模型的出现，预计将启用通用目的的AI应用程序，同时，围绕AI模型的软件的增加价值将逐渐减少。

文中引用了Richard Sutton于2019年发表的《The Bitter Lesson》一文，强调了“通用方法”是长期最有效的一种方法，并通过大量历史案例支持这一观点，包括语言识别、计算机围棋以及计算机视觉等。现在AI模型虽然有了进步，但仍无法在很多领域建立出规模化的高绩效AI产品，仍然存在许多限制。更好、更强大的AI模型将在未来直接解决这个问题，使未来AI产品不会过分依赖于由人类构建的复杂的软件架构，而是更多地依赖于更强大的计算和通用的模型。

**要点总结**：
1. **AI发展历史**：AI研究历史上，常常依赖领域知识来构建系统，但最终计算能力的提升或更通用的方法总是能胜出。
2. **AI初创企业发展困境**：AI应用领域初创企业在产品设计上重复了过去的错误，深入挖掘需要的领域知识和构建严格的约束条件，忽视了更灵活、基于广泛计算能力的方法。
3. **产品性能与市场采纳**：AI产品的“更好”在于其不仅在性能上，也在市场上能够更好地采纳和推广，更好的性能意味着能够解决更复杂的实际问题。
4. **模型与产品性能**：随着AI模型性能的提升，构建软件包装用于解决特定问题的工程努力将逐渐失去价值，更多需要的是部署更强大的、通用的AI模型。
5. **解决方案的集中点**：**通用方法**是AI发展的未来趋势，在效率操作自主性和具体性的平衡中，更通用的解决方案往往能在长期发展中取得更好的性能。
## Full Content
Title: Chapter 1/4, AI founders will learn The Bitter Lesson

URL Source: https://lukaspetersson.github.io/blog/2025/bitter-vertical/

Markdown Content:
_tl;dr:_

*   Historically, general approaches always win in AI.
*   Founders in AI application space now repeat the mistakes AI researchers made in the past.
*   Better AI models will enable general purpose AI applications. At the same time, the added value of the software around the AI model will diminish.

Recent AI progress has enabled new `products` that solve a broad range of `problems`. I saw this firsthand watching over 100 pitches during YC alumni Demo Day. These problems share a common thread - they’re simple enough to be solved with `constrained` AI. Yet the real power of AI lies in its `flexibility`. While `products` with fewer constraints generally work better, current AI `models` aren’t reliable enough to build such products at scale. We’ve been here before with AI, many times. Each time, the winning move has been the same. AI founders need to learn this history, or I fear they’ll discover these lessons the hard way.

In 2019, Richard Sutton started his famous essay “The Bitter Lesson” with:

“The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin”.

He points out that throughout AI’s history, researchers have repeatedly tried to improve systems by building in human domain knowledge. The “bitter” part of the title comes from what happens next: systems that simply use more computing power end up outperforming these carefully crafted solutions. We’ve seen this pattern in speech recognition, computer chess, and computer vision. If Sutton wrote his essay today, he’d likely add generative AI to that list. And he warns us: this pattern isn’t finished playing out.

“As a field, we still have not thoroughly learned it, as we are continuing to make the same kind of mistakes (…). We have to learn the bitter lesson that building in how we think we think does not work in the long run. The bitter lesson is based on the historical observations that 1) AI researchers have often tried to build knowledge into their agents, 2) this always helps in the short term, and is personally satisfying to the researcher, but 3) in the long run it plateaus and even inhibits further progress, and 4) breakthrough progress eventually arrives by an opposing approach based on scaling computation”

From an AI research perspective, the Bitter Lesson deals with clear definitions of “better.” In computer chess, it’s your win rate; in speech recognition, it’s word accuracy. But this post looks at AI `products` in the application layer (see Figure 1), where “better” means both `performance` and `adoption` in the market. We’ll cover adoption in Chapter 2. For now, let’s focus on product performance - the amount of economically valuable work a product can replace. Better performance means handling more complex problems, which unlocks more value.

![Image 11: stack](https://lukaspetersson.com/assets/img/stack.png)

_Figure 1, illustration of different types of AI products. In this post, we talk about the application layer._

AI `products` are typically an AI `model` wrapped in some `packaging software`. You can improve their performance in two ways:

1.  Through engineering effort: using domain knowledge to build constraints into the packaging software
2.  Through better models: waiting for AI labs to release more capable models

You can pursue both paths, but here’s the crucial insight: as models improve, the value of engineering effort diminishes. Right now, there are huge gains to be made in building better packaging software, but only because current models make many mistakes. As models become more reliable, this will change. Eventually, you’ll just need to connect a model to a computer to solve most problems - no complex engineering required.

![Image 12: perf-vs-effort](https://lukaspetersson.com/assets/img/perf-vs-effort.png)

_Figure 2, illustration of the diminishing returns of engineering effort when building AI products in the application layer. The value diminishes both as more engineering effort is made and as better models are released._

The graph above shows how engineering effort becomes less valuable as models improve. Current models have significant limitations, which means companies can still gain a lot from engineering work. I saw this at YC alumni Demo Day, where companies were finding success. The landscape splits into two groups: those with products in production at scale (solving simple problems) - a small group for now - and those targeting slightly more complex problems. This second group is doing well because their proof-of-concepts suggest their goals are achievable with enough engineering effort.

But here’s the key question these companies face: will the next model release make all that engineering work obsolete, destroying their competitive advantage? The launch of OpenAI’s o1 model illustrates this risk. I spoke with many founders in the AI application layer who were worried because they’d invested heavily in perfecting prompts to boost performance. But with o1, prompt engineering matters less. As Figure 2 shows, o1 is smarter, but this means there’s less value in the engineering work these companies did.

At its core, this engineering effort aims to constrain AI and reduce its mistakes. From observing many solutions, I’ve identified two main types of constraints:

*   `Specificity`: This represents how focused a solution is. A `vertical` solution has packaging software built for one specific problem. A `horizontal` product, in contrast, can handle many different types of problems.
*   `Autonomy`: This measures how independently the AI can operate. Following Anthropic’s terminology, we have `workflows` - systems where LLMs and tools follow predefined code paths - and `agents` - systems where LLMs control their own processes and tool usage, deciding how to complete tasks.

These two types of constraints create a framework for categorizing AI products:

|   | **Vertical** | **Horizontal** |
| --- | --- | --- |
| **Workflow** | Harvey | ChatGPT |
| **Agent** | Devin | Claude computer-use |

_Table 1: Classification of famous AI products. Note that ChatGPT likely follows a predefined code path for each message, making it a workflow rather than an agent._

Let’s explore how each category might be implemented for the same task: a business analyst creating investment pitch slides. Here’s one possible approach for each:

*   `Vertical` `workflow`: A fixed sequence of steps: First, makes a RAG query on a company database, passes this to a small LLM for summarization, then to a more capable LLM that extracts key numbers and uses a calculator tool. The LLM checks if these numbers make sense before writing slide content. Finally, a slide generator creates the presentation. This exact sequence runs every time.
*   `Vertical` `agent`: An LLM runs in a loop, using its output from one iteration as input for the next. It has access to the same tools as the workflow version but decides for itself when to use them. The loop continues until the agent determines the results meet its quality threshold.
*   `Horizontal` `workflow`: ChatGPT and similar tools could assist with parts of the task, but can’t complete it end-to-end. They lack both the specialization and autonomy needed for the full job.
*   `Horizontal` `agent`: Claude computer-use gets access to standard company software. The analyst provides instructions in natural language, and the agent operates the computer like a human would, adapting its approach as needed.

Almost all products at Demo Day fell into the vertical workflow category. This makes sense - current models aren’t reliable enough for other approaches. As a result, even problems too complex for vertical workflows are being forced into this mold since it’s the only way to get close to acceptable performance with current model capabilities. While engineering can improve these solutions, there’s an upper limit to what it can achieve. For problems that are out of reach with current models, the better strategy would be to wait for more capable models that can handle them with minimal engineering. As Leopold Aschenbrenner argues in “Situational Awareness,” for many problems, the engineering work will take longer than the wait for better models:

“It seems plausible that the schlep will take longer than the unhobbling, that is, by the time the drop-in remote worker is able to automate a large number of jobs, intermediate models won’t yet have been fully harnessed and integrated”

This pattern should sound familiar. Let’s return to the Bitter Lesson. AI researchers repeatedly tried to engineer their way to “acceptable performance,” only to be overtaken by more general solutions that simply used more compute. The parallel to how today’s AI products are built is striking. And we can make this connection even clearer by examining how the Bitter Lesson applies to our two types of constraints:

| Bitter Lesson Observation | Autonomy | Specificity |
| --- | --- | --- |
| 1) AI researchers have often tried to build knowledge into their agents | The developer experiments with an autonomous agent but finds it unreliable. Instead, they hardcode the execution steps to follow the workflow that they would go through themselves when solving the task. | The developer starts building a general document analysis system but finds it unreliable. Instead, they constrain it to just analyze financial statements, hardcoding specific metrics and validation rules. |
| 2) This always helps in the short term and is personally satisfying to the researcher | The developer finds that this increases reliability. | The developer finds that specialization improves accuracy since the model only needs to handle a narrow set of documents and metrics. |
| 3) In the long run, it plateaus and even inhibits further progress | The constrained workflow sometimes does not give the correct output when faced with novel situations that weren’t considered in the hardcoded steps. | The specialized system can’t handle related tasks like analyzing merger documents or earnings calls, requiring separate specialized systems for each type of analysis. |
| 4) Breakthrough progress eventually arrives by an opposing approach based on scaling computation | New model releases enable reliable agents that can figure out the right approach dynamically, backtracking and correcting mistakes as needed. | New model releases can understand any business document holistically, extracting relevant information regardless of format or type, making specialized systems unnecessary. |

For problems with unclear solution paths, products with more autonomy will achieve better performance. Similarly, when dealing with large, complex input spaces, less specific products will perform better.

This is the first in a four-part series examining the role of startups in AI. We’ve observed a historical pattern: AI models that leverage domain knowledge consistently get overtaken by those that leverage compute. Today’s AI products show striking parallels to this pattern.

Though I’ve tried to focus on observations rather than opinions in this first part, my view likely shows through. Building software to compensate for current model limitations seems like fighting a losing battle, especially given how rapidly models are advancing. As Jarred, partner at YC, noted in the Lightcone podcast: “that first wave of LLM apps \[vertical workflows\] mostly did get crushed by the next wave of GPTs.”

Sam Altman has repeatedly advocated for building startups that make you excited for releases of better models, rather than scared of them. Many of the founders in the AI application layer I speak to are excited about model releases, but for the sake of their startup, I don’t think they should be. They might be missing the insight from Figure 2; better models might actually reduce your edge, not enhance it. Of course, this is from the point of view of product performance - building something that can solve harder problems more effectively. In the next part, we’ll explore a different dimension: market adoption. After all, having better performance doesn’t guarantee winning the market.

### **Appendix A: Statistical View of The Bitter Lesson**

There’s another way to understand the Bitter Lesson using basic statistics. When building models, you typically face a tradeoff. You can either make a model that’s very precise in how it approaches problems (high bias) or one that’s more flexible but less predictable (high variance). The Bitter Lesson suggests choosing the flexible approach.

Why? Because with more compute power and data, you can make flexible models more reliable. It’s like having more practice shots in basketball - eventually, you’ll become consistent even with a less rigid shooting form. The reverse isn’t true - a overly rigid approach will always be limited by its built-in assumptions.

This maps directly to our discussion of AI products. Vertical workflows and specific constraints are like adding rigid rules - they make the AI more reliable now but limit how good it can eventually become. In contrast, letting AI operate more freely might seem risky today, but it allows the AI to find better solutions as models improve. As we’ve seen throughout this essay, betting against flexibility has historically been a losing strategy.

### **Appendix B: End-to-end vs Feature Engineering**

![Image 13: e2e](https://lukaspetersson.com/assets/img/e2e.png)

_Figure 1: Comparison of traditional machine learning, which requires manual feature engineering, with deep learning’s end-to-end approach. The traditional approach needs humans to define what’s important in the data, while deep learning figures this out by itself._

Traditional machine learning requires humans to decide what’s important in the data. You take raw input, like an image, and manually extract meaningful patterns or “features” - like counting specific shapes or measuring certain properties. Deep learning, in contrast, learns these patterns automatically.

![Image 14: car-features](https://lukaspetersson.com/assets/img/car-features.png)

_Figure 2: Self-driving car visualization showing feature extraction in action. The system identifies and tracks specific objects like cars, pedestrians, and lane markings. This represents the traditional approach of breaking down a complex problem into smaller, defined pieces._

Let’s use self-driving cars as an example. You could build it two ways:

1.  Feature engineering: Break down what the car sees into specific pieces - where are the other cars, where are the lanes, how fast is that pedestrian moving?
2.  End-to-end: Feed raw video directly into a neural network and let it figure out how to drive.

The feature engineering approach feels safer and more controlled. That’s why it dominated early AI. But as George Hotz observed: “if anything about the history of AI has taught us anything, it’s that feature engineering approaches will always be replaced and loose to end-to-end.”

![Image 15: sholto](https://lukaspetersson.com/assets/img/sholto.png)

_Figure 3: Tweet from Sholto Douglas_

This connects directly to our discussion of AI products. Building vertical-specific tools is like feature engineering - you’re deciding what information matters ahead of time. When you constrain a model’s autonomy, you’re doing the same thing. While this might work better today, history suggests betting on end-to-end approaches will win in the long run.

“if anything about the history of AI has taught us anything, it’s that feature engineering approaches will always be replaced and lose to end-to-end.” - [George Hotz](https://www.youtube.com/watch?v=pGF2xK_Hntw&t=372s)

Follow me on [X](https://x.com/lukaspet) or subscribe via [RSS](https://lukaspetersson.com/feed.xml) to stay updated.

