---
title: The Illustrated DeepSeek-R1
date: 2025-01-28
extra:
  source: https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1
  original_title: The Illustrated DeepSeek-R1
---
## Summary
**摘要**：
本文详细阐述了DeepSeek-R1这一最新人工智能进步里程碑的构建过程，对于机器学习研发社区而言，其创新点在于模型是开放权重、包含小型精简版本，并共享了一种用于复现OpenAI O1推理模型的训练方法。文中详细分解了该模型的构建流程，从大型语言模型的基础训练、到受指导语言调整和偏好调整阶段，强调了R1遵循的复杂方法论。文中阐述了R1创建过程中三个特别的亮点，包括合成生成大量数据以弥补数据规模差距的策略，以及利用行为奖励模型优化非推理应用的策略。文章还描述了R1的架构，包括其作为Transformer解码器堆栈的构成、维度和关键参数。总之，文章对DeepSeek-R1的创新之处、构建流程、关键步骤及其应用提供了一幅完整的画面，为读者理解这一AI技术的前沿发展提供了宝贵的视角。

**要点总结**：
1. **模型开放与版本化**：DeepSeek-R1作为开放权重模型，包括小型精简版本，使得研究人员更容易理解和改进AI模型的基础架构。
2. **方法论创新**：文中分享了一种用于复现OpenAI O1推理模型的训练方法，展示了AI研究在快速迭代和共享知识方面的进展。
3. **数据合成**：通过生成极其有价值的数据集来弥补大型模型训练时数据规模的差距，展示了数据在模型训练中的关键作用。
4. **强化学习的精细化**：深入分析如何利用行为奖励模型优化模型在非推理应用中的性能，展示了在特定领域利用强化学习技术的可能性。
5. **模型架构解析**：对模型采用的61个密集群Transformer解码堆栈和其与其他模型之间的相似性进行了详细介绍，涉及维度、参数等关键组件，突出了其构建的技术细节和效率优化策略。
## Full Content
Title: The Illustrated DeepSeek-R1

URL Source: https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1

Published Time: 2025-01-27T20:15:46+00:00

