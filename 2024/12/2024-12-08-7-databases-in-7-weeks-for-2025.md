# 7 Databases in 7 Weeks for 2025
- URL: https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/
- Added At: 2024-12-08 04:39:57
- [Link To Text](2024-12-08-7-databases-in-7-weeks-for-2025_raw.md)

## Summary
**摘要**：
本文由 Matt 进行撰写，强调了在2025年花一周时间深入了解7种数据库技术的潜在价值。这7个数据库分别是 PostgreSQL、SQLite、DuckDB、ClickHouse、FoundationDB、TigerBeetle 和 CockroachDB。目标是建议工程师和数据专家探索可能未深入了解到的技术，并通过文章的内容引领读者理解、评价这7种数据库的特点和适用场景。

每个数据库的单独简介涵盖了它们提供的技术关键特点、应用焦点以及对比其他常用数据库的优势或独特之处。例如，对 PostgreSQL 强调了其在“无趣技术”领域的稳定性能，SQLMain 特性丰富且支持广泛；对 ClickHouse 则从其建立的易于操作系统和大型数据集实时分析的优势；FoundationDB 则以其有序键值存储的独特架构和高级安全性得到强调；而 CockroachDB 则在于其全球分布式能力，并具有强一致性和横向扩展性。

**要点总结**：
1. **PostgreSQL**：针对默认模型的全面数据库，含有丰富的扩展特性，支持图形数据结构、时间序列数据处理，强大的生态系统，以及用于移植或替代基于客户端的模型的WebAssembly安装。
   - 实施简单 CRUD 应用，实验 Postgres 扩展。
2. **SQLite**：本地优先的数据库，直接与应用程序共享驻于同一设备。展示如何导入大文件并进行效率提升，如通过 Litestream 或 LiteFS。 
   - 实验本地优先架构，迁移从 Postgres 到完全依赖 SQLite 的方法。
3. **DuckDB**：支持SQL查询、从各种格式快速导入数据，包括CSV、TSV、JSON、Parquet等，为数据分析提供灵活工具和大数据集查询。
   - 用于解决分析大型数据集或实时查询的速度问题，对比基础的DB。
4. **FoundationDB**：构筑基础的数据库，经验丰富的用户能够实现全介质的ACID事务，既具局限也带来灵活性，支持通用工作负载的测试和模拟。
   - 熟悉基础架构概念、使用教程、核心文档和可重构功能，理解独特语言（如Zig）的运用。
5. **TigerBeetle**：为金融交易所设计的精准数据库，确保写入数据绝对可靠，安全性和严格并发控制，通过流行的Zig语言构建。
   - 进行基于本地的金融账户模型构建，学习Tiger Style程序风格。
6. **ClickHouse**：高度优化的流式数据库，专门用于在线分析处理，处理大数据集的分析，提供解决问题的方法。
   - 分析复杂查询需求，对比嵌入式ClickHouse与常规SQL数据库的日常操作。
7. **CockroachDB**：专注于全球分布的数据库系统，与谷歌的Spanner系统相一致，以保证低延迟性和数据一致性的高可用性。
   - 重新实现CockroachDB的示例应用（例如movr），以新技术语言和框架进行。
