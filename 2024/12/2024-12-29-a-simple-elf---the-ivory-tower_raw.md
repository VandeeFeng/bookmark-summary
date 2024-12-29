Title: A Simple ELF - The Ivory Tower

URL Source: https://4zm.org/2024/12/25/a-simple-elf.html

Markdown Content:
Let's write a simple program for Linux. How hard can it be? Well, simple is the opposite of complex, not of hard, and it is surprisingly hard to create something simple. What is left when we get rid of the complexity from the standard library, all the modern security features, debugging information, and error handling mechanisms?

•  •  •

Let's start with something complex:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-0-1)#include <stdio.h>
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-0-2)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-0-3)int main() {
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-0-4)    printf("Hello Simplicity!\n");
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-0-5)}
```

Wait, what?! It doesn't look very complex, does it... Hmm, let's compile it and take a look:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-1-1)$ gcc -o hello hello.c
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-1-2)$ ./hello
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-1-3)Hello Simplicity!
```

Still looks pretty simple, right? Wrong! While this might be familiar territory and _easy_ to comprehend, the program is far from _simple_. Let's take a look behind the curtain.

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-1)$ objdump -t hello
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-2)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-3)hello:     file format elf64-x86-64
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-4)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-5)SYMBOL TABLE:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-6)0000000000000000 l    df *ABS*  0000000000000000              Scrt1.o
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-7)000000000000038c l     O .note.ABI-tag  0000000000000020              __abi_tag
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-8)0000000000000000 l    df *ABS*  0000000000000000              crtstuff.c
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-9)0000000000001090 l     F .text  0000000000000000              deregister_tm_clones
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-10)00000000000010c0 l     F .text  0000000000000000              register_tm_clones
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-11)0000000000001100 l     F .text  0000000000000000              __do_global_dtors_aux
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-12)0000000000004010 l     O .bss   0000000000000001              completed.0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-13)0000000000003dc0 l     O .fini_array    0000000000000000              __do_global_dtors_aux_fini_array_entry
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-14)0000000000001140 l     F .text  0000000000000000              frame_dummy
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-15)0000000000003db8 l     O .init_array    0000000000000000              __frame_dummy_init_array_entry
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-16)0000000000000000 l    df *ABS*  0000000000000000              hello.c
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-17)0000000000000000 l    df *ABS*  0000000000000000              crtstuff.c
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-18)00000000000020f8 l     O .eh_frame  0000000000000000              __FRAME_END__
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-19)0000000000000000 l    df *ABS*  0000000000000000
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-20)0000000000003dc8 l     O .dynamic   0000000000000000              _DYNAMIC
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-21)0000000000002018 l       .eh_frame_hdr  0000000000000000              __GNU_EH_FRAME_HDR
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-22)0000000000003fb8 l     O .got   0000000000000000              _GLOBAL_OFFSET_TABLE_
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-23)0000000000000000       F *UND*  0000000000000000              __libc_start_main@GLIBC_2.34
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-24)0000000000000000  w      *UND*  0000000000000000              _ITM_deregisterTMCloneTable
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-25)0000000000004000  w      .data  0000000000000000              data_start
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-26)0000000000000000       F *UND*  0000000000000000              puts@GLIBC_2.2.5
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-27)0000000000004010 g       .data  0000000000000000              _edata
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-28)0000000000001168 g     F .fini  0000000000000000              .hidden _fini
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-29)0000000000004000 g       .data  0000000000000000              __data_start
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-30)0000000000000000  w      *UND*  0000000000000000              __gmon_start__
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-31)0000000000004008 g     O .data  0000000000000000              .hidden __dso_handle
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-32)0000000000002000 g     O .rodata    0000000000000004              _IO_stdin_used
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-33)0000000000004018 g       .bss   0000000000000000              _end
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-34)0000000000001060 g     F .text  0000000000000026              _start
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-35)0000000000004010 g       .bss   0000000000000000              __bss_start
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-36)0000000000001149 g     F .text  000000000000001e              main
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-37)0000000000004010 g     O .data  0000000000000000              .hidden __TMC_END__
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-38)0000000000000000  w      *UND*  0000000000000000              _ITM_registerTMCloneTable
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-39)0000000000000000  w    F *UND*  0000000000000000              __cxa_finalize@GLIBC_2.2.5
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-2-40)0000000000001000 g     F .init  0000000000000000              .hidden _init
```

That's a lot of symbols! Actually, as far as symbol tables go, this one is quite modest. Any non-trivial program will have many more symbols, but still, what are they all for? We're just printing a string!

We recognize our `main` function in the `.text` segment at address `0x1149`. But where is the `printf` function?

It turns out that for simple cases, where there is no formatting work required by `printf`, GCC optimizes the code and replaces it with the simpler `puts@GLIBC_2.2.5` from libc. The address is all zeros since the symbol is undefined (`*UND*`). It will be resolved when the program is loaded together with the dynamic libc.so library as we run it.

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-3-1)0000000000001149 g     F .text  000000000000001e              main
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-3-2)0000000000000000       F *UND*  0000000000000000              puts@GLIBC_2.2.5
```

