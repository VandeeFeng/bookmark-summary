---
title: Discovery Coding
date: 2025-01-29
extra:
  source: https://jimmyhmiller.github.io/discovery-coding
  original_title: Discovery Coding
---
## Summary
**摘要**：
文章主要探讨了“发现式编码”的概念，这是一个编程实践，即通过直接编写代码来理解问题，而不是预先设计或思考。与构建大纲的程序员形成对比，发现式程序员在开始编写代码前通常没有明确的计划。发现式编码旨在通过编写代码并观察代码给出的阻力来理解问题，进而制定解决问题的计划。文章认为，发现式编码不应被视为负面实践，因为目标不仅仅是代码本身，而是创作过程。它提供了了解系统工作方式并获取约束条件的优势，而不是继承现成的解决方案。最后，文章呼吁编程界接受发现式编码，并认识到不同的开发思想并不意味着一种方法优于另一种，并鼓励工具和技术的发展以支持不同类型的开发实践。

**要点总结**：
- **定义**：发现式编码是一种了解问题的实践，通过编写代码而不是预先设计或思考来实现。
- **与大纲相比**：发现式程序员在开始编写代码时通常没有明确的计划，他们的方法可能被视为杂乱或无条理。
- **优点**：避免项目的先入为主，使程序员能够通过编写代码理解环境的规则和需求，而不是依赖过去的解决方案。
- **编程文化和工具**：当前的文化和技术倾向于结构化操作，可能导致将发现式编码视为负面实践，然而，确实有工具和技术可以支持这样的开发方式。
- **接受与理解差异**：编程界应接受并理解不同类型的编程方法，认识到一种方法的广泛使用并不意味着它总是最佳选择，接受多样性与创新。
## Full Content
Title: Discovery Coding

URL Source: https://jimmyhmiller.github.io/discovery-coding

Markdown Content:
> I don't take notes; I don't outline, I don't do anything like that. I just flail away at the goddamn thing. - Steven King

In writing (particularly fiction writing), there is a generally accepted distinction between authors who start by writing an outline and those who discover their stories through the process of writing. For some reason, we have no such distinction in programming, so I am here to introduce it.

Discovery Coding Explained
--------------------------

Discovery coding is a practice of understanding a problem by writing code first, rather than attempting to do some design process or thinking beforehand. This means that a discovery programmer does not always start with a plan before starting to write code; rather, they think about the situation they are in. What is the tension we are trying to solve with this new code? What are the situations that have given rise to this demand? How do these various bits of the system interact? It is only in the process of writing code and seeing the pushback the code gives that discovery programmers understand and devise a plan forward.

Discovery programmers can often be seen as messy or undisciplined. When working with their outlining counterparts, there may be some tension that isn't properly placed. The outline programmer may feel unease when seeing the haphazard approach of the discovery programmer. The discovery programmer, on the other hand, may be confused by the seemingly incorrectly timed questions posed by the outliner.

In our current culture that prefers more structured technologies (static type systems, enforced memory safety, schema enforcement tools, etc.), it is easy to label discovery coding as a bad practice, but it is important to distinguish the process of creation from the end-artifact. There is no reason that a discovery programmer cannot create a highly structured, rigorous end-artifact.

**Aside Discovery Coding is not Bottom Up**

Discovery coding and bottom-up design are not the same thing. It wouldn't surprise me if discovery coders often tend to enjoy bottom-up design, and outliners prefer top-down design. But these are orthogonal axes. Top-down design is about the angle by which you tackle a problem, not the process by which you go about understanding it. Imagine this: you write a detailed design document well ahead of coding, laying out core primitives and how they will compose to solve the problem. Here we clearly have an outliner doing a bottom-up design process.

Benefits of Discovery Coding
----------------------------

Even for the outliner, I think discovery coding can have quite a few benefits. When approaching problems looking for a solution, it is very easy to start with those solutions we are most familiar with. Discovery coding, by its nature, avoids this pitfall. Discovery coding does not have a solution to offer, so the code we begin writing is instead about poking the system and understanding how it works. By doing this, you are filling your mind not with the context of past solutions or descriptions of solutions others have told you. Instead, you are loading up a series of constraints that the system has that your solution must satisfy.

For me, this is the only way I can do anything. Anytime I try to outline before I write code, my outline is thrown away within hours of writing code. My design docs that are written beforehand are wholly unsatisfying, even if they get approved. It is only as I begin writing code that I begin to understand my problem. So the next section here won't be on the benefits of outlining. Not because there aren't any, but because I'm not the person to write those. (Nor will I write about the downsides of discovery coding, because I am certain everyone can list those.)

**Aside Tooling to help with Discovery Coding**

I don't think many tools today are designed with discovery coding in mind. Things like live programming in a running system (see how (most) Clojurists or SmallTalkers work) are incredibly valuable for a discovery programmer. Systems that let you visualize on the fly, instrument parts of the system, etc., make it much easier and faster to discover things. This is the sense of dynamic (unrelated to typing) that I feel we often lose sight of.

We Ought to Accept Discovery Coding
-----------------------------------

The writing community has learned to accept that some people just are discovery writers. That the very process of outlining before writing can cause some people to be unable to write in the way they want to. My exhortation for the programming community is that we ought to do the same thing. What I'm not advocating for is the banning of all design documents (those can be useful), but instead the recognition and acceptance that some people simply think differently. That being less organized isn't an inferior approach. That being able to think through details before you code isn't superior.

Perhaps I have the wrong read of the current cultural milieu (or perhaps you are reading this years later and culture has shifted). Perhaps discovery coding is loved and cherished and outlining is scorned. If so, please invert all of the above. What I hope we can recognize is that there is no one answer. Designing software is a human process and not all humans are the same.

