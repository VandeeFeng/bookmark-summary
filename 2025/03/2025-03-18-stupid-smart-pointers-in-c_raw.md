Title: Stupid Smart Pointers in C

URL Source: https://blog.kevinalbs.com/stupid_smart_pointers

Markdown Content:
Managing memory in C is difficult and error prone. C++ solves this with smart pointers like `std::unique_ptr` and `std::shared_ptr`. This article demonstrates a proof-of-concept (aka stupid) smart pointer in C with very little code. Along the way we'll look at the layout of the 32-bit x86 call stack and write assembly in a C program.

### [§1 Managing Memory in C](https://blog.kevinalbs.com/stupid_smart_pointers#Managing_Memory_in_C)

In C, heap memory is allocated with a call to `malloc` and deallocated with a call to `free`. It is the programmer's responsibility to free allocated memory when no longer in use. Otherwise, memory leaks grow the program's memory usage, exhausting valuable system resources.

Sometimes knowing where to call `free` is clear.

```
char *data = (char *) malloc (100);
// do something with data, don't need it anymore
free (data);
```

But even simple cases may be difficult to properly free. For example, suppose a function `f` allocates resources in order and frees them before returning.

```
void f () {
   char *resource_1 = get_resource ();
   if (resource_1 == NULL) return;

   char *resource_2 = get_resource ();
   if (resource_2 == NULL) {
      free (resource_1);
      return;
   }

   char *resource_3 = get_resource ();
   if (resource_3 == NULL) {
      free (resource_2);
      free (resource_1);
      return;
   }

   // etc.
}
```

Each return must free everything previously allocated. The list of calls to `free` grows for every additional resource allocated. There are ways to organize this to reduce some redundancy. But the root of the problem remains: the lifetime of the allocated resource is bound to where `f` returns. Whenever `f` returns, we need to guarantee all of these resources are freed.

A nice solution in C is described in Eli Bendersky's article: [Using goto for error handling in C](https://eli.thegreenplace.net/2009/04/27/using-goto-for-error-handling-in-c). This uses the goto statement and places all free calls at the end of the function.

```
void f () {
   char *resource_1 = NULL, *resource_2 = NULL, *resource_3 = NULL;
   resource_1 = get_resource ();
   if (resource_1 == NULL) return;

   resource_2 = get_resource ();
   if (resource_2 == NULL) goto free_resource_1;

   resource_3 = get_resource ();
   if (resource_3 == NULL) goto free_resource_2;

// etc.

free_resource_2:
   free (resource_2); // fall through
free_resource_1:
   free (resource_1);
   return;
}
```

But C++ has an even better solution. Since objects have destructors, we can explicitly bind the lifetime of a pointer to the lifetime of an object.

```
void f () {
   auto resource_1 = std::unique_ptr<char> (get_resource ());
   if (resource_1.get () == nullptr) return;
   auto resource_2 = std::unique_ptr<char> (get_resource ());
   if (resource_2.get () == nullptr) return;
   auto resource_3 = std::unique_ptr<char> (get_resource ());
   if (resource_3.get () == nullptr) return;
   /* ... */
}
```

The `unique_ptr` object wraps around the allocated pointer, and frees it when the `unique_ptr` goes out of scope.

Unfortunately, C has no destructors we can hook onto, so there are no native smart pointers. But we can create a surprisingly simple approximation.

### [§2 Implementation](https://blog.kevinalbs.com/stupid_smart_pointers#Implementation)

The smart pointer will only consist of one function, `free_on_exit`, to free the passed pointer when the current function returns. This will allow us to rewrite our above example without any calls to `free`.

```
void f () {
   char *resource_1 = free_on_exit (get_resource ());
   if (resource_1 == NULL) return;

   char *resource_2 = free_on_exit (get_resource ());
   if (resource_2 == NULL) return;

   char *resource_3 = free_on_exit (get_resource ());
   if (resource_3 == NULL) return;
}
```

Wherever `f` returns, it frees everything allocated before. But how can we possibly implement `free_on_exit`? How can we know when `f` returns and free all previous allocations? The trick is to manipulate the call stack. Instead of `f` returning to its original caller, we can manipulate the stack to have it return to our own custom function.

### [§2.1 The Call Stack](https://blog.kevinalbs.com/stupid_smart_pointers#The_Call_Stack)