Let's keep digging. What sections are there in the program? The only data we have is the hardcoded string and its length. Surely we only need a `.text` section? Let's see what we got:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-1)$ objdump -h hello
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-2)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-3)hello:     file format elf64-x86-64
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-4)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-5)Sections:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-6)Idx Name          Size      VMA               LMA               File off  Algn
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-7)  0 .interp       0000001c  0000000000000318  0000000000000318  00000318  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-8)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-9)  1 .note.gnu.property 00000030  0000000000000338  0000000000000338  00000338  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-10)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-11)  2 .note.gnu.build-id 00000024  0000000000000368  0000000000000368  00000368  2**2
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-12)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-13)  3 .note.ABI-tag 00000020  000000000000038c  000000000000038c  0000038c  2**2
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-14)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-15)  4 .gnu.hash     00000024  00000000000003b0  00000000000003b0  000003b0  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-16)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-17)  5 .dynsym       000000a8  00000000000003d8  00000000000003d8  000003d8  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-18)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-19)  6 .dynstr       0000008d  0000000000000480  0000000000000480  00000480  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-20)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-21)  7 .gnu.version  0000000e  000000000000050e  000000000000050e  0000050e  2**1
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-22)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-23)  8 .gnu.version_r 00000030  0000000000000520  0000000000000520  00000520  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-24)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-25)  9 .rela.dyn     000000c0  0000000000000550  0000000000000550  00000550  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-26)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-27) 10 .rela.plt     00000018  0000000000000610  0000000000000610  00000610  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-28)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-29) 11 .init         0000001b  0000000000001000  0000000000001000  00001000  2**2
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-30)                  CONTENTS, ALLOC, LOAD, READONLY, CODE
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-31) 12 .plt          00000020  0000000000001020  0000000000001020  00001020  2**4
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-32)                  CONTENTS, ALLOC, LOAD, READONLY, CODE
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-33) 13 .plt.got      00000010  0000000000001040  0000000000001040  00001040  2**4
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-34)                  CONTENTS, ALLOC, LOAD, READONLY, CODE
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-35) 14 .plt.sec      00000010  0000000000001050  0000000000001050  00001050  2**4
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-36)                  CONTENTS, ALLOC, LOAD, READONLY, CODE
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-37) 15 .text         00000107  0000000000001060  0000000000001060  00001060  2**4
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-38)                  CONTENTS, ALLOC, LOAD, READONLY, CODE
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-39) 16 .fini         0000000d  0000000000001168  0000000000001168  00001168  2**2
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-40)                  CONTENTS, ALLOC, LOAD, READONLY, CODE
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-41) 17 .rodata       00000011  0000000000002000  0000000000002000  00002000  2**2
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-42)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-43) 18 .eh_frame_hdr 00000034  0000000000002014  0000000000002014  00002014  2**2
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-44)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-45) 19 .eh_frame     000000ac  0000000000002048  0000000000002048  00002048  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-46)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-47) 20 .init_array   00000008  0000000000003db8  0000000000003db8  00002db8  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-48)                  CONTENTS, ALLOC, LOAD, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-49) 21 .fini_array   00000008  0000000000003dc0  0000000000003dc0  00002dc0  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-50)                  CONTENTS, ALLOC, LOAD, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-51) 22 .dynamic      000001f0  0000000000003dc8  0000000000003dc8  00002dc8  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-52)                  CONTENTS, ALLOC, LOAD, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-53) 23 .got          00000048  0000000000003fb8  0000000000003fb8  00002fb8  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-54)                  CONTENTS, ALLOC, LOAD, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-55) 24 .data         00000010  0000000000004000  0000000000004000  00003000  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-56)                  CONTENTS, ALLOC, LOAD, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-57) 25 .bss          00000008  0000000000004010  0000000000004010  00003010  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-58)                  ALLOC
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-59) 26 .comment      0000002b  0000000000000000  0000000000000000  00003010  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-4-60)                  CONTENTS, READONLY
```

Ok, so that's definitely complex. It's not just a simple `.text` section. There are a LOT of them.

This is too much to deal with right now. Where does the program even start? It starts with `main`, right? Wrong again!

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-5-1)$ objdump -f hello
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-5-2)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-5-3)hello:     file format elf64-x86-64
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-5-4)architecture: i386:x86-64, flags 0x00000150:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-5-5)HAS_SYMS, DYNAMIC, D_PAGED
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-5-6)start address 0x0000000000001060
```

