---
title: From where I left - antirez
date: 2024-12-12
extra:
  source: https://antirez.com/news/144
  original_title: From where I left - antirez
---
## Summary
**摘要**：
文章主要讲述了作者Vandee回归Redis项目的经历。Vandee原先因为希望追求写作、与家人共度更多时光和卸下项目管理的重担，选择离开Redis。几年后，Vandee的女儿长大成人后，希望能与Vandee一起去纽约城庆祝她的十二岁生日。Vandee意识到她是时候重新回到科技界，与他人合作为Redis制定新的发展方向。

Vandee最初对开放源代码的严谨看法被揭示为基于信仰的思考，他逐渐意识到开放源代码并不一定是编写软件的唯一途径。HSV开关是为了平衡云供应商的角色问题而做出的决定，旨在突出Redis核心的集中研发，并为新功能设计创造更多空间，同时消除云供应商正版差别而复制Redis来源的问题。

在此次回归中，Vandee表达了他对人工智能领域的兴趣，如何利用AI对工作进行加速和增强，表明了他的期待，即数据类型将提供一种以向量评分作为特征的自适应系统（向量集），以此支持IO密集型的AI处理，为Redis推出新功能，提供了一种Ften相配合的自动生成技术。此外，Vandee也剧本正在设计的新特性，包括向量集的事务操作等。

**要点总结**：
1. 随着女儿的成长和Vandee对写作的追求，其决定离开Redis，寻找新的方向。
2. 几年后，Vandee意识到需要回到科技环境中，与Rowan Trollope合作，讨论Redis的未来。
3. 随着Redis的业务模式改变和保持与社区的联系的需求，决定进行了一次知识产权转换，以平衡云供应商的利益冲突。
4. Vandee对AI领域的投入激增，认为AI正在改变工作环境，为高效工作提供了新的可能性。
5. Vandee正推动Redis开发新的功能，包括向量集 setData type，以支持AI密集型工作负载，提高效率。
## Full Content
Title: From where I left - <antirez>

URL Source: https://antirez.com/news/144

