Title: Long-context GRPO (R1 Reasoning)

URL Source: https://unsloth.ai/blog/grpo

Markdown Content:
Long-context GRPO

Feb 20, 2025 • By Daniel & Michael
----------------------------------

Feb 20, 2025
------------

•
-

By Daniel & Michael
-------------------

You can now train your own reasoning model with just **5GB VRAM** for Qwen2.5 (1.5B) - down from 7GB in our previous GRPO release 2 weeks ago!Currently, achieving longer context lengths is one of GRPO's biggest challenges. Our newly derived Unsloth Efficient GRPO algorithm enables **_10x longer context_** lengths while using **_90% less VRAM_** vs. all other GRPO LoRA/QLoRA implementations, even those utilizing Flash Attention 2 (FA2).

With a GRPO setup using TRL + FA2, Llama 3.1 (8B) training at 20K context length demands 510.8GB of VRAM. However, Unsloth’s 90% VRAM reduction brings the requirement down to just 54.3GB in the same setup.

Try our free GRPO notebook with 10x longer context: [Llama 3.1 (8B) on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-GRPO.ipynb)  
We'd highly recommend reading [our Guide](https://docs.unsloth.ai/basics/reasoning-grpo-and-rl) for everything on GRPO + reward functions/verifiers.  
View our GRPO notebooks featuring other models like Phi-4 [here](https://docs.unsloth.ai/).

❤️ P.S. If you enjoyed our work, don't forget to ⭐Star us: [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth)

🦥 90% less VRAM for long context

When you’re using Unsloth to do GRPO, we smartly reduce VRAM usage by over 90% when compared to standard implementations with Flash Attention 2 by using multiple tricks! On 20K context lengths for example with 8 generations per prompt, Unsloth uses only **54.3GB of VRAM for Llama 3.1 8B**, whilst standard implementations take **510.8GB (90% less for Unsloth)**.

*   Our new memory efficient linear algorithm for GRPO slashes memory usage by 8x or more. **_This shaves 68.5GB of memory_****,** whilst being actually faster through the help of torch.compile for num\_generations = 8 and 20K context length.
*   We leverage our smart [Unsloth gradient checkpointing](https://unsloth.ai/blog/long-context) algorithm which we released a while ago. It smartly offloads intermediate activations to system RAM asynchronously whilst being only 1% slower. **_This shaves a whopping 372GB VRAM_** since we need num\_generations = 8. We can reduce this memory usage even further through intermediate gradient accumulation.
*   Unsloth also uses the same GPU / CUDA memory space as the underlying inference engine (vLLM), unlike implementations in other packages. **This shaves 16GB of VRAM**.

| Metric | 🦥 Unsloth | TRL + FA2 |
| --- | --- | --- |
| Training Memory Cost (GB) | 42GB | 414GB |
| GRPO Memory Cost (GB) | 9.8GB | 78.3GB |
| Inference Cost (GB) | 0GB | 16GB |
| Inference KV Cache for 20K context (GB) | 2.5GB | 2.5GB |
| Total Memory Usage | 54.3GB (90% less) | 510.8GB |

In typical standard GRPO implementations, you need to create 2 logits of size (8, 20K) to calculate the GRPO loss. This takes 2 \* 2 bytes \* 8 (num generations) \* 20K (context length) \* 128256 (vocabulary size) = 78.3GB in VRAM.Unsloth shaves 8x memory usage for long context GRPO, so we need only an extra 9.8GB in extra VRAM for 20K context lengths!

We also need to from the KV Cache in 16bit. Llama 3.1 8B has 32 layers, and both K and V are 1024 in size. So memory usage for 20K context length = 2 \* 2 bytes \* 32 layers \* 20K context length \* 1024 = 2.5GB per batch. We would set the batch size for vLLM to 8, but we shall leave it at 1 for our calculations to save VRAM. Otherwise you will need 20GB for the KV cache.

🦥 Unsloth Efficient GRPO algorithm

We got inspired from Horace [He’s linear cross entropy](https://gist.github.com/Chillee/22cd93e11b887db1f596ab754d60a899) implementation, and managed to make it work for GRPO! We actually found a few surprising points:

*   The reference GRPO implementation uses the reverse KL divergence, not the forward KL divergence.
*   Naively implementing linear cross entropy on float16 mixed precision (and also float8) with automatic mixed precision scaling mechanisms will break if not handled properly.
*   We found other quirks in terms of the implementation of the GRPO loss - primarily in terms of the formulation of the reverse KL divergence.

💡 Maths of GRPO & Issues Found

GRPO was first introduced in [DeepSeek’s Math paper](https://arxiv.org/abs/2402.03300) back in February 2024 to April 2024 DeepSeek then leveraged the GRPO algorithm in creating DeepSeek R1, as mentioned in their [paper](https://arxiv.org/abs/2501.12948).We leverage Hugging Face’s TRL GRPO implementation [here](https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_trainer.py). We see that the TRL implementation performs:

L \= 1 n ⁢ ∑ β ⁢ D KL ⁢ ( q ‖ p ) + A L = \\frac{1}{n}\\sum{\\beta D\_{\\text{KL}}}\\big( q \\,\\|\\, p \\big) + A

where we utilize the **reverse KL divergence** (not the forward KL divergence). Beta is a scaling factor set to 0.04, and A is the advantages obtained after considering all reward functions.Q is the new trained model, and P is the original reference model.We then notice interestingly that the implementation calculates the reverse KL divergence as:

p \= σ ⁡ ( f ⁡ ( x ) ) q \= σ ⁡ ( f ′ ⁡ ( x ) ) D KL ⁢ ( q ‖ p ) i \= exp ⁡ ( log ⁡ ( p ) − log ⁡ ( q ) ) − ( log ⁡ ( p ) − log ⁡ ( q ) ) − 1 \= exp ⁡ ( l ⁢ o ⁢ g ⁡ ( p q ) ) − l ⁢ o ⁢ g ⁡ ( p q ) − 1 \= p q − l ⁢ o ⁢ g ⁡ ( p q ) − 1 \\begin{align} p &\= \\sigma (f(x)) \\\\ q &\= \\sigma (f'(x)) \\\\ D\_{\\text{KL}}\\big( q \\,\\|\\, p \\big)\_i &\= \\exp(\\log(p)-\\log(q))-(\\log(p)-\\log(q)) - 1 \\\\ &\= \\exp\\bigg(log\\bigg(\\frac{p}{q}\\bigg)\\bigg)-log\\bigg(\\frac{p}{q}\\bigg) - 1 \\\\ &\= \\frac{p}{q} - log\\bigg(\\frac{p}{q}\\bigg) - 1 \\end{align}

But is this actually correct? We first try to derive it, and collect like terms:

D KL ⁡ ( q ‖ p ) \= ∑ q ⁢ \[ p q − log ⁡ ( p q ) − 1 \] \= ∑ q ⁢ p q − ∑ q ⁢ log ⁡ ( p q ) − ∑ q \= ∑ p − ∑ q ⁢ log ⁡ ( p q ) − 1 \= 1 − ∑ q ⁢ log ⁡ ( p q ) − 1 \= − ∑ q ⁢ log ⁡ ( p q ) D KL ⁡ ( q ‖ p ) \= ∑ q ⁢ log ⁡ ( q p ) \\begin{align} D\_{\\text{KL}}\\big( q \\,\\|\\, p \\big) &\= \\sum q \\bigg\[ \\frac{p}{q} - \\log{\\bigg(\\frac{p}{q}\\bigg)} - 1 \\bigg\] \\\\ &\= \\sum q \\frac{p}{q} - \\sum q \\log{\\bigg(\\frac{p}{q}\\bigg)} - \\sum q \\\\ &\= \\sum p - \\sum q \\log{\\bigg(\\frac{p}{q}\\bigg)} - 1 \\\\ &\= 1 - \\sum q \\log{\\bigg(\\frac{p}{q}\\bigg)} - 1 \\\\ &\= - \\sum q \\log{\\bigg(\\frac{p}{q}\\bigg)} \\\\ D\_{\\text{KL}}\\big( q \\,\\|\\, p \\big) &\= \\sum q \\log{\\bigg(\\frac{q}{p}\\bigg)} \\\\ \\end{align}

So what this means is that the implementation might be missing a multiplication by the Q (new distribution term)?But this seems to be correct as seen in the DeepSeek Math paper which first introduced GRPO on [page 14](https://arxiv.org/pdf/2402.03300). Likewise John [Schulman's blog](http://joschu.net/blog/kl-approx.html) also says that an unbiased estimator for the reverse KL term in fact does not need the extra Q term. We see in the blog that:

r \= p ⁡ ( x ) q ⁡ ( x ) KL ⁡ \[ q , p \] \= ( r − 1 ) − log ⁡ r \= p q − 1 − log ⁡ p q \\begin{align} r &\= \\frac{p(x)}{q(x)} \\\\ \\text{KL}\[q, p\] &\= (r-1)-\\log{r} \\\\ &\= \\frac{p}{q} - 1 - \\log{\\frac{p}{q}} \\end{align}

We also found interestingly that:```
torch.exp(q - q.detach()) * advantages.unsqueeze(1)
```Is used, which should be evaluated to 1 right?  
We actually found this is necessary - it seems that the autograd engine might not be propagating gradients correctly.So we perform 4 experiments:

*   Do normal GRPO via reference implementation (red line)
*   Remove detach code (blue line)
*   Full reverse KL with an extra term as discussed before (yellow line)
*   Forward KL divergence instead (green line)![Image 1](https://unsloth.ai/cgi/image/Different_KL_Divergences(1)_-fz9M74jz3VBJn9qGHe1u.svg?width=2048&quality=80&format=auto)

In general, removing detach definitely breaks all training, so we must leave it there - this will most likely need more investigation. It seems like all other implementations seem similar? We might need to run the model for longer to see different effects maybe.In all implementations, we also utilize the logsumexp trick:

log ⁡ σ ⁡ ( x ) \= log ⁡ exp ⁡ ( x ) ∑ exp ⁡ ( x ) \= x − log ⁡ ∑ exp ⁡ ( x ) \= x − logsumexp ⁡ ( x ) \\begin{align} \\log\\sigma(x) = \\log{\\frac{\\exp(x)}{\\sum{\\exp(x)}}} &\= x - \\log\\sum{\\exp(x)} \\\\ &\= x - \\text{logsumexp}(x) \\end{align}

📈 Full Logging for GRPO

We also provide full logging details for all reward functions now! Previously we only showed the total aggregated reward function itself.![Image 2](https://unsloth.ai/cgi/image/Screenshot_2025-02-20_at_04-52-52_Copy_of_Yet_another_copy_of_Llama3.1_(8B)-GRPO.ipynb_-_Colab_5lpAL05rCEjw67tij45ua.png?width=3840&quality=80&format=auto)You also do not need to call functions to patch GRPO anymore! I.e. remove this at the top (we do it automatically):```
from unsloth import PatchFastRL
PatchFastRL("GRPO", FastLanguageModel)
```

🖥️ vLLM inference options

We also now allow you to use FP8 KV caches for vLLM, which allows for 2x less KV cache space usage on newer GPUs (RTX 3090, A100 and newer)```
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "meta-llama/meta-Llama-3.1-8B-Instruct",
    max_seq_length = max_seq_length,
    load_in_4bit = True, # False for LoRA 16bit
    fast_inference = True, # Enable vLLM fast inference
    max_lora_rank = lora_rank,
    gpu_memory_utilization = 0.6, # Reduce if out of memory
    float8_kv_cache = True, # Enable float8 KV cache
)
```If you want to use min\_p = 0.1, or other sampling params in vLLM, we also support passing anything in vLLM’s SamplingParams arguments!```
max_prompt_length = 256
from trl import GRPOConfig, GRPOTrainer
from unsloth import vLLMSamplingParams
vllm_sampling_params = vLLMSamplingParams(
    min_p = 0.1,
    seed = 3407,
    ...
)
training_args = GRPOConfig(
    ...
    vllm_sampling_params = vllm_sampling_params,
    temperature = 1.5,
)
```

✨ Other Updates

🦥 Run Unsloth Dynamic 4-bit directly with vLLM
-----------------------------------------------

You can now run and do inference with our dynamic quants directly in vLLM. This was due to an [accepted PR](https://github.com/vllm-project/vllm/pull/12974) we did for the vLLM repo. Read how our dynamic quants greatly increase accuracy than standard 4-bit with examples and benchmarks [here](https://unsloth.ai/blog/dynamic-4bit).

🚀 Run Perplexity's R1-1776
---------------------------

You also now download our [R1-1776 Dynamic GGUFs](https://huggingface.co/unsloth/r1-1776-GGUF) for Perplexity AI’s new R1-1776 model which is a finetune of DeepSeek-R1 that removes all censorship whilst maintaining reasoning capabilities. Run them locally on your own device!

🐱 GitHub Universe Interview
----------------------------

In October during GitHub's 2024 Universe, we did a wonderful interview with Andrea and now the video is out! We talk about our backgrounds from Australia, how we built Unsloth, how amazing all of you are and more! [Watch on YouTube](https://www.youtube.com/watch?v=lyVxD0bJDOk)

💕 Thank you!

Thank you to [Eyera](https://huggingface.co/Orenguteng), [Edd](https://github.com/Erland366) and [Keith](https://www.linkedin.com/feed/update/urn:li:activity:7290108099607097344/) for once again helping us with this release. A huge thank you to everyone for using & sharing Unsloth - we really appreciate it. 🙏As always, be sure to join our [Reddit page](https://www.reddit.com/r/unsloth/) and [Discord](https://discord.gg/unsloth) server for help or just to show your support! You can also follow us on [Twitter](https://twitter.com/unslothai) and [newsletter](https://unsloth.ai/newsletter).

Thank you for reading!

Daniel & Michael Han 🦥  
20 Feb 2025
