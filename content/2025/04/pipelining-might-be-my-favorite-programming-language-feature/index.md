---
title: Pipelining might be my favorite programming language feature
date: 2025-04-22
extra:
  source: https://herecomesthemoon.net/2025/04/pipelining/
  original_title: Pipelining might be my favorite programming language feature
---
## Summary
**摘要**：
**摘要**：
作者认为管道化是编程语言中一个非常棒的特性，它允许省略参数列表中的单个参数，通过传递前一个值来实现。管道化使得代码可以按行阅读，易于注释，无需引入新变量即可提高可读性。作者通过对比管道化和非管道化的代码示例，强调了管道化在可读性、代码发现和编辑方面的优势。在SQL中，管道化可以简化嵌套查询，并使其更易于理解。此外，文章还提到了构建器模式，它与管道化结合使用可以更方便地构建复杂对象。作者还探讨了Haskell语言中管道化的应用，以及Rust语言中管道化的优点，Rust兼具类型推断和命名空间的优点，使得管道化使用起来非常方便。总而言之，作者喜欢从上到下、从左到右阅读代码，喜欢编辑器在按下“.”时显示所有字段和方法，喜欢`git diff`和代码仓库的`blame`层看起来不混乱，以及在添加函数调用时无需解析整行代码。

**要点总结**：
1.  **代码可读性**：管道化通过链式调用，使得代码可以按步骤阅读和理解，数据流向清晰，避免了从内到外的复杂嵌套结构，提高了代码的可读性，更易于理解每一步操作的目的。
2.  **编辑的便捷性**：在管道化的代码中，添加、删除或修改步骤更加简单直观，无需过多关注括号的匹配和参数的位置，减少了出错的可能性，并且在代码版本控制中，修改的内容可以清晰地显示出来，方便代码审查和追踪。
3.  **代码发现**：通过IDE的代码自动完成功能，可以快速找到对象可用的方法和属性，无需手动查找文档，能够极大地提高开发效率，而管道化能够使IDE更容易地识别出对象的类型，从而提供更准确的代码提示。
4.  **SQL中的应用**：管道化可以应用于SQL查询中，将嵌套查询转换为更易读的链式操作，从而简化复杂的SQL语句，使得数据处理的流程更加清晰，降低了理解和维护SQL代码的难度。
5.  **Rust的优势**：Rust语言在支持类型推断的同时，还提供了命名空间、方法和关联值，使得管道化在Rust中既具有灵活性又具有结构性，避免了传统面向对象编程中复杂的继承关系，让代码更加简洁和易于维护。

## Full Content
Title: Pipelining might be my favorite programming language feature

URL Source: https://herecomesthemoon.net/2025/04/pipelining/

Published Time: 2025-04-21T00:00:00+00:00

Markdown Content:
_**Epistemic status:** Don’t take it too seriously. Or do. idk, I can’t stop you._