The "start address" (also known as the entry point), is `_start`, not `main`. This mystery function at `0x1060` must call our `main` somehow, but where does it come from!?

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-6-1)0000000000001060 g     F .text  0000000000000026              _start
```

Let's start simplifying the program. As we peel off complexity, we will get a chance to focus on understanding a few things at a time.

Life without libc
-----------------

A major source of complexity in our program comes from the standard libraries. They are used for printing the string and initializing the program. Let's get rid of them.

Easy enough, just compile with: `-nostdlib`.

Unfortunately, that means we no longer have access to the `printf` (or the `puts`) function. That's unfortunate since we still want to print "Hello Simplicity!".

It also means we will lose the `_start` function. It is provided by the C runtime library (CRT) to perform some initialization (like clearing the `.bss` segment) and call our `main` function. Since we still need our `main` to be executed, we will have to do something about that.

Fortunately, we can provide our own entry point with `-Wl,-e,<function_name>`. We _could_ specify `main` as our entry point directly, but that would mean treating it as `void main()` instead of `int main()`. The entry point doesn't return anything. I feel that changing the signature of `main` is one bridge too far; let's instead create our own `void startup()` function that calls `main`.

For writing to `stdout`, we resort to the `syscall` assembly instruction. This instruction is how we ask the Linux kernel to do things for us. In this particular case, we would like to execute the `write` syscall to write a string to `stdout` (file descriptor = 1). Later on, we also want to call `exit` to terminate the process.

When calling the `syscall` instruction, we pass the syscall number in the `rax` register and the arguments in registers `rdi`, `rsi`, and `rdx`. The `write` syscall has number `0x01` and the `exit` syscall has number `0x3c`.

These are their C signatures:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-7-1)ssize_t write(int fildes, const void *buf, size_t nbyte);
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-7-2)void exit(int status);
```

