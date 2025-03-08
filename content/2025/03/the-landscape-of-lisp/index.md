---
title: The Landscape of Lisp
date: 2025-03-08
extra:
  source: https://churchofturing.github.io/landscapeoflisp.html
  original_title: The Landscape of Lisp
---
## Summary
**摘要**：
本文是作者对Lisp编程语言家族的概述，旨在帮助有兴趣的读者选择适合自己的Lisp方言。Lisp语言自1960年John McCarthy发表重要论文后，经历了多次演变，形成了多种方言，如Scheme、Common Lisp、Racket和Clojure。作者认为，Lisp的多样性是其优点之一，但同时也导致了方言之间的隔阂。文章建议，选择Lisp方言应基于个人对软件开发的理念。Scheme适合那些追求极简主义和学术风格的开发者；Common Lisp则为需要强大功能和丰富库的开发者而设计；Clojure为那些喜欢函数式编程、并发和JVM互操作性的开发者提供了选择；Racket则注重教育和可扩展性，适合初学者。此外，文章还推荐了一些Lisp相关的文章，并探讨了Lisp文化中可能存在的部落主义现象。作者还提到了Lisp的历史，并推荐了一些关于Lisp历史的论文。文章分别对Scheme、Common Lisp、Clojure和Racket进行了详细介绍，包括它们的特点、学习资源、社区以及一些有用的链接。最后，文章还列举了一些值得关注的Lisp方言，如Emacs Lisp、Jank、Hy等。

**要点总结**：

1.  Lisp语言家族庞大且多样，选择Lisp方言应基于个人对软件开发的理念。文章推荐了四种主要的Lisp方言：Scheme、Common Lisp、Clojure和Racket，分别适用于不同的编程需求和偏好。Scheme以其极简主义和学术性著称，Common Lisp则以其强大的功能和稳定性见长，Clojure在JVM平台上提供了函数式编程和并发的优势，而Racket则以其教育性和可扩展性而受到青睐。

2.  Scheme是一种极简主义的Lisp方言，适合作为教学语言和嵌入式扩展语言。Scheme以其小巧而强大的标准库、词法作用域、头等延续和尾调用优化而闻名。然而，Scheme的标准和实现非常复杂，存在多个标准（RnRS）、多个实现以及SRFI（Scheme Requests for Implementations），这使得Scheme的学习曲线较为陡峭。尽管如此，作者仍然鼓励新手选择一个实现并开始实践。

3.  Common Lisp是一种稳定且功能强大的Lisp方言，适合需要长期稳定性的项目。Common Lisp在1994年被ANSI标准化，并且保持了惊人的稳定性。尽管Common Lisp非常稳定，但这并不意味着它停滞不前。Common Lisp有许多实现，其中最著名的是Steel Bank Common Lisp (SBCL)，它以其速度、强大的调试器、分析工具和线程支持而闻名。

4.  Clojure是一种现代的Lisp方言，运行在JVM上，并鼓励函数式编程风格。Clojure的特点包括与Java生态系统的互操作性、不可变数据结构以及对并发编程的良好支持。Clojure的创建者Rich Hickey仍然积极参与语言的开发和社区的建设。Clojure还有一个名为ClojureScript的变体，它可以编译成JavaScript。

5.  Racket是一种Lisp方言，旨在用于教学和编程语言研究。作者提到Racket具有强大的宏系统，并且在东北大学的计算机科学课程中被广泛使用。Racket提供了丰富的学习资源和社区支持，包括书籍、视频和在线论坛。

## Full Content
Title: Church Of Turing - The Landscape of Lisp

URL Source: https://churchofturing.github.io/landscapeoflisp.html

Markdown Content:
_04/03/2025_

* * *

[Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language)) is a family of programming languages with a long, rich and oftentimes confusing tradition. Unware of it at the time, in 1960 John McCarthy published [a paper](https://www-formal.stanford.edu/jmc/recursive.pdf) that over the next 64 years would spawn a thousand dialects and a number of _very_ good ideas.

The fragmentation of the Lisp family from an outside perspective can seem really confusing to newcomers, like a software Tower of Babel. In fact the variety of Lisp is in my opinion one of it's best qualities. It almost guarantees that as long as you can overcome the (relatively) small barriers of the paren-heavy syntax and prefix notation that there will be a dialect and community that closely mirrors your philosophy on software development.

The purpose of this post isn't to convince the reader of how great Lisp is; rather, I assume the reader is already somewhat interested and is now trying to figure out which of these dialects is the best fit for them. It also isn't about "which Lisp is the best" type questions, but instead it's just my subjective view of the more prominent Lisp dialects. The most prominent dialects being Scheme, Common Lisp, Racket and Clojure.

Tl;dr:

*   If you want a minimalist, elegant Lisp with a strong academic foundation: choose Scheme.
*   If you want a powerful, batteries-included Lisp with a rich standard library and decades of history: choose Common Lisp.
*   If you want a modern Lisp with functional programming, concurrency, and JVM interop: choose Clojure.
*   If you want a beginner-friendly Lisp with great tooling and a focus on education and extensibility: choose Racket.

If the reader isn't already convinced but is still curious, I would recommend reading the following articles:

*   [Beating the Averages - Paul Graham](https://paulgraham.com/avg.html)
*   [Lisp: Good News, Bad News, How to Win Big - Richard P. Gabriel](https://dreamsongs.com/WIB.html)
*   [The Art of Lisp & Writing - Richard P. Gabriel](https://dreamsongs.com/ArtOfLisp.html)
*   [Programming Bottom-Up - Paul Graham](https://paulgraham.com/progbot.html)
*   [How To Become A Hacker - Eric Steven Raymond](http://www.catb.org/%7Eesr/faqs/hacker-howto.html)
*   [How Lisp Became God's Own Programming Language - Sinclair Target](https://twobithistory.org/2018/10/14/lisp.html)

Culture
-------

I mentioned earlier that Lisp's variety is one of it's best qualities, and I stand by that. A side effect of this however is that inter-dialect tribalism is unfortunately common. It's a weird reality that the smallest of differences seem to incite the most vitriol, whether it's with programming language dialects or [Northern Conservative Baptism.](https://www.youtube.com/watch?v=l3fAcxcxoZ8) As an example, of the four mentioned dialects I'll be talking about I've heard three of them being argued as not-actually-lisps. Can you guess which ones?

Not to leave on a sour note, Lisp also attracts some of the most thoughtful and intelligent people whose willingness to openly share their knowledge has changed me for the better.

History
-------

A quick aside. It can be hard to understand the design decisions made by Lisps without knowing at least a bit about their evolutionary history. Why do humans get goosebumps? Why is Emacs Lisp dynamically scoped? The best way of getting a sense of how Lisp has evolved is to reference the numerous papers written at various times.

This isn't at all necessary to picking up a Lisp by the way, I just think it's neat.

*   [Lisp 1.5 Programmer's Manual John McCarthy et al. (1962)](https://www.softwarepreservation.org/projects/LISP/book/LISP%201.5%20Programmers%20Manual.pdf)
*   [History of Lisp - John McCarthy (1979)](http://jmc.stanford.edu/articles/lisp/lisp.pdf)
*   [The Evolution of Lisp - Richard P. Gabriel, Guy L. Steele Jr (1993)](https://www.dreamsongs.com/Files/HOPL2-Uncut.pdf)
*   [The History of Lisp - Herbert Stoyan](https://www.softwarepreservation.org/projects/LISP/book/Stoyan-Geschichte.pdf)
*   [History Of Lisp - Paul McJones](https://www.softwarepreservation.org/projects/LISP/)
*   [Lisp History Resources - Paul McJones](https://www.softwarepreservation.org/projects/LISP/resource/)

Scheme
------

[Scheme](https://www.scheme.org/) is a minimalist Lisp [created at MIT](https://standards.scheme.org/official/r0rs.pdf) in the 70's by [Guy L. Steele Jr.](https://en.wikipedia.org/wiki/Guy_L._Steele_Jr.) and [Gerald Jay Sussman](https://en.wikipedia.org/wiki/Gerald_Jay_Sussman). It began as a series of [papers](https://research.scheme.org/lambda-papers/), then eventually a [report](https://dspace.mit.edu/bitstream/handle/1721.1/5794/AIM-349.pdf), and subsequently evolved as revisions to the report were made.

The minimalism of Scheme makes it well suited both as a teaching language and an embedded extension language in other programs. Scheme's minimalism also makes it attractive to Lisp implementers, and as a result there is a [rich ecosystem](http://community.schemewiki.org/?category-implementations) of Scheme [compilers and interpreters](https://get.scheme.org/).

I've quite the soft spot for Scheme - it was the first Lisp I learned via [SICP](https://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs), and the programs I've written and read tend to have an elegance that's hard to find elsewhere. There are few programming languages I would describe as beautiful but Scheme is definitely in that list (pun intended).

Scheme's notable for a few different reasons:

*   A minimalist design with a small but powerful standard library.
*   It was the first Lisp to choose lexical scoping as a default.
*   It supports first class continuations.
*   It facilitates functional programming by requiring implementations to support tail-call optimisation.
*   There are a _lot_ of Scheme implementations, each with their own tradeoffs and benefits.
*   It was the teaching language used by Ableson and Sussman in their classic "Structure and Interpretation of Computer Programs".

Despite the simplicity of Scheme itself, everything else around it can seem complicated and daunting at a first glance. The next few paragraphs are what I would consider essential context.

The 'Revisedⁿ Report on the Algorithmic Language Scheme', (typically abbreviated RⁿRS) is the de-facto Scheme language specification. As of now there is [1 original report](https://codeberg.org/scheme/r7rs/wiki#report-on-scheme-1975) and 7 revision documents. I suppose technically 8 revisions given the most recent revision has been split in two. The most commonly talked about [standards](https://standards.scheme.org/) are also the most recent: [R5RS (1998)](https://standards.scheme.org/official/r5rs.pdf), [R6RS (2007)](https://standards.scheme.org/official/r6rs.pdf), [R7RS-small (2013)](https://standards.scheme.org/official/r7rs.pdf) and [R7RS-large (ongoing)](https://codeberg.org/scheme/r7rs). As mentioned previously R7RS is divided into two parts: ["...a small language primarily for embedding, education, and research; and a large language to address the practical needs of mainstream software development."](https://r7rs.org/)

Now this is where things start to get a little hairy. R6RS was (or is) very controversial in the Scheme community for [various reasons](https://small.r7rs.org/wiki/SixRejection/3/) that I wont get into here, but to quote Gwen Weinholt's summary from their [post on the topic](https://weinholt.se/articles/r7rs-vs-r6rs/):

> R6RS is more demanding on implementers but easier on users. Conversely, R7RS is easier on implementers but more demanding on users.

This unsurprisingly resulted in more [implementations](https://get.scheme.org/) supporting R7RS than R6RS.

Another important thing to understand about Scheme are ["SRFIs" (Scheme Requests for Implementations)](https://srfi.schemers.org/). Due to Scheme's inherent minimalism and many implementations, coordinating library proposals became essential for writing portable code. There are a bunch of SRFIs and each Schemer will typically have a set of them they commonly use.

So between RnRS's, SRFIs and a smorgasbord of implementations we find ourselves in a weird position.

*   The language has _multiple_ standards.
*   The language has _many_ implementations.
*   The implementations can support _one or many_ standards.
*   The implementations can (and often do) _extend the language_ in non-standard ways.
*   The implementations can _choose what SRFIs_ to support.

Due to this complexity and [the challenges the R7RS-large](https://dpk.land/io/r7rswtf) working group have faced when reaching agreement, it's not unusual to see expressed the feeling that Scheme as a standard is dying. I'm not sure I fully believe this myself but only time will tell.

If you're new to Scheme don't let this discourage you for a second. The trick is to not think about it too much; it's perfectly fine to pick an implementation and just start having fun hacking.

One last thing - Scheme's minimalism makes it great for embedding as an extension language in other programs. See [Chibi-Scheme](https://github.com/ashinn/chibi-scheme) for an example of this.

Writings
--------

The writings and videos below are either explicitly about Scheme or incidentally use Scheme as a teaching tool.

Classics:

*   [The Lambda Papers - Guy L. Steele Jr. and Gerald Jay Sussman](https://research.scheme.org/lambda-papers/)
*   [Structure and Interpretation of Computer Programs (SICP) - Hal Abelson and Gerald Jay Sussman](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html)
    *   SICP isn't just a Scheme classic but an all time classic.
*   [The Little Schemer - Daniel P. Friedman and Matthias Felleisen](https://felleisen.org/matthias/BTLS-index.html)
*   [The Seasoned Schemer - Daniel P. Friedman and Matthias Felleisen](https://felleisen.org/matthias/BTSS-index.html)
*   [Software Design for Flexibility - Chris Hanson and Gerald Jay Sussman](https://mitpress.mit.edu/9780262045490/software-design-for-flexibility/)

There are a _lot_ of high quality Scheme learning resources online, many of them free too.

*   [Simply Scheme - Brian Harvey and Matthew Wright](https://people.eecs.berkeley.edu/~bh/ss-toc2.html)
*   [Scheme and the Art of Programming - George Springer and Daniel P. Friedman](https://www.amazon.co.uk/Scheme-Art-Programming-G-Springer/dp/0262192888)
*   [Teach Yourself Scheme in Fixnum Days - Dorai Sitaram](http://ds26gte.github.io/tyscheme/index.html)
*   [The Adventures of a Pythonista in Schemeland - Michele Simionato](https://www.artima.com/weblogs/viewpost.jsp?thread=251474)

Misc:

*   [The evolution of a Scheme programmer](https://erkin.party/blog/200715/evolution/)
*   [Learn X in Y where X=Chicken](https://learnxinyminutes.com/docs/chicken/)
*   [Community Scheme Wiki](http://community.schemewiki.org/)

Videos
------

*   [Growing a Language - Guy L. Steele Jr.](https://www.youtube.com/watch?v=_ahvzDzKdB0)
    *   Not necessarily about Scheme, but relevant in ways I hope are obvious.
*   [MIT 6.001 SICP (1986)](https://www.youtube.com/playlist?list=PLE18841CABEA24090)
    *   The classic 1986 SICP lecture series.
*   [Scheme: Feel the Cool - Andy Balaam](https://www.youtube.com/playlist?list=PLgyU3jNA6VjRMB-LXXR9ZWcU3-GCzJPm0)
*   [R7RS Large Status and Progress - Daphne Preston-Kendal](https://www.youtube.com/watch?v=BMvurzOj9ww)
    *   Daphne Preston-Kendal is the [chair of the R7RS working group 2](https://codeberg.org/scheme/r7rs/wiki). She's really good at communicating the state of R7RS, and being chair is a hard task but I'm glad she's doing it.
*   [The Most Beautiful Program Ever Written - William Byrd](https://www.youtube.com/watch?v=OyfBQmvr2Hc)
*   [Unlock Lisp / Scheme's magic: beginner to Scheme-in-Scheme in one hour - Christine Lemmer-Webber](https://www.youtube.com/watch?v=DDROSL-gGOo)
    *   A very fun introduction to Scheme for beginners.
*   [Programming Should Eat Itself - Nada Amin](https://www.youtube.com/watch?v=SrKj4hYic5A)
*   [Knit, Chisel, Hack: Building Programs in Guile Scheme - Andy Wingo](https://www.youtube.com/watch?v=uwiaT3MoDVs)

Scheme has a relatively small but [dedicated community](https://community.scheme.org/). If you're coming from a more popular language like JavaScript it might surprise you that discussions usually happen over days instead of minutes. This is perfectly normal.

*   [/r/scheme on Reddit](https://old.reddit.com/r/scheme/)
*   [comp.lang.scheme](https://comp.lang.scheme.narkive.com/)
    *   Pretty quiet these days and sometimes spammed, but contains a lot of interesting historic discussions.
*   IRC: #scheme (and #lisp) on [Libera.Chat](https://libera.chat/)
    *   There are various implementation specific channels on Libera too.
*   [Scheme Discord](https://discord.gg/ZcTYrdx)

Common Lisp
-----------

If Scheme is often seen as minimal and academic, Common Lisp in contrast could be considered robust and industrial. Their histories play a significant role in this perception and the history of Common Lisp is quite an interesting one - the curious reader can find out more about it [here](https://www.dreamsongs.com/Files/Hopl2.pdf). Summarising the best I can, in the early 80's Lisp was highly fragmented. ARPA weren't that interested in funding multiple projects with incompatible Lisp implementations, so they brought the kingdoms together and from this meeting grew the idea of a common Lisp to rule them all. To this day if someone directly refers to "Lisp" but not in the broad language-family sense, they're probably talking about Common Lisp.

Common Lisp (CL) was ANSI standardised in 1994 and since then has remained remarkably stable. If I needed to write a piece of software I knew wouldn't give me hassle in 30 years I'd choose Common Lisp. This level of stability is almost unthinkable to a great deal of software developers.

Something to note: just because CL is stable doesn't mean it's stagnant. There has been a great deal of effort spent on improving the many [Common Lisp implementations](https://lisp-lang.org/wiki/article/implementations), improving the library ecosystem, improving the tooling etc. If you're coming from a larger and faster moving ecosystem don't be surprised when you see libraries that were last updated 10 years ago. They're not dead, they're just sleeping - if you wake them up they'll work just as well as the day they were written.

I mentioned previously that Common Lisp has many implementations, but the most prominent of them is probably [Steel Bank Common Lisp (SBCL)](http://www.sbcl.org/). SBCL is great, and here's why:

*   It's [very fast](http://web.archive.org/web/20211018040529mp_/https://programming-language-benchmarks.vercel.app/lisp). All the [benchmarks](https://benchmarksgame-team.pages.debian.net/benchmarksgame/measurements/sbcl.html) I've seen blow similar dynamically typed and garbage collected languages out of the water.
*   It has a powerful and [highly interactive debugger](https://lispcookbook.github.io/cl-cookbook/debugging.html).
*   It comes with [sophisticated profiling tools](https://lispcookbook.github.io/cl-cookbook/performance.html#know-your-lisps-statistical-profiler).
*   It provides support for [threading.](https://lispcookbook.github.io/cl-cookbook/process.html)
*   It's [image based](https://old.reddit.com/r/lisp/comments/go3dzr/what_is_image_based_programming/frfg8dp/) (google it).

I'm not here to evangalise SBCL but it really is an awesome tool.

Something worth mentioning is programming style. Lisps in general are often described as being "functional" languages and this (especially historically) is a huge misconception. Common Lisp is incredibly unopinionated and leaves it entirely up to the programmer to choose how they want to use it. Want to write heavily procedural code? Great! More of a functional programmer? That's awesome too. Huge OOP fan? The Common Lisp Object System (CLOS) is one of the most sophisticated and robust out there.

Writings
--------

Despite not considering myself a Common Lisper, it's a fact that some of the most eye-opening books written about Lisp use Common Lisp as their mode of teaching.

*   [CLHS - Common Lisp Hyperspec](https://www.lispworks.com/documentation/HyperSpec/Front/Contents.htm)
    *   The language reference. You'll get familiar with this quick enough.
*   [CL Community Spec](https://cl-community-spec.github.io/pages/index.html)
    *   Like the hyperspec but nicer.
*   [Common Lisp Cookbook](https://lispcookbook.github.io/cl-cookbook/)
*   [Practical Common Lisp - Peter Seibel](https://gigamonkeys.com/book/)
    *   The quickest way to get up to speed with Common Lisp if you have previous programming experience.
*   [ANSI Common Lisp - Paul Graham](https://paulgraham.com/acl.html)
*   [Common Lisp Recipes - Edmund Weitz](https://weitz.de/cl-recipes/)
*   [On Lisp - Paul Graham](https://paulgraham.com/onlisp.html)
    *   _The_ book on advanced lisp techniques.
*   [Let Over Lambda - Doug Hoyte](https://letoverlambda.com/)
    *   Spiritual success to "On Lisp", contains deep and interesting macrology. For the advanced Lisper.
*   [The Art of the Metaobject Protocol - Gregor Kiczales](https://en.wikipedia.org/wiki/The_Art_of_the_Metaobject_Protocol)
    *   A deep dive into CLOS. Also not for the faint of heart.
*   [Common Lisp: A Gentle Introduction to Symbolic Computation - David S. Touretzky](https://www.cs.cmu.edu/~dst/LispBook/)
*   [Land of Lisp – Conrad Barski](http://landoflisp.com/)
*   [CLiki: The Common Lisp Wiki](https://www.cliki.net/)
*   [Paradigms of AI Programming - Peter Norvig](https://norvig.github.io/paip-lisp/#/)

Videos
------

*   [Little Bits of Lisp - Baggers](https://www.youtube.com/watch?v=m0TsdytmGhc&list=PL2VAYZE_4wRJi_vgpjsH75kMhN4KsuzR_)
*   [Common Lisp programming: from novice to effective developer - Vincent Dardel](https://www.udemy.com/course/common-lisp-programming/)
*   [Google Talk: Practical Common Lisp - Peter Seibel](https://www.youtube.com/watch?v=VeAdryYZ7ak)
*   [Growing a Language - Guy L. Steele Jr](https://www.youtube.com/watch?v=_ahvzDzKdB0)
    *   Not specifically about Common Lisp, but it's too good to not mention.
*   [Gavin Freeborn](https://www.youtube.com/@GavinFreeborn/videos)
    *   Great YouTube channel.
*   [Common Lisp Series - Neil Munro](https://www.youtube.com/watch?v=xyXDE5gP2QI&list=PLCpux10P7KDKPb4eI5b_qSnQaY1ePGKGK)
*   [Land of Lisp - The Music Video](https://www.youtube.com/watch?v=HM1Zb3xmvMc)
*   [BALISP playlist](https://www.youtube.com/playlist?list=PLoH3jteqsb2h-F5AHG4XVyZ6GwODX4uVB)

Common Lisp has a pretty small yet dedicated community. From what I've seen from an outside perspective, there's quite a few regional Common Lisp groups dotted around the world. A first step would be to see if there's any in your area.

*   [/r/Common\_Lisp](https://old.reddit.com/r/Common_Lisp/)
*   [CL Discord](https://discord.com/invite/hhk46CE)
*   [European Lisp Symposium](https://european-lisp-symposium.org/index.html)
*   [Toronto Lisp Users Group](https://torlisp.neocities.org/)
*   [Atlanta Functional Programming](https://www.youtube.com/@atlantafunctionalprogrammi6401/featured)
*   [comp.lang.lisp](https://groups.google.com/g/comp.lang.lisp)
    *   Mostly spammed to death these days, very interesting as an historical record. Reading through the archived posts and seeing 30 year old flame wars is always fun.
    *   If you're interested in the reputation comp.lang.lisp used to have, read this [19 year old blog post](https://eli.thegreenplace.net/2006/10/27/the-sad-state-of-the-lisp-user-community).
*   [IRC: #lisp, #commonlisp on Libera.Chat](https://libera.chat/)
*   [Awesome Common Lisp](https://github.com/CodyReichert/awesome-cl)

Clojure
-------

Clojure is the most recent of the language discussed so far, and since its appearance in 2007 has spawned a sort of mini-renaissance of renewed Lisp interest. It's also the Lisp I'm most fond of for my own personal projects.

Here's some points that set Clojure apart:

*   Runs on the JVM and can therefore interop with the Java ecosystem.
*   Encourages a functional programming style with immutable data structures.
*   Provides a variety of ergonomic, basic data structures: map, vectors, sets, lists.
*   The focus on immutable data structures and [software transactional memory](https://clojure.org/reference/refs) makes it very pleasant to use for writing concurrent software.
*   A comparatively healthy library ecosystem for writing web services.

Something else that sets Clojure apart is that its creator, Rich Hickey, is still heavily involved in the language and its community. This is in contrast to other Lisps which tend to be much more committee and community driven. In the Clojure community you'll see frequent reference to Rich's talks of which there's a good few. They're all worth watching in my opinion.

Oh, and there's also [ClojureScript](https://clojurescript.org/). It's Clojure that compiles to JavaScript - I haven't used it much but if that interests you, go for it.

Writings
--------

Clojure has quite a lot written about it. I'd typically just recommend looking around until you find a resource that matches your tastes.

*   [Practical Clojure - Luke VanderHart](https://www.amazon.co.uk/Practical-Clojure-Experts-Voice-Source/dp/1430272317)
    *   It's quite an early book having been published in 2010. It'll still be largely relevant but will miss some advanced features such as transducers, spec etc.
*   [Clojure from the Ground Up - Kyle Kingsbury](https://github.com/ligurio/clojure-from-the-ground-up)
*   [Elements of Clojure - Zachary Tellman](https://elementsofclojure.com/)
*   [Clojure for the Brave and True - Daniel Higginbotham](https://www.braveclojure.com/)
*   [Clojure Koans - Aaron Bedra et al](https://github.com/functional-koans/clojure-koans)
*   [Learn X in Y where X = Clojure](https://learnxinyminutes.com/clojure/)
*   [An Opinionated List of Excellent Clojure Learning Materials - Srihari Sriraman](https://gist.github.com/ssrihari/0bf159afb781eef7cc552a1a0b17786f)
*   [Awesome Clojure - Michał Buczko](https://github.com/mbuczko/awesome-clojure)
*   [A History of Clojure - Rich Hickey](https://clojure.org/about/history)
*   [ClojureDocs](https://clojuredocs.org/)

Videos
------

In my opinion, there's not a whole lot of really interesting Clojure talks other than the handful from Rich.

*   [Simple Made Easy - Rich Hickey](https://youtu.be/LKtk3HCgTa8)
*   [Clojure for Java Programmers Part 1 - Rich Hickey](https://www.youtube.com/watch?v=P76Vbsk_3J0)
*   [Clojure for Java Programmers Part 2 - Rich Hickey](https://www.youtube.com/watch?v=hb3rurFxrZ8)
*   [Rich Hickey Playlist](https://www.youtube.com/playlist?list=PLZdCLR02grLrEwKaZv-5QbUzK0zGKOOcr)
*   [Expert to Expert: Rich Hickey and Brian Beckman - Inside Clojure](https://www.youtube.com/watch?v=wASCH_gPnDw)
*   [Every Clojure Talk Ever - Alex Engelberg and Derek Slager](https://www.youtube.com/watch?v=jlPaby7suOc)
*   [Understanding Clojure's thread macros - Misophistful](https://www.youtube.com/watch?v=qxE5wDbt964)

I'd wager a guess that Clojure is the most popular of the Lisps out there, making it fairly easy to get into the community.

*   [/r/clojure](https://old.reddit.com/r/Clojure/)
*   [Clojure Discord (discljord)](https://discord.com/invite/discljord)
*   [Clojure Google Group](https://groups.google.com/g/clojure)
*   [Community Resources](https://clojure.org/community/resources)
*   [Clojure Forum](https://ask.clojure.org/)
*   [Clojurians Slack](http://clojurians.net/)

Racket
------

[Racket](https://en.wikipedia.org/wiki/Racket_(programming_language)) is an interesting one. It's a dialect of Scheme that began in the mid-90s and developed by PLT Inc (which was founded by [Matthias Felleisen](https://en.wikipedia.org/wiki/Matthias_Felleisen)). Its main goals were as a tool for teaching and as a playground for programming language research and development - to these ends it's by all means a great language. It's often said that Racket has one of the most powerful macro systems amongst the Lisps, and as proof more than a few postgrads have earned their PhDs using it.

Up [until very recently](https://huntnewsnu.com/82511/editorial/op-eds/op-ed-northeasterns-redesign-of-the-khoury-curriculum-abandons-the-fundamentals-of-computer-science/), Racket was a significant part of Northeastern University's "Fundamentals of Computer Science" cirriculum. This is now apparently being phased out in favour of another course that primarily used Python, to mixed [reception](https://old.reddit.com/r/Racket/comments/1hxt0q1/northeastern_abandoning_racket_in_favor_of_python/). I don't personally have an opinion, but it is interesting to note that this is effectively the same thing that happened to [MIT's introductory 6.001 course](https://www.wisdomandwonder.com/link/2110/why-mit-switched-from-scheme-to-python). I've another blog post brewing about Universities becoming trade schools, but that's for a different day.

Writings
--------

*   [How to Design Programs, Second Edition - Matthias Felleisen et al.](https://htdp.org/2024-11-6/Book/index.html)
    *   This book is often described as a more contemporary alternative to the Structure and Interpretation of Computer Programs. It's a good introduction to programming.
*   [Realm of Racket - Matthias Felleisen](https://nostarch.com/realmofracket.htm)
*   [Beautiful Racket - Matthew Butterick](https://beautifulracket.com/)
    *   Amazing, can't understate how good this is. A certified hood classic.
*   [The Racket Guide - Matthew Flatt et al.](https://docs.racket-lang.org/guide/index.html)
*   [Programming Languages: Application and Interpretation - Shriram Krishnamurthi](https://www.plai.org/)
    *   I haven't read this, at a glance it looks decent.

Videos
------

There's a very surprising amount of Racket talks - probably because it's a playground for programming language experimentation and people are excited to share what they've did. It's not something I've really dived into, so here's a few starting recommendations.

*   [Racket: A Programming-Language Programming Language - Robby Findler](https://www.youtube.com/watch?v=qqeteRf2GW8)
*   [Language-Oriented Programming with Racket - Matthias Felleisen](https://www.youtube.com/watch?v=z8Pz4bJV3Tk)
*   [Keynote presentation by Hal Abelson and Gerald Sussman at the fourteenth RacketCon](https://www.youtube.com/watch?v=_2qXIDO-cWw)
    *   I managed to catch the live stream, great gesture.
*   [The Racket Way - Matthew Flatt](https://www.infoq.com/presentations/Racket/)

*   [/r/Racket](https://old.reddit.com/r/Racket/)
*   [Discord](https://discordapp.com/invite/6Zq8sH5)
*   [IRC: #racket on Libera.Chat](https://libera.chat/)
*   [Racket Blog](https://blog.racket-lang.org/)

Honorable Mentions
------------------

There's a thousands different Lisps and I only really covered the big four. This feels a bit shallow, because it is.

Here's some Lisps that are worth giving a glance and might be right for you depending on your interests.

*   [Emacs Lisp](https://www.gnu.org/software/emacs/) - I'd rather not.
*   [Jank](https://jank-lang.org/) - Clojure freed from the JVM.
*   [Hy](https://hylang.org/) - Python embedded Lisp.
*   [LispFlavouredErlang](https://lfe.io/) - Love the BEAM but hate Erlang's prolog derived syntax? This is for you.
*   [Lisp in Small Pieces - Christian Queinnec](https://www.cambridge.org/core/books/lisp-in-small-pieces/66FD2BE3EDDDC68CA87D652C82CF849E) - Want to make your own Lisp?
*   [Fennel](https://fennel-lang.org/) - Lisp embedded in Lua
*   [Arc](https://paulgraham.com/arc.html) - You must really love HN.

Conclusion
----------

Oh, and to answer the question of which of the previously mentioned Lisps are argued as not-really-lisps:

*   Clojure, because no Cons cells.
*   Scheme, because [reasons](https://groups.google.com/g/comp.lang.lisp/c/Bj8Hx6mZEYI?pli=1).
*   Racket, because Scheme descendant, see above.

Bit silly in my opinion but it is what it is.

Updates
-------

*   05/03/2025 - Removed MAL from honourable mentions, replaced with Lisp in Small Pieces. Thanks [/u/kagevf](https://old.reddit.com/r/lisp/comments/1j3mcxe/the_landscape_of_lisp/mg2od7c/).
*   05/03/2025 - Added Norvig's PAIP to CL writings section. Thanks [/u/dmpk2k](https://old.reddit.com/r/lisp/comments/1j3mcxe/the_landscape_of_lisp/mg4l3na/)

