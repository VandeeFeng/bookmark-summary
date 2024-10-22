---
title: LLM from scratch with Pytorch
date: 2024-10-22
extra:
  source: https://medium.com/@msouza.os/llm-from-scratch-with-pytorch-9f21808c6319
  original_title: LLM from scratch with Pytorch
---
## TL;DR
这篇文章介绍了如何从头开始构建一个大型语言模型（LLM）。LLM是一种基于Transformer的模型，用于生成类似人类语言的文本。文章首先介绍了LLM的基本原理和工作机制，然后展示了如何使用预训练嵌入层和自定义令牌化方法来改善模型的性能。文章还比较了使用不同预训练模型的结果，证明了GPT-2模型的优异性能。
## Summary
总结
======

**LLM 简介**
------------

*   LLM（Large Language Model）是一种基于 Transformer 的模型，用于生成人类语言类似的文本。
*   本文将从头开始构建一个 LLM 模型，介绍其工作原理和训练过程。

**什么是 LLM？**
--------------

*   LLM 是一种能够理解自然语言并生成类似人类文本的模型。
*   它通过预测下一个令牌（token）来实现文本生成。

### LLM 的工作原理

*   LLM 使用 Transformer 架构来处理序列数据。
*   它通过掩盖部分输入序列来预测下一个令牌。

**令牌化**
------------

*   令牌化（Tokenization）是将原始文本转换为数值表示的过程。
*   一个简单的令牌化方法是将文本分割为单个字符或单词。

### 令牌化示例

*   示例中使用了一个简单的令牌化方法来将文本分割为单个字符。
*   使用正则表达式来分割文本，并将结果存储在词典中。

**使用预训练嵌入层**
---------------------

*   使用预训练的 GPT-2 嵌入层可以减少训练时间和资源需求。
*   示例中使用了 Transformer 库来加载 GPT-2 的令牌化器和嵌入层。

### 与其他模型的比较

*   示例中还比较了使用其他预训练模型（如 BERT、T5 和 RoBERTa）的结果。
*   GPT-2 模型取得了最佳性能和最快的训练速度。

**总结**
----------

*   本文介绍了如何从头开始构建一个 LLM 模型。
*   示例中展示了使用预训练嵌入层和自定义令牌化方法来改善 LLM 模型的性能。
## Full Content
Title: LLM from scratch with Pytorch - Matheus Oliveira De Souza - Medium

URL Source: https://medium.com/@msouza.os/llm-from-scratch-with-pytorch-9f21808c6319

Published Time: 2024-05-19T14:07:00.780Z