and this is our new program `hello-syscall.c`:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-1)int main() {
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-2)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-3)  volatile const char message[] = "Hello Simplicity!\n";
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-4)  volatile const unsigned long length = sizeof(message) - 1;
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-5)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-6)  // write(1, message, length)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-7)  asm volatile("mov $1, %%rax\n"                // write syscall number (0x01)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-8)               "mov $1, %%rdi\n"                // Stdout file descriptor (0x01)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-9)               "mov %0, %%rsi\n"                // Message buffer
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-10)               "mov %1, %%rdx\n"                // Buffer length
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-11)               "syscall"                        // Make the syscall
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-12)               :                                // No output operands
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-13)               : "r"(message), "r"(length)      // Input operands
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-14)               : "%rax", "%rdi", "%rsi", "%rdx" // Clobbered registers
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-15)  );
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-16)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-17)  return 0;
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-18)}
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-19)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-20)void startup() {
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-21)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-22)  volatile unsigned long status = main();
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-23)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-24)  // exit(status)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-25)  asm volatile("mov $0x3c, %%rax\n" // exit syscall number (0x3c)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-26)               "mov %0, %%rdi\n"    // exit status
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-27)               "syscall"            // Make the syscall
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-28)               :                    // No output operands
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-29)               : "r"(status)        // Input operands
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-30)               : "%rax", "%rdi"     // Clobbered registers
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-31)  );
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-8-32)}
```

In case you are wondering, the `volatile` keyword is required to prevent GCC from optimizing away the variables. And `unsigned long` is used instead of `int` to match the size of the `r__` 64-bit registers.

We build it like so:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-9-1)gcc -Wl,-entry=startup -nostdlib -o hello-nostd hello-syscall.c
```

Is this really simpler than before? Well, yes!

It might not be _easier_ to understand unless you are accustomed to assembly language, syscalls, and custom entry points. But simple is not synonymous with easy. Simple is the opposite of complex. Complex things are intrinsically hard to understand, no matter how much you know. Simple things are only hard to understand until you have acquired the appropriate skills. Rich Hickey explains this eloquently in his 2011 talk "[Simple Made Easy](https://youtu.be/SxdOUGdseq4?si=hsXwuad7doytJeJc)".

Still not convinced that we have actually made the program simpler? Let's take a look at the symbols and sections:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-1)$ objdump -h -t hello-nostd
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-2)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-3)Sections:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-4)Idx Name          Size      VMA               LMA               File off  Algn
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-5)  0 .interp       0000001c  0000000000000318  0000000000000318  00000318  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-6)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-7)  1 .note.gnu.property 00000020  0000000000000338  0000000000000338  00000338  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-8)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-9)  2 .note.gnu.build-id 00000024  0000000000000358  0000000000000358  00000358  2**2
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-10)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-11)  3 .gnu.hash     0000001c  0000000000000380  0000000000000380  00000380  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-12)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-13)  4 .dynsym       00000018  00000000000003a0  00000000000003a0  000003a0  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-14)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-15)  5 .dynstr       00000001  00000000000003b8  00000000000003b8  000003b8  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-16)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-17)  6 .text         0000007f  0000000000001000  0000000000001000  00001000  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-18)                  CONTENTS, ALLOC, LOAD, READONLY, CODE
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-19)  7 .eh_frame_hdr 0000001c  0000000000002000  0000000000002000  00002000  2**2
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-20)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-21)  8 .eh_frame     00000058  0000000000002020  0000000000002020  00002020  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-22)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-23)  9 .dynamic      000000e0  0000000000003f20  0000000000003f20  00002f20  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-24)                  CONTENTS, ALLOC, LOAD, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-25) 10 .comment      0000002b  0000000000000000  0000000000000000  00003000  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-26)                  CONTENTS, READONLY
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-27)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-28)SYMBOL TABLE:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-29)0000000000000000 l    df *ABS*  0000000000000000 hello-syscall.c
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-30)0000000000000000 l    df *ABS*  0000000000000000
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-31)0000000000003f20 l     O .dynamic   0000000000000000 _DYNAMIC
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-32)0000000000002000 l       .eh_frame_hdr  0000000000000000 __GNU_EH_FRAME_HDR
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-33)0000000000001050 g     F .text  000000000000002f startup
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-34)0000000000004000 g       .dynamic   0000000000000000 __bss_start
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-35)0000000000001000 g     F .text  0000000000000050 main
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-36)0000000000004000 g       .dynamic   0000000000000000 _edata
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-10-37)0000000000004000 g       .dynamic   0000000000000000 _end
```

There's still a lot going on here, but at least it now fits on one screen. As expected, `objdump -f` gives us a new start address: `0x1050`. It's our `startup` function!

Let's continue simplifying!

Life without PIE
----------------

For the last 20 years, your programs have been loaded into memory at random addresses as a security mitigation. ASLR (Address Space Layout Randomization) makes it harder to write exploits since the shellcode can't jump to hardcoded destinations. It also means jumps in your regular programs can't be hardcoded.

By default, programs on modern systems are built as Position Independent Executables (PIE). Addresses are resolved when the program is loaded into memory. It's great for security, but it adds complexity. Let's get rid of it with: `-no-pie`.

To further unclutter our assembly code, we turn off some more safety features with `-fcf-protection=none` and `-fno-stack-protector`. We also get rid of some metadata generation with `-Wl,--build-id=none` and some debugger-friendly stack unwinding info with `-fno-unwind-tables` and `-fno-asynchronous-unwind-tables`.

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-11-1)gcc -no-pie \
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-11-2)    -nostdlib \
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-11-3)    -Wl,-e,startup \
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-11-4)    -Wl,--build-id=none \
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-11-5)    -fcf-protection=none \
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-11-6)    -fno-stack-protector \
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-11-7)    -fno-asynchronous-unwind-tables \
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-11-8)    -fno-unwind-tables \
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-11-9)    -o hello-nostd-nopie hello.c
```

