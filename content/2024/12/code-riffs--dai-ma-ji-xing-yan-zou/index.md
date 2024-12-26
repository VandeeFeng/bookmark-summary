---
title: Code Riffs-代码即兴演奏
date: 2024-12-24
extra:
  source: https://blog.fogus.me/2023/01/06/code-riffs/
  original_title: Code Riffs-代码即兴演奏
---
## Summary
**摘要**：
文章由Fogus撰写，探讨了“Code Riffs”这一概念，借用音乐界“riff”的创意，将它应用于编程中。代码“riff”指的是独立于项目叙事、通常无用、美丽抽象、在探索精神驱动下生成的代码片段。文中引用了《The Joy of Clojure》中的一段代码作为代码“riff”的例子，演示了通过简短的代码实现对列表元素的处理。Fogus还提到个人创造了多个代码“riff”，如Tori Lisp、Evalive、Unfix和《The Joy of Clojure》中提到的`break`宏，并鼓励读者分享自己的代码“riff”。

**要点总结**：
- **概念定义**：代码“riff”为独立于项目叙事、无用、美丽抽象且源于探索精神的代码片段。
- **代码示例**：使用Clojure代码展示“riff”的制作形式，实现对列表元素的处理。
- **个人作品分享**：Fogus分享了个人创造的代码“riff”，如Tori Lisp、Evalive、Unfix和《The Joy of Clojure》中提及的`break`宏。
- **邀请互动**：文章结束时邀请读者分享自己的代码“riff”，鼓励社区交流与分享。
- **身份与领域**：文章作者为活跃在Clojure和ClojureScript领域的贡献者，并倾向于阅读与写作。
## Full Content
Title: Code Riffs « Send More Paramedics

URL Source: https://blog.fogus.me/2023/01/06/code-riffs/

Markdown Content:
Code Riffs
----------

[![Image 3](https://blog.fogus.me/wp-content/uploads/2023/01/vs.png)](https://blog.fogus.me/wp-content/uploads/2023/01/vs.png)

Once upon a time I was deep into the MD/DC/VA area punk scene, and believe it or not I played in my share of bands and participated in my share of punk shows — both in the crowd and sometimes even on stage. I look back on this time fondly, but to be honest I can’t say that I ever contributed any song to the universe of music that was worth listening to. That said, while I can’t claim to have been a talented song-writer, like many aspiring musicians I did discover my fair share of riffs along the way.

A riff is an interesting little musical phrase that one often comes across whilst playing around with a guitar in a casual fashion. Very often riffs form the seeds of what becomes fully-realized songs. Sometimes these songs are good and sometimes they’re not, but in most cases they are grown like crystals from the original musical fragment found on the fret-board. For musicians, both practicing and aspiring, the riff represents a universe of potential out of which any number of potential works of musical art may spawn.

A few years ago I devised a phrase that I called [Code Painting](https://blog.fogus.me/2015/02/16/code-painting/) describing source code that: told a story, was usually not generally useful, was beautifully abstract, and created in the spirit of exploration. Unlike a code painting, a code riff is more atomic and often addresses a singular notion. If I were to characterize the attributes of a code riff then perhaps the following will suffice:

*   A code riff exists independent to a project narrative
*   A code riff need not be useful
*   A code riff is often “found” during the act of playful programming or sprung forth from one’s mind
*   A code riff should be beautiful, abstract, and as amusing if possible
*   A code riff should invoke [Huh? A ha! Ha ha!](https://blog.fogus.me/2013/09/04/a-ha-ha-ha-aah/) [1](https://blog.fogus.me/2023/01/06/code-riffs/#fn:rh)

In my time I’ve created my share of code riffs; some that inspired something more and some still ripe with potential. If you’re interested in some code riffs then a few are available on Github as [Tori Lisp](https://github.com/fogus/tori-lisp), [Evalive](https://github.com/fogus/evalive), and [Unfix](https://github.com/fogus/unfix) and additionally the `break` macro in chapter 17 of [The Joy of Clojure](https://www.amazon.com/Joy-Clojure-Michael-Fogus/dp/1617291412?tag=fogus-20).

Here’s a Clojure code riff from a presentation that I gave many years ago called “The Magnificent Seven”:

```
(def NIL ((fn [x y] (if (= x y) x)) = (= = =)))

(def CAR (fn [[h & _]] h))
(def CDR  (fn [[_ & t]] t))

(def CONS
  (fn [h t]
    (fn ([] h)
        ([_] t))))

(def FIRST (fn [s] (s)))
(def REST (fn [s] (s NIL)))

(FIRST (CONS 1 (CONS 2 NIL)))
;;=> 1

(FIRST (REST (CONS 1 (CONS 2 NIL)))
;;=> 2
```

Do you have any code riffs to share?

:F

Tags: [clojure](https://blog.fogus.me/tag/clojure/), [code-riff](https://blog.fogus.me/tag/code-riff/), [programming](https://blog.fogus.me/tag/programming/)

Categories: [programming](https://blog.fogus.me/category/programming/)

### About Send More Paramedics

My name is Fogus, although those intimate with my offline identity tend to call me Mike. I spend a lot of time with Clojure and ClojureScript as a contributor to the languages and an avid user. I also love to read and write. I can be found at various locations on the Internets, including: My \[…\][more →](https://blog.fogus.me/about/)
