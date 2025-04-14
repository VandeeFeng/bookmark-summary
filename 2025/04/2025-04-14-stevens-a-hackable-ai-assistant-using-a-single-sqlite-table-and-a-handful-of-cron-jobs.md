# Stevens: a hackable AI assistant using a single SQLite table and a handful of cron jobs
- URL: https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs
- Added At: 2025-04-14 00:58:17
- [Link To Text](2025-04-14-stevens-a-hackable-ai-assistant-using-a-single-sqlite-table-and-a-handful-of-cron-jobs_raw.md)

## Summary
**摘要**：
作者分享了如何利用简单的架构，即一个SQLite数据库表和一些定时任务（cron jobs），构建了一个名为Stevens的AI助手。Stevens的功能包括每日发送包含日历、天气、邮件和提醒的简报。用户可以通过Telegram与Stevens交互，转发邮件、设置提醒或提问。Stevens的后台架构依赖于Val.town平台，该平台提供SQLite存储、HTTP请求处理、定时任务以及邮件收发功能。Stevens的核心是“笔记本”，也就是SQLite表，记录了所有已知信息，包括带有日期的相关条目和无日期的一般背景信息。每日简报通过定时任务调用Claude API生成，内容包括未来一周的日志条目和背景条目。信息的录入通过多个数据导入器完成，包括从Google日历、天气API、USPS邮件扫描、Telegram和邮件消息等来源获取数据。作者强调，这种架构易于扩展，只需添加新的数据导入器即可。作者还分享了关于个人AI工具、简单记忆方法和通过调整语气使项目更有趣的思考。虽然Stevens不是一个可以直接使用的产品，但作者提供了代码供读者参考和修改。

**要点总结**：
1.  **个人AI工具无需复杂技术：** 构建有用的个人AI工具不需要复杂的 Agent、Memory 或 RAG 技术。简单的架构，如SQLite数据库和定时任务，足以实现基本功能。
    *   作者通过实际案例展示了如何使用简单的技术栈构建实用的AI助手，强调了在构建个人AI工具时，应注重实用性而非盲目追求复杂技术。

2.  **核心是统一的记忆存储：** Stevens 的核心在于一个 SQLite 表，用于存储所有信息，包括日程安排、天气预报、邮件内容和用户提醒等。这种统一的存储方式使得检索和利用信息变得简单高效。
    *   通过SQLite表集中管理信息，简化了信息的存储和检索过程，为AI助手提供了全面的上下文，使其能够更好地理解用户需求并提供相关服务。

3.  **数据导入器的可扩展性：** Stevens 的数据来源多样，包括 Google 日历、天气 API、USPS Informed Delivery、Telegram 和电子邮件等。每个数据来源都通过一个独立的数据导入器接入，这种模块化的设计使得系统易于扩展和维护。
    *   通过模块化的数据导入器，可以方便地添加新的数据来源，从而不断丰富AI助手的信息储备，提高其智能化水平和服务能力。

4.  **AI应融入更广泛的个人信息：** 个人AI工具应能访问来自不同信息源的上下文信息，例如日历和天气预报，从而将简单的聊天机器人转变为有用的助手。
    *   作者认为，个人AI的未来在于小型工具对共享的个人生活信息池进行操作，打破应用孤岛，实现更智能、更集成化的服务。


