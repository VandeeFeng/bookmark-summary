---
title: Software is eating the world
date: 2025-01-10
extra:
  source: https://medium.com/@metapgmr/software-is-eating-the-world-all-right-faedbab6d623
  original_title: Software is eating the world
---
## Summary
**摘要**：
本文是作者法兰斯瓦-吉尔伯特林对马克-安德莱斯在2011年提出的“软件正在吞噬世界”这一论点的深刻反思，结合他作为小企业主的亲自体验。作者关注软件行业的若干问题，从企业管理、产品设计、人机交互以及服务的数字化过程等方面，批判性地探讨了软件和数字化技术对传统商业模式和人际关系的影响，认为软件行业过度追求利润最大化，导致了许多适得其反的情况，损害了消费者和员工的利益，甚至助长了负面行为和歧视现象。作者强调了数字化革命在社会层面带来的系统性挑战，并提出了对软件行业的反思和未来的期许。

**要点总结**：
- **软件公司的利润提升成本**：软件公司通过提高订阅服务价格来增加利润，导致消费者不满，例如Clover提高在线订单服务费引起了顾客愤怒并最终被撤消。
- **产品设计的不顾客观反馈**：Doordash自动关闭繁忙餐馆以减少取消订单，影响了客户体验，但即时发现窗口后恶意关闭机制已被取消。
- **数字化拼接人际关系**：通过数据驱动的自动化算法（如Doordash的送餐算法）来处理人员关系，忽视了人工互动的价值，导致员工与客户关系的紧张。
- **审查系统引起暴戾**：数字化的审查系统允许虚假信息、含攻击性和歧视性的评论肆意流传，削弱年轻员工的自尊心，破坏了企业的正面形象和文化。
- **身份验证过程的低效率**：Facebook的身份验证系统故障，导致账户在未经客户同意的情况下被关闭，影响了企业的正常运营和客户体验。
- **医疗保健难题**：小企业的医疗保健计划面临复杂和低效的数字化流程，导致运营成本增加，且积极改善这一体验的可能性被忽视。
- **期望与现实的差距**：数字化时代的企业中，期望完美以至于对服务和产品过于苛责，反映了工作场所内部挑剔文化蔓延的问题。
- **警惕潜在的社会问题**：倡导构建一个有防护的“负面言论防火墙”，保护传统人际交往文化，支持女性和少数族裔的安全工作环境。
## Full Content
Title: Software is eating the world, … all right - Jean-Jacques Dubray - Medium

URL Source: https://medium.com/@metapgmr/software-is-eating-the-world-all-right-faedbab6d623

Published Time: 2024-05-18T20:41:38.994Z

