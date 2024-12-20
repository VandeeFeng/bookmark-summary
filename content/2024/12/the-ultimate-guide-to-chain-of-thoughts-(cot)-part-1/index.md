---
title: The Ultimate Guide to Chain of Thoughts (CoT)- Part 1
date: 2024-12-20
extra:
  source: https://learnprompting.org/blog/guide-to-chain-of-thought-part-one
  original_title: The Ultimate Guide to Chain of Thoughts (CoT)- Part 1
---
## Summary
**摘要**：
本文主要讲解了Chain-of-Thought（这里的简称被称作CoT）推理策略在大型语言模型（LLMs）中的关键作用以及其对LLMs推理能力的重要性。LLMs通过被命名为“CoT”的策略实现了解决问题、推理和多步骤任务生成等各种复杂任务的能力提升，这种技术使得模型在数学问题解决、逻辑推理、复杂语言生成任务等领域更加准确。随后，文章详细介绍了标准CoT、零样本CoT、自一致性、自动化CoT（Auto-CoT）、表格化CoT（Tab-CoT）等CoT策略的版本，并阐述了它们如何使CoT技术在各个领域变革。本文同样讨论了CoT策略的多样性和路径拓展，如对比式CoT、决策树结构化思考（即Tree-of-Thoughts ToT）以及结构化思考图（Graph of Thoughts GoT）的概念。此外，讨论了编程性思考促进策略（Programs of thoughts PoT），支持LLMs通过与外部语言解释器的交互（例如Python）来解决复杂问题。最后，文章引导读者理解为何掌握CoT技巧对AI工程师至关重要，这将直接影响AI系统的可解释性和可理解性。

**要点总结**：
- **CoT推理策略**：CLMs在处理复杂任务时提出断链性问题并将其分解为多个步骤。
- **标准CoT**：借助用户输入的数个示例，此方法允许LLMs系统逐个解决问题，然后组合得出答案。
- **零样本CoT**：通过任务特有的提示词“让我们一步一步思考”，此方法无需示例即可回答问题，主要适用于算术、符号推理和逻辑推理任务。
- **自一致性**：通过向LMM提问多次，收集并聚合多个回答，确保结果的一致性，降低算法不完全推理的风险。
- **自动化CoT（Auto-CoT）**：利用算法自动生成推理步骤，进一步自动化后零样本CoT过程。
- **表格化CoT（Tab-CoT）**：通过在表格中显式建模推理过程，提高输出的清晰度与结构化。
- **对比式CoT**：通过提供正确与错误的推理示例，训练模型识别问题避免滥推。
- **决策树结构化思考（Tree-of-Thoughts ToT）**：鼓励LLMs通过多个思维链发展逻辑推理，相似于决策树。
- **结构化思考图（Graph of Thoughts GoT）**：巩固CoT概念，通过建模信息网络为LLMs提供更为动态的推理框架。
- **编程性思考促进策略（Programs of thoughts PoT）**：编码生成的数学表达式并执行，解决复杂数学表达式和迭代数值计算。
- **在AI领域的应用**：掌握CoT技巧对AI工程师凸显了对构建可解释、准确、适应性强的AI系统的价值。
## Full Content
Title: The Ultimate Guide to Chain of Thoughts (CoT): Part 1

URL Source: https://learnprompting.org/blog/guide-to-chain-of-thought-part-one

Markdown Content:
8 minutes

🟢easy Reading Level

Let's face it, we live in an era where machines can understand and generate human language with astonishing accuracy. Thanks to Large Language Models (LLMs), cutting-edge technology is revolutionizing how we interact with computers.

Among all the prompting approaches, **Chain-of-Thought (CoT)** prompting has the most significant impact on LLMs’ ability to reason and solve problems.

_In this first installment of the ultimate guide to Chain-of-Thought (CoT), we’ll break down what CoT prompting is, how it works, why it’s so impactful, and how its variations are transforming industries in every domain._

