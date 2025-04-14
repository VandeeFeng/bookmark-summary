---
title: Stevens- a hackable AI assistant using a single SQLite table and a handful of cron jobs
date: 2025-04-14
extra:
  source: https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs
  original_title: Stevens- a hackable AI assistant using a single SQLite table and a handful of cron jobs
---
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


## Full Content
Title: Stevens: a hackable AI assistant using a single SQLite table and a handful of cron jobs

URL Source: https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs

Markdown Content:
There’s a lot of hype these days around patterns for building with AI. Agents, memory, RAG, assistants—so many buzzwords! But the reality is, **you don’t need fancy techniques or libraries to build useful personal tools with LLMs.**

In this short post, I’ll show you how I built a useful AI assistant for my family using a dead simple architecture: a single SQLite table of memories, and a handful of cron jobs for ingesting memories and sending updates, all hosted on [Val.town](https://www.val.town/). The whole thing is so simple that you can easily copy and extend it yourself.

Meet Stevens[](https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs#meet-stevens)
--------------------------------------------------------------------------------------------------------------------------------

The assistant is called Stevens, named after the butler in the great Ishiguro novel [Remains of the Day](https://en.wikipedia.org/wiki/The_Remains_of_the_Day). Every morning it sends a brief to me and my wife via Telegram, including our calendar schedules for the day, a preview of the weather forecast, any postal mail or packages we’re expected to receive, and any reminders we’ve asked it to keep track of. All written up nice and formally, just like you’d expect from a proper butler.

Here’s an example. (I’ll use fake data throughout this post, beacuse our actual updates contain private information.)

![Image 1](https://www.geoffreylitt.com/images/article_images/stevens/telegram.png?1744560139)

Beyond the daily brief, we can communicate with Stevens on-demand—we can forward an email with some important info, or just leave a reminder or ask a question via Telegram chat.

![Image 2](https://www.geoffreylitt.com/images/article_images/stevens/coffee.png?1744560139)

That’s Stevens. It’s rudimentary, but already more useful to me than Siri!

Behind the scenes[](https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs#behind-the-scenes)
--------------------------------------------------------------------------------------------------------------------------------

Let’s break down the simple architecture behind Stevens. The whole thing is hosted on [Val.town](https://www.val.town/), a lovely platform that offers SQLite storage, HTTP request handling, scheduled cron jobs, and inbound/outbound email: a perfect set of capabilities for this project.

First, how does Stevens know what goes in the morning brief? The key is the butler’s notebook, a log of everything that Stevens knows. There’s an admin view where we can see the notebook contents—let’s peek and see what’s in there:

![Image 3](https://www.geoffreylitt.com/images/article_images/stevens/notebook.png?1744560139)

You can see some of the entries that fed into the morning brief above—for example, the parent-teacher conference has a log entry.

In addition to some text, entries can have a _date_ when they are expected to be relevant. There are also entries with no date that serve as general background info, and are always included. You can see these particular background memories came from a Telegram chat, because Stevens does an intake interview via Telegram when you first get started:

![Image 4](https://www.geoffreylitt.com/images/article_images/stevens/background.png?1744560139)

**With this notebook in hand, sending the morning brief is easy**: just run a cron job which makes a call to the Claude API to write the update, and then sends the text to a Telegram thread. As context for the model, we include any log entries dated for the coming week, as well as the undated background entries.

Under the hood, the “notebook” is just a single SQLite table with a few columns. Here’s a more boring view of things:

![Image 5](https://www.geoffreylitt.com/images/article_images/stevens/db.png?1744560139)

But wait: how did the various log entries get there in the first place? In the admin view, we can watch Stevens buzzing around entering things into the log from various sources:

This is just some data importers populating the table:

*   An hourly data pull from the Google Calendar API
*   An hourly check of the local weather forecast using a weather API
*   I forward [USPS Informed Delivery](https://www.usps.com/manage/informed-delivery.htm) containing scans of our postal mail, and Stevens OCRs them using Claude
*   Inbound Telegram and email messages can also result in log entries
*   Every week, some “fun facts” get added into the log, as a way of adding some color to future daily updates.

**This system is easily extensible with new importers.** An importer is just any process that adds/edits memories in the log. The memory contents can be any arbitrary text, since they’ll just be fed back into an LLM later anyways.

Reflections[](https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs#reflections)
--------------------------------------------------------------------------------------------------------------------------------

A few quick reflections on this project:

**It’s very useful for personal AI tools to have access to broader context from other information sources.** Awareness of things like my calendar and the weather forecast turns a dumb chatbot into a useful assistant. ChatGPT recently added memory of past conversations, but there’s lots of information not stored within that silo. I’ve [written before](https://x.com/geoffreylitt/status/1810442615264796864) about how the endgame for AI-driven personal software isn’t more app silos, it’s small tools operating on a shared pool of context about our lives.

**“Memory” can start simple.** In this case, the use cases of the assistant are limited, and its information is inherently time-bounded, so it’s fairly easy to query for the relevant context to give to the LLM. It also helps that some modern models have long context windows. As the available information grows in size, RAG and [fancier](https://x.com/sjwhitmore/status/1910439061615239520) [approaches](https://arxiv.org/abs/2304.03442) to memory may be needed, but you can start simple.

**Vibe coding enables sillier projects.** Initially, Stevens spoke with a dry tone, like you might expect from a generic Apple or Google product. But it turned out it was just more _fun_ to have the assistant speak like a formal butler. This was trivial to do, just a couple lines in a prompt. Similarly, I decided to make the admin dashboard views feel like a video game, because why not? I generated the image assets in ChatGPT, and vibe coded the whole UI in Cursor + Claude 3.7 Sonnet; it took a tiny bit of extra effort in exchange for a lot more fun.

Try it yourself[](https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs#try-it-yourself)
--------------------------------------------------------------------------------------------------------------------------------

Stevens isn’t a product you can run out of the box, it’s just a personal project I made for myself.

But if you’re curious, you can check out the code and fork the project [here](https://www.val.town/x/geoffreylitt/stevensDemo). You should be able to apply this basic pattern—a single memories table and an extensible constellation of cron jobs—to do lots of other useful things.

I recommend editing the code using your AI editor of choice with the [Valtown CLI](https://github.com/pomdtr/vt) to sync to local filesystem.