Markdown Content:
[antirez](https://antirez.com/user/antirez) 1 day ago. 205612 views.

I’m not the kind of person that develops a strong attachment to their own work. When I decided to leave Redis, about 1620 days ago (~ 4.44 years), I never looked at the source code, commit messages, or anything related to Redis again. From time to time, when I needed Redis, I just downloaded it and compiled it. I just typed “make” and I was very happy to see that, after many years, building Redis was still so simple.

My detachment was not the result of me hating my past work. While in the long run my creative work was less and less important and the “handling the project” activities became more and more substantial — a shift that many programmers are able to do, but that’s not my bread and butter — well, I still enjoyed doing Redis stuff when I left. However, I don’t share the vision that most people at my age (I’m 47 now) have: that they are still young. I wanted to do new stuff, especially writing. I wanted to stay more with my family and help my relatives. I definitely needed a break.

However, during the “writing years” (I’m still writing, by the way), I often returned to coding, as a way to take breaks from intense writing sessions (writing is the only mental activity I found to be a great deal more taxing than coding): I did a few embedded projects; played more with neural networks; built Telegram bots: a bit of everything. Hacking randomly was cool but, in the long run, my feeling was that I was lacking a real purpose, and every day I started to feel a bigger urgency to be part of the tech world again. At the same time, I saw the Redis community fragmenting, something that was a bit concerning to me, even as an outsider.

So I started to think that maybe, after all, I could have a role back in the Redis ecosystem. Perhaps I could be able to reshape the company's attitude towards the community. Maybe I could even help to take back the role of the Redis core as the primary focus of new developments. Basically I could be some kind of “evangelist” (I don’t love the name of this role, but… well, you get it), that is, on one side, a bridge between the company and the community, but also somebody that could produce programming demos, invent and describe new patterns, write documentation, videos and blog posts about new and old stuff. And, what about the design of new stuff? I could learn from the work of people in the wild, from their difficulties, distill it, and report back design ideas, in order for Redis to evolve.

# Time in NY

At some point my daughter, who is now 12, and is a crucial person in my life, enlightening my days with her intelligence, creativity and love, wanted to visit NYC for her birthday. We decided that yes, this was a good idea after all, we had a couple very difficult years recently, so, why not? My daughter is now more of a girl than a child. So, in NYC, I thought: maybe this is the right time, I can do a part time job. I met the new Redis CEO, Rowan Trollope, very recently, in a video call. I had the feeling that I could work with him to tune the future of the company’s relationships with the community and the codebase direction. So I wrote him an email saying: do you think I could be back in some kind of capacity? Rowan showed interest in my proposal, and quickly we found some agreement.

# About the license switch

People will ask questions about why I \*actually\* did this, whether there is some back story other than what I just wrote above, if there is some agreement involved, or a big amount of money; something odd or unclear. But sometimes things are very boring: 1. I contacted the company, not the reverse. 2. I’m not getting crazy money to re-enter, it’s not about exploiting some situation — normal salary (but, disclaimer: yes, I have Redis stock options like I had before, no less, no more). 3. I don’t have huge issues with Redis changing its license; Specifically I don’t think the fracture with the community is \*really\* about this. But since people will ask me about that very important matter, it is better to tell you all the truth immediately.

# The licensing dilemma

I wrote open source software for almost my whole life. Yet, as I’m an atheist and still I’m happy when I see other people believing in God, if this helps them to survive life’s hardships, I also don’t believe that open source is the only way to write software. When I started to develop Redis in the context of a company where I was one of the two founders and where we kept the software code closed (Redis was opened as it was considered not part of the core product). We didn't want our services to be copied by others, as simple as that. So I’m not an extremist in this regard – I’m an extremist only about software design.

Moreover, I don’t believe that openness and licensing are only what the OSI tells us they are. I see licensing as a spectrum of things you can and can’t do. At the same time, I’m truly concerned that big cloud providers have changed the incentives in the system software arena. Redis was not the only project to change license, it was actually the last one… of a big pile. And I have the feeling that in recent years many projects didn’t even start because of a lack of a clear potential business model. So, the Redis license switch was not my decision and perhaps I would have chosen a different license? I’m not sure, it’s too easy to relitigate right now, far from the scene for many years and without business pressures. But in general, I can understand the choice.

Moreover, if you read the new Redis license, sure, it’s not BSD, but basically as long as you don’t sell Redis as a service, you can use it in very similar ways and with similar freedoms as before (what I mean is that you can still modify Redis, redistribute it, use Redis commercially, in your for-profit company, for free, and so forth). You can \*even\* still sell Redis as a service if you want, as long as you release all the orchestration systems under the same license (something that nobody would likely do, but this shows the copyleft approach of the license). The license language is almost the same as the AGPL, with changes regarding the SAAS stuff. So, not OSI approved? Yes, but I have issues calling the SSPL a closed license.

You will say (I can hear you): the real problem is that there are companies controlling OSS projects’ direction! So eventually the interests get more aligned with companies and less with the user base. I’m grateful there are many projects out there with zero direct companies involvement (if not external sponsorship), but well, you know what? Involvement of companies, in many large projects, actually slows down this process of skewing the right path. This surely happened in the case of Redis.

# The Robin Hood of software

Let's jump back into the past, to the first days of Redis.

When Redis started to become popular, I wanted to find a way to continue working on it. This was before VMware offered me to sponsor my work. I started to play with the idea of a business model, and guess what? It was in the form of closed source products that would kinda help people running Redis, in some way or the other. (Amazingly, one of the repositories associated with this idea is still online, showing commits of \*15\* years ago: [https://github.com/antirez/redis-tools](https://github.com/antirez/redis-tools))

I was about to try some kind of open core approach; I also remember I was thinking about delaying the BSD license for new code for six months, in order to create some kind of advantage for paying users. Now I don’t believe I would be a jerk and do strange games with my users, but I would not be what I was able to be thanks to VMware and, later, more extensively thanks to Redis Labs later: a freaking Robin Hood of open source software, where I was well compensated by a company and no, not to do the interests of the company itself, but only to make the best interests of the Redis community. This is a better setup than having your own company, I’m sure about that.

VMWare, and later Redis Labs, didn’t pay just for me. If you give a quick look at the repository contributions history, you’ll see the second all time contributor to be Oran Agra (Redis) then there is Pieter Noordhuis (VMWare) and so forth.

So basically I think that 12 years of BSD code written just focusing on the user base is a good deal, and it’s something to be happy about. And right now for me the most important part is that the fracture with the community is not about licensing, or at least it’s not mainly about licensing. Actually the new license can solve some part of it: now there is no longer an incentive to just leave the core in maintenance mode and put the new developments into modules. With the new license, cloud providers can’t just cut and paste the Redis code base and sell it without any revenue sharing (was this really asking for too much? This could have prevented all the license switches you saw lately, not just Redis). With the new license, the spotlight can be back on the Redis core, with new, exciting features in the hands of the developers around the world. With tens of people well compensated for their work pushing useful, well documented changes in the GitHub repository. This is also one of the things I would like to help the company with, and I’ll try hard. We need to make the license switch having good effects on the user base and features: that’s my idea.

# About AI, LLMs and vector indexing

But there is more: Redis is getting interested in developing vector capabilities, and in general to support the kind of programming you can do with AI. Now, every day, I read Hacker News, and I see a huge amount of technical people who dislike AI and the new developments. I also see a lot of people who don't even care to really try the latest models available in depth (hint: Claude AI is in its own league) and still dismiss them as kinda useless. For me, it’s different. I always loved neural networks. I wrote my first NN library in 2003 and was totally shocked by how powerful and cool the whole concept was. And now, at the end of 2024, I’m finally seeing incredible results in the field, things that looked like sci-fi a few years ago are now possible: Claude AI is my reasoning / editor / coding partner lately. I’m able to accomplish a lot more than I was able to do in the past. I often do \*more work\* because of AI, but I do better work. Recently I wrote a sci-fi short story for an Italian publisher, and thanks to Claude criticizing parts of it I rewrote the ending and produced a much better work (I didn’t let Claude write a single line of the story or the plot: great use of AI is not making machines do what you can do better).

Yesterday I needed to evaluate how much faster dot product could be computed with 8 bit quantization of my vectors; I told Claude I needed a benchmark designed in a specific way, and two minutes later I could test it, modify it, and understand whether it was worthwhile or not. Basically, AI didn’t replace me, AI accelerated me or improved me with feedback about my work. And I believe that (regardless of the popularity of RAG, which is not necessarily the main application, nor the most future proof or useful, as models contexts are becoming larger and larger, and soon popular models attention may have linear complexity), sorry for the digression, I was saying that I believe that learned embeddings are here to stay, and vector search is something that belongs to Redis for several reasons: first because vector indexes are data structures, particularly slow data structures, and such data structures can work very well in memory. Also, because I think I found the perfect API to expose them.

During my work in designing Redis, I always showed some contradictory tendencies. I was always ready to say “no” to certain things that looked like perfect fits for the project (named Lua scripts, hash fields expires, that are both part of Redis now, btw) but at the same time I added Lua scripting capabilities — when it looked like nuts, an interpreter inside Redis?! —, the Pub/Sub capability, that seemed out of context, then streams, and even synthetic data structures that don’t exist in computer science books, like sorted sets. Because, for me, the fitness of new features into Redis was about two things: use cases and internal design fit. Redis, for me, is lego for programmers, not a “product”.

# Vector sets

So recently I started to think that sorted sets can inspire a new data type, where the score is actually a vector. And while I was in talks with Rowan, I started to write a design document, then I started to implement a proof of concept of the new data structure, reimplementing HNSWs from scratch (instead of using one of the available libraries, since I wanted to tune every little bit), the Redis way, and well, I’m not sure how this will end, I’m still in the early stages of coding, but perhaps I may end up contributing code again, if this proposal gets accepted. The module I implemented (that would be later merged into the core – for now it’s a module just for the sake of simplicity) implements new commands that manipulate embeddings directly. I’ll show you just that as a hint:


VSIM top\_1000\_movies\_imdb ELE "The Matrix"  WITHSCORES
 1) "The Matrix"
 2) "0.9999999403953552"
 3) "Ex Machina"
 4) "0.8680362105369568"
 5) "Akira"
 6) "0.8635441958904266"
 7) "District 9"
 8) "0.8631418347358704"
 9) "The Martian"
