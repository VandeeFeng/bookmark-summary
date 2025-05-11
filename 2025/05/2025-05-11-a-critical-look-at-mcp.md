# A Critical Look at MCP
- URL: https://raz.sh/blog/2025-05-02_a_critical_look_at_mcp
- Added At: 2025-05-11 02:58:20
- [Link To Text](2025-05-11-a-critical-look-at-mcp_raw.md)

## Summary
**摘要**：
本文作者对MCP（Model Context Protocol）提出了批评，MCP旨在标准化LLM与外部世界的交互方式。作者指出，尽管MCP的概念很好，但其工程实践和文档质量令人失望。作者特别关注MCP的HTTP传输方式，包括HTTP+SSE和Streamable HTTP，认为这两种方式都不如直接使用WebSockets。Streamable HTTP试图在SSE基础上实现类似WebSockets的功能，导致设计复杂、容易出错且存在安全隐患。作者认为，应该抛弃现有的HTTP传输方案，转而采用类似于stdio的WebSockets。同时，作者还提到IBM的ACP和Google的A2A等其他相关协议，认为它们的功能可以通过MCP扩展来实现，并建议行业应关注最常见的用例，而不是为了迁就少数特殊情况而牺牲整体效率和安全性。总而言之，作者希望通过这篇文章，能够帮助大家更好的理解MCP协议，避免出现不必要的错误。

**要点总结**：
1.  **MCP协议的设计目标与现实的差距**：MCP旨在为LLM提供统一的接口，使其能够与各种数据源和工具交互，类似于AI应用程序的USB-C接口。然而，实际的工程实践和文档质量却远未达到预期，主要的LLM厂商在投入大量资源训练模型后，在SDK和实施指南方面显得不足。
2.  **HTTP传输方式的问题**：MCP的HTTP传输方式，特别是Streamable HTTP，试图在Server-Sent Events（SSE）之上模拟WebSockets，导致了设计上的复杂性和潜在的安全问题。这种方式增加了开发者的认知负担，可能导致实现不一致，并可能引入会话劫持、重放攻击和拒绝服务（DoS）等漏洞。
3.  **应该使用WebSockets替代Streamable HTTP**：作者认为，WebSockets是比Streamable HTTP更合适的HTTP传输选择。WebSockets能够更好地模拟stdio的socket-like行为，简化跨服务器会话管理，并减少不必要的复杂性和潜在的安全风险。
4.  **替代协议的必要性**：虽然有ACP和A2A等其他协议出现，但作者认为它们的功能可以通过MCP扩展来实现。这些协议试图为Agent（代理）提供接口，但实际上可以将它们视为MCP的工具或资源。
5.  **关注常见用例而非边缘情况**：作者建议，行业应该优先考虑最常见的用例，而不是为了适应少数特殊情况而牺牲整体的效率和安全性。在协议设计和实施中，应该选择最适合大多数情况的方案，而不是追求过于灵活和复杂的解决方案。
