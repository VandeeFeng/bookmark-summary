# attention is logarithmic, actually
- URL: https://supaiku.com/attention-is-logarithmic
- Added At: 2025-03-23 11:31:14
- [Link To Text](2025-03-23-attention-is-logarithmic,-actually_raw.md)

## Summary
**摘要**：
本文作者探讨了在并行计算时代，时间复杂度作为衡量算法快慢的标准已经不再适用。作者主张使用work-depth模型来分析算法复杂度，work指的是算法执行的操作总数，depth指的是计算图中不可并行化的最小操作数。文章通过分析元素级乘法、向量求和、张量积、矩阵乘法和Softmax等操作的depth复杂度，论证了在Transformer中实现的vanilla attention机制，其计算复杂度应被视为对数级别。文章指出，元素级乘法具有常数级depth，向量求和的depth复杂度为O(log n)，矩阵乘法为O(log n)，而attention机制的depth复杂度为O(log n + log d)，其中n为序列长度，d为嵌入维度。然而，作者也承认depth分析存在局限性，它忽略了内存访问模式和缓存友好性。当张量过大无法放入L2缓存时，attention的实际depth复杂度可能退化为O(n log n)。最后，作者推测未来芯片设计将更多地考虑权重数据的局部性，以优化深度学习模型的性能。

**要点总结**：
1.  **时间复杂度的局限性**：在单核时代，时间复杂度是衡量算法效率的有效指标。然而，随着多核处理器的普及，时间复杂度无法区分可高度并行化和不可并行化的算法，因此不再适用。
2.  **Work-Depth模型**：Work-Depth模型是分析并行算法复杂度的有效方法。Work指的是算法执行的总操作数，Depth指的是计算图中依赖关系最长的路径，即最少的不可并行化的操作步骤。通过关注Depth，可以更好地理解算法在并行环境下的性能瓶颈。
3.  **基本运算的Depth分析**：文章分析了元素级乘法、向量求和（contraction）、张量积和矩阵乘法等基本运算的Depth复杂度。元素级乘法Depth为O(1)，向量求和Depth为O(log n)，张量积Depth为O(1)，矩阵乘法Depth为O(log n)，为后续分析Attention机制的复杂度奠定了基础。
4.  **Attention机制的Depth复杂度**：通过将Attention机制分解为矩阵乘法、Softmax等基本操作，文章得出结论：Attention机制的Depth复杂度为O(log n + log d)，其中n为序列长度，d为嵌入维度。这意味着在理想情况下，Attention机制的计算效率很高。
5.  **Depth分析的局限性与未来展望**：Depth分析忽略了内存访问模式和缓存大小等因素。在实际应用中，由于QK^T矩阵过大，无法完全放入L2缓存，导致Attention机制的性能下降。未来芯片设计应更多考虑权重数据的局部性，将权重数据存储在更快的存储器上，以提高计算效率。