We are now down to this:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-1)$ objdump -h -t hello-nostd-nopie
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-2)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-3)hello-nostd-nopie:     file format elf64-x86-64
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-4)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-5)Sections:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-6)Idx Name          Size      VMA               LMA               File off  Algn
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-7)  0 .text         00000077  0000000000401000  0000000000401000  00001000  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-8)                  CONTENTS, ALLOC, LOAD, READONLY, CODE
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-9)  1 .comment      0000002b  0000000000000000  0000000000000000  00001077  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-10)                  CONTENTS, READONLY
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-11)SYMBOL TABLE:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-12)0000000000000000 l    df *ABS*  0000000000000000 hello-syscall.c
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-13)000000000040104c g     F .text  000000000000002b startup
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-14)0000000000402000 g       .text  0000000000000000 __bss_start
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-15)0000000000401000 g     F .text  000000000000004c main
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-16)0000000000402000 g       .text  0000000000000000 _edata
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-12-17)0000000000402000 g       .text  0000000000000000 _end
```

Did you notice how the symbol addresses changed with `-no-pie`? Before, they were relative, waiting for some offset to be added at load time. Now, they are absolute, and `main` will really be at `0x00401000`.

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-13-1)$ gdb hi
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-13-2)(gdb) break main
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-13-3)Breakpoint 1 at 0x401004
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-13-4)(gdb) run
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-13-5)Breakpoint 1, 0x0000000000401004 in main ()
```