![Image 1: Pop culture reference.](https://herecomesthemoon.net/2025/04/pipelining/images/dithers/neat2_dithered.png)

Pop culture reference.Toggle original/dithered image

Pipelining might be my favorite programming language feature.

What is pipelining? Pipelining is the feature that allows you to omit a single argument from your parameter list, by instead passing the previous value.

When I say pipelining, I’m talking about the ability to write code like this:

```
fn get_ids(data: Vec<Widget>) -> Vec<Id> {
    data.iter()              // get iterator over elements of the list
        .filter(|w| w.alive) // use lambda to ignore tombstoned widgets
        .map(|w| w.id)       // extract ids from widgets
        .collect()           // assemble iterator into data structure (Vec)
}
```

As opposed to code like this. (This is not real Rust code. Quick challenge for the curious Rustacean, can you explain why we cannot rewrite the above code like this, even if we import all of the symbols?)

```
fn get_ids(data: Vec<Widget>) -> Vec<Id> {
    collect(map(filter(iter(data), |w| w.alive), |w| w.id))
}
```

I honestly feel like this should be so obvious that it shouldn’t even be up for debate. The first code example—with its nice ‘pipelining’ or ‘method chaining’ or whatever you want to call it—it _just works_. It can be read line-by-line. It’s easy to annotate it with comments. It doesn’t require introduction of new variables to become more readable since it’s already readable as is.

As opposed to, y’know, _the first word in the line describing the final action our function performs_.

Let me make it very clear: This is an ~article~ _hot take_ about syntax. In practice, _semantics beat syntax every day of the week_. In other words, don’t take it too seriously.

Second, this is not about imperative vs. functional programming. This article takes for granted that you’re already on board with concepts such as ‘map’ and ‘filter’. It’s possible to overuse that style, but I won’t talk about it here.

*   [You already agree with me](https://herecomesthemoon.net/2025/04/pipelining/#you-already-agree-with-me)
*   [Code Discovery](https://herecomesthemoon.net/2025/04/pipelining/#code-discovery)
*   [Editing Benefits](https://herecomesthemoon.net/2025/04/pipelining/#editing-benefits)
*   [SQL](https://herecomesthemoon.net/2025/04/pipelining/#sql)
*   [The Builder Pattern](https://herecomesthemoon.net/2025/04/pipelining/#the-builder-pattern)
*   [Rust’s pipelining is pretty neat](https://herecomesthemoon.net/2025/04/pipelining/#rusts-pipelining-is-pretty-neat)
*   [Conclusion](https://herecomesthemoon.net/2025/04/pipelining/#conclusion)

You already agree with me
-------------------------

Here is a feature that’s so bog-standard in modern programming languages that it barely feels like a feature at all. Member access for structs or classes with our beloved friend the `.`\-operator.

This is a form of pipelining. It puts the data first, the operator in the middle, and concludes with the action (restricting to a member field). That’s an instance of what I call pipelining.

```
type Bar struct {
	field int
}

func get_field(bar Bar) int {
	return bar.field
}
// vs. syntax like that of Python's `getattr` function
func get_field(bar Bar) int {
	return getattr(bar, "field")
}
```

You see what I am getting at, right? It’s the same principle. One of the reasons why `x.y`\-style member access syntax (and `x.y()`\-style method call syntax!) is popular is since it’s easy to read and chains easily.

Let’s make the comparison slightly more fair, and pretend that we have to write `x.get(y)`. Compare:

```
fizz.get(bar).get(buzz).get(foo)
// vs.
get(get(get(fizz, bar), buzz), foo)
```

Which one of these is easier to read? The pipelined syntax, obviously. This example is easy to parse either way, but imagine you’d like to blend out some information and purely focus on the final operation.

```
<previous stuff>.get(foo)
// vs.
get(<previous stuff>, foo)
```

You see the problem, right? In the first example, we have ‘all of the previous stuff’ and then _apply another operation_ to it. In the second example, the operation which we want to perform (`get`) and the new operand (`foo`) are spread out with ‘all of the previous stuff’ sitting between them.

Looking back at our original example, the problem should be obvious:

```
fn get_ids(data: Vec<Widget>) -> Vec<Id> {
    collect(map(filter(iter(data), |w| w.alive), |w| w.id))
}
-----------------------------1 // it's fun to parse the whole line to find the start
------------------------2
-----------------3
---------------------------------------4 // all the way back to find the second arg
-------------5
------------------------------------------------------6 // and all the way back again
-----7 // okay the final step is the first word in the line that makes sense
```

I cannot deny the allegations: I just don’t think it makes sense to write code like that as long as a clearly better option exists.

Why would I have to parse the whole line just to figure out where my input comes in, and why is the data flow ‘from the inside to the outside’? It’s kind of silly, if you ask me.

Editing Benefits
----------------

![Image 2: The experience of trying to use pipelining syntax in Python.](https://herecomesthemoon.net/2025/04/pipelining/images/dithers/pipe-rock_dithered.png)

The experience of trying to use pipelining syntax in Python.Toggle original/dithered image

Readability is nice, and I could add add a whole section complaining about the mess that’s Python’s ‘functional’ features.

However, let’s take a step back and talk about ease of editing. Going back to the example above, imagine you’d like to add another `map` (or any other function call) in the middle there. How easy is this?

```
fn get_ids(data: Vec<Widget>) -> Vec<Id> {
    collect(map(filter(map(iter(data), |w| w.toWingding()), |w| w.alive), |w| w.id))
}
```

Consider:

1.  You’ll have to parse through the line, counting commas and parentheses to find the exact place to add the closing parenthesis.
2.  The `git diff` of this is going to be basically unreadable, everything is crammed onto one line.
3.  This line is getting long and unreadable, and at that point you’ll want to refactor it anyway!

```
fn get_ids(data: Vec<Widget>) -> Vec<Id> {
    data.iter()
        .map(|w| w.toWingding())
        .filter(|w| w.alive)
        .map(|w| w.id)
        .collect()
}
```

This is adding a single line of code. No parentheses counting. It’s easy and obvious. It’s easy to write and easy to review. Perhaps most importantly, it shows up _incredibly nicely_ in the `blame` layer of whatever editor or code exploration tool you’re using.

You might think that this issue is _just_ about trying to cram everything onto a single line, but frankly, trying to move away from that doesn’t help much. It will still mess up your git diffs and the blame layer.

You can, of course, just assign the result of every `filter` and `map` call to a helper variable, and I will (begrudgingly) acknowledge that that works, and is _significantly_ better than trying to do absurd levels of nesting.

Code Discovery
--------------

When you press `.` in your IDE, it will show a neat little pop-up that tells you which methods you can call or which fields you can access.

This is probably the single IDE feature with the biggest value add, and if not that, then at least the single most frequently used one. Some people will tell you that static analysis for namespace or module-level code discovery is useless in the age of AI autocompletion and vibe coding, but I very much disagree.[1](https://herecomesthemoon.net/2025/04/pipelining/#fn:1)

A [wise shaman once said](https://grugbrain.dev/):

> “grug very like type systems make programming easier. for grug, type systems most value when grug hit dot on keyboard and list of things grug can do pop up magic. this 90% of value of type system or more to grug” — grug

Words to live by. What he’s describing here is something that essentially _requires_ pipelining to work at all. (And types or type annotation, but having those is the direction the industry is moving in anyway.)

It doesn’t matter if it’s the trusty `.` operator, C++’s `->`, or if it’s something more bespoke such as Elm’s or Gleam’s `|>` or Haskell’s `&`. In the end, it’s a pipeline operator—the same principle applies. If your [LSP](https://en.wikipedia.org/wiki/Language_Server_Protocol) knows the type of what’s on the left, it _should_ in principle be able to offer suggestions for what to do next.

If your favorite language’s LSP/IDE does a poor job at offering suggestions during pipelining, then it’s probably one of the following reasons:

1.  You don’t know which type you’re even holding. This happens most often when the language is dynamically typed, ’types’ are hard to deduce with static analysis, and you’re touching/writing code without type annotations. (e.g. Python)
2.  The ecosystem and LSP just didn’t have enough time put into them, or most active users don’t care enough. (e.g. any sufficiently obscure language)
3.  You are in a situation in which even looking up which methods are available is hard, often due to a bespoke build process that confuses the editor. (e.g. basically any build or runtime generation of code, or bespoke loading/selection of libraries).

In either case, great editor/LSP support is more or less considered mandatory for modern programming languages. And of course, this is where pipelining shines.

Ask any IDE, autocompleting `fizz.bu... -> fizz.buzz()` is _much easier_ than autocompleting `bu... -> buzz(...)`, for the obvious reason that you _didn’t even write `fizz` in the second example yet_, so your editor has less information to work with.

SQL
---

Pipelining is _amazing_ at data processing, and allows you to transform code that’s commonly written with ‘inside-out’ control flow into ’line-by-line’ transformations.

Where could this possibly be more clear than in SQL, the presumably single most significant language for querying and aggregating complex large-scale datasets?

You’ll be pleased to hear that, yes, people are in fact working on bringing pipelining to SQL. (Whether it’s actually going to happen in this specific form [is a different question](https://sqlite.org/forum/forumpost/2d2720461b82f2fd), let’s not get too carried away here.)

Unless you’re one of those people who spends so much time dealing with SQL that it’s become second nature, and the thought that the control flow of nested queries is hard to follow for the average non-database engineer is incomprehensible to you, I guess.

Personally, I’m a fan.

Anyway, if you’re interested, listen to this [ten minute talk presented at HYTRADBOI 2025](https://www.hytradboi.com/2025/f8582cd3-1e39-43a8-8749-46817b2910cf-pipe-syntax-in-sql-its-time).

I’ll put their example of how a standard nested query can be simplified here, for convenience:

```
SELECT c_count, COUNT(*) AS custdist
  FROM
  (
    SELECT c_custkey, COUNT(o_orderkey) c_count
    FROM customer
    LEFT OUTER JOIN orders
      ON c_custkey = o_custkey
      AND o_comment NOT LIKE '%unusual%'
    GROUP BY c_custkey
  ) AS c_orders
GROUP BY c_count
ORDER BY custdist DESC;
```

Versus the SQL Syntax she told you not to worry about:

```
FROM customer
|> LEFT OUTER JOIN orders
    ON c_custkey = o_custkey
    AND o_comment NOT LIKE '%unusual%'
|> AGGREGATE COUNT(o_orderkey) AS c_count
  GROUP BY c_custkey
|> AGGREGATE COUNT(*) AS custdist
  GROUP BY c_count
|> ORDER BY custdist DESC;
```

Less nesting. More aligned with other languages and [LINQ](https://learn.microsoft.com/en-us/dotnet/csharp/linq/). Can easily be read line-by-line.

Here’s a more [skeptical voice (warning, LinkedIn!)](https://www.linkedin.com/pulse/not-so-good-idea-pipe-syntax-sql-franck-pachot-dx6he). Franck Pachot raises the great point that the `SELECT` statement at the top of a query is (essentially) its function signature and specifies the return type. With pipe syntax, you lose some of this readability.

I agree, but that seems like a solvable problem to me.

The Builder pattern
-------------------

![Image 3: A picture of some pipes half-way through to break up the text and make the article less monotonous.](https://herecomesthemoon.net/2025/04/pipelining/images/dithers/pipes_dithered.png)

A picture of some pipes half-way through to break up the text and make the article less monotonous.Toggle original/dithered image

Out of the Gang of Four [Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns), the [builder pattern](https://en.wikipedia.org/wiki/Builder_pattern) is one that isn’t completely irredeemable.

And—surprise, surprise—it fits pretty well into pipelining. Any situation where you need to construct a complex, stateful object (e.g. a client or runtime), it’s a great way to feed complex, optional arguments into an object.

Some people say they prefer optional/named arguments, but honestly, I don’t understand why: An optional named `foo` parameter is harder to track down in code (and harder to mark as deprecated!) than all instances of a `.setFoo()` builder function.

If you have no clue what I’m talking about, this here is the type of pattern I’m talking about. You have a ‘builder’ object, call some methods on it to configure it, and finally `build()` the object you’re actually interested in.

```
use tokio::runtime::Builder;

fn main() {
    // build runtime
    let runtime = Builder::new_multi_thread()
        .worker_threads(4)
        .thread_name("my-custom-name")
        .thread_stack_size(3 * 1024 * 1024)
        .build()
        .unwrap();

    // use runtime ...
}
```

This too, is pipelining.

Making Haskell (slightly more) readable
---------------------------------------

Haskell is hard to read.

It has these weird operators like `<$>`, `<*>`, `$`, or `>>=` and when you ask Haskell programmers about what they mean, they say something like “Oh, this is just a special case of the generalized [Kleisli Monad Operator](https://hackage.haskell.org/package/base-4.12.0.0/docs/Control-Monad.html#v:-62--61--62-) `>=>` in the category of endo-pro-applicatives over a locally small poset.” and your eyes have glazed over before they’ve even finished the sentence.

(It also doesn’t help that Haskell allows you to define custom operators however you please, yes.)

If you’re wondering “How could a language have so many bespoke operators?”, my understanding is that most of them are just fancy ways of telling Haskell to compose some functions in a highly advanced way. Here’s the second-most basic[2](https://herecomesthemoon.net/2025/04/pipelining/#fn:2) example, the `$` operator.

Imagine you have functions `foo`, `bar`, and some value `data`. In a “““normal””” language you might write `foo(data)`. In Haskell, this is written as `foo data`. This is since `foo` will automatically ‘grab’ values to the right as its arguments, so you don’t need the parentheses.

A consequence of this is that `bar(foo(data))` is written as `bar (foo data)` in Haskell. If you wrote `bar foo data`, the compiler will interpret it as `bar(foo)(data)`, which would be wrong. This is what people mean when they say that Haskell’s function call syntax is [left-associative](https://en.wikipedia.org/wiki/Associative_property).

The `$` operator is _nothing but syntactic sugar_ that allows you to write `bar $ foo data` instead of having to write `bar (foo data)`. That’s it. People were fed-up with having to put parens everywhere, I guess.

If your eyes glazed over at this point, I can’t blame you.

Let’s get back on track.

Talking about any of the fancier operators would be punching well above my weight-class, so I’ll just stick to what I’ve been saying throughout this entire post already. Here’s a stilted Haskell toy example, intentionally not written in [pointfree](https://wiki.haskell.org/Pointfree) style.

```
-- Take an input string `content`
-- Split into lines, check whether each line is a palindrome and stringify
-- Ex. "foo\nradar" -> "False\nTrue"
checkPalindromes :: String -> String
checkPalindromes content = unlines $ map (show . isPalindrome) $ lines $ map toLower content
  where
    isPalindrome xs = xs == reverse xs
```

If you want to figure out the flow of data, this whole function body has to be read _right-to-left_.

To make things even funnier, you need to start with the `where` clause to figure out which local “variables” are being defined. This happens (for whatever reason) at the end of the function instead of at the start. (Calling `isPalindrome` a variable is misleading, but that’s besides the point.)

At this point you might wonder if Haskell has some sort of pipelining operator, and yes, it turns out that one was [added in 2014](https://github.com/haskell/core-libraries-committee/issues/78#issuecomment-1183568372)! That’s pretty late considering that Haskell exists since 1990. This allows us to refactor the above code as follows:

```
checkPalindromes :: String -> String
checkPalindromes content =
  content
    & map toLower
    & lines
    & map (show . isPalindrome)
    & unlines
  where
    isPalindrome xs = xs == reverse xs
```

Isn’t that way easier to read?

_This_ is code which you can show to an enterprise Java programmer, tell them that they’re looking at [Java Streams](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html) with slightly weird syntax, and they’ll get the idea.

Of course, in reality nothing is as simple. The Haskell ecosystem seems to be split between users of `$`, users of `&`, and users of the [Flow](https://hackage.haskell.org/package/flow-2.0.0.0/docs/Flow.html#g:1)\-provided operators, which allow the same functionality, but allow you to write `|>` instead of `&`.[3](https://herecomesthemoon.net/2025/04/pipelining/#fn:3)

I don’t know what to say about that, other than that—not entirely unlike C++—Haskell has its own share of operator-related and cultural historical baggage, and a split ecosystem, and this makes the language significantly less approachable than it has to be.

Rust’s pipelining is pretty neat
--------------------------------

![Image 4: Pop(?) culture reference.](https://herecomesthemoon.net/2025/04/pipelining/images/dithers/magrittepipe_dithered.png)

Pop(?) culture reference.Toggle original/dithered image

In the beginning I said that ‘Pipelining is the feature that allows you to omit a single argument from your parameter list, by instead passing the previous value.’

I still think that this is true, but it doesn’t get across the whole picture. If you’ve paid attention in the previous sections, you’ll have noticed that `object.member` and `iterator & map` share basically _nothing_ in common outside of the order of operations.

In the first case, we’re accessing a value that’s _scoped_ to the object. In the second, we’re ‘just’ passing an expression to a free-standing function.

Or in other words, pipelining is not the same as pipelining. Even from an IDE-perspective, they’re different. In Java, your editor will look for methods associated with an object and walk up the inheritance chain. In Haskell, your editor will put a so-called [’typed hole’](https://downloads.haskell.org/~ghc/7.10.3-rc1/users_guide/typed-holes.html), and try to deduce which functions have a type that ‘fits’ into the hole using [Hindley-Milner Type Inference](https://herecomesthemoon.net/2025/01/type-inference-in-rust-and-cpp/).

Personally, I like type inference (and [type classes](https://en.wikipedia.org/wiki/Type_class)), but I also like if types have a namespace attached to them, with methods and associated functions. I am pragmatic like that.

What I like about Rust is that it gives me the best out of both worlds here: You get traits and type inference without needing to wrap your head around a fully functional, immutable, lazy, monad-driven programming paradigm, and you get methods and associated values without the absolute dumpster fire of complex inheritance chains or AbstractBeanFactoryConstructors.

I’ve not seen any other language that even comes close to the convenience of Rust’s pipelines, and its lack of higher-kinded types or inheritance did not stop it. Quite the opposite, if anything.

Conclusion
----------

I like pipelining. That’s the one thing that definitely should be obvious if you’ve read all the way through this article.

I just think they’re neat, y’know?

I like reading my code top-to-bottom, left-to-right instead of from-the-inside-to-the-outside.

I like when I don’t need to count arguments and parentheses to figure out which value is the first argument of the second function, and which is the second argument of the first function.

I like when my editor can show me all fields of a struct, and all methods or functions associated with a value, just when I press `.` on my keyboard. It’s great.

I like when `git diff` and the `blame` layer of the code repository don’t look like complete ass.

I like when adding a function call in the middle of a process doesn’t require me to parse the whole line to add the closing parenthesis, and doesn’t require me to adjust the nesting of the whole block.

I like when my functions distinguish between ‘a main value which we are acting upon’ and ‘secondary arguments’, as opposed to treating them all as the same.

I like when I don’t have to pollute my namespaces with a ton of helper variables or free-standing functions that I had to pull in from somewhere.

If you’re writing pipelined code—and not trying overly hard to fit everything into a single, convoluted, nested pipeline—then your functions will naturally split up into a few pipeline chunks.

Each chunk starts with a piece of ‘main data’ that travels on a conveyer belt, where every line performs exactly one action to transform it. Finally, a single value comes out at the end and gets its own name, so that it may be used later.

And that is—in my humble opinion—exactly how it should be. Neat, convenient, separated ‘chunks’, each of which can easily be understood in its own right.

Idk, subscribe to my [newsletter](https://buttondown.com/mond) or something.

_Thanks to kreest for proofreading this article._

