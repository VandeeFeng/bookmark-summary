---
title: Ghostty- Reflecting on Reaching 1.0
date: 2024-12-27
extra:
  source: https://mitchellh.com/writing/ghostty-1-0-reflection
  original_title: Ghostty- Reflecting on Reaching 1.0
---
## Summary
**摘要**：
Ghostty版本1.0已经发布，它不仅仅是一个终端仿真器的发布，而是作者个人对终端及其未来的构建愿景的深刻反思。项目最初仅作为一个实验，观察Zig语言和图形编程的特性，以及进一步深入了解终端。但随着项目进展，作者开始注意到现有终端存在的问题，如特定的功能缺失、性能低下、以及缺乏重大创新，进而认识到不同用户可能对终端有独特的期望和需求。于是，Ghostty诞生了，它并非完美也非最终答案，但在作者的价值观中有着特殊的地位。该终端旨在体现作者对理想终端的独特设想。

**要点总结**：
1. **Ghostty背景及意义**：项目由想探索Zig的语言特性和了解终端的作者发起，后变为致力于提供一种创新的终端特性的项目。它代表了用户可能期望的不同之处，并不仅仅是简单的功能堆砌或性能改进。
2. **私有测试版**：尽管私有测试版主要意图是帮助作者管理个人时间，同时确保用户反馈有助于成熟发布，但它意外引起了广泛的关注和期待，同时也带来了公关和参与度上的挑战。
3. **技术栈与架构**：项目采用Zig作为核心语言和平台特定的GUI架构，这一选择为Hello World和平台整合奠定了基础。通过私人测试版，新用户提供持续的反馈和贡献机会，展现Zig作为友好的，可以促进贡献的语言的一面。
4. **社区的形成**：尽管社区最初私密，但其对于项目热情和专注的特性表明社区成员出于共同的终端追求，专注于性能、设计、高质量软件和所做的正确事情。这个社区为项目带来了价值，并影响了作者的个人成长和社区交往。
5. **发布后的展望**：版本1.0发布并不意味着项目的终结，未来包括但不限于改善现有功能、质量控制以及向其他项目提供稳定的libghostty实现，促进更广泛的终端开发者社区的发展。作者强调将继续追求个人兴趣，确保项目和社区保持其原始属性。
## Full Content
Title: Ghostty: Reflecting on Reaching 1.0

URL Source: https://mitchellh.com/writing/ghostty-1-0-reflection

Published Time: 2024-12-26T00:00:00.000Z

Markdown Content:
This isn't a release announcement. Ghostty 1.0 is out. You can download it and read about it [on the Ghostty website](https://ghostty.org/). This is a personal reflection on the project.

Ghostty 1.0 is out.

If you told me two years ago that I would be releasing a terminal emulator, I wouldn't have believed you. I've always been a fan of the terminal, my entire career was built around shipping terminal-first software. But they're a solved problem, right? That's what I thought.

I started the project in 2022 merely as a way to play with Zig, do some graphics programming, and deepen my understanding of terminals. I never intended to release it. I didn't think there was innovation to be had. I thought I would learn a lot over a few months and move on.

But as I worked on it, I looked at other terminals differently. I saw tradeoffs that I didn't like. I saw features that I wanted. I saw performance that I could improve. I saw stagnation. There are many _fantastic_ terminals out there and you should use them if they work for you. But I wanted something different and thought maybe others did too.

And so Ghostty was born. It's not perfect, it's not done, it's not for everyone. But it's mine. It's a reflection of my values and my vision for what a terminal could be.

