# Writing an LLM from scratch, part 8 -- trainable self-attention
- URL: https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention
- Added At: 2025-03-05 08:21:34
- [Link To Text](2025-03-05-writing-an-llm-from-scratch,-part-8----trainable-self-attention_raw.md)

## Summary
**摘要**：
本文是作者学习 Sebastian Raschka 的《Build a Large Language Model (from Scratch)》一书的第八篇博客，主要讲解了如何实现带有可训练权重的自注意力机制。文章首先回顾了GPT类型解码器LLM的工作流程，包括分词、生成token embeddings和position embeddings、相加生成input embeddings，以及自注意力机制等步骤。然后，详细解释了 scaled dot product attention 的原理和计算过程，包括如何通过 query weights matrix、key weights matrix 和 value weights matrix 将 input embeddings 投影到不同的空间，并计算 attention score 和 attention weights，最终生成 context vectors。作者还介绍了如何通过矩阵乘法高效地完成这些计算，并对 softmax 函数在处理高维度数据时的问题进行了讨论，提出了缩放的方法。最后，作者将所有步骤整合在一起，总结了自注意力机制的实现过程，并展望了后续的学习计划，包括因果自注意力和多头注意力机制。

**要点总结**：

1.  **LLM工作流程**: LLM通过一系列步骤处理文本数据，从分词开始，到生成token embeddings和position embeddings，再到通过自注意力机制生成上下文向量，为预测下一个token做准备。Token embeddings是将token转换成向量，Position embeddings是代表token位置信息的向量。
2.  **Scaled Dot Product Attention**: 这是一种可训练的自注意力机制，通过 query weights matrix (Wq), key weights matrix (Wk), 和 value weights matrix (Wv) 将输入向量投影到query空间、key空间和value空间，然后计算attention score和attention weights。
3.  **矩阵乘法的应用**: 通过矩阵乘法，可以高效地对所有输入序列同时进行投影、计算 attention score 和生成上下文向量，减少了循环计算的开销。
4.  **Softmax 函数的改进**: 为了避免在高维度空间中使用 softmax 函数时出现梯度消失的问题，通常会先将 attention score 除以维度 c 的平方根，然后再进行 softmax 归一化。
5.  **Context Vectors的生成**: 通过将输入 embeddings 投影到 value space，并根据 attention weights 进行加权求和，可以得到 context vectors，这些向量包含了输入 token 在整个上下文中的含义信息。

