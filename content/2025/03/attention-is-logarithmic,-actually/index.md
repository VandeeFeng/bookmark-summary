---
title: attention is logarithmic, actually
date: 2025-03-23
extra:
  source: https://supaiku.com/attention-is-logarithmic
  original_title: attention is logarithmic, actually
---
## Summary
**摘要**：
本文作者探讨了在并行计算时代，时间复杂度作为衡量算法快慢的标准已经不再适用。作者主张使用work-depth模型来分析算法复杂度，work指的是算法执行的操作总数，depth指的是计算图中不可并行化的最小操作数。文章通过分析元素级乘法、向量求和、张量积、矩阵乘法和Softmax等操作的depth复杂度，论证了在Transformer中实现的vanilla attention机制，其计算复杂度应被视为对数级别。文章指出，元素级乘法具有常数级depth，向量求和的depth复杂度为O(log n)，矩阵乘法为O(log n)，而attention机制的depth复杂度为O(log n + log d)，其中n为序列长度，d为嵌入维度。然而，作者也承认depth分析存在局限性，它忽略了内存访问模式和缓存友好性。当张量过大无法放入L2缓存时，attention的实际depth复杂度可能退化为O(n log n)。最后，作者推测未来芯片设计将更多地考虑权重数据的局部性，以优化深度学习模型的性能。

**要点总结**：
1.  **时间复杂度的局限性**：在单核时代，时间复杂度是衡量算法效率的有效指标。然而，随着多核处理器的普及，时间复杂度无法区分可高度并行化和不可并行化的算法，因此不再适用。
2.  **Work-Depth模型**：Work-Depth模型是分析并行算法复杂度的有效方法。Work指的是算法执行的总操作数，Depth指的是计算图中依赖关系最长的路径，即最少的不可并行化的操作步骤。通过关注Depth，可以更好地理解算法在并行环境下的性能瓶颈。
3.  **基本运算的Depth分析**：文章分析了元素级乘法、向量求和（contraction）、张量积和矩阵乘法等基本运算的Depth复杂度。元素级乘法Depth为O(1)，向量求和Depth为O(log n)，张量积Depth为O(1)，矩阵乘法Depth为O(log n)，为后续分析Attention机制的复杂度奠定了基础。
4.  **Attention机制的Depth复杂度**：通过将Attention机制分解为矩阵乘法、Softmax等基本操作，文章得出结论：Attention机制的Depth复杂度为O(log n + log d)，其中n为序列长度，d为嵌入维度。这意味着在理想情况下，Attention机制的计算效率很高。
5.  **Depth分析的局限性与未来展望**：Depth分析忽略了内存访问模式和缓存大小等因素。在实际应用中，由于QK^T矩阵过大，无法完全放入L2缓存，导致Attention机制的性能下降。未来芯片设计应更多考虑权重数据的局部性，将权重数据存储在更快的存储器上，以提高计算效率。

## Full Content
Title: attention is logarithmic, actually

URL Source: https://supaiku.com/attention-is-logarithmic

Markdown Content:
### [supaiku dot com](https://supaiku.com/)

* * *

