---
title: Open-R1- Update 1
date: 2025-02-03
extra:
  source: https://huggingface.co/blog/open-r1/update-1
  original_title: Open-R1- Update 1
---
## Summary
**摘要**:
文章是关于Hugging Face团队发展与完整复制DeepSeek R1项目状态的更新。重点包括四个关键方面:进展、学习、社区和未来方向。

**要点总结**:

1. **进展**:
   - 成功复刻了DeepSeek R1评估数据,并得到与原始报告相同的结果。指出DeepSeek模型生成的回答极长,最长可达约20,000个词,在几十页,但这种特征看来在复刻过程中不影响整体的执行效率。
   - 评论者对DeepSeek R1使用自动生成的内容训练到什么程度有不同的见解,暗示仍在进行调查以弄清潜在的影响。

2. **学习**:
   - 指出复刻过程中可能遇到的问题,以及一些合理推断,例如针对可能从OpenAI获取训练数据的指称并没有对DeepSeek R1项目产生直接的负面结果。
   - 深入研究DeepSeek R1系统的背景及可能使用的硬件设施,以了解训练流程的潜在效率。

3. **社区**:
   - 大量的社区活动围绕着DeepSeek R1模型,包括制作实验项目摸索基本学习原理、构建新的合成数据集和对原始模型进行技术复刻和对比实验。
   - 项目包括微型实验,显示即使是较小的模型,也能复制深度学习的基本原理;利用基础模型3B构建了个人“AHA时刻”的实验;对7B数学模型进行了推理研究;以及打造一个多模式版本的R1模型,涉及图形提取等相关技术。

4. **未来方向**:
   - 目标是完成训练管道并尝试在较小的模型上运行,使用扩展的推理管道生成高质量的数据集。
   - 提供贡献者途径,通过Hugging Face开放源代码的GitHub仓库或加入特定的组织来贡献项目的发展。
## Full Content
Title: Open-R1: Update #1

URL Source: https://huggingface.co/blog/open-r1/update-1

