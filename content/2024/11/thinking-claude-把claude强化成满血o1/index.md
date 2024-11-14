---
title: Thinking Claude 把Claude强化成满血o1
date: 2024-11-14
extra:
  source: https://mp.weixin.qq.com/s/IAKD0FfcYehs5FsDkLbTJQ
  original_title: Thinking Claude 把Claude强化成满血o1
---
## Summary
**摘要**：
这篇文章展示了17岁高中生Richards Tu（涂津豪）开发的创造力程序，名为Thinking Claude，通过一个名为anthropic_thinking_protocol的独特Prompt，将Claude模型的智能水平极大提升，接近零级（o1）的表现。该Prompt能够使模型的思考逻辑和对话过程更像人类，包括自我提问、思考、解决和创造的能力。这个Prompt在用户中获得广泛关注，被用来解决计算器构建、文学创作等任务，显示了高度的模仿能力。

**要点总结**：
1. **Prompt开发背景**：针对Claude模型思维链与人类思考过程的差异，Richards Tu使用Prompt尝试使其更为拟人化，使其模仿人类思考模式，提高智能对话和解决问题的能力。
2. **Prompt功能**： Prompt的核心是提升Claude的思考逻辑能力和讲解流程，实现模型的自我提问、自我思考、逻辑分析，以及在回答过程中加入甚至讨论可能的替代方案，显示出了丰富的思考过程。
3. **实践效果**： 实验促使Claude模型能够自行解决基本的计算器构建、文学创作任务，同时展示多次迭代和优化提高了模型的成功率和表现。
4. **创新过程**： 这个Prompt通过与Claude互动、优化迭代的方式生成，展示了Prompt在增强大模型能力、推动其接近人类智能表现的可能性上的潜力。
5. **影响力与应用**： Thinking Claude激发了用户对其的极大兴趣，展现了广泛的实用性，包括现实生活问题的解决、创造力提升等方面，并且作者愿意分享资源、向下兼容的插件开发，进一步推动了技术的共享和应用。
## Full Content
Title: 17岁高中生写了个神级Prompt，直接把Claude强化成了满血o1。

URL Source: https://mp.weixin.qq.com/s/IAKD0FfcYehs5FsDkLbTJQ

Markdown Content:
这两天，我被这个Claude3.5这个神级Prompt惊呆了。

佩服的五体投地。  

非常简单的话说，就是它用Prompt把o1级别的思维链，复刻到了Claude3.5里，而且思考逻辑更详细、更像人，甚至思考过程都跟o1一样，可以展开折叠。

