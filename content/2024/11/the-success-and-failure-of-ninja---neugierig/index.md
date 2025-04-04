---
title: The Success and Failure of Ninja - neugierig
date: 2024-11-30
extra:
  source: https://neugierig.org/software/blog/2020/05/ninja.html
  original_title: The Success and Failure of Ninja - neugierig
---
## Summary
**摘要**：
九年前，我发布了一个名为 Ninja 的构建系统，其功能与 Make 相似。尽管我最初对分享这个副项目有些尴尬，但 Ninja 后来变得非常流行。若非详尽列举所有用户，一些大型项目使用了 Ninja，例如：
- Chrome，最终移除了所有非-Ninja 构建；
- Android，使用了它的一部分系统，但具体部分我并未完全了解；
- 所有 Meson 项目的使用，这些似乎是自由软件领域的首选构建系统；
- 许多使用 Ninja 和 CMake 的项目，例如 Swift 语言的构建指南指出，要安装 Ninja。Ninja 被视为我最成功的开源项目，无论按照何种衡量标准。我在 2011 年发布 Ninja，2014 年移交了所有权，并在后来被转交给第三位维护者。回顾这段经历，我学到了不少：
- 技术问题往往以解决代码问题为主，但实质上或多或少与之无关。初、高级工程师的转型之路对此有着深刻的阐述。
- 技术：
  - Ninja 的主要功能很简单，由合格的系统课程大学生也能凭直觉构建类似系统。它接受一个包含所有命令、文件消耗和产生的`ninja.build`文件，检查文件的修改时间，并并行执行必要的命令更新。
  - 技术侧重于优化速度，采用各种精心设计但小规模的优化。Ninja 导入文件路径到一个唯一的内存对象，用于进行路径相等性测试（类似内建字符串）。
- 架构设计：
  - Ninja 使用二部图来表示构建结构，文件节点与命令节点之间互相引用。这种表示清晰地勾勒了构建的结构，其中任意命令的输入改变都将导致其更新所有输出。
- CMake 集成：
  - Ninja 与 CMake 的集成主要由 Peter Collingbourne 完成，Peter 对使 Ninja 成功于现实世界中贡献了主要力量，尽管我在支持这一整合中表现不佳。
- Windows 支持：
  - 悉心提供了 Windows 版本，当时推动该项目的Google 产品（Chrome）需要 Windows 社区的用户群支持。Windows 是开发者的主要平台之一，在这里，一个项目一旦能得到 Windows 开发者的使用，总会吸引大量的关注。
- 相关工作：
  - 在构建系统领域中，Ninja 的设计并非建立在深厚的研究基础上。论文“Build Systems à la Carte”讨论了增量计算问题，尽管它发布时间早于 Ninja。

**要点总结**：
1. **技术背景**：
   - Ninja 的功能有限，但足够高效，重点在于速度而不是工具集的丰富性，适用于大规模项目（如 >100k 输入文件）。
   - 使用二部图表示构建过程，使指挥命令更新的逻辑得以清晰呈现，文件和命令节点间相互关联。
2. **设计决策**：
   - Ninja 设计特色如文件路径的**唯一内存对象映射**和路径相等地检测（类似内建字符串），以优化执行速度。
3. **CMake 集成贡献**：
   - Ninja 与 CMake 的集成大部分由 Peter Collingbourne 完成，成为了 Ninja 成功的关键一步。
4. **Windows 支持的背景**：
   - Ninja 得以支持 Windows 的原因在于它为开发者社区提供了周到的工具，尤其是对于那些渴求工具但往往选择付费软件的 Windows 开发者群。
5. **开源维护者的心路历程**：
   - 作为一名开源维护者，作者体验了一种复杂情感交织的经历，包括骄傲、失望、挫败和对理想社区的期待，同时也反思了作为开源项目的创作动机的变化。
## Full Content
Title: The Success and Failure of Ninja

URL Source: https://neugierig.org/software/blog/2020/05/ninja.html

