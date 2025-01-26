---
title: simplerl-reason
date: 2025-01-26
extra:
  source: https://hkust-nlp.notion.site/simplerl-reason
  original_title: simplerl-reason
---
## Summary
**摘要**：
这篇博客文章介绍了一项研究，专注于利用强化学习（Reinforcement Learning）技术提升7B模型的数学推理能力。研究仅使用了8,000个数学问题及答案示例，便获得了AIME、AMC以及MATH等复杂数学推理测试的显著性能提升。通过直接对7B基础模型进行强化学习，该研究发现与直觉式细则奖励模型和序列到序列（Sequence-to-Sequence，SFT）方法相比，强化学习在保持简单的同时展现出卓越效果，尤其在小模型在小数据集上的应用方面。该结果不仅超出了基础模型但未进行强化学习的性能，而且能在没有奖励模型的辅助下，与在更大数据集上训练的模型取得相竞争的表现，其中涉及到更复杂组件的研究，如.prime和.rStar-MATH。

**要点总结**：
- **主要方法**：通过仅使用8,000个数学问题示例对7B基础模型进行强化学习，提升模型在复杂数学推理测试中的性能。
- **性能提升**：即使在有限数据集的情况下，所训练模型也能够达到与使用更大数据集训练的模型相媲美的效果。
- **方法与技术**：仅采用了PPO算法作为强化学习方法，并使用了一种基于规则的奖励函数，避免了奖励模型和MCTS等复杂技术的应用，以使模型能够快速学习生成期望的格式和正确性的响应。
- **结果与发现**：实验揭示了训练过程中的自反性模式，强化了模型的学习并提高了性能，特别是在生成过程的适应性上展现出了独特的能力，尤其是在逐步学习过程中，模型能够产生反思性响应，达到一种理解其决策过程的自我提升状态。
- **分享与扩展**：研究者提供了他们的训练代码和详细信息的开源，为社区开创了一个基于7B基础模型的简明有效人工一般化学习领域研究的起点，旨在探索强化学习在推理任务上的潜力。
## Full Content
Title: Notion – The all-in-one workspace for your notes, tasks, wikis, and databases.

URL Source: https://hkust-nlp.notion.site/simplerl-reason

Markdown Content:
7B Model and 8K Examples: Emerging Reasoning with Reinforcement Learning is Both Effective and Efficient
--------------------------------------------------------------------------------------------------------

