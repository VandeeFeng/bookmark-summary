---
title: Drawing the Transformer Network from Scratch (Part 1)
date: 2024-11-04
extra:
  source: https://towardsdatascience.com/drawing-the-transformer-network-from-scratch-part-1-9269ed9a2c5e
  original_title: Drawing the Transformer Network from Scratch (Part 1)
---
## Summary
**摘要**：
本文是探索Transformer架构中构建过程的系列第一部分（原本是「从零绘制变压器神经网络」系列的开头），此系列旨在以引人入胜的方式帮助读者形成清晰的Transformer概念模型。文章持续描绘它的各个组成部分，以从底部至顶部（Bottom-top fashion）的方式揭示整个架构，期望读者能轻松构建Transformer的“心理模型”。由谷歌团队于2017年提出的Transformer，因其“注意力机制”成为文献界中不可忽视的重要一员。

### 输入
Transformer接收到的输入是词汇序列，这些词汇以向量形式呈现。通常在自然语言处理任务中，使用词汇表（或字典）表示每个词汇，每个词汇分配一个唯一的索引，在实践中是词汇表中的至少10,000个不同索引。所有一热向量表示都有相同的欧几里得距离√2。为了减少维度并利用词汇向量的优势，文章将一热编码向量与命名为“嵌入矩阵”的矩阵相乘，得到更具体的“词汇嵌入”。

### 词汇嵌入
通过将一热编码向量与名为“嵌入矩阵”的矩阵相乘，减小向量的维度，以减少计算复杂度，并且能将具有相似含义的词放置在同一部分的向量空间中，这种方法显著降低了语言模型的存储需求。这不仅便于计算机处理，还优化了训练阶段的效率。

### 位置编码
位置信息不随输入序列顺序传递的问题由位置编码解决。在这个过程中，向每个输入向量添加一个向量，这种做法将顺序或绝对位置的信息注入输入序列中，使词汇正确地排列并降低时间复杂度。

### 关键与查询
向词向量执行调试乘以WQ和WK矩阵，以获得关键向量（Size 64）和查询向量（Size 64）。这一过程的目的是构建平均激励模型，允许Transformer在不同的词汇位置间学习依赖关系。

### 自注意力
执行所有可能的查询与关键向量的点积计算，点积将结果归一化用于作为权重因子。这些权重指示输入句子中不同位置处的单词间依赖程度，称为“自注意”。这意味着在特定位置考察关注的单词，以及忽略短篇文本处理中不相关或附近的单词。

### 规模与softmax
通过缩放权重因子，将它们除以8（关键向量的维度64的平方根），以确保训练阶段的稳定性。紧随缩放与softmax步骤，对局部分权因子执行了归一化过程，以便按比例考虑输入序列中的每个词汇频率。

### 值
从嵌入矩阵WV乘以词向量得到“值向量”，大小为64，关键在于自注意力结果的对比。接下来，我们利用权重因子对每个值向量进行加权，随后汇总所有加权值产生自注意力层的输出。

### DECORA
文章解释了Transformer的高级部分，包括多头自注意力模型，它使用了八个并行的注意力头部和一个额外的权重矩阵WO将推理与结果相加。这是一个关键步骤，确保模型同时关注不同表示子空间的信息。

需要补充的是，大多数谈及Transformer的文章都会忽视将其合并为一段文本，即约10,000个不同指示器实际声调阵列可以密集化为1024的序列层级，进行长度范围的有效压缩。维度削减有助于处理更长序列中的数据，同时通过额外步骤保持处理效率。此外，为确保训练时效率且稳定结果，不应忽视上述讨论的每个组件和步骤，使注意力机制在不同应用领域更加直观。

### 重点提炼**
1. **输入序列预处理**：Transformer接收词汇序列，并通过一热编码将其转换为低维度数字向量，用于便于计算和数据分析。
2. **嵌入与位置编码**：通过嵌入矩阵将原始向量化数据转换为表示更丰富特征的词语嵌入，并通过位置编码确保词汇的顺序信息。
3. **自注意力机制**：涵盖了利用点积和softmax函数调整权重的计算过程，以实现精准的自注意力，并通过权重编码依存关系，帮助模型识别相关的语言元素。
4. **多头自注意力**：整合了多个并行的注意力机制以提升模型性能和精细度，允许模型更加全面和精确地处理和转换输入信息。

以上内容为进一步理解Transformer在自然语言处理领域的应用提供了基础性理解，使复杂机制变得更加清晰易懂，进而能够在实际工作中应用于各种常见文本处理任务。
## Full Content
Title: Drawing the Transformer Network from Scratch (Part 1)

URL Source: https://towardsdatascience.com/drawing-the-transformer-network-from-scratch-part-1-9269ed9a2c5e

Published Time: 2020-11-15T07:55:15.792Z

Markdown Content:
Getting a mental model of the Transformer in a playful way
----------------------------------------------------------

