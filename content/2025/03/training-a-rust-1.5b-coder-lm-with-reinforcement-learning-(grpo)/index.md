---
title: Training a Rust 1.5B Coder LM with Reinforcement Learning (GRPO)
date: 2025-03-09
extra:
  source: https://ghost.oxen.ai/training-a-rust-1-5b-coder-lm-with-reinforcement-learning-grpo/
  original_title: Training a Rust 1.5B Coder LM with Reinforcement Learning (GRPO)
---
## Summary
**摘要**：
本文介绍了如何使用 Group Relative Policy Optimization (GRPO) 算法，结合 Rust 编译器和 cargo 工具，训练一个用于 Rust 编程的 1.5B 参数的小型语言模型 (LLM)。文章作者通过将 Python 代码问题转换为 Rust 代码问题，并利用 Qwen 2.5 Coder 32B Instruct 模型生成 Rust 代码和单元测试，构建了一个包含 16500 个 prompt,code,unit\_test 三元组的数据集。作者将问题建模为让模型在同一次生成中同时生成代码和测试，并设计了一系列奖励函数，包括检查代码块、cargo 构建、clippy 检查和单元测试等。实验结果表明，经过 GRPO 训练后，模型的代码构建通过率从 61% 提升到 80%，单元测试通过率从 22% 提升到 37%。作者还分享了训练过程中的一些技巧，例如使用 RustTool 类来运行 cargo 命令，并使用装饰器来记录奖励函数的结果。最后，作者展望了未来工作，包括扩展数据集以支持更多类型的编程任务，以及在更大的模型上进行实验。

**要点总结**：

1.  **利用 GRPO 算法和 Rust 工具链训练小型 Rust 编程语言模型**：文章展示了如何使用 GRPO，一种强化学习算法，来训练一个专门用于 Rust 编程的小型语言模型。通过利用 Rust 编译器和 cargo 工具的反馈，模型可以学习生成编译通过且单元测试也通过的代码。
2.  **构建 Rust 编程数据集**：由于缺乏 Rust 编程的训练数据，作者首先将现有的 Python 编程数据集转换为了 Rust 数据集。这个数据集包含了提示 (prompts)、生成的 Rust 代码以及对应的单元测试，为后续的模型训练提供了数据基础。
3.  **将问题建模为单次生成代码和测试**：区别于先有代码再有单元测试的流程，作者另辟蹊径，让模型在一次生成过程中同时产生代码和单元测试。这种方法简化了训练流程，但同时也需要设计额外的奖励机制，以防止模型通过生成过于简单的代码和测试来“作弊”。
4.  **设计 Cargo 奖励函数以优化模型**：文章详细介绍了如何使用 cargo 工具链（Rust 的包管理器和构建工具）来设计奖励函数。这些奖励函数会评估生成的代码是否能够成功编译、通过 clippy 检查（代码风格检查）以及通过单元测试来指导模型的学习过程。
5.  **实验结果表明 GRPO 提升了模型性能**：经过一个 epoch 的 GRPO 训练后，模型的性能有了显著提升。代码构建通过率从 61% 提高到 80%，单元测试通过率从 22% 提高到 37%，证明了 GRPO 算法在提升小模型 Rust 编程能力方面的有效性。

## Full Content
Title: Training a Rust 1.5B Coder LM with Reinforcement Learning (GRPO)

URL Source: https://ghost.oxen.ai/training-a-rust-1-5b-coder-lm-with-reinforcement-learning-grpo/

Published Time: 2025-03-06T00:22:09.000Z

