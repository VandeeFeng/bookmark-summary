---
title: A Modern XPath and XSLT Engine in Rust
date: 2025-03-29
extra:
  source: https://blog.startifact.com/posts/xee/
  original_title: A Modern XPath and XSLT Engine in Rust
---
## Summary
**摘要**：
本文介绍了作者在过去两年里用Rust编写的名为Xee的XML执行引擎，它支持现代版本的XPath和XSLT。XPath是一种XML查询语言，而XSLT是一种可以将XML文档转换为其他文档的语言，它以XPath作为其表达式语言。Xee旨在为Rust以及其他编程语言提供现代XML技术，甚至可以编译为WASM在浏览器中运行。文章回顾了XML的发展历程，虽然XML不像2000年初那样流行，但它仍然被广泛使用。作者提到，Java领域有很好的XPath和XSLT支持，但开源领域中，`libxml2`和`libxslt`仍停留在XPath 1.0和XSLT 1.0版本。Xee的出现是为了提供一个更现代的替代方案。Xee的架构遵循常见的编程语言实现模式，包括词法分析、语法分析、生成抽象语法树（AST）、转换为中间表示（IR）以及编译成字节码。XPath和XSLT是完全指定的编程语言，因此Xee的实现需要遵循大量的规范。目前，Xee在XPath 3.1的实现上取得了很大进展，大部分标准库已经实现，并通过了大量的兼容性测试。作者希望有人能参与到Xee项目中，共同为XML的未来贡献力量。

**要点总结**：

1.  **Xee是一个用Rust编写的现代XML执行引擎，支持XPath和XSLT。** XPath是用于查询XML文档的语言，而XSLT则用于转换XML文档的语言，Xee旨在提供这些技术的现代实现，并将其引入Rust生态系统。
2.  **XML技术仍然重要，但现有的开源实现（如`libxml2`和`libxslt`）已经过时。** 尽管XML的热度不如以前，但它仍在许多领域发挥作用。然而，许多现有的开源库只支持旧版本的XPath和XSLT，Xee旨在填补这一空白，提供对最新标准的支持。
3.  **Xee的架构基于常见的编程语言实现模式，包括词法分析、语法分析、中间表示和字节码解释器。** Xee通过将XPath和XSLT代码转换为字节码，然后使用解释器执行这些字节码来实现其功能。这种架构允许进行优化，并支持未来的扩展。
4.  **XPath和XSLT是完全指定的编程语言，这意味着Xee的开发需要遵循大量的规范。** 遵循规范既带来了清晰的目标，也意味着需要投入大量精力来实现所有规定的功能。XPath 3.1和XSLT 3.0规范非常庞大，包含了大量的特性和标准库函数。
5.  **Xee在XPath 3.1的实现上已经取得了显著进展，但仍有许多工作要做，作者呼吁社区贡献。** Xee已经通过了大量的XPath 3.1兼容性测试，这表明其实现的质量很高。然而，仍有一些标准库函数尚未实现，XSLT的实现也需要进一步完善。作者希望能够吸引更多的开发者参与到Xee项目中，共同推动XML技术的未来发展。

## Full Content
Title: Xee: A Modern XPath and XSLT Engine in Rust

URL Source: https://blog.startifact.com/posts/xee/

Markdown Content:
For the last two years I've been working on a programming language implementation in Rust named Xee. Xee stands for "XML Execution Engine" and it supports modern versions of XPath and XSLT. Those are programming languages, and yes, that's XML stuff.

Now hold on. Your brain might shut down when I talk about XML. I totally get that XML may not be your cup of tea. But I'm also going to be talking about a strange different world of technology where everything is specified, and the implementation of a programming language using Rust, so I hope you still decide to read on if those topics could interest you.

And if XML _does_ happen to be your cup of tea, I think you should be excited about Xee, as I think it can help secure a better future for XML technologies.

Here's the [Xee repository](https://github.com/Paligo/xee).

