# The Best Way to Use Text Embeddings Portably is With Parquet and Polars
- URL: https://minimaxir.com/2025/02/embeddings-parquet/
- Added At: 2025-02-25 04:11:17
- [Link To Text](2025-02-25-the-best-way-to-use-text-embeddings-portably-is-with-parquet-and-polars_raw.md)

## Summary
**摘要**：
本文探讨了在处理文本嵌入时，如何以一种便携且非专有的格式存储和使用它们，避免对向量数据库的过度依赖。作者以自己创建的Magic: The Gathering卡牌的文本嵌入为例，展示了文本嵌入在识别卡牌之间的相似性以及通过UMAP进行数据降维和聚类方面的应用。文章对比了几种存储嵌入的方法，包括CSV、Numpy的.txt格式、Python的pickle以及Numpy的.npy格式，指出它们在存储效率、读写速度和安全性方面存在不足。作者推荐使用Parquet文件，并详细介绍了如何使用pyarrow和polars库来高效地读写Parquet文件。其中，polars库因其对嵌套数据的良好支持和与numpy的无缝集成，成为处理嵌入的理想选择。通过polars，可以轻松地将元数据与嵌入一同存储，实现快速的相似性搜索和灵活的元数据过滤。最后，作者还讨论了在数据量较大时，可以考虑使用SQLite数据库及其sqlite-vec扩展作为替代方案。

**要点总结**：

1.  **文本嵌入的应用**：文本嵌入是一种将文本数据转换为数值向量的技术，它可以捕捉文本的语义信息，从而实现文本相似度计算、聚类和分类等任务。作者通过Magic: The Gathering卡牌的例子，展示如何使用卡牌名称、描述等信息生成嵌入，并利用这些嵌入找到相似的卡牌，或者进行聚类分析。
2.  **存储嵌入的挑战**：存储文本嵌入需要考虑存储效率、读写速度、数据可移植性和元数据管理等因素。传统的CSV、pickle等格式存在存储空间大、读写速度慢、安全性差等问题。
3.  **Parquet文件的优势**：Parquet是一种列式存储格式，能够高效地存储和读取结构化数据，包括嵌套的列表数据，非常适合存储文本嵌入。Parquet文件不仅节省存储空间，还支持快速的列式读取，方便进行数据分析和处理。
4.  **polars库的强大功能**：polars是一个用Rust编写的Python库，专门用于处理表格数据。它支持Arrow columnar内存格式，能够高效地读取和写入Parquet文件。更重要的是，polars对嵌套数据有很好的支持，可以直接将嵌入存储为数组，避免了pandas在处理嵌套数据时的性能问题。
5.   **在实际项目中使用polars和Parquet的建议**：对于小型或非商业项目，可以考虑使用polars和Parquet文件来存储和处理文本嵌入，而无需依赖复杂的向量数据库。polars提供了快速的相似性搜索和灵活的元数据过滤功能，能够满足大多数应用的需求。对于大规模的商业项目，向量数据库可能更适合，但polars和Parquet仍然是很好的数据预处理和探索工具。