Markdown Content:
[Group Relative Policy Optimization (GRPO)](https://www.oxen.ai/blog/why-grpo-is-important-and-how-it-works?ref=ghost.oxen.ai) has proven to be a useful algorithm for training LLMs to reason and improve on benchmarks. [DeepSeek-R1](https://www.oxen.ai/blog/how-deepseek-r1-grpo-and-previous-deepseek-models-work?ref=ghost.oxen.ai) showed that you can bootstrap a model through a combination of supervised fine-tuning and GRPO to compete with the state of the art models such as OpenAI's o1.

To learn more about how it works in practice, we wanted to try out some of the techniques on a real world task. This post will outline how to train your own custom small LLM using GRPO, your own data, and custom reward functions. Below is a sneak preview of some of the training curves we will see later. It is quite entertaining to watch the model learn to generate code blocks, get better at generating valid code that compiles, and finally code that passes unit tests.

![Image 1](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-05-at-4.07.17-PM.png)

If you want to jump straight into the action, the GitHub repository can be found [here](https://github.com/Oxen-AI/GRPO-With-Cargo-Feedback/tree/main?ref=ghost.oxen.ai).

[GitHub - Oxen-AI/GRPO-With-Cargo-Feedback: This repository has code for fine-tuning LLMs with GRPO specifically for Rust Programming using cargo as feedback This repository has code for fine-tuning LLMs with GRPO specifically for Rust Programming using cargo as feedback - Oxen-AI/GRPO-With-Cargo-Feedback ![Image 2](https://ghost.oxen.ai/content/images/icon/pinned-octocat-093da3e6fa40-7.svg)Oxen-AI ![Image 3](https://ghost.oxen.ai/content/images/thumbnail/GRPO-With-Cargo-Feedback)](https://github.com/Oxen-AI/GRPO-With-Cargo-Feedback?tab=readme-ov-file&ref=ghost.oxen.ai#-grpo-with-cargo-feedback)

This post will not go into the fundamentals of GRPO, if you want to learn more about how it works at a fundamental level, feel free to checkout our deep dive into the algorithm below.

[Why GRPO is Important and How it Works | Oxen.ai Last week on Arxiv Dives we dug into research behind DeepSeek-R1, and uncovered that one of the techniques they use in the their training pipeline is called Group Relative Policy Optimization (GRPO). At it’s core, GRPO is a Reinforcement Learning (RL) algorithm that is aimed at improving the model’s reasoning ability. It was first introduced in their paper DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models, but was also used in the post-training of DeepSeek-R1. ![Image 4](https://ghost.oxen.ai/content/images/icon/favicon-47.ico)Oxen.ai ![Image 5](https://ghost.oxen.ai/content/images/thumbnail/opengraph-image-1defv3-11)](https://www.oxen.ai/blog/why-grpo-is-important-and-how-it-works?ref=ghost.oxen.ai)

Why Rust?
---------

Rust seems like it would be a great playground for Reinforcement Learning (RL) because you have access to the rust compiler and the cargo tooling. The Rust compiler gives great error messages and is pretty strict.

In this project, the first experiment we wanted to prove out was that you can use cargo as a feedback mechanism to teach a model to become a better programmer. The second experiment we wanted to try was to see how small of a language model can you get away with. These experiments are purposely limited to a single node H100 to limit costs and show how accessible the training can be.

We are also a Rust dev shop at Oxen.ai, so have some interesting applications 🦀 x 🐂.

Why 1.5B?
---------

Recently, there is a lot of work seeing how far we can push the boundaries of small language models for specific tasks. When you have a concrete feedback mechanism such as the correct answer to a math problem or the output of a program, it seems you can shrink the model while maintaining very competitive performance.

The rStar-Math paper from Microsoft shows this in the domain of verifiable math problems allowing the model to reason. The 1.5B model outperforms GPT-4o and o1-preview.

![Image 6](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-04-at-9.31.07-AM.png)

[rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking We present rStar-Math to demonstrate that small language models (SLMs) can rival or even surpass the math reasoning capability of OpenAI o1, without distillation from superior models. rStar-Math achieves this by exercising “deep thinking” through Monte Carlo Tree Search (MCTS), where a math policy SLM performs test-time search guided by an SLM-based process reward model. rStar-Math introduces three innovations to tackle the challenges in training the two SLMs: (1) a novel code-augmented CoT data sythesis method, which performs extensive MCTS rollouts to generate step-by-step verified reasoning trajectories used to train the policy SLM; (2) a novel process reward model training method that avoids naïve step-level score annotation, yielding a more effective process preference model (PPM); (3) a self-evolution recipe in which the policy SLM and PPM are built from scratch and iteratively evolved to improve reasoning capabilities. Through 4 rounds of self-evolution with millions of synthesized solutions for 747k math problems, rStar-Math boosts SLMs’ math reasoning to state-of-the-art levels. On the MATH benchmark, it improves Qwen2.5-Math-7B from 58.8% to 90.0% and Phi3-mini-3.8B from 41.4% to 86.4%, surpassing o1-preview by +4.5% and +0.9%. On the USA Math Olympiad (AIME), rStar-Math solves an average of 53.3% (8/15) of problems, ranking among the top 20% the brightest high school math students. Code and data will be available at https://github.com/microsoft/rStar. ![Image 7](https://ghost.oxen.ai/content/images/icon/apple-touch-icon-36.png)arXiv.orgXinyu Guan ![Image 8](https://ghost.oxen.ai/content/images/thumbnail/arxiv-logo-fb-32.png)](https://arxiv.org/abs/2501.04519?ref=ghost.oxen.ai)

My hypothesis is that we can push similar level of performance on coding, since you have a similar verifiable reward: _Does the code compile and does it pass unit tests?_

Benefits of Smol LMs
--------------------

Having small coding models have many benefits including cost, throughput, data privacy, and ability to customize to your own codebase / coding practices. Plus it's just a fun challenge.

The dream would be to eventually have this small model do all the cursor-like tasks of next tab prediction, fill in the middle, and improve it’s code in an agent loop. But let’s start simple.

Formulating the Problem
-----------------------

There are a few different ways you could structure the problem of writing code that passes unit tests. We ended up trying a few. A seemingly straightforward option would be to have a set of verifiable unit tests that must pass given the generated code. This would give us a gold standard set of verifiable answers.

![Image 9](https://ghost.oxen.ai/content/images/2025/03/Prompt-Code-Unit-Tests-1.png)

After trying out this flow we found two main problems. First, if you don’t let the model see the unit tests while writing the code, it will have no sense of the interface it is writing for. Many of the errors ended up being type or naming mismatches between the code and the unit tests while evaluating against pre-built, verified unit tests.

![Image 10](https://ghost.oxen.ai/content/images/2025/03/Errors-1.png)

Second, if you allow the model to see the unit tests while its writing the code, you lose out on developer experience. Unless you are a hard core “Test Driven Developer” you probably just want to send in a prompt and not think about the function definition or unit tests yet.

Rather than trying to come up with something more clever, we ended up optimizing for simplicity. We reformulated the problem to have the model generate the code and the tests _within the same response_.

![Image 11](https://ghost.oxen.ai/content/images/2025/03/Simplified.png)

With single pass there is a danger of the model hacking the reward function to make the functions and unit tests trivial. For example it could just have println! and no assert statements to get everything to compile and pass. We will return to putting guardrails on for this later.

Finally we add a verbose `system` prompt to give the model guidance on the task.

![Image 12](https://ghost.oxen.ai/content/images/2025/03/system-prompt.png)

The system prompt gives the model some context in the format and style in which we are expecting the model to answer the user queries.

The Dataset
-----------

Before training, we need a dataset. When starting out, we did not see many datasets targeted at Rust. Many of the LLM benchmarks are targeted at Python. So the first thing we did was convert a dataset of prompts asking Pythonic questions to a dataset of Rust prompts.

We took a random 20k prompts from the [Ace-Code-87k](https://www.oxen.ai/TIGER-Lab/AceCode-87K?ref=ghost.oxen.ai) dataset. We then used Qwen 2.5 Coder 32B Instruct to write rust code and unit tests. We ran the code and unit tests through the compiler and testing framework to filter out any triples that did not pass the unit tests. This left us with 16500 prompt,code,unit\_test triples that we could train and evaluate on. The dataset was split into 15000 train, 1000 test, and 500 evaluation data points.

The final data looks like the following:

![Image 13](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-04-at-3.45.31-PM.png)

[ox/Rust/cargo\_test\_passed\_train.parquet at main This is a dataset of rust questions and generated code created to fine tune small language models on rust.. Contribute to the ox/Rust repository by creating an account on Oxen.ai ![Image 14](https://ghost.oxen.ai/content/images/icon/favicon-48.ico) ![Image 15](https://ghost.oxen.ai/content/images/thumbnail/file-13)](https://www.oxen.ai/ox/Rust/file/main/cargo_test_passed_train.parquet?ref=ghost.oxen.ai)

You can follow the prompts and steps by looking at these model runs:

1) Translate to Rust: [https://www.oxen.ai/ox/mbrp-playground/evaluations/ce45630c-d9e8-4fac-9b41-2d41692076b3](https://www.oxen.ai/ox/mbrp-playground/evaluations/ce45630c-d9e8-4fac-9b41-2d41692076b3?ref=ghost.oxen.ai)

2) Write Rust code: [https://www.oxen.ai/ox/mbrp-playground/evaluations/febc562a-9bd4-4e91-88d7-a95ee676a5ed](https://www.oxen.ai/ox/mbrp-playground/evaluations/febc562a-9bd4-4e91-88d7-a95ee676a5ed?ref=ghost.oxen.ai)

3) Write Rust unit tests - [https://www.oxen.ai/ox/mbrp-playground/evaluations/b886ddd6-b501-4db8-8ed6-0b719d0ac595](https://www.oxen.ai/ox/mbrp-playground/evaluations/b886ddd6-b501-4db8-8ed6-0b719d0ac595?ref=ghost.oxen.ai)

Funny enough, for the final formulation of the GRPO training we ended up throwing away the gold standard rust code and unit tests columns. With our reinforcement learning loop we only need the prompts as input. This makes it pretty easy to collect more data in the future. We’ll dive into how the single prompt as input works in the following sections. Even though we threw away the code and unit tests for training, it was nice to know the prompts are solvable.

Setting a Baseline
------------------

Once we formulated the problem, and have a dataset, we wanted to set a baseline and see how well the initial model performs. We will be bootstrapping the training with `Qwen/Qwen2.5-Coder-1.5B-Instruct`.

Below the results are split into how often the build passed, the clippy linter passed, and the unit tests passed.

![Image 16](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-04-at-7.15.38-PM.png)

Clippy depends on the build passing, so those numbers tend to be pretty correlated. Feel free to poke around the raw data on Oxen.ai.

[ox/Rust/results/Qwen2.5-Coder-1.5B-Instruct/results\_code\_and\_tests.parquet at main This is a dataset of rust questions and generated code created to fine tune small language models on rust.. Contribute to the ox/Rust repository by creating an account on Oxen.ai ![Image 17](https://ghost.oxen.ai/content/images/icon/favicon-49.ico) ![Image 18](https://ghost.oxen.ai/content/images/thumbnail/file-14)](https://www.oxen.ai/ox/Rust/file/main/results/Qwen2.5-Coder-1.5B-Instruct/results_code_and_tests.parquet?ref=ghost.oxen.ai)

How does this compare to SOTA?
------------------------------

We also wanted to see how some of the larger foundation models perform on the task. This will give us a theoretical bar to aim for. The best model we found was GPT4.5, to see other models we experimented with and poke around the results check the appendix at the end.

GPT4.5 passes the build 98% of time and passes it's own tests 87% of time. Pretty impressive.

![Image 19](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-03-at-5.29.20-PM.png)

[ox/Rust/results/GPT4.5/predictions.parquet at gpt4-5-results This is a dataset of rust questions and generated code created to fine tune small language models on rust.. Contribute to the ox/Rust repository by creating an account on Oxen.ai ![Image 20](https://ghost.oxen.ai/content/images/icon/favicon-50.ico) ![Image 21](https://ghost.oxen.ai/content/images/thumbnail/file-15)](https://www.oxen.ai/ox/Rust/file/gpt4-5-results/results/GPT4.5/predictions.parquet?ref=ghost.oxen.ai)

Coming in a close second was Claude 3.7 Sonnet.

![Image 22](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-03-at-5.40.42-PM.png)

Okay, all the setup work is complete. We formulated the problem, we have a dataset, we have a baseline, we have a target...finally we can get to training a model!

Designing Reward Functions
--------------------------

One of the beautiful parts of GRPO is the ability to engineer rewards as simple python functions. Once the rewards are defined, you let the model figure out how to optimize for them. Will Brown from Morgan Stanley calls this “Rubric Engineering”. It gives engineers an accessible way to steer models through RL.

![Image 23](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-02-22-at-9.30.32-AM.png)

You can see the whole talk here:

GRPO reward functions take in the prompts, responses and target answers. In fact for some rubrics you do not even need the target answers, you may just be grading attributes about the completion itself like it’s format. Example rubrics could be:

*   Correctness (direct string match)
*   Response Length (number of tokens)
*   Response Format (xml, json, code etc)
*   External Tool Calls (cargo in our case)
*   LLM As A Judge (truthful, helpful, harmless, etc)

We will be using a combination of formatting and running cargo build tools as the rewards. The starter code was taken from @[willccbb](https://gist.github.com/willccbb?ref=ghost.oxen.ai)’s fantastic gist.

[https://gist.github.com/willccbb/4676755236bb08cab5f4e54a0475d6fb](https://gist.github.com/willccbb/4676755236bb08cab5f4e54a0475d6fb?ref=ghost.oxen.ai)

Our Rubric
----------

Let’s see what a “Rubric” looks for our problem. We take a user prompt in, have the LLM generate code and tests, then have a few functions that grade the response.

![Image 24](https://ghost.oxen.ai/content/images/2025/03/RewardsRubric.png)

A reward function could be as simple as a regex requiring that we have a valid test block in our code.

```
# Simple regex for checking if a code block has a rust tests module
def code_has_test_block(code: str) -> Optional[str]:
    # Use re.DOTALL to make '.' match newlines as well
    result = re.search(
        r'(#\[cfg\(test\)\]\s*mod\s+tests\s*\{.*?\})',
        code,
        re.DOTALL
    )
    return 1.0 if result else 0.0

# For each prompt and completion, reward if the response has a test block
def test_block_reward_func(prompts, completions, **kwargs) -> list[float]:
    contents = [completion[0]["content"] for completion in completions]
    return [code_has_test_block(c) for c in contents]
```

You’ll notice that the `prompts` and `completions` are a list and we return a list\[float\] as well. This is because GRPO has a parameter called `num_generations` that determines how many completions may be generated. Also you may have large batches of prompts + completions during generation. The GRPO algorithm generates N different responses per prompt, and each one gets run through your rubric. Here you can see the model trying different iterations, each passing and failing different rubrics.

![Image 25](https://ghost.oxen.ai/content/images/2025/03/ManyRubrics.png)

Over time, the model will learn to pass more and more of the rubrics that you define. With the help of the `trl` library, you can specify multiple different reward functions and pass them into a GRPOTrainer to train the model.

```
trainer = GRPOTrainer(
  model=model,
  processing_class=tokenizer,
  reward_funcs=[
      cargo_build_reward_func, # 1.0 if passes cargo build else 0.0
      cargo_clippy_reward_func, # 1.0 if passes cargo clippy else 0.0
      cargo_test_reward_func, # 1.0 if passes cargo test else 0.0
      non_empty_reward_func, # 1.0 if the code is not empty else 0.0
      code_block_reward_func, # 1.0 if there is a code block else 0.0
      test_block_reward_func, # 1.0 if there is a test block else 0.0
      tests_have_asserts_reward_func # 1.0 if there are assert statements in the test else 0.0
  ],
  args=training_args,
  train_dataset=train_dataset
)
trainer.train()
```

Designing the reward functions is the most _rewarding_ part of setting up a GRPO training loop. Pun intended 🙂.

Cargo Reward Functions
----------------------

Like we alluded to at the start of the post, we will be using the `cargo` toolchain for our rewards. Since reward functions can be defined as pure python functions we will simply use `subprocess` to run the cargo tooling.

The full code can be found in this Marimo notebook on GitHub:

[GRPO-With-Cargo-Feedback/train.py at main · Oxen-AI/GRPO-With-Cargo-Feedback This repository has code for fine-tuning LLMs with GRPO specifically for Rust Programming using cargo as feedback - Oxen-AI/GRPO-With-Cargo-Feedback ![Image 26](https://ghost.oxen.ai/content/images/icon/pinned-octocat-093da3e6fa40-8.svg)GitHubOxen-AI ![Image 27](https://ghost.oxen.ai/content/images/thumbnail/GRPO-With-Cargo-Feedback-1)](https://github.com/Oxen-AI/GRPO-With-Cargo-Feedback/blob/main/train.py?ref=ghost.oxen.ai)

We define a `RustTool` class that can run `cargo build`, `cargo clippy` or `cargo test`. It has a `run()` function that will populate and return a dictionary of results with information about the tool passing/failing and any error messages.

```
class RustTool:
    def __init__(self, name):
        self.name = name

    def run(self, results, project_dir):
        try:
            result = subprocess.run(
                ["cargo", self.name, "--quiet"],
                cwd=project_dir,
                capture_output=True,
                timeout=10
            )
            results[f'{self.name}_passed'] = result.returncode == 0
            results[f'{self.name}_stdout'] = str(result.stdout)
            results[f'{self.name}_stderr'] = str(result.stderr)
        except Exception as e:
            results[f'{self.name}_passed'] = False
            results[f'{self.name}_stdout'] = f"cargo {self.name} failure"
            results[f'{self.name}_stderr'] = f"{e}"
        return results
```

This tool then can be used in a project directory that we will setup for each test. The project setup and tear down creates a directory, writes `main.rs` and `Cargo.toml` files, populates them with the code and tests, the cleans it up after they are run. See the `setup_and_test_rust_project` function in the code for more details on this.

With the ability to setup and teardown mini rust projects, we need to hook this into a GRPO reward function. The signature of reward functions take in a batch of prompts and completions and expects you to grade each prompt+completion pair.

```
# GRPO reward functions take in lists of prompts and completions from the model during training
def cargo_build_reward_func(prompts, completions, **kwargs) -> list[float]:
    # Extract the answers from the completions
    responses = [completion[0]['content'] for completion in completions]
    extracted_answers = [extract_rust_code(r) for r in responses]
    results = []
    for i, answer in enumerate(extracted_answers):
        data = {'rust_code': answer}
        tools = [RustTool("build")]
        cargo_results = setup_and_test_rust_project(data, tools)
        score = 1.0 if cargo_results['build_passed'] else 0.0
        results.append(score)
    return results
```

It can be helpful to log the prompts and completions to disk you to get a sense of how the GRPO algorithm works under the hood. For each prompt you will get N completions. Say we set N=4. This gives our model 4 chances at getting the completion correct.

Take for example task\_8347 from our logs. You can see it tried to implement the particular function four times, and got the solution correct one time. GRPO rewards the model for the correct solution, improving it’s performance over time. The red below are 3 failed unit tests while the green is a single passed on for the given prompt.

![Image 28](https://ghost.oxen.ai/content/images/2025/03/CorrectAndIncorrectSolutions.png)

We setup different reward functions for cargo build, test, and clippy using the same tooling and logic. There are also tests that ensure that the code and tests are non-empty and that the tests do indeed have assert! statements. This makes sure that the model does not hack the reward function and simply write tests with print statements that pass `cargo test`.

All of the results are logged to [Oxen.ai](http://oxen.ai/?ref=ghost.oxen.ai) during training so that we can plot them over time and monitor how well the model is learning. This is where the curves from the beginning come in. As the model is training, we simply compute a rolling average over the data to see if it is improving at the given reward.

```
rolling_avg = df['score'].rolling(window=window_size, min_periods=1).mean()
```

You can see the model begins fluctuating between 30-40% passing the build, and slowly rises up to 70% within the windows as it trains.

![Image 29](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-04-at-7.58.14-PM.png)

The tests take a little longer to start passing, and have a wider variation of success passing.

![Image 30](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-04-at-7.55.24-PM.png)

It is important to monitor how your model is improving on each on of your reward categories as well as look at some inputs and outputs as they flow through the model. This helps to make sure you don’t have any bugs and that the numbers make sense. In order to do this, we wrote a little `@experiment.log` python decorator that wraps the reward functions and logs the results to a jsonl file that is automatically committed to Oxen.ai.

![Image 31](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-04-at-8.01.47-PM.png)

The decorator itself simply writes results to the specified file every time the function gets called. Then there is a separate callback in the training loop that commits the data to [Oxen.ai](http://oxen.ai/?ref=ghost.oxen.ai) every N steps. The data is in chronological order, so you will have to paginate to the end to see the generations at the end of the training run. Below is some sample outputs.

[ox/Rust/outputs/GRPO\_82\_2025-03-02\_22-49-17\_Qwen2.5-Coder-1.5B-Instruct/cargo\_test\_rewards.jsonl at GRPO\_82\_2025-03-02\_22-49-17\_Qwen2.5-Coder-1.5B-Instruct This is a dataset of rust questions and generated code created to fine tune small language models on rust.. Contribute to the ox/Rust repository by creating an account on Oxen.ai ![Image 32](https://ghost.oxen.ai/content/images/icon/favicon-51.ico) ![Image 33](https://ghost.oxen.ai/content/images/thumbnail/file-16)](https://www.oxen.ai/ox/Rust/file/GRPO_82_2025-03-02_22-49-17_Qwen2.5-Coder-1.5B-Instruct/outputs/GRPO_82_2025-03-02_22-49-17_Qwen2.5-Coder-1.5B-Instruct/cargo_test_rewards.jsonl?page=497&ref=ghost.oxen.ai)

How'd we do?
------------

If you remember from earlier when we set a baseline, the `Qwen/Qwen2.5-Coder-1.5B-Instruct` model only got 61% accuracy writing code that builds and 22% accuracy passing the tests.

![Image 34](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-04-at-7.15.38-PM-1.png)

After one epoch of training with GRPO we bumped the build pass rate up to 80% and the tests are passing 37% of the time 🎉. This is a 20% and 15% bump in accuracy respectively with a single training epoch.

![Image 35](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-05-at-10.46.47-AM.png)

Not too shabby for a couple function definitions and a relatively small dataset. The raw results from the 1.5B model can be explored here:

[ox/Rust/results/GRPO\_82\_2025-03-02\_22-49-17\_Qwen2.5-Coder-1.5B-Instruct/results\_code\_and\_tests.parquet at main This is a dataset of rust questions and generated code created to fine tune small language models on rust.. Contribute to the ox/Rust repository by creating an account on Oxen.ai ![Image 36](https://ghost.oxen.ai/content/images/icon/favicon-52.ico) ![Image 37](https://ghost.oxen.ai/content/images/thumbnail/file-17)](https://www.oxen.ai/ox/Rust/file/main/results/GRPO_82_2025-03-02_22-49-17_Qwen2.5-Coder-1.5B-Instruct/results_code_and_tests.parquet?ref=ghost.oxen.ai)

This is a pretty encouraging start. The training took a bit over 24hrs and cost < $100 on [Lambda Labs](https://lambdalabs.com/?ref=ghost.oxen.ai). Here's the cost per hour of an H100 for reference:

![Image 38](https://ghost.oxen.ai/content/images/2025/03/Screenshot-2025-03-05-at-4.19.22-PM.png)

The experiment shows that the GRPO algorithm is relatively accessible for anyone to define their own arbitrary reward functions, and get a substantial bump in performance even on a small model.

Next Up
-------

This task was pretty limiting to writing a single function with unit tests that pass. Ideally you would want your coding model to be able to complete a variety of use cases. We will be working on extending the dataset to have different categories of tasks:

*   ✅ Writing functions
*   ✅ Writing unit tests
*   Fixing errors from the compiler
*   Fill in the middle / autocomplete
*   Create a patch/diff given a prompt
*   Next edit (tab) prediction

If you have any others that you think would be interesting to add to this list, let us know! We are also going to be running experiments on larger models such as 3B and 8B to see how the performance compares.

Want More?
----------

This post is a part of a series called Arxiv Dives where we take research on [arxiv.org](http://arxiv.org/?ref=ghost.oxen.ai), cover it in a paper club, and see how well it works in practice on real world tasks. If you are interested in joining any of the live sessions, we do them over zoom on Fridays. We also have a bunch of recordings of past dives on YouTube.

[Oxen Oxen.ai is wicked fast versioning and collaboration tools for data. Even millions of unstructured images, we quickly handle any type of data so you can build cutting-edge AI. Arxiv Dives: Each week we dive deep into a topic in machine learning or general artificial intelligence research. The sessions are live with a group of smart Oxen every Friday. Create an account: www.oxen.ai and join the discussion: https://lu.ma/oxen ![Image 39](https://ghost.oxen.ai/content/images/icon/favicon_144x144-1.png)YouTube ![Image 40](https://ghost.oxen.ai/content/images/thumbnail/ckfvphazhPxipKaxEod9i707jTkYjrWHB1SUl-D2yvtgc6yvF3Pkatq8wm4VkeQxBX2EWhUPxQ-s900-c-k-c0x00ffffff-no-rj-1)](https://www.youtube.com/@oxen-ai?ref=ghost.oxen.ai)

Feel free to follow me on X (formerly Twitter) to get updates on any of this work.

[https://x.com/gregschoeninger](https://x.com/gregschoeninger?ref=ghost.oxen.ai)

And finally, if you are curious about fine-tuning your own models, feel free to reach out to [hello@oxen.ai](mailto:hello@oxen.ai). We’re happy to bring our expertise to your use case and give you guidance bringing AI in your product from idea to reality.

