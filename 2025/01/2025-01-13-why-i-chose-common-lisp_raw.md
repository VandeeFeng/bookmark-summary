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
