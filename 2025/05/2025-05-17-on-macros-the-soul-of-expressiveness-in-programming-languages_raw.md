Title: On Macros: The Soul of Expressiveness in Programming Languages

URL Source: http://lemonhx.moe/macro?locale=en

Published Time: 2025-01-31T17:21:28.473Z

Markdown Content:
I have a thought now that "Macro" actually refers to too many things. At least in my mind, there are many things that can be called Macro. I will first list out what I have in mind and then see what connections exist between these things.

1.   **Preprocessor**: Simple text replacement, without involving syntax or semantic analysis.
2.   **Syntactic macro**: Operates on and generates code at the syntactic level, understanding the syntax structure of the language.
3.   **Partial elaborator**: Performs a certain degree of semantic analysis during code expansion to ensure the correctness of the code.
4.   **Ad hoc elaborator**: A highly flexible code generation system that allows developers to customize code expansion rules as needed.

There may be some that you have seen and some that you have not. I will explain them one by one, along with their connections and differences.

1.   **String replacing macro (Preprocessor)**:

    *   This type of macro is usually implemented through simple text replacement, such as the `#define` macro in C. These macros perform text replacement before compilation, without involving syntax analysis or semantic understanding. Their role is indeed to preprocess the source code before compilation.

2.   **Macros in Common Lisp (Syntactic macro)**:

    *   Macros in Common Lisp are "syntactic macros," which expand at compile time and can operate on and generate Lisp code. These macros are not just text replacements; they can understand the syntax structure of Lisp and generate new syntax structures.

3.   **Macros in Scheme (Hygienic macro) / Partial elaborator**:

    *   Macros in Scheme (especially hygienic macros) avoid issues like variable capture during expansion, ensuring that the code after macro expansion does not accidentally change the meaning of the program. They perform a certain degree of semantic analysis during code expansion to ensure that the expanded code is semantically correct.

4.   **Macros in Racket / Templates in Lean / Templates in Template Haskell (Ad hoc elaborator)**:

    *   In Racket, Lean, and Template Haskell, the macro or template systems are more flexible and powerful, allowing developers to define complex code generation rules as needed. These systems allow developers to customize code generation and expansion according to specific needs, offering high flexibility and expressiveness.

Syntax and Semantics[#](http://lemonhx.moe/macro?locale=en#user-content-syntax-and-semantics)
---------------------------------------------------------------------------------------------

I will explain in detail the differences between **Preprocessor**, **Syntactic Macro**, and **Elaborator**, and further illustrate this with **syntax** and **semantics**.

### 1. **Preprocessor**[#](http://lemonhx.moe/macro?locale=en#user-content-1-preprocessor)

*   **Keywords**: Text replacement, no syntax awareness, no semantic awareness.
*   **Definition**: A preprocessor is a tool that performs simple text replacement on source code before compilation. It does not care about the syntactic structure or semantic meaning of the code; it mechanically performs string replacement.
*   **Syntax**: The preprocessor does not parse the syntactic structure of the code, so it cannot distinguish between syntactic elements (such as variables, functions, expressions, etc.) in the code.
*   **Semantics**: The preprocessor does not care about the semantics of the code; it simply replaces one string with another, and whether the replaced code is valid is handled by the compiler or interpreter later.
*   **Examples**: 
    *   The `#define` macro in C: ```
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```  Here, `MAX(a, b)` will be simply replaced with `((a) > (b) ? (a) : (b))`, and the preprocessor will not check whether `a` and `b` are valid expressions.
    *   The preprocessor can also be used for conditional compilation: ```
#ifdef DEBUG
printf("Debug mode\n");
#endif
```  Here, `#ifdef` and `#endif` are preprocessor directives that decide whether to include a certain piece of code based on conditions.

### 2. **Syntactic Macro**[#](http://lemonhx.moe/macro?locale=en#user-content-2-syntactic-macro)

*   **Keywords**: Syntax awareness, syntax tree manipulation, no semantic awareness.
*   **Definition**: A syntactic macro is a mechanism that expands at compile time and operates on the syntactic structure of the code (usually the abstract syntax tree, AST). Syntactic macros can generate new syntax structures, but they do not care whether the generated code is semantically correct.
*   **Syntax**: Syntactic macros understand the syntactic structure of the code, so they can manipulate the syntax tree (AST). For example, they can recognize syntactic elements like function calls, variable declarations, etc., and generate new syntax structures.
*   **Semantics**: Syntactic macros do not care about the semantics of the code. They are only responsible for generating syntax structures, and whether the generated code is valid is checked by subsequent compilers or interpreters.
*   **Examples**: 
    *   Macros in Common Lisp: ```
(defmacro unless (condition &body body)
  `(if (not ,condition) (progn ,@body)))