Phew! We are finally approaching something simple-ish. Now, our entire program even fits on one screen:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-1)$ objdump -d -M intel hello-nostd-nopie
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-2)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-3)Disassembly of section .text:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-4)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-5)0000000000401000 <main>:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-6)  401000:   55                      push   rbp
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-7)  401001:   48 89 e5                mov    rbp,rsp
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-8)  401004:   48 b8 48 65 6c 6c 6f    movabs rax,0x6953206f6c6c6548
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-9)  40100b:   20 53 69
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-10)  40100e:   48 ba 6d 70 6c 69 63    movabs rdx,0x79746963696c706d
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-11)  401015:   69 74 79
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-12)  401018:   48 89 45 e0             mov    QWORD PTR [rbp-0x20],rax
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-13)  40101c:   48 89 55 e8             mov    QWORD PTR [rbp-0x18],rdx
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-14)  401020:   66 c7 45 f0 21 0a       mov    WORD PTR [rbp-0x10],0xa21
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-15)  401026:   c6 45 f2 00             mov    BYTE PTR [rbp-0xe],0x0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-16)  40102a:   48 c7 45 d8 12 00 00    mov    QWORD PTR [rbp-0x28],0x12
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-17)  401031:   00
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-18)  401032:   4c 8b 45 d8             mov    r8,QWORD PTR [rbp-0x28]
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-19)  401036:   48 8d 4d e0             lea    rcx,[rbp-0x20]
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-20)  40103a:   48 c7 c0 01 00 00 00    mov    rax,0x1
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-21)  401041:   48 c7 c7 01 00 00 00    mov    rdi,0x1
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-22)  401048:   48 89 ce                mov    rsi,rcx
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-23)  40104b:   4c 89 c2                mov    rdx,r8
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-24)  40104e:   0f 05                   syscall
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-25)  401050:   b8 00 00 00 00          mov    eax,0x0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-26)  401055:   5d                      pop    rbp
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-27)  401056:   c3                      ret
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-28)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-29)0000000000401057 <startup>:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-30)  401057:   55                      push   rbp
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-31)  401058:   48 89 e5                mov    rbp,rsp
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-32)  40105b:   48 83 ec 10             sub    rsp,0x10
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-33)  40105f:   b8 00 00 00 00          mov    eax,0x0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-34)  401064:   e8 97 ff ff ff          call   401000 <main>
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-35)  401069:   48 98                   cdqe
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-36)  40106b:   48 89 45 f8             mov    QWORD PTR [rbp-0x8],rax
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-37)  40106f:   48 8b 55 f8             mov    rdx,QWORD PTR [rbp-0x8]
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-38)  401073:   48 c7 c0 3c 00 00 00    mov    rax,0x3c
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-39)  40107a:   48 89 d7                mov    rdi,rdx
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-40)  40107d:   0f 05                   syscall
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-41)  40107f:   90                      nop
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-42)  401080:   c9                      leave
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-14-43)  401081:   c3                      ret
```

You can see the `startup` function calling `main`, the two syscalls, and the "Hello Simplicity!" string hardcoded as a large number of ASCII values (being loaded onto the stack, relative to the stack base pointer `rbp`).

There's not a lot of complexity left, at least not at this level. Our ELF is actually quite simple! But wait, there is more!

Linker Scripts
--------------

Where do the strange symbols (like `__bss_start`) come from? And who decides that our `startup` function should be loaded into memory at `0x0040104c`? What if we want our code to live in the cool `0xc0d30000` address range?

These things are specified in the linker script. Until now, we have been using the default one, which you can see with `ld -verbose`. It's very complex. Let's get rid of it.

Our simple hello world application doesn't use any global variables. If it had, they would fall into three categories:

*   `.rodata`: Constants with values provided at compile time, like our hardcoded string.
*   `.data`: Non-const variables with values provided at compile time.
*   `.bss`: Uninitialized global variables.

Let's complicate our program a tiny bit by introducing a symbol for each category. This will provide a more interesting linker script example. Here is the new program `hello-data.c`:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-1)const char message[] = "Hello Simplicity!\n";   // .rodata
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-2)unsigned long length = sizeof(message) - 1;     // .data
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-3)unsigned long status;                           // .bss
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-4)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-5)int main() {
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-6)  // write(1, message, length)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-7)  asm volatile("mov $1, %%rax\n"                // write syscall number (0x01)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-8)               "mov $1, %%rdi\n"                // Stdout file descriptor (0x01)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-9)               "mov %0, %%rsi\n"                // Message buffer
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-10)               "mov %1, %%rdx\n"                // Buffer length
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-11)               "syscall"                        // Make the syscall
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-12)               :                                // No output operands
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-13)               : "r"(message), "r"(length)      // Input operands
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-14)               : "%rax", "%rdi", "%rsi", "%rdx" // Clobbered registers
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-15)  );
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-16)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-17)  return 0;
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-18)}
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-19)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-20)void startup() {
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-21)  status = main();
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-22)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-23)  // exit(status)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-24)  asm volatile("mov $0x3c, %%rax\n" // exit syscall number (0x3c)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-25)               "mov %0, %%rdi\n"    // exit status
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-26)               "syscall"            // Make the syscall
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-27)               :                    // No output operands
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-28)               : "r"(status)        // Input operands
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-29)               : "%rax", "%rdi"     // Clobbered registers
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-30)  );
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-15-31)}
```

