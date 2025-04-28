---
title: Recognizing patterns in memory
date: 2025-04-28
extra:
  source: https://www.timdbg.com/posts/recognizing-patterns/
  original_title: Recognizing patterns in memory
---
## Summary
**摘要**：
作者分享了在调试过程中识别内存模式的经验，认为这对于发现如内存损坏等难以调试的错误非常有帮助。文章列举了几种常见的内存模式。首先是32位或64位对齐的数据，这些数据在内存中会呈现出特定的列模式。其次是指针，通过检查其高位部分是否为零可以快速识别。UTF-16编码的字符串也容易识别，通常表现为ASCII字符与空字节交替出现。此外，文章还介绍了如何识别x86和x64架构的代码，如通过`CC`字节（int 3指令）和`4X 8X`序列（REX前缀和ALU操作）来判断。最后，对于无法识别的、无明显对齐特征的数据，作者认为可能是高熵数据，通常是压缩或加密的数据，需要查找头部信息来进一步判断。作者希望通过这些技巧，读者可以开始训练自己识别内存模式，提升调试技能。

**要点总结**：

1.  **对齐的32/64位数据：** 许多文件格式和内存数据结构使用对齐的32位或64位数据。即使实际数值远小于分配的空间，也会进行对齐，从而在内存中形成特定的列模式。例如，每隔4个字节重复出现的模式，表明存在32位的值。

2.  **指针：** 指针是对齐数据的一个特例，通常很容易识别。在Windows用户模式进程中，有效的指针地址通常位于128TB的地址空间内（`0x0000'00000000`到`0x7FFF'FFFFFFFF`）。检查64位值的高16位是否全为零（例如，`0x0000XXXX'XXXXXXXX`），可以初步判断其是否为指针。可以使用`!address <address>`命令验证地址的有效性，`ln`命令查找最近的符号，`!heap`命令查找堆分配信息。

3.  **UTF-16字符：** UTF-16是一种常见的Windows文本编码，其特征是ASCII字符与空字节交替出现。在十六进制查看器中，UTF-16编码的字符串通常显示为在每隔一个字节后出现“空字符”。例如，字符串"Program Files"在UTF-16编码下会呈现出`00 00 43 00 3A 00 5C 00 50 00 72 00 6F 00 67 00`这样的模式。

4.  **代码字节：** 识别代码字节的模式有助于区分代码和数据。x86和x64代码通常没有严格的对齐，并且包含大量的`CC`字节（int 3指令，用于触发软件断点）和`C3`字节（ret指令，函数结尾）。在x64代码中，`4X`字节（REX前缀）也很常见，常用于访问更大的寄存器集，`4X 8X`序列通常表示基本的ALU操作或MOV操作。

5.  **高熵数据：** 高熵数据没有明显的对齐特征，也不包含可执行代码，通常是压缩或加密的数据。识别高熵数据需要查找头部信息或考虑程序可能处理的压缩或加密数据类型。如果发现小段高熵数据损坏了其他内存，需要考虑应用程序可能正在处理哪种类型的高熵数据，例如是否正在解压缩数据或通过网络传输加密数据。
## Full Content
Title: Recognizing patterns in memory

URL Source: https://www.timdbg.com/posts/recognizing-patterns/

Published Time: 2022-11-24T08:30:09-07:00

Markdown Content:
Something I find frustrating is how hard it is to teach debugging skills. I think the biggest reason is because there are many things that can only be learned through experience. This is true for anything that requires pattern recognition. Our brains are great at recognizing patterns, but it often takes a large amount of practice to be able to identify useful patterns in data.

I can’t instantly give you pattern recognition skills with a short blog post, but I can tell you about some of the patterns that I look for so you can start to train your brain to see these as well. Recognizing patterns in memory can be useful as it can give you a hint for things like memory corruption, which are often some of the hardest errors to debug from a postmortem analysis. Getting a rough idea of what type data is ovewriting other data in a process can tell you where to look next for the source of memory corruption. It can help narrow down where an issue might be because the bug is usually near the code that wrote this data.

Aligned 32/64-bit data
----------------------

A frequent pattern in both file formats and in-memory data structures is aligned 32-bit or 64-bit data. We often choose to use 32-bits for values that will never come close to filling the full space. Additionally, even when smaller data types are used, it’s common for these values to be aligned to 32-bit or 64-bit boundaries. In both cases, we see distinct patterns when most of the data is much smaller than the reserved space.

Take this memory dump for example:

