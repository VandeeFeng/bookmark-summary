Title: Aman's AI Journal • Primers • DeepSeek R1

URL Source: https://aman.ai/primers/ai/deepseek-R1/

Markdown Content:
*   [Introduction](https://aman.ai/primers/ai/deepseek-R1/#introduction)
*   [Architectural Foundations](https://aman.ai/primers/ai/deepseek-R1/#architectural-foundations)
    *   [Mixture of Experts (MoE)](https://aman.ai/primers/ai/deepseek-R1/#mixture-of-experts-moe)
    *   [Multihead Latent Attention (MLA)](https://aman.ai/primers/ai/deepseek-R1/#multihead-latent-attention-mla)
    *   [FP8 Quantization](https://aman.ai/primers/ai/deepseek-R1/#fp8-quantization)
    *   [Multi-Token Prediction (MTP)](https://aman.ai/primers/ai/deepseek-R1/#multi-token-prediction-mtp)
*   [Training Pipeline: from Pre-Training to Reasoning](https://aman.ai/primers/ai/deepseek-R1/#training-pipeline-from-pre-training-to-reasoning)
    *   [Stage 1: Cold Start with Supervised Fine-Tuning (SFT)](https://aman.ai/primers/ai/deepseek-R1/#stage-1-cold-start-with-supervised-fine-tuning-sft)
    *   [Stage 2: Reinforcement Learning (RL)](https://aman.ai/primers/ai/deepseek-R1/#stage-2-reinforcement-learning-rl)
        *   [Rewards](https://aman.ai/primers/ai/deepseek-R1/#rewards)
*   [Group Relative Policy Optimization (GRPO)](https://aman.ai/primers/ai/deepseek-R1/#group-relative-policy-optimization-grpo)
    *   [How GRPO Works](https://aman.ai/primers/ai/deepseek-R1/#how-grpo-works)
    *   [Step-by-Step Breakdown](https://aman.ai/primers/ai/deepseek-R1/#step-by-step-breakdown)
    *   [PPO vs. DPO vs. KTO vs. APO vs. GRPO](https://aman.ai/primers/ai/deepseek-R1/#ppo-vs-dpo-vs-kto-vs-apo-vs-grpo)
        *   [Tabular Comparison](https://aman.ai/primers/ai/deepseek-R1/#tabular-comparison)
*   [Emergent Reasoning Behaviors](https://aman.ai/primers/ai/deepseek-R1/#emergent-reasoning-behaviors)
*   [Distillation: Reasoning in Compact Models](https://aman.ai/primers/ai/deepseek-R1/#distillation-reasoning-in-compact-models)
*   [Results](https://aman.ai/primers/ai/deepseek-R1/#results)
*   [Open Questions](https://aman.ai/primers/ai/deepseek-R1/#open-questions)
    *   [Open-R1](https://aman.ai/primers/ai/deepseek-R1/#open-r1)
        *   [Objectives of Open-R1](https://aman.ai/primers/ai/deepseek-R1/#objectives-of-open-r1)
        *   [Impact on the Community](https://aman.ai/primers/ai/deepseek-R1/#impact-on-the-community)
*   [Reasoning Datasets](https://aman.ai/primers/ai/deepseek-R1/#reasoning-datasets)
*   [References](https://aman.ai/primers/ai/deepseek-R1/#references)

Introduction
------------

*   [DeepSeek-R1](https://arxiv.org/abs/2501.12948) represents a landmark in reasoning-capable Large Language Models (LLMs). [Released](https://huggingface.co/deepseek-ai/DeepSeek-R1) under an MIT license, this model rivals closed-source giants like OpenAI’s o1 series while pioneering a reinforcement learning (RL)-driven framework for reasoning tasks.
*   DeepSeek-R1 leverages Group Relative Policy Optimization (GRPO), introduced in [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300), which replaces traditional methods like PPO, making training both efficient and scalable. DeepSeek-R1 also utilizes Multihead Latent Attention (MLA), introduced in [DeepSeek-V3](https://arxiv.org/abs/2412.19437), reduces computational and memory inefficiencies, particularly for long-context processing, by projecting Key-Query-Value (KQV) matrices into a lower-dimensional latent space. Furthermore, DeepSeek-R1 demonstrates how reasoning capabilities emerge naturally through RL without relying on massive supervised fine-tuning (SFT).
*   DeepSeek-R1 redefines open-source AI, proving that reasoning capabilities can emerge from RL alone. Through innovations like GRPO, FP8 quantization, and emergent CoT reasoning, it rivals closed-source models while fostering transparency and accessibility. As the research community builds upon these innovations, DeepSeek-R1 signals a shift towards efficient, reasoning-driven AI accessible to all.
*   This primer explores its architecture, multi-stage training pipeline, GRPO mechanics, and emergent reasoning behaviors, alongside how distillation propagates reasoning capabilities to smaller models.

Architectural Foundations
-------------------------

*   DeepSeek-R1 builds upon the [DeepSeek-V3-Base](https://arxiv.org/abs/2412.19437) model, integrating cutting-edge architectural innovations that optimize both training efficiency and inference performance. These foundational enhancements include Mixture of Experts (MoE), Multihead Latent Attention (MLA), FP8 Quantization, and Multi-Token Prediction (MTP). This section provides a detailed breakdown of each component.
*   The architectural foundations of DeepSeek-R1 represent a synthesis of state-of-the-art techniques that collectively optimize its performance across reasoning-intensive tasks. These innovations make it a leading open-source large language model, rivaling proprietary counterparts in efficiency and reasoning capability.

### Mixture of Experts (MoE)

*   **Overview**: The Mixture of Experts (MoE) mechanism activates only a subset of the total parameters within each Transformer block, enabling substantial computational savings while preserving model quality. This selective activation is particularly advantageous for scaling up model parameters without proportionally increasing computational costs.
    
*   **DeepSeek-V3 Implementation**: DeepSeek-V3 employs a sparse routing mechanism in MoE, where a gating network selects the top-k experts per token. This ensures only a fraction of the parameters are activated at any given time, significantly reducing computation while maintaining performance.
    
*   **DeepSeek-R1 Enhancements & Implementation Details**:
    
    *   **Dynamic Expert Assignment**: Reduces the risk of over-specialization by dynamically selecting experts based on token context.
    *   **Reinforcement Learning Optimization**: Implements reinforcement learning-guided expert utilization to balance computational loads and optimize inference speed.
    *   **Sparse Activation Constraints**: Introduces sparsity constraints to minimize computational overhead while maintaining model expressiveness.
    *   **Mathematical Formulation**:
        *   The expert selection process is governed by a gating function \\(G(x)\\) that routes tokens \\(x\\) to experts \\(E\_k\\), defined as: \\(G(x) = \\text{softmax}(W\_g x)\\)
        *   Each token is then processed by the selected experts, aggregated as: \\(y = \\sum\_{k \\in K} G\_k(x) E\_k(x)\\)
        *   Load balancing loss is added to encourage equal expert utilization, reducing computational bottlenecks.

### Multihead Latent Attention (MLA)

*   **Overview**: Multihead Latent Attention (MLA), introduced in [DeepSeek-V3](https://arxiv.org/abs/2412.19437), reduces computational and memory inefficiencies by projecting Key-Query-Value (KQV) matrices into a lower-dimensional latent space. This innovation is critical for decreasing inference latency and computational costs, particularly for long-context processing.
    
*   **DeepSeek-V3 Implementation**: DeepSeek-V3 introduced MLA to mitigate the high memory and computational costs of traditional self-attention mechanisms. By projecting KQV matrices into a compact latent space, it significantly reduces attention complexity while preserving model performance.
    
*   **DeepSeek-R1 Enhancements & Implementation Details**:
    
    *   **Hybrid Latent Projection**: Combines fixed and adaptive scaling of the latent space based on context complexity.
    *   **Hierarchical Caching**: Introduces an advanced caching mechanism to reuse latent projections across multiple tokens, significantly reducing redundant computation.
    *   **Equation for Latent Projection**:
        *   The transformation of the attention mechanism is formulated as: \\(K, Q, V = W\_k X, W\_q X, W\_v X\\)
        *   These are projected into a lower-dimensional latent space \\(L\\) as: \\(K\_L, Q\_L, V\_L = W\_L K, W\_L Q, W\_L V\\)
        *   This reduces the attention computation complexity from \\(O(N^2)\\) to \\(O(Nd\_L)\\), where \\(d\_L\\) is the latent space dimension.

### FP8 Quantization

*   **Overview**: DeepSeek-R1 employs 8-bit floating-point (FP8) quantization to reduce memory usage and computational costs. Compared to FP32 formats, FP8 provides a 75% reduction in memory requirements while maintaining numerical stability during training and inference.
    
*   **DeepSeek-R1 Enhancements & Implementation Details**:
    
    *   **Adaptive Bit-Width Scaling**: Dynamically adjusts the bit precision across different network layers based on computational demands.
    *   **Loss-Aware Quantization**: Uses loss-sensitive scaling functions to ensure stability and precision.
    *   **Mathematical Representation**:
        *   Quantization function: \\(x\_q = \\text{clip}( \\text{round}(x / S), -127, 127)\\)
        *   Where \\(S\\) is the scaling factor determined dynamically based on loss gradients.

### Multi-Token Prediction (MTP)

*   **Overview**: Multi-Token Prediction (MTP) allows DeepSeek-R1 to predict multiple tokens simultaneously instead of generating one token at a time. This innovation significantly improves inference efficiency, particularly in long-context reasoning tasks.
    
*   **Key Features**:
    *   **Parallel Decoding**: Extends the autoregressive framework by allowing multiple token predictions within the same context window.
    *   **Token Sampling and Re-ranking**: Multi-token outputs are sampled from a probabilistic distribution and re-ranked for coherence.
    *   **Dynamic Prediction Horizon**: Adjusts the number of predicted tokens per step based on model confidence.
*   **DeepSeek-R1 Enhancements & Implementation Details**:
    *   **Reinforcement Learning-Guided Token Selection**: Ensures coherence in multi-token predictions and reduces error propagation.
    *   **Hierarchical Token Verification**: Dynamically adjusts the number of predicted tokens per step based on uncertainty estimation.
    *   **Mathematical Formulation**:
        *   Prediction function: \\(P(y\_t | x) = \\prod\_{t=1}^{T} P(y\_t | y\_{<t}, x)\\)
        *   Parallelization reduces decoding complexity from \\(O(T)\\) to \\(O(T/k)\\), where \\(k\\) is the number of predicted tokens per step.

Training Pipeline: from Pre-Training to Reasoning
-------------------------------------------------

*   DeepSeek-R1 employs a multi-stage pipeline meticulously designed to maximize its reasoning capabilities while minimizing computational costs. This process consists of distinct stages, each guided by task-specific loss functions and reward mechanisms.

### Stage 1: Cold Start with Supervised Fine-Tuning (SFT)

*   DeepSeek-R1 begins its journey by fine-tuning the V3-Base model with high-quality Chain-of-Thought (CoT) examples. These examples are carefully curated using few-shot prompting, manual annotation, and refinement of DeepSeek-R1-Zero outputs.
    
*   **Comparison to Cold Start in Recommender Systems:**
    *   In recommender systems, the “cold start problem” refers to the challenge of providing accurate recommendations for new users or items with limited historical data. The focus is on mitigating data sparsity by learning user preferences or item properties.
    *   In contrast, DeepSeek-R1’s cold start addresses the challenge of initializing a large language model with structured reasoning and readability. By fine-tuning on curated data, the model develops a foundational understanding of chain-of-thought reasoning, overcoming instability observed in RL-only training setups.
*   **Advantages of Cold Start:**
    
    *   **Readability:** DeepSeek-R1-Zero struggled with poor readability and language mixing. In contrast, the cold-start phase imposes a structured output format:
        
        ```
        <reasoning_process> CoT explanation </reasoning_process>
        <summary> Final Answer </summary>
        ```
        
    *   **Alignment:** Cold start data introduces **human priors**, accelerating convergence and improving performance on reasoning-intensive tasks.
        
    *   DeepSeek-R1 begins its journey by fine-tuning the V3-Base model with high-quality CoT examples. These examples are carefully curated using few-shot prompting, manual annotation, and refinement of DeepSeek-R1-Zero outputs.
*   **Loss Function for SFT:**
    
    *   The model is fine-tuned using a supervised cross-entropy loss:
        
        \\\[L\_{\\text{SFT}} = -\\sum\_{i=1}^{n} \\log P\_{\\theta}(o\_i|q, \\{o\_1, \\dots, o\_{i-1}\\}),\\\]
        *   where:
            *   \\(o\_i\\): the \\(i\\)-th token in the output sequence,
            *   \\(q\\): the input query,
            *   \\(o\_1, ..., o\_{i-1}\\): previously generated tokens.

### Stage 2: Reinforcement Learning (RL)

*   Reinforcement learning is the backbone of DeepSeek-R1’s reasoning evolution. The model learns from rewards rather than curated datasets, enabling self-improvement over thousands of iterations.

#### Rewards

*   DeepSeek-R1 uses two primary reward functions:
    
    1.  **Accuracy Rewards:**
        
        *   Evaluate the correctness of deterministic tasks, such as math problems and code-generation outputs. For example:
            *   In math, the model’s final answer is verified against a ground truth.
            *   For coding, unit tests evaluate the validity of generated code solutions.
    2.  **Format Rewards:**
        
        *   Encourage consistent reasoning structures by rewarding outputs that adhere to the specified CoT format. For example:
            
            ```
            <reasoning_process> Step-by-step explanation </reasoning_process>
            <answer> Final Output </answer>
            ```
            

Group Relative Policy Optimization (GRPO)
-----------------------------------------

*   Group Relative Policy Optimization (GRPO), introduced in [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300), is the centerpiece of DeepSeek-R1’s RL framework, introducing a simplified and efficient alternative to traditional policy optimization methods like PPO and DPO. Here, we explore how GRPO works, why it differs, and its key advantages over other approaches.

### How GRPO Works

*   The GRPO objective is:

\\\[J\_{\\text{GRPO}}(\\theta) = \\mathbb{E}\_{q \\sim P(Q), \\{o\_i\\}\_{i=1}^G \\sim \\pi\_{\\theta\_{\\text{old}}}(O|q)} \\left\[ \\frac{1}{G} \\sum\_{i=1}^G \\min\\left(\\rho\_i A\_i, \\text{clip}(\\rho\_i, 1-\\epsilon, 1+\\epsilon) A\_i\\right) - \\beta D\_{\\text{KL}}(\\pi\_\\theta \\| \\pi\_{\\text{ref}}) \\right\]\\\]

### Step-by-Step Breakdown

1.  **Likelihood Ratio \\(\\rho\_i\\):**
    *   The likelihood ratio measures how much more likely the new policy \\(\\pi\_\\theta\\) is to produce an output \\(o\_i\\) compared to the old policy \\(\\pi\_{\\theta\_{\\text{old}}}\\): \\(\\rho\_i = \\frac{\\pi\_\\theta(o\_i|q)}{\\pi\_{\\theta\_{\\text{old}}}(o\_i|q)}.\\)
2.  **Advantage Function \\(A\_i\\):**
    *   The advantage function evaluates how much better an output \\(o\_i\\) is compared to the average outputs in the group: \\(A\_i = \\frac{r\_i - \\text{mean}(r\_1, ..., r\_G)}{\\text{std}(r\_1, ..., r\_G)},\\)
        
        where \\(r\_i\\) is the reward associated with the \\(i\\)-th output.
        
3.  **Clipping Mechanism:**
    *   Clipping ensures that the policy updates remain stable by restricting the likelihood ratio within the range \\(\[1-\\epsilon, 1+\\epsilon\]\\): \\(\\text{clip}(\\rho\_i, 1-\\epsilon, 1+\\epsilon).\\)
    *   This prevents overly aggressive updates that could destabilize training.
4.  **KL Divergence Penalty:**
    
    *   The KL divergence term ensures the new policy remains close to a reference policy:
        
        \\\[- \\beta \\, D\_{\\text{KL}}\\bigl(\\pi\_\\theta \\;\\|\\; \\pi\_{\\text{ref}}\\bigr)\\\]
        *   where, \\(\\beta\\) controls how much the KL term influences the overall objective.

### PPO vs. DPO vs. KTO vs. APO vs. GRPO

1.  **PPO**:
    *   **Function**: An RL algorithm that optimizes the language model by limiting how far it can drift from a previous version of the model.
    *   **Implementation**: Involves sampling generations from the current model, judging them with a reward model, and using this feedback for updates.
    *   **Practical Challenges**: Can be slow and unstable, especially in distributed settings.
2.  **DPO**:
    *   **Function**: Minimizes the negative log-likelihood of observed human preferences to align the language model with human feedback.
    *   **Data Requirement**: Requires paired preference data.
    *   **Comparison with KTO**: While DPO has been effective, KTO offers competitive or superior performance without the need for paired preferences.
3.  **KTO**:
    *   **Function**: Adapts the Kahneman-Tversky human value function to the language model setting. It uses this adapted function to directly maximize the utility of model outputs.
    *   **Data Requirement**: Does not need paired preference data, only knowledge of whether an output is desirable or undesirable for a given input.
    *   **Practicality**: Easier to deploy in real-world scenarios where desirable/undesirable outcome data is more abundant.
    *   **Model Comparison**: Matches or exceeds the performance of direct preference optimization methods across various model sizes (from 1B to 30B).
4.  **APO**:
    *   **Function**: Introduces a family of contrastive objectives explicitly accounting for the relationship between the model and the preference dataset. This includes APO-zero, which increases desirable outputs while decreasing undesirable ones, and APO-down, which fine-tunes models based on specific quality thresholds.
    *   **Data Requirement**: Works effectively with paired preference datasets created through controlled methods like CLAIR and supports stable alignment even for challenging datasets.
    *   **Practicality**: Excels at aligning strong models with minimally contrasting preferences, enhancing performance on challenging metrics like MixEval-Hard while providing stable, interpretable training dynamics.
    *   **Model Comparison**: Outperformed conventional alignment objectives across multiple benchmarks, closing a 45% performance gap with GPT4-turbo when trained with CLAIR preferences.
5.  **GRPO**:
    *   **Function**: A variant of PPO that removes the need for a critic model by estimating the baseline using group scores, improving memory and computational efficiency while enhancing the mathematical reasoning of models.
    *   **Data Requirement**: Utilizes group-based rewards computed from multiple outputs for each query, normalizing these scores to guide optimization.
    *   **Practicality**: Focuses on reducing training resource consumption compared to PPO and improving reinforcement learning stability.
    *   **Model Comparison**: Demonstrated superior performance on tasks like GSM8K and MATH benchmarks, outperforming other models of similar scale while improving both in-domain and out-of-domain reasoning tasks.

#### Tabular Comparison

| **Aspect** | **PPO** | **DPO** | **KTO** | **APO** | **GRPO** |
| --- | --- | --- | --- | --- | --- |
| Objective | Maximizes expected reward while preventing large policy updates. | Optimizes policy based on binary classification of human preferences. | Aligns models based on Kahneman-Tversky optimization for utility maximization. | Anchored alignment with specific control over preference-based likelihood adjustments for stability and performance. | Leverages group-based relative advantages and removes the critic network. |
| Input Data | States and rewards from the environment. | Paired human preference data. | Binary labels indicating desirability of outputs. | Minimally contrasting preference pairs or other datasets requiring tailored anchoring. | Grouped LLM outputs scored by a reward model. |
| Learning Mechanism | Policy gradients with a clipped surrogate objective. | Cross-entropy optimization over paired preferences. | Maximizes desirable likelihoods relative to undesirables, without paired data. | Uses variants like APO-zero or APO-down to balance desirable/undesirable likelihood changes. | Group normalization with policy gradients, eliminating the critic network. |
| Output | Actions in the environment. | Aligned responses based on human preferences. | Model outputs optimized for human utility. | Refined outputs aligned to the quality of preference pairs, with control over optimization dynamics. | Outputs optimized for reasoning, reducing computational overhead. |
| Data Requirements | Requires environment rewards. | Needs paired preference data. | Binary feedback, no need for explicit pairings. | Performs best with datasets that maintain controlled contrastiveness, e.g., CLAIR. | Reward scores grouped across multiple outputs. |

Emergent Reasoning Behaviors
----------------------------

*   During training, DeepSeek-R1 developed remarkable reasoning patterns:
    
    *   **Reflection:** Revisiting and revising intermediate steps.
    *   **Self-Correction:** Identifying and fixing errors in real-time.
    *   **Aha Moments:** Pausing and reevaluating to discover new solutions.
*   For example:
    
    *   Solving \\(x^2 - 5x + 6 = 0\\), the model might initially propose incorrect factors, pause to reflect, and ultimately derive \\(x = 2\\) and \\(x = 3\\).
    *   The table below from the original paper, we can see where R1 has it’s “aha” moment and re-evaluates the solution:
    
    ![Image 13](https://aman.ai/primers/ai/assets/DeepSeek/2.png)
    

Distillation: Reasoning in Compact Models
-----------------------------------------

*   DeepSeek-R1’s reasoning capabilities were distilled into smaller models (e.g., Qwen-7B, Llama-8B), achieving state-of-the-art performance:
    
    *   **Teacher-Student Paradigm:** Outputs from DeepSeek-R1 trained smaller models with minimal computational overhead.
    *   **Efficiency:** Distilled models retained reasoning capabilities while outperforming larger, non-reasoning models like GPT-4o.
*   The table below shows how distilled R1 models and how they compare on reasoning related benchmarks.
    

![Image 14](https://aman.ai/primers/ai/assets/DeepSeek/3.png)

Results
-------

*   The figure below from the [original paper](https://arxiv.org/abs/2501.12948), shows the performance of DeepSeek R1 being at par with or outperforming OpenAI’s models at several benchmarks.

![Image 15](https://aman.ai/primers/ai/assets/DeepSeek/1.png)

Open Questions
--------------

*   As shown in the figure below ([source](https://huggingface.co/blog/open-r1)), making a powerful reasoning model is now very simple if you have access to a capable base model and a high-quality data mixture:

![Image 16](https://aman.ai/primers/ai/assets/DeepSeek/reasoningLLM.png)

*   Despite DeepSeek-R1’s advances, several open questions remain regarding its development and optimal implementation:
    
    *   **Data Collection**: How were the reasoning-specific datasets curated? Understanding the sources and selection criteria for data is crucial for replicating and improving the model’s performance.
    *   **Model Training**: No training code was released by DeepSeek, leaving uncertainty about which hyperparameters work best and how they differ across model families and scales.
    *   **Scaling Laws**: What are the compute and data trade-offs in training reasoning models? Identifying these relationships is critical for optimizing future models.

### Open-R1

*   While DeepSeek-R1 provides open weights, the datasets and code used in training remain proprietary. The aforementioned questions have driven the [Open-R1: a fully open reproduction of DeepSeek-R1](https://huggingface.co/blog/open-r1) project, an initiative to systematically reconstruct DeepSeek-R1’s data and training pipeline, validate its claims, and push the boundaries of open reasoning models. The motivation behind building [Open-R1](https://github.com/huggingface/open-r1) is to provide transparency on how reinforcement learning can enhance reasoning, share reproducible insights with the open-source community, and create a foundation for future models to leverage these techniques.

#### Objectives of Open-R1

1.  **Reproducing R1-Distill Models**: By distilling a high-quality reasoning dataset from DeepSeek-R1, Open-R1 aims to replicate the R1-Distill models faithfully.
2.  **Replicating the RL Training Pipeline**: A critical component of DeepSeek-R1 is its reinforcement learning-based training methodology. Open-R1 will curate large-scale datasets for mathematics, reasoning, and code to enable this training process.
3.  **Advancing Multi-Stage Training**: Demonstrating the full transition from a base model through SFT to RL will be a key milestone, ensuring a reproducible and scalable methodology.

*   As shown in the figure below ([source](https://huggingface.co/blog/open-r1)), here’s the Open-R1 plan:

![Image 17](https://aman.ai/primers/ai/assets/DeepSeek/open-r1-steps.png)

*   **Accessible Reasoning Models**: Open-R1’s synthetic datasets will allow anyone to fine-tune existing or new LLMs for reasoning tasks simply by leveraging these datasets.
*   **Open RL Recipes**: The initiative will provide well-documented reinforcement learning methodologies that can serve as a foundation for future research and experimentation.
*   **Exploring Beyond Math**: While mathematical reasoning is a primary focus, Open-R1 will explore extensions into other domains, including programming and scientific applications such as medicine, where reasoning models can make a significant impact.

Reasoning Datasets
------------------

1.  [OpenThoughts](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k): 114k samples distilled from R1 on math, code, and science.
2.  [R1-Distill-SFT](https://huggingface.co/datasets/ServiceNow-AI/R1-Distill-SFT): 1.7M samples distilled from R1-32B on NuminaMath and Allen AI’s Tulu.

References
----------

*   [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
*   [DeepSeek-R1: A Pure RL-based Reasoning Model](https://www.linkedin.com/pulse/deepseek-r1-pure-rl-based-reasoning-model-jayant-kumar-yfopc/?trackingId=Tc70aMqJS42SK6oiIPqBZA%3D%3D)
*   [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)
*   [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)
*   [Open-R1: a fully open reproduction of DeepSeek-R1](https://huggingface.co/blog/open-r1)
