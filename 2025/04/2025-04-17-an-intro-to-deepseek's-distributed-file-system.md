# An Intro to DeepSeek's Distributed File System
- URL: https://maknee.github.io/blog/2025/3FS-Performance-Journal-1/
- Added At: 2025-04-17 16:29:42
- [Link To Text](2025-04-17-an-intro-to-deepseek's-distributed-file-system_raw.md)

## Summary
**摘要**：
本文介绍了DeepSeek发布的一款名为3FS（Fire-Flyer File System）的分布式文件系统。分布式文件系统通过抽象化，让应用程序感觉像是在与本地文件系统交互，隐藏了文件在多个机器上分散存储的复杂性。与本地存储相比，分布式文件系统具有存储容量大、吞吐量高、容错性和数据冗余等优点，广泛应用于并行处理、机器学习、大规模数据存储等领域。3FS的核心组件包括Meta（管理元数据）、Mgmtd（管理集群配置）、Storage（存储实际文件数据）和Client（客户端，与所有节点通信）。Mgmtd跟踪集群中的节点，维护节点配置和CRAQ链信息。Meta节点处理客户端的RPC调用，管理文件元数据，Storage节点管理物理存储，将数据分成多个chunk。CRAQ是一种保证强一致性的协议，用于保持数据chunk的容错性。文章还探讨了CRAQ的读写性能特点及其在3FS中的应用，最后作者提出了后续博客文章要探讨的问题，包括3FS的性能瓶颈、适用场景以及与其他分布式文件系统的比较等，旨在深入分析3FS的性能表现。

**要点总结**：
1.  **3FS的构成和作用**：3FS是一个由DeepSeek开源的分布式文件系统，旨在提供大规模、高吞吐量和高可靠性的数据存储解决方案。它由Meta节点（管理元数据）、Mgmtd节点（管理集群配置）、Storage节点（存储实际文件数据）和Client节点（客户端）组成，共同协作实现文件的存储和访问。
2.  **Mgmtd节点的核心功能**：Mgmtd节点负责跟踪集群中所有活动节点的状态，并通过心跳机制监控它们的健康状况。此外，它还维护集群的配置信息，包括CRAQ链的配置，使得其他节点能够发现彼此，从而降低了节点发现的复杂性。Mgmtd节点类似于一个中心服务器，负责维护整个系统的拓扑结构和配置信息。
3.  **Meta节点与元数据管理**：Meta节点通过RPC调用与客户端进行通信，执行文件系统的基本操作，例如打开、创建、查看状态和删除文件。它利用inodes存储文件的元数据，包括大小、权限、所有者和时间戳等属性。DirEntry对象则负责将路径映射到inodes，类似于符号链接。这些元数据存储在FoundationDB中，并通过会话管理器跟踪打开的文件，确保数据的一致性。
4.  **Storage节点和ChunkEngine**：Storage节点负责管理物理存储上的数据，将数据分割成多个chunk。ChunkEngine是Storage节点的核心组件，用于跟踪磁盘存储块，并维护其元数据，例如ID、大小、磁盘偏移量、物理磁盘、校验和以及版本信息。存储节点通过AllocateWorker分配新的数据块，通过PunchHoleWorker回收不再使用的数据块，并通过AioReadWorker处理读取请求。
5.  **CRAQ协议及其在3FS中的应用**：CRAQ（Chain Replication with Apportioned Queries）是一种用于实现强一致性的协议，被3FS用于保证数据chunk的容错性。在CRAQ中，写操作从头部节点开始，依次传递到尾部节点，并在每个节点上标记为“dirty”。一旦写操作到达尾部节点，数据被标记为“clean”并提交。读操作通常从头部节点读取，如果数据是“dirty”，则从尾部节点读取以确保强一致性。3FS通过CRAQ协议在多个存储节点上复制数据，从而提高系统的可用性和可靠性。

