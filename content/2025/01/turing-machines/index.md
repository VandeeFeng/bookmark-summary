---
title: Turing Machines
date: 2025-01-14
extra:
  source: https://samwho.dev/turing-machines/
  original_title: Turing Machines
---
## Summary
**摘要**：
文章探讨了图灵机器（Turing machine）的概念，一种理论上的设备，它能够计算任何可以被计算的事物。文章首先介绍了图灵的生平和他的突破性贡献，解释了图灵机器的四个组成部分（磁带、读/写头、程序、状态）以及五条基本指令（P（打印）、R（右移）、L（左移）、↪︎（转到状态）、H（停止））。接着详细解释了图灵机器的运行机制和指令集，包括如何使用它们来实现各种计算任务。文章展示了图灵机器在实现复杂算法（如“Kevin”程序和二进制整数相加）时的具体操作，并与现代计算机的结构和功能进行了对比。文章最后提供了一个在线编辑器，让读者可以实践设计和运行自己的图灵机器程序。

**要点总结**：
1. 探索了图灵机器的基本概念，一种复杂的理论设备，设计目的是计算任何可计算的任务。
2. 介绍了图灵机器四个组成部分的功能及其用于执行任务的五条指令。
3. 示例演示图灵机器如何通过执行指令来执行简单的指令（如打印数字）和复杂任务（如二进制整数相加）。
4. 通过在线编辑器提供了一个平台，让读者可以亲手设计和运行自己的图灵机器程序。
5. 将图灵机器的原理与现代计算机的结构和功能进行比较，加深读者对计算理论的理解。
## Full Content
Title: Turing Machines

URL Source: https://samwho.dev/turing-machines/