```  This macro defines an `unless` structure that expands to an `if` expression at compile time. The macro operates on the syntax tree during expansion but does not check whether `condition` and `body` are semantically correct.
    *   The `syntax-rules` macro in Scheme: ```
(define-syntax unless
  (syntax-rules ()
    ((_ condition body ...)
     (if (not condition) (begin body ...)))))
```  This macro also operates on the syntax tree, but it avoids variable capture issues through the hygienic macro mechanism.

### 3. **Elaborator**[#](http://lemonhx.moe/macro?locale=en#user-content-3-elaborator)

*   **Keywords**: Syntax awareness, semantic awareness, type checking, code generation.
*   **Definition**: An elaborator is a more advanced code expansion mechanism that not only operates on the syntax tree but also performs semantic analysis (such as type checking, scope analysis, etc.). Elaborators are typically used to expand high-level language features (such as pattern matching, type classes, dependent types, etc.) into a lower-level core language.
*   **Syntax**: Elaborators understand the syntactic structure of the code, so they can manipulate the syntax tree.
*   **Semantics**: Elaborators care about the semantics of the code. They perform semantic analysis during code expansion to ensure that the generated code is semantically correct (for example, type correctness, variable scope correctness, etc.).
*   **Examples**: 
    *   The elaborator in Lean:

 The elaborator in the Lean language is responsible for expanding high-level syntax (such as dependent types, pattern matching) into core language representations. It performs type checking and semantic analysis to ensure that the generated code is valid. ```
def add (x y : Nat) : Nat := x + y
```  Here, the definition of the `add` function will be expanded by the elaborator into a lower-level core language representation while performing type checking.
    *   The elaborator in Idris:

 The elaborator in Idris is responsible for expanding high-level syntax (such as type classes, dependent types) into core language representations. For example: ```
add : Nat -> Nat -> Nat
add x y = x + y
```  Here, the definition of the `add` function will be expanded by the elaborator into a lower-level representation and undergo type checking.

### Comparison Summary[#](http://lemonhx.moe/macro?locale=en#user-content-comparison-summary)

| Feature | Preprocessor | Syntactic Macro | Elaborator |
| --- | --- | --- | --- |
| **Syntax Awareness** | No | Yes | Yes |
| **Semantic Awareness** | No | No | Yes |
| **Operating Object** | Text strings | Syntax tree (AST) | Syntax tree (AST) |
| **Generates Valid Code** | Not necessarily (depends on subsequent compiler) | Not necessarily (depends on subsequent compiler) | Yes (will perform semantic checks) |
| **Typical Example** | C language's `#define` | Common Lisp macros | Lean, Idris's Elaborator |