[![Image 1: Thomas Kurbiel](https://miro.medium.com/v2/resize:fill:88:88/2*cl5oQpys6xTyBc2iYy5MPg.jpeg)](https://tkurbiel.medium.com/?source=post_page---byline--9269ed9a2c5e--------------------------------)

[![Image 2: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--9269ed9a2c5e--------------------------------)

![Image 3](https://miro.medium.com/v2/resize:fit:700/1*YBd5d5ysZ2myU7Nxxh4yTg.png)

(Image by author)

The Transformer Neural Networks — usually just called “Transformers” — were introduced by a Google-led team in 2017 in a paper titled “Attention Is All You Need”. They were refined and popularized by many people in the following work.

Like many models invented before it, the Transformer has an encoder-decoder architecture. In this post, we put our focus on the encoder part. We will successively draw all its parts in a Bottom-top fashion. Doing so will hopefully allow the readers to easily develop a “mental model” of the Transformer.

The animation below shows in fast motion what we will cover in this post:

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*UH5SSuMy9y-BcBtvAUhTmQ.gif)

(Image by author)

Input
-----

A Transformer takes as input a sequence of words, which are presented to the network as vectors. In NLP tasks usually a vocabulary (also called dictionary) is used, in which each word is assigned a unique index. The index can be represented as a so called one-hot vector, which is predominantly made up of zeros, with a single “one” value at the correct location. A simple one-hot word encoding for a small vocabulary of ten words is shown in the diagram below:

![Image 5](https://miro.medium.com/v2/resize:fit:376/1*y5d-7nqdE-QIZJCngreBog.png)

Please note that the one-hot encoded vectors have the same size as the number of words in the vocabulary, which in real-world application is at least 10.000. Furthermore, all one-hot encodings have the same Euclidean distance of √2 to each other.

Word Embeddings
---------------

Next, we reduce the dimensionality of the one-hot encoded vectors by multiplying them with a so called “embedding matrix”. The resulting vectors are called word embeddings. The size of the word embeddings in the original paper is 512.

The huge benefit of word embeddings is that words with similar meanings are put close to each other, e.g. the word “cat” and “kitty” end up having similar embedding vectors.

Please note that the “embedding matrix” is a normal matrix, just with a fancy name.

Positional Encoding
-------------------

All the words are presented to the Transformer simultaneously. This is a huge difference to recurrent neural networks, e.g. LSTMs, where words are fed successively. However, this means that the order in which words occur in the input sequence is lost. To address this, the Transformer adds a vector to each input embedding, thus injecting some information about the relative or absolute position.

Keys and Queries
----------------

Finally, we multiply the word embeddings by matrices WQ and WK to obtain the “query vectors” and “key vectors”, each of size 64.

All the components, mentioned so far, are drawn in the following animation:

![Image 6](https://miro.medium.com/v2/resize:fit:700/1*GDC-85VrLe-J8p-G3kEZCA.gif)

Input Sequence, Word Embeddings, Positional Encoding, Keys and Queries (Image by author)

Please note that the order in which we draw the single elements has nothing to do with the order in which the elements are computed.

Parallelization
---------------

One thing to emphasize before we continue, is the way the Transformer lends itself to parallelization. Please note, that all the word embeddings can be computed in parallel. Once we’ve got the embeddings, we also can simultaneously compute the query vectors and key vectors for all the embeddings. This pattern will continue throughout the whole architecture. Please pay attention to it.

Dot Products
------------

We calculate the dot products for all possible combinations of “query vectors” and “key vectors”. The result of a dot product is a single number, which in a later step will be used as a weight factor. The weights factors tell us, how much two words at different positions of the input sentence depend on each other. This is called self-attention in the original paper. The mechanism of self-attention allows the Transformer to learn difficult dependencies even between distant positions.

![Image 7](https://miro.medium.com/v2/resize:fit:700/1*GzF4v8w0rOFAczA-sI6RCQ.gif)

Dot products of “query vectors” and “key vectors” (Image by author)

Scaling
-------

Subsequently, all weight factors are divided by 8 (the square root of the dimension of the key vectors 64). The authors assume that during training the dot products can grow large in magnitude, thus pushing the softmax function into regions where it has extremely small gradients. Dividing by 8 leads to having more stable gradients.

Softmax
-------

The scaled factors are put through a softmax function, which normalizes them so they are all positive and sum up to 1.

In the animation below, we perform the scaling for the weight factors belonging to the first word in our sentence, which is “The”. Please remember, that the weight factors belonging to the first word are the dot products: q1\*k1, q1\*k2, q1\*k3 and q1\*k4.

![Image 8](https://miro.medium.com/v2/resize:fit:700/1*ctrN__xt86dvW7NX06yCaQ.gif)

Scaling and softmax of the weight factors belonging to the first word “The” (Image by author)

Analogously, for the other words “car”, “is” and “blue” in our input sequence we get:

![Image 9](https://miro.medium.com/v2/resize:fit:700/1*ttQAXZnlrcq4QPfWIkVSlA.gif)

Scaling and softmax of the weights belonging to the remaining words: “car”, “is” and “blue” (Image by author)

This completes the calculation of the weights factors.

Values
------

Identical to the computation of the “key vector” and “query vectors” we obtain the “value vectors” by multiplying the word embeddings by matrix WV. Again the size of the value vectors is 64.

Weighting
---------

Now, we multiply each “value vector” by its corresponding “weight factor”. As mentioned before, this way we only keep the words we want to focus on, while irrelevant words are suppressed by weighting them by tiny numbers like 0.001

Summation
---------

Now we sum up all the weighted “value vectors” belonging to a word. This produces the output of the self-attention layer at this position.

In the next animation we depict the computation of the “value vectors” and their subsequent weighting and summation performed for the first word in the input sequence.

![Image 10](https://miro.medium.com/v2/resize:fit:700/1*x3NcwCBExL-_5UVPQraizg.gif)

Values, Weighting and Summation for the first word “The” (Image by author)

Analogously for the other words “car”, “is”, “blue” in our input sequence, we get:

![Image 11](https://miro.medium.com/v2/resize:fit:700/1*I3yHUigmcykbl8EEdpJopw.gif)

Values, Weighting and Summation for the remaining words: “car”, “is” and “blue” (Image by author)

That concludes the self-attention calculation. The output of the self-attention layer can be considered as a context enriched word embedding. Depending on the context, a word can have different meanings:

*   I like fresh, crisp **fall** weather.
*   Don’t **fall** on your way to the tram.

Please note that the embeddings matrix at the bottom is operating on single words only. Hence for both sentences, we would wrongly obtain the same embedding vector. The self-attention layer is taking this into consideration.

Shorter Sentences
-----------------

The length of the input sequence is supposed to be fixed in length — basically it is the length of the longest sentence in training dataset. Hence, a parameter defines the maximum length of a sequence that the Transformer can accept. Sequences that are greater in length are just truncated. Shorter sequences are padded with zeros. However, padded words are not supposed to contribute to the self-attention calculation. This is avoided by masking the corresponding words (setting them to -inf) before the softmax step in the self-attention calculation. This in fact sets their weight factors to zero.

![Image 12](https://miro.medium.com/v2/resize:fit:700/1*uAn_WIagYnYYL-q3rfqhHQ.gif)

Masking out non used positions (Image by author)

Multi-Head Self-Attention
-------------------------

Instead of performing a single self-attention function, the authors employ multiple self-attention heads, each with different weight matrices. Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. The Transformer in the original paper uses eight parallel attention heads. The outputs of the attention heads are concatenated and once again multiplied by an additional weights matrix WO.

![Image 13](https://miro.medium.com/v2/resize:fit:700/1*9SGL9LbtH1CWTkkHgV-Xpw.gif)

Multi-Head Self-Attention with 3 heads, original paper uses 8 heads (Image by author)

Add & Normalize
---------------

The multi-head self-attention mechanism, just covered, is the first sub-module of the encoder. It has a residual connection around it, and is followed by a layer-normalization step. Layer-normalization just subtracts the mean of each vector and divides by its standard deviation.

![Image 14](https://miro.medium.com/v2/resize:fit:700/1*FMRS9vf5B4aBf2c_e_F8gg.gif)

Residual Connections, Layer Normalization (Image by author)

Feed Forward
------------

The outputs of the self-attention layer are fed to a fully connected feed-forward network. This consists of two linear transformations with a ReLU activation in between. The dimensionality of input and output is 512, and the inner-layer has dimensionality 2048. The exact same feed-forward network is independently applied to each position, i.e. for each word in the input sequence.

Next, we again employ a residual connection around the fully connected feed-forward layer, followed by layer normalization.

![Image 15](https://miro.medium.com/v2/resize:fit:700/1*2KZQBhtv2l2Z5or5IFUELg.gif)

Fully Connected Feed-Forward Network, Residual Connections, Layer Normalization (Image by author)

Stack of Encoders
-----------------

The entire encoding component is a stack of six encoders. The encoders are all identical in structure, yet they do not share weights.

![Image 16](https://miro.medium.com/v2/resize:fit:700/1*hTuCAGdXQT-DV_--RW3iYg.gif)

Stack of six Encoders (Image by author)

In the next post, we are going to cover the decoder part of the Transformer. This should be quite straight forward since most of the required concepts were already covered in this post.

Reference
---------

[Original Paper](https://arxiv.org/pdf/1706.03762.pdf)  
[The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)  
[Transformers Explained](https://towardsdatascience.com/transformers-explained-65454c0f3fa7)  
[Get Busy with Word Embeddings](https://www.r-craft.org/r-news/get-busy-with-word-embeddings-an-introduction/)