![Image 1: Image](https://mmbiz.qpic.cn/mmbiz_gif/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4liclb4MOL7gl43suib6sVIP75aQJXZII0Uguqg1NPBE2RwjdiaFLdEvXA/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

被这个Prompt强化过的Claude3.5，真的强到离谱。智能程度、成功率、像人的程度，都大幅提升。

我的朋友们已经在群里玩疯了。

比如群友@洛小山直接用这段Prompt强化过的Claude3.5，当场造了一个flappy bird。

![Image 2: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4CAuickibiczXiaBRIO3Fj863IyyhHjhQNibFQQpP5JibcoibAy1pXh9MekpbQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

而且是真的能直接玩起来，给他看懵了。

![Image 3: Image](https://mmbiz.qpic.cn/mmbiz_jpg/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4NZjibVVvibViadnKH54N3uJ07lrCJomeUoRpr588qtBM8tzqVafjMtic3w/640?wx_fmt=jpeg)

然后，又生成了德州扑克，不仅可以玩，还是带了AI玩家的那种。。。  

![Image 4: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4WF2KMqEudkBVBHBCXXg0GtAjk7dcF2TtZKa1A9ViboQaF2iabpaEDNeQ/640?wx_fmt=png&from=appmsg)

![Image 5: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4OeiabanVic9eLMAkTsRuBf2zBibBC3XVgFSv1LuhGZFtQMp0smrCtCr3A/640?wx_fmt=png&from=appmsg)

给群里鲜虾包都看震惊了。  

![Image 6: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4uJic4Ns10K25LQySOTfCTK6iats6PxgPg13dnKQFZHiaYw2yvrVdX6X6Q/640?wx_fmt=png&from=appmsg)

但是众人还没来得及为这个case称赞，后面好几个更秀的case就接踵而来。  

这一切，都是来源于那个神级Prompt。  

而这个Prompt，它的名字，叫做Thinking Claude。

顾名思义，思考版的Claude。

我之前先贴他的Prompt吧，非常长，当然你也可以去作者的Github上看，地址是：

https://github.com/richards199999/Thinking-Claude/tree/main

完整的Prompt，是这样的（前方高能预警），可以直接先滑过去，给文章点个收藏下次再复制：

```
<anthropic_thinking_protocol>
```

太恐怖了。  

**而更恐怖的点是，这个Prompt的作者，是一位07年出生，现在17岁的高中生，@Richards Tu，****涂津豪****。**  

![Image 7: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu41lbPfdjib0ib0ciajvSAcZmyyvrWFzic1ewmLglQKZI0EM31GiaWTySmPDQ/640?wx_fmt=png&from=appmsg)

**同时，他也是之前阿里巴巴全球数学竞赛AI赛道的全球第一。**  

我的17岁，和别人的17岁，形成了鲜明的对比。

这个Prompt过于复杂，我先给大家稍微讲一下这个Prompt，让大家能具象化的了解一下它的能力。  

首先，整个AI圈，都有个共识是，思维链对于大模型一定是会有正向加成的，这个从去年到现在，看到o1的成功后，一定不会有人会怀疑了。  

但是以o1为节点，其实思维链在o1前时代和后时代是有很大的不同的。  

在o1前时代，思维链的实际情况跟我们真正想要的思考过程还是有很大的差距的，我们希望思维链是模仿我们人类的思考过程，但模型实际上只是模仿它在预训练中看到的所谓的推理路径。

而在o1后时代，思维链变了。跟那些教科书式的死板解法看起来有非常大的不同，你可以看到模型在回溯历史，会看到它说“或者，我们试试”或“等等，但”这些东西，这些，更像我们人类在思考时候的“内心独白”，或者说，“意识流”。

![Image 8: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4BkZVSq27u4JnR9bju1CAdKzmhsWzpUZXdZicxwPze8fptQUIjjoERlQ/640?wx_fmt=png&from=appmsg)

而涂津豪写这个Prompt的灵感就是来源于此。

Claude本身的底子就很强，如果用类似o1的方式去给Claude加一道拟人化的思维链，虽然不能完美比肩o1，但是会不会在Claude的原基础上有较大的提升？

说试就试，涂津豪就直接按自己的理解，徒手写了一段拟人化的思维链Prompt。这也是Thinking Claude的雏形，v0.01版本。

原Prompt是英文的，我翻译成中文给大家看下。  

![Image 9: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4mmkn9AR7xfs20TC1KDiaSmd3s8WvzCVW2LibXZsYUq469nnUiaibSEUdwQ/640?wx_fmt=png&from=appmsg)

核心其实是那句：**“Claude的思维应该更像是一个意识流。”**

这一版虽然已经有了一些思维链的过程，但是还是偏僵硬，效果也一般，于是涂津豪做了一个很有趣的操作。

他直接把这段Prompt扔给Claude，问他人类的思考框架是什么样的，我要如何优化我的Prompt。

然后Claude给出了一段非常棒的框架，类似于这样的。

![Image 10: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4jiac9VaZkrtNVAUj4zHpeYfrMKwhXwVnhVgKKxRwyLsvsmJ0SbwFxFw/640?wx_fmt=png&from=appmsg)

涂津豪把Claude给出的回答改吧改吧，加到了自己的Prompt里面去。

又新开了一个窗口，把迭代完的思维链Prompt，扔给了Claude3.5，继续跟他对话进行迭代。

如此，修改了80多版，硬生生把Team版的账号对话额度都给用完了。  

才有了现在的Thinking Claude。

当你把这段Prompt发送给Claude后，你就可以随便提出你的问题。  

![Image 11: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4Xib7kD3uPXyLkLwBMR75JaqQibJZLCpzpUAUTPTbFO9b334POYb2Qv6Q/640?wx_fmt=png&from=appmsg)

比如，我想让他做一个计算器。他就会先思考一整段应该怎么做，再去进行操作。  

这个思考过程，就极度的有趣了。  

我们来看看Claude3.5在上了这段Prompt之后，说了什么话。

![Image 12: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4aM5icG4UdKROHSny2hGa4FqOaJKUlGib9PniceyU10ym0whicvXfcI7YTw/640?wx_fmt=png&from=appmsg)

最重要的是中间那句话。

**“但我应该包括更高级的操作吗？也许是科学功能？不，让我们从基础知识开始，因为用户没有指定任何更复杂的东西。”**  

自问自答，自己思考，然后理清需求。

这是真正的思考过程。

为什么它不把计算器设计的非常复杂呢，因为我们没有指定。我们只是要想要一个简简单单的计算器。

他好像，可以理解我们这句指令，背后的一些东西。

当然，最后的计算器，肯定是一把成，这玩意对于加了思维链的Claude3.5来说，几乎没有难度。  

![Image 13: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4blsvHibHYZnNiaUpmhntliaLh2kVduEXtcibDWNkjpaNdUA9M4GVY5hFIQ/640?wx_fmt=png&from=appmsg)

而在文学创作上，表现的一样很好。  

比如我们希望Claude，**“给我一个关于科幻短篇小说的糟糕的想法，但是要出色地执行它。**”  

糟糕的想法，但出色的执行，听着就有挑战。

我们来看看Thinking Claude是怎么思考的。

![Image 14: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4eiaiaeK2XqsOWP6aFozEKzGhpRjWMUQlicO2pLmCqpe0icqkw1IcYW1cJg/640?wx_fmt=png&from=appmsg)

“或者...”，“等等，有了”

这些人类的思考，人类的欢呼，在这条思维链中体现了。  

三体人那种思维透明的交流过程，忽然有了一种非常具象化的表达。

最后，这篇短篇小说诞生了。

作为一个科幻迷，刘慈欣老师的忠实读者，当我看到这篇“科幻故事”的事后，我是脑子一嗡。  

我想过科幻故事的很多种展开，但是我没想象过，这是用几封信串起来的故事。

我觉得，我有必要，放一下这个故事的完整版，让大家感受一下，Thinking Claude的强大。

![Image 15: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4Tcib4n4QomQVjRaRL4Tv91rqpDZowZiaYDW6wCrhx84QPZsm7aAVJ6kw/640?wx_fmt=png&from=appmsg)

![Image 16: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4cJEeokSTVibrQ1MuibJ6ibVb6cvhSdGNofzS250QOAwlbPtPftCvebTGA/640?wx_fmt=png&from=appmsg)

![Image 17: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4sr3wUUPcrR8otYLcYMrxrYCYyd0TkiavLbiaKMDrFvHz3I1sBEVwyCZg/640?wx_fmt=png&from=appmsg)

![Image 18: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4sdsQPbfCtc6h5ico6AIAQWIOysVdvicxib0sf58RhvMswz2sH7WFroRow/640?wx_fmt=png&from=appmsg)

![Image 19: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4RLkjV6Rku1LBKWQexia7iclqWA1AdHNXfcnL8uZBVOCeibnkqHlnibLuLw/640?wx_fmt=png&from=appmsg)

凌晨2点34，我看完了这篇科幻故事。

然后抬头看向窗外的星空。

我忽然明白了情感的意义。

这是一篇，由AI写出来的小说，所带给我的震撼。  

而这，是由Thinking Claude加持之后的。

现在，你能体会到，Thinking这个力量的强大吗。

你可曾感受过，我们人类，思考力量之强大么？

所以，我在这，同样把这个Prompt安利给你们。

让学会思考的大模型，能帮助我们，做更多的事情。  

当然，事情到这，其实还没完。  

涂津豪说，Claude3.5的思考过程，也希望像o1一样，能让用户自主选择展开还是收起，现在是一直都展开的。

![Image 20: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu46KjUcwOaongsDytjGMAVGRUgodqTibFoKSBBn5PbwpbSzib18Pe9D40g/640?wx_fmt=png&from=appmsg)

Think代码块里承载的，就是Claude的思考过程。  

但是我是真的觉得，看Thinking Claude的思考过程，其实是一种享受。

而涂津豪觉得，并不是所有人，都希望看到这个思考过程来打扰用户的。

所以他想完全复刻o1，再做一个展开和收起。

而这个想法，他也不是很懂该怎么做，于是，他去问了Thinking Claude。

而Thinking Claude告诉他，开发个Chrome插件吧，就能解决这个问题。

于是，又在一番折腾之后，这个插件出炉了。  

当你装上后，你会发现。  

整个思考过程，被折叠了。

![Image 21: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu494y10tCZpgibOLyzM21S1GgkkqHu5jBwia71fiaeibbosDXdINk9F5VoeA/640?wx_fmt=png&from=appmsg)

而在你需要的时候，会随时展开。

过于酷了。  

这个插件我放在后台了，**公众号私信“TC”就有**，下载完成以后解压，然后进入Chrome浏览器的扩展程序管理界面，打开右上角的开发者模式，左上角加载解压完的文件夹就行。

![Image 22: Image](https://mmbiz.qpic.cn/mmbiz_png/OjgKEXmLURpWgSMGibXEPErjW1CvfYYu4bu7JOH2o3aZ9n1mste7sRbtXvWzQEV4N4bm30vegibQGJiaLnmw9ksLQ/640?wx_fmt=png&from=appmsg)

真的，以Claude底层能力，加上Thinking Claude的思维链强化，再有强无敌的Artifacts功能。

称为满血o1都不为过。  

现在的o1，不能识图、不能运行代码、排版一团糟，体验真的很差。

相比之下，Claude实在强太多了。  

最后，谢谢Claude，也谢谢涂津豪。  

17岁的少年。

最美的热血。  

实属吾辈楷模。  

希望能一起在成为最厉害最厉害最厉害的道路上。

共勉。

******以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。******

\>/ 作者：卡兹克

\>/ 投稿或爆料，请联系邮箱：wzglyay@gmail.com

