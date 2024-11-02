---
title: Creating a LLM-as-a-Judge That Drives Business Results
date: 2024-11-02
extra:
  source: https://hamel.dev/blog/posts/llm-judge/
  original_title: Creating a LLM-as-a-Judge That Drives Business Results
---
## Summary
**摘要**

文章《创建一个作为法官的 LLM，推动业务成果》深入讲解了在业务中应用 LLM（大型语言模型）的方法和步骤。这篇指南旨在帮助解决问题：AI 团队在数据海洋中淹没，无法判断构建的 AI 系统是否真正有效。指南提出了一种称为“批判性阴影法”的解决方案，以逐步指导读者实现这一目标。

**核心要点**

### 1. 遇到的问题：AI 团队在数据海洋中淹没

AI 团队通常在数据分析部门容易迷失方向，遇到以下几个常见问题：
- **过量指标**：创建无法管理的多指标体系。
- **任意评分系统**：在不同维度使用未经校准的分数标准，评分之间的差异不可预测，主观性较强。
- **忽视领域专家**：未充分利用对领域有深入理解的专家进行反馈。
- **未验证的指标**：使用未通过实际用户或业务验证的衡量标准。

这些失误导致团队在数据和评估上无法得到清晰的答案，影响了进度和兴趣。

### 2. 寻找关键领域专家

为了确保 AI 产品的成功，需先找出一项或两名关键领袖/专家，他们能从专业的角度决定 AI 系统的技术标准，并解析用户需求。他们的指导和评价至关重要，能确保系统与用户期望保持一致。

### 3. 构建数据集

下一步是构建适用于评估 AI 输出的数据集。要确保数据集具有多样性，覆盖 AI 在生产环境中可能遇到的各种情况，真实体现用户行为，进而帮助识别 AI 的潜在弱点。

### 施行过程

1. **发现关键领域专家**：对于大部分组织而言，(key)通常存在一两位关键掌舵者，对 AI 产品的成功起着决定性作用。这些人往往是领域专家或目标用户的代表。
   
2. **创建数据集**：围绕关键领域专家的需求，构建一个能够覆盖AI在面对实际应用场景时可能遇到的多种特殊情况的数据集。

3. **执行后续步骤**：根据指南逐步执行每个部分，逐渐融合到构建 AI 系统的关键阶段。

在保持文章专业性的同时，调整了描述形式和语言表达，确保摘要符合既定的格式和严格要求。
## Full Content
Title: Creating a LLM-as-a-Judge That Drives Business Results –

URL Source: https://hamel.dev/blog/posts/llm-judge/

Markdown Content:
Table Of Contents
-----------------