Markdown Content:
_\[Draft post, updates to come, please let me know if you have any suggestions or feedback here or on [Bluesky](https://bsky.app/profile/jayalammar.bsky.social) or [X/Twitter](https://x.com/JayAlammar)\]_

[![Image 75](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98138856-a4de-45e3-ad08-1434378127c2_1130x408.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98138856-a4de-45e3-ad08-1434378127c2_1130x408.png)

DeepSeek-R1 is the latest resounding beat in the steady drumroll of AI progress. For the ML R&D community, it is a major release for reasons including:

1.  It is an open weights model with smaller, distilled versions and
    
2.  It shares and reflects upon a training method to reproduce a reasoning model like OpenAI O1.
    

In this post, we’ll see how it was built.

Contents:

*   Recap: How LLMs are trained
    
*   DeepSeek-R1 Training Recipe
    
*   1- Long chains of reasoning SFT Data
    
*   2- An interim high-quality reasoning LLM (but worse at non-reasoning tasks).
    
*   3- Creating reasoning models with large-scale reinforcement learning (RL)
    
    *   3.1- Large-Scale Reasoning-Oriented Reinforcement Learning (R1-Zero)
        
    *   3.2- Creating SFT reasoning data with the interim reasoning model
        
    *   3.3- General RL training phase
        
*   Architecture
    

Most of the foundational knowledge you need to understand how such a model works is available in our book, [Hands-On Large Language Models](https://github.com/handsOnLLM/Hands-On-Large-Language-Models).

Just like most existing LLMs, DeepSeek-R1 generates one token at a time, except it excels at solving math and reasoning problems because it is able to spend more time processing a problem through the process of generating thinking tokens that explain its chain of thought.

[![Image 76](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5280089e-8989-45d7-8194-93396b25557d_613x152.gif)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5280089e-8989-45d7-8194-93396b25557d_613x152.gif)

The following figure, from Chapter 12 of our book shows the general recipe of creating a high-quality LLM over three steps:

[![Image 77](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa354473-6ae0-4ae7-a20c-e858c804d6c4_1600x477.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa354473-6ae0-4ae7-a20c-e858c804d6c4_1600x477.png)

1) The language modeling step where we train the model to predict the next word using a massive amount of web data. This step results in a base model.

2) a supervised fine-tuning step that makes the model more useful in following instructions and answering questions. This step results in an instruction tuned model or a supervised fine -tuning / SFT model.

3) and finally a preference tuning step which further polishes its behaviors and aligns to human preferences, resulting in the final preference-tuned LLM which you interact with on playgrounds and apps.

DeepSeek-R1 follows this general recipe. The details of that first step come from a [previous paper for the DeepSeek-V3 model](https://arxiv.org/pdf/2412.19437v1). R1 uses the _base_ model (not the final DeepSeek-v3 model) from that previous paper, and still goes through an SFT and preference tuning steps, but the details of how it does them are what's different.

[![Image 78](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc66dff5b-8332-4696-b484-b2ddb029b78c_854x234.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc66dff5b-8332-4696-b484-b2ddb029b78c_854x234.png)

There are three special things to highlight in the R1 creation process.

[![Image 79](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26136780-897d-4f64-b1e5-45936b6078dd_854x434.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26136780-897d-4f64-b1e5-45936b6078dd_854x434.png)

This is a large number of long chain-of-thought reasoning examples (600,000 of them). These are very hard to come by and very expensive to label with humans at this scale. Which is why the process to create them is the second special thing to highlight

This data is created by a precursor to R1, an unnamed sibling which specializes in reasoning. This sibling is inspired by a third model called _R1-Zero_ (that we’ll discuss shortly). It is significant not because it’s a great LLM to use, but because creating it required so little labeled data alongside large-scale reinforcement learning resulting in a model that excels at solving reasoning problems.

The outputs of this unnamed specialist reasoning model can then be used to train a more general model that can also do other, non-reasoning tasks, to the level users expect from an LLM.

[![Image 80](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4caea6a5-52a1-4651-8c71-4586c0637f3e_924x427.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4caea6a5-52a1-4651-8c71-4586c0637f3e_924x427.png)

This happens in two steps:

[![Image 81](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45ca8c84-6eb6-4879-ab53-035174b17ce1_1620x700.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45ca8c84-6eb6-4879-ab53-035174b17ce1_1620x700.png)

Here, RL is used to create the interim reasoning model. The model is then used to generate the SFT reasoning examples. But what makes creating this model possible is an earlier experiment creating an earlier model called _DeepSeek-R1-Zero_.

[![Image 82](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69b9f117-caa3-42fd-a949-dc6433990d26_1526x506.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69b9f117-caa3-42fd-a949-dc6433990d26_1526x506.png)

R1-Zero is special because it is able to excel at reasoning tasks without having a labeled SFT training set. Its training goes directly from a pre-trained base model through a RL training process (no SFT step). It does this so well that it’s competitive with o1.

[![Image 83](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b5c964f-b654-49b2-ab5a-5618b256ef99_1588x418.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b5c964f-b654-49b2-ab5a-5618b256ef99_1588x418.png)

This is significant because data has always been the fuel for ML model capability. How can this model depart from that history? This points to two things:

1- Modern base models have crossed a certain threshold of quality and capability (this base model was trained on 14.8 trillion high-quality tokens).

2- Reasoning problems, in contrast to general chat or writing requests, can be automatically verified or labeled. Let’s show this with an example. This can be a prompt/question that is a part of this RL training step:

> Write python code that takes a list of numbers, returns them in a sorted order, but also adds 42 at the start.

A question like this lends itself to many ways of automatic verification. Say we present this this to the model being trained, and it generates a completion:

*   A software linter can check if the completion is proper python code or not
    
*   We can execute the python code to see if it even runs
    
*   Other modern coding LLMs can create unit tests to verify the desired behavior (without being reasoning experts themselves).
    
*   We can go even one step further and measure execution time and make the training process prefer more performant solutions over other solutions — even if they’re correct python programs that solve the issue.
    

We can present a question like this to the model in a training step, and generate multiple possible solutions.

[![Image 84](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8edd9db2-a071-4bba-9d14-bbdb076d6355_798x444.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8edd9db2-a071-4bba-9d14-bbdb076d6355_798x444.png)

We can automatically check (with no human intervention) and see that the first completion is not even code. The second one is indeed python code but does not solve the problem. The third is a possible solution, but fails the unit tests, and the forth is a correct solution.

[![Image 85](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f9645a0-b1fb-4753-942c-583504297c25_972x517.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f9645a0-b1fb-4753-942c-583504297c25_972x517.png)

These are all signals that can be directly use to improve the model. This is of course done over many examples (in mini-batches) and over successive training steps.

[![Image 86](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b595e04-bd57-4f78-8c9b-ab37797e9b66_955x543.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5b595e04-bd57-4f78-8c9b-ab37797e9b66_955x543.png)

These reward signals and model updates are how the model continues improving on tasks over the RL training process as seen in Figure 2 from the paper.

[![Image 87](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe48af6fa-8956-44b0-84cf-915e607f3b5e_1546x884.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe48af6fa-8956-44b0-84cf-915e607f3b5e_1546x884.png)

Corresponding with the improvement of this capability is the length of the generated response, where the model generates more thinking tokens to process the problem.

[![Image 88](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd2b7d78-62ac-408c-8bd7-e14053bb8a46_1518x912.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd2b7d78-62ac-408c-8bd7-e14053bb8a46_1518x912.png)

This process is useful, but the R1-Zero model, despite scoring high on these reasoning problems, confronts other issues that make it less usable than desired.

> Although DeepSeek-R1-Zero exhibits strong reasoning capabilities and autonomously develops unexpected and powerful reasoning behaviors, it faces several issues. For instance, DeepSeek-R1-Zero struggles with challenges like poor readability, and language mixing.

R1 is meant to be a more usable model. So instead of relying completely on the RL process, it is used in two places as we’ve mentioned earlier in this section:

1- creating an interim reasoning model to generate SFT data points

2- Training the R1 model to improve on reasoning and non-reasoning problems (using other types of verifiers)

[![Image 89](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45ca8c84-6eb6-4879-ab53-035174b17ce1_1620x700.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45ca8c84-6eb6-4879-ab53-035174b17ce1_1620x700.png)

To make the interim reasoning model more useful, it goes through an supervised fine-tuning (SFT) training step on a few thousand examples of reasoning problems (some of which are generated and filtered from R1-Zero). The paper refers to this as cold start data”

> **2.3.1. Cold Start**  
> Unlike DeepSeek-R1-Zero, to prevent the early unstable cold start phase of RL training from the base model, for DeepSeek-R1 we construct and collect a small amount of long CoT data to fine-tune the model as the initial RL actor. To collect such data, we have explored several approaches: using few-shot prompting with a long CoT as an example, directly prompting models to generate detailed answers with reflection and verification, gathering DeepSeek-R1- Zero outputs in a readable format, and refining the results through post-processing by human annotators.

[![Image 90](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a89a9a0-c08f-430d-b135-7f012c2810ba_1824x586.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a89a9a0-c08f-430d-b135-7f012c2810ba_1824x586.png)

But wait, if we have this data, then why are we relying on the RL process? It’s because of the scale of the data. This dataset might be 5,000 examples (which is possible to source), but to train R1, 600,000 examples were needed. This interim model bridges that gap and allows to synthetically generate that extremely valuable data.

[![Image 91](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F857e61c8-03e7-4bc7-bcbe-ca182f60a70e_3300x1170.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F857e61c8-03e7-4bc7-bcbe-ca182f60a70e_3300x1170.png)

If you’re new to the concept of Supervised Fine-Tuning (SFT), that is the process that presents the model with training examples in the form of prompt and correct completion. This figure from chapter 12 shows a couple of SFT training examples:

[![Image 92](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b630dbc-aaa4-4c27-804b-542055b0f298_2264x1324.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b630dbc-aaa4-4c27-804b-542055b0f298_2264x1324.png)

This enables R1 to excel at reasoning as well as other non-reasoning tasks. The process is similar to the the RL process we’ve seen before. But since it extends to non-reasoning applications, it utilizes a helpfulnes and a safety reward model (not unlike the Llama models) for prompts that belong to these applications.

[![Image 93](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e5f9acf-b4ca-4ec4-9731-4845c8fc5515_902x394.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e5f9acf-b4ca-4ec4-9731-4845c8fc5515_902x394.png)

Just like previous models from the dawn of [GPT2](https://jalammar.github.io/illustrated-gpt2/) and [GPT 3](https://jalammar.github.io/how-gpt3-works-visualizations-animations/), DeepSeek-R1 is a stack of [Transformer](https://jalammar.github.io/illustrated-transformer/) decoder blocks. It’s made up 61 of them. The first three are dense, but the rest are mixture-of-experts layers (See my co-author Maarten’s incredible intro guide here: [A Visual Guide to Mixture of Experts (MoE)](https://substack.com/home/post/p-148217245)).

[![Image 94](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F199f326e-9a8d-4a95-8574-4778d5b7657b_538x413.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F199f326e-9a8d-4a95-8574-4778d5b7657b_538x413.png)

In terms of model dimension size and other hyperparameters, they look like this:

[![Image 95](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ee664ae-a544-4e19-a145-0ae87acc43fa_916x481.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ee664ae-a544-4e19-a145-0ae87acc43fa_916x481.png)

More details about the model architecture are presented in their two earlier papers:

*   [DeepSeek-V3 Technical Report](https://arxiv.org/pdf/2412.19437v1)
    
*   [DeepSeekMoE: Towards Ultimate Expert Specialization in](https://arxiv.org/pdf/2401.06066)
    
    [Mixture-of-Experts Language Models](https://arxiv.org/pdf/2401.06066)
    

With this, you should now have the main intuitions to wrap your head around the DeepSeek-R1 model.

[![Image 96](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed7fd8c3-7654-497c-a8e2-1f2e7930992e_3302x1438.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed7fd8c3-7654-497c-a8e2-1f2e7930992e_3302x1438.png)

If you felt needed a little more foundational information to understand this post, I’d suggest you pick up a copy of [Hands-On Large Language Models](https://www.llm-book.com/) or read it online on [O’Reilly](https://learning.oreilly.com/library/view/hands-on-large-language/9781098150952/) and check it out on [Github](https://github.com/handsOnLLM/Hands-On-Large-Language-Models).

[![Image 97: Book Cover](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd7beb5f-e943-4d2d-8b4c-eb1e80231670_582x768.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd7beb5f-e943-4d2d-8b4c-eb1e80231670_582x768.png)

Other suggested resources are:

*   [DeepSeek R1's recipe to replicate o1 and the future of reasoning LMs](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1) by
    
*   [A Visual Guide to Mixture of Experts (MoE)](https://substack.com/home/post/p-148217245) by
    
*   Sasha Rush’s YouTube video [Speculations on Test-Time Scaling (o1)](https://www.youtube.com/watch?v=6PEJ96k1kiw)
    
*   Yannis Kilcher’s [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (Paper Explained)](https://www.youtube.com/watch?v=bAWV_yrqx4w)
    
*   [Open R1](https://github.com/huggingface/open-r1) is the HuggingFace project to openly reproduce DeepSeek-R1
    
*   [Putting RL back in RLHF](https://huggingface.co/blog/putting_rl_back_in_rlhf_with_rloo)

