Title: I Write Type Safe Generic Data Structures in C

URL Source: https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/

Published Time: 2025-06-25T00:00:00+00:00

Markdown Content:
I write type safe generic data structures in C using a technique that I haven’t seen elsewhere[1](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/#fn:1). It uses unions to associate type information with a generic data structure, but we’ll get to that. My approach works for any type of data structure: maps, arrays, binary trees… but for this article I illustrate the ideas by implementing a basic linked list. Since many people aren’t aware you can do C generics _at all_, I figured I’d start simple and build up to this:

```
typedef struct {
    int value;
} Foo;
    
List(int) int_list = {0};
list_prepend(&int_list, 3);

List(Foo) foo_list = {0};
list_prepend(&foo_list, (Foo){ 5 });
list_prepend(&foo_list, (Foo){ 3 });

// this won't compile, which is good!
// list_prepend(&foo_list, 7); 

list_for(item, &foo_list) {
    // `item` is of type `Foo *`
    printf("%i\n", item->value);
}
```

I hesitate to even mention this, because I do not like it[2](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/#fn:2), but its worth comparing to the technique at the end of this article. It works like this: you write your data structure in a header, using macros for your types, and then `#include` the header multiple times; once for each type the data structure will be used with.

Click to see the Code

`list.h`

```
#ifndef T
#error "T must be defined before including this header"
#endif

#define _CONCAT(a, b) a##b
#define CONCAT(a, b) _CONCAT(a, b)

#define NODE_TYPE CONCAT(T, ListNode)
#define PREPEND_FUNC CONCAT(T, _list_prepend)

typedef struct NODE_TYPE NODE_TYPE;
struct NODE_TYPE {
    NODE_TYPE *next;
    T data;
};

void PREPEND_FUNC(NODE_TYPE **head, T data) {
    NODE_TYPE *node = malloc(sizeof(*node));
    node->data = data;
    node->next = *head;
    *head = node;
}

#undef T
#undef _CONCAT
#undef CONCAT
#undef NODE_TYPE
#undef PREPEND_FUNC
```

`main.c`

```
typedef struct {
    int a;
} Foo;

typedef struct {
    char *str;
    double num;
} Bar;

#define T Foo
#include "list.h"

#define T Bar
#include "list.h"

FooListNode *foo_head = NULL;
Foo_list_prepend(&foo_head, (Foo){1})

BarListNode *bar_head = NULL;
Bar_list_prepend(&bar_head, (Bar){"hello", 5.4})
```

While it _is_ generic and type safe, it has downsides:

*   makes it hard to find where types and functions are defined (because they’re constructed by macros)
*   code completion may not handle them well
*   bloats your binary size and build times with copies of the same functions
*   requires using type-prefixed functions: `Foo_list_prepend() and int_list_prepend()` vs just `list_prepend()`

### Generics level 1: `void *`

Another way to make a data structure generic is to use `void *`. It’s not type safe but we’ll get to that.

```
typedef struct ListNode ListNode;
struct ListNode {
    ListNode *next;
    void *data;
};

void list_prepend(ListNode **head, void *data) {
    ListNode *node = malloc(sizeof(*node));
    node->data = data;
    node->next = *head;
    *head = node;
}
```

Note: `malloc` is used for familiarity, but I highly recommend Arenas instead. You can [watch](https://www.youtube.com/watch?v=TZ5a3gCCZYo) or [read](https://www.rfleury.com/p/untangling-lifetimes-the-arena-allocator) about them.

Having `ListNode` and its `data` as separate allocations isn’t ideal from a memory and performance perspective. It requires 2 allocations per node when one would do, the `data` pointer uses memory unnecessarily, and you will likely get two cache misses per node when traversing the list: once getting the next node, and once getting its data. We can fix these issues with…

### Generics level 2: Inline storage

Instead of storing a pointer to the node’s data, we can use a [Flexible Array Member](https://en.wikipedia.org/wiki/Flexible_array_member) to store the data inside the node. To do so, we make a single allocation large enough for both the node and the type it stores[3](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/#fn:3):

```
typedef struct ListNode ListNode;
struct ListNode {
    ListNode *next;
    char data[]; // glossing over some padding/alignment details here
};

void list_prepend(ListNode **head, 
                 void *data, 
                 size_t data_size) 
{
    ListNode *node = malloc(sizeof(*node) + data_size);
    memcpy(node->data, data, data_size);
    node->next = *head;
    *head = node;
}

void main() {
    ListNode *foo_list = NULL;
    Foo foo = {5};
    list_prepend(&foo_list, &foo, sizeof(foo));
}
```

Now `next` and the actual contents of `data` are beside each other in memory, solving the issues of the `void *` approach. Unfortunately we now have to pass the size, but we’ll fix that in the next section

If you wanted to avoid the `memcpy`, and initialize the node’s memory directly, you could do so with a `list_alloc_front` function:

```
void *list_alloc_front(ListNode **head, size_t data_size)  {
    ListNode *node = malloc(sizeof(*node) + data_size);
    node->next = *head;
    *head = node;
    return node->data;
}

Foo *new_foo = list_alloc_front(&foo_list, sizeof(*new_foo));
new_foo->value = 5;
```

### Generics level 3: Type Checking

The part you’ve all been waiting for: how to get the compiler to error when we try to add the wrong type to a list. The way I found to do this is to use a union with a `payload` member that has a parameterized type:

```
#define List(type) union { \
    ListNode *head; \
    type *payload; \
}

List(Foo) foo_list = {0};
List(int) int_list = {0};
```

How does that help us? Well, we can use the ternary operator to enforce that the `item` parameter is the same type as the list’s `payload`:

```
// Note: leading underscore add to the 
// function name since only the macro should call it
void _list_prepend(ListNode **head, 
                 void *data, 
                 size_t data_size);

#define list_prepend(list, item) \
    _list_prepend(&((list)->head), \
                  (1 ? (item) : (list)->payload), \
                  sizeof(*(list)->payload)) 
               
List(Foo) *foo_list = NULL;
Bar bar = {5, 6};
list_prepend(&foo_list, &bar); // error!
```

The macro also handles passing the item size for us! This is the error Clang produces when adding the wrong type to the list:

```
error: pointer type mismatch ('Foo *' and 'Bar *') [-Werror,-Wpointer-type-mismatch]
   38 |     list_prepend(&foo_list, &bar);
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
note: expanded from macro 'list_prepend'
   15 |     _list_prepend(&((list)->head), (1 ? (item) : (list)->payload), sizeof(*(list)->payload))
      |
```

Macros get a bad rep, but I think this is fairly understandable. Some things to note: `payload` is never used at runtime, it exists just for type information at compile time. Using a union makes `payload` not consume any memory.

If you’re writing a generic function that needs to return a pointer to contained data, you can use `__typeof__()` to cast the return type from `void *` to the data structure’s `payload` type. `__typeof__()` is supported in all three big C compilers (clang, gcc, **and** msvc since version 19.39).

```
#define list_alloc_front(list) \
    (__typeof__((list)->payload))_list_alloc_front(&(list)->head, sizeof(*(list)->payload))
    
void *_list_alloc_front(ListNode **head) {...}
```

If for some reason you don’t like using the ternary operator to ensure two types are the same, a previous version of this article used a different technique:

Read the old technique

We can use `__typeof__(foo_list.payload)` to get the type the list contains. We’ll write a `list_prepend` macro, which will call `_list_prepend` with a cast function type so that the `void *` parameter is the list’s `payload` type

```
// Note: I added a leading underscore to the 
// function name since only the macro should call it
void _list_prepend(ListNode **head, 
                 void *data, 
                 size_t data_size);

#define list_prepend(list, item) \
    /* cast function type */ \
    ((void (*)(ListNode **, \
               __typeof__((list)->payload), \
               size_t))_list_prepend)  \
               /* call function */ \
               (&((list)->head), item, sizeof(*(list)->payload)) 
               
List(Foo) *foo_list = NULL;
Bar bar = {5};
list_prepend(&foo_list, &bar); // error!
```

Calling a typecast function pointer is technically undefined behavior, but in practice it’s fine when compiled by modern compilers targeting modern platforms.

`typeof` on old compilers
-------------------------

`__typeof__()` was an optional extension until C23, which made it part of the C standard. While Clang and gcc have supported it for a _long_ time, some compilers haven’t (like msvc versions prior to 19.39). To make this technique work on those compilers, you can use the terenary operator instead of typeof

```
#define List(type) struct { \
    ListNode *head; \
    type *payload; \
}

#define list_prepend(list, item) \
    _list_prepend(&((list)->head), (1 ? (item) : (list)->payload), sizeof(*(list)->payload))
```

It’s possible to do type safe returns as well, by assigning through `payload`, but I’ll leave the details as an exercise for the reader. [#](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/#typeof-msvc)

Passing a Parameter
-------------------

One annoying thing about C compilers released prior to late 2025[4](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/#fn:4) is that they do not consider these two variables to have the same type:

```
List(Foo) a;
List(Foo) b = a; // error

void my_function(List(Foo) list);
my_function(a); // error: incompatible type
```

Even though the variables have identical type definitions, the compiler still errors because they are _two distinct definitions_. A `typedef` avoids the issue:

```
typedef List(Foo) ListFoo; // this makes it all work

ListFoo a;
ListFoo b = a; // ok

void my_function(ListFoo list);
my_function(a); // ok

List(Foo) local_foo_list; // still works
```

### Conclusion

You can use this for any type of data structure, even ones with multiple associated types, like a hash map:

```
typedef struct {
    ...
} MapInternal;

#define Map(key_type, value_type) union { \
    MapInternal map; \
    key_type *key; \
    value_type *value; \
}
```

For more detail, like how the `list_for` macro is implemented, see the code [here](https://gist.github.com/danielchasehooper/a646a109b62441ca1b4d75d94436b5cf)

* * *

Thanks to [Martin Fouilleul](https://forkingpaths.dev/index.html) for the encouragement to finish this post, which I’ve been sitting on for months, and the feedback on early drafts.

* * *

1.   [stb_ds.h](https://github.com/nothings/stb/blob/master/stb_ds.h) is an example of a type-safe generic data structure, but the techniques it uses aren’t as general as what I present here - it only works because the array and map are implemented using a c array. The compiler catches some type errors upon assignment to that c array, not at the point that values are passed as parameters to generic functions. i.e. `struct {int a; int b;} baz; STBDS_ADDRESSOF(baz, 5)` compiles successfully, when you really want a type error.[↩︎](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/#fnref:1)

2.   If you want to write a generic function that requires type-specific code gen (like generating `add_int` and `add_double` from the same source), this option has more merit. You can get creative with c features in other ways to get type-specific behavior, like for hashing functions, for example.[↩︎](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/#fnref:2)

3.   I’m glossing over some information about alignment, padding, and size calculations that come into play with the `data` member, but that’s a whole other topic that you sohuld read up on elsewhere if you’re unfamiliar.[↩︎](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/#fnref:3)

4.   Structurally identical types will be considered the same type in GCC 15 and Clang later in 2025 thanks to a [rule change](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3037.pdf)[↩︎](https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/#fnref:4)