Markdown Content:
[![Image 1: Matheus Oliveira De Souza](https://miro.medium.com/v2/resize:fill:88:88/1*1yJ1vHpLv3uG615vC8MlHQ.jpeg)](https://medium.com/@msouza.os?source=post_page-----9f21808c6319--------------------------------)

![Image 2](https://miro.medium.com/v2/resize:fit:643/1*vPRykSHf1nSM7W26WL_dMw.png)

LLM with Pytorch (Image by Author).

Introduction
------------

Generative models are currently one of the most intriguing fields in AI, more specifically, those _text-to-text_ models that generate text based on an initial user prompt. One famous example is **ChatGPT** by **OpenAI**, which is an [Assistant](https://arxiv.org/pdf/2203.02155.pdf) model capable to respond user questions about multiple topics.

In this paper, we cover LLM, how it works and how to train it from scratch. I’ll try to be clear in all topics of this paper, and I hope most of you could understand and learn something from it 😁.

If you are going to run all of the code examples, make sure that you have imported the libraries first.

import torch  
import torch.nn as nn  
import torch.nn.functional as F

What is a LLM?
--------------

You might be thinking that LLM are simply models that generate human-like text or something like that, right? Well, you are correctly, actually. In essence, LLM is a Transformer-based model trained on vast text datasets. It learns to understand the meaning of words and text, enabling it to generate human-like text. In practice, LLM functions as a text completion model, attempting to predict the next _token_ in a sequence based on probabilities. Given a sequence of N tokens, what might the next token be?

![Image 3](https://miro.medium.com/v2/resize:fit:700/1*P9f389f2rJP6-u8Xuq7weQ.png)

Token classification given a context (Image by Author).

Tokenization
------------

Before feed into our model some text data, preprocessing is necessary. As you may know, computers can only understand numbers, not raw text like humans do. Therefore, we need to convert our text into a numeric representation.

A Tokenizer is an algorithm that split raw text into a sequence of words, commonly referred as _tokens._ Each word will be feed to the model vocabulary which store all words that our model knows.

For each token stored in the model vocabulary, it will receives an integer representation referred to that token. As a result, each word will then be converted to an integer.

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*wxywmFV85YBmrpKpDss0WA.png)

Text tokenization (Image by Author).

There isn’t a strict rule to follow when building your own Tokenizer. There are several techniques for text tokenization. We can tokenize these text in character level, so each character is tokenized separately. We can also tokenize them in word level, splitting our text and retrieve sequences of characters that have some meaning. Keep in mind that your tokenization approach will impact your model’s performance during training. This is because the way you tokenize your text determines how your model will interpret it. So a bad tokenization technique will reflect in a bad understanding of text.

Instead of building your own tokenizer, you can use libraries to perform this task for you if you don’t want to spend too much time on this step. Two most famous libraries are [**TikToken**](https://github.com/openai/tiktoken) by OpenAI and [**SentencePiece**](https://github.com/google/sentencepiece) by Google. You can check their repositories on GitHub for more details.

A simple tokenizer that tokenizes in character level can be built in the following code below:

class Tokenizer:@staticmethod  
    def create\_vocab(dataset):  
        """  
        Create a vocabulary from a dataset.Args:  
            dataset (str): Text dataset to be used to create the character vocab.

Returns:  
            Dict\[str, int\]: Character vocabulary.  
        """

  
        vocab = {  
            token: index  
            for index, token in enumerate(sorted(list(set(dataset))))  
        }

vocab\["<unk\>"\] = len(vocab)

return vocab

def \_\_init\_\_(self, vocab):  
        """  
        Initialize the tokenizer.Args:  
            vocab (Dict\[str, int\]): Vocabulary.  
        """

  
        self.vocab\_encode = {str(k): int(v) for k, v in vocab.items()}  
        self.vocab\_decode = {v: k for k, v in self.vocab\_encode.items()}

def encode(self, text):  
        """  
        Encode a text in level character.Args:  
            text (str): Input text to be encoded.

Returns:  
            List\[int\]: List with token indices.  
        """

  
        return \[self.vocab\_encode.get(char, self.vocab\_encode\["<unk\>"\]) for char in text\]

def decode(self, indices):  
        """  
        Decode a list of token indices.Args:  
            indices (List\[int\]): List of token indices.

Returns:  
            str: The decoded text.  
        """

  
        return "".join(\[self.vocab\_decode.get(idx, "<unk\>") for idx in indices\])

Embedding
---------

While we have numeric representations of words and characters in our text, we cannot yet feed them directly into the neural network. Despite computers being able to ‘read’ and ‘understand’ our text, static numbers are not sufficient for capturing their true meanings. Let’s analyze the following words:

> Woman , Fruit , Vehicle, Car , Animal

These words are different among them, but if we try to see their relationship or similarity in a spacial visualization, we’ll probably see something like this:

![Image 5](https://miro.medium.com/v2/resize:fit:327/1*T_bxNmQHqVWU7yW2xGiwjg.png)

Word distribution based on their relationship and similarities (Image by Author).

We can imagine that most of those words are completely different, but _Car_ and _Vehicle_ are quiet similar, because, well.. car is a vehicle. This is why they are near each other. The rest of the words are spreed over the entire space because they don’t have any similarity among them.

However, this is how we perceive those words. Now, imagine trying to explain this concept to a computer, which only sees a single number for each word. It’s likely impossible for computers to comprehend this task with only a single numeric representation for each word. Hence, we need an alternative representation that can capture the meanings of words more effectively. So here is where the Embedding layers are useful.

Embedding are vector representations for our tokens, formed from learnable parameters that are adjusted during training to improve the word representation. But how do we convert a number into a vector? Imagine the Embedding layer as a **lookup table** with rows and columns. The rows correspond to the vocabulary size of our model, encompassing all possible tokens that our models could predict during generation. The columns refers to the embedding (vector) size of each token.

For example, consider the word “person” in our dataset. After tokenization, we got the number “153” to this word. This number will be used as a row-index to our lookup table. When we find the row related to that index, we’ll extract the vector stored there.

![Image 6](https://miro.medium.com/v2/resize:fit:554/1*ZI-O4-vJZfycVWubAf7egg.png)

Simple illustration of a lookup table of Embedding layer (Image by Author).

Here, we have a Embedding layer with N rows, each row correspond to a vector representation of a numeric token generated by Tokenizer. The size of each vector can be determined by us. Large vectors can learn and capture more details about words in our dataset, but it is more expensive computationally. On the other hand, small vectors is more cheap to be computed, but for large and complex dataset with a large vocabulary it might perform bad during training. Moreover, our model probably won’t capture important details about the data. The “perfect” size of an Embedding layer will be different for each dataset.

The interesting thing about Embedding layers is that they’ll learn how to represent those words in a continuous vector space based on the text feed into our neural network. After that, our model can understand the meaning of words in our text. Back to our previous example about the word similarity, if we try to compare two trained vectors, we can use a distance metric to compute how similar each vector is to the other! Normally, the _cosine distance_ is used to solve this problem.

Transformers
------------

![Image 7](https://miro.medium.com/v2/resize:fit:428/1*PCPPVL4zVCNd-49NmZ8bZg.png)

Transformer architecture.

As I said before, LLM is a [**Transformer**](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) based model. This architecture has been built initially to solve language translation problems. It is composed by a _Encoder_ and _Decoder_ block that utilizes an attention mechanism called _Scaled Dot-Product Attention_ that computes the relationship between tokens in a context.

The Encoder and Decoder block work completely different. Briefly, the Encoder block tries to analyze each word considering the entire text context. On the other hand, the Decoder block mask all future words at _t_ position and uses only the previous words available to analyze the current one. The main block of the entire Transformer that we’ll focus on is the Attention mechanism, called _Multi-Head Attention._ It is the main key of the entire LLM architecture that we’ll build soon. But first, let’s prepare our data and make it ready to be feed to our model.

Consider the sentence: _“Hi! My name is Matheus.”._ First of all, we need to tokenize this text into numeric presentation. To do so, we will need to split the text into a list of words like that:

> \[“Hi”, “!”, “ My”, “ name”, “ is”, “ Mat”, “he”, “us”, “.”\]

Well, you might be thinking “why did he split the text that way?”. I just used the _cl100k\_base_ tokenizer from [**TikTokenizer**](https://tiktokenizer.vercel.app/?model=gpt-4-1106-preview) website. After that, we need to convert those strings into a number. The _cl100k\_base_ gave to me these tokens:

> \[13347, 0, 3092, 836, 374, 7011, 383, 355, 13\]

Each token will be used as an index to our Embedding layer. Let’s assume that the vector representation of our Embedding has 5 parameters only. So, for each number, we’ll replace it by a vector of size 5.

> \[\[0.5488135 0.71518937 0.60276338 0.54488318 0.4236548 \]  
> \[0.64589411 0.43758721 0.891773 0.96366276 0.38344152\]  
> \[0.79172504 0.52889492 0.56804456 0.92559664 0.07103606\]  
> \[0.0871293 0.0202184 0.83261985 0.77815675 0.87001215\]  
> \[0.97861834 0.79915856 0.46147936 0.78052918 0.11827443\]  
> \[0.63992102 0.14335329 0.94466892 0.52184832 0.41466194\]  
> \[0.26455561 0.77423369 0.45615033 0.56843395 0.0187898 \]  
> \[0.6176355 0.61209572 0.616934 0.94374808 0.6818203 \]  
> \[0.3595079 0.43703195 0.6976312 0.06022547 0.66676672\]\]

Here we have a vector of size (9,5) where 9 refers to each token in our list above while 5 is the size of the Embedding. This will be the input data to our attention mechanism.

Attention mechanism
-------------------

![Image 8](https://miro.medium.com/v2/resize:fit:635/1*qrGVA8m-XwIp_Fry6dt9Zg.png)

Attention mechanism diagram

The Attention mechanism is referring to the _Scaled Dot-Product Attention._ As you can see, we have three data that is used as input to this block, and we call them Query, Key and Value. In our problem that involves text generation, it comes from the same source. We’ll see in practice what they are.

Each Q, K and V is computed by a linear transformation from our embedded text. Let’s ignore the second block called _Multi-Head Attention_ for now and focus only to first one. We’ll feed our attention block with our embedded text for each linear layer of Query, Key and Value. In this example, each layer will receive a vector of size (9,5) and produce a new vector of size (9,5) as well. So now we have three new representation of our data.

The first operation we’ll perform is the matrix multiplication between Query and Key. You might be asking “what is Query and Key?”. Roughly speaking, Query is the information you’re trying to looking for and Key is where you will find this information. Imagine you are in a library store and you’re looking for a specific book: this is our Query. The book you’re looking for might be stored in a bookcase: this would be our Key in this context.

Here, we’re trying to find the relationship among all tokens in our context text.

![Image 9](https://miro.medium.com/v2/resize:fit:315/1*rSu4nqEITOWN3ANe0sRxlA.png)

Token relationship in a context (Image by Author).

Both Query and Key are (9,5) vectors. During matrix multiplication, we multiply the columns of one matrix by the rows of another. So we need to make sure that the columns of Query match to the rows of Key. To do this, we need to transpose the Key matrix first, and then, multiply by Query.

> **Q = (9,5)**
> 
> **K = (9,5)**
> 
> **QK = Q \* K.t = (9,9)**

![Image 10](https://miro.medium.com/v2/resize:fit:524/1*Dq5yB3rKGqjiwF9fBMDWKA.png)

Attention matrix by Query and Key multiplication (Image by Author).

Scaling attention
-----------------

After computing the relationship among tokens, we feed them into a Softmax function that normalizes all values in rows to 0 and 1, where the sum of each row results in 1. But, before this, we need to scale them dividing by _sqrt(emb\_dim)_, where _emb\_dim_ is 9 in our example, to avoid extremely values to be passed to Softmax, that occasionally causes [**one-hot**](https://en.wikipedia.org/wiki/One-hot) vectors. Does that make any sense? Let me show an example.

Imagine we have a (1,25) tensor with these numbers:

> \[\[ 1.76405235 0.40015721 0.97873798 2.2408932 1.86755799 -0.97727788  
> 0.95008842 -0.15135721 -0.10321885 0.4105985 0.14404357 1.45427351  
> 0.76103773 0.12167502 0.44386323 0.33367433 1.49407907 -0.20515826  
> 0.3130677 -0.85409574 -2.55298982 0.6536186 0.8644362 -0.74216502  
> 2.26975462\]\]

This tensor has a normal distribution, that means that the variance of this distribution is close to 1 and the mean is close to 0 _(actually, we need to increase the number of values to see this mean and variance better)_, let’s imagine that this tensor is the result of our **_Q \* K.t_** multiplication. When we apply Softmax, the result of this tensor is:

> \[\[0.08930983 0.02283322 0.04072317 0.14387608 0.09904925 0.0057591  
> 0.03957302 0.01315369 0.01380237 0.02307288 0.01767414 0.06551851  
> 0.03275635 0.01728319 0.0238533 0.02136456 0.06817911 0.0124647  
> 0.02092881 0.00651406 0.00119133 0.02942009 0.03632461 0.00728556  
> 0.14808906\]\]

You can see that the highest number _(2.26975462)_ after the Softmax transformation was converted to 0.14808906 and the lowest number _(-2.55298982)_ became 0.00119133, if you try to sum up all these numbers you will see that it results exactly in one. Now, let’s scale those values by 10 and imagine that our **_Q \* K.t_** multiplication returned to us this scaled tensor, let’s apply Softmax again and see it results.

> \[\[3.58702875e-03 4.27970206e-09 1.39366347e-06 4.22307087e-01  
> 1.00984369e-02 4.45952862e-15 1.04648843e-06 1.72272857e-11  
> 2.78791214e-11 4.75072069e-09 3.30465511e-10 1.61950560e-04  
> 1.58014778e-07 2.64229159e-10 6.62561792e-09 2.20131429e-09  
> 2.41132545e-04 1.00591629e-11 1.79138368e-09 1.52848857e-14  
> 6.39821702e-22 5.39737202e-08 4.44376999e-07 4.68135020e-14  
> 5.63601247e-01\]\]

Well, as you can see, our well distributed probabilities disappeared now, low values became lower and the highest one became even higher, if we continue increase this scale the highest value will be approximately one whereas the rest of those probabilities will become closer to zero. To avoid this situation, one approach used by **Transformer’s Authors** is to divide the **_Q \* K.t_** result by the squared root of the embedding dimension, and in this example, the embedding dimension is 25. The reason for do it is because we unsure that our data distribution computed by Queries and Keys will have a variance approximately to one, which avoids the one-hot problem.

> **emb\_dim = 25**
> 
> **attention = (Q \* K.t) / sqrt(emb\_dim)**

Well, back to our example above, we have a (9,5) tensor referent to our text _“Hi! My name is Matheus.”._ We compute the attention matrix multiplying Query and Key, scale it by 5 _(embedding size of our tensor)_ and then we use it to multiply by Value. It’s the vector representation of the information we were looking for.

> **V = (9,5)**
> 
> **attention = (9,9)**
> 
> **Out = attention \* V = (9,5)**

Attention Mask
--------------

Back to our image above that shows the attention matrix of our text _“Hi! My name is Matheus.”_, we can see that we computed the attention for all tokens. This is an interesting thing about the _Attention Mechanism_ of Transformers because, actually, we are trying to predict every single token in our sequence and not only the last one. So our LLM can predicts with a high confidence the next token of a sequence even if it has less context than the expected.

But, during the training stage of a LLM, we want to predict the next token given a sequence of tokens as context. To do so, we need to consider just the previous token to predict the next one, right? Well, here’s a problem, because we are not doing it, but only considering the entire text during the final stage of _Attention Mechanism_, in other words. The entire attention matrix is being used to compute the new representation of our data by _attention \* V_. To solve this problem, we need to hide all consecutive tokens of all samples. We do it just by using a triangular mask and apply it over our attention matrix.

![Image 11](https://miro.medium.com/v2/resize:fit:648/1*02UQ-5wbbl9LudEmBOMWPA.png)

Attention masking (Image by Author).

Let’s implement our _Attention Mechanism_ in **Pytorch** and see it in practice! You can run this block of code on [**Google Colab**](https://colab.research.google.com/) if you want to.

torch.random.manual\_seed(seed=1234)text = "Hi! My name is Matheus."  
tokens = \[13347, 0, 3092, 836, 374, 7011, 383, 355, 13\]

vocab\_size = max(tokens) + 1   
emb\_dim = 5   
context = len(tokens)

embedding = nn.Embedding(num\_embeddings=vocab\_size, embedding\_dim=emb\_dim)  
query = nn.Linear(in\_features=emb\_dim, out\_features=emb\_dim, bias=False)  
key = nn.Linear(in\_features=emb\_dim, out\_features=emb\_dim, bias=False)  
value = nn.Linear(in\_features=emb\_dim, out\_features=emb\_dim, bias=False)

ones = torch.ones(size=\[context, context\], dtype=torch.float)  
mask = torch.tril(input\=ones)

t\_tokens = torch.tensor(data=tokens).unsqueeze(dim=0)   
x = embedding(t\_tokens)

B, T, C = x.size()  
Q = query(x)   
K = key(x)   
V = value(x)

QK = Q @ K.transpose(-2, -1) \* C\*\*-0.5   
attention = QK.masked\_fill(mask\[:T,:T\] == 0, float("-inf"))   
attention = F.softmax(input\=attention, dim=-1)

out = attention @ V

print(out.size()) 

Positional Encoding
-------------------

As all we know, the order of words in any sentence matters a lot. This is because in some cases the final meaning of text might change depending how the words are placed, especially the meaning of some words depending how it is distributed in text.

In theory, if we change the order of our token sequence, we might see a different representation to that tokens in our text, right? But if you print the _x_ variable first, then, uncomment the line 11 to reverse the entire tokens sequence and print the _x_ variable again, you’ll see that. Even the order of tokens has changed, its meaning is still the same. In other words, the vector representation for each token must be different if we change it orders.

Positional Encoding tries to solve this problem encoding each token position with a fixed value for each position. It can be made by embedding layer that learns how to encoding each position of our text. This encoding will be summed to our embedding representation of our text, and then, it’ll be feed to our model.

torch.random.manual\_seed(seed=1234)text = "Hi! My name is Matheus."  
tokens = \[13347, 0, 3092, 836, 374, 7011, 383, 355, 13\]

vocab\_size = max(tokens) + 1   
emb\_dim = 5   
context = len(tokens)

pe = nn.Embedding(num\_embeddings=context, embedding\_dim=emb\_dim)   
embedding = nn.Embedding(num\_embeddings=vocab\_size, embedding\_dim=emb\_dim)  
query = nn.Linear(in\_features=emb\_dim, out\_features=emb\_dim, bias=False)  
key = nn.Linear(in\_features=emb\_dim, out\_features=emb\_dim, bias=False)  
value = nn.Linear(in\_features=emb\_dim, out\_features=emb\_dim, bias=False)

ones = torch.ones(size=\[context, context\], dtype=torch.float)  
mask = torch.tril(input\=ones)

indices = torch.arange(context, dtype=torch.long)

t\_tokens = torch.tensor(data=tokens).unsqueeze(dim=0)   
x = embedding(t\_tokens)   
x = pe(indices) + x

B, T, C = x.size()  
Q = query(x)   
K = key(x)   
V = value(x)

QK = Q @ K.transpose(-2, -1) \* C\*\*-0.5   
attention = QK.masked\_fill(mask\[:T,:T\] == 0, float("-inf"))   
attention = F.softmax(input\=attention, dim=-1)

out = attention @ V

print(out.size()) 

If you try to run this code and print the x variable again, you’ll see that when we change the order of our tokens, its meaning changes as well.

Here, is the final code with both embedding layer and attention block:

class Embedding(nn.Module):  
    def \_\_init\_\_(self, vocab\_size, embedding\_dim):  
        """  
        Initialize the Embedding layer with Positional Encoding.Args:  
            vocab\_size (int): Size of the vocabulary.  
            embedding\_dim (int): Dimensionality of the word embeddings.  
        """

  
        super().\_\_init\_\_()  
        self.embedding = nn.Embedding(vocab\_size, embedding\_dim)  
        self.pe = nn.Embedding(vocab\_size, embedding\_dim)def forward(self, x):  
        """  
        Forward pass of the Embedding layer.Args:  
            x (torch.Tensor): Input tensor of shape (batch\_size, seq\_len).

Returns:  
            torch.Tensor: Output tensor of shape (batch\_size, seq\_len, embedding\_dim).  
        """

  
        word\_emb = self.embedding(x)  
        word\_pe = self.pe(x)  
        return word\_emb + word\_pe

class AttentionBlock(nn.Module):

def \_\_init\_\_(self, embedding\_dim, context\_size):  
        """  
        Initialize the AttentionBlock layer.Args:  
            embedding\_dim (int): Dimensionality of the word embeddings.  
            context\_size (int): Size of the context window.  
        """

  
        super().\_\_init\_\_()  
        self.query = nn.Linear(embedding\_dim, embedding\_dim, bias=False)  
        self.key = nn.Linear(embedding\_dim, embedding\_dim, bias=False)  
        self.value = nn.Linear(embedding\_dim, embedding\_dim, bias=False)

ones = torch.ones(size=\[context\_size, context\_size\], dtype=torch.float)  
        self.register\_buffer(name="mask", tensor=torch.tril(input\=ones))

def forward(self, x):  
        """  
        Forward pass of the AttentionBlock layer.Args:  
            x (torch.Tensor): Input tensor of shape (batch\_size, seq\_len, embedding\_dim).

Returns:  
            torch.Tensor: New embedding representation of shape (batch\_size, seq\_len, embedding\_dim).  
        """

  
        B, T, C = x.size()

query = self.query(x)  
        key = self.key(x)  
        value = self.value(x)

qk = query @ key.transpose(-2, -1) \* C\*\*-0.5  
        attention = qk.masked\_fill(self.mask\[:T,:T\] == 0, float("-inf"))  
        attention = F.softmax(input\=attention, dim=-1)

out = attention @ value  
        return out

Multi Head Attention
--------------------

Instead of perform a single attention block, we can perform multiple attention blocks in parallel and then concatenate their results. In practice, each Head _(attention block)_ has separated learnable parameters and they will try to find different relevant information about our data simultaneously. It is important to mention that each Head will compute a chunk of the embedding fed to the attention block, and the number of Heads must be divisible by the embedding size.

class MultiAttentionBlock(nn.Module):def \_\_init\_\_(self, embedding\_dim, num\_heads, context\_size):  
        """  
        Initialize the MultiAttentionBlock layer.Args:  
            embedding\_dim (int): Dimensionality of the word embeddings.  
            num\_heads (int): Number of attention heads.  
            context\_size (int): Size of the context window.  
        """

  
        super().\_\_init\_\_()

head\_dim = embedding\_dim // num\_heads  
        assert head\_dim \* num\_heads == embedding\_dim, "Embedding dimension must be divisible by number of heads"

self.attention = nn.ModuleList(modules=\[AttentionBlock(embedding\_dim, head\_dim, context\_size) for \_ in range(num\_heads)\])  
        self.linear = nn.Linear(in\_features=embedding\_dim, out\_features=embedding\_dim)

def forward(self, x):  
        """  
        Forward pass of the MultiAttentionBlock layer.Args:  
            x (torch.Tensor): Input tensor of shape (batch\_size, seq\_len, embedding\_dim).

Returns:  
            torch.Tensor: New embedding representation of shape (batch\_size, seq\_len, embedding\_dim).  
        """

  
        out = torch.cat(tensors=\[attention(x) for attention in self.attention\], dim=-1)  
        x = self.linear(x)  
        return x

To prevent problems like vanishing gradients, we normally apply a skip-connection after the Multi-Head-Attention block. Then, we apply a Batch normalization and feed a Fully-Connected-Neurons to help the model to process the useful information extracted from previous block before feed it again to another Attention block ahead. The Transformer diagram above shows how this workflow works.

class FeedForward(nn.Module):def \_\_init\_\_(self, embedding\_dim, ff\_dim):  
        """  
        Initialize the feed forward layer.Args:  
            emb\_dim (int) : The dimension of the embedding.  
            ff\_dim (int) : The dimension of the feed forward layer.  
            dropout\_rate (float) : The dropout rate. (default: 0.2)  
        """

  
        super().\_\_init\_\_()  
        self.linear\_1 = nn.Linear(embedding\_dim, ff\_dim)  
        self.relu = nn.ReLU()  
        self.linear\_2 = nn.Linear(ff\_dim, embedding\_dim)

def forward(self, x):  
        """  
        Forward pass of the feed forward layer.Args:  
            x (torch.Tensor) : The input tensor.

Returns:  
            torch.Tensor : The output tensor.  
        """

  
        x = self.linear\_1(x)  
        x = self.relu(x)  
        x = self.linear\_2(x)  
        return x

class DecoderLayer(nn.Module):

def \_\_init\_\_(self, embedding\_dim, head\_dim, context\_size, ff\_dim):  
        """  
        Initialize the decoder layer.Args:  
            embedding\_dim (int): Dimensionality of the word embeddings.  
            head\_dim (int): Dimensionality of each head.  
            context\_size (int): Size of the context window.  
            ff\_dim (int): Dimensionality of the feed-forward layer.  
        """

  
        super().\_\_init\_\_()  
        self.attention = MultiAttentionBlock(embedding\_dim, head\_dim, context\_size)  
        self.feed\_forward = FeedForward(embedding\_dim, ff\_dim)  
        self.norm\_1 = nn.LayerNorm(normalized\_shape=embedding\_dim)  
        self.norm\_2 = nn.LayerNorm(normalized\_shape=embedding\_dim)

def forward(self, x):  
        """  
        Forward pass of the decoder layer.Args:  
            x (torch.Tensor) : The input tensor.

Returns:  
            torch.Tensor : The output tensor.  
        """

  
        x\_norm = self.norm\_1(x)  
        attention = self.attention(x\_norm)  
        attention = attention + x

attention\_norm = self.norm\_2(attention)  
        ff = self.feed\_forward(attention\_norm)  
        ff = ff + attention

return ff

![Image 12](https://miro.medium.com/v2/resize:fit:700/1*rNUNg-5fIq2aeJDgL3867A.png)

Medium Article Generator project (Image by Author).

Recently, I trained and tested my own LLM using Pytorch. My objective was to develop a [**Medium Article Generator**](https://github.com/MTxSouza/MediumArticleGenerator), a model that receives a title and generate text related to that title.

Train LLM from scratch is hard because the high computational resource. It requires a large GPU memory for training and high RAM memory to load and preprocess large dataset to train it. It is important to mention it requires hours of training because the large number of parameters to be trained and a large text dataset to be used in training.

I won’t go to full details about the development process but just explain and show important parts about the project.

Dataset
-------

The dataset used was the [Medium Articles](https://www.kaggle.com/datasets/fabiochiusano/medium-articles) from **Kaggle.** It is a public dataset and it has around 190 thousands articles from Medium with a title and an article related to that title. In general, I was not expecting the model to generate text related to every single topic in the world. The dataset used has a limited content about some topics.

![Image 13](https://miro.medium.com/v2/resize:fit:1000/1*lGo_WlTVi8n7LwvjjMPbrQ.png)

Article topics in dataset (Image by Author).

I excluded articles with non-utf-8 characters and some based on a length condition, which reduced the number of samples for training.

LLM from scratch
----------------

First, I decided to train it from scratch, training the entire neural net, even its embedding layers for word representations. My tokenize algorithm was based on a simple regex that splits the text following a pattern rule. The regex function divides sequence of characters from punctuation and numbers.

Then, my approach was to delimited title and article, telling to the model where the title and article starts and ends. After that, I added padding tokens to each article to standardize the length of the data to be feed to the model.

During data preprocessing, I stored all new tokens into a vocabulary dictionary and create an index to refers to take new token. I limited my vocabulary size to 50K~80K tokens, just to control the number of parameters required to train the embedding layer.

I used some regularization methods like Dropout layers with rate of 10% and Weight-Decay of 0.0001 to avoid my model to _overfitting_. It was trained on a RTX 4090 with 24Gb for 15 hours. I used _Cross-Entropy_ loss to predict each token in each position and I used the _Accuracy_ metric to evaluate the quality of my generation.

![Image 14](https://miro.medium.com/v2/resize:fit:1000/1*YI75cOnWYMNya8qprGPz3g.png)

Loss graph of the LLM trained from scratch (Image by Author).

During inference, the model could complete the text quiet well but just for a few tokens. During long generations, it started to complete the input text, but then it repeated the same sentence it predicted before infinitely.

GPT-2 Pre-Trained Embedding + Decoder
-------------------------------------

I experimented with using the pre-trained Embedding layer of OpenAI’s GPT-2, which contains pre-computed word representations. This reduced training time to just one hour and lowered resource requirements for training the rest of the model.

To achieve this, I used the Transformer library to load both the tokenizer and embedding from GPT-2. However, I encountered a limitation with the GPT-2 tokenizer, it only includes the _<|endoftext|\>_ special token, which solely marks the end of text. Ideally, I would have liked to specify the start of the article as well and potentially add padding to standardize article lengths.

Given this constraint, my approach with GPT-2 involved simply concatenating the title and article. I then used the _<|endoftext|\>_ token to pad the text, even though this approach of not specifying the start and end of text sections may seem unconventional. Surprisingly, it yielded positive results. While I tested other tokenizers and embeddings like **BERT**, **T5**, and **RoBERTa**, GPT-2 achieved the best performance and fastest training times.

![Image 15](https://miro.medium.com/v2/resize:fit:1000/1*3_Bnv_6ublEGTTem017Isg.png)

Loss graph of the LLM trained with GPT-2 pre-trained embedding layer (Image by Author).

> The final mode results and its text generation performance can be found in my [**GitHub repository**](https://github.com/MTxSouza/MediumArticleGenerator).

Final considerations
--------------------

In this exploration, we delved into the inner workings LLM and demonstrated the process of building one from scratch. My personal project served as a practical example, showcasing the results achievable with limited hardware and a focused dataset. While achieving peak performance wasn’t possible under these constraints, the project yielded valuable insights and improvements.

The project highlighted the impact of hardware and dataset size on LLM performance. It served as a valuable learning experience, allowing me to explore the trade-offs involved in LLM development.

For those interested in further exploration, [Andrej Karpathy](https://medium.com/u/ac9d9a35533e?source=post_page-----9f21808c6319--------------------------------)’s video on building LLMs from scratch provides excellent material:

In conclusion, this exploration provided a practical introduction to LLM and the considerations involved in their development.

Thank you for reading!