Let's refresh on what the call stack looks like. The layout of the call stack depends on the architecture. We'll use 32 bit x86 as our target architecture (which has a simpler layout and calling conventions than 64 bit). Eli Bendersky has another great article, [Where the top of the stack is on x86](https://eli.thegreenplace.net/2011/02/04/where-the-top-of-the-stack-is-on-x86/), with more depth, but the following is a brief overview.

Here's an example of what the stack looks like when function `main` calls function `sum` in 32 bit x86 architecture.

```
int sum (int x, int y) {
   int z = x + y;
   return z;
}

int main () {
   int value = sum (2, 3);
}
```

![Image 1](https://blog.kevinalbs.com/img/stupid_smart_pointers/function_call.svg)

The call stack during a function call.

During a function call, the caller and callee split the responsibilities of what data to push onto the stack. The caller `main` is responsible for saving the current `eip`, but the callee `f` is responsible for saving the current `ebp`.

### [§2.2 Hijacking a Return Address](https://blog.kevinalbs.com/stupid_smart_pointers#Hijacking_a_Return_Address)

But how can the stack be modified in a C program? One way is to use assembly to obtain stack addresses, and then change the values they point to. The following uses inline assembly to change a function's return address.

```
#include <stdio.h>
void hijacked () {
   printf ("hijacked\n");
}

void f () {
   printf ("f starts\n");

   int *base = NULL;
   // get the value of ebp.
   __asm__("movl %%ebp, %0 \n"
           : "=r"(base) // output
           );

   // change the return address.
   *(base + 1) = (int) hijacked;

   printf ("f ends\n");
}

int main () {
   printf ("main starts\n");
   f ();
   printf ("main ends\n");
}
```

hijack.c

To run this program:

```
$ gcc -O0 hijack.c -m32 -o hijack
$ ./hijack
main starts
f starts
f ends
hijacked
Bus error: 10
```

We can see that `f` never returns to `main`, but instead to the hijacked function! How does this work?

In `f`, we get the current value of the `ebp` register in `base` using the inline assembly function `__asm__`.

```
__asm__ (
"movl %%ebp, %0 \n" 
: "=r" (base) // output
);
```

`"movl %%ebp, %0 \n"` is the assembly instruction we run. Registers are denoted with `%%`. The `%0` is a placeholder for the first output variable.

`: "=r" (base)` says use the C variable `base` as the first output variable. `"=r"` means store the operand in a register before copying to the output variable.

For more information about `__asm__`, see the article [A Tiny Guide to GCC Inline Assembly](http://ericw.ca/notes/a-tiny-guide-to-gcc-inline-assembly.html) by Eric Woroshow.

Once we have the value of `ebp` in `base`, we can use it just like any pointer.

```
*(base + 1) = (int) hijacked;
```

Since `base` is of type `int*` adding one increments the address by the size of an int (4 bytes in this case). Therefore, this line changes the saved `eip` on the stack from `main` to the address of the function `hijacked`.

Note, after we return from `hijacked` there's an error (yours may be a segmentation fault). Next we'll see how to fix that error.

### [§2.3 Restoring the Return Address](https://blog.kevinalbs.com/stupid_smart_pointers#Restoring_the_Return_Address)

The example before ended with an error. When `hijacked` returns, there isn't an address to pop off of the stack, so it jumps to an invalid address.

![Image 2](https://blog.kevinalbs.com/img/stupid_smart_pointers/hijack.svg)

The caller is responsible for pushing the return address. When we jump directly to `hijacked` we bypass the usual call convention.

Instead we want `hijacked` to return back to the original return address in `main`. To do so we can use a pure assembly function to avoid the typical function call and return sequence of a compiled C function.

```
.section .text
.globl trampoline
.type trampoline, @function
trampoline:
# call hijacked. This pushes the address of the next instruction.
# when hijacked returns, we jump directly to the address in eax.
# eax contains the returned value of hijacked.
call hijacked
jmp %eax
```

trampoline.S

This assembly function named `trampoline` bypasses the usual call sequence generated by compiling a C function. Instead of popping a return address to return to, we `jmp` directly to the value stored in `eax`. The value returned by `hijacked` is stored in `eax`. We modify `hijacked` and `f` as follows:

```
// forward declare the assembly trampoline.
void trampoline ();
int return_address;

int hijacked () {
   printf ("hijacked\n");
   return return_address;
}

void f () {
   printf ("f starts\n");

   int *base;
   // get the value of the ebp.
   __asm__("movl %%ebp, %0 \n"
           : "=r"(base) // output
           );

   // save the return address.
   return_address = *(base + 1);
   // change the return address.
   *(base + 1) = (int) trampoline;

   printf ("f ends\n");
}
```

Compile and run with:

```
$ gcc -o hijack -O0 -m32 hijack.c trampoline.S
$ ./hijack
main starts
f starts
f ends
hijacked 
main ends
```

Now our hijacked function restores the original return address after executing. We'll use this same technique to implement our smart pointer.

### [§2.4 One Smart Pointer](https://blog.kevinalbs.com/stupid_smart_pointers#One_Smart_Pointer)

We're one small step away from creating a smart pointer. Let's rename `hijacked` to `do_free`, and add the function `free_on_exit`, which now hijacks the _caller's_ return address.

```
#include <stdio.h>
#include <stdlib.h>
/* forward declare the assembly trampoline. */
void trampoline ();
int return_address;
void *tracked_pointer;

int do_free () {
   free (tracked_pointer);
   return return_address;
}

void *free_on_exit (void *ptr) {
   int *base;
   // get the value of the caller's ebp by dereferencing ebp.
   __asm__("movl (%%ebp), %0 \n"
           : "=r"(base) // output
           );

   // save and change the caller's return address.
   return_address = *(base + 1);
   *(base + 1) = (int) trampoline;
   return ptr;
}

void f () {
   char *resource = free_on_exit (malloc (1));
}

int main () {
   f ();
}
```

Calling `free_on_exit` stores the passed pointer and sets the caller's return address to `trampoline`. After the caller `f` returns, it automatically frees its `malloc`'ed byte. We now have a smart pointer!

### [§2.5 Many Smart Pointers](https://blog.kevinalbs.com/stupid_smart_pointers#Many_Smart_Pointers)

The `free_on_exit` above is only a single-use function. If called multiple times, it only frees the pointer passed in the most recent call. Fortunately, it's only another small step to make `free_on_exit` work with any number of repeated calls.

To do so we can store a list of tracked pointers for each function call. Stack these lists, and each time a new function calls free\_on\_exit, add a new stack entry. When do\_free is called, it frees the list of pointers on the top most entry of the stack.

At the risk of including too much code in this article, here is the full implementation in under one hundred lines of code:

```
#ifndef _SMART
#define _SMART
void *free_on_exit (void *);
#endif
```

smart.h

```
#include "smart.h"

#include <stdlib.h> // free
#include <string.h> // memset

/* these limits are arbitrary. */
#define STACK_SIZE 256
#define MAX_PER_FRAME 32

typedef struct {
   int caller_ebp; /* ebp of the caller. This identifes the frame. */
   int caller_eip; /* the original return eip of the caller. */
   void *tracked_pointers[MAX_PER_FRAME];
   int tail; /* points to one past last entry. */
} tracked_stack_entry_t;

typedef struct {
   tracked_stack_entry_t stack[STACK_SIZE];
   int tail; /* points to one past last entry. */
} tracked_stack_t;

/* forward declare the assembly trampoline. */
void trampoline ();

tracked_stack_t tracked = {0};

int do_free () {
   tracked_stack_entry_t *entry = tracked.stack + (tracked.tail - 1);
   tracked.tail--; /* pop. */
   for (int i = 0; i < MAX_PER_FRAME; i++) {
      if (entry->tracked_pointers[i] == 0) break;
      free (entry->tracked_pointers[i]);
   }
   return entry->caller_eip;
}

void *free_on_exit (void *entry) {
   int ret_addr = 0;
   int do_free_addr = (int) &do_free;
   int *caller_ebp;

   /* get the value of ebp. */
   __asm__("movl (%%ebp), %0 \n"
           : "=r"(caller_ebp) /* output. */
           );

   /* check if there is a pre-existing stack entry for this caller
    * (identified by caller's ebp). */
   tracked_stack_entry_t *tracked_entry;

   if (tracked.tail > 0 &&
       tracked.stack[tracked.tail - 1].caller_ebp == (int) caller_ebp) {
      /* re-use. */
      tracked_entry = tracked.stack + tracked.tail - 1;
   } else {
      /* make a new entry. */
      tracked_entry = tracked.stack + tracked.tail++;
      memset (tracked_entry, 0, sizeof (*tracked_entry));
      tracked_entry->caller_ebp = (int) caller_ebp;
      /* hijack caller's return eip to return to do_free. */
      tracked_entry->caller_eip = *(caller_ebp + 1);
      *(caller_ebp + 1) = (int) trampoline;
   }

   /* push the passed pointer. */
   tracked_entry->tracked_pointers[tracked_entry->tail++] = entry;
   return entry;
}
```

smart.c

```
# This can be compiled by itself with `as --32`
# This is GNU assembler syntax (aka AT-T syntax) (src, dest)
.section .text
.globl trampoline 
.type trampoline, @function
trampoline:
call do_free
jmp %eax # jump directly back to the old eip.
```

trampoline.S

Additionally, the code is in a [GitHub repository](https://github.com/kevinAlbs/SmartPointer).

### [§3 Conclusion](https://blog.kevinalbs.com/stupid_smart_pointers#Conclusion)

In this article we've shown how to build a simple and incomplete smart pointer on an 32 bit x86 architecture. We've looked at the call stack, hijacked return addresses, and written some assembly in the process.

I recently discovered the implementation of `free_on_exit` won't work if called directly from `main` if gcc aligns the stack. In this case, `main` adds padding between the saved `eip` and the saved `ebp`, [(example)](https://stackoverflow.com/q/4228261/774658). I think this can be fixed some tweaking, and will update this article when it is fixed.

For more reading, check out the following articles:

*   [libcsptr](https://github.com/Snaipe/libcsptr) a full-fledged smart pointer library written in C
*   [A Guide to inline Assembly](http://ericw.ca/notes/a-tiny-guide-to-gcc-inline-assembly.html) by Eric Woroshow
*   [Where the top of the stack is on x86](https://eli.thegreenplace.net/2011/02/04/where-the-top-of-the-stack-is-on-x86/) by Eli Bendersky
*   [Stack frame layout on x86-64](https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64) by Eli Bendersky
*   [Using goto for error handling in C](https://eli.thegreenplace.net/2009/04/27/using-goto-for-error-handling-in-c) by Eli Bendersky
