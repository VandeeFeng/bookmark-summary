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
