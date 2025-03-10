---
title: 八位 Google 员工开创了现代 AI 的新纪元，揭秘他们的故事 [译]
date: 2024-10-18
extra:
  source: https://baoyu.io/translations/story/eight-google-employees-invented-modern-ai-transformers-paper
  original_title: 八位 Google 员工开创了现代 AI 的新纪元，揭秘他们的故事 [译]
---
## TL;DR
以下是对这篇文章的简短总结：

Transformer 模型是人工智能技术的重要组成部分，它广泛应用于自然语言处理和图像识别等领域。该模型由 Google 研究团队开发，核心思想是通过自注意力机制来处理序列数据，提高模型表现和效率。Transformer 模型的成功受到广泛关注，成为人工智能发展史上的一项重要成就。
## Summary
本文介绍了 Transformer 模型的诞生故事， Transformer 模型是现代人工智能技术的重要组成部分。它的诞生，得益于一群充满创新热情的研究人员，以及支持他们的环境和文化。Transformer 模型被广泛应用于自然语言处理和图像识别等领域。

下面是 Transformer 模型诞生故事的重点摘要：

Transformer 模型的核心思想是通过自注意力机制来处理序列数据。这种方法能够更好地捕捉序列数据中的长期依赖和关系，从而提高模型的表现和效率。Transformer 模型由 Google 的一支研究团队进行了研究和开发。团队的主要成员，包括 Ashish Vaswani、Jakob Uszkoreit、Alex Grave 的主导下，经历了数月的研究和开发，最终成功开发了第一版 Transformer 模型，并且获得了令人瞩目的实验结果。Transformer 模型的成功受到业界的广泛关注，并且很快被应用于多个领域，包括自然语言处理和图像识别等。总之，Transformer 模型的诞生是人工智能发展史上的一项重要成就。

Transformer 模型诞生故事的重点包括：

1.  **团队背景**: introduces Researchers from Google, including Ashish Vaswani,Jakob Uszkoreit,Niki Parmar,Llion Jones,Łukasz Kaiser,Aidan Gomez,Noam Shazeer.
2.  **问题解决**: describes the limitations of traditional recurrent neural networks (RNNs) and the need for a new approach to handle sequential data.
3.  **自注意力机制**: explains the self-attention mechanism introduced in the Transformer model, which allows the model to weigh the importance of different input elements relative to each other.
4.  **模型结构**: describes the overall structure of the Transformer model, including the encoder, decoder, and attention mechanisms.
5.  **实验结果**: presents the experimental results of the Transformer model on various tasks, including machine translation and image recognition.
6.  **影响和发展**: discusses the impact of the Transformer model on the field of natural language processing and its applications in other areas, such as computer vision and speech recognition.

 Transformer 模型的成功并不局限于这些研究人员和他们的团队。事实上，它们的工作激发了整个研究界对新型序列模型的探索和开发，最终推动了一场真正的 AI 革命。
## Full Content
Title: 八位 Google 员工开创了现代 AI 的新纪元，揭秘他们的故事 [译]

URL Source: https://baoyu.io/translations/story/eight-google-employees-invented-modern-ai-transformers-paper

Markdown Content:
他们因缘际会，对一项创意产生了浓厚的兴趣，并共同撰写了“Transformers”论文——这是近代史上最具里程碑意义的技术革新。