Markdown Content:
Around nine years ago I published Ninja, a build system that is mostly comparable to Make. At the time [I was a bit embarrassed to share my side project](https://neugierig.org/software/chromium/notes/2011/02/ninja.html) but since then it has become widely popular.

I can't list all of the users off the top of my head anymore, but some of the "big" projects that use Ninja include:

*   Chrome, which eventually removed all of its non-Ninja builds;
*   Android, which uses it for some large component of the system that I've never quite understood;
*   all [Meson](https://mesonbuild.com/) projects, which appears to increasingly be the build system used in the free software world;
*   many other projects that that use Ninja with CMake (for one random example, the [build instructions for the Swift programming language](https://github.com/apple/swift#system-requirements) tell you to install Ninja).

Ninja has been by far my most successful open source project, depending on how you quantify success. (Other projects of mine like Chrome have more users, but I was responsible for only parts of Chrome; Ninja also has had important contributions by collaborators but it feels more like "mine".) I released Ninja in 2011, gave ownership of the Ninja project away in 2014, and it has since been passed on again to a third maintainer, so now that my part in the story is pretty much over I here would like to reflect on what I learned.

If I were to summarize what I learned in a single sentence, it would be this: we talk about programming like it is about writing code, but the code ends up being less important than the architecture, and the architecture ends up being less important than social issues.

That is, as programmers we like to talk about problems as if they are primarily technical — "how do I optimize this loop to squeeze more qps out of this service?" — when in my experience the tech almost always ends up secondary to bigger picture factors. I have since seen that same observation in other words stated by many others as describing the journey from a "junior" to "senior" engineer which also rings very true against my career, so I also hope in this retrospective to give some insight into what that means.

The tech
--------

Let's start by getting some technical details out of the way.

What Ninja specifically does is pretty simple; given a description of the requirements, I'd expect a competent undergrad, perhaps in a systems course, to be able to bang out a basic version of it without much help. To summarize, the user gives Ninja a `ninja.build` file which (omitting some details) contains all the commands you'd like Ninja to run, along with which files each command consumes and produces. Ninja loads this file, checks the modification timestamps of the various files, and executes in parallel the commands needed to bring everything up to date. As compared to Make (which does pretty much the same thing) Ninja provides _fewer_ features in its input build language, and is primarily structured around making the few things it does very fast.

The few things Ninja does are: (1) parse and interpret that build file; (2) check the modification times of its inputs; (3) execute the needed commands. The goal is to get to step 3 as fast as possible even on huge (\>100k input files) projects, and doing so is a collection of careful but small optimizations. For one small example, Ninja is careful to map each input file path to a unique in-memory object as early as possible, and then on it uses pointer comparisons between those objects for testing path equality (interned strings, effectively). I wrote a chapter for the book "The Performance of Open Source Software" about Ninja that tells some of the stories of the lower level technical details of making that fast which [you can read online](https://www.aosabook.org/en/posa/ninja.html).

Many people have done rewrites of Ninja over the years. It's a small enough project that it's fun to try implementing in your favorite language. For some examples, [llbuild](https://github.com/apple/swift-llbuild) and [Shake](https://shakebuild.com/) both support Ninja files as inputs, and [samurai](https://github.com/michaelforney/samurai) is a nearly file-by-file reimplementation (with less code, but with fewer features and no tests(!)). Ninja is pretty easy to implement for the fun 20% of it and the remaining 80% is "just" some fiddly details. To my knowledge nobody has ever made a faster implementation.

Some architecture notes
-----------------------

Some pieces of Ninja took struggle to get to and then are obvious in retrospect. I think this is true of much of math, that once you have distilled the ideas to their essence they seem obvious. The power comes from having the right way of thinking about the problem. I mostly stumbled through Ninja's design but once I was on the other side of it I came to see I accidentally hit some good points in the design space. Here are a few examples.

**The graph representation**. Make doesn't well handle the case when build rules produce multiple files. I don't know how Make is structured internally, but I would guess that it represents the build structure as a graph between files since that is what the input syntax looks like and that structure would generate that behavior. Ninja instead uses a bipartite graph between files and commands, where file nodes are edges into command nodes which have edges back out to files. This representation better captures the structure of builds: the command is out of date if any of its inputs change, and it updates all its outputs when it runs. (The one graph invariant is that a given file may have at most one input edge.) For another consequence of this, note that the command line itself can be thought of as an input to command nodes, in that the command is out of date (and consequently so are its outputs) if the command-line flags change.

**The deps log**. To get C header dependencies right you need to consume additional dependency data produced by the C compiler. It's described more in [the book chapter](https://www.aosabook.org/en/posa/ninja.html). I recall struggling with whether to bring in a database and how to reconcile that with my aspirations of simplicity until I finally hit upon a [representation format](https://github.com/ninja-build/ninja/blob/master/src/deps_log.h#L29) that ended up pretty tight. (It's unfortunately still wrong in some important ways but oh well.)

**End-to-end / crash-only**. Ninja is not a persistent daemon process but instead does all its work from scratch on each execution. This is intentional and a mixture of the insights of [the end-to-end principle](https://en.wikipedia.org/wiki/End-to-end_principle) and [crash only software](https://en.wikipedia.org/wiki/Crash-only_software), which is to say: given that you need to run Ninja from scratch sometimes, if you make that fast, then you don't need to build a second "online" codepath. Projects that can stay memory-resident tend to eventually let their startup performance languish.

**File status**. The reason programmers sometimes expect build tools to be memory resident is so they can cache status about files on disk. But in practice, the kernel is already caching this information in memory and caching it again in userland doesn't save you much; fetching file status from Linux is extremely fast. Ninja does it all from a single thread even. On a machine that was "fast" ten years ago you can [stat 30k files in 10s of milliseconds](https://github.com/ninja-build/ninja/wiki/Timing-Numbers). (A programming joke: half of performance problems are fixed by introducing a cache; the other half are fixed by removing one.)

**Orders of magnitude**. A rule of thumb is that you can get scale by 2x with optimization, but to scale by 10x you need to rearchitecture. Ninja was designed around Chrome's build which at the time had around 30k build steps. These days it's used in much smaller settings where it's likely not needed (see below discussion on speed) and in larger settings like the Android build where it is failing to scale and will likely need an alternative approach.

**Underspecifying and overspecifying**. Ninja executes commands in parallel, so it requires the user to provide enough information to get that correct. But at the other extreme, it also doesn't mandate that it has a complete picture of the build. You can see one discussion of this dynamic [in this bug in particular](https://github.com/ninja-build/ninja/issues/1303) (search for "evmar" to see my comments). You must often compromise between correctness and convenience or performance and you should be intentional when you choose a point along that continuum. I find some programmers are inflexible when considering this dynamic, where it's somehow obvious that one of those concerns dominates, but in my experience the interplay is pretty subtle; for example, a tool that trades off correctness for convenience might overall produce a more correct ecosystem than a more correct but less convenient alternative, if programmers end up avoiding the latter. (That could be [one reason Haskell isn't more successful](https://neugierig.org/software/blog/2011/10/why-not-haskell.html). Now that I work in programming languages I see this dynamic play out regularly.)

And finally, the biggest architectural insight is:

The 'assembler' metaphor
------------------------

When people think of build systems they think of a broad range of features, so broad that often the way build systems talk about themselves sometimes aren't even comparable across different tools. The marketing text for these tools often talks about how user-friendly the input syntax is.

Ninja's insight (discovered in retrospect) is that all of these tools, no matter the high-level features, ultimately eventually must construct some sort of graph of the _actions_: the files they intend to keep up to date and which commands to execute. Ninja only implements that action graph and leaves it to the user to choose another "generator" program on top.

I originally invented this two program split just because it neatly fit into the project (Chrome) I was working on at the time, but I have since come to see it as Ninja's primary contribution.

On one side, it allowed me to make Ninja stupid but quick, because anything costly (such as "glob for \*.c") is forced into the generator. Compared to other build systems that do all the work in one pass, Ninja's design effectively forces you to "snapshot" the action graph to disk once you've computed it. Another way to look at this is that it effectively has you cache the action graph across builds.

On the other side, it also meant Ninja was useful in very flexible ways, because the generator could be as high level as the user wanted ("tests are found by globbing the entire source tree for files with 'test' in their name"). Importantly, it forced the developer who used Ninja to decide what they were going to pay for. If their generator program wanted to glob all over the disk looking for files, it was welcome to, but then it would be more obvious to them why their builds were slow.

(I should note here that a clean separation between a generator and the resulting action graph is not as easy as I make it out to be. Ninja ultimately has a lot of fiddly details that are all struggling around which layer the work belongs in, but it's hard to write up the lessons learned.)

The irony of this aspect of Ninja's design is that there is nothing preventing anyone else from doing this. Xcode or Visual Studio's build systems (for example) could just as well do the same thing: do a bunch of work up front, then snapshot the result for quick reexecution. I think the reason so few succeed at this is that it's just too tempting to mix the layers.

Ninja's closest relative is Make, which attempts to encompass all of this programmer-facing functionality (with globbing, variable expansions, substringing, functions, etc.) that resulted in a programming language that was too weak to express all the needed features (witness autotools) but still strong enough to let people write slow Makefiles. This is vaguely [Greenspun's tenth rule](https://en.wikipedia.org/wiki/Greenspun%27s_tenth_rule), which I strongly attempted to avoid in Ninja.

Defaults dominate
-----------------

By default, Ninja executes the desired commands in parallel. Make is capable of this too; Ninja borrows the same flag name for this capability (`-j`) and just uses a different default value. However, because Make defaulted to running commands serially, it is relatively easy to write a Makefile that underspecifies dependencies such that it is unsafe to execute it in parallel. In fact, there's even some commercial vendor that offers some sort of "Makefile accelerator" tool that helps people discover and repair underspecified dependencies.

In contrast, because Ninja always executes commands in parallel (even on a single-core system) it ends up revealing mistakes like these earlier. This means that programs that build with Ninja typically end up safe to build in parallel. (Ninja has no fancy system for detecting when you've gotten things wrong, it just causes wrong builds more often.) In contrast, users often forget or are unaware of the flag to Make that makes it also run in parallel. It is embarrassing to take credit for this because it's just a flag, but just because of its default value, Ninja in practice will end up being "twice as fast as Make" or more for users who aren't careful. The lesson is that all the optimization in the world doesn't matter if your users don't actually see it.

Speed
-----

In this post I have talked about performance a few times, and it's important to note that there are lots of different kinds of performance metrics to care about in a build system. For example, one might care "how long does the build take when I start from scratch?" Ninja was solely focused on the edit-compile cycle of _incremental_ builds in large codebases, which is to say you've run a build, you've edited one file, and you run the next build.

When I wrote Ninja, I had a memory of blaze (aka [bazel](https://bazel.build/)) being very fast, but it had been years since I had last used it. Because of this memory, I kept trying to make Ninja even faster, to try to catch up with my memory of blaze. Ironically it turns out blaze is not particularly fast on the speed metric I cared about; because blaze is a Java program, even having blaze print its "help" output is pretty slow.

It is maybe silly of me to fixate on incremental builds, but I strongly believe that iteration time has a huge impact on programmer satisfaction, and Ninja is used exactly in the edit-compile loop where the difference of 1 second and 4 seconds is critical. I think I am personally more latency-sensitive than the average programmer, but I also believe that programmers _feel_ latency and it affects their mood even if they don't notice it. (Google has recently done some research in this area that kinda confirmed my belief, here's hoping they'll publish it publicly!)

It is very difficult to communicate to users the many possible meanings of "fast". The Ninja manual tries to warn people away from using it on small programs. Literally the [second paragraph after the introduction](https://ninja-build.org/manual.html#_using_ninja_for_your_project) says "If your project is small, Ninja's speed impact is likely unnoticeable" and recommends using a different build system. Unfortunately "fast" sells, and the Ninja list often had users trying to use it for their miniature apps and getting frustrated by its lack of features.

Though Ninja focused on incremental rebuild performance, some users reported that Ninja improved their end-to-end build performance too. This was unintentional, but is because Ninja (again by virtue of doing nearly nothing) consumes very little CPU while running those builds, while comparable programs for whatever reason consume more CPU while running and that takes CPU away from the underlying build.

In my post ["What does it mean for a browser to be fast"](https://neugierig.org/software/chromium/notes/2010/05/fast.html) I go into how there are many aspects to speed, and that ultimately what's important is the user's _perception_ of speed. Ninja is very terse in its output: for most successful builds, it prints a single line. In contrast, other build systems tend to print a bunch of (often gratuitously colored) output with timing numbers about the various stages of the build it's going through, which makes them feel heavy. Ninja, by virtue of saying little, makes it feel even more like it's not there.

CMake
-----

I originally built Ninja to work with Chrome's wacky one-off build system and left it at that. Somehow a kind stranger named Peter Collingbourne found Ninja and did the work to plug it into the much more popular CMake build system. Ninja's design fits well into CMake, but there were (as always) a lot of details to work out and Peter did most of this, initially to use Ninja to work on LLVM. This was more than just CMake, but also required building new semantics into Ninja. If anyone is responsible for making Ninja succeed out there in the real world, Peter is due the credit.

The CMake authors eventually took over this integration and I feel bad about how poorly I supported them; they were very kind and patient with me but I never really had the time to answer their requests or concerns. Brad, if you read this, I am very sorry! To this day I've never actually used CMake and I never could find the time to worry about it.

Windows
-------

Because the motivating project for Ninja was Chrome and Chrome targets Windows too, we got it working on Windows. (This was another part of Ninja that was primarily written by [a contributor](http://h4ck3r.net/).)

At a technical level, supporting Windows is mostly a big hassle. In the places where the Linux code doesn't work as is, it requires either uninteresting abstractions or major redesigns. For an example of the former, spawning processes and capturing their output is very different between the platforms, but mostly in that you need to learn a totally different API. For an example of the latter, Ninja's design centrally relies on the property that you can get a kernel-cached file's last modification time quickly, and that is [just not true on Windows](https://github.com/ninja-build/ninja/wiki/Timing-Numbers).

But Windows is still a huge platform in terms of developers, and those developers are starved for tools. The underlying dynamic is that when someone makes a neat tool for Linux, the impulse is to share it, but when they do so for Windows, the impulse is to sell it, and so because of that there aren't as many tools freely available on Windows.

It was a surprise to me how many of the early Ninja users were Windows users, but in retrospect it is kind of obvious: even if only one in a hundred Windows developers cared about Ninja, there are so many people on Windows that they would eventually show up. (Sometimes in the Linux Chrome early days we talked about it this way: even if we got ~all desktop Linux users using Chrome, in terms of total humans that's only like getting an additional 5% of Windows users. You can disagree with the specific value of that number but hopefully you get my point.)

Related work
------------

I mentioned that I stumbled through Ninja's design. I regret not spending more time researching before building, but I intended the whole project as just a weekend demo hack, not a serious thing. (Relatedly, please forgive me for the embarrassing name.) Since then I have come to appreciate how important it is to actually understand the design space when building a thing. I now find myself noticing how rare it is for programmers to discuss related work and it now drives me mad.

The term I used above ("action graph") is not how I thought about it in Ninja, but is instead taken from Google's build system ("blaze"/"bazel"). In bazel, they explicitly talk about how there's a graph of targets (higher-level user concepts like "library" and "binary") and how that generates a [graph of actions (commands)](https://docs.bazel.build/versions/master/bazel-overview.html#how-does-bazel-work).

I wrote above a bit about how the command-line text can be viewed as an 'input' to commands in the same way that files are. This is a specific instance of the broader concept of incremental computation, which covers not only build systems but also incrementality in UI. My friend [Rado](https://twitter.com/radokirov) has been reading the research in this area for the past year or so(!) and is working on a series of blog posts that attempt to summarize it; watch for it. The Jane Street blog has had [some work on summarizing this area too](https://blog.janestreet.com/introducing-incremental/); as you can see there, there's even a connection to our recent renaissance in UI construction as found in React.

The fantastic paper ["Build Systems à la Carte"](https://www.microsoft.com/en-us/research/uploads/prod/2018/03/build-systems-final.pdf) discusses incremental computation in the context of build systems. I wish this paper had existed before I wrote Ninja.

Open source
-----------

I'd like to wrap this up by talking a bit about being an open source maintainer. As you might have read elsewhere, it ends up not being especially fun. ([This talk "The Hard Parts of Open Source"](https://www.youtube.com/watch?v=o_4EX4dPppA) is worth your time.)

When I try to take stock of my overall feelings about the project, it is a mixture of the occasional pride when I see someone on proggit or HN say something nice about it and a larger overall sense of disappointment.

I made this thing that I thought was cool and I gave it away, and what I got back were occasionally friendly people who nicely requested things from me, but more often angry users who demanded things of me, and rarely anyone saying thanks. People repeatedly threatened to fork the project when I didn't agree to their demands, never once considering the possibility that I had more context on the design space than they did.

A different source of sadness were the friendly and intelligent people who made reasonable-seeming contributions that conflicted with my design goals, where I wanted to repay their effort with a thorough explanation about why I was turning them down, and doing that was itself exhausting.

I got into programming via free software, and I wrote code with the desire to give back to the people who gave me so much. (If you are reading this post then I predict you are benefiting from one or more one of my free software contributions.) But today I see that free software is not really about sharing between equals anymore; people instead think of themselves as customers and treat authors as if they can go complain to the manager.

Another way of saying this is that today I am motivated by just trying to impress or live up to the ~ten hackers that I admire, people like apenwarr or agl or bradfitz or graydon, and while it's occasionally cool to meet someone and have the reputation of my software precede me, I think a lot of "succeeding" was mostly just kind of a burden. I think I could have learned about as much with a much smaller fraction of the success.

Final acknowledgements
----------------------

I mentioned a few people already in this post, but I'd like to also specifically thank Nico Weber, both for being a careful collaborator and for taking on maintainership of Ninja for years, and also Jan Niklas Hasse, who took over after Nico and whom I don't know at all but who seems to be doing a fine job. And finally, thanks to the many other [authors of Ninja](https://github.com/ninja-build/ninja/graphs/contributors).