![Image 22: 💡](blob:https://hkust-nlp.notion.site/2ae2cc6f0544e8fcceb52fb6a599a7ea)

This blog will present a replicate of the [DeepSeek-R1-Zero and DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) training on small models with limited data, many of the experiments were developed and performed by us independently before DeepSeek-R1’s release. We show that long Chain-of-Thought (CoT) and self-reflection can emerge on a 7B model with only 8K MATH examples, and we achieve surprisingly strong results on complex mathematical reasoning. Importantly, we fully open-source our training code and details to the community to inspire more works on reasoning.

Starting from Qwen2.5-Math-7B (base model), we perform reinforcement learning on it directly with only 8K examples from the MATH dataset. No reward model, no SFT, just 8K MATH examples for verification, the resultant model achieves (pass@1 accuracy) 33.3% on AIME, 62.5% on AMC, and 77.2% on MATH, outperforming Qwen2.5-math-7B-instruct and being comparable to [PRIME](https://github.com/PRIME-RL/PRIME) and [rStar-MATH](https://arxiv.org/abs/2501.04519) that use \>50x more data and more complicated components. We also try performing a long CoT SFT with the same 8K examples before the RL stage and obtain even better performance.

![Image 23: 👉](blob:https://hkust-nlp.notion.site/2ae2cc6f0544e8fcceb52fb6a599a7ea)

Many of our experiments were completed prior to the release of DeepSeek-R1. Interestingly, we independently converged on a similar and straightforward RL approach as DeepSeek-R1, finding it to be highly effective. The primary difference lies in our use of PPO instead of GRPO. While this research is still ongoing, we believe it is valuable to share our intermediate findings with the community. We hope our work serves as a simple yet effective replication of DeepSeek-R1 Zero and DeepSeek-R1, tailored for smaller models and limited datasets.

![Image 24](https://hkust-nlp.notion.site/image/attachment%3A55e42b69-8668-4d88-9e27-7af252642994%3Aimage_(7).png?table=block&id=18639bdc-1c6b-8096-911d-d5692b1b883e&spaceId=0bc39406-d20a-4cfc-97ae-850d0b3aa667&width=1340&userId=&cache=v2)

Training dynamics of our Qwen2.5-SimpleRL-Zero training starting from the Qwen2.5-Math-7B base model, without SFT or reward models. The average benchmark accuracy and length are on 8 complex math reasoning benchmarks. We observe a length decrease in the initial stage because we found the Qwen2.5-Math-7B base model tended to generate both language and code in the response, resulting in lengthy outputs. This default pattern is quickly discouraged throughout RL and the model learns to output in a more appropriate format, and then the length starts to increase regularly. After just a few training steps, we also experienced the "aha moment" described in the DeepSeek-R1 paper — the emergence of self reflection in the model's responses.

Many researchers are exploring possible paths towards learning o-style models, such as distillation, MCTS, process-based reward models, and reinforcement learning. Recently, both [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) and [Kimi-k1.5](https://github.com/MoonshotAI/Kimi-k1.5) demonstrate an extremely simple recipe on this path, using simple RL algorithms to learn emerging long CoT and self-reflection patterns and leading to strong results, where no MCTS and reward models are used. However, their experiments are based on huge models in a large-scale RL setting. It remains unknown whether small models can demonstrate similar behaviors, how much data is needed, and how would the quantitative results compare with other approaches. This blog reproduces the training of DeepSeek-R1-Zero and DeepSeek-R1 for complex mathematical reasoning, starting from Qwen-2.5-Math-7B (base model), and only using 8K (query, final answer) examples from the original MATH dataset for rule-based reward modeling in RL. We are surprised how far the 8K MATH examples lift this 7B base model without any other external signals:

All results are in pass@1 accuracy

Qwen2.5-7B-SimpleRL-Zero is the simple RL training from the base model directly, using only 8K MATH examples. It achieves gains of nearly 20 absolute points on average compared to the base model. Compared to Qwen2.5-Math-7B-Base with the same 8K data SFT, RL enjoys much better generalization being 22% higher absolutely. Moreover, Qwen2.5-7B-SimpleRL-Zero outperforms Qwen-2.5-Math-7B-Instruct on average, and is roughly comparable to the recently released [Eurus-2-7B-PRIME](https://github.com/PRIME-RL/PRIME) and [rStar-Math-7B](https://arxiv.org/abs/2501.04519) which are also based on Qwen-2.5-Math-7B. These baselines contain much more complicated components such as reward models and use at least 50x more and advanced data:

Data comparison of different approaches

We are both excited and surprised by the significant gains achieved using only 8K MATH examples. Notably, while the MATH queries are considerably easier than many challenging benchmarks such as AIME and AMC, this simple RL recipe demonstrates remarkable generalization, with performance increasing by at least 10 absolute points compared to the base model. This easy-to-hard generalization effect is something we could not have envisioned with standard SFT training on the same dataset. We fully open-source our training code and details, hopefully as a strong baseline setup for the community to further explore the potential of RL for reasoning.

Next, we are going to zoom into the details on our setup, and what is happening during this RL training, such as the emergence of long CoT and self-reflection patterns.

Similar to DeepSeek R1, our RL recipe is kept extremely simple without using reward models or MCTS-like techniques. We use the PPO algorithm, and employ a rule-based reward function that assigns rewards based on the format and correctness of the generated response:

If the response provides a final answer in the specified format and is correct, it receives a reward of +1.

If the response provides a final answer but it is incorrect, the reward is set to -0.5.

If the response fails to provide a final answer, the reward is set to -1.

The implementation is based on [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF). Our initial trials showed that this reward function helps the policy model quickly converge towards producing responses in the desired format.

In our experiments, we start from the [Qwen2.5-Math-7B-Base](https://huggingface.co/Qwen/Qwen2.5-Math-7B) model and evaluate the performance on challenging mathematics reasoning benchmarks, including AIME2024, AMC23, GSM8K, MATH-500, Minerva Math, and OlympiadBench. The training utilizes approximately 8,000 queries from difficulty levels 3-5 of the MATH training dataset. We conduct experiments in the following two settings following DeepSeek-R1-Zero and DeepSeek-R1 respectively:

SimpleRL-Zero: We perform RL directly from the base model without doing SFT first. We only use the 8K MATH (query, answer) pairs

SimpleRL: We perform long-cot SFT first as a cold start. The SFT data is the 8K MATH queries with responses distilled from QwQ-32B-Preview. Then we perform our RL recipe using the same 8K MATH examples.

Our main results of SimpleRL-Zero has been reported in the introduction section, it outperforms Qwen2.5-Math-7B-Instruct and achieves comparable results to PRIME and rStar-Math even though it only uses 8K MATH examples. Below we share the training dynamics and some interesting emerging patterns.

Training reward and rollout response length

![Image 25](https://hkust-nlp.notion.site/image/attachment%3A5f34e56d-4b7b-4231-baa2-95e26330ed11%3Atrain_reward_zero_v2.png?table=block&id=18639bdc-1c6b-801e-9260-cbb7e3ff1386&spaceId=0bc39406-d20a-4cfc-97ae-850d0b3aa667&width=670&userId=&cache=v2)

Evaluation accuracy (pass@1) and response length across 8 benchmarks

As shown above, the accuracy is improving steadily over training on all benchmarks, while the length decreases first and then gradually increases. After further investigation, we found that the Qwen2.5-Math-7B base model tends to generate a lot of code in the beginning, which may be due to the original training data distribution of the model. We found that the length decreases first because the RL training gradually removes such patterns, learning to reason with normal language. Then after that the generation length starts to increase again, where the self-reflection pattern emerges as exemplified below.

Around step 40, we found that the model starts to generate self-reflection patterns, the “aha moment” from the DeepSeek-R1 paper. Below we show an example.

![Image 26](https://hkust-nlp.notion.site/image/attachment%3A7476c0db-d7a0-405b-9e2e-e9fafab62041%3Aimage.png?table=block&id=18639bdc-1c6b-8075-aced-cda817f6034d&spaceId=0bc39406-d20a-4cfc-97ae-850d0b3aa667&width=1420&userId=&cache=v2)