2017 年春，一篇名为“Attention Is All You Need”的科研论文罗列了八位作者的名字，这些人都是 [Google](https://www.wired.com/story/google-prepares-for-a-future-where-search-isnt-king/) 的研究员，虽然其中一人已经离开了公司。最资深的贡献者 Noam Shazeer 在看到初稿时，对自己的名字排在第一位表示惊讶，这似乎意味着他做出了最重大的贡献。“这是我没想到的，”他表示。

![Image 1: 此图像可能展示了艺术作品、绘画、成人、人脸、头部、摄影作品及肖像画](https://media.wired.com/photos/65f9c29a65a43d9e4f031280/master/w_1600%2Cc_limit/Wired_MA_06.jpg)

此图像可能展示了艺术作品、绘画、成人、人脸、头部、摄影作品及肖像画

**/ 姓名：NOAM SHAZEER / 职务：CHARACTER AI 联合创始人及首席执行官**

在决定作者名单的排列顺序上，谁应该位列前茅，谁又应该位居末尾，总是需要慎重考虑的。尤其是在这种情况下，每位参与者都在这次真正的团队合作中留下了独特的印记。随着研究人员加紧完成他们的论文，他们最终选择了打破对贡献者排序的常规做法。他们在每个名字旁边标上了星号，并加上一条脚注：“各贡献均等”，声明“作者名单的排列顺序是随机的。”这篇论文在截稿日期前不久提交给了一个知名的人工智能会议——从此开启了一场科技革命。

ADVERTISEMENT

即将迎来七周年的[“注意力”论文](https://arxiv.org/abs/1706.03762)已成为传奇。作者们以一项正在蓬勃发展并持续改进的技术为起点——那就是被广泛称作神经网络的 AI——并将其演变成了一种异常强大的数字系统，其产出之惊人，仿佛出自[外星智能](https://www.wired.com/story/plaintext-groq-mindblowing-chatbot-answers-instantly/#intcid=recommendations_wired-bottom-recirc-v4_efa0ebfa-8b30-44aa-826f-37cbd7ba731a_similar2-3)之手。这一新架构，名为变换器（Transformers），已成为包括[ChatGPT](https://www.wired.com/tag/chatgpt/)在内及诸如 Dall-E 和 Midjourney 这样的图形生成器背后的关键技术。Shazeer 现在回想起来笑称，若早知道这篇论文会大受欢迎，他“可能对作者的排名顺序考虑得更多一些。”现在，所有八位作者都小有名气了。“仅仅因为我署名在一篇论文上，就有人来找我自拍！”Llion Jones，恰好是名单上的第五位，这样说。

![Image 2: Image may contain Art Drawing Adult Person Accessories Glasses Face Head Photography and Portrait](https://media.wired.com/photos/65f9c534d09dadb341af1007/master/w_1600%2Cc_limit/Wired_MA_04.jpg)

Image may contain Art Drawing Adult Person Accessories Glasses Face Head Photography and Portrait

**/ 名字：LLION JONES / 职务：SAKANA AI 的联合创始人**

“如果没有 Transformer 技术，我们可能根本不会站在这里。”这是[Geoffrey Hinton](https://www.wired.com/story/geoffrey-hinton-ai-chatgpt-dangers/)的看法，他虽不是本文作者之一，却是全球最知名的 AI 科学家之一。他谈到的是我们正经历的重大转折点，[OpenAI 以及其他公司正构建着](https://www.wired.com/story/what-openai-really-wants/)在某些方面能够与人类成果抗衡乃至超越的系统。

自那以后，所有八位作者已经离开了 Google。就像数以百万计的其他人一样，他们现在正以某种方式参与到他们在 2017 年创造出的技术驱动的系统中。我采访了这八位 Transformer 的创造者，试图还原那个创新突破的全貌：一次人类智慧的集结，旨在创造出一台最终可能拥有独立发声权的机器。

![Image 3: Image may contain Art Drawing Adult Person Face Head Photography and Portrait](https://media.wired.com/photos/65f9c32209f8af8a0f4dfce5/master/w_1600%2Cc_limit/Wired_MA_01.jpg)

Image may contain Art Drawing Adult Person Face Head Photography and Portrait

**/ 名字：JAKOB USZKOREIT / 职务：INCEPTIVE 的联合创始人及首席执行官**

Transformer 的故事从八位创造者中的第四位，Jakob Uszkoreit，开始。

Uszkoreit 是 Hans Uszkoreit 的儿子，后者是一位闻名遐迩的计算语言学大家。1960 年代末，还是高中学生的 Hans 因反抗苏联对捷克斯洛伐克的侵略，在东德被囚禁了 15 个月。获释之后，他逃亡至西德，在柏林投入计算机与语言学的研究。迁往美国后，他在加州门洛帕克的 SRI 研究所从事人工智能研究，此时 Jakob 降生。家庭最终返回德国，Jakob 在那里接受大学教育。尽管最初没有打算深入研究语言领域，但在开始研究生学习的旅程中，他通过在谷歌山景城办公室的一次实习，意外地成为了公司翻译团队的一员，从此踏上了家族的足迹。放弃了攻读博士学位的计划，他在 2012 年决定加盟谷歌的一个项目组，致力于开发一种新系统，该系统能直接在搜索页回应用户的提问，无需跳转至其他网页。正值苹果发布 Siri，这个能够以轻松对话形式提供直接答案的虚拟助手，令谷歌高层察觉到一股强烈的竞争压力，担心 Siri 会分食他们的搜索流量，因此他们开始更加重视 Uszkoreit 所在的新团队。

“这只是一场无谓的恐慌，”Uszkoreit 表示。实际上，Siri 从未对 Google 构成真正的威胁。然而，他对深入探讨能够与人类进行对话的计算机系统抱有极大兴趣。在那时，一度被学术界边缘化的循环神经网络突然展现出超越其他人工智能技术的能力。这些网络结构复杂，通过层层传递信息来挑选出最合适的回应。在图像识别等领域取得重大突破的神经网络标志着人工智能新纪元的到来。Google 紧随其后，忙不迭地调整团队结构，以融入这些新技术。公司期望其系统能生成像人一样的反应，比如自动完成电子邮件中的句子或是打造简易的客户服务聊天机器人。

但这个领域很快就遭遇了瓶颈。当处理长文本时，循环神经网络显得力不从心。拿这样一段话来说：“Joe 是个棒球运动员，享用了丰盛的早餐之后，他去公园打球，击出了两个安打。”为了理解“两个安打”，语言模型需要回忆起关于棒球的那部分内容。换句话说，它需要保持关注。长短期记忆（LSTM）技术被引入作为解决方法，它让语言模型能够处理更长、更复杂的文本序列。然而，计算机还是按部就班地一词一词地处理文本，忽视了可能在文段后出现的上下文提示。“我们使用的方法，归根到底，就像是临时补救措施，”Uszkoreit 说。“我们没能让这些方法在大规模上有效运作。”

在 2014 年左右，他开始酝酿一个新颖的概念，称之为自注意力。这种网络结构能够参考文章中的任意其他部分来翻译单词。这些部分有助于阐明单词的含义，从而使系统能够更准确地进行翻译。“这实际上是一个考虑所有因素的高效方法，它能够同时处理多个输入，然后以非常精确的方式抽取信息，”他解释道。尽管 AI 科学家们通常避免将神经网络的比喻与生物大脑的实际运作方式混淆，但 Uszkoreit 相信，自注意力在某种程度上与人类处理语言的方式有着相似之处。

Uszkoreit 认为，相比循环神经网络，自注意力模型可能更快、更高效。其处理信息的方式非常适合那些为了支持机器学习而大量生产的强大并行处理芯片。不同于逐字查看的线性方法，自注意力采用了一种并行方法，能同时处理多个单词。Uszkoreit 猜想，如果操作得当，完全依赖自注意力模型就能取得更佳的效果。

虽然并不是每个人都对这一理念抱有同样的期待，甚至包括 Uszkoreit 的父亲在内——在他儿子服务于该公司期间，他已经获得了两项 Google 教师研究奖。“因为这一理念颠覆了所有现有的神经网络架构，所以人们对此颇为怀疑，”Jakob Uszkoreit 表示。彻底摒弃循环神经网络？这简直是异端！“通过与我父亲的晚餐谈话，我们发现在这个问题上并不总是看法一致。”

Uszkoreit 成功说服了几位同事，一起探索自注意力机制的奥秘。他们的尝试迅速展现出潜力，2016 年他们便发表了一篇研究论文。虽然团队的实验仅仅触及了一小段文本，但 Uszkoreit 有着更远大的梦想，想要深入研究。可惜，他的合作伙伴并不买账，宁愿像得到一些小额赢利的赌徒一样，满足于将新学到的知识应用于实践。“事实证明，这方法行得通，”他回忆说，“参与那篇论文的团队成员对于能够在谷歌的各种领域，包括搜索和广告，应用它而感到兴奋。这无疑是一次巨大的成功，但我并不想就此止步。”

在 Uszkoreit 看来，自注意力机制有能力完成更为重大的任务。他总是向每一个愿意（或不愿意）倾听的人强调，_肯定有更好的方法_。在谷歌园区北侧的 Charleston 路 1945 号大楼（根据地址命名）的白板前，他激情洋溢地描绘着他的愿景。

![Image 4: Image may contain Art Drawing Face Head Person Photography Portrait and Adult](https://media.wired.com/photos/65f9c3b3b60e315d4b0e135c/master/w_1600%2Cc_limit/Wired_MA_03.jpg)

Image may contain Art Drawing Face Head Person Photography Portrait and Adult

**/ 名称：ILLIA POLOSUKHIN / 职业：NEAR 的联合创始人**

2016 年的一天，Uszkoreit 在谷歌的一家咖啡厅与来自乌克兰的科学家 Illia Polosukhin 一起用餐。Polosukhin 在谷歌的工作已近三年，他的任务是回答搜索框中直接提出的问题。这个任务进展得不是很顺利。“要在 Google.com 上提供答案，你需要的解决方案既要成本低廉又要性能出色，”Polosukhin 表示，“因为回应时间只有几毫秒。”面对 Polosukhin 的不满，Uszkoreit 轻松提出了解决方案。“他提出了一个想法，为什么不尝试自我关注机制 (self-attention) 呢？”Polosukhin 说。

Polosukhin 时不时会和一位名叫 Ashish Vaswani 的同事合作。Vaswani 出生于印度，大部分时间在中东成长，他前往南加州大学，从该校顶尖的机器翻译小组获得了博士学位。学成之后，他搬到了山景城，加入了谷歌，尤其是一个名为 [Google Brain](https://www.wired.com/2013/05/neuro-artificial-intelligence/) 的新兴团队。他描述 Google Brain 为“一个具有激进理念的团队”，他们坚信“神经网络能够促进人类的理解进步”。但他仍在寻找一个重大的项目投身其中。他的团队位于 1965 号楼，与 Polosukhin 的语言团队在 1945 号楼为邻。当他听说自我关注的概念时，他认为这或许就是他一直在寻找的项目。他决定参与这项工作。

![Image 5: Image may contain Art Drawing Adult Person Face Head Photography and Portrait](https://media.wired.com/photos/65f9c4220af8fef18d227d06/master/w_1600%2Cc_limit/Wired_MA_08.jpg)

Image may contain Art Drawing Adult Person Face Head Photography and Portrait

**/ 名字：ASHISH VASWANI / 职位：ESSENTIAL AI 的联合创始人及首席执行官**

三位研究者共同制定了一个设计文档，命名为《变形金刚：迭代自我关注及其在各种任务中的处理》。Uszkoreit 表示，“变形金刚”这个名字从项目伊始就已确定。他们的构想是，这一机制能够转化其处理的信息，使系统能够像人类一样抽取信息，或至少产生这样的假象。另外，Uszkoreit 还回忆说，他小时候非常喜欢玩孩之宝的变形金刚玩具，“我很小的时候就有两个变形金刚玩具。”这份文档以一幅图画作结，图中六个变形金刚在山地互射激光。

论文的开篇是一句带有些许狂妄的声明：“我们太棒了。”

2017 年初，Polosukhin 离开谷歌，开始创建自己的企业。那时，新的合作伙伴陆续加入。一位来自印度的工程师 Niki Parmar 曾在印度为一家美国软件公司工作，后来她搬到了美国。2015 年，她从南加州大学获得了硕士学位，并且收到了所有大型科技公司的邀请。她选择加入谷歌，并很快与 Uszkoreit 一道工作，专注于开发模型变体，以提升谷歌搜索的效能。

![Image 6: Image may contain Art Drawing Face Head Person Photography Portrait and Adult](https://media.wired.com/photos/65f9c4aa874aa893d485456a/master/w_1600%2Cc_limit/Wired_MA_02.jpg)

Image may contain Art Drawing Face Head Person Photography Portrait and Adult

**/ 姓名：NIKI PARMAR / 职业：ESSENTIAL AI 的联合创始人**

新加入的成员之一是 Llion Jones，一个土生土长的威尔士人，他对计算机情有独钟，原因是他觉得计算机领域充满了不寻常的魅力。在伯明翰大学期间，他修读了一门人工智能课程，期间他对作为课堂趣谈的神经网络产生了浓厚的兴趣。2009 年 7 月，他获得了硕士学位，但因为经济衰退难以找到工作，不得不领取了几个月的失业救济。最终，他在一家本地企业找到了一份工作，并随后抱着试一试的心态向 Google 投递了简历。出乎意料的是，他被录用了，并最终进入了 Google 研究部门，彼时的上司是 Polosukhin。某天，Jones 从同事 Mat Kelcey 那里第一次听说了自注意力这一概念，这促使他加入了 Transformer 团队。（后来，当 Jones 向 Kelcey 介绍 Transformer 项目时，Kelcey 表示怀疑。“我跟他说，‘我不觉得这能成，’这无疑成了我这辈子最大的误判，”Kelcey 如今回忆道。）

Transformer 项目吸引了其他一些也在努力改善[大语言模型](https://www.wired.com/story/how-chatgpt-works-large-language-model/)的 Google Brain 研究员加入。第三批加入的成员包括波兰理论计算机科学家 Łukasz Kaiser 及其实习生 Aidan Gomez。Gomez 在加拿大安大略的一个小农村长大，那里的家人每年春天都会采集枫树液制作糖浆。在多伦多大学就读三年级时，他对 AI 产生了浓厚的兴趣，并加入了 Geoffrey Hinton 领导的机器学习小组。他开始向在 Google 发表过有意思的论文的人发邮件，提出自己对其研究工作的拓展想法。Kaiser 对此感兴趣，邀请他来实习。直到几个月后，Gomez 才得知，这些实习机会原本是为博士生准备的，而他只是一个本科生。

Kaiser 和 Gomez 很快意识到，自注意力（self-attention）技术似乎是解决他们所面临问题的一个前景光明且更具革命性的方案。“我们认真讨论了是否要将两个项目合并的问题，”Gomez 表示。答案是肯定的。

Transformer 团队开始构建一个自注意力模型，用于实现跨语言文本的翻译。他们通过一个称为 BLEU 的标准来衡量模型的表现，该标准通过将机器的翻译结果与人类翻译者的工作进行对比。他们的新模型从一开始就展现出了良好的性能。“我们从没有任何概念验证转变为至少能与当时的最佳选择，即 LSTM，媲美，”Uszkoreit 说。但相较于长短期记忆模型（long short-term memory），它并没有显示出更好的表现。

直到 2017 年的一天，Noam Shazeer 偶然间了解到了他们的项目，这个局面才有了转机。作为一名加入谷歌于 2000 年的资深员工，Shazeer 以其在公司早期广告系统上的贡献而成为了一位内部传奇。近年来，他对大语言模型（LLM）产生了兴趣，尽管这些模型还远未实现他所设想的流畅对话。

Shazeer 记得，那天他正走在 1965 号楼的走廊里，经过 Kaiser 的工作区。他无意中听到了一场热情的讨论。“我记得 Ashish 正谈论采用自注意力技术的想法，Niki 显得非常兴奋。我心想，哇，这听起来是个很棒的点子。看起来这是一群既有趣又聪明的人在做一件有潜力的事情。”Shazeer 对现有的循环神经网络感到“不耐烦”，并想，“让我们来改变它们吧！”

Shazeer 的加入对团队至关重要。“理论上的或基于直觉的机制，比如自注意力（self-attention），其实现通常需要极其细致，往往只有少数经验丰富的技术‘巫师’才能让它们初现生机，”Uszkoreit 表示。Shazeer 很快就开始施展他的“魔法”。他决定自行编写 transformer 团队代码的一个新版本。“我把这个基本想法变成了现实，”他说。虽然偶尔会向 Kaiser 咨询一些问题，但大多数时间，他表示自己“只是默默工作了一段时间，然后回来宣布，‘看，它有效果了。’”凭借团队成员后来形容的“魔法”、“炼金术”以及“技术细节”，他成功将系统提升至新的高度。

“这标志着冲刺阶段的开始，”Gomez 说。他们感到极度振奋，同时也想抓住即将来临的重要截止日期——5 月 19 日，即在当年最大的 AI 盛会，12 月的神经信息处理系统会议上提交论文的最后期限。随着硅谷的冬季渐渐转向春天，实验进度明显加快。他们测试了两个版本的 transformer 模型：一个是经过 12 小时训练得到的，另一个更为强大的版本命名为 Big，经过了三天半的训练。他们将这两个模型应用于英德翻译任务上。

基础模型超越了所有竞争对手——而 Big 版本则以一项决定性的 BLEU 分数刷新了记录，同时在计算效率上也表现更佳。“我们完成这一切的时间比任何人都短，”Parmar 说。“这只是开始，因为成绩还在不断提高。”当 Uszkoreit 得知这一成就时，他从他的山地探险车里拿出了一瓶珍藏的香槟庆祝。

截至最后期限的前两周，整个团队都陷入了疯狂的工作状态。虽然有些团队成员在官方记录上还保留着 1945 大楼的工位，但他们大多数人实际上是在 1965 大楼工作，原因很简单：那里有一台更上档次的浓缩咖啡机。Gomez 回忆说：“大家几乎都在夜以继日地工作。”作为实习生的他，不仅深陷代码调试的无尽循环中，还负责制作论文中的图示和图表。在这样的项目中，常常会做一种“消融测试”，即移除某些部分，以验证剩余部分是否足以独立完成任务。

Gomez 讲到：“我们尝试了各种可能的技巧和模块组合，探究哪些是有用的，哪些是无用的。不行的就拿掉，换成其他的。”他说，“模型为何会表现出这种违背直觉的行为？原来是我们忘了正确设置遮蔽。现在能正常工作了吗？可以了，那就进入下一个阶段。所有这些，都是我们如今称之为 Transformers 模型的关键组成部分，它们都是通过快节奏的反复试验和错误校正过程中产生的。”Shazeer 负责实现的消融测试最终呈现出了一种“简约之美”，正如 Jones 所说，“Noam 简直就像个魔法师。”

Vaswani 记得，有一次在凌晨时分，他躺在办公室的沙发上，准备休息。那时，隔断沙发与房间其他部分的窗帘引起了他的注意，窗帘上的图案在他看来像极了神经元和突触。Gomez 也在场，Vaswani 对他说，他们手头的研究工作将远远超越机器翻译的范畴。“就像人脑需要将语言、音频、视觉等多种模态融为一体一样，”他说，“我强烈感觉到我们正在触及到某种更为普遍适用的东西。”

在 Google 的上层领导看来，这个项目不过是另一个引人注目的 AI 项目。我询问了几位 Transformer 团队的成员，是否有过被上级召唤汇报项目进展的情况。回答是并不频繁。但是 Uszkoreit 表示，“我们意识到这可能是一个非常重要的突破。”“这让我们对论文结尾提到的未来工作特别着重，其中我们讨论了未来的可能性。”

这段论文预见了接下来可能采取的方向——将 Transformer 模型应用到几乎所有人类表达的形式。“我们对基于注意力模型的未来充满期待，”他们写道。“我们计划将 Transformer 应用于除文本以外的输入和输出方式，进一步探索图像、音频和视频。”

截止日期前几天，Uszkoreit 意识到他们需要一个吸引人的标题。Jones 提到，团队决定彻底摒弃了被广泛接受的最佳实践，尤其是 LSTM，转而专注于一个技术——注意力。Jones 回忆道，披头士乐队有一首歌叫做“All You Need Is Love（你所需要的就是爱）”。那么，为什么不将这篇论文命名为“Attention Is All You Need（注意力就是你所需要的）”呢？

_披头士乐队？_

“我是英国人，”Jones 说。“这个想法几乎是即兴而来的。我没想到他们真的会采纳。”

直到截止日期那一刻，他们还在不断地汇总实验结果。“提交论文前五分钟，我们才收到了英法转换的数据，”Parmar 回忆道。“那时我正坐在 1965 年的小厨房里，匆忙记录下最后一组数据。”最终，在截止时间前仅剩两分钟，他们提交了论文。

Google 和其他许多科技公司一样，迅速为这项工作申请了临时专利。这样做的目的不是为了阻止他人使用这些创意，而是为了在专利战中保护自己。（公司坚持一种观点：“只要技术进步，Google 就能从中受益。”）

当 Transformer 团队收到会议同行评审的反馈时，意见各不相同。Parmar 表示：“有的评价是正面的，有的极为肯定，还有的是‘可以接受’。”最终，他们的论文被选中在一个晚间的海报展示环节中展出。

到了 12 月份，这篇论文逐渐成为热门话题。12 月 6 日举行的四小时展示会吸引了众多科学家，他们希望深入了解。作者们不停地讲解，直到声音嘶哑。即便是在晚上 10:30 会议结束时，现场仍然人头攒动。“最后是安保人员告诉我们必须离开，”Uszkoreit 说。对他来说，最令人满意的时刻莫过于计算机科学家 Sepp Hochreiter 走过来，对他们的工作表示赞赏。考虑到 Hochreiter 是长短期记忆技术的共同发明者，这样的赞扬分外重要，因为 Transformer 正在挑战长短期记忆技术在 AI 领域中的主导地位。

Transformer 技术并没有立刻颠覆全世界，甚至没有立即改变 Google。Kaiser 回忆，论文发表时，Shazeer 曾建议 Google 的高层完全摒弃传统的搜索索引，转而使用基于 Transformer 的庞大网络——这实际上是对 Google 信息组织方式的一次根本性转变。那时，连 Kaiser 本人都觉得这个提议不切实际。然而，现在人们普遍认为，这种变革只是时间问题。

一家名叫 OpenAI 的新兴企业抓住了一个重大机遇，比其他人更快更果断地行动起来。这家公司的首席研究员 Ilya Sutskever，在谷歌期间就认识了 transformer 研发团队，他建议团队中的一位科学家 Alec Radford 探索这个新颖的想法。他们的努力孕育了首批 GPT 产品。正如 OpenAI 的 CEO Sam Altman 去年与我分享的，“transformer 论文发布之初，谷歌里几乎没人真正理解它的深远意义。”

事实上，谷歌内部的情况要复杂得多。“很显然，我们认识到 transformers 能够创造出令人难以置信的成果，”Uszkoreit 表示。“你可能会问，为什么在 2018 年我们就没推出类似 ChatGPT 的产品？事实上，到了 2019 年乃至 2020 年，我们完全有能力推出 GPT-3 或是 3.5 版。真正的问题不在于我们是否意识到了它的潜力，而是在于面对这一发现，我们为何没有采取行动。这个问题的答案并不简单。”

![Image 7: 这张图片展示了艺术、绘画、成人、人物、脸部、头部、摄影以及肖像](https://media.wired.com/photos/65f9c64fe3773ae5531008fc/master/w_1600%2Cc_limit/Wired_MA_07.jpg)

这张图片展示了艺术、绘画、成人、人物、脸部、头部、摄影以及肖像

**/ 姓名：AIDAN GOMEZ / 职位：COHERE 共同创始人及首席执行官**

众多技术批评家认为，谷歌已从一个创新为核心的乐园转变为一个以利益为先的官僚机构。正如 Gomez 在《金融时报》[告诉](https://www.ft.com/content/37bb01af-ee46-4483-982f-ef3921436a50)我们的，“他们未能跟上时代，也没有采用新兴技术。”然而，对于一个技术领先行业并且几十年来收益丰厚的巨头公司来说，这样做确实需要极大的勇气。自 2018 年起，谷歌开始将 Transformer 技术集成到其产品中，首发产品是其翻译工具。同年，它还推出了一个名为 BERT 的新型基于 Transformer 的语言模型，并在次年开始应用于搜索引擎。

然而，与 OpenAI 的突破性进步和微软将基于 Transformer 的系统大胆融合进其产品线相比，谷歌的这些内部改变显得过于保守。去年，当我询问 CEO Sundar Pichai 为什么谷歌没有成为首个推出像 ChatGPT 这样的大型语言模型的公司时，他表示，在这种情况下，观望他人先行对谷歌是有利的。“我不完全确定如果由我们来首创，结果会不会这么成功。事实上，人们在看到它如何运作后，我们能做的更多，”他解释说。

不可否认，这篇论文的八位作者均已离开谷歌。Polosukhin 所领导的 Near 公司，开发了一个市值高达 40 亿美元的区块链技术。Parmar 和 Vaswani 在 2021 年联手创办了 Adept（预估价值 10 亿美元），并已着手其第二个项目，Essential AI（获得资金 800 万美元）。位于东京的 Sakana AI，由 Llion Jones 创建，市值达到了 2 亿美元。Shazeer 在 2021 年 10 月离开后，共同创立了 Character AI（估值大约 50 亿美元）。实习生出身的 Aidan Gomez 于 2019 年在多伦多共同创立了 Cohere（估值约 22 亿美元）。Jakob Uszkoreit 的生物技术公司 Inceptive，市值为 3 亿美元。这些公司（除了 Near）均采用了 transformer 技术。

![Image 8: 该图片描绘的是一位艺术家的肖像，可能包含了艺术作品、绘画、面部特写、个人形象、摄影作品及肖像画等元素。](https://media.wired.com/photos/65f9c5aa1c6cb005dfa0fe0d/master/w_1600%2Cc_limit/Wired_MA_05.jpg)

该图片描绘的是一位艺术家的肖像，可能包含了艺术作品、绘画、面部特写、个人形象、摄影作品及肖像画等元素。

**/ 名字：LUKASZ KAISER / 职位：OPENAI 研究员**

Kaiser 是仅有的未创办公司的成员。他加盟 OpenAI，成为了一项名为 [Q\*](https://www.wired.com/story/fast-forward-clues-hint-openai-shadowy-q-project/) 新技术的共同发明者，Altman 曾在去年表示，该技术将“推动我们突破无知的界限，拓宽发现的新领域。”（当我在采访中试图向 Kaiser 询问此项技术时，OpenAI 的公关团队差点儿采取行动让他保持沉默。）

谷歌是否对这些离职者感到惋惜？毫无疑问，特别是那些转投新兴 AI 创业公司的前员工。（皮查伊在谈到 Transformer 技术团队的成员流失时提醒我，业界瞩目的 OpenAI 也经历了人才流失：“AI 领域变化万千，非常活跃，”他表示。）但谷歌可以骄傲地声称，它营造了一种环境，鼓励追寻与众不同的想法。“从很多方面来说，谷歌一直走在前列——他们投资于顶尖人才，并打造出一个让我们能自由探索、不断突破的环境，”帕尔马如是说。“它需要时间来接受这些新想法，并不令人意外。对于谷歌而言，挑战更大、风险也更高。”

没有这样的创新氛围，就不会有 Transformer 的诞生。所有的作者都是谷歌的员工，他们在同一办公室内协作。偶然在走廊上的相遇、午餐时的闲聊催生了伟大的创意。此外，这个团队在文化上也极其多元。八位作者中有六人出生于美国以外，剩下两人分别是两位在加州暂居的德国绿卡持有者的孩子，以及一个家族曾逃避迫害的第一代美国人。

乌斯科雷特在柏林的办公室分享道，创新的关键在于创造正确的条件。“把一群对某事充满热情、正处于人生正确阶段的人聚在一起是关键，”他说。“如果你能做到这些，同时在做事时享受乐趣，处理正确的问题，加上一点运气，魔法就会发生。”

乌斯科雷特与他那位著名的父亲之间也发生了不可思议的故事。经过无数次的餐桌辩论，汉斯·乌斯科雷特的儿子现在报告说，他的父亲已经共同创办了一家致力于开发大语言模型的公司。当然，这一切都离不开 Transformer。