```
09 00 00 00 30 43 00 00 0A 55 02 00 10 00 00 00
E0 49 01 00 2A 0B 01 00 06 00 00 00 A8 00 00 00
78 06 00 00 07 00 00 00 38 00 00 00 EC 00 00 00
0F 00 00 00 54 05 00 00 24 01 00 00 0C 00 00 00
F8 3A 00 00 32 D0 00 00 15 00 00 00 EC 01 00 00
A4 2A 00 00 16 00 00 00 98 00 00 00 90 2C 00 00
```

When viewing the data as 8 bytes or 16 bytes per line, columns show up with similar types of data. Column 0 is the least significant byte of a 4-byte field, and is all non-zero. Column 3 is most significant byte, and is all zeros because none of the values are larger than 24 bits. You can see a similar pattern across the other columns repeating every 4 bytes, so we can say with high confidence that there are a bunch of 32-bit values here.

Pointers
--------

A special case of aligned data is pointers. These are often very easy to spot. While a 64-bit pointer could span the entire address range, in reality they exist in a limited part of the address space in windows usermode processes. The virtual address space is [the 128-terabyte range 0x0000'00000000 through 0x7FFF’FFFFFFFF](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/virtual-address-spaces). As a result, one easy way to see if 64-bit value might be a pointer is checking if the high 16 bits are all zero. (e.g. in the form of `0x0000XXXX'XXXXXXXX`). To make things easier, the allocated virtual memory tends to be “clumped together” in a few clusters for most processes.

Take this stack dump for instance:

```
0:000> dp @rsp
000000d3`f213ef00  00000000`00000000 000000d3`f213ef90
000000d3`f213ef10  00000000`00000000 000000d3`f213ef90
000000d3`f213ef20  00000000`00000000 00000000`00000040
000000d3`f213ef30  00000000`00000010 00007ffc`690e3ff5
000000d3`f213ef40  00007ffc`69135a00 00007ffc`69135900
000000d3`f213ef50  00007ffc`69135900 00007ffc`69135900
000000d3`f213ef60  000000d3`f213f034 00007ffc`00000004
000000d3`f213ef70  00000000`00000000 00000000`00000000
```

You can see two patterns that stand out. There are a few 64-bit values that start with `00007ffc`, and a few that start with `000000d3`. The ones that start with `d3` are stack addresses, and you can see that from the fact that RSP starts with `d3` as well. (cross-thread stack references are rare, but stacks will often start with the same 32-bits). The `00007fXX` sequence is also very common, and is usually loaded modules. The stack and heap addresses are somewhat random, but unless an application has high memory consumption, there will probably be only a few of these that are valid within a process. You can see this by running `!address` in a process with no parameters.

The nice part is that if something “looks like” an address, it’s very easy to check if it actually is a valid address. Just run `!address <address>`, which will tell you if the address is valid in the current process. The odds of a 64-bit value being a pointer by chance is quite low.

Other useful commands to use with an arbitrary address include `ln` to find the closest symbol (for addresess inside a module) and `!heap` to find information about a heap allocation.

UTF-16 characters
-----------------

A common text encoding in Windows is UTF-16. This is usually very easy to recognize since most hex viewers will show you the ASCII representation of data, and UTF-16 encoding will usually look like ascii characters with “blank characters” every other byte, like this:

```
..C.:.\.P.r.o.g.
r.a.m. .F.i.l.e.
s.\.W.i.n.d.o.w.
```

Obviously UTF-16 could look much different if they were for localized strings in other languages, but it’s still very common to see strings where the characters are in the range of 0-127, where the interpretation overlap with the ASCII interpretation. (As a side note, I’ll mention that no matter how careful you are, you will always find someone who thinks you have used the incorrect terminology when it comes to text encoding)

If you are viewing just hex bytes, it’s nearly as easy to recognize:

```
00 00 43 00 3A 00 5C 00 50 00 72 00 6F 00 67 00
72 00 61 00 6D 00 20 00 46 00 69 00 6C 00 65 00
73 00 5C 00 57 00 69 00 6E 00 64 00 6F 00 77 00
```

Every other column will be full of zeros, and the other columns will generally be 20-7F.

Code bytes
----------

Each architecture is a bit different in the way that instructions are encoded. Most of my experience is with x86 and x64 code. It tends to be very easy to spot “normal” code that was generated by a compiler. Hand coded assembly can sometimes be harder to spot.

There are a few tricks to spotting x64 code quickly. Take this data for instance:

```
F0 01 00 00 5B C3 CC CC CC CC CC CC CC CC CC CC
48 83 EC 38 48 83 64 24 20 00 41 B9 01 00 00 00
4C 8D 44 24 40 41 8D 51 10 48 C7 C1 FE FF FF FF
E8 0B CC FC FF 85 C0 78 0A 80 7C 24 40 00 75 03
CC EB 00 48 83 C4 38 C3 CC CC CC CC CC CC CC CC
```

The first thing you’ll notice is the lack of alignment. X86 uses a variable length encoding, and there is generally not a reason to align code on 32-bit or 64-bit boundaries inside a function (although there is a reason to have 32-bit aligned addresses as the _start_ of a function or other jump target). The second thing you will notice is the abundance of `CC` bytes. This is the one byte encoding for the `int 3` instruction, which is the instruction used to trigger a software breakpoint. These are sometimes inserted in between functions to align the entry address of the next function. Using `CC` bytes means a misjump to these locations will trigger an immediate breakpoint exception instead of accidentally running some arbitrary part of code. So you’ll see these sequences of `CC` bytes, and they will always end at some aligned address. The other thing to notice about these sequences is that they usually start with a `C3` byte, which is single byte encoding for a `ret` instruction, which is very frequently (but not always) the last instruction of a function.

These tricks work very well for binaries that are part of Windows, as the compiler options used means these sequences will nearly always show up. Other compilers and compiler options won’t have these. Or you may be looking at a small part of a larger function. For this, there are some other tricks I use. Take this code for instance:

```
41 54 55 57 56 53 48 83 EC 20 48 8B 35 CF 73 1F
00 85 D2 48 89 CF 89 D3 4C 89 C5 89 16 75 54 8B
05 5B 1D 21 00 85 C0 74 33 E8 A2 52 17 00 49 89
E8 31 D2 48 89 F9 E8 75 63 17 00 49 89 E8 89 DA
```

Two patterns I’ll direct your attention to. The first is the sequence `54 55 57 56 53`. It doesn’t look completely random, and in fact there is a reason why there are a bunch of bytes in the 50-57 range. These are all single byte “push” instructions. In fact, anything starting with a 5 is either a push or a pop instruction. These often show up in a sequence because push and pop instructions can be found clustered at the start and end of a function. The other thing to notice is that there are a bunch of `4X` bytes in this sequence. These are very common in x64 code because they are a prefix byte used to access the larger register set available in x64 compared to x86 (called the REX prefix). It’s possible to see a `4X` byte in the middle of an instruction and not acting as a prefix, of course, but more often than not this will mark the beginning of an instruction. If you see a `4X` byte followed by an `8X` byte, it’s very likely a basic ALU operation or `MOV` operation. These represent a very large percent of most code. Just look through disassembly for any function and you will likely see a lot of `8X` or `4X 8X` sequences at the start of instructions.

You can always use a disassembler to test this theory and see if the instructions “look” right, but determining what looks right would could be a blog post of its own.

High entropy data
-----------------

If you have something that doesn’t show any obvious signs of alignment, and doesn’t have any executable code, it’s possible that you’re looking at some high entropy data. Take this sequence:

```
02 4D 1C 07 18 CF 3F 2B F4 B0 50 F8 D9 6E 1D 91
83 4E DF 75 D0 BE B2 D2 9F AC 79 18 C4 67 A5 A0
47 04 EF F4 85 A0 53 8C 52 90 84 4C B7 22 4B C5
```

Here we see no obvious alignment, no sequences of `CC`, no occurrences of `C3`, and no sequences of `4X 8X`. High entropy data could be any number of things, but it almost always falls into one of two categories:

1.  Compressed data
2.  Encrypted data

Without more context, it’s generally not possible to identify the format of high entropy data or even to determine if a sequence of bytes is compressed or encrypted. There are probably some cases where you can find some data structures embedded for compressed data (like data about video frames for instance), but given that the compressed portion will usually be larger than the fixed layout structures, it will usually take more work to find. The best bet here is to try to find a header for the data, and see if there is some signature that tells you more. But if there’s just a small snippet of high entropy data corrupting some other memory, you may want to consider what sort of high entropy data the application could be dealing with (could it be decompressing data? transmitting encrypted data over a network?)

Conclusion
----------

The idea of recognizing a sequences of bytes and finding the meaning behind them has always felt very satisfying to me. Have you ever found this useful? Do you have any tricks of your own? Let me know on [Twitter](https://twitter.com/timmisiak) or [Mastodon](https://dbg.social/@tim)!