Looking at the symbol table again, without using a custom linker script, we can see the globals in `.data`, `.rodata` and `.bss` respectively:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-16-1)000000000040102f g     F .text  000000000000002d startup
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-16-2)0000000000403010 g     O .data  0000000000000008 length
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-16-3)0000000000402000 g     O .rodata    000000000000000e message
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-16-4)0000000000401000 g     F .text  000000000000002f main
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-16-5)0000000000403018 g     O .bss   0000000000000008 status
```

Now, let's create a simple and fun linker script (`hello.ld`) with a cool memory map and emojis in the section names:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-1)MEMORY {
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-2)  IRAM (rx) : ORIGIN = 0xC0DE0000, LENGTH = 0x1000
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-3)  RAM  (rw) : ORIGIN = 0xFEED0000, LENGTH = 0x1000
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-4)  ROM  (r)  : ORIGIN = 0xDEAD0000, LENGTH = 0x1000
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-5)}
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-6)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-7)SECTIONS
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-8){
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-9)  "📜 .text" : {
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-10)    *(.text*)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-11)  } > IRAM
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-12)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-13)  "📦 .data" : {
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-14)    *(.data*)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-15)  } > RAM
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-16)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-17)  "📁 .bss" : {
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-18)    *(.bss*)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-19)  } > RAM
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-20)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-21)  "🧊 .rodata" : {
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-22)    *(.rodata*)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-23)  }  > ROM
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-24)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-25)  /DISCARD/ : { *(.comment) }
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-26)}
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-27)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-17-28)ENTRY(startup)
```

We use the same build options as before but add `-T hello.ld` to start using our linker script.

This is the simple program in its final form:

```
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-1)$ objdump -t -h hello-data
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-2)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-3)hello-data:     file format elf64-x86-64
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-4)
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-5)Sections:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-6)Idx Name          Size      VMA               LMA               File off  Algn
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-7)  0 📜 .text    0000005c  00000000c0de0000  00000000c0de0000  00001000  2**0
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-8)                  CONTENTS, ALLOC, LOAD, READONLY, CODE
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-9)  1 📦 .data    00000008  00000000feed0000  00000000feed0000  00003000  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-10)                  CONTENTS, ALLOC, LOAD, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-11)  2 📁 .bss     00000008  00000000feed0008  00000000feed0008  00003008  2**3
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-12)                  ALLOC
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-13)  3 🧊 .rodata  00000013  00000000dead0000  00000000dead0000  00002000  2**4
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-14)                  CONTENTS, ALLOC, LOAD, READONLY, DATA
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-15)SYMBOL TABLE:
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-16)0000000000000000 l    df *ABS*  0000000000000000 hello-data.c
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-17)00000000c0de002f g     F 📜 .text    000000000000002d startup
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-18)00000000feed0000 g     O 📦 .data    0000000000000008 length
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-19)00000000dead0000 g     O 🧊 .rodata  0000000000000013 message
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-20)00000000c0de0000 g     F 📜 .text    000000000000002f main
[](https://4zm.org/2024/12/25/a-simple-elf.html#__codelineno-18-21)00000000feed0008 g     O 📁 .bss 0000000000000008 status
```

Isn't that absolutely adorable?!

I've put some sample code over at [github.com/4ZM/elf-shenanigans](https://github.com/4ZM/elf-shenanigans) to reproduce the examples in this article.

If you want to learn more about linker scripts (and why wouldn't you?!) this is an outstanding technical documentation: "[c\_Using\_LD](https://users.informatik.haw-hamburg.de/~krabat/FH-Labor/gnupro/5_GNUPro_Utilities/c_Using_LD/ldLinker_scripts.html)".

If you want to explore more ridiculous things to do with section names, check out my other article: "[ELF Shenanigans](https://4zm.org/2024/12/25/elf-shenanigans.html)".

•  •  •