> time complexity is a very bad model when working with parallelism.
> 
> in which i make the case for [work-depth](https://en.wikipedia.org/wiki/Analysis_of_parallel_algorithms) analysis instead of [time complexity](https://en.wikipedia.org/wiki/Time_complexity).

* * *

[time complexity](https://en.wikipedia.org/wiki/Time_complexity) is the default model brought up when discussing whether an algorithm is “fast” or “slow”.

back in the 80s, when every computer had only one core and no one besides a couple of [weirdos](https://en.wikipedia.org/wiki/Thinking_Machines_Corporation) knew what a [SIMD](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) was, this was largely correct.

but the year is now 2025. it is very hard to find computers with a single core. even smartphones have 4-8 cores \[source needed\]. as a result, time complexity largely fails as a measure of how fast or slow certain algorithms are.

using time complexity, there is no way to distinguish between an algorithm that requires O(n^3) operations that is [embarrassingly parallel](https://en.wikipedia.org/wiki/Embarrassingly_parallel) , versus one that is irreducibly sequential

worse yet, time complexity is sometimes still used to describe inherently parallel algorithms, such as every [linear algebra operation ever](https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication).

this is ridiculous. we need a better way to think about the “complexity” of different algorithms. the [work-depth model](https://www.cs.cmu.edu/~scandal/cacm/node1.html) of analysis provides a good level of abstraction for thinking about the theoretical lower bound complexity of algorithms not as the number of operations with respect to input size.

instead of thinking about the raw numbers of operations an algorithm performs, or **work**, it’s better to think about the **depth** of the computation graph with respect to input size, or in other words, the minimum number of non-parallelizable sequential operations. as these are irreducibly blocking, no matter how many cores you have in your computer.

my expertise is mostly in performance engineering of ml systems, so the focus of this article will mostly relate to algorithms that apply to tensors.

this model is not perfect, and i will detail why in a [later section](https://supaiku.com/attention-is-logarithmic#limitations), but to start off, the best question to ask is:

> what is the time complexity of element wise multiplication?

from which we will eventually work up to my thesis, which is that **vanilla** attention as it is implemented in transformers, should be considered logarithmic in computational complexity.

* * *

case 1: element wise multiplication
-----------------------------------

given a vector a and a vector b with the same number of elements.

element wise multiplication takes every element in a and multiplies it with the matching index in b and stores it in a new vector c (or in place)

the pseudo code will look like:

```
n   = <big integer>
a,b = arange(n), arange(n)
c   = zeros(n)
for i in range(n):
  c[i] = a[i] * b[i]
```

time complexity wise, this is obviously linear. and performed on a single thread, this is true!

however if you take a closer look, you’ll realize that in the computation graph of this problem, none of the steps in range(n) depend on one another. they’re entirely independent.

so ... why not do them in parallel?

which is exactly what every linear algebra/tensor library does under the hood.

and you quickly find out that, the problem isn’t linear at all! it actually looks like constant time until a mysterious cutoff point (that we will detail later).

more concretely, we can analyze the work and depth of element wise multiplication:

```
+-------+-------+-------------------+------+
|   OP  | DEPTH |       INPUT       | WORK |
+-------+-------+-------------------+------+
|       |       |                   |      |
|  LOAD |   1   | [a_1 a_2 ... a_i] |  n   |
|  LOAD |   1   | [b_1 b_2 ... b_i] |  n   |
|  MUL  |   1   |    *  *      *    |  n   |
| STORE |   1   | [c_1 c_2 ... c_i] |  n   |
|       |       |                   |      |
+-------+-------+-------------------+------+
| TOTAL |   4   |                   |  4n  |
|       |       |                   |      |
| ASYMP |  O(1) |                   | O(n) |
+-------+-------+-------------------+------+
```

every operation required in the algorithm: load, mul, store, all have constant depth, and given enough parallel compute (up to the magical cutoff point mentioned above), all of them can effectively be done in constant time.

* * *

case 2: vector summation (aka contraction)
------------------------------------------

summation (henceforth referred to as CONTRACT)

is a bit more complicated than elementwise operations. here, we clearly see that there is a dependency between two steps (since accumulation requires calling into c’s state). and this cannot be done emberassingly in parallel.

```
n = <big integer>
a = arange(n)
c = 0
for i in range(n):
  c += a[i]
```

fortunately though, if you look a bit closer, you’ll realize that this is only a dependency between every _two_ steps, or pairs.

it is in fact still possible to parallelize this operation, by instead of doing every elementwise operation in parallel in one step, doing every **pairwise** operation in one step.

for a list of length n, the progression is as follows:

1.  sum up every adjacent even and odd pair of numbers in the list (there are n/2 of such pairs), and store them into either the even or odd index of the pair.
    
2.  sum up every adjacent **summed pair**, and do the same index trick (there are n/4 of such pairs of pairs)
    
3.  pairs of pairs of ... pairs
    
4.  after log\_2(n) steps, you’ll have a single number that is the sum every element in the list.
    

```
+------------+----------+---------------------------------------+------+
|     OP     |  DEPTH   |                 INPUT                 | WORK |
+------------+----------+---------------------------------------+------+
|            |          |                                       |      |
|    LOAD    |    1     | [a_1     a_2     a_3     a_4  ⋯  a_i] | n/2  |
|            |          |      \     /       \     /       /    |      |
| PAIRWISE + |    1     |     [a_1+a_2         a_3+a_4   ⋯  ]   | n/4  |
|            |          |           \           /        /      |      |
| PAIRWISE + |    1     |          [(a_1+a_2)+(a_3+a_4) ⋯ ]     | n/8  |
|            |          |                    \   /              |      |
|     ⋯      |    ⋯     |                      ⋯                |  ⋯   |
|            |          |                      |                |      |
| PAIRWISE + |    1     |                    [∑a]               |  1   |
|   STORE    |    1     |                    [∑a]               |  1   |
|            |          |                                       |      |
+------------+----------+---------------------------------------+------+
|   TOTAL    | (logn)+1 |                                       | n+1  |
|            |          |                                       |      |
|   ASYMP    | O(log n) |                                       | O(n) |
+------------+----------+---------------------------------------+------+
```

* * *

case 3: tensor product
----------------------

```
+-------+-------+-------------------------------+---------+
|   OP  | DEPTH |             INPUT             |   WORK  |
+-------+-------+-------------------------------+---------+
|       |       |                               |         |
|  LOAD |   1   |   [a_11 a_12 ⋯ a_1j ⋯ a_ij]   |    n²   |
|  LOAD |   1   |   [b_11 b_12 ⋯ b_1k ⋯ b_jk]   |    n²   |
|  MUL  |   1   |       *   *     *     *       |    n³   |
| STORE |   1   | [c_111 c_112 ⋯ c_1jk ⋯ c_ijk] |    n³   |
|       |       |                               |         |
+-------+-------+-------------------------------+---------+
| TOTAL |   4   |                               | 2n²+2n³ |
|       |       |                               |         |
| ASYMP |  O(1) |                               |  O(n³)  |
+-------+-------+-------------------------------+---------+
```

the [tensor product](https://en.wikipedia.org/wiki/Tensor_product) (henceforth called TENSOR) is a fundamental operation on tensors. basically, it takes all indeces of two tensors and does element wise multiplication over all of the requested indeces, (some of which can be shared).

in the case of the tensor product of two matrices with one shared axis, this materializes a cubic tensor. but since the only operations required are a parallel load, store and elementwise multiplication, this also has constant depth.

caveat: it only has constant depth only if the materialized tensor (or the materialized sections) fits neatly into cache). every time the tensor doesn’t fit into cache, this becomes an irreducible depth and the problem becomes at least sequential at that cache level.

the tensor product is not talked about very often in machine learning, but it is a much more elegant way to think about most tensor operations than the 20+ ways of thinking about tensors.

instead of having permute, sum, matmul, hadamard product, direct product, every batched operation, etc etc. everything is just some variant of tensor product -\> some variant of contraction.

* * *

case 4: matrix multiplication
-----------------------------

the [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication) (MATMUL), is one such tensor operation that is elegantly described using the tensor product into a contraction.

given two tensors A,B of dimensionality (i j) and (j k), the tensor product constructs a tensor C that has elements C\[i,j,k\] = A\[i,j\] \* B\[j,k\], and then sums (contracts) along the j dimension into a matrix D of shape (i k). (for efficiency, C is usually never fully materialized, instead the contraction is fused between shards of the tensor product)

this can be trivially batched / broadcasted by simply ignoring the outer axes. in short, the matmul is described as

```
einsum("...ij, ...jk -> ...ik", A, B)
```

pseudocode for stuff under the hood:

```
A = some matrix of shape (i j)
B = some matrix of shape (j k)
C = zeros of shape (i j k)

for _i in range i:
  for _j in range j:
    for _k in range k:
      C[_i,_j,_k] = A[_i,_j] * B[_j,_k] # element wise multiply


D = zeros of shape (i k)

for _i in range i:
  for _j in range j:
    for _k in range k:
      D[_i,_k] += C[_i,_j,_k]           # contraction

```

note that this is just a sequential composition of TENSOR into CONTRACT, which have depth complexity O(1) and O(logn) respectively:

```
+----------+----------+---------------------------+---------+
|    OP    |  DEPTH   |           INPUT           |   WORK  |
+----------+----------+---------------------------+---------+
|          |          |                           |         |
|   LOAD   |    1     | [a_11 a_12 ⋯ a_1j ⋯ a_ij] |    n²   |
|   LOAD   |    1     | [b_11 b_12 ⋯ b_1k ⋯ b_jk] |    n²   |
|  TENSOR  |    1     |        "ij,jk->ijk"       |    n³   |
| CONTRACT |  log n   |         "ijk->ik"         |    n³   |
|  STORE   |    1     | [d_11 d_12 ⋯ d_1k ⋯ d_ik] |    n²   |
|          |          |                           |         |
+----------+----------+---------------------------+---------+
|  TOTAL   | (logn)+4 |                           | 2n²+2n³ |
|          |          |                           |         |
|  ASYMP   | O(log n) |                           |  O(n³)  |
+----------+----------+---------------------------+---------+
```

* * *

case 5: softmax
---------------

softmax is not at all special. elementwise application of e^x, followed by a contraction, followed by a element wise division.

here’s the depth complexity analysis as usual:

```
+-------+----------+-------------+------+
|   OP  |  DEPTH   |    INPUT    | WORK |
+-------+----------+-------------+------+
|       |          |             |      |
|  LOAD |    1     |    x ∈ ℝⁿ   |  n   |
|  MAX  |  log n   |  m = max(x) |  n   |
|  SUB  |    1     |  x' = x - m |  n   |
|  EXP  |    1     | e = exp(x') |  n   |
|  SUM  |  log n   |  s = sum(e) |  n   |
|  DIV  |    1     |  y = e / s  |  n   |
| STORE |    1     |    y ∈ ℝⁿ   |  n   |
|       |          |             |      |
+-------+----------+-------------+------+
| TOTAL | 2log n+5 |             |  7n  |
|       |          |             |      |
| ASYMP | O(log n) |             | O(n) |
+-------+----------+-------------+------+
```

* * *

case 6: attention
-----------------

and without further ado, attention. at this point we’re probably already used to the composition. here’s the depth analysis:

```
+---------+------------+--------------------------------+---------+
|    OP   |   DEPTH    |             INPUT              |   WORK  |
+---------+------------+--------------------------------+---------+
|   LOAD  |     1      |           X ∈ ℝᵇˣⁿˣᵈ           |   bnd   |
|   LOAD  |     1      |        Wq,Wk,Wv ∈ ℝᵈˣᵈ         |   3d²   |
|  MATMUL |   3log d   | Q = X·Wq ; K = X·Wk ; V = X·Wv |  3bnd²  |
|  MATMUL |   log d    |            S = Q·Kᵀ            |   bn²d  |
|   DIV   |     1      |          S' = S / √d           |   bn²   |
| SOFTMAX |   log n    |        A = softmax(S')         |   bn²   |
|  MATMUL |   log n    |            O = A·V             |   bn²d  |
|  STORE  |     1      |           O ∈ ℝᵇˣⁿˣᵈ           |   bnd   |
|         |            |                                |         |
+---------+------------+--------------------------------+---------+
|  TOTAL  |  4log d +  |                                |  ≈ bn²d |
|         | 2log n + 5 |                                |         |
|         |            |                                |         |
|  ASYMP  |  O(logn +  |                                | O(bn²d) |
|         |    logd)   |                                |         |
+---------+------------+--------------------------------+---------+
```

as we can see, through the sequential composition of an integer number of matmuls contractions, and a bunch of elementwise unary ops, attention has asymptotic depth complexity of just O(logn + logd), where n and d are sequence length and embedding dim respectively.

in practice, this usually means O(log sequence\_length), since sequence\_length is usually far greater than embedding\_dim.

limitations
-----------

however, depth analysis isn’t perfect, and the problem becomes immediately apparent when taking into account memory access patterns and cache friendliness.

in particular, this model fails when:

*   max width of tree \>\> computation units (whatever cores are).
*   memory access patterns are not contiguous / vectorizable?
*   materialized variables don’t play nice with memory hierarchy.

in practice, this mostly means that the size of your materialized tensors must stay within L2-ish cache for the depth complexity bounds to hold. nice memory patterns usually come for free for (dense) tensors.

so why isn’t attention logarithmic?
-----------------------------------

the truth is, since attention requires at least partially materializing QK^T (which is usually (very big integer, very big integer) this will almost certainly overfill your L2 cache (which either forces you to do compute in memory an OOM slower, or, forces you to turn it into a sequential problem by **sharding the QK^T matrix into partially associative chunks to pass into softmax**[1](https://supaiku.com/attention-is-logarithmic#user-content-fn-1)).

which means that for regular computers, the depth complexity for attention is more something like O(n log n). though this in no way is an irreducible problem, for which i have some speculative solutions in the next section.

speculations on future compute?
-------------------------------

so, what does this mean for current chips and future chips?

i think it means quite a lot, assuming one key fact, **that training paradigms remain largely non-concurrent** (i.e looks like forward -\> backward passes on a loop, or some mix like [dualpipe](https://github.com/deepseek-ai/DualPipe))

why? because if this is the case, then the weights of the neural net (what makes up the majority of the volume of movement ops in a nn pass) are largely static, and can have increasing amounts of locality to compute units.

we already see this happening. weights used to be offloaded to disk, or saved to ram, and only launched to the gpu for specialized kernels.

then everyone and their grandma started training fully on device memory (VRAM or HBM).

and now chip manufacturers have caught on, and realized that they can get another OOM (by effectively chopping off whole sections where the depth complexity analysis fails) by moving weights onto even faster memory, like L2. (**cough**, gr\*q).

* * *

```
@misc{doan2025attnislogarithmic,
  title = {Attention is logarithmic, actually},
  url = {https://supaiku.com/attention-is-logarithmic},
  year = {2025}
}
```

1.  this is my reductionist take for what flash attention is. [↩](https://supaiku.com/attention-is-logarithmic#user-content-fnref-1)