Markdown Content:
[![Image 9: Jean-Jacques Dubray](https://miro.medium.com/v2/resize:fill:88:88/0*-NYON7PGPHdUtcUc.jpg)](https://medium.com/@metapgmr?source=post_page---byline--faedbab6d623--------------------------------)

![Image 10](https://miro.medium.com/v2/resize:fit:700/1*VWzBXJ8Rq4p6BtsS7iqo3Q.jpeg)

I retired from my IT career a couple of months ago after 43 years of commercial software product development and transitioned to the real world where I run two “brick-and-mortar” small businesses.

I was fortunate enough to live it all, from the rise of Personal Computing starting with my TRS-80 (and its 4kB RAM), the Laser printer, the Mac and NeXT computers, the emergence of the Internet and Web-Based Applications, the Open Source Movement, Software as a Service (SaaS), Service Oriented Architectures, the Mobile Revolution (yes I was a huge Apple fanboy), Cloud Computing, Big Data, and Generative AI, not to forget the upcoming Quantum computing revolution.

I enjoy [writing code](https://github.com/jdubray/sam-lib) and have been drinking the cool aid of our industry for a very long time.

As my last professional post, I’d like to reflect on Marc Andressen’s 2011 seminal article on [Why software is eating the world](https://a16z.com/why-software-is-eating-the-world/). I believed every word and even wrote [a book](https://books.apple.com/us/book/b-mc2/id584185735): B = mc2 to explore my views on digital transformations. When I transitioned to my first business three years ago, in preparation for my retirement I dreamed about exploring further the digital revolution. Little did I know…

I am not sure Marc if you will ever read this post, but it is written to you:

Marc,

I would like to share some perspectives on “Why software is eating the world”, from the point of view of a small business owner. No big deal.

Let’s start with the management of “digital companies”: senior managers are eating the cake and having it too. Subscriptions have become a license to kill businesses. Sales are going down? Need to improve your margins? How about a cool 25% increase in the subscription’s price? Customers see the value, they’ll pay, right? Clover decided one day in 2023 that I was getting so much value from their online ordering features that they added a cool $1.50 per order over $30. That was roughly $500/month, just for the privilege of using a terrible online ordering system that didn’t do half of what we needed. I switched immediately and informed our customers, some even cheered encouraging me to fight back. Clover has since reverted their decision, but I will never use their online ordering system, even if they pay me. Clover also offers a “free” timesheet app on their platform, but you have to pay $30/month to extract the results. Fortunately, Clover also offers a free (as in free-for-how-long?) API, so I asked chatGPT to write the code to add up the hours, damn.., it failed miserably, it couldn’t deal with the edge cases of pay periods, and I had to debug its code, but I got it to work, imagine that I got a basic feature that now runs free of charge.

The reality, Marc, is that 20 cents of every dollar that flows through my two businesses fall into the pockets of software companies. Software is eating the world, all right.

Let’s move on to products. By now, you may have guessed that I operate a couple of small restaurants. Let’s start by talking about the digital geniuses at Doordash. Last year a big data team came up with a brilliant idea: let’s close restaurants automatically to minimize cancelled orders when they are too busy. We never had an order canceled in three years of operation because we were too busy, yet they would close our restaurants without notifying us, just in case, so when the orders stopped coming for 20+ minutes, we had to check on the Doordash app, and sure enough, they had closed us, over and over, and over. Amazingly, customers figured out that our UberEats store was open and ordered there. How much did Doordash lose in business with that digital maneuver? This brilliant “algorithm” is no longer deployed, thank god! They even bragged about it on infoQ.

But that’s nothing, let’s talk about the effect of digitization on human interactions. From day one I decided that the delivery drivers were part of our team and they could use our facilities, we gave them drinks, some have become friends, a couple even brought us some presents from their home countries. What’s great about small businesses is that you can “connect” without a protocol. No amount of data and so-called data science will let you build that kind of connection. So what did the geniuses at Doordash do to improve the way we connect? You guessed it, they devised an algorithm that will make the dashers angry at the business owners, as a feature. How? …very easy: the restaurant says the order will be ready in 15 min, just tell the driver it will be ready in 10. The dasher comes and becomes agitated because the food is not ready and we are just a bunch of losers wasting his or her time. I get it, a driver can’t just wait all day for the food to get ready, but come on, the product manager responsible for that feature ought to be fired immediately. And it doesn’t stop there, since dashers are rated on how fast they pick up the food when they get a double delivery, they don’t want to pick the first order because it’s not leaving the restaurant fast enough and they get penalized, they demand to have the two orders handed out at the same time creating some workflow issues. I had to send a dasher home last month because I couldn’t deal with that “feature” any longer. As you can imagine, we can’t easily reorder the order queue to match the desires of any given dasher. Who is the genius who came up with the idea that a double order could magically exit the restaurant one at a time?

Now let’s talk about the geniuses as Google and Yelp. The review system is designed to encourage any sociopath to smash businesses at will. Good luck trying to overturn a review, that process has been removed and replaced by algorithms. Is it normal when customers use words like “clueless and absent” when talking about a twenty-year-old African-American women or “the servers \[in this restaurant\] are sweet”. Don’t you think these kinds of words could be easily filtered by algorithms and no personal references should be allowed in reviews? These young hard-working individuals are proud of their new roles and eager to share their excitement with friends and family, only to then read the kind of words we see in reviews. Imagine living the idea that I am just a piece of candy? Can you Marc? What do these words do to these young women’s self-esteem? How does it build their character? How does it help them progress in life? Is Google in the business of encouraging people to go to some restaurants because of the look of the servers? The review system is abhorrent it encourages abuse and hate when in this industry there is only one type of feedback that works, positive feedback: you know that dish? The customer liked it, can you prepare it again that way?

The geniuses at Yelp have designed a mind reader algorithm, no less. I was the server that day, and even though from the height of my Ph.D. and a half, I like to be the best server I can be, I was in shock when I got a five-star review for my service, and you guessed it, Yelp filtered it explaining to me that it was not ok to (sic) “solicit reviews” as if their algorithm knows for sure that I asked this customer for a review, actually my standard response to customers who want to give a review is don’t waste your time, that system is broken, do not encourage these suckers, break that system, kill that golden goose, let just the sociopaths unleash their Venum, then it will collapse. I suspect that Yelp and Google rank bad reviews higher to encourage good decent human beings to say, that’s not fair, let me write some nice words otherwise nobody in their right mind would spend time writing a review. Heck, you even have professional reviewers now who wine and dine every day and describe every step of their “adventure” with dozens of insipid pictures. How did our parents survive without reviews? Can I give a review to Google’s CEO? Yelp CEO? That’d be fun.

Software is eating the world, all right, pushing hate and friction when it should connect and reward. These digital heroes have chosen their camp: hate, punishment, attracting perverts, and shackling hard-working people in servant roles: you better serve me perfectly, or else…

Now Facebook, IMHO, has won the gold when it comes to digital processes, they hired the cream de la crème of the planet’s innovators who came up with the smartest identity validation process ever.

So, I opened my second business, and decided, unlike the first one to use Facebook. To create a business page, you need a personal account, so far, so good, I use my real name, create the page of my business, post some pictures, and start an ad campaign. Facebook shows me how great they are, I got 3 customer engagements, woohoo!! (asking on messenger for the restaurant’s address) for no less than the bargain price of $9.83 each. Software is eating the world, all right. Then out of the blue this week, while the campaign was running with my credit card, in my name, my real name, my real business. They tell me they need to verify my identity. How? They demand a selfie (sic) and lock my entire account while an ad campaign is running at $10 a pop for someone to review the selfie. Twenty-four hours later their decision came, my account was obviously fake, just like my name, the money I spent with them or the location of my business and the food we serve and they closed my account without any possibility of appeal. Genius, pure genius! I have all the screenshots, I can detail how their “digital process” works, step by step, that ought to go into the computer museum.

Let’s talk for a minute about healthcare. I care about my employees and I offer 100% paid healthcare. Yep, even Microsoft, Facebook, or Amazon can’t do that. It took me three months and threats to cancel my group policy, just to be able to receive plastic healthcare coverage cards. Many small business employees never had healthcare coverage in their lives having a card with a number where to call is a minimum that the digital gurus can’t even imagine. The carrier instead demanded that everything be done online. Did I use a 3rd level carrier? No, Kaiser Permanente! We even got robocalls in English demanding to talk to my employees to onboard them. Software is eating the world, all right.

Last but not least I would like to say a word about my fellow digitizers, the haz-everything generation (including healthcare) that expects perfection each time they spend a fraction of their fat salaries. Have you ever noticed how sophisticated the palate of tech people is? All dishes must match their precise expectations or bam… it’s a guaranteed one-star. The 3 bad reviews we got when we opened our new location was from haz-everything from Zillow, Apple and Amazon, including one PhD, Fulbright recipient complaining how much food she got. Heck, I even had to school a Facebook manager who had invited his team to my restaurant as to what the best process to mail 50 letters would be (hint: batching operations was actually a desirable optimization, and I had news for him, apparently, it worked in restaurants too!). Shall I say a word about tipping? These people are the wealthiest and most successful group of people in the country and some of them have no problem leaving insulting tips in the range of 1 or 2% for a full dine-in service, with no apparent problem in the service, even some extreme cases, past the closing time of the restaurant.

My best advice to a hiring manager is to check the reviews written by your future hires, you will have direct visibility into how they will perform in your organization and how toxic or emphatic they will be.

So that’s enough, I had enough of what I once thought would be a major step forward for humanity. The “digital revolution” is financially corrupt, morally bankrupt, and appears more and more every day like a parasite on its way to killing its host. Yep, Software is eating the world, all right.

Marc, that is the society the digital revolution has built and is building every single day. Humans cooperate because they communicate. The digital revolution is now a systemic challenge to the way we interacted since the dawn of time.

I beg you to stop what you started, I dare you to bring these digital CEOs to a round table, and rewrite your seminal article as a manifesto demanding companies stop the bleeding, keep the digitization of human interactions off limits, and immediately build a “hate firewall” to create a perimeter where people can work safely, especially women and minorities. In all my life I have never been to an establishment that deserved the level of hate we see regularly expressed publicly everywhere. Never, and I am certain that is true for you as well.

The state of our industry is disastrous at all levels: leadership, products, staff. It hurts me to come to that conclusion after 43 years of dedication, I still have to come to the realization that things are so broken. You don’t believe me? just talk with your local small business owners.

I’ll leave you with Sir Ken Robinson who knew a thing or two about humanity and transformations: “[the power of imagination](https://www.youtube.com/watch?v=0l-7oF5nzco)”

