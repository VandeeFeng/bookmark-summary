---
title: Run DeepSeek-R1 Dynamic 1.58-bit
date: 2025-01-28
extra:
  source: https://unsloth.ai/blog/deepseekr1-dynamic
  original_title: Run DeepSeek-R1 Dynamic 1.58-bit
---
## Summary
**摘要**：
本文由Daniel & Michael撰写，标题为《Run DeepSeek R1 Dynamic 1.58-bit》，介绍了作者如何将DeepSeek-R1的参数模型大小从720GB削减到131GB，同时保持非常合理的性能。通过动态量化特定层为更高位数（如4位），同时让大部分MoE层保持在1.5位，作者成功在GPU（如2xH100 80GB）上实现快速推理并达到约每秒140个令牌的性能。提供了一个高性价比的模型版本，并在模型官网上免费供用户下载。因此，这篇博文主要关注的模型详细参数、性能测试、量化方法、模型构建及部署指南，以及一个用于验证模型功能的示例游戏。

**要点总结**：
- **模型压缩**：通过动态量化技术，DeepSeek-R1模型大小显著缩减至131GB，同时保持高精度性能。
- **加速推理**：模型在160GB VRAM场景下可实现快速推理，速度可达每秒140个令牌。
- **多种量化版本**：提供了不同大小（131GB到212GB）的动态量化版本以适应不同硬件环境，绑定器支持包括Ollama、vLLM等。
- **性能评估**：通过Flappy Bird游戏任务对模型的量化版本进行评估，并与原始模型性能进行了对比，表现出优良的稳定性及创意输出。
- **模型使用指南**：提供从安装到运行和部署的完整指引，包括GPU利用策略及不同大小模型在不同硬件条件下最佳配置。

安排清晰、全面的部署流程，配合深入的技术解析，使不同资源条件的用户均能高效利用DeepSeek-R1的动态1.58位版本。
## Full Content
Title: Run DeepSeek-R1 Dynamic 1.58-bit

URL Source: https://unsloth.ai/blog/deepseekr1-dynamic

Markdown Content:
Run DeepSeek R1  
Dynamic 1.58-bit

Jan 27, 2025 • By Daniel & Michael
----------------------------------

Jan 27, 2025
------------

•
-

By Daniel & Michael
-------------------

DeepSeek-R1 has been making waves recently by rivaling OpenAI's O1 reasoning model while being fully open-source. We explored how to enable more local users to run it and managed to quantize DeepSeek’s R1 671B parameter model to 131GB in size, a **80% reduction** in size from the original 720GB, whilst being very functional.By studying DeepSeek R1’s architecture, we managed to selectively quantize certain layers to higher bits (like 4bit), and leave most MoE layers (like those used in GPT-4) to 1.5bit (see [Unsloth Dynamic 4-bit](https://unsloth.ai/blog/dynamic-4bit)). Naively quantizing all layers breaks the model entirely, causing endless loops and gibberish outputs. Our dynamic quants solve this.

The 1.58bit quantization should fit in 160GB of VRAM for fast inference (2x H100 80GB), with it attaining around **140 tokens per second**. You don't need VRAM (GPU) to run 1.58bit R1, just 20GB of RAM (CPU) will work however it maybe slow. For optimal performance, we recommend the sum of VRAM + RAM to be at least 80GB+.