*   [The Problem: AI Teams Are Drowning in Data](https://hamel.dev/blog/posts/llm-judge/#the-problem-ai-teams-are-drowning-in-data)
*   [Step 1: Find _The_ Principal Domain Expert](https://hamel.dev/blog/posts/llm-judge/#step-1-find-the-principal-domain-expert)
    *   [Next Steps](https://hamel.dev/blog/posts/llm-judge/#next-steps)
*   [Step 2: Create a Dataset](https://hamel.dev/blog/posts/llm-judge/#step-2-create-a-dataset)
    *   [Why a Diverse Dataset Matters](https://hamel.dev/blog/posts/llm-judge/#why-a-diverse-dataset-matters)
    *   [Dimensions for Structuring Your Dataset](https://hamel.dev/blog/posts/llm-judge/#dimensions-for-structuring-your-dataset)
    *   [Examples of Features, Scenarios, and Personas](https://hamel.dev/blog/posts/llm-judge/#examples-of-features-scenarios-and-personas)
    *   [This taxonomy is not universal](https://hamel.dev/blog/posts/llm-judge/#this-taxonomy-is-not-universal)
    *   [Generating Data](https://hamel.dev/blog/posts/llm-judge/#generating-data)
    *   [Example LLM Prompts for Generating User Inputs](https://hamel.dev/blog/posts/llm-judge/#example-llm-prompts-for-generating-user-inputs)
    *   [Generating Synthetic Data](https://hamel.dev/blog/posts/llm-judge/#generating-synthetic-data)
    *   [Next Steps](https://hamel.dev/blog/posts/llm-judge/#next-steps-1)
*   [Step 3: Direct The Domain Expert to Make Pass/Fail Judgments with Critiques](https://hamel.dev/blog/posts/llm-judge/#step-3-direct-the-domain-expert-to-make-passfail-judgments-with-critiques)
    *   [Why are simple pass/fail metrics important?](https://hamel.dev/blog/posts/llm-judge/#why-are-simple-passfail-metrics-important)
    *   [The Role of Critiques](https://hamel.dev/blog/posts/llm-judge/#the-role-of-critiques)
    *   [Examples of Good Critiques](https://hamel.dev/blog/posts/llm-judge/#examples-of-good-critiques)
    *   [Don’t stray from binary pass/fail judgments when starting out](https://hamel.dev/blog/posts/llm-judge/#dont-stray-from-binary-passfail-judgments-when-starting-out)
    *   [Make it easy for the domain expert to review data](https://hamel.dev/blog/posts/llm-judge/#make-it-easy-for-the-domain-expert-to-review-data)
    *   [How many examples do you need?](https://hamel.dev/blog/posts/llm-judge/#how-many-examples-do-you-need)
*   [Step 4: Fix Errors](https://hamel.dev/blog/posts/llm-judge/#step-4-fix-errors)
*   [Step 5: Build Your LLM as A Judge, Iteratively](https://hamel.dev/blog/posts/llm-judge/#step-5-build-your-llm-as-a-judge-iteratively)
    *   [The Hidden Power of Critiques](https://hamel.dev/blog/posts/llm-judge/#the-hidden-power-of-critiques)
    *   [Start with Expert Examples](https://hamel.dev/blog/posts/llm-judge/#start-with-expert-examples)
    *   [Keep Iterating on the Prompt Until Convergence With Domain Expert](https://hamel.dev/blog/posts/llm-judge/#keep-iterating-on-the-prompt-until-convergence-with-domain-expert)
    *   [How to Optimize the LLM Judge Prompt?](https://hamel.dev/blog/posts/llm-judge/#how-to-optimize-the-llm-judge-prompt)
    *   [The Human Side of the Process](https://hamel.dev/blog/posts/llm-judge/#the-human-side-of-the-process)
    *   [How Often Should You Evaluate?](https://hamel.dev/blog/posts/llm-judge/#how-often-should-you-evaluate)
    *   [What if this doesn’t work?](https://hamel.dev/blog/posts/llm-judge/#what-if-this-doesnt-work)
    *   [Mistakes I’ve noticed in LLM judge prompts](https://hamel.dev/blog/posts/llm-judge/#mistakes-ive-noticed-in-llm-judge-prompts)
*   [Step 6: Perform Error Analysis](https://hamel.dev/blog/posts/llm-judge/#step-6-perform-error-analysis)
    *   [Classify Traces](https://hamel.dev/blog/posts/llm-judge/#classify-traces)
    *   [An Interactive Walkthrough of Error Analysis](https://hamel.dev/blog/posts/llm-judge/#an-interactive-walkthrough-of-error-analysis)
    *   [Fix Your Errors, Again](https://hamel.dev/blog/posts/llm-judge/#fix-your-errors-again)
    *   [Doing this well requires data literacy](https://hamel.dev/blog/posts/llm-judge/#doing-this-well-requires-data-literacy)
*   [Step 7: Create More Specialized LLM Judges (if needed)](https://hamel.dev/blog/posts/llm-judge/#step-7-create-more-specialized-llm-judges-if-needed)
*   [Recap of Critique Shadowing](https://hamel.dev/blog/posts/llm-judge/#recap-of-critique-shadowing)
    *   [It’s Not The Judge That Created Value, Afterall](https://hamel.dev/blog/posts/llm-judge/#its-not-the-judge-that-created-value-afterall)
    *   [Do You Really Need This?](https://hamel.dev/blog/posts/llm-judge/#do-you-really-need-this)
*   [FAQ](https://hamel.dev/blog/posts/llm-judge/#faq)
    *   [If I have a good judge LLM, isn’t that also the LLM I’d also want to use?](https://hamel.dev/blog/posts/llm-judge/#if-i-have-a-good-judge-llm-isnt-that-also-the-llm-id-also-want-to-use)
    *   [Do you recommend fine-tuning judges?](https://hamel.dev/blog/posts/llm-judge/#do-you-recommend-fine-tuning-judges)
    *   [What’s wrong with off-the-shelf LLM judges?](https://hamel.dev/blog/posts/llm-judge/#whats-wrong-with-off-the-shelf-llm-judges)
    *   [How Do you evaluate the LLM judge?](https://hamel.dev/blog/posts/llm-judge/#how-do-you-evaluate-the-llm-judge)
    *   [What model do you use for the LLM judge?](https://hamel.dev/blog/posts/llm-judge/#what-model-do-you-use-for-the-llm-judge)
    *   [What about guardrails?](https://hamel.dev/blog/posts/llm-judge/#what-about-guardrails)
    *   [I’m using LLM as a judge, and getting tremendous value but I didn’t follow this approach.](https://hamel.dev/blog/posts/llm-judge/#im-using-llm-as-a-judge-and-getting-tremendous-value-but-i-didnt-follow-this-approach.)
    *   [How do you choose between traditional ML techniques, LLM-as-a-judge and human annotations?](https://hamel.dev/blog/posts/llm-judge/#how-do-you-choose-between-traditional-ml-techniques-llm-as-a-judge-and-human-annotations)
    *   [Can you make judges from small models?](https://hamel.dev/blog/posts/llm-judge/#can-you-make-judges-from-small-models)
    *   [How do you ensure consistency when updating your LLM model?](https://hamel.dev/blog/posts/llm-judge/#how-do-you-ensure-consistency-when-updating-your-llm-model)
    *   [How do you phase out human in the loop to scale this?](https://hamel.dev/blog/posts/llm-judge/#how-do-you-phase-out-human-in-the-loop-to-scale-this)
*   [Resources](https://hamel.dev/blog/posts/llm-judge/#resources)
*   [Stay Connected](https://hamel.dev/blog/posts/llm-judge/#stay-connected)

Earlier this year, I wrote [Your AI product needs evals](https://hamel.dev/blog/posts/evals/). Many of you asked, “How do I get started with LLM-as-a-judge?” This guide shares what I’ve learned after helping over [30 companies](https://parlance-labs.com/) set up their evaluation systems.

The Problem: AI Teams Are Drowning in Data
------------------------------------------

Ever spend weeks building an AI system, only to realize you have no idea if it’s actually working? You’re not alone. I’ve noticed teams repeat the same mistakes when using LLMs to evaluate AI outputs:

1.  **Too Many Metrics**: Creating numerous measurements that become unmanageable.
2.  **Arbitrary Scoring Systems**: Using uncalibrated scales (like 1-5) across multiple dimensions, where the difference between scores is unclear and subjective. What makes something a 3 versus a 4? Nobody knows, and different evaluators often interpret these scales differently.
3.  **Ignoring Domain Experts**: Not involving the people who understand the subject matter deeply.
4.  **Unvalidated Metrics**: Using measurements that don’t truly reflect what matters to the users or the business.

The result? Teams end up buried under mountains of metrics or data they don’t trust and can’t use. Progress grinds to a halt. Everyone gets frustrated.

For example, it’s not uncommon for me to see dashboards that look like this:

![Image 1](https://hamel.dev/blog/posts/llm-judge/blog_header.png)

An illustrative example of a bad eval dashboard

Tracking a bunch of scores on a 1-5 scale is often a sign of a bad eval process (I’ll discuss why later). In this post, I’ll show you how to avoid these pitfalls. The solution is to use a technique that I call **“Critique Shadowing”**. Here’s how to do it, step by step.

Step 1: Find _The_ Principal Domain Expert
------------------------------------------

In most organizations there is usually one (maybe two) key individuals whose judgment is crucial for the success of your AI product. These are the people with deep domain expertise or represent your target users. Identifying and involving this **Principal Domain Expert** early in the process is critical.

**Why is finding the right domain expert so important?**

*   **They Set the Standard**: This person not only defines what is acceptable technically, but also helps you understand if you’re building something users actually want.
    
*   **Capture Unspoken Expectations**: By involving them, you uncover their preferences and expectations, which they might not be able to fully articulate upfront. Through the evaluation process, you help them clarify what a “passable” AI interaction looks like.
    
*   **Consistency in Judgment**: People in your organization may have different opinions about the AI’s performance. Focusing on the principal expert ensures that evaluations are consistent and aligned with the most critical standards.
    
*   **Sense of Ownership**: Involving the expert gives them a stake in the AI’s development. They feel invested because they’ve had a hand in shaping it. In the end, they are more likely to approve of the AI.
    

**Examples of Principal Domain Experts:**

*   A **psychologist** for a mental health AI assistant.
*   A **lawyer** for an AI that analyzes legal documents.
*   A **customer service director** for a support chatbot.
*   A **lead teacher or curriculum developer** for an educational AI tool.

In a smaller company, this might be the CEO or founder. If you are an independent developer, you should be the domain expert (but be honest with yourself about your expertise).

If you must rely on leadership, you should regularly validate their assumptions against real user feedback.

Many developers attempt to act as the domain expert themselves, or find a convenient proxy (ex: their superior). This is a recipe for disaster. People will have varying opinions about what is acceptable, and you can’t make everyone happy. What’s important is that your principal domain expert is satisfied.

**Remember:** This doesn’t have to take a lot of the domain expert’s time. Later in this post, I’ll discuss how you can make the process efficient. Their involvement is absolutely critical to the AI’s success.

### Next Steps

Once you’ve found your expert, we need to give them the right data to review. Let’s talk about how to do that next.

Step 2: Create a Dataset
------------------------

With your principal domain expert on board, the next step is to build a dataset that captures problems that your AI will encounter. It’s important that the dataset is diverse and represents the types of interactions that your AI will have in production.

### Why a Diverse Dataset Matters

*   **Comprehensive Testing**: Ensures your AI is evaluated across a wide range of situations.
*   **Realistic Interactions**: Reflects actual user behavior for more relevant evaluations.
*   **Identifies Weaknesses**: Helps uncover areas where the AI may struggle or produce errors.

### Dimensions for Structuring Your Dataset

You want to define dimensions that make sense for your use case. For example, here are ones that I often use for B2C applications:

1.  **Features**: Specific functionalities of your AI product.
2.  **Scenarios**: Situations or problems the AI may encounter and needs to handle.
3.  **Personas**: Representative user profiles with distinct characteristics and needs.

### Examples of Features, Scenarios, and Personas

#### Features

 
|  |
| --- |