Markdown Content:
[Back to Articles](https://huggingface.co/blog)

*   [Progress after 1 Week](https://huggingface.co/blog/open-r1/update-1#progress-after-1-week "Progress after 1 Week")
    *   [Evaluation](https://huggingface.co/blog/open-r1/update-1#evaluation "Evaluation")
        
    *   [Training Pipeline](https://huggingface.co/blog/open-r1/update-1#training-pipeline "Training Pipeline")
        
    *   [Synthetic Data Generation](https://huggingface.co/blog/open-r1/update-1#synthetic-data-generation "Synthetic Data Generation")
        
    *   [Outreach](https://huggingface.co/blog/open-r1/update-1#outreach "Outreach")
        
*   [What have we learned about DeepSeek-R1?](https://huggingface.co/blog/open-r1/update-1#what-have-we-learned-about-deepseek-r1 "What have we learned about DeepSeek-R1?")
    *   [Responses to R1](https://huggingface.co/blog/open-r1/update-1#responses-to-r1 "Responses to R1")
        
    *   [DeepSeek V3 Training Compute](https://huggingface.co/blog/open-r1/update-1#deepseek-v3-training-compute "DeepSeek V3 Training Compute")
        
    *   [Training Dataset](https://huggingface.co/blog/open-r1/update-1#training-dataset "Training Dataset")
        
*   [Community](https://huggingface.co/blog/open-r1/update-1#community "Community")
    *   [Projects](https://huggingface.co/blog/open-r1/update-1#projects "Projects")
        
    *   [Datasets](https://huggingface.co/blog/open-r1/update-1#datasets "Datasets")
        
*   [What's next?](https://huggingface.co/blog/open-r1/update-1#whats-next "What&#39;s next?")
    

[![Image 52: image/png](https://cdn-uploads.huggingface.co/production/uploads/5e48005437cb5b49818287a5/HVmAAo3Piw3nNnf8r88-d.png)](https://cdn-uploads.huggingface.co/production/uploads/5e48005437cb5b49818287a5/HVmAAo3Piw3nNnf8r88-d.png)

It’s been two weeks since the release of DeepSeek R1 and just a week since we started the [open-r1](https://github.com/huggingface/open-r1) project to replicate the missing pieces, namely the training pipeline and the synthetic data. This post summarizes:

*   the progress of Open-R1 to replicate the DeepSeek-R1 pipeline and dataset
*   what we learned about DeepSeek-R1 and discussions around it
*   cool projects the community has built since the release of DeepSeek-R1

It should serve both as an update on the project and as a collection of interesting resources around DeepSeek-R1.

[](https://huggingface.co/blog/open-r1/update-1#progress-after-1-week)Progress after 1 Week
-------------------------------------------------------------------------------------------

Let’s start by looking at the progress we made on Open-R1. We started Open-R1 just one week ago and people across the teams as well as the community came together to work on it and we have some progress to report.

### [](https://huggingface.co/blog/open-r1/update-1#evaluation)Evaluation

The first step in reproduction is to verify that we can match the evaluation scores. We are able to reproduce Deepseek's reported results on the MATH-500 Benchmark:

| Model | MATH-500 (HF lighteval) | MATH-500 (DeepSeek Reported) |
| --- | --- | --- |
| DeepSeek-R1-Distill-Qwen-1.5B | 81.6 | 83.9 |
| DeepSeek-R1-Distill-Qwen-7B | 91.8 | 92.8 |
| DeepSeek-R1-Distill-Qwen-14B | 94.2 | 93.9 |
| DeepSeek-R1-Distill-Qwen-32B | 95.0 | 94.3 |
| DeepSeek-R1-Distill-Llama-8B | 85.8 | 89.1 |
| DeepSeek-R1-Distill-Llama-70B | 93.4 | 94.5 |

You can find the instructions to run these evaluations in the [open-r1 repository](https://github.com/huggingface/open-r1?tab=readme-ov-file#reproducing-deepseeks-evaluation-results-on-math-500).

One observation we have made is the enormous size of the generations from the DeepSeek models, which makes even evaluating the model challenging. Here we show DeepSeek-R1 response lengths in the OpenThoughts dataset:

[![Image 53: Distribution of R1’s responses shows that they are on average very long with the average response being 6,000 tokens long and some responses containing more than 20,000 tokens. Worth noting that the average page contains ~500 words and one token is on average slightly less than a word, which means the many reponses are over 10 pages long. (src: [https://x.com/gui_penedo/status/1884953463051649052](https://x.com/gui_penedo/status/1884953463051649052))](https://cdn-uploads.huggingface.co/production/uploads/5e48005437cb5b49818287a5/9VTGYr3wg1jZHw9uviB6j.png)](https://cdn-uploads.huggingface.co/production/uploads/5e48005437cb5b49818287a5/9VTGYr3wg1jZHw9uviB6j.png)

Distribution of R1’s responses shows that they are on average very long with the average response being 6,000 tokens long and some responses containing more than 20,000 tokens. Worth noting that the average page contains ~500 words and one token is on average slightly less than a word, which means the many reponses are over 10 pages long. (src: [https://x.com/gui\_penedo/status/1884953463051649052](https://x.com/gui_penedo/status/1884953463051649052))

The length of responses will make GPRO training challenging, as we will have to generate long completions which will require a significant proportion of GPU memory to store the activations / gradients for the optimization step.

In order to share our progress publicly, we have created an open-r1 evaluation leaderboard, so the community can follow our reproduction efforts (space is [here](https://huggingface.co/spaces/open-r1/open-r1-eval-leaderboard)):

### [](https://huggingface.co/blog/open-r1/update-1#training-pipeline)Training Pipeline

Following the release of Open R1, GRPO (Grouped Relative Policy Optimization) was integrated into the latest TRL release ([version 0.14](https://x.com/QGallouedec/status/1884978284686905468)). This integration enables training any model with one or multiple reward functions or models. The GRPO implementation integrates with DeepSpeed ZeRO 1/2/3 for parallelized training that scales to many GPUs, and uses vLLM for fast generation, which is the primary bottleneck in online training methods.

```
from datasets import load_dataset
from trl import GRPOConfig, GRPOTrainer

dataset = load_dataset("trl-lib/tldr", split="train")

# Dummy reward: rewards completions that are close to 20 characters
def reward_len(completions, **kwargs):
    return [-abs(20 - len(completion)) for completion in completions]

training_args = GRPOConfig(output_dir="Qwen2-0.5B-GRPO", logging_steps=10)
trainer = GRPOTrainer(
    model="Qwen/Qwen2-0.5B-Instruct",
    reward_funcs=reward_len,
    args=training_args,
    train_dataset=dataset,
)
trainer.train()
```

There are still some limitations relating to the use of high memory usage, and progress is being made to profile and reduce them.

### [](https://huggingface.co/blog/open-r1/update-1#synthetic-data-generation)Synthetic Data Generation

One of the most exciting findings of the R1 report was that the main model can be used to generate synthetic reasoning traces and smaller models fine-tuned on this dataset see similar performance gains as the main model. So naturally we want to re-create the synthetic reasoning dataset as well such that the community can fine-tune other models on it.

With a model as big as R1 the main challenge is scaling up generation efficiently and fast. We spent a week tinkering with various setups and configurations.

The model fits on two 8xH100 nodes so naturally we started experimenting with that setup and used vLLM as inference server. However, we quickly noticed that this configuration is not ideal: the throughput is sub-optimal and only allows for 8 parallel request, because the GPU KV cache fills up too quickly. What happens when the cache fills up ist that the requests which use a lot of cache are preempted and if the config uses `PreemptionMode.RECOMPUTE` the requests are scheduled again later when more VRAM is available.

We then switched to a setup with 4x 8xH100 nodes, so 32 GPUs in total. This leaves enough spare VRAM for 32 requests running in parallel with barely any of them getting rescheduled due to 100% cache utilization.

Originally we started querying the vLLM servers with batches of requests but noticed quickly, that straggles in the batches would cause the GPU utiliziation to vary since a new batch would only start processing once the last sample of the previous batch is done. Switching the batched inference to streaming helped stabilize the GPU utilization significantly:

[![Image 54: image/png](https://cdn-uploads.huggingface.co/production/uploads/5e48005437cb5b49818287a5/37qSDNV_r9lefG9KA54hD.png)](https://cdn-uploads.huggingface.co/production/uploads/5e48005437cb5b49818287a5/37qSDNV_r9lefG9KA54hD.png)

It only required changing the code sending requests to the vLLM servers. The code for batched inference:

```
# send requests in batches of 500
for batch in batch_generator(dataset, bs=500):
    active_tasks = []
    for row in batch:
        task = asyncio.create_task(send_requests(row))
        active_tasks.add(task)
    if active_tasks:
        await asyncio.gather(*active_tasks)
```

The new code for streaming requests:

```
active_tasks = []
for row in dataset:
    # keep the total active requests under 500
    while len(active_tasks) >= 500:
        done, active_tasks = await asyncio.wait(
            active_tasks,
            return_when=asyncio.FIRST_COMPLETED
        )

    task = asyncio.create_task(send_requests(row))
    active_tasks.add(task)

# wait for all remaining tasks to complete
if active_tasks:
    await asyncio.gather(*active_tasks)
```

We are generating at a fairly constant rate but might still explore a bit further if for example switching to the CPU cache is a better strategy when long queries get preempted.

The current inference code can be found [here](https://gist.github.com/anton-l/7e3bcfd0cd3847af44c61b9963107de0).

### [](https://huggingface.co/blog/open-r1/update-1#outreach)Outreach

There has been wide interest in open-r1, including from the media so various team members have been in the news in the past week:

*   Lewis was live (!) on CNN: [https://x.com/\_lewtun/status/1884377909038833894?s=46](https://x.com/_lewtun/status/1884377909038833894?s=46)
*   Thom appeared on Bloomberg: [https://x.com/Thom\_Wolf/status/1884353433865777520](https://x.com/Thom_Wolf/status/1884353433865777520)
*   Leandro chatted on NPR’s Money Planet (at ~21min): [https://www.npr.org/2024/11/29/1215793948/deepseek-ai-china-us-semiconductors-stock-nvidia](https://www.npr.org/2024/11/29/1215793948/deepseek-ai-china-us-semiconductors-stock-nvidia)

Other mentions: [Washington Post](https://www.washingtonpost.com/technology/2025/01/28/deepseek-ai-china-us-trump/), [Financial Times](https://www.msn.com/en-gb/technology/artificial-intelligence/china-s-emboldened-ai-industry-releases-flurry-of-model-updates/ar-AA1xZbTE?ocid=BingNewsVerp), [Financial Times](https://www.ft.com/content/757950e1-a81d-4c66-983e-1cf333262d66), [Fortune](https://www.msn.com/en-us/technology/artificial-intelligence/deepseek-isn-t-china-s-only-new-ai-model-and-analysts-are-calling-the-flurry-of-new-applications-a-coordinated-psyops/ar-AA1xZqi4?ocid=BingNewsVerp), [Fortune](https://fortune.com/2025/01/27/deepseek-just-flipped-the-ai-script-in-favor-of-open-source-and-the-irony-for-openai-and-anthropic-is-brutal/), [The Verge](https://www.theverge.com/ai-artificial-intelligence/598846/deepseek-big-tech-ai-industry-nvidia-impac), [Financial Review](https://www.afr.com/technology/why-the-deepseek-breakthrough-is-actually-a-good-thing-20250128-p5l7pn), [Tech Crunch](https://techcrunch.com/2025/01/28/hugging-face-researchers-are-trying-to-build-a-more-open-version-of-deepseeks-ai-reasoning-model/), [Die Zeit](https://www.zeit.de/digital/internet/2025-01/deepseek-kuenstliche-intelligenz-startup-china-sprachmodell/seite-2), [Financial Times](https://www.ft.com/content/ea803121-196f-4c61-ab70-93b38043836e), [New York Times](https://www.nytimes.com/2025/01/29/technology/deepseek-ai-startups-venture-capital.html), [The Wall Street Journal](https://www.wsj.com/articles/how-deepseeks-ai-stacks-up-against-openais-model-e938c3d6), [EuroNews](https://uk.news.yahoo.com/deepseek-wake-call-europe-ai-150850807.html), [Barrons](https://www.barrons.com/news/behind-ai-makers-claims-to-share-open-source-models-8e8b8b8a), [New York Times](https://www.nytimes.com/2025/01/29/technology/meta-deepseek-ai-open-source.html), [Vox](https://www.vox.com/technology/397330/deepseek-openai-chatgpt-gemini-nvidia-china), [Nature](https://www.nature.com/articles/d41586-025-00259-0), [SwissInfo](https://www.swissinfo.ch/eng/science/switzerland-caught-in-middle-of-us-china-race-for-ai-dominance/88804566), [Handelsblatt](https://www.handelsblatt.com/technik/ki/kuenstliche-intelligenz-durchbruch-oder-hype-so-innovativ-ist-deepseek/100094406.html), [Business Insider](https://www.businessinsider.com/deepseek-r1-open-source-replicate-ai-west-china-hugging-face-2025-1), [IEEE Spectrum](https://spectrum.ieee.org/deepseek), [MIT Tech Review](https://www.technologyreview.com/2025/01/31/1110740/how-deepseek-ripped-up-the-ai-playbook-and-why-everyones-going-to-follow-it/), [LeMonde](https://www.lemonde.fr/en/opinion/article/2025/01/31/behind-deepseek-and-the-paris-summit-lies-the-challenge-of-open-and-economical-artificial-intelligence_6737615_23.html).

[](https://huggingface.co/blog/open-r1/update-1#what-have-we-learned-about-deepseek-r1)What have we learned about DeepSeek-R1?
------------------------------------------------------------------------------------------------------------------------------

While the community is still digesting DeepSeek-R1’s results and report, DeepSeek has captured broader public attention just two weeks after its release.

### [](https://huggingface.co/blog/open-r1/update-1#responses-to-r1)Responses to R1

After a relatively calm first week post-release, the second week saw significant market reactions, prompting responses from multiple AI research labs:

*   Stock market took a hit on Monday but stabilized or recovered in the days that followed: [https://x.com/KobeissiLetter/status/1883831022149927352](https://x.com/KobeissiLetter/status/1883831022149927352)
*   Sam Altman, CEO of OpenAI, congratulated DeepSeek and announced that they’ll move up the timeline to release some new things soon: [https://x.com/sama/status/1884066337103962416](https://x.com/sama/status/1884066337103962416)
*   Mark Chen, Chief Research Officer of OpenAI, commented on how DeepSeek discovered similar ideas as the ones OpenAI used for o1: [https://x.com/markchen90/status/1884303237186216272](https://x.com/markchen90/status/1884303237186216272)
*   Dario Amodei, CEO of Anthropic, used the occasion to double down on export controls, painting a picture of a bi-polar or uni-polar world: [https://x.com/DarioAmodei/status/1884636410839535967](https://x.com/DarioAmodei/status/1884636410839535967)

In parallel, several companies worked on providing the DeepSeek models through various platforms (non-exhaustive list):

*   Dell: In partnership with Hugging Face, Dell CEO & Founder, Michael Dell, announced an on-premise solution to run DeepSeek-R1: [https://x.com/MichaelDell/status/1884677233014398994](https://x.com/MichaelDell/status/1884677233014398994)
*   AWS: Amazon CEO Andy Jassy announced DeepSeek-R1 is now available on Amazon BedRock & SageMaker: [https://x.com/ajassy/status/1885120938813120549](https://x.com/ajassy/status/1885120938813120549)
*   Hyperbolic AI: [https://hyperbolic.xyz/blog/deepseek-r1-now-hosted-on-hyperbolic](https://hyperbolic.xyz/blog/deepseek-r1-now-hosted-on-hyperbolic)
*   Together AI: [https://x.com/togethercompute/status/1882110120274088278](https://x.com/togethercompute/status/1882110120274088278)
*   Fireworks AI: [https://fireworks.ai/models/fireworks/deepseek-r1](https://fireworks.ai/models/fireworks/deepseek-r1)

### [](https://huggingface.co/blog/open-r1/update-1#deepseek-v3-training-compute)DeepSeek V3 Training Compute

There has been a lot of interest around the proclaimed cost of training V3/R1. While the exact number probably doesn’t matter so much, people worked on some back-of-the-envelope calculations to verify the order of magnitude here. TL;DR the numbers seem generally in the right order of magnitude, as seen in these discussions:

*   Tom Goldstein, professor at the University of Maryland: [https://x.com/tomgoldsteincs/status/1884651376854122774](https://x.com/tomgoldsteincs/status/1884651376854122774)
*   Reiner Pope, founder of MatX, compares Llama3 to DeepSeek V3 [https://x.com/reinerpope/status/1884056274893168896](https://x.com/reinerpope/status/1884056274893168896)
*   Lukas Beyer, OpenAI ex-Google Brain/DeepMind, with discussions about the origin of MFU: [https://x.com/giffmana/status/1884160434846224688](https://x.com/giffmana/status/1884160434846224688)
*   SemiAnalysis put out a report speculating about the infrastructure available to DeepSeek: [https://x.com/SemiAnalysis\_/status/1885192148037112023](https://x.com/SemiAnalysis_/status/1885192148037112023)

As many groups are working on reproducing the training pipeline, we’ll get more evidence on the possible training efficiency for the model.

### [](https://huggingface.co/blog/open-r1/update-1#training-dataset)Training Dataset

Last week some speculations surfaced that DeepSeek might have been using OpenAI outputs to train its models. See for example the [Financial Times](https://www.ft.com/content/a0dfedd1-5255-4fa9-8ccc-1fe01de87ea6). However, it is unclear at this point what the consequences of these allegations will be.

[](https://huggingface.co/blog/open-r1/update-1#community)Community
-------------------------------------------------------------------

The open source community has been extremely active around DeepSeek-R1 and many people started building interesting projects around the model.

### [](https://huggingface.co/blog/open-r1/update-1#projects)Projects

There have been a number of projects that try to reproduce the basic learning mechanics at smaller scale, so you can test the basic learning principles at home.

*   [Will Brown showed](https://x.com/willccbb/status/1883414339518148960) that you can use the [GRPO Trainer in TRL](https://huggingface.co/docs/trl/main/en/grpo_trainer) to reproduce a minimal training curve with Llama 1B.
*   [TinyZero](https://github.com/Jiayi-Pan/TinyZero) shows that with <30$ and a 3B base model you can experience the [“ahah”-moment](https://x.com/jiayi_pirate/status/1882839370505621655) yourself!
*   Philipp Schmid also released a [tutorial](https://www.philschmid.de/mini-deepseek-r1) on Mini-R1, again showing how to reproduce the “aha” moment.
*   At a bigger model scale, researchers at HKUST released a [blogpost](https://hkust-nlp.notion.site/simplerl-reason) showing the emergence of reasoning with a 7B math model.
*   Folks at the Evolving LLM lab have started working on a multimodal version of R1: [https://github.com/EvolvingLMMs-Lab/open-r1-multimodal](https://github.com/EvolvingLMMs-Lab/open-r1-multimodal)
*   [Stepanov](https://huggingface.co/Ihor) started working using R1 to extract graphs from text: [https://huggingface.co/blog/Ihor/replicating-deepseek-r1-for-information-extraction](https://huggingface.co/blog/Ihor/replicating-deepseek-r1-for-information-extraction)

### [](https://huggingface.co/blog/open-r1/update-1#datasets)Datasets

The community has been busy on a number of dataset efforts related to R1, some highlights include:

*   [bespokelabs/Bespoke-Stratos-17k](https://huggingface.co/datasets/bespokelabs/Bespoke-Stratos-17k): is a replication of the [Berkeley Sky-T1](https://novasky-ai.github.io/posts/sky-t1/) data pipeline which uses DeepSeek-R1 to create a dataset of questions, reasoning traces and answers. This data was subsequently used to fine-tune 7B and 32B Qwen models using a distillation approach similar to the R1 paper.
*   [open-thoughts/OpenThoughts-114k](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k): an "Open synthetic reasoning dataset with 114k high-quality examples covering math, science, code, and puzzles". Part of the Open Thoughts effort.
*   [cognitivecomputations/dolphin-r1](https://huggingface.co/datasets/cognitivecomputations/dolphin-r1): 800k sample dataset with completions from DeepSeek-R1, Gemini flash and 200k samples from Dolphin chat with the goal of helping train R1 style models.
*   [ServiceNow-AI/R1-Distill-SFT](https://huggingface.co/datasets/ServiceNow-AI/R1-Distill-SFT): Currently at 17,000 samples, an effort by the ServiceNow Language Models lab to create data to support Open-R1 efforts.
*   [NovaSky-AI/Sky-T1\_data\_17k](https://huggingface.co/datasets/NovaSky-AI/Sky-T1_data_17k): A dataset used to train Sky-T1-32B-Preview. This dataset was part of a fairly early effort to replicate o1 style reasoning. The model trained on this dataset was trained for less than $450. This [blog post](https://novasky-ai.github.io/posts/sky-t1/) goes into more detail.
*   [Magpie-Align/Magpie-Reasoning-V2-250K-CoT-Deepseek-R1-Llama-70B](https://huggingface.co/datasets/Magpie-Align/Magpie-Reasoning-V2-250K-CoT-Deepseek-R1-Llama-70B): This dataset extends [Magpie](https://huggingface.co/papers/2406.08464) and approach to generating instruction data without starting prompts to include reasoning in the responses. The instructions are generated by Llama 3.1 70B Instruct and Llama 3.3 70B Instruct, and the responses are generated by DeepSeek-R1-Distill-Llama-70B

This list only covers a small number of reasoning and problem solving related datasets on the Hub. We’re excited to see what other datasets the community build in the coming weeks.

[](https://huggingface.co/blog/open-r1/update-1#whats-next)What's next?
-----------------------------------------------------------------------

We are just getting started and want to finish the training pipeline and try it on smaller models and use the scaled up inference pipeline to generate high quality datasets. If you want to contribute check out the [open-r1 repository on GitHub](https://github.com/huggingface/open-r1) or follow the [Hugging Face open-r1 org](https://huggingface.co/open-r1).