We uploaded dynamic quantized versions ranging from 131GB to 212GB in size to: [huggingface.co/unsloth/DeepSeek-R1-GGUF](https://huggingface.co/unsloth/DeepSeek-R1-GGUF)

P.S. if you liked our work, feel free to ⭐Star us: [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth) or follow us on X [@UnslothAi](https://x.com/unslothai) 💖

🦥 1. Dynamic Quantized versions

We provide 4 dynamic quantized versions. The first 3 uses an importance matrix to calibrate the quantization process (imatrix via llama.cpp) to allow lower bit representations. The last 212GB version is a general 2bit quant with no calibration.

These instructions work for the R1 distilled and non distilled models, however keep in mind that they will require different hardware requirements. See further below for R1 requirements.

📊 2. Benchmarks and ablations

To test all quantized models, instead of relying on general benchmarks, we instead ask DeepSeek r1 to create a Flappy Bird game with 3 tries (pass@3), and we score it on 10 criteria (like using random colors, random shapes, whether it can run in an Python interpreter). We used seed 3407, 3408 and 3409, and the suggested temperature of 0.6.On the left, we have an example of what [chat.deepseek.com](https://chat.deepseek.com/) generated. On the right is the 1.58bit version.

DeepSeek Original
-----------------

![Image 18](https://unsloth.ai/cgi/image/InShot_20250127_043158375_H8Uu6tyJXYAFwUEIu04Am.gif?width=1080&quality=80&format=auto)

1.58-bit Version
----------------

![Image 19](https://unsloth.ai/cgi/image/InShot_20250127_042648160_lrtL8-eRhl4qtLaUDSU87.gif?width=1080&quality=80&format=auto)

We see surprisingly that our dynamic 1.58bit version seems to still produce valid output!  
However, if you DO NOT use our dynamic 1.58bit version and instead naively quantize all layers, you will get infinite repetitions like in seed 3407: “Colours with dark Colours with dark Colours with dark Colours with dark Colours with dark” or in seed 3408: “Set up the Pygame's Pygame display with a Pygame's Pygame's Pygame's Pygame's Pygame's Pygame's Pygame's Pygame's Pygame's”.Similarly, if you do not use our dynamic version, and instead quantize all layers to 1.75bits (149GB), infinite repetitions stop, but the result is totally incorrect. All output produces fully black screens. If you quantize all layers to even 2.06bits (175GB), the result is even worse than the 1.58bit (131GB) dynamic quant. You would rather use the 2.22bit (183GB) version which is superior in performance.

The 1.58bit dynamic quants does sometimes rarely produce 1 incorrect token per 8000 tokens, which we need to comment out. Using [min\_p = 0.1](https://arxiv.org/abs/2407.01082) or 0.05 should mitigate the 1.58bit from generating singular incorrect tokens.

For a summary for a score out of 10 and Pass@3, we get:

| Model Size | Dynamic Quant | Model Size | Basic Quant |
| --- | --- | --- | --- |
| 131GB | 6.92 | 133GB | 0 |
| 158GB | 9.08 | 149GB | 1.67 |
| 183GB | 9.17 | 175GB | 6.17 |

We provide more detailed results at the end of the blog post.

🐋 3. Exploiting DeepSeek R1’s architecture

In [our previous analysis](https://x.com/danielhanchen/status/1872719599029850391) of the DeepSeek V3 model, which used DeepSeek r1 for synthetic data generation, we noted that the first 3 layers of DeepSeek are fully dense, and not MoE. As a refresher, MoE (mixture of experts) layers allow us to increase the number of parameters in a model, without increasing the number of FLOPs used, since we dynamically mask most entries as 0, and so we essentially skip doing matrix multiples on the zeroed out entries.![Image 20](https://unsloth.ai/cgi/image/deepseek_v3_analysis_gTjgng6coSIvRvrUkg3fL.jpg?width=1200&quality=80&format=auto)The goal of MoEs is to “trick” the scaling laws, since we increase the number of parameters without changing the compute cost. For more notes on MoEs and a new method called Memory Layers, which aims to do better than MoEs, see this tweet: [x.com/danielhanchen/status/1868748998783517093](https://x.com/danielhanchen/status/1868748998783517093)By combining 4 ideas, including:

*   Our [4-bit Dynamic Quantization](https://unsloth.ai/blog/dynamic-4bit) method
*   The [1.58-bit LLMs paper](https://arxiv.org/abs/2402.17764)
*   [Llama.cpp’s 1.5-bit](https://github.com/ggerganov/llama.cpp/pull/5453) quantization
*   The [Super Weights paper](https://arxiv.org/abs/2411.07191)

We managed to employ these insights:

*   The first 3 dense layers use 0.5% of all weights. We’ll leave these as 4 or 6bit.
*   MoE layers use shared experts, using 1.5% of weights. We’ll use 6bit.
*   We can leave all MLA attention modules as 4 or 6bit, using <5% of weights. We should quantize the attention output (3%), but it’s best to leave it in higher precision.
*   The down\_proj is the most sensitive to quantization, especially in the first few layers. We corroborated our findings with the Super Weights paper, our dynamic quantization method and llama.cpp’s GGUF quantization methods. So, we shall leave the first 3 to 6 MoE down\_proj matrices in higher precision. For example in the [Super Weights paper](https://arxiv.org/pdf/2411.07191), we see nearly all weights which should NOT be quantized are in the down\_proj:  
    ![Image 21](https://unsloth.ai/cgi/image/superweights_t3PXOuE0uhMCFWT1AIBeb.png?width=2048&quality=80&format=auto)The main insight on why all the “super weights” or the most important weights are in the down\_proj is because of SwiGLU which does:\[ f ⁡ ( X ⁢ W g ⁢ a ⁢ t ⁢ e ) ∗ ( X ⁢ W u ⁢ p ) \] ⁢ W d ⁢ o ⁢ w ⁢ n
    
      
    This means the up and gate projection essentially multiply to form high numbers, and the down\_proj has to scale them down - this means quantizing the down\_proj might not be a good idea, especially in the early layers of the transformer.
*   We should leave the embedding and lm\_head as 4bit and 6bit respectively. The MoE router and all layer norms are left in 32bit.
*   This leaves ~88% of the weights as the MoE weights! By quantizing them to 1.58bit, we can massively shrink the model!
*   We provided our dynamic quantization code as a fork to llama.cpp: [github.com/unslothai/llama.cpp](https://github.com/unslothai/llama.cpp)
*   We leveraged [Bartowski](https://huggingface.co/bartowski)’s importance matrix for the lower quants.

💬 Chat Template Issues

All distilled versions and the main 671B R1 model use the same chat template:`<｜begin▁of▁sentence｜><｜User｜>What is 1+1?<｜Assistant｜>It's 2.<｜end▁of▁sentence｜><｜User｜>Explain more!<｜Assistant｜>`A BOS is forcibly added, and an EOS separates each interaction. To counteract double BOS tokens during inference, you should only call tokenizer.encode(..., add\_special\_tokens = False) since the chat template auto adds a BOS token as well.  
For llama.cpp / GGUF inference, you should skip the BOS since it’ll auto add it.`<｜User｜>What is 1+1?<｜Assistant｜>`The <think\> and </think\> tokens get their own designated tokens. For the distilled versions for Qwen and Llama, some tokens are re-mapped, whilst Qwen for example did not have a BOS token, so <|object\_ref\_start|\> had to be used instead.Tokenizer ID Mappings:

| Token | R1 | Distill Qwen | Distill Llama |
| --- | --- | --- | --- |
| <think\> | 128798 | 151648 | 128013 |
| </think\> | 128799 | 151649 | 128014 |
| <|begin\_of\_sentence|\> | 0 | 151646 | 128000 |
| <|end\_of\_sentence|\> | 1 | 151643 | 128001 |
| <|User|\> | 128803 | 151644 | 128011 |
| <|Assistant|\> | 128804 | 151645 | 128012 |
| Padding token | 2 | 151654 | 128004 |

Original tokens in models:

| Token | Qwen 2.5 32B Base | Llama 3.3 70B Instruct |
| --- | --- | --- |
| <think\> | <|box\_start|\> | <|reserved\_special\_token\_5|\> |
| </think\> | <|box\_end|\> | <|reserved\_special\_token\_6|\> |
| <｜begin▁of▁sentence｜\> | <|object\_ref\_start|\> | <|begin\_of\_text|\> |
| <｜end▁of▁sentence｜\> | <|endoftext|\> | <|end\_of\_text|\> |
| <｜User｜\> | <|im\_start|\> | <|reserved\_special\_token\_3|\> |
| <｜Assistant｜\> | <|im\_end|\> | <|reserved\_special\_token\_4|\> |
| Padding token | <|vision\_pad|\> | <|finetune\_right\_pad\_id|\> |

All Distilled and the original R1 versions seem to have accidentally assigned the padding token to <｜end▁of▁sentence｜\>, which is mostly not a good idea, especially if you want to further finetune on top of these reasoning models. This will cause endless infinite generations, since most frameworks will mask the EOS token out as -100.We fixed all distilled and the original R1 versions with the correct padding token (Qwen uses <|vision\_pad|\>, Llama uses <|finetune\_right\_pad\_id|\>, and R1 uses <｜▁pad▁｜\> or our own added <｜PAD▁TOKEN｜\>.

🖥️ Running Dynamic Quants

You do NOT need to use a new llama.cpp version - any system (like Ollama, [OpenWebUI](https://github.com/open-webui/open-webui), Transformers, even vLLM) which can run GGUFs should be able to run dynamic quants. It might be slow if you do not have enough VRAM or RAM, but it works.If you want to use llama.cpp directly, follow the build instructions for llama.cpp [here](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md) - don’t forget to enable GPU support! I normally use the below:

```
apt-get update
apt-get install build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggerganov/llama.cpp
cmake llama.cpp -B llama.cpp/build \
	-DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli
cp llama.cpp/build/bin/llama-* llama.cpp
```Then download the model through [huggingface.co/unsloth/DeepSeek-R1-GGUF](https://huggingface.co/unsloth/DeepSeek-R1-GGUF) You can use Hugging Face for this. To download the 1.58bit version, do:```
# pip install huggingface_hub
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/DeepSeek-R1-GGUF",
    local_dir = "DeepSeek-R1-GGUF",
    allow_patterns = [“*UD-IQ1_S*”],
)
```This will download 3 GGUF files to DeepSeek-R1-GGUF/DeepSeek-R1-UD-IQ1\_S. Then, use this formula to decide how many layers you can offload to the GPU. If you do not have a GPU, set offloading to 0:n offload \= VRAM ⁡ ( G ⁢ B ) Filesize ⁡ ( G ⁢ B ) × n layers − 4

DeepSeek R1 has 61 layers. For example with a 24GB GPU or 80GB GPU, you can expect to offload after rounding down (reduce by 1 if it goes out of memory):

| Quant | File Size | 24GB GPU | 80GB GPU | 2x80GB GPU |
| --- | --- | --- | --- | --- |
| 1.58bit | 131GB | 7 | 33 | All layers 61 |
| 1.73bit | 158GB | 5 | 26 | 57 |
| 2.22bit | 183GB | 4 | 22 | 49 |
| 2.51bit | 212GB | 2 | 19 | 32 |

To run the model, we quantize the K cache to 4bit. Quantizing the V cache requires flash attention kernels to be compiled for llama.cpp. We use all threads on the machine, and use the recommended temperature by DeepSeek of 0.6. The context size is how many tokens you want the model to generate.```
./llama.cpp/llama-cli \
	--model DeepSeek-R1-UD-IQ1_S/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \
	--cache-type-k q4_0 \
	--threads 12 -no-cnv --n-gpu-layers 61 --prio 2 \
	--temp 0.6 \
	--ctx-size 8192 \
	--seed 3407 \
	--prompt "<｜User｜>Create a Flappy Bird game in Python.<｜Assistant｜>”
```

🦙 Run in Ollama/vLLM
---------------------

If you want to use [Ollama](https://github.com/ollama/ollama) or [vLLM](https://docs.vllm.ai/en/latest/features/quantization/gguf.html) for inference on GGUFs, you need to first merge the 3 GGUF split files into 1 like the code below. Then you will need to run the model locally.```
./llama.cpp/llama-gguf-split --merge \
DeepSeek-R1-UD-IQ1_S/DeepSeek-R1-UD-IQ1_S-00001-of-00003.gguf \
	merged_file.gguf
```

💡 Prompt and results

The full prompt used is below:  
Create a Flappy Bird game in Python. You must include these things:

*   You must use pygame.
*   The background color should be randomly chosen and is a light shade. Start with a light blue color.
*   Pressing SPACE multiple times will accelerate the bird.
*   The bird's shape should be randomly chosen as a square, circle or triangle. The color should be randomly chosen as a dark color.
*   Place on the bottom some land colored as dark brown or yellow chosen randomly.
*   Make a score shown on the top right side. Increment if you pass pipes and don't hit them.
*   Make randomly spaced pipes with enough space. Color them randomly as dark green or light brown or a dark gray shade.
*   When you lose, show the best score. Make the text inside the screen. Pressing q or Esc will quit the game. Restarting is pressing SPACE again.

The final game should be inside a markdown section in Python. Check your code for errors and fix them before the final markdown section.Full tables and results at: [docs.unsloth.ai/basics/deepseek-r1-dynamic-1.58-bit](https://docs.unsloth.ai/basics/deepseek-r1-dynamic-1.58-bit)  
All 18 outputs and Python generated code are also uploaded there!

💕 Thank you!

As usual, a huge thank you to everyone for using & sharing Unsloth - we really appreciate it. 🙏As always, be sure to join our [Reddit page](https://www.reddit.com/r/unsloth/) and [Discord](https://discord.gg/unsloth) server for help or just to show your support! You can also follow us on [Twitter](https://twitter.com/unslothai) and [newsletter](https://unsloth.ai/newsletter).

Thank you for reading!

Daniel & Michael Han 🦥  
27 Jan 2025

