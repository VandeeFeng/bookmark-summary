---
title: Driving Compilers
date: 2025-05-04
extra:
  source: https://fabiensanglard.net/dc/index.php
  original_title: Driving Compilers
---
## Summary
**摘要**：  
本文作者回忆了学习编程语言与编译工具的对比经历，指出大多数语言教材仅提供基础示例却缺乏编译过程的深度解析，导致学习者在面对复杂编译错误时无从下手。文章系列旨在填补这一知识空白，通过详细解释可执行文件生成的核心概念，帮助读者理解编译器、链接器等工具的工作流程。作者强调将结合实际操作步骤与工具链分析，覆盖Linux、macOS、Windows等平台的等效工具，并按编译驱动、预处理、编译、链接、加载器五大模块展开，旨在提供系统性知识框架和实用工具使用指南。

**要点总结**：  
1. **学习资源失衡**：编程语言教材普遍聚焦语法与库函数，但缺乏对编译工具链的系统讲解，导致学习者在遇到链接错误（如LNK2019）时缺乏解决思路。  
2. **知识填补目标**：本文系列不教授语言语法或编译器实现，而是聚焦于解释如何通过工具链将源代码转化为可执行文件，提供可复现的实践步骤。  
3. **平台工具链对比**：列举Linux、macOS、Windows等平台的编译器驱动（gcc/clang/CL.EXE）、目标格式及库类型差异，强调跨平台概念一致性。  
4. **编译流程分层解析**：按编译器驱动、预处理（cpp）、编译（cc）、链接（ld）及加载器五大阶段拆解，明确各阶段输入输出与核心功能。  
5. **工具与理论结合**：通过-bintools与详细日志（-v）等实操手段，结合理论框架，帮助读者构建从源码到可执行文件的完整认知地图。
## Full Content
Title: Driving Compilers

URL Source: https://fabiensanglard.net/dc/index.php

Markdown Content:
DRIVING COMPILERS

By Fabien Sanglard
May 3rd, 2023


Mistake - Suggestion
Feedback

INTRODUCTION
 →

I remember how pleasant it was to learn to program in C. There were so many good books explaining not only the language but also the standard library. I devoured both The C Programming Language (K&R) by Kernighan/Ritchie and The Standard C Library by P.J. Plauger. Then came Expert C Programming by Van der Linden and finally C: A Reference Manual by Harbison and Steele.

It was an equally enjoyable experience when I took on C++. I found myself unable to put down the Effective C++ series by Scott Meyers. I loved the simple layout and the astute usage of red text for emphasis. I must have read half the first volume while standing in Toronto World's Biggest Bookstore before I left with the complete series under my arm. I remember power walking to my place to keep on reading.

A contrasting experience was to learn how to use the tools to turn my programs into executable. It was a painfully slow and deeply unpleasant process where knowledge was gathered here and there after trial, errors, and a lot of time spent on search engines. It felt like acquiring the same level of comfort to use a compiler took significantly more than learning the language.

I blame this experience on the lack of literature on the topic. Most language books start with a "Hello World" code sample. In the case of K&R, it would be hello.c.

#include <stdio.h>

int main()
{
    printf("hello, world\n");
} 

The reader is given the command to convert that text file into an executable and it is the last time they will hear about how to use the compiler.

$ cc hello.c
$ ./a.out
hello, world

This is the gap this series attempts to fill. It won't teach about a language, its libraries, or an SDK. It won't teach how to write a compiler or a linker either. These articles are meant to ease leaving the world of one-file examples. It is a pot-pourri of the things I wish I had known when I was pulling my hair over mysterious LNK2019 and other LNK4002 errors.

Here will be explained the core concepts associated with the creation of an executable. As much as possible claims will be backed up with reproducible steps relying on bintools and driver verbose mode (-v). The goal is to provide the readers with both the tools and a mental map to explore beyond the charted territories of these pages.

Note: Some liberties were taken with command invocation outputs for typesetting purposes. Commands such as clang -v generate a lot more than what is actually printed here. The uninteresting parts were removed to only keep what is relevant to the topic at hand. Rest assured that no command-line tools were hurt during the making of this text.

Environment

The examples assume a Linux platform. Depending on which illustrate the topic better, gcc or clang compiler drivers are used. If you are using Mac OS X or Windows, the ideas and concepts should be similar. Here is a table of equivalencies.

Platform	Driver	Object format	Dynamic library	Static library	Executable
Linux	gcc	elf	library.so	library.a	elf
Mac OS X	clang	macho	library.dylib	library.a	macho
Windows	CL.EXE	COFF	library.dll	library.lib	PE

The platform / toolchain association is the one most often encountered but they may vary. For example, clang is available on all platforms and gcc is available on Windows via cygwin.

Structure
1. driver	
2. cpp	3. cc	4. ld	5. loader

This series is divided into five parts. First is explained the component which rules them all, the compiler driver (1). Then we drill into the three stages of the compilation pipeline, detailing their inputs/outputs. The pre-processor (2), cpp, converts source code files into translation units (TU), is covered first. Then comes the compiler cc (3), which ingests TUs and outputs relocatable (object) files. Then we look at the element combining all objects together into and executable, the linker ld (4).

In the fifth and final part we take a look at the linux loader (also called ld) (5) to further understand the linker output.

NEXT

The Compiler Driver (1/5)

*