10) "0.8608670234680176"
11) "The Bourne Ultimatum"
12) "0.8599717319011688"
13) "The Bourne Supremacy"
14) "0.8591427505016327"
15) "Blade Runner"
16) "0.8585404753684998"
17) "Metropolis"
18) "0.8572960793972015"
19) "Inception"
20) "0.8521313071250916"

So you have VSIM, VADD, VCARD, all the obvious stuff. It’s exactly the idea of sorted sets, but with multi-dimensional scores (embeddings!) and K-NN matches. What do you think? And, of course, on top of that there are many implementation tricks to make stuff more efficient. But for now it’s proof of concept code, let me work a bit more on it. I’m implementing threading, dimensionality reduction, quantization, and many more things. Quite fun, to be honest.

As you can see, there is no mention of hybrid search, the recent buzzword about vector stores. Again, this is the Redis way: to let the developer have a role and decide on their tradeoffs: they know what they are modeling, after all. You have a vector index per key, and like what programmers were able to do with sorted sets, they will invent interesting splitting strategies, new schemas, Lua scripts, patterns and all that is required in order to model their use cases.

Still, while normally the associated item will likely be a small string or a document ID, nothing prevents it from being something more complex, with metadata that can be filtered later (but I’ll resist). I just have the feeling that many use cases don’t really need complex server-side filtering, and can be modeled by pre-partitioning data.

What I see with great interest is the addition of a potential STORE option, to store the result into a sorted set instead of returning it to the user, where the score is the similarity, of course. All this also has complex and interesting effects on efficiency, scalability, ability to use scripting, and so forth: I hope I’ll have the opportunity to talk more about it in the next weeks and months.

Ok, ok: back to the point of this blog post. But perhaps the above is the \*real\* point, having new ideas that can be exciting.

# So, I’m back 🙂

All this to say that, I’m back. I think it’s the right moment for a big thank you to all the Redis community, for what it has done over the years. See you around, I hope there is something more to add to this journey.

P.S. I’m active on BlueSky, if you want to follow the developments of all this. [https://bsky.app/profile/antirez.bsky.social](https://bsky.app/profile/antirez.bsky.social)

