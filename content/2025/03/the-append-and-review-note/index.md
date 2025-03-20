---
title: The append-and-review note
date: 2025-03-20
extra:
  source: https://karpathy.bearblog.dev/the-append-and-review-note/
  original_title: The append-and-review note
---
## Summary
**摘要**：
作者介绍了一种名为“附加和回顾笔记”的笔记方法，这种方法简单易用，能有效捕捉日常笔记需求。该方法的核心是维护一个单一的文本笔记，作者使用Apple Notes应用，这样做的好处是避免了管理多个笔记和复杂文件夹结构带来的认知负担，同时利用CTRL+F功能可以轻松搜索。使用时，随时将想法、待办事项等以文本形式添加到笔记顶部，不添加额外的结构化元数据，只使用"watch:"、"listen:"或"read:"等标签方便查找。定期回顾笔记，将值得关注的内容复制粘贴到顶部，合并、处理或修改相关笔记，不重要的内容自然沉淀到底部。作者分享了多种使用场景，包括记录突发的想法、电影推荐、书评、每日待办事项、写作灵感、推文草稿、有趣引言、备忘事项、论文笔记、临时剪贴板、常用命令、实验记录以及缓解焦虑等。这种方法让人可以立即清空工作记忆，专注于手头任务，并确信之后可以回顾和处理这些想法。长期下来，笔记会变得非常庞大，回顾旧内容能带来新的视角和感悟。

**要点总结**：
1.  **单一文本笔记**：作者强调使用单一的文本笔记，避免多重笔记和复杂文件夹结构带来的认知负担，利用应用自带的搜索功能快速查找信息。这种做法简化了信息管理，降低了维护成本。
2.  **附加记录**：随时随地将想法、待办事项等以文本形式添加到笔记顶部，无需过多关注格式和元数据，方便快速记录。这种即时记录的方式有助于捕捉灵感，防止遗忘。
3.  **标签分类**：虽然作者通常不使用结构化元数据，但会使用"watch:"、"listen:"或"read:"等标签对内容进行简单分类，方便在特定场景下快速查找相关信息。这种轻量级的分类方式提高了信息检索的效率。
4.  **定期回顾与整理**：定期回顾笔记内容，将重要的信息复制粘贴到顶部，合并、处理或修改相关笔记，不重要的内容自然沉淀到底部。这种回顾和整理的过程有助于知识的沉淀和新想法的产生。
5.  **多种使用场景**：作者分享了多种使用场景，展示了这种笔记方法在生活和工作中的灵活性和实用性，包括记录想法、备忘、写作、学习和实验等。这些例子说明了该方法适用于各种不同的信息记录和管理需求。

## Full Content
Title: The append-and-review note

URL Source: https://karpathy.bearblog.dev/the-append-and-review-note/

Markdown Content:
_19 Mar, 2025_

A few words on an approach to note taking that I stumbled on and has worked for me quite well for many years. I call it the _"append-and-review note"_. I find that this approach strikes a good balance of being super simple and easy to use but it also captures the majority of day-to-day note taking use cases.

![Image 1: Screenshot 2025-03-19 at 10](https://bear-images.sfo2.cdn.digitaloceanspaces.com/karpathy/26am.webp)

**Data structure.** I maintain one single text note in the Apple Notes app just called "notes". Maintaining more than one note and managing and sorting them into folders and recursive substructures costs way too much cognitive bloat. A single note means CTRL+F is simple and trivial. Apple does a good job of optional offline editing, syncing between devices, and backup.

**Append.** Any time any idea or any todo or anything else comes to mind, I append it to the note on top, simply as text. Either when I'm on my computer when working, or my iPhone when on the go. I don't find that tagging these notes with any other structured metadata (dates, links, concepts, tags) is that useful and I don't do it by default. The only exception is that I use tags like "watch:", "listen:", or "read:", so they are easy to CTRL+F for when I'm looking for something to watch late at night, listen to during a run/walk, or read during a flight, etc.

**Review.** As things get added to the top, everything else starts to sink towards the bottom, almost as if under gravity. Every now and then, I fish through the notes by scrolling downwards and skimming. If I find anything that deserves to not leave my attention, I rescue it towards the top by simply copy pasting. Sometimes I merge, process, group or modify notes when they seem related. I delete a note only rarely. Notes that repeatedly don't deserve attention will naturally continue to sink. They are never lost, they just don't deserve the top of mind.

Example usage:

*   Totally random idea springs to mind but I'm on the go and can't think about it, so I add it to the note, to get back around to later.
*   Someone at a party mentions a movie I should watch.
*   I see a glowing review of a book while doom scrolling through X.
*   I sit down in the morning and write a small TODO list for what I'd like to achieve that day.
*   I just need some writing surface for something I'm thinking about.
*   I was going to post a tweet but I think it needs a bit more thought. Copy paste into notes to think through a bit more later.
*   I find an interesting quote and I want to be reminded of it now and then.
*   My future self should really think about this thing more.
*   I'm reading a paper and I want to note some interesting numbers down.
*   I'm working on something random and I just need a temporary surface to CTRL+C and CTRL+V a few things around.
*   I keep forgetting that shell command that lists all Python files recursively so now I keep it in the note.
*   I'm running a hyperparameter sweep of my neural network and I record the commands I ran and the eventual outcome of the experiment.
*   I feel stressed that there are too many things on my mind and I worry that I'll lose them, so I just sit down and quickly dump them into a bullet point list.
*   I realize while I'm re-ordering some of my notes that I've actually thought about the same thing a lot but from different perspectives. I process it a bit more, merge some of the notes into one. I feel additional insight.

When I note something down, I feel that I can immediately move on, wipe my working memory, and focus fully on something else at that time. I have confidence that I'll be able to revisit that idea later during review and process it when I have more time.

My note has grown quite giant over the last few years. It feels nice to scroll through some of the old things/thoughts that occupied me a long time ago. Sometimes ideas don't stand the repeated scrutiny of a review and they just sink deeper down. Sometimes I'm surprised that I've thought about something for so long. And sometimes an idea from a while ago is suddenly relevant in a new light.

One text note ftw.

