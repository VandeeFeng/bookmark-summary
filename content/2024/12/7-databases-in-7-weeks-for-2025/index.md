---
title: 7 Databases in 7 Weeks for 2025
date: 2024-12-08
extra:
  source: https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/
  original_title: 7 Databases in 7 Weeks for 2025
---
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
## Full Content
Title: 7 Databases in 7 Weeks for 2025

URL Source: https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/

Markdown Content:
I’ve been running databases-as-a-service for a long time, and there are always new things to keep abreast of - new technologies, different ways of solving problems, not to mention all the research coming out of universities. In 2025, consider spending a week with each of these database technologies.

![Image 3: A line drawing of a bookshelf, with the books labelled for each database covered - PostgreSQL, SQLite, DuckDB, ClickHouse, FoundationDB, TigerBeetle and CockroachDB](https://matt.blwt.io/7-databases-in-7-weeks-for-2025/header.webp)

Preamble
--------

These aren’t the “7 Best Databases” or something similar to power a Buzzfeed listicle - these are just 7 databases that I think are worth your time to really look into for a week or so. You might ask something like “why not Neo4j or MongoDB or MySQL/Vitess or <insert other db here\>” - the answer is mostly that I don’t find them interesting. I’m also not covering Kafka or other similar streaming data services - definitely worth your time, but not covered.

This post was inspired by the original book [7 Databases In 7 Weeks](https://7dbs.io/) by Luc Perkins with Eric Redmond and Jim Wilson.

Table of Contents
-----------------

1.  [PostgreSQL](https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/#1-postgresql)
2.  [SQLite](https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/#2-sqlite)
3.  [DuckDB](https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/#3-duckdb)
4.  [ClickHouse](https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/#4-clickhouse)
5.  [FoundationDB](https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/#5-foundationdb)
6.  [TigerBeetle](https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/#6-tigerbeetle)
7.  [CockroachDB](https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/#7-cockroachdb)

*   [Wrap Up](https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/#wrap-up)

1\. PostgreSQL
--------------

### The Default Database

“Just use Postgres” is basically a meme at this point, and for good reason. [PostgreSQL](https://www.postgresql.org/) is the pinnacle of [boring technology](https://boringtechnology.club/), and should be the database you reach for when you need a client-server model for your database. ACID compliant, plenty of interesting tricks for replication - both physical and logical - and incredibly well supported across all the major vendors.

My favourite feature of Postgres, however, are [extensions](https://wiki.postgresql.org/wiki/Extensions). This is where I feel Postgres really comes alive in a way that few other databases can. There are extensions for almost everything you could want - [AGE](https://age.apache.org/) enables graph data structures and the user of the Cypher query language, [TimescaleDB](https://docs.timescale.com/self-hosted/latest/) enables time-series workloads, [Hydra Columnar](https://github.com/hydradatabase/hydra/tree/main/columnar) provides an alternate columnar storage engine, and so on. I’ve [written about writing an extension](https://matt.blwt.io/post/building-a-postgresql-extension-line-by-line) relatively recently if you’d like to give it a go yourself.

Postgres shines as a great “default” database for that reason, and we’re seeing even more non-Postgres services rely on the [Postgres wire protocol](https://www.postgresql.org/docs/current/protocol.html) as a general-purpose Layer 7 protocol to provide client compatibility. With a rich ecosystem, sensible default behaviour and that it can even be fit into a [Wasm install](https://pglite.dev/) makes it a database worth understanding.

Spend a week learning about whats possible with Postgres, but also some of its limitations - [MVCC](https://www.geeksforgeeks.org/multiversion-concurrency-control-mvcc-in-postgresql/) can be fickle. Implement a simple CRUD app in your favourite language. Maybe even build a Postgres extension.

2\. SQLite
----------

### The Local-First Database

Moving on from a client-server model, we take a detour into “embedded” databases, starting with [SQLite](https://www.sqlite.org/index.html). I’ve termed this the “[local-first](https://www.inkandswitch.com/local-first/)” database, where the SQLite database is directly co-located with the application. One of the more famous examples of this usage is [WhatsApp](https://www.whatsapp.com/), which stored chats as local SQLite databases on the device being used. [Signal](https://signal.org/) also does the same thing.

Beyond that, we’re starting to see more creative uses of SQLite rather than “just” a local ACID-compliant database. With the advent of tools like [Litestream](https://litestream.io/) enabling streaming backups and [LiteFS](https://fly.io/docs/litefs/) to provide distributed access, we can devise more interesting topologies. Extensions like [CR-SQLite](https://github.com/vlcn-io/cr-sqlite) allow the use of [CRDTs](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) to avoid needing conflict resolution when merging changesets, as used in [Corrosion](https://github.com/superfly/corrosion).

SQLite has also had a small resurgence thanks to [Ruby on Rails 8.0](https://rubyonrails.org/2024/9/27/rails-8-beta1-no-paas-required) - 37signals has gone all in on SQLite, building a bunch of Rails modules like [Solid Queue](https://github.com/rails/solid_queue) and configuring Rails to manipulate multiple SQLite databases via `database.yml` for this purpose. [Bluesky uses SQLite for the Personal Data Servers](https://newsletter.pragmaticengineer.com/p/bluesky?open=false#%C2%A7sqlite) - every user has their own SQLite database.

Spend a week experimenting with local-first architectures using SQLite, or even seeing if you can migrate a client-server model using Postgres to something that “just” needs SQLite instead.

3\. DuckDB
----------

### The Query-Anything Database

Onto the next embedded database, we have [DuckDB](https://duckdb.org/). Much like SQLite, DuckDB is intended to be an in-process database system, but more focused on online analytical processing (OLAP) versus online transaction processing (OLTP).

Where DuckDB shines is its use as a “query-anything” database, using SQL as its dialect of choice. It can natively pull data into its engine from CSVs, TSVs, JSON etc, but also formats like Parquet - just check out the list of [data sources](https://duckdb.org/docs/data/data_sources.html). This gives it extreme flexibility - check out [this example of querying the Bluesky firehose](https://motherduck.com/blog/how-to-extract-analytics-from-bluesky/).

Much like Postgres, DuckDB also [has extensions](https://duckdb.org/docs/extensions/overview), though not quite as rich an ecosystem - DuckDB is much younger, after all. Many contributed by the community can be found on the [list of community extensions](https://duckdb.org/community_extensions/list_of_extensions), though a particular favourite of mine is [`gsheets`](https://duckdb.org/community_extensions/extensions/gsheets.html).

Spend a week doing some data analysis and processing with DuckDB - be it via a Python notebook or something like [Evidence](https://evidence.dev/), maybe even see how it fits in with your “local-first” approach with SQLite by offloading analytics queries of your SQLite database to DuckDB, which [can read it](https://duckdb.org/docs/guides/database_integration/sqlite.html).

4\. ClickHouse
--------------

### The Columnar Database

Leaving the embedded database sphere, but sticking with the analytics theme, we come to [ClickHouse](https://clickhouse.com/). If I had to only pick two databases to deal with, I’d be quite happy with just Postgres and ClickHouse - the former for OLTP, the latter for OLAP.

ClickHouse specialises in analytics workloads, and can support very high ingest rates through [horizontal scaling](https://clickhouse.com/docs/en/architecture/horizontal-scaling) and sharded storage. It also supports [tiered storage](https://clickhouse.com/docs/en/guides/separation-storage-compute), allowing you to split “hot” and “cold” data - [GitLab](https://docs.gitlab.com/ee/development/database/clickhouse/tiered_storage.html) have a pretty thorough doc on this.

Where ClickHouse comes into its own is when you have analytics queries to run on a dataset too big for something like DuckDB, or you need “real-time” analytics. There is a lot of “benchmarketing” around these datasets, so I’m not going to repeat them here.

Another reason I suggest checking out ClickHouse is that it is a _joy_ to operate - deployment, scaling, backups and so on are [well documented](https://clickhouse.com/docs/en/architecture/cluster-deployment) - even down to setting [the right CPU governor](https://clickhouse.com/docs/en/operations/tips) is covered.

Spend a week exploring some larger analytics datasets, or converting some of the DuckDB analytics from above into a ClickHouse deployment. ClickHouse also has an embedded version - [chDB](https://clickhouse.com/docs/en/chdb) - that can offer a more direct comparison.

5\. FoundationDB
----------------

### The Layered Database

We now enter the “mind expanding” section of this list, with [FoundationDB](https://www.foundationdb.org/). Arguably, FoundationDB is not a database, but quite literally the foundation for _a_ database. Used in production by Apple, Snowflake and [Tigris Data](https://www.tigrisdata.com/blog/building-a-database-using-foundationdb/), FoundationDB is worth your time because it is quite unique in the world of key-value storage.

Yes, it’s an ordered key-value store, but that isn’t what is interesting about it. At first glance, it has some curious [limitations](https://apple.github.io/foundationdb/known-limitations.html) - transactions cannot exceed 10MB of affected data and they cannot take longer than five seconds after the first read in a transaction. But, as they say, limits set us free. By having these limits, it can achieve full ACID transactions at very large scale - 100+ TiB clusters are known to be in operation.

FoundationDB is architected for specific workloads and [extensively tested](https://apple.github.io/foundationdb/testing.html) using simulation testing, which has been picked up by other technologies, including another database on this list and [Antithesis](https://www.antithesis.com/), founded by some ex-FoundationDB folks. For more notes on this, check out [Tyler Neely’s](https://sled.rs/simulation.html) and [Phil Eaton’s](https://notes.eatonphil.com/2024-08-20-deterministic-simulation-testing.html) notes on the topic.

As mentioned, FoundationDB has some very specific semantics that take some getting used to - their [Anti-Features](https://apple.github.io/foundationdb/anti-features.html) and [Features](https://apple.github.io/foundationdb/features.html) docs are worth familiarising yourself with to understand the problems they are looking to solve.

But why is it the “layered” database? This is because of the [Layers concept](https://apple.github.io/foundationdb/layer-concept.html). Instead of tying the storage engine to the data model, instead the storage is flexible enough to be remapped across different layers. [Tigris Data](https://www.tigrisdata.com/blog/data-layer-foundationdb/) have a great post about building such a layer, and there are some examples such as a [Record layer](https://github.com/FoundationDB/fdb-record-layer) and a [Document layer](https://github.com/FoundationDB/fdb-document-layer) from the FoundationDB org.

Spend a week going through the [tutorials](https://apple.github.io/foundationdb/tutorials.html) and think about how you could use FoundationDB in place of something like [RocksDB](https://rocksdb.org/). Maybe check out some of the [Design Recipes](https://apple.github.io/foundationdb/design-recipes.html) and go read the [paper](https://www.foundationdb.org/files/fdb-paper.pdf).

6\. TigerBeetle
---------------

### The Obsessively Correct Database

Flowing on from the deterministic simulation testing, [TigerBeetle](https://tigerbeetle.com/) breaks the mold from our previous databases in that it is decidedly _not_ a general purpose database - it is entirely dedicated to financial transactions.

Why is this worth a look? Single-purpose databases are unusual, and one that is as _obsessively correct_ as TigerBeetle are a true rarity, especially considering it is open source. They include everything from [NASA’s Power of Ten Rules](https://en.wikipedia.org/wiki/The_Power_of_10:_Rules_for_Developing_Safety-Critical_Code) and [Protocol-Aware Recovery](https://www.usenix.org/conference/fast18/presentation/alagappan), through to strict serialisability and Direct I/O to avoid issues with the kernel page cache. It is _seriously_ impressive - just go read their [Safety doc](https://github.com/tigerbeetle/tigerbeetle/blob/a43f2205f5335cb8f56d6e8bfcc6b2d99a4fc4a4/docs/about/safety.md) and their [approach to programming they call Tiger Style](https://github.com/tigerbeetle/tigerbeetle/blob/a43f2205f5335cb8f56d6e8bfcc6b2d99a4fc4a4/docs/TIGER_STYLE.md).

Another interesting point about TigerBeetle is that it’s written in [Zig](https://ziglang.org/) - a relative newcomer to the systems programming language school, but clearly has fit well with what the TigerBeetle folks are trying to accomplish.

Spend a week modelling your financial accounts in a local deployment of TigerBeetle - follow the [Quick Start](https://docs.tigerbeetle.com/quick-start) and take a look at the [System Architecture](https://docs.tigerbeetle.com/coding/system-architecture) docs on how you might use it in conjunction with one of the more general-purpose databases above.

7\. CockroachDB
---------------

### The Global Database

Finally, we come full circle. I struggled a little on what to put here in the last slot. Thoughts originally went to [Valkey](https://valkey.io/), but FoundationDB scratched the key-value itch. I thought about graph databases, or something like [ScyllaDB](https://www.scylladb.com/) or [Cassandra](https://cassandra.apache.org/_/index.html). I thought about [DynamoDB](https://aws.amazon.com/dynamodb/), but not being able to run it locally/for free put me off.

In the end, I decided to close on a globally distributed database - [CockroachDB](https://www.cockroachlabs.com/). It’s Postgres wire-protocol compatible, and inherits some of the more interesting features discussed above - large horizontal scaling, strong consistency - and has some interesting features of its own.

CockroachDB enables scaling a database across multiple geographies through being based on Google’s [Spanner](http://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf) system, which relies on atomic and GPS clocks for extremely accurate time synchronisation. Commodity hardware, however, doesn’t have such luxuries, so CockroachDB has some [clever solutions](https://www.cockroachlabs.com/blog/living-without-atomic-clocks/#How-does-CockroachDB-choose-transaction-timestamps?) where reads are retried or delayed to account for clock sync delay with NTP, and nodes also compare clock drift amongst themselves and terminate members if they exceed the maximum offset.

Another interesting feature of CockroachDB is how [multi-region configurations](https://www.cockroachlabs.com/docs/stable/multiregion-overview) are used, including [table localities](https://www.cockroachlabs.com/docs/stable/table-localities), where there are different options depending on the read/write tradeoffs you want to make.

Spend a week re-implementing the the [`movr`](https://www.cockroachlabs.com/docs/v24.3/movr) example in a language and framework of your choice.

Wrap Up
-------

We’ve explored a bunch of different databases, all used in production by some of the largest companies on the planet, and hopefully this will have exposed you to some technologies you weren’t familiar with before. Take this knowledge with you as you look to solve interesting problems.