To learn more about how Ghostty differentiates itself from other terminals and my vision for the project, read the [Ghostty 1.0 is coming](https://mitchellh.com/writing/ghostty-is-coming) post.

The Private Beta
----------------

The most controversial part of Ghostty was the private beta. Oh boy, the private beta. I vastly underestimated the effect this would have on the project. Good and bad.

### The Private Beta: The Good

First, why a private beta? The primary reason was to manage my own personal bandwidth. I began publicly sharing the project shortly before my first child was born. I have experience launching software and I knew the stress that comes with it. I wanted to avoid that stress and be able to focus on my family. I felt I could curate a small group of interested users to throttle issues, only increasing the user base as I felt comfortable.

A secondary, but much less important reason was that I felt a terminal emulator more than most software either works or it doesn't. You can't ship a terminal emulator that emulates only half the features Vim needs. You can't incrementally improve a terminal emulator below a certain threshold of functionality. I wanted to ensure that the first public release met that threshold. I wanted people to be able to use it productively and professionally right away.

On these two fronts, the private beta was a _massive success_ (far beyond my expectations). I was able to manage my bandwidth and focus on my family. For the first year of my daughter's life, I woke her up every morning, I played with her every wake window, I went to every doctor's appointment, I was there for every milestone[1](https://mitchellh.com/writing/ghostty-1-0-reflection#user-content-fn-2).

And the beta community was _amazing_. They were patient, they were understanding, they were helpful. They found bugs, they provided feedback, and **they made Ghostty so much better** than it would have been without them. I can't thank them enough.

### The Private Beta: The Bad

Everything else was an unintended consequence of the private beta. The hype, the frustration from those who couldn't get in, the elitisim perceived by some, etc.

I didn't anticipate the hype. Some people think I am lying when I say this. I'm not. I'm not so naive to think that private betas and exclusive access don't generate hype _in principle_. But I didn't think many people at all would be interested in a terminal emulator. I thought I was building boring software for a niche audience. No hype!

But I was wrong, and the consequences were real. People were frustrated that they couldn't get in. People felt left out. People felt like I was being fake to generate hype. The waitlist grew larger than I was comfortable allowing in (given my prior stated priorities).

I'm sorry about that. All I can say is that I didn't intend for this to happen. I ramped up beta invites to try to get as many people in as I felt comfortable with (well, a bit beyond that). We ended the beta at around 5,000 users in a Discord of 28,000 at the time. Not quite the percentage of access I wanted for people but more than I could handle.

The good news is Ghostty is now public and everyone can use it! I hope we can put the negative aspects of the private beta behind us and focus on the future.

**One more negative aspect of the hype is the expectation of Ghostty being revolutionary.** It is and it isn't. Ghostty has different goals and tradeoffs than other terminals. For those looking for those properties, Ghostty is a breath of fresh air and does things that no other terminal does. But for others, it's just a terminal. And that's okay. I hope you find a terminal that works for you and I don't claim that Ghostty is the end all be all of terminals.

The Tech Stack
--------------

Ghostty has an unconventional tech stack and architecture: [Zig](https://ziglang.org/) for the core and platform-specific code for the GUIs. More details on the tech stack can be found in the [original talk I gave on Ghostty](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns).

Two years later, I'm extremely happy with the tech stack and architecture. I think it was the right choice for the project but more than that, I think this architecture could be the right choice for many projects[2](https://mitchellh.com/writing/ghostty-1-0-reflection#user-content-fn-1).

Zig has been an absolute joy to work with. I have _fun_ writing Zig every single day and that fun hasn't diminished a bit over two years. The build system is fantastic, the community is amazing, and the core maintainers are brilliant. My excitement is well known and I've also put my money where my mouth is by [sponsoring the Zig Software Foundation](https://mitchellh.com/writing/zig-donation).

The split between shared core written in Zig and platform-specific GUIs has also been a success. I've been able to effortless integrate [platform-native experiences](https://gpanders.com/blog/ghostty-is-native-so-what/) into Ghostty while keeping over 90% of the code shared.

The beta community has also had no problem contributing to the project. I think this shows that despite being a new, niche language, Zig is easily approachable and productive for new contributors. This is great news for the future of the project.

The community that formed around Ghostty was unexpected and amazing.

To be specific, I'm talking about the private beta community. The public community is a bit of a wild west due to the unstructured nature of not having access to the software. But the private community has focus and purpose and it has been a joy to be a part of.

The Ghostty community is a group of people who are passionate about terminals (of course!) but also about performance, design, software quality, _doing things right_ and for the right reasons. It's a group of people that are pleasant to be around and collaborate with. It's a group of people that I've really enjoyed getting to know and I'm excited to continue to work with.

For me personally, it's also unlikely because most people in the Ghostty community are also _new to my work_. Most don't have a background in infrastructure and therefore aren't familiar with my previous work. It has been fun to build a new community and it reminds me a lot of the early days of my career when I was building a community around my first open source project.

A Post-1.0 Future
-----------------

Ghostty 1.0 is out but the project is far from done for me. Even the 1.0 is less complete than I would have liked! But I had to draw a line in the sand somewhere and I think the 1.0 turned out great.

For the short term, I want to continue focusing on the ["best existing terminal"](https://mitchellh.com/writing/ghostty-is-coming) goal. I want to shore up the features that didn't make it into 1.0 and fix the bugs that are still present. I want to make sure that the foundation that Ghostty is built on is solid for future innovation.

In the medium but not too long term (within 2025), I want to shift focus to release a stable and standalone [`libghostty`](https://ghostty.org/docs/about#libghostty) that can be used by other projects to build their own terminal emulator frontends. I think `libghostty` is the most promising part of the project for the long term impact Ghostty can have within the tech community.

But, regardless of goals, Ghostty will always first and foremost be a passion project for me. I work on this project because it's fun and I want to make sure the community and I don't lose sight of that.

Thanks
------

I believe nothing in this world is accomplished alone. I may have started Ghostty alone but I didn't finish it alone and I have so many people to show appreciation for along the way.

The impact of the Ghostty beta community cannot be overstated. I said this already in this post but Ghostty is only as feature rich and polished as it is thanks to the attention to detail and feedback of the beta community. I'm extremely grateful to everyone who participated in the beta and helped make Ghostty what it is today.

The Discord mods deserve a special shoutout. They worked _hard_ to keep the peace and keep the community focused on the right things. I could see their effort daily in trying to create an environment that allowed me to focus and the beta community to thrive. We have less than 10 mods for 30,000 people and they did an amazing job given the circumstances[3](https://mitchellh.com/writing/ghostty-1-0-reflection#user-content-fn-3).

And finally, and most importantly, I want to thank my wife. We're first time parents and juggling a new baby with a side project I wanted to find time to work on was no small feat (even with the private beta aspect). She helped me find the time to work on Ghostty and she patiently listened (fell asleep) to my ramblings about font rendering.

I hope you enjoy Ghostty 1.0 and feel the love and care that went into it. I'm excited to see where we go from here!

1.  I had to leave for a couple weeks over the first year so I did miss some days, but I was as present as I could be. [↩](https://mitchellh.com/writing/ghostty-1-0-reflection#user-content-fnref-2)
    
2.  I'm not saying I invented it! But it isn't something I see often. [↩](https://mitchellh.com/writing/ghostty-1-0-reflection#user-content-fnref-1)
    
3.  I will acknowledge that the mods and I wielded the ban hammer liberally. I'm sure we kicked out some good people. But given the size of the Discord we had very little patience for people who acted out. [↩](https://mitchellh.com/writing/ghostty-1-0-reflection#user-content-fnref-3)

