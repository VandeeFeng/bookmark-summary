---
title: Two publishers and three authors fail to understand what “vibe coding” means
date: 2025-05-02
extra:
  source: https://simonwillison.net/2025/May/1/not-vibe-coding/
  original_title: Two publishers and three authors fail to understand what “vibe coding” means
---
## Summary
**摘要**：  
作者Simon Willison批评两位出版商和三位作者错误地将“vibe coding”与使用AI工具辅助编程混为一谈。他明确指出，vibe coding的核心在于“忘记代码存在”，仅用于构建一次性项目（throwaway projects），而非负责任地开发生产级代码。作者引用Andrej Karpathy的定义强调，vibe coding依赖于LLM的强大能力，通过快速生成和复制代码实现“无需深度理解”的编程方式。他批评出版商未正确理解这一概念，导致术语被滥用，并呼吁重新审视该术语的定义。同时，作者提出需要一本面向非开发者的书籍，指导如何安全有效地使用vibe coding技术解决实际问题，而非仅服务于现有软件工程师。

**要点总结**：  
1. **vibe coding的定义**：作者强调vibe coding并非使用AI工具编写代码，而是指在生成代码时完全忽视代码本身的质量与存在，主要用于一次性项目（throwaway projects）。  
2. **术语滥用问题**：两位出版商和三位作者错误地将vibe coding与AI辅助编程等同，导致概念混淆，作者批评其未正确理解原始定义。  
3. **Andrej Karpathy的定义**：引用其推文说明vibe coding依赖LLM的高效生成能力，通过快速复制代码和忽略调试流程实现“无脑编程”，但仅适用于非正式项目。  
4. **对非开发者的需求**：作者提出需一本指导非开发者如何安全使用vibe coding技术的书籍，以帮助普通人通过AI工具自动化生活任务，而非替代专业开发者。  
5. **术语规范的呼吁**：作者担忧术语滥用可能引发混乱，呼吁行业重新审视vibe coding的定义，并指出其潜在价值未被充分挖掘。
## Full Content
Title: Two publishers and three authors fail to understand what “vibe coding” means

URL Source: https://simonwillison.net/2025/May/1/not-vibe-coding/

Markdown Content:
1st May 2025

**Vibe coding** does not mean “using AI tools to help write code”. It means “generating code with AI without caring about the code that is produced”. See **[Not all AI-assisted programming is vibe coding](https://simonwillison.net/2025/Mar/19/vibe-coding/)** for my previous writing on this subject. This is a hill I am willing to die on. I fear it will be the death of me.

I just learned about not one but _two_ forthcoming books that use vibe coding in the title and abuse that very clear definition!

**Vibe Coding** by Gene Kim and Steve Yegge (published by IT Revolution) carries the subtitle “Building Production-Grade Software With GenAI, Chat, Agents, and Beyond”—exactly what vibe coding is not.

**Vibe Coding: The Future of Programming** by Addie Osmani (published by O’Reilly Media) likewise talks about how professional engineers can integrate AI-assisted coding tools into their workflow.

I fear it may be too late for these authors and publishers to fix their embarrassing mistakes: they’ve already designed the cover art!

![Image 1: Side-by-side comparison of two programming books: Left - "VIBE CODING: BUILDING PRODUCTION-GRADE SOFTWARE WITH GENAI, CHAT, AGENTS, AND BEYOND" by GENE KIM & STEVE YEGGE with a rainbow digital background; Right - O'REILLY "Vibe Coding: The Future of Programming - Leverage Your Experience in the Age of AI" by Addy Osmani with "Early Release RAW & UNEDITED" badge and bird illustrations.](https://static.simonwillison.net/static/2025/vibe-coding-books.jpg)

I wonder if this a new record for the time from a term being coined to the first published books that use that term entirely incorrectly.

Vibe coding was only coined by Andrej Karpathy on February 6th, 84 days ago. I will once again quote [Andrej’s tweet](https://twitter.com/karpathy/status/1886192184808149383), with my own highlights for emphasis:

> There’s a new kind of coding I call “vibe coding”, where you fully give in to the vibes, embrace exponentials, and **forget that the code even exists**. It’s possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper so I barely even touch the keyboard.
> 
> I ask for the dumbest things like “decrease the padding on the sidebar by half” because I’m too lazy to find it. I “Accept All” always, I don’t read the diffs anymore. When I get error messages I just copy paste them in with no comment, usually that fixes it. The code grows beyond my usual comprehension, I’d have to really read through it for a while. Sometimes the LLMs can’t fix a bug so I just work around it or ask for random changes until it goes away.
> 
> **It’s not too bad for throwaway weekend projects, but still quite amusing**. I’m building a project or webapp, but it’s not really coding—I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works.

Andrej could not have stated this more clearly: vibe coding is when you **forget that the code even exists**, as a fun way to build **throwaway projects**. It’s not the same thing as using LLM tools as part of your process for responsibly building production code.

I know it’s harder now that tweets are longer than 480 characters, but it’s vitally important you **read to the end of the tweet** before publishing a book about something!

#### Now what do we call books on about real vibe coding? [#](https://simonwillison.net/2025/May/1/not-vibe-coding/#now-what-do-we-call-books-on-about-real-vibe-coding-)

This is the aspect of this whole thing that most disappoints me.

I think there is a real need for a book on _actual_ vibe coding: helping people who are _not_ software developers—and who don’t want to become developers—learn how to use vibe coding techniques [safely, effectively and responsibly](https://simonwillison.net/2025/Mar/19/vibe-coding/#when-is-it-ok-to-vibe-code-) to solve their problems.

This is a rich, deep topic! Most of the population of the world are never going to learn to code, but thanks to vibe coding tools those people now have a path to building custom software.

Everyone deserves the right to automate tedious things in their lives with a computer. They shouldn’t have to learn programming in order to do that. **That** is who vibe coding is for. It’s not for people who are software engineers already!

There are so many questions to be answered here. What kind of projects can be built in this way? How can you avoid the traps around security, privacy, reliability and a [risk of over-spending](https://twitter.com/leojr94_/status/1901560276488511759)? How can you navigate the jagged frontier of things that can be achieved in this way versus things that are completely impossible?

A book for people like that could be a genuine bestseller! But because three authors and the staff of two publishers didn’t read to the end of the tweet we now need to find a new buzzy term for that, despite having the _perfect_ term for it already.

I’m fully aware that I’ve lost at this point—[Semantic Diffusion](https://simonwillison.net/2025/Mar/23/semantic-diffusion/) is an unstoppable force. What next? A book about prompt injection that’s [actually about jailbreaking](https://simonwillison.net/2024/Mar/5/prompt-injection-jailbreaking/)?

I’d like the publishers and authors responsible to at least understand how much potential value—in terms of both helping out more people and making more money—they have left on the table because they didn’t read all the way to the end of the tweet.

