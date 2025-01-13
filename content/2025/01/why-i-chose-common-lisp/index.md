---
title: Why I Chose Common Lisp
date: 2025-01-13
extra:
  source: https://blog.djhaskin.com/blog/why-i-chose-common-lisp/
  original_title: Why I Chose Common Lisp
---
## Summary
**摘要**：
原作者Dan在他的文章《为什么我选择了Common Lisp——Dan的思考》中，详细阐述了他从Clojure转而选择Common Lisp的原因与经历。核心可总结为一系列转而采用新的LISP语言的驱动因素。在转投Common Lisp之前，Dan面临了Clojure中的多个挑战，如启动时间过长，社区对于这一问题的重视度不足，以及在实现快速原生执行文件时遇到的技术难度。这篇文章逻辑条理清晰，层层推进，阐述了每个标准要求以及是如何满足或超越自身过去的选择。

**要点总结**：
1. **满足快速启动需求的工具链**：
   - Common Lisp具备简洁且可行的方法来生成广泛应用程序的快速启动和独立执行文件，解决了启动时间太长的问题。

2. **跨平台兼容性**：
   - 包括Windows、Mac和Linux在内的多操作系统环境下的广泛支持，满足了Dan对于持久服务和跨平台应用开发的需求。

3. **连接到更大的声明式生态系统**：
   - Basic Foreign Function Interface (CFFI)的使用，使得它能够很好地与其他语言（如C）互动，特别是在发展基于大型社区的特定功能时。

4. **高性能运行时环境**：
   - SBCL作为最受欢迎的实现，提供了令人印象深刻的快速性能，满足Dan对执行效率的高要求。

5. **丰富的多线程支持**：
   - 通过Bordeaux-Threads、lparallel、cl-async和blackbird等多个库的支持，Common Lisp提供了强大的多线程能力，使得并发编程成为可能。

**摘录**主要内容依据逻辑顺序展开如下：

1. **与前一个项目Clojure的道别**：
   - 初期调用主要对Clojure启动费时的不满，以及后续尝试通过使用native-image方法加速启动，但最终仍未能实现快速的独立可执行文件，这一问题被认定为亲密编程语言的必要要求。在此背景下，Dan决定舍弃Clojure。

2. **转而探索新LISP语言的动机**：
   - 认出Clojure的欠缺后，Dan开始寻找新的LISP语言，列出了一系列所需特点，涵盖生成快速启动的可执行文件、兼容Vim和Emacs、支持多种操作系统、与广泛社区和生态系统相互融合，以及快速且高效运行的能力。

3. **Common Lisp的提出和使用**：
   - 经过Francky Pierret的链接介绍，以及自身对CLtLv2工具的学习和HyperSpec的深入阅读，Dan最终决定采用Common Lisp，特别是在了解其多编译器、快启动、以及社区活跃度后。

4. **探索Common Lisp的好奇心**：
   - 提供诸如JSON解析、SQLite支持、HTTP请求和功能性数据结构等实用功能的广泛库，以适应创建CLI工具的常见任务需求。同时，Dan提到在事件处理、/web开发、独立运行脚本、自动化和其他专有项目中使用的个案研究，阐明其使用范围和灵活性。

5. **喜悦和技术上的回报**：
   - 强烈的社区、活跃的用户、网络资源和其他社区提供的CLU和CL孤立模块，为开发者提供解决特定问题和挑战的途径。通过实践和应用，用户体验到了技术挑战被满足的喜悦，并在此过程期间，发现了关于标准、工具、技术和实践的独特见解。