There are two highlights: a command-line tool [`xee`](https://github.com/Paligo/xee/?tab=readme-ov-file#obtaining-the-xee-commandline-tool) that lets you do XPath queries, and a Rust library [`xee-xpath`](https://docs.rs/xee-xpath/latest/xee_xpath/) to issue XPath queries from Rust.

[](https://blog.startifact.com/posts/xee/#genesis)Genesis
---------------------------------------------------------

In 2023 I was asked by [Paligo](https://paligo.net/), my amazing and generous client, whether I wanted to implement a modern version of XPath and XSLT in Rust. I felt extremely nervous for a week. Then I told them that this was a big project. I told them that I could do it and I was excited to do it, but it was going to be a _lot_ of work.

And although I was right to be very intimidated by the scope, I _still_ underestimated the effort at the time.

But Xee has come a long way nonetheless! I'm going to take you along on its journey if you're willing to follow.

[](https://blog.startifact.com/posts/xee/#what-is-xee)What is Xee?
------------------------------------------------------------------

Xee is a programming language implementation. It implements two core XML programming languages: [XPath](https://en.wikipedia.org/wiki/XPath) and, partially at the time of writing, [XSLT](https://en.wikipedia.org/wiki/XSLT). XPath is an XML query language, and XSLT is a language that uses XPath as its expression language which lets you transform XML documents into other documents. Xee implements _modern_ versions of these specifications, rather than the versions released in 1999.

Xee implements these languages in the Rust programming language. This brings modern XML technology not just to Rust. Rust is a systems programming language and is good at integration with other programming languages. So Xee can bring its capabilities to other programming languages as well, from PHP to Python. I've already experimented with [PHP bindings](https://github.com/Paligo/xee-php).

Since Xee is written in Rust, it should also be possible to compile the Xee interpreter to WASM and run this stuff in the browser.

I'll continue to talk about how Xee is implemented later, but first we'll take a break and share some XML history.

[](https://blog.startifact.com/posts/xee/#xml-history)XML history
-----------------------------------------------------------------

Let's talk a bit about XML. XML emerged in the late 90s, and though it may be difficult to believe now, for a while in the early part of the 2000s, XML was a cool technology everyone wanted to use. There was much excitement in the form of industry activity and many computer science papers were also published.

To illustrate how big this was, last year I was at the RustNL conference and I spoke to _two separate speakers_ who mentioned they had worked on an XSLT engine[1](https://blog.startifact.com/posts/xee/#different) in the past. One of them was [Niko Matsakis](https://smallcultfollowing.com/babysteps/), Rust core developer.

So me being a young and hip developer back then [2](https://blog.startifact.com/posts/xee/#hip), I was doing cool XML stuff too. My biggest accomplishment in the XML space was the creation of [lxml](https://lxml.de/), the XML library for Python. I started that project in late 2004. Early on [Stefan Behnel](http://consulting.behnel.de/index.en.html) joined the project and he has competently maintained it ever since - it would not have been as successful without him.

While XML technology isn't cool anymore today, it's still everywhere. The core language web browsers use is not XML but its close cousin HTML. Embedded in HTML are true XML-based languages, such as SVG and MathML. Even though JSON and other languages took a large chunk out of it, XML is still used to store and transmit a lot of data, and it's extensively used for documents as well, in formats such as docbook and JATS. XML is now niche technology, but it's a bigger niche than you might think, and it's not going to go away any time soon.

In my own career, I became less and less involved with XML over time, though I'd still run into it on a regular basis. It's both amusing and useful that whenever I talk to a potential client that uses Python, they're already using lxml somewhere.

A few years ago I entered back into the XML world. And here I am, that relatively rare bird who knows a fancy modern programming language like Rust, and is at the same time very familiar with XML.

[](https://blog.startifact.com/posts/xee/#xpath-and-xslt-are-programming-languages)XPath and XSLT are programming languages
---------------------------------------------------------------------------------------------------------------------------

So XPath and XSLT are both programming languages.

XPath is a query language for XML. Given an XML document, let's say something like HTML, you can query it with expressions like: `/html/body//p` to get all `p` elements inside the `body` element of the outer `html` element. XPath in its modern incarnation is a functional programming language with a type system, variables, function definition, conditionals, loops and so on.

XSLT is a transformation language for XML. It describes, using templates and a functional approach, how to transform an XML document of one type into another. You can for instance use it to transform docbook XML, which describes documents, into HTML. It builds on XPath - XPath expressions are the expression language of XSLT. XSLT itself _also_ supports programming constructs like variables, loops, conditionals, functions and the like, in a partial duplication of XPath.

[](https://blog.startifact.com/posts/xee/#state-of-the-xml-open-source-stack)State of the XML open source stack
---------------------------------------------------------------------------------------------------------------

So if you want to use these programming languages and you use an open source stack, where do you go?

The Java world has good modern XPath and XSLT support. XPath and XSLT are implemented by Saxon, which has been around for a long time. Saxon is available on .NET as well. There are also PHP and Python bindings via a rather complex C to Java bridge, and Saxon offers a JavaScript reimplemention of its runtime as well. Besides its open source offerings, Saxon also has closed-source professional/enterprise editions which provide more features. Besides Saxon, there are also open source XQuery[3](https://blog.startifact.com/posts/xee/#xquery) implementations in Java.

But if you step out of the Java world and its periphery, and if you look in your average open source stack or Linux distribution for an XPath or XSLT implementation you don't find Saxon or these XQuery databases; you find `libxml2` and `libxslt`.

`libxml2` and `libxslt` are C libraries for handling XML. This amalgam of libraries supports parsing XML, querying it using XPath, transforming it using XSLT and more. `libxml2` is everywhere - in your Linux distribution and in MacOS. People don't just use it from C code - for Python for instance I built `lxml` on top.

These libraries were originally created by [Daniel Veillard](http://veillard.com/). I remember speaking to him once, many years ago. We came from different worlds - he was thinking about writing fast processor-cache friendly code in C, whereas I was interested in an easy to use API in Python. I was impressed he had implemented all these specifications - `lxml` was merely piggybacking on that hard work.

But `libxml2` is stuck in the past - it implements XPath, but only XPath 1.0, and similarly `libxslt` implements XSLT 1.0 only. These are specifications from 1999. The XPath 2 specification was released in 2007, and we're currently actually at XPath 3.1, released in 2017. Similarly XSLT 2.0 was released in 2007 and XSLT 3.0, the current version, in 2017.

My hope is that Xee can be a more modern alternative to `libxml2` and `libxslt` that finds its home in the open source world. For XPath and XSLT to be thriving standards they need multiple implementations, in multiple programming languages, by multiple parties.

And personally I feel like I have come full circle - finally, in these latter days of XML, I am where Daniel Veillard had gone ages before with `libxml2`. I find myself implementing the same stuff, not in C, but still in a systems programming language, Rust.

[](https://blog.startifact.com/posts/xee/#specification-culture)Specification culture
-------------------------------------------------------------------------------------

I was at [XML Prague](https://www.xmlprague.cz/), an XML conference, last year, and I noticed something interesting about XML culture. It is still very standards focused. This was a very prevalent attitude in the web development world in the early 2000s, but I think that although standards are still considered important today, they're less culturally prominent.

The XML culture is different: stuff needs to be specified. If it's not in a specification it's not fully _real_. This makes the XML community move more slowly than the rest of the software community. I was somewhat bemused to hear talk in 2024 about updating the RESTXQ spec, an XQuery based web framework standard, first discussed in 2012, to make use of language features like hashmaps and arrays, now that they had been finally added to XPath/XQuery in 2017.

These XML specifications go deep, they build on each other, they are solid. If you value solid foundations that will stand the test of time, the XML world has got your back.

[](https://blog.startifact.com/posts/xee/#implementing-a-programming-language)Implementing a programming language
-----------------------------------------------------------------------------------------------------------------

You might be bored with XML by now so before I return to the discussion of specifications, I will talk a bit about the architecture of Xee.

Xee follows various familiar patterns in the implementation of programming languages. I based part of its architecture on the excellent book [Crafting Interpreters](https://craftinginterpreters.com/).

In Xee, XPath gets lexed into tokens, then parsed into an abstract syntax tree (AST). The AST is then transformed into an intermediate representation (IR) that represents the expression in a more compact way. This IR is then compiled into bytecode - a simple assembly-language like stack machine, similar to the one that underlies many programming languages such as Python and Java. The Xee interpreter can then execute the bytecode.

This translation at present is straightforward; while I've prepared the IR to support optimization passes such as constant folding and the like, this doesn't happen yet.[4](https://blog.startifact.com/posts/xee/#optimization)

XSLT, though unfinished, is built on the same architecture as the XPath engine. There's a frontend that transforms XSLT XML into an XSLT AST, and then this is transformed into the same IR as the one used for XPath. It uses the same bytecode intepreter. So, only the XSLT frontend is different, everything else is the same. This made it easy to implement a whole bunch of XSLT features as I had already implemented them for XPath.

Implementing programming languages is fun!

[](https://blog.startifact.com/posts/xee/#specifications-again)Specifications, again
------------------------------------------------------------------------------------

XPath and XSLT are programming languages that are fully specified. You can really implement them from the specification. On the one hand this makes life a lot easier - the goals are clear as it's clearly specified how things are supposed to work. There's a vast conformance test suite available as well. On the other hand this means an endless treadmill; I can't just stop when I think it looks good enough when there's more specification left to implement.

XPath 3.1 has grown a _lot_ bigger than XPath 1.0; it became a full-fledged programming language, with a much larger standard library. XSLT 3.0 has also evolved a lot since XSLT 1.0. Specifications keep building on each other, and add more features in new updates, until implementing them becomes a daunting task. I sometimes I wish I was implementing XPath 1.0 and XSLT 1.0, like Daniel Veillard back in the day.

Let me give you a quick tour of various specifications so you can understand something about the magnitude of the task of implementing them.

The grammar and behavior of the XPath language is laid out in the W3C specification [XML Xpath Language (XPath) 3.1](https://www.w3.org/TR/xpath-31/). This refers to another specification, [XQuery and XPath Data Model 3.1](https://www.w3.org/TR/xpath-datamodel-31/) which describes how XPath views XML data - what properties of XML data exist. It also builds on another specification [XPath and XQuery Functions and Operators 3.1](https://www.w3.org/TR/xpath-functions-31/), which not only describes the behavior of XPath operators such as `+`, `-` and `*`, but also defines its standard library of functions.

XPath has a type system, and its types are described by [W3C XML Schema Definition Language (XSD) 1.1: Part 1: Structures](https://www.w3.org/TR/xmlschema11-1/) and [W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes](https://www.w3.org/TR/xmlschema11-2/). This defines atomic types (which Xee implements) but also lets you define new types and use types from an XML schema, which Xee doesn't implement at present. These specifications also describe how XPath is to parse and format strings of atomic types, such as the format of decimals and dates.

Oh, and that XPath functions and operators specification? Some of the functions use regular expressions. The specification defines XPath regular expressions as an extension of the regular expressions system defined in the XML schema specification. And all of that builds on the unicode specification but that's another country. So I ended up implementing [a regex engine](https://github.com/Paligo/regexml/) too.

Over to XSLT. There's [XSL Transformations (XSLT) Version 3.0](https://www.w3.org/TR/xslt-30/) which defines the XSLT programming language. It builds on all the specifications that went before, and also builds on [XSLT and XQuery Serialization 3.0](https://www.w3.org/TR/xslt-xquery-serialization-30/), which describes options for how to serialize XML and various other things.

Of course all of this builds on the XML specification itself, [Extensive Markup Language (XML) 1.0 (Fifth Edition)](https://www.w3.org/TR/xml/), extended with namespaces, in [Namespaces in XML 1.0](https://www.w3.org/TR/REC-xml-names/).

Then there are a few stray specifications that are also relevant like [XML Base](https://www.w3.org/TR/xmlbase/) and [xml:id](https://www.w3.org/TR/xml-id/). But those are small ones.

Once I counted up the page count[5](https://blog.startifact.com/posts/xee/#pdf) of just the XPath and XSLT specifications along with the most relevant XML Schema spec (part 2), and that subset is over 1800 pages.

I probably forgot a few specifications, because after a while they start coming out of my ears, but this should give you an impression.

[](https://blog.startifact.com/posts/xee/#xee-status)Xee status
---------------------------------------------------------------

What I'm most proud of is the XPath 3.1 implementation in Xee. The XPath core language and most of its standard library have been implemented. There are gaps in the standard library implementation still - some formatting functions are particularly huge, for instance, but overall it's pretty complete.

There's an XPath 3.1 conformance test suite, and of the 21859 tests, 20130 tests are passing at the time of writing. Most of the failing tests have to do with the implementation of missing standard library functionality.

Incidentally, this test suite runs those 20130 tests in 13 seconds on my machine. Computers are fast.

Meanwhile Xee also provides a solid basis for XSLT, reusing a lot of the XPath infrastructure. While a lot of XSLT works, much remains to be done and I'm hoping to find people who want to help contribute!

[](https://blog.startifact.com/posts/xee/#a-call-for-contributors)A call for contributors
-----------------------------------------------------------------------------------------

So now I will call for this rare bird: someone who read all this, saw all those XML specifications, knows a bit of Rust, likes implementing programming languages and thought: cool! I want to help!

*   Do you like the challenge of implementing some functionality, small or large, according to spec? Xee has plenty of tasks for you.
    
*   Are you interested in programming language implementation? Perhaps do cool programming language optimization work? For a programming language that has an existing user base already? Xee has the foundations.
    
*   Do you like to think about query optimization problems? Care about using [succinct](https://blog.startifact.com/posts/succinct/) data structures? (not integrated into Xee proper yet). We have plenty of what should interest you.
    
*   Do you care about the future of XML and want to ensure a modern open source implementation is available outside of the Java world?
    

The Xee project could use your help and is ready for it. Small and large contributions are possible and welcome!

2

I'm still hip. I say so. Even though I do XML stuff.

1

Not the same XSLT engine. Different ones!

3

XQuery is a superset of XPath.

4

So you're interested in working on programming language optimization you've come to the right place!

5

I printed each specification HTML page to PDF to see how many pages they were.