So after all this, what is `Ad hoc elaborator`?[#](http://lemonhx.moe/macro?locale=en#user-content-so-after-all-this-what-is-ad-hoc-elaborator)
-----------------------------------------------------------------------------------------------------------------------------------------------

### **What is Ad hoc?** A common question[#](http://lemonhx.moe/macro?locale=en#user-content-what-is-ad-hoc-a-common-question)

*   **Ad hoc** is a Latin phrase meaning "designed for a specific purpose" or "special." In programming languages, **Ad hoc** is often used to describe a **non-general**, **specific problem** solution.
*   An **ad hoc elaborator** can be understood as a **code expansion mechanism designed for specific needs**. Unlike a general elaborator, it does not have strict rules and constraints, allowing developers to flexibly define code generation logic as needed.

### **Why is Racket's macro an Ad hoc elaborator?**[#](http://lemonhx.moe/macro?locale=en#user-content-why-is-rackets-macro-an-ad-hoc-elaborator)

Racket's macro system is very powerful and flexible, allowing developers to define complex code generation rules as needed. Here are the reasons why Racket macros are called **Ad hoc elaborators**:

#### **Flexibility**[#](http://lemonhx.moe/macro?locale=en#user-content-flexibility)

*   Racket's macro system allows developers to define **arbitrarily complex code transformation rules**. Developers can design macros according to specific needs without being constrained by the core syntax of the language.
*   For example, Racket's macros can manipulate the syntax tree (AST), generate new syntax structures, and even introduce new language features (such as DSLs, domain-specific languages).

#### **Phases and Namespaces**[#](http://lemonhx.moe/macro?locale=en#user-content-phases-and-namespaces)

*   Racket's macro system introduces the concept of **phases**, allowing macros to run at different compilation stages. Each phase has its own namespace, avoiding naming conflicts. 
    *   For example, Racket's macros can run at **compile time**, generating code that can be used at **runtime**.
    *   This layered mechanism allows macros to handle code generation and expansion more flexibly.

*   Other languages' macro systems typically lack this concept of phases and namespaces, limiting their macro functionality.

#### **Solutions for Specific Problems**[#](http://lemonhx.moe/macro?locale=en#user-content-solutions-for-specific-problems)

*   Racket's macro system allows developers to define **customized code generation rules for specific needs**. For example: 
    *   You can define a macro to simplify a specific programming pattern.
    *   You can define a macro to implement a domain-specific language (DSL).

*   This **design for specific problems** is the core feature of **Ad hoc**.

#### **Difference from General Elaborator**[#](http://lemonhx.moe/macro?locale=en#user-content-difference-from-general-elaborator)

*   General elaborators (such as those in Lean or Idris) usually have strict rules and constraints, such as type checking and semantic analysis.
*   Racket's macro system is more flexible, allowing developers to define code generation rules as needed without strict semantic constraints. Therefore, it resembles an **Ad hoc elaborator**.

### **Racket's Macro System Phases and Namespaces**[#](http://lemonhx.moe/macro?locale=en#user-content-rackets-macro-system-phases-and-namespaces)

Racket's macro system introduces the concepts of **phases** and **namespaces**, making its macro system more flexible and powerful.

#### **Phases**[#](http://lemonhx.moe/macro?locale=en#user-content-phases)

*   Racket's macro system supports **multi-stage compilation**. Each stage has its own syntax environment and namespace. 
    *   For example, macros can run at **compile time**, generating code that can be used at **runtime**.
    *   This layered mechanism avoids naming conflicts and allows macros to operate on code at different stages.

*   Other languages' macro systems typically lack this concept of phases, limiting their macro functionality.

#### **Namespaces**[#](http://lemonhx.moe/macro?locale=en#user-content-namespaces)

*   Racket's macro system provides independent namespaces for each phase. This means: 
    *   Macros can define and use variables at compile time without conflicting with runtime variables.
    *   This namespace mechanism allows macros to operate on code more flexibly without introducing unintended side effects.

### **Why Other Languages' Macros Are Not Ad hoc Elaborators?**[#](http://lemonhx.moe/macro?locale=en#user-content-why-other-languages-macros-are-not-ad-hoc-elaborators)

*   **Common Lisp's Macros**: Although Common Lisp's macros are very powerful, they lack the concept of phases and namespaces, so they do not meet the flexible customization characteristic of **Ad hoc**.
*   **Scheme's Macros**: While Scheme's macros (especially hygienic macros) avoid variable capture issues, their functionality is relatively limited and cannot flexibly define code generation rules like Racket's macros.

What is the difference between `Elaborator` and `Compile time execution`?[#](http://lemonhx.moe/macro?locale=en#user-content-what-is-the-difference-between-elaborator-and-compile-time-execution)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> In this chapter, `macro` refers to `Elaborator`, not `Syntactic Macro`.

Thinking in this direction, you are close to grasping the core. Now let's delve into the relationship between **macros (elaborators)** and **compile-time execution**, and why **elaborators** need the cooperation of **compile-time execution** to achieve more powerful functionality.

### **Role of Elaborator**[#](http://lemonhx.moe/macro?locale=en#user-content-role-of-elaborator)

*   The main task of an **elaborator** is to expand high-level language features (such as pattern matching, type classes, dependent types, etc.) into lower-level core language representations.
*   It is not just simple syntax transformation; it also performs semantic analysis (such as type checking, scope analysis, etc.) to ensure that the generated code is semantically correct.

### **Role of Compile-time Execution**[#](http://lemonhx.moe/macro?locale=en#user-content-role-of-compile-time-execution)

*   **Compile-time execution** refers to executing certain code during the compilation phase to generate or optimize the final program.
*   The code executed at compile time is usually a **basic form evaluator**, which can compute constant expressions, expand macros, optimize code, etc.

### **Relationship Between Elaborator and Compile-time Execution**[#](http://lemonhx.moe/macro?locale=en#user-content-relationship-between-elaborator-and-compile-time-execution)

Elaborators and compile-time execution complement each other, working together to achieve more powerful compile-time functionality.

#### **Elaborator Needs Support from Compile-time Execution**[#](http://lemonhx.moe/macro?locale=en#user-content-elaborator-needs-support-from-compile-time-execution)

*   Elaborators often need to execute some calculations when expanding high-level language features. For example: 
    *   In dependent type systems, type checking may require computing certain expressions at compile time.
    *   In pattern matching, the expansion of patterns may need to compute certain conditions at compile time.

*   These calculations require the support of **compile-time execution**; otherwise, the elaborator cannot complete its tasks.

#### **Compile-time Execution Needs Support from Elaborator**[#](http://lemonhx.moe/macro?locale=en#user-content-compile-time-execution-needs-support-from-elaborator)

*   Compile-time execution often needs to manipulate the syntax tree (AST), and the elaborator is responsible for expanding high-level language features into the syntax tree.
*   For example, when executing certain code at compile time, it may be necessary to first expand high-level language features into a lower-level representation through the elaborator before performing calculations.

### **Specific Examples**[#](http://lemonhx.moe/macro?locale=en#user-content-specific-examples)

#### **Dependent Type Systems**[#](http://lemonhx.moe/macro?locale=en#user-content-dependent-type-systems)

*   In dependent type systems (such as Idris or Lean), type checking may require computing certain expressions at compile time.
*   For example: ```
add : (n : Nat) -> (m : Nat) -> Nat
add n m = n + m
```  Here, type checking may require computing the type of `n + m` at compile time. The elaborator is responsible for expanding the `add` function into a core language representation, while compile-time execution handles the type computation.

#### **Pattern Matching**[#](http://lemonhx.moe/macro?locale=en#user-content-pattern-matching)

*   In pattern matching, the expansion of patterns may require computing certain conditions at compile time.
*   For example: ```
factorial : Nat -> Nat
factorial 0 = 1
factorial n = n * factorial (n - 1)
```  Here, the pattern matching needs to be expanded into an `if-else` structure at compile time. The elaborator is responsible for expanding the pattern matching into a core language representation, while compile-time execution handles the condition computation.

#### **Racket's Macro System**[#](http://lemonhx.moe/macro?locale=en#user-content-rackets-macro-system)

*   Racket's macro system allows arbitrary code to be executed at compile time to generate new syntax structures.
*   For example: ```
(define-syntax (unless stx)
  (syntax-case stx ()
    [(_ condition body ...)
     #'(if (not condition) (begin body ...))]))
```  Here, the `unless` macro expands to an `if` expression at compile time. The elaborator is responsible for expanding `unless` into `if`, while compile-time execution computes `condition` and `body` at compile time.

### **Why Does Elaborator Need Compile-time Execution to Be Perfect?**[#](http://lemonhx.moe/macro?locale=en#user-content-why-does-elaborator-need-compile-time-execution-to-be-perfect)

*   **Dynamic Computation**: Elaborators often need to dynamically compute certain expressions when expanding high-level language features. These computations need to be completed at compile time, thus requiring the support of compile-time execution.
*   **Optimization**: Compile-time execution can optimize code at compile time, such as constant folding, dead code elimination, etc. These optimizations require the support of the elaborator to expand high-level language features into lower-level representations.
*   **Flexibility**: Compile-time execution allows arbitrary code to be executed at compile time, enabling the elaborator to handle code generation and expansion more flexibly.

Wait, I'm still a bit confused. Look at why Zig finds macros troublesome but seems flexible after introducing compile-time execution?[#](http://lemonhx.moe/macro?locale=en#user-content-wait-im-still-a-bit-confused-look-at-why-zig-finds-macros-troublesome-but-seems-flexible-after-introducing-compile-time-execution)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We need to analyze the fundamental flaws of relying solely on **compile-time execution** without the **elaborator** or **macro** system from the perspective of the underlying mechanisms of programming language design. Here, we will focus on two core issues:

1.   **Rigidity of Type System**: Compile-time execution can only operate on **base forms**, unable to break through the abstract boundaries set by language designers.
2.   **Collapse of Metaprogramming Dimensions**: The metaprogramming capabilities of compile-time execution are limited to the **value computation** level, lacking deep control over the language's **syntax structure** and **compilation pipeline**.

### **Rigidity of Type System**[#](http://lemonhx.moe/macro?locale=en#user-content-rigidity-of-type-system)

**Fundamental Contradiction**: When compile-time execution can only operate on **base forms**, it means that all metaprogramming behaviors are confined within the native type system and syntax structure of the language, unable to break through the abstract boundaries set by language designers.

#### **Inflexibility of Type Inference**[#](http://lemonhx.moe/macro?locale=en#user-content-inflexibility-of-type-inference)

*   **Zig's Limitations**: Zig's compile-time functions (`comptime`) can compute values but cannot generate new type system rules. For example: ```
// Cannot define new type inference rules at compile time
const MyType = comptime {
    // Suppose we want to automatically infer a specific type based on context
    return if (some_condition) u32 else f64; // Must explicitly return a type
};
```  This code generation is static and cannot dynamically infer types based on context, limiting the flexibility of the type system.
*   **Comparison with Elaborator**: In dependent type languages (like Lean), the elaborator can dynamically generate type constraints: ```
def myFunction (x : Nat) :=
  if x > 0 then x + 1 else "Error"  -- The type system automatically infers `Nat ⊕ String`
```  Here, type inference is dynamic, while Zig's compile-time execution cannot achieve this.

#### **Strong Coupling of Syntax and Semantics**[#](http://lemonhx.moe/macro?locale=en#user-content-strong-coupling-of-syntax-and-semantics)

*   **Zig's Dilemma**: Code generated at compile time must strictly adhere to Zig's syntax and type rules, unable to relax or strengthen rules for specific scenarios. For example: 
    *   Cannot define a "no panic" subset of code in embedded development.
    *   Cannot disable safety checks for performance-critical code.

*   **Elaborator's Solution**: Racket's macros can define new control flow semantics: ```
(define-syntax-rule (?? expr default)
  (if (not (null? expr)) expr default))
```  This macro can redefine the behavior of the `??` operator at the syntax level, while Zig's compile-time execution cannot achieve similar functionality.

### **Collapse of Metaprogramming Dimensions**[#](http://lemonhx.moe/macro?locale=en#user-content-collapse-of-metaprogramming-dimensions)

**Core Issue**: The metaprogramming capabilities of compile-time execution are limited to the **value computation** level, lacking deep control over the language's **syntax structure** and **compilation pipeline**.

#### **Lack of Syntax Tree Manipulation**[#](http://lemonhx.moe/macro?locale=en#user-content-lack-of-syntax-tree-manipulation)

*   **Zig's Flaw**: Zig cannot directly manipulate the abstract syntax tree (AST); all code generated at compile time must be implemented through string concatenation or templated code structures. For example: ```
// Generating code through string concatenation (similar to C preprocessor)
const code = comptime {
    var buf: [100]u8 = undefined;
    _ = std.fmt.bufPrint(&buf, "fn foo() void {{}}");
    return buf[0..];
};
```  This approach is essentially text replacement, which is prone to security vulnerabilities (like injection attacks) and cannot undergo static analysis.
*   **Elaborator's Advantage**: (Assuming Rust's proc macro is an elaborator that can perform deeper analysis and type checking) Rust's procedural macros (proc-macro) can directly manipulate the AST: ```
#[derive(Debug)]  // Procedural macro automatically generates the implementation of the `Debug` trait
struct Point { x: i32, y: i32 }
```  This ability to operate at the AST level is type-safe and analyzable, while Zig's text replacement approach cannot achieve similar functionality.

#### **Inability to Intervene in Compilation Pipeline**[#](http://lemonhx.moe/macro?locale=en#user-content-inability-to-intervene-in-compilation-pipeline)

*   **Zig's Closure**: Zig's compilation pipeline is fixed, and developers cannot insert custom compilation stages (such as custom optimizations, code transformations). For example: 
    *   Cannot implement custom optimizations for intermediate representations (IR) like LLVM.
    *   Cannot inject dynamically generated code segments at compile time (like JIT compilation).

*   **Comparison with Lisp Family**: Lisp's macro system allows code transformations to be inserted at any compilation stage: ```
(defmacro at-compile-time (&body body)
  `(eval-when (:compile-toplevel) ,@body))
```  This capability allows Lisp to freely control the compilation pipeline, while Zig's compile-time execution cannot break through the language's preset pipeline stages.

### **Cost of Semantic Consistency**[#](http://lemonhx.moe/macro?locale=en#user-content-cost-of-semantic-consistency)

**Deep Contradiction**: Relying solely on compile-time execution for metaprogramming forces developers to impose the **mental model of language designers** on all metaprogramming behaviors, leading to an inability to achieve truly domain-specific abstractions.

#### **Inability to Implement Domain-Specific Languages (DSLs)**[#](http://lemonhx.moe/macro?locale=en#user-content-inability-to-implement-domain-specific-languages-dsls)

*   **Zig's Limitations**: Due to the lack of syntax macros, Zig cannot design dedicated syntax for specific domains (such as hardware description, protocol definition). For example: 
    *   Cannot implement hardware description syntax similar to Verilog.
    *   Cannot define query syntax similar to SQL.

*   **Elaborator's Breakthrough**: The elaborator in Idris can implement embedded DSLs through semantic macros: ```
query : DSL (List Person)
query = select [name, age] from people where (age > 30)
```  Here, `select` and `where` are DSL structures generated by macros, while Zig cannot achieve similar functionality.

#### **Forced Coupling of Semantic Consistency**[#](http://lemonhx.moe/macro?locale=en#user-content-forced-coupling-of-semantic-consistency)

*   **Zig's Cost**: All code generated at compile time must conform to Zig's semantic rules (such as memory safety, error handling), unable to relax or strengthen rules for specific scenarios. For example: 
    *   Cannot define a "no panic" subset of code in embedded development.
    *   Cannot disable safety checks for performance-critical code.

*   **Comparison with C++ Template Metaprogramming**: C++ templates, while complex, allow for semantic-level code generation through specialization and SFINAE: ```
template<typename T>
auto serialize(T t) -> decltype(t.toBytes()) { return t.toBytes(); }
```  This ability allows C++ to dynamically select serialization strategies based on types, while Zig's compile-time execution cannot achieve similar functionality.

| **Defect Dimension** | **Zig (Only Compile-time Execution)** | **Elaborator/Macro System** |
| --- | --- | --- |
| **Type System Extensibility** | Limited by language's preset type rules | Can dynamically generate type constraints and inference rules |
| **Syntax Structure Control** | Can only generate code that conforms to native syntax | Can define new syntax structures and semantic rules |
| **Intervention in Compilation Pipeline** | Fixed pipeline, cannot insert custom logic | Can freely control compilation stages and code transformations |
| **Domain-Specific Abstractions** | Cannot implement DSLs and domain-specific semantics | Supports embedded DSLs and domain-driven design |
| **Metaprogramming Safety** | Text replacement prone to security vulnerabilities | AST manipulation ensures syntax and type safety |

### **Ultimate Contradiction: Lack of Language Bootstrapping Capability**[#](http://lemonhx.moe/macro?locale=en#user-content-ultimate-contradiction-lack-of-language-bootstrapping-capability)

If a language cannot use its own mechanisms to achieve complete bootstrapping (i.e., using the language to write its own compiler and toolchain), then its metaprogramming capabilities have fundamental flaws. Zig's compile-time execution can accomplish some code generation, but it cannot achieve the following key capabilities:

1.   **Self-modifying Compiler**: Cannot write a compiler in Zig that can dynamically modify its own compilation logic.
2.   **Metaprogramming for Toolchain**: Cannot implement a meta-object protocol (MOP) similar to Lisp in Zig.
3.   **Autonomy of Language Evolution**: The expansion of language functionality must rely on modifications by the compiler author, rather than community-driven metaprogramming.

So why do I see that `C++` can do it but it doesn't look good and I don't dare to use it? What causes this?[#](http://lemonhx.moe/macro?locale=en#user-content-so-why-do-i-see-that-c-can-do-it-but-it-doesnt-look-good-and-i-dont-dare-to-use-it-what-causes-this)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

C++'s `template`, `constexpr`, and `concept` systems indeed have some design issues and ambiguities. We can critique C++'s design from three aspects: **Templates as Elaborators**, **Relationship Between `constexpr` and Templates**, and **Introduction of Concept Systems**.

### **C++ Templates as Elaborators**[#](http://lemonhx.moe/macro?locale=en#user-content-c-templates-as-elaborators)

*   **C++ Templates** are a compile-time code generation mechanism that allows developers to write generic code (such as generic programming). They can generate specific code instances at compile time.
*   **Limitations as Elaborators**: 
    1.   **Complex Syntax, Difficult to Understand**: 
        *   The syntax of C++ templates is very complex, especially when it comes to template specialization, SFINAE, and other techniques, which greatly reduce code readability and maintainability.
        *   For example, template metaprogramming (TMP) often requires writing obscure code, which contradicts the principle that elaborators should be clear and easy to use.

    2.   **Lack of Semantic Analysis**: 
        *   C++ templates are essentially a syntax replacement mechanism that does not perform deep semantic analysis. For example, templates cannot directly check whether types meet certain semantic constraints (before C++20).
        *   This leads to template errors that are often very obscure and difficult to debug.

    3.   **Limited Compile-time Computation Capability**: 
        *   The compile-time computation capability of C++ templates relies on template metaprogramming, which is not only difficult to use but also incurs significant performance overhead.
        *   For example, calculating the Fibonacci sequence using template metaprogramming: ```
template<int N>
struct Fibonacci {
    static const int value = Fibonacci<N-1>::value + Fibonacci<N-2>::value;
};
template<>
struct Fibonacci<0> {
    static const int value = 0;
};
template<>
struct Fibonacci<1> {
    static const int value = 1;
};
```  This code is not only difficult to write but also has poor readability.

### **Unclear Relationship Between `constexpr` and Templates**[#](http://lemonhx.moe/macro?locale=en#user-content-unclear-relationship-between-constexpr-and-templates)

*   **`constexpr`** is a feature introduced in C++11 that allows constant expressions to be computed at compile time.
*   **Issues**: 
    1.   **Overlap with Templates**: 
        *   Both `constexpr` and templates can be used for compile-time computation, but their design purposes and implementation methods are completely different.
        *   Templates are primarily used for code generation, while `constexpr` is mainly for constant computation. This functional overlap can confuse developers when using them.

    2.   **Limitations of `constexpr`**: 
        *   `constexpr` functions and variables have strict limitations, such as not allowing dynamic memory allocation or side effects. This restricts their expressive power.
        *   For example, `constexpr` functions cannot directly operate on types generated by templates, leading to a lack of smooth collaboration between the two.

    3.   **Lack of a Unified Compile-time Computation Model**: 
        *   C++ does not provide a unified compile-time computation model; templates and `constexpr` are two independent mechanisms. This increases language complexity and the learning cost for developers.

### **Introduction of C++ Concept Systems**[#](http://lemonhx.moe/macro?locale=en#user-content-introduction-of-c-concept-systems)

*   **Concepts** are a feature introduced in C++20 for constraining template parameters, improving the readability of templates and error messages.
*   **Issues**: 
    1.   **Timing of Introduction**: 
        *   The concept system was introduced only in C++20, while the template system has existed since C++98. This means that before the introduction of concepts, C++ developers had to endure years of obscure template error messages.

    2.   **Integration with Templates Not Natural Enough**: 
        *   The design of the concept system does not fully resolve the complexity of templates. For example, concepts still need to be used in conjunction with template syntax, leading to code that is still not intuitive.
        *   For example: ```
template<typename T>
requires Integral<T>
T add(T a, T b) {
    return a + b;
}
```  While concepts improve code readability, the syntax remains complex.

    3.   **Limited Expressive Power of Concepts**: 
        *   The concept system is mainly used for type constraints, but it cannot fully replace the functionality of template metaprogramming. For example, concepts cannot be directly used for compile-time computation or code generation.

Summary[#](http://lemonhx.moe/macro?locale=en#user-content-summary)
-------------------------------------------------------------------

The design level of the macro system directly determines the "self-evolving capability" of the language. Truly master-level tools (like Lisp, Racket) treat macros as first-class citizens of the language, rather than a patch mechanism added later.