### [Curious about prompting? Join our "Inroduction to Prompt Engineering" course to learn the fundamentals of prompting!](https://learnprompting.org/courses/introduction_to_prompt_engineering)

Large Language Models and Prompting
-----------------------------------

LLM has achieved great reasoning ability and has started the generative AI revolution. Despite the ever-increasing size of the models, LLMs alone are insufficient to perform complex tasks such as challenging arithmetic, commonsense, and symbolic reasoning problems.

Among different prompting strategies designed to improve LLMs' reasoning ability, Chain-of-Though (CoT) prompting has stood out as the most impactful. CoT prompting enables LLMs to break down complex tasks into sequential intermediate steps, emulating a form of human reasoning. This technique allows models to approach problems more methodically, thus enhancing their accuracy in mathematical problem-solving, logical reasoning, multi-step language generation tasks, and other tasks.

Standard Chain-of-Thought (CoT) Prompting
-----------------------------------------

The main idea behind [Standard Chain-of-Thought or Few-Shot Chain-of-Thought](https://learnprompting.org/docs/intermediate/chain_of_thought) lies in our cognition process. Just like how humans solve problems by breaking them into smaller, more digestible parts, the chain-of-thought technique breaks down complex tasks into sequential intermediate steps.

Many real-world problems are multi-step reasoning problems; hence, CoT performs well in these scenarios. Instead of directly answering a problem, a typical problem is broken down into intermediate steps, and each step is solved before giving the final answer. Furthermore, this makes the answer more interpretable with the steps provided.

Here are multiple examples from the original paper for different scenarios.

To use CoT, we need to provide the sequence of thoughts to answer a similar question as an input context to enable LLM to answer the next question.

Here's a Prompt Template:

![Image 14: Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75)

#### Prompt Template

* * *

Q: \[Example of Input\]

A: \[Example of Chain of Thought Process e.g.: Initially, …. Then … therefore…\] \[Output: eg: The answer is …\]

Q: \[Your Question\]

A:

Variants of CoT
---------------

### Zero-shot Chain-of-Thought (Zero-shot CoT)

The standard CoT is also known as a Few-shot CoT, as a few examples are provided as input context for LLM. However, it’s cumbersome for a user to provide examples in every scenario.

It was soon discovered that large language models are zero-shot reasoners, i.e., they can answer questions without providing specific examples in the prompt just by adding a single phrase, “Let’s think step by step.” This is what's called [Zero-shot Chain-of-Thought (Zero-shot CoT)](https://learnprompting.org/docs/intermediate/zero_shot_cot).

Zero-shot CoT performs well for arithmetic, symbolic reasoning, and other logical reasoning tasks.

![Image 15: Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75)

#### Prompt Template

* * *

\[Problem\].

Let’s think step by step.

As demonstrated below, zero-shot prompting can be used to employ a two-stage prompting technique to extract reasoning and an answer.

The extraction step must often be task-specific, making Zero-Shot CoT less generalizable than it initially appears. Here’s another example

![Image 16: Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75)

#### Prompt

* * *

If a car travels 60 kilometers per hour for 2 hours, how far will it travel?

Think step-by-step.

![Image 17: Robot](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Frobot.webp&w=48&q=75)

#### AI Output

* * *

Step 1: Calculate how far the car travels in one hour by multiplying the speed (60 kilometers per hour) by the time (1 hour).

60 km/h x 1 hour = 60 kilometers

Step 2: Since the car travels for 2 hours, multiply the distance traveled in one hour by 2.

60 km x 2 = 120 kilometers

Therefore, the car will travel 120 kilometers in 2 hours.

### Self-Consistency

Large Language Models do not necessarily generate the same answer to the same question. LLMs often incorporate a degree of randomness in their responses to make them sound more natural and less predictable. Hence, LLM may give wrong answers due to the selection of a random chain of thought for reasoning.

[Self-consistency](https://learnprompting.org/docs/intermediate/self_consistency) is an approach that asks a model the exact prompt multiple times and takes most of the results as the final answer. By aggregating multiple responses to the same prompt, the final answer can represent a consistent answer from multiple responses.

Many complex math or science problems require logical rigor. Applying self-consistency techniques helps reduce errors caused by incomplete reasoning.

Most LLMs employ self-consistency behind the scenes by sampling multiple outputs, aggregating them, and returning the most consistent one. In some LLMs, you can change between the answers as different drafts. Here’s an example from Gemini.

### Automatic Chain Of Thought Prompting (Auto-CoT)

[Automatic Chain of Thought Prompting](https://learnprompting.org/docs/advanced/thought_generation/automatic_chain_of_thought) automatically generates intermediate reasoning steps extendeding the automation introduced by zero-shot prompting even further.

Don't confuse Auto-CoT with [Zero-Shot CoT](https://learnprompting.org/docs/intermediate/zero_shot_cot). While Auto-CoT uses a procedure to generate reasoning chains for CoT prompting, Zero-Shot CoT provides no additional demonstrations and relies solely on the "Let's think step by step" prompt.

To use Auto-CoT, you need to:

1.  Apply **Sentence-BERT** or similar model to embed and cluster questions based on semantic similarity. The goal is to ensure the selected demonstrations cover a diverse range of reasoning patterns.
    
2.  Once clusters are formed, Auto-CoT selects representative questions from each cluster and uses **Zero-Shot CoT** to generate reasoning chains for each. These chains are then used as demonstrations for the LLM to solve new tasks.
    

This strategy applies to large-scale automated decision-making workflows, making reasoning scalable for diverse reasoning tasks. However, it may require fine-tuning or advanced tooling for optimal results.

The code for Auto-CoT is open-sourced by Amazon Science and available for further research and implementation at [amazon-science/auto-cot](https://github.com/amazon-science/auto-cot).

### Tabular Chain-of-Thought Prompting (Tab-CoT)

[Zero-shot Tabular Chain of Thought (Tab-CoT)](https://learnprompting.org/docs/advanced/thought_generation/tabular_chain_of_thought_tab_cot) approach allows the complex reasoning process to be explicitly modeled in a highly structured manner, i.e. in a tabular form.

Tab-CoT extends the Zero-shot prompting by presenting the output in a tabular form.

![Image 18: Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75)

#### Prompt Template

* * *

\[Your Question\]

|step|subquestion|procedure|result|

Data analysis and multi-step computation tasks are examples of use cases for this approach. Even though it ensures clarity and structure in output, it’s flexibility is limited for non-tabular tasks.

Note: Most current chat apps are designed to always think step-by-step; hence, a step-by-step answer might override the table structure.

Extending CoT
-------------

### Contrastive Chain-of-Thought (CoT)

In the conventional CoT, we usually only provide question-answer pairs as input context. This does not inform language models about what mistakes to avoid, potentially leading to more errors.

Inspired by how humans learn from positive and negative examples, [Contrastive Chain-of-Thought Prompting](https://learnprompting.org/docs/advanced/thought_generation/contrastive_cot) extends the standard CoT where user provides examples of positive and negative answers in the context to enhance language model reasoning. Providing valid and invalid reasoning examples guides the model in reasoning step-by-step while reducing reasoning mistakes.

![Image 19: Astronaut](https://learnprompting.org/_next/image?url=%2Fdocs%2Fassets%2Fastronaut.webp&w=48&q=75)

#### Prompt Template

* * *

\[Sample question or example question\] \[Correct explanation question\] \[Incorrect explanation for question\]

Actual question/query

This type of prompting can be useful in scenarios where logical fallacies are common, and pointing out certain fallacies or biases in the input context helps the model avoid such issues in the response. For example, problems that involve deductive or inductive reasoning often require careful attention to avoid biases and fallacies like hasty generalization, anchoring bias, etc.

Similarly, when evaluating arguments or claims, it's essential to recognize fallacies such as ad hominem attacks, straw man arguments, or appeals to emotion, which can undermine the validity of the reasoning. Identifying such issues in the input context helps prevent the model from producing incorrect responses.

### Tree-of-Thoughts (ToT)

[Tree of Thoughts (ToT)](https://learnprompting.org/docs/advanced/decomposition/tree_of_thoughts) expands on the concept of Chain of Thought (CoT) by encouraging bot linear reasoning through intermediate steps and branching into multiple pathways, similar to decision trees. This approach enables models to explore diverse reasoning paths before selecting the most optimal solution.

Tree-of-Thoughts is analogous to traditional planning search algorithms that explore different pathways before arriving at the goal state. Tree-of-Thought effectively extends the CoT into multiple chains of thoughts forming a tree.

### Graph of Thoughts (GoT)

[Graph of Thoughts (GoT)](https://arxiv.org/abs/2308.09687) is a framework that further generalizes the idea of Chain-of-Thoughts beyond Tree-of-Thoughts(ToT).

It models the information generated by LLMs as an arbitrary graph where units of information are vertices connected through their interdependencies indicated by edges. This extension requires building a graph framework through LLMs, as mentioned in the architecture below.

The GoT architecture includes a set of interacting modules consisting of

1.  Prompter that prepares the messages for the LLM
2.  Parser that extracts information from LLM thoughts
3.  Scoring module that verifies and scores the LLM thoughts
4.  Controller that coordinates the entire reasoning process and decides on how to progress it

Each module provides APIs to work with them, as visible in the diagram below.

Here’s an example of the prompt and the graph reasoning state for the sorting problem.

### Program of Thoughts Prompting

In Chain-of-Thought (CoT) Prompting, LLMs perform both reasoning and computations. The LLM generates mathematical expressions as a reasoning step and then solves it to get the final answer. However, LLMs are not the ideal candidate for solving mathematical expressions as they are not capable of solving complex mathematical expressions and are inefficient for performing iterative numerical computations.

[Program of Thoughts (PoT)](https://learnprompting.org/docs/advanced/decomposition/program_of_thoughts) prompting technique delegates the computation steps to an external language interpreter such as a python to get accurate response. It utilizes a zero-shot CoT approach to write and execute code to get the final answer. Here’s an example of how PoT can perform better compared to CoT.

PoT requires execution of generated code. Generation of malicious code may harm the machine running the snippets. Nevertheless, PoT can be very helpful for algorithmic

Why Chain-of-Thought is Critical for AI Engineers
-------------------------------------------------

For AI engineers, mastering CoT techniques is crucial because it directly impacts the **explainability** and **interpretability** of AI systems. As deep learning models grow more complex, understanding the reasoning behind AI-generated solutions is vital for debugging, improving accuracy, and ensuring ethical AI deployment. Furthermore, CoT techniques allow engineers to address previously unsolvable challenges in tasks that require logic and step-wise problem-solving, making it a cornerstone in the development of next-generation AI systems.

The unique characteristic of CoT is its ability to **generate intermediate steps** that offer a logical pathway, much like how humans mentally break down tasks into smaller parts before reaching conclusions. This progressive reasoning process is a paradigm shift from traditional black-box machine learning models, which often leave human engineers unable to trace or understand the decision-making process.

Conclusion
----------

Chain-of-Thought reasoning represents a significant leap forward in AI’s ability to handle complex tasks with **accuracy**, **transparency**, and **flexibility**. By breaking problems into manageable steps, CoT enables AI engineers to design models that mirror human-like reasoning, ultimately leading to more **explainable**, **accurate**, and **adaptable AI systems**.

As we look toward the future, it’s clear that CoT techniques will continue to shape the landscape of artificial intelligence, paving the way for innovations in **NLP**, **problem solving**, and **autonomous decision-making**. For AI engineers, the time to master Chain-of-Thought is now.