**参考资料**：
- Clojure: [https://clojure.org/](https://clojure.org/)
- CLI: [https://github.com/djha-skin/degasolv](https://github.com/djha-skin/degasolv)
## Full Content
Title: Why I Chose Common Lisp — Dan's Musings

URL Source: https://blog.djhaskin.com/blog/why-i-chose-common-lisp/

Markdown Content:
Goodbye, Clojure
----------------

After ~7 years, I was _done_ with [Clojure](https://clojure.org/). I was writing a some [CLI](https://github.com/djha-skin/degasolv) [apps](https://github.com/djha-skin/zic), and I _hated_ how long they took to start up. The community at large seemed not to care about this problem, except for the [babashka](https://github.com/babashka/babashka) folks. However, I spent long, hard hours banging my head against [native-image](https://www.graalvm.org/latest/reference-manual/native-image/) and it just wasn't working out. It was incredibly painful, and at the end of it, I still didn't have standalone, fast-starting native executables. I decided that that was a requirement for my main driving hobby language, and that Clojure didn't have it. It was then that I decided to move on from Clojure.

On the Hunt for a New Lisp
--------------------------

I started shopping around for a new lisp to use after hours like I'd done before with my home projects. I had specific requirements in mind, though I didn't actually list them when I started. I can list them now in hindsight, though:

1.  It must be easy to create standalone, fast-starting executables using a reasonable toolchain (to address my main concern with Clojure)
2.  [I can't use Emacs](https://blog.djhaskin.com/blog/emacs-users-im-okay-i-promise/), so it's got to be usable in Vim.
3.  It must have good support for Windows and Mac, in addition just Linux/POSIX operating systems.
4.  It would be nice if it allows plugging into some other, large-community imperative language, like Clojure does with Java.
5.  It must have a reasonably fast runtime -- hopefully as good or better as Clojure's.
6.  The language must have a strong multithreading story. It would be grand if whatever language it was didn't have a [GIL](https://en.wikipedia.org/wiki/Global_interpreter_lock), for example.
7.  Must have a strong community.
8.  Must have a good ecosystem, with at least the following libraries well-implemented, thus supporting my common use cases of making CLI tools:
    1.  JSON parsing and serialization
    2.  Sqlite3 support
    3.  HTTP requests library
    4.  Would be nice if it had functional data structures like Clojure's (this ended up being less of an issue later)

I looked at [Scheme](https://www.scheme.org/), but that community seemed to still be fractured over the [r6rs](https://elmord.org/blog/?entry=20171001-r6rs-r7rs)/[r7rs](https://groups.google.com/g/scheme-reports-wg2/c/xGd0_eeKmGI/m/q-xM5fbuAQAJ?pli=1) mess. Also, there wasn't [a big enough ecosystem](https://akkuscm.org/packages/) to suit my liking.

I'd already tried [Racket](https://racket-lang.org/) in school and didn't like it. The runtime was a bit slow and bloated for my tastes.

I had seen [lisp-lang.org](https://lisp-lang.org/) shared on [the Orange Site](https://news.ycombinator.com/item?id=28725958). I was impressed with the site. I came back to it later after I first saw it and thought, why not. Maybe I'll give Common Lisp a shot.

Magic Happens Here
------------------

I will spare the reader the full narrative of my learning CL. It was a rough ride learning the language. (I went about it the wrong way, getting [CLtLv2](https://www.amazon.com/Common-LISP-Language-Second-Steele/dp/1555580416/ref=sr_1_1?crid=2W8Y093RT5UQN&dib=eyJ2IjoiMSJ9.ZDcuOzchQwO4txmVOLrlDRGU3K0TMYMsM0OMVdMocZUW_Wj2K3YYFfB8bATRFvKaR-Vz-P1ai5hpSAzE1q6Ii1FwQK7zu1d8vn3qa88EQCipfnbJoYsHbiNQKbl8NJBhuhZu410r8KXjyJNjG_gvC7r9TX_PSp6VDNLcalMgo4g9xI7m52SnG1BOdFxZ44tmKdn97DKpv0Oqw9ngYg_dDm5_6MUuPan0hPrbrMKcp58.H5QKWhJtzda3Xl9dXb_siYXClmIBIseqGTy3IKAkN-0&dib_tag=se&keywords=common+lisp+the+language&qid=1736648071&sprefix=common+lisp+the+language+%2Caps%2C146&sr=8-1) for Christmas and reading through that. I eventually found the [HyperSpec](https://clhs.lisp.se/) and started reading that as well.)

There were some weird things I didn't expect to find about CL. It's a _standardized_ language, more like C than Java that way. There are many compilers, interpreters, and runtimes that implement that standard. There's even [a tool to help install them all and wrangle them](https://github.com/roswell/roswell). The most popular one [according to the community](https://blog.djhaskin.com/blog/common-lisp-community-survey-2024-results/) is [SBCL](https://www.sbcl.org/).

If I had heard about [Janet](https://janet-lang.org/) when starting this hunt, I might have stopped there and not gone on to CL. Nice syntax, small, fast executables, [C FFI](https://janet-lang.org/docs/ffi.html), [a fun intro book](https://janet.guide/). It checks all my boxes.

However, I'm glad I did learn CL first, because I think I'd miss the [CLOS](https://en.wikipedia.org/wiki/Common_Lisp_Object_System) and the Conditions System, things I learned about later in my journey. Common Lisp is just a bit of a stronger language.

Requirements Met
----------------

I found answers to all my questions, and decided my next lisp was going to be Common Lisp. I've been coding in it ever since. Here are the things I found:

1.  **Standalone Executables**: there are lots of ways to do this in Common Lisp. I summarize my favorite way in [another blog post](https://blog.djhaskin.com/blog/release-common-lisp-on-your-first-day/). Start up times range from a fraction of a second to nearly instant, depending on if you compile the executable with compression or not. This is not a bolt-on feature; it's a first-class-citizen way to distribute Lisp programs.
2.  **Vim Workflow**: There are a lot of good ones here, but I eventually settled into [a Vim workflow of my own](https://blog.djhaskin.com/blog/developing-common-lisp-using-vim-with-tmux-or-conemu/). Readers may also be interested to know that [I found VS Code perfectly usable](https://blog.djhaskin.com/blog/experience-report-using-vs-code-alive-to-write-common-lisp/) as a Common Lisp IDE.
3.  **Windows/Mac/Linux Support**: SBCL, a popular implementation and compiler for Common Lisp, supports The Big Three relatively well, as outlined in the blog post linked in point #1.
4.  **Larger Imperative Ecosystem**: Most implementations actually hook into the C programming language pretty well through the [CFFI](http://common-lisp.net/project/cffi). That works for me.
5.  **Runtime Speed**: SBCL is [crazy fast](https://github.com/niklas-heer/speed-comparison).
6.  **Multithreading**: While the Common Lisp standard does not make provisions for multithreading, all major implementations do support it and their differences are papered over with a library called [Bordeaux-Threads](https://sionescu.github.io/bordeaux-threads/). This library serves as an underpinning for the [lparallel](https://github.com/lmj/lparallel) library, an excellent library for multithreading. There's also [cl-async](https://orthecreedence.github.io/cl-async/) and [blackbird](https://orthecreedence.github.io/blackbird/) for asynchronous programming and promises, respectively.
7.  **Strong Community**: I discovered the community as I did the rest of the language -- in fits and starts. A good summary of the community (as it was in 2024) is summarized in the [Common Lisp Community Survey 2024](https://blog.djhaskin.com/blog/common-lisp-community-survey-2024-results/). CL features prominently at the [European Lisp Symposium](https://www.european-lisp-symposium.org/). CL has a strong [blogosphere](https://planet.lisp.org/) and [subreddit](https://www.reddit.com/r/Common_Lisp/).
8.  **Ecosystem**: The ecosystem is pretty great. Most folks use [Quicklisp](https://www.quicklisp.org/beta/), though I use [OCICL](https://github.com/ocicl/ocicl/releases) for package management. The [Common Lisp Cookbook](https://lispcookbook.github.io/cl-cookbook/), the [CLiki](https://www.cliki.net/), and [Awesome CL](https://github.com/CodyReichert/awesome-cl) provide nice survey of available libraries and techniques. Here are some answers to those particular libary queries I had:
    1.  **JSON**: [jzon](https://github.com/Zulu-Inuoe/jzon)
    2.  **Sqlite3**: [cl-sqlite](https://cl-sqlite.common-lisp.dev/)
    3.  **HTTP requests**: [dexador](https://github.com/fukamachi/dexador)
    4.  **Functional Datastructures**: [FSet](https://fset.common-lisp.dev/), [cl-hamt](https://github.com/danshapero/cl-hamt)

New Friends Take Note
---------------------

I wrote this blog post because I noticed that there have been more newcomers on the [Common Lisp Discord](https://discord.gg/HsxkkvQ) and they've been asking the same questions I was when I was first looking at the language. I wanted to lay down a bit of history around why I came to Common Lisp, and how I acclimated to the language. I hope it may be helpful to those new to or curious about Common Lisp.