Markdown Content:
![Image 13: Alan Turing's written signature](https://samwho.dev/images/turing-signature.svg)**ALAN M. TURING**

23 June 1912 – 7 June 1954

 [![Image 14: A pencil drawing of Alan Turing, drawn by the post author Sam Rose.](https://samwho.dev/images/turing-sketch.png)](https://samwho.dev/)F | | P(T) R P(u) R P(r) R P(i) R P(n) R P(g) R P( ) R P(M) R P(a) R P(c) R P(h) R P(i) R P(n) R P(e) R P(s) R -\> B B | | L P( ) L P( ) L P( ) L P( ) L P( ) L P( ) L P( ) L P( ) L P( ) L P( ) L P( ) L P( ) L P( ) L P( ) L P( ) -\> F

In 1928, David Hilbert, one of the most influential mathematicians of his time, asked whether it is possible to create an algorithm that could determine the correctness of a mathematical statement. This was called the "decision problem," or "Entscheidungsproblem" in Hilbert's native German. In 1936 both Alan Turing and Alonzo Church independently reached the conclusion, using different methods, that the answer is "no."

The way Turing did it was to imagine a "universal machine", a machine that could compute anything that could be computed. This idea, the "Turing machine" as Alonzo Church christened it in 1937, laid the foundations for the device you are using to read this post. If we look hard enough we can see Turing's legacy in today's CPUs.

By the end of this post, you will know:

*   What a Turing machine is.
*   What can and cannot be computed.
*   What it means to be Turing complete.
*   How modern computers relate to Turing machines.
*   How to write and run your own programs for a Turing machine.

[#](https://samwho.dev/turing-machines/#what-is-a-turing-machine) What _is_ a Turing machine?
---------------------------------------------------------------------------------------------

You might expect a universal machine, capable of computing anything that can be computed, to be a complex device. Nothing could be further from the truth. The machine has just 4 parts, and the language used to program it has just 5 instructions.

It's important to keep in mind that what Turing described is a **theoretical** machine. It was created as a thought experiment to explore the limits of what can be computed. Some have of course [been built](https://www.youtube.com/watch?v=vo8izCKHiF0), but in 1936 they existed only in the heads of Turing and those who read his paper.The parts are: a !tape, a !head, a !program, and a !state. When you're ready, go ahead and press !play.

start | | P(0) R -\> startWhat you're seeing here is a program that executes P(0) to print 0 to the tape, moves the head right with the R instruction, then !jumps back to the start. It will go on printing 0s forever.

At any point, feel free to !pause, step the machine !forwards or !backwards one instruction at a time, or !restart the program from the beginning. There is also a speed selector on the far right of the controls if you want to speed up the machine.

Notice that !state and !value never change. Every time the machine performs a !jump, the current state and value are used to pick the correct next row of instructions to execute. This program only has a single state, start, and every time it jumps, the symbol under the !head is !blank.

Let's take a look at a program with multiple states.

zero | | P(0) R -\> one one | | P(1) R -\> zeroThis program prints alternating 0s and 1s to the tape. It has 2 states, zero and one, to illustrate what happens when you !jump to a different state.

**Things moving too fast?** The slider below can be used to adjust the speed of all the Turing machines on this page.100%

You can also achieve this same result by using a single !state and alternating the !value. Here's an example of that:

start | | R P(1) -\> start start | 1 | R P(0) -\> start start | 0 | R P(1) -\> startThe !value column always stays up to date with what the current symbol is under the !head, then when we !jump that value is used to know which row of instructions to execute. Combining state and value gives us a surprising amount of control over what our !program does.

We've so far seen 3 instructions:

*   P prints a given symbol to the tape.
*   R moves the tape head right.
*   ↪︎ jumps to a given state.

There are 2 more:

*   L moves the tape head left.
*   H halts the machine.

0 | | P(n) L -\> 1 1 | | P(a) L -\> 2 2 | | P(l) L -\> 3 3 | | P(A) HThis program prints the word "Alan" from right to left then halts. If you can't see the full word, you can drag the !tape left and right. If the machine has halted, you can use !restart to start it again from the beginning.

You're telling me that everything can be computed with just these 5 instructions? Word processors, YouTube, video games, all of it?All of it! You're probably not going to get Crysis running at 60fps on a simulated Turing machine, but all of the calculations required to render each frame can be done with just these 5 instructions. Everything you have ever seen a computer do can be done with a Turing machine. We'll see a glimpse of how that can work in practice a little later.

The last example I want to show you before we move on is the very first program Alan Turing showed the world. It's the first program featured in his 1936 paper: _"On Computable Numbers, with an application to the Entsheidungsproblem."_

b | | P(0) R -\> c c | | R -\> e e | | P(1) R -\> k k | | R -\> bTuring liked to leave spaces between symbols, going as far as to even define them as "F-squares" and "E-squares". F for figure, and E for erasable. His algorithms would often make use of E-squares to help the machine remember the location of specific !tape squares.

[#](https://samwho.dev/turing-machines/#what-does-it-mean-to-compute) What does it mean to _compute_?
-----------------------------------------------------------------------------------------------------

Something is said to be "computable" if there exists an algorithm that can get from the given input to the expected output. For example, adding together 2 integers is computable. Here I'm giving the machine a !tape that starts out with the values 2 and 6 in binary separated by a !blank.

b1 | 0 | R -\> b1 b1 | 1 | R -\> b1 b1 | | R -\> b2

```
b2 | 0 | R -> b2
b2 | 1 | R -> b2
b2 |   | L -> dec

dec | 0 | P(1) L -> dec
dec | 1 | P(0) L -> b3
dec |   | H

b3 | 0 | L -> b3
b3 | 1 | L -> b3
b3 |   | L -> inc

inc | 0 | P(1) R -> b1
inc | 1 | P(0) L -> inc
inc |   | P(1) R -> b1
```
This program adds the two numbers together, arriving at the answer 8. It does this by decrementing from the right number and incrementing the left number until the right number is 0. Here's the purpose of each state:

*   b1 Move right until the first !blank square is found. This is to navigate past the first number.
*   b2 Move right until the second !blank square is found. This is to navigate past the second number.
*   dec Decrement the current number by 1. In practice this will always be the right number. It decrements by flipping bits until it either reaches a 1, where it will navigate back to the left number, or a !blank, which it will interpret as the number having hit 0.
*   b3 Move left until the first !blank square again. This is only ever used after we've decremented the rightmost number. We can't reuse the b1 state here because when we reach the !blank, we want to jump to inc.
*   inc Increment the current number by 1. Similar to decrementing, this will only ever happen on the leftmost number in practice. This is done by flipping bits until we reach a 0, at which point we navigate back to the right number.

That we can write this program at all is proof that addition is computable, but it also implies that all integers are computable. If we can add any 2 integers, we can compute any other integer. 1 is 0+1, 2 is 1+1, 3 is 2+1, and so on.

Why is the right number 111 and not 000 at the end of this program?It's tricky to write the equivalent of `if (rightNum === 0) break;` in a Turing machine, so this program does it as part of the decrementing process. If, while decrementing, it gets all the way to a !blank square, it interprets that to mean the number has hit 0 and halts.

### [#](https://samwho.dev/turing-machines/#binary-vs-decimal) Binary vs Decimal

You may have wondered why I'm choosing to work with binary numbers rather than decimal. It's not just because that's how modern computers work. I'm going to show you 2 examples, and from those examples you'll be able to see _why_ modern computers choose to work in binary.

The first example is a program that increments a binary number in an endless loop.

move | 1 | R -\> move move | 0 | R -\> move move | | L -\> flip flip | 0 | P(1) R -\> move flip | 1 | P(0) L -\> flip flip | | P(1) R -\> moveThe second example is a program that increments a decimal number in an endless loop.

inc | 0 | P(1) -\> back inc | 1 | P(2) -\> back inc | 2 | P(3) -\> back inc | 3 | P(4) -\> back inc | 4 | P(5) -\> back inc | 5 | P(6) -\> back inc | 6 | P(7) -\> back inc | 7 | P(8) -\> back inc | 8 | P(9) -\> back inc | 9 | P(0) L -\> inc inc | | P(1) -\> back back | | L -\> inc back | \* | R -\> backThese two programs are doing the same thing, but the program for manipulating decimal numbers is much longer. We've even introduced some new syntax, the \* symbol, to handle a !value under the !head that does not match any of the other values for that !state. It's for this reason when programming Turing machines we prefer binary numbers: the programs end up being shorter and easier to reason about.

This benefit also translates to the physical world. Components that switch between 2 states are cheaper, smaller, and more reliable than components that switch between 10. It was more practical to build computers that worked in binary than ones that work in decimal, though attempts to build decimal computers [were made](https://en.wikipedia.org/wiki/Decimal_computer).

[#](https://samwho.dev/turing-machines/#what-can-t-be-computed) What _can't_ be computed?
-----------------------------------------------------------------------------------------

To approach this question we need to explain the "Halting problem." It goes like this:

> Given a program and some input, is it possible to write a second program that will tell you with certainty whether the first program will halt or run forever?

The answer is no, and this is what Turing essentially proved. The proof is complicated and I'm not ashamed to admit I don't understand it, but there is an example I can give you that can be intuitively understood to be "undecidable."

Imagine you write a program that takes as its input the program being used to decide whether it will halt or not. What it then does is run the decider program on itself, and then do the opposite of what the decider program says.

```
function undecidable(willHalt) {
  if (willHalt(undecidable)) {
    while (true);
  } else {
    return true;
  }
}
```

This program intentionally enters an infinite loop if it is told it will halt, and halts if it is told it will run forever. It seems like a silly example, the kind of answer a cheeky high school student might try to get away with, but it is a legitimate counterexample to the idea that the halting problem can be solved.

If you were to imagine encoding the program and input into something that could be represented on the !tape, there would be no !program that could determine whether the program would halt or not. Imagining this encoding becomes quite natural when you realise that modern programs are encoded as binary data to be saved to disk.

[#](https://samwho.dev/turing-machines/#what-does-it-mean-to-be-turing-complete) What does it mean to be _Turing complete_?
---------------------------------------------------------------------------------------------------------------------------

If you've been involved in the world of programming for more than a few years, there's a good chance you've come across the term "Turing complete." Most likely in the context of things that really ought not to be Turing complete, like [C++ templates](https://rtraba.com/wp-content/uploads/2015/05/cppturing.pdf), [TypeScript's type system](https://itnext.io/typescript-and-turing-completeness-ba8ded8f3de3) or [Microsoft Excel](https://www.infoq.com/articles/excel-lambda-turing-complete/).

But what does it _mean_?

Like the Halting problem, the proof is complicated but there's a straightforward test you can apply to something to judge it Turing complete:

> A system is Turing complete if it can be used to simulate a Turing machine.

I've written this post, with the Turing machine simulations, in JavaScript. Therefore JavaScript is Turing complete. The C++ template example given above simulates a Turing machine in C++'s template system. The TypeScript example takes the route of writing an interpreter for a different Turing complete language.

Wait a second, wouldn't you need an infinite amount of memory to simulate a Turing machine? Doesn't the !tape extend forever in both directions?You're right, and everyone tends to cheat a bit with the definition. When someone says something is Turing complete, what they mean is it _would_ be Turing complete if it had an infinite amount of memory. The infinite tape limitation means no Turing machine could ever exist in our physical reality, so that requirement tends to get waived.

[#](https://samwho.dev/turing-machines/#how-does-this-all-relate-to-modern-computers) How does this all relate to _modern computers_?
-------------------------------------------------------------------------------------------------------------------------------------

If you read around the topic of Turing machines outside of this post, you might see it said that modern computers are effectively Turing machines. You would be forgiven for finding it difficult to imagine how you go from adding 2 integers in binary on a !tape to running a web browser, but the line is there.

A key difference between our Turing machine and the device you're reading this on is that your device's CPU has "registers." These are small pieces of memory that live directly on the CPU and are used to store values temporarily while they're being operated on. Values are being constantly loaded from memory into registers and saved back again. You can think of registers as variables for your CPU, but they can only store fixed-size numbers.

We _can_ create registers in our Turing machine. We can do this by creating a "format" for our tape.

Here we define 3 registers: A, B, and C. Each register contains a 3 bits and can store numbers between 0 and 7. Then at the far left we have an H, which stands for "home", which will help us navigate.

To increment register C, we can write a program like this:

goto\_c | \* | R -\> goto\_c goto\_c | C | R R R -\> inc inc | 0 | P(1) -\> goto\_h goto\_h | \* | L -\> goto\_h goto\_h | H | HWe're making a lot more liberal use of the \* symbol here to help us navigate to specific parts of the !tape without having to enumerate all possible values that could be under the !head on the way there.

This program is effectively equivalent to the following x86 assembly code, if x86 had a register named `c`:

```
mov c, 0 ; Load 0 into c
inc c    ; Increment c by 1
```

If we wanted to add values in A and B, storing the result in C, we need to do more work. Here's the assembly code we're trying to replicate:

```
mov a, 2  ; Load 2 into a
mov b, 3  ; Load 3 into b
add c, a  ; Add a to c
add c, b  ; Add b to c
```

Before you scroll down I will warn you that the program is long and complex. It is the last program we will see in this post, and I don't expect you to understand it in full to continue to the end. Its main purpose is to show you that we _can_ implement operations seen in modern assembly code on a Turing machine.

inita | \* | R R P(0) R P(1) R P(0) R -\> initb initb | \* | R P(0) R P(1) R P(1) R -\> start

```
start | * | L -> start
start | H | R -> go_a

go_a | * | R -> go_a
go_a | A | R R R -> dec_a

dec_a  | 0 | P(1) L -> cry_a
dec_a  | 1 | P(0) -> go_c1

cry_a | 0 | P(1) L -> cry_a
cry_a | 1 | P(0) -> go_c1
cry_a | * | R P(0) R P(0) R P(0) -> goto_b

go_c1 | * | R -> go_c1
go_c1 | C | R R R -> inc_c1

inc_c1 | 0 | P(1) -> h2a
inc_c1 | 1 | P(0) L -> cry_ca

cry_ca | 0 | P(1) -> h2a
cry_ca | 1 | P(0) L -> cry_ca
cry_ca | * | R -> h2a

h2a | * | L -> h2a
h2a | H | R -> go_a

goto_b | * | R -> goto_b
goto_b | B | R R R -> dec_b

dec_b | 0 | P(1) L -> dec_bc
dec_b | 1 | P(0) -> go_c2

dec_bc | 0 | P(1) L -> dec_bc
dec_bc | 1 | P(0) -> go_c2
dec_bc | * | R P(0) R P(0) R P(0) -> end

go_c2 | * | R -> go_c2
go_c2 | C | R R R -> inc_c2

inc_c2 | 0 | P(1) -> go_hb
inc_c2 | 1 | P(0) L -> cry_cb

cry_cb | 0 | P(1) -> go_hb
cry_cb | 1 | P(0) L -> cry_cb
cry_cb | * | R -> go_hb

go_hb | * | L -> go_hb
go_hb | H | R -> goto_b

end | * | L -> end
end | H | H
```
This is painfully laborious, and it doesn't even precisely match the assembly code. It destroys the values in A and B as it adds them together, and it doesn't handle overflow. But it's a start, and I hope it gives you a glimpse of how this theoretical machine can be built up to operate like a modern CPU.

If you watch the program run to completion, something that might strike you is just how much work is required to do something as simple as adding 2 numbers. Turing machines were not designed to be practical, Turing never intended anyone to go out and build one of these machines in the hope it will be useful.

Modern machines have circuits within them that can add 2 numbers together by passing 2 electrical signals in and getting the sum as a single signal out. This happens in less than a nanosecond. Modern machines have memory where any byte can be accessed at any time, no tape manipulation required. This memory access takes a few dozen nanoseconds.

[#](https://samwho.dev/turing-machines/#writing-and-running-your-own-programs) Writing and running your own programs
--------------------------------------------------------------------------------------------------------------------

I've built a web-based development environment for writing programs that will run on the Turing machine visualisations you've seen throughout the post.

You can access the editor **[here](https://samwho.dev/christopher)**.

I encourage you to play around with it. Set a simple goal, like adding together 2 numbers without going back to look at the way I did it in the post. It's a great way to get a feel for how the machine works.

[#](https://samwho.dev/turing-machines/#conclusion) Conclusion
--------------------------------------------------------------

To recap, we've covered:

*   What a Turing machine is.
*   What can and cannot be computed.
*   What it means to be Turing complete.
*   How modern computers relate to Turing machines.

And you now have access to an environment for writing and running your own Turing machine programs. If you use it to make something neat, please do reach out to me and show me! My email address is [hello@samwho.dev](mailto:hello@samwho.dev).

![Image 15](https://samwho.dev/images/turing-apple.png)

On June 8th, 1954, Alan Turing was found dead in bed, at his home in Wilmslow. He had died the day before, aged 41, from cyanide poisoning. A half-slice of apple was on his bedside table, laced with cyanide. An inquest ruled the death a suicide.

[#](https://samwho.dev/turing-machines/#further-reading) Further reading
------------------------------------------------------------------------

*   [Turing's original paper](https://archive.org/details/Turing1936OnCumputableNumbers/page/n3/mode/2up) on computable numbers.
*   [The Annotated Turing](https://www.charlespetzold.com/AnnotatedTuring/) I referenced this throughout the making of this post. It is a fabulous read, strongly recommend.
*   [Alan Turing: The Enigma](https://en.wikipedia.org/wiki/Alan_Turing:_The_Enigma) by Andrew Hodges. An excellent biography of Turing, I read this during the writing of this post.
*   [Calculating a Mandelbrot Set using a Turing Machine](https://redfrontdoor.org/turing-mandelbrot/). This was exceptionally useful for me to understand how to get from Turing machines to modern computers.

![Image 16](https://samwho.dev/images/christopher-morcom.png)

Christopher Morcom, 13 July 1911 - 13 February 1930. Turing's childhood friend and first love.

[#](https://samwho.dev/turing-machines/#acknowledgements) Acknowledgements
--------------------------------------------------------------------------

These posts are never a solo effort, and this one is no exception. Sincere thanks go to the following people:

*   To my wife, Sophie, who drew the biographical sketches you're seeing at the end here, and for putting up with my incessant talking about this post the last 2 weeks.
*   Everyone who let me watch them read this post in real-time over a video call and gave me feedback: [Jaga Santagostino](https://jagasantagostino.com/), [Robert Aboukhalil](https://robert.bio/), [Tarun Verghis](https://bsky.app/profile/me.tverghis.space), [Tyler Sparks](https://tylerity.com/).
*   Everyone who came to hang out and help out in the [Twitch streams](https://www.twitch.tv/samwhoo) when I was building out the early versions of the Turing machine visualisations.
*   Everyone who supports my work on [Patreon](https://patreon.com/samwho).
*   Everyone who works on the tools used to build this post: TypeScript, Bun, Two.js, Tween.js, Monaco, Peggy, Zed, and many other indirect dependencies. We really do stand upon the shoulders of giants.

![Image 17](https://samwho.dev/images/hut-8.png)

Hut 8, Bletchley Park, where Turing worked during World War II. It was in this hut that Alan worked with his team to break the German Naval Enigma code.

