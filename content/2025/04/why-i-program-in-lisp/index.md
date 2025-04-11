---
title: Why I Program in Lisp
date: 2025-04-11
extra:
  source: http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html
  original_title: Why I Program in Lisp
---
## Summary
**摘要**：
作者阐述了自己偏爱使用Lisp编程的原因。尽管Lisp在流行度、库的数量和用户社区规模上不如其他通用语言，但作者仍然坚持使用Lisp进行原型设计和探索性编程。Lisp的优势在于其简洁的语法，统一的Cambridge Polish notation（也称为前缀表达式，运算符位于操作数之前，如`(+ 2 3)`），降低了记忆负担，减少了编程时的认知摩擦。Lisp对函数式编程提供了良好的支持，允许避免副作用，直接支持替换模型，便于代码重构。通过`lambda`表达式，Lisp能够方便地将表达式转换为函数，实现更高层次的抽象。函数式编程强调将复杂问题分解为简单函数的组合，Lisp在这一方面表现出色。Lisp的动态类型允许编写更具通用性的代码，可以用于多种数据类型，而其REPL环境（Read-Eval-Print Loop，交互式解释器）和调试器则可以加快开发速度和问题排查，同时Lisp的安全内存模型可以避免程序错误对工作区造成破坏。总而言之，Lisp为思考和解决问题提供了一种优秀的工具，使编程过程更加愉快。

**要点总结**：
1.  **简洁的语法和统一的表达方式**：Lisp使用Cambridge Polish notation，即前缀表达式，语法的统一性减少了记忆负担，降低了编程时的认知摩擦。这种表示方式对于所有操作都一致，无需记忆不同形式的括号或操作符优先级。
2.  **对函数式编程的良好支持**：Lisp支持无副作用的函数式编程，直接支持替换模型，便于代码重构和移动。函数式编程将问题分解为函数的组合，Lisp通过`lambda`表达式方便地将表达式转换为函数，实现更高层次的抽象。
3.  **灵活的抽象能力**：Lisp允许通过将变量替换为函数来计算数量，从而实现更高层次的抽象。`lambda`表达式使得将表达式转换为函数变得简单，这在其他语言中可能较为繁琐。
4.  **动态类型带来的通用性**：Lisp的动态类型允许编写可以用于多种数据类型的通用代码，只要这些数据类型支持程序中使用的操作符。
5.  **快速原型设计和交互式开发**：Lisp的REPL（交互式解释器，读取-求值-输出循环）允许快速尝试新想法，程序可以像语言内置功能一样被扩展。Lisp的调试器和安全内存模型增强了探索问题和调试的效率。

## Full Content
Title: Why I Program in Lisp

URL Source: http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html

Markdown Content:
Abstract Heresies: Why I Program in Lisp
===============  

 

[Abstract Heresies](http://funcall.blogspot.com/)
=================================================

Unorthodox opinions on computer science and programming.

Thursday, April 10, 2025
------------------------

 

### Why I Program in Lisp

Lisp is not the most popular language. It never was. Other general purpose languages are more popular and ultimately can do everything that Lisp can (if Church and Turing are correct). They have more libraries and a larger user community than Lisp does. They are more likely to be installed on a machine than Lisp is.

Yet I prefer to program in Lisp. I keep a Lisp REPL open at all times, and I write prototypes and exploratory code in Lisp. Why do I do this? Lisp is easier to remember, has fewer limitations and hoops you have to jump through, has lower “friction” between my thoughts and my program, is easily customizable, and, frankly, more fun.

Lisp's dreaded Cambridge Polish notation is uniform and universal. I don't have to remember whether a form takes curly braces or square brackets or what the operator precedency is or some weird punctuated syntax that was invented for no good reason. It is (operator operands ...) for everything. Nothing to remember. I basically stopped noticing the parenthesis 40 years ago. I can indent how I please.

I program mostly functionally, and Lisp has three features that help out tremendously here. First, if you avoid side effects, it directly supports the substitution model. You can tell Lisp that when it sees this simple form, it can just replace it with that more complex one. Lisp isn't constantly pushing you into thinking imperatively. Second, since the syntax is uniform and doesn't depend on the context, you can refactor and move code around at will. Just move things in balanced parenthesis and you'll pretty much be ok.

Third, in most computer languages, you can abstract a specific value by replacing it with a variable that names a value. But you can perform a further abstraction by replacing a variable that names a quantity with a function that computes a quantity. In functional programming, you often downplay the distinction between a value and a function that produces that value. After all, the difference is only one of time spent waiting for the answer. In Lisp, you can change an expression that denotes an object into an abtraction that computes an object by simply wrapping a `lambda` around it. It's less of a big deal these days, but properly working `lambda` expressions were only available in Lisp until recently. Even so, `lambda` expressions are generally pretty clumsy in other languages.

Functional programming focuses on functions (go figure!). These are the ideal black box abstraction: values go in, answer comes out. What happens inside? Who knows! Who cares! But you can plug little simple functions together and get bigger more complex functions. There is no limit on doing this. If you can frame your problem as "I have this, I want that", then you can code it as a functional program. It is true that functional programming takes a bit of practice to get used to, but it allows you to build complex systems out of very simple parts. Once you get the hang of it, you start seeing everything as a function. (This isn't a limitation. Church's lambda calculus is a model of computation based on functional composition.)

Lisp lets me try out new ideas as quickly as I can come up with them. New programs are indistinguishable from those built in to the language, so I can build upon them just as easily. Lisp's debugger means I don't have to stop everything and restart the world from scratch every time something goes wrong. Lisp's safe memory model means that bugs don't trash my workspace as I explore the problem.

The REPL in lisp evaluates _expressions_, which are the fundamental fragments of Lisp programs. You can type in part of a Lisp program and see what it does immediately. If it works, you can simply embed the expression in a larger program. Your program takes shape in real time as you explore the problem.

Lisp's dynamic typing gives you virtually automatic ad hoc polymorphism. If you write a program that calls +, it will work on any pair of objects that have a well-defined + operator. Now this can be a problem if you are cavalier about your types, but if you exercise a little discipline (like not defining + on combinations of strings and numbers, for example), and if you avoid automatic type coercion, then you can write very generic code that works on a superset of your data types. (Dynamic typing is a two-edged sword. It allows for fast prototyping, but it can hide bugs that would be caught at compile time in a statically typed language.)

Other languages may share some of these features, but Lisp has them all together. It is a language that was designed to be used as a tool for thinking about problems, and that is the fun part of programming.

Posted by [Joe Marshall](https://www.blogger.com/profile/03233353484280456977 "author profile") at  [12:00 AM](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html "permanent link")  [![Image 1](https://resources.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/8288194986820249216/3404727118065375102 "Email Post")[![Image 2](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=8288194986820249216&postID=3404727118065375102&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=8288194986820249216&postID=3404727118065375102&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=8288194986820249216&postID=3404727118065375102&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=8288194986820249216&postID=3404727118065375102&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=8288194986820249216&postID=3404727118065375102&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=8288194986820249216&postID=3404727118065375102&target=pinterest "Share to Pinterest")

Labels: [Common Lisp](http://funcall.blogspot.com/search/label/Common%20Lisp)

#### 8 comments:

![Image 3](http://resources.blogblog.com/img/blank.gif)

Anonymous said...

Could you please elaborate the last part about polymorphism? What I do not understand is: you mentioning the + (operator). Even if you would define a function named \`plus\`, in CL it is not possible to automatically dispatch on argument type. You would have to write the dispatching manually (e.g. via \`cond\`) inside that \`plus\` function. Only if you use CLOS, generic functions, and methods, the dispatch table is implicitly generated for you. Other languages like C++ (not C!) can do that, I know that feature by the name of \`operator overloading\`.

[April 11, 2025 at 1:23 AM](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html?showComment=1744359831563#c6063162546311623574 "comment permalink") [![Image 4](https://resources.blogblog.com/img/icon_delete13.gif)](https://www.blogger.com/comment/delete/8288194986820249216/6063162546311623574 "Delete Comment") 

[![Image 5](https://resources.blogblog.com/img/blank.gif)](https://www.blogger.com/profile/03233353484280456977)

[Joe Marshall](https://www.blogger.com/profile/03233353484280456977) said...

Ok, to be more specific.  
  
Ask a C programmer to write factorial and you will likely get something like this (excuse the underbars, they are there because blogger doesn't format code in comments):  
  
int factorial (int x) {  
\_\_\_\_if (x == 0)  
\_\_\_\_\_\_\_\_return 1;  
\_\_\_\_else  
\_\_\_\_\_\_\_\_return x \* factorial (x - 1);  
}  
  
And the Lisp programmer will give you:  
  
(defun factorial (x)  
\_\_(if (zerop x)  
\_\_\_\_\_\_1  
\_\_\_\_\_\_(\* x (factorial (- x 1)))))  
  
But now let's take the factorial of 54.0  
  
The C program won't do it, it is defined on ints.  
  
The Lisp program returns 2.308436973392414d71  
  
The C program is narrowly defined on the data type that the programmer guessed would be sufficient.  
  
The Lisp program is defined on any type that supports the zerop, \*, and - operators.  
  
Now it is true that if you mentioned this to the C programmer they could go back and re-write the program to handle bignums and floats (and rationals, and complexes, and matrices, and whatever weird number-like object that you send its way), but by default they don't do this.  
  
Lisp programmers get this for free.

[April 11, 2025 at 2:15 AM](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html?showComment=1744362944097#c3209271801284865243 "comment permalink") [![Image 7](https://resources.blogblog.com/img/icon_delete13.gif)](https://www.blogger.com/comment/delete/8288194986820249216/3209271801284865243 "Delete Comment") 

![Image 8](http://resources.blogblog.com/img/blank.gif)

Anonymous said...

The C type system is pretty puny, though. In a language with something like typeclasses (e.g. Haskell or Rust) you can constrain the types to the categories you need, with something like  
  
fac :: (Eq a, Num a, Enum a) =\> a -\> a  
fac 0 = 1  
fac n = n \* fac (pred n)  
  
and you can do \`fac 54.0\` and get \`2.308436973392414e71\` just fine, but going \`fac "a string"\` is a compilation error.  
  
Rust \_can\_ do the same thing, but the constraint gets a lot more verbose and you \_do\_ have to import some stuff to get arbitrary precision. E.g. running \`fac(54.0)\` on  
  
fn fac(x: T) -\> T  
where  
\_\_\_\_T: Clone + Copy + PartialEq + Sub + Mul + From,  
{  
\_\_\_\_if x == T::from(0) {  
\_\_\_\_\_\_\_\_T::from(1)  
\_\_\_\_} else {  
\_\_\_\_\_\_\_\_x \* fac(x - T::from(1))  
\_\_\_\_}  
}  
  
will net you an equally precise answer as your lisp example.  
  
You can even add some constraints like making sure the input is non-negative so you don't get into an unending loop at \`(factorial -1)\`. Good type systems add a lot of power. :)

[April 11, 2025 at 4:26 AM](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html?showComment=1744370788453#c4548670186844613959 "comment permalink") [![Image 9](https://resources.blogblog.com/img/icon_delete13.gif)](https://www.blogger.com/comment/delete/8288194986820249216/4548670186844613959 "Delete Comment") 

![Image 10](http://resources.blogblog.com/img/blank.gif)

Anonymous said...

The Rust example is missing a <T\> in fn fac<T\>(x: T) -\> T. Guessing blogspot eats HTML-like stuff

[April 11, 2025 at 4:28 AM](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html?showComment=1744370909576#c2444657668518822159 "comment permalink") [![Image 11](https://resources.blogblog.com/img/icon_delete13.gif)](https://www.blogger.com/comment/delete/8288194986820249216/2444657668518822159 "Delete Comment") 

![Image 12](http://resources.blogblog.com/img/blank.gif)

Gordon said...

Wonderful write-up! The one thing I’ll add, and honestly I could hear it in your voice, is that Lisp is aesthetically beautiful. It is beautiful in its overt simplicity and appealing to the eye. It is beautiful in its homoiconicity, its innate form and function.  
  
It genuinely makes me happy working in the REPL.

[April 11, 2025 at 5:49 AM](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html?showComment=1744375778016#c2529086334954592719 "comment permalink") [![Image 13](https://resources.blogblog.com/img/icon_delete13.gif)](https://www.blogger.com/comment/delete/8288194986820249216/2529086334954592719 "Delete Comment") 

![Image 14](http://resources.blogblog.com/img/blank.gif)

Simon said...

The C# example has become pretty neat after the introduction of numerical constraints on generic type arguments:  
  
T Factorial(T n) where T : INumber  
\=\> n == T.One ? T.One : n \* Factorial(n - T.One);

[April 11, 2025 at 7:02 AM](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html?showComment=1744380166635#c2804643619825864025 "comment permalink") [![Image 15](https://resources.blogblog.com/img/icon_delete13.gif)](https://www.blogger.com/comment/delete/8288194986820249216/2804643619825864025 "Delete Comment") 

![Image 16](http://resources.blogblog.com/img/blank.gif)

Anonymous said...

(+ < T \> in the signature)

[April 11, 2025 at 7:04 AM](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html?showComment=1744380263988#c5984757065470190936 "comment permalink") [![Image 17](https://resources.blogblog.com/img/icon_delete13.gif)](https://www.blogger.com/comment/delete/8288194986820249216/5984757065470190936 "Delete Comment") 

[![Image 18](https://resources.blogblog.com/img/blank.gif)](https://www.blogger.com/profile/03233353484280456977)

[Joe Marshall](https://www.blogger.com/profile/03233353484280456977) said...

(Trolling) So what I am hearing is  
"A sufficiently sophisticated static type system will allow you to express, with some verbosity, the constraints necessary for a compile time check equivalent to a naïve run time check."  
  
In all seriousness, though, let us conside Euclid's algorithm:  
  
(defun euclid (left right)  
\_\_(cond ((= left right) left)  
\_\_\_\_\_\_\_\_((\> left right) (euclid (- left right) right)))  
\_\_\_\_\_\_\_\_(t (euclid left (- right left))))  
  
Now you write it in your favorite statically typed language.  
  
The Common Lisp version of Euclid's algorithm will work on any type that is a Euclidean ring, e.g. univariate polynomials. Does your version handle those?  
  
My point is not that a dynamic type system is more expressive (it isn't), but that you get, without any effort, the more expansive interpretation of the types of the arguments. If you can live with the late-bound, run-time type checks, it is a sweet spot for prototyping. After you've figured out how to make it work, of course it is nice to cast the constraints in stone so that the compiler can make guarantees, and it is unfortunate that Lisp doesn't do that.

[April 11, 2025 at 7:26 AM](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html?showComment=1744381577837#c8654318448793124850 "comment permalink") [![Image 20](https://resources.blogblog.com/img/icon_delete13.gif)](https://www.blogger.com/comment/delete/8288194986820249216/8654318448793124850 "Delete Comment") 

[Post a Comment](https://www.blogger.com/comment/fullpage/post/8288194986820249216/3404727118065375102)

[Newer Post](http://funcall.blogspot.com/2025/04/bloom-filter.html "Newer Post") [Older Post](http://funcall.blogspot.com/2025/04/lisp-programs-dont-have-parentheses.html "Older Post") [Home](http://funcall.blogspot.com/)

Subscribe to: [Post Comments (Atom)](http://funcall.blogspot.com/feeds/3404727118065375102/comments/default)

Blog Archive
------------

*   [▼](javascript:void(0))  [2025](http://funcall.blogspot.com/2025/) (73)
    
    *   [▼](javascript:void(0))  [April](http://funcall.blogspot.com/2025/04/) (9)
        *   [Bloom Filter](http://funcall.blogspot.com/2025/04/bloom-filter.html)
        *   [Why I Program in Lisp](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html)
        *   [Lisp Programs Don't Have Parentheses](http://funcall.blogspot.com/2025/04/lisp-programs-dont-have-parentheses.html)
        *   [Are You Tail Recursive?](http://funcall.blogspot.com/2025/04/are-you-tail-recursive.html)
        *   [When Laymen Try to be Programmers](http://funcall.blogspot.com/2025/04/when-laymen-try-to-be-programmers.html)
        *   [Suddenly](http://funcall.blogspot.com/2025/04/suddenly.html)
        *   [Blacksmithing and Lisp](http://funcall.blogspot.com/2025/04/blacksmithing-and-lisp.html)
        *   [Lisp at Work](http://funcall.blogspot.com/2025/04/lisp-at-work.html)
        *   [Vibe Coding, final word](http://funcall.blogspot.com/2025/04/vibe-coding-final-word.html)
    
    *   [►](javascript:void(0))  [March](http://funcall.blogspot.com/2025/03/) (30)
    
    *   [►](javascript:void(0))  [February](http://funcall.blogspot.com/2025/02/) (20)
    
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2025/01/) (14)

*   [►](javascript:void(0))  [2024](http://funcall.blogspot.com/2024/) (45)
    
    *   [►](javascript:void(0))  [December](http://funcall.blogspot.com/2024/12/) (10)
    
    *   [►](javascript:void(0))  [November](http://funcall.blogspot.com/2024/11/) (1)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2024/10/) (1)
    
    *   [►](javascript:void(0))  [July](http://funcall.blogspot.com/2024/07/) (3)
    
    *   [►](javascript:void(0))  [June](http://funcall.blogspot.com/2024/06/) (7)
    
    *   [►](javascript:void(0))  [May](http://funcall.blogspot.com/2024/05/) (12)
    
    *   [►](javascript:void(0))  [April](http://funcall.blogspot.com/2024/04/) (4)
    
    *   [►](javascript:void(0))  [March](http://funcall.blogspot.com/2024/03/) (3)
    
    *   [►](javascript:void(0))  [February](http://funcall.blogspot.com/2024/02/) (2)
    
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2024/01/) (2)

*   [►](javascript:void(0))  [2023](http://funcall.blogspot.com/2023/) (10)
    
    *   [►](javascript:void(0))  [November](http://funcall.blogspot.com/2023/11/) (1)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2023/10/) (1)
    
    *   [►](javascript:void(0))  [September](http://funcall.blogspot.com/2023/09/) (1)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2023/08/) (1)
    
    *   [►](javascript:void(0))  [July](http://funcall.blogspot.com/2023/07/) (2)
    
    *   [►](javascript:void(0))  [June](http://funcall.blogspot.com/2023/06/) (3)
    
    *   [►](javascript:void(0))  [May](http://funcall.blogspot.com/2023/05/) (1)

*   [►](javascript:void(0))  [2022](http://funcall.blogspot.com/2022/) (14)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2022/10/) (2)
    
    *   [►](javascript:void(0))  [September](http://funcall.blogspot.com/2022/09/) (3)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2022/08/) (1)
    
    *   [►](javascript:void(0))  [July](http://funcall.blogspot.com/2022/07/) (4)
    
    *   [►](javascript:void(0))  [March](http://funcall.blogspot.com/2022/03/) (1)
    
    *   [►](javascript:void(0))  [February](http://funcall.blogspot.com/2022/02/) (2)
    
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2022/01/) (1)

*   [►](javascript:void(0))  [2021](http://funcall.blogspot.com/2021/) (13)
    
    *   [►](javascript:void(0))  [December](http://funcall.blogspot.com/2021/12/) (1)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2021/10/) (1)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2021/08/) (3)
    
    *   [►](javascript:void(0))  [May](http://funcall.blogspot.com/2021/05/) (4)
    
    *   [►](javascript:void(0))  [April](http://funcall.blogspot.com/2021/04/) (3)
    
    *   [►](javascript:void(0))  [March](http://funcall.blogspot.com/2021/03/) (1)

*   [►](javascript:void(0))  [2020](http://funcall.blogspot.com/2020/) (22)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2020/10/) (1)
    
    *   [►](javascript:void(0))  [February](http://funcall.blogspot.com/2020/02/) (6)
    
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2020/01/) (15)

*   [►](javascript:void(0))  [2019](http://funcall.blogspot.com/2019/) (5)
    *   [►](javascript:void(0))  [December](http://funcall.blogspot.com/2019/12/) (5)

*   [►](javascript:void(0))  [2016](http://funcall.blogspot.com/2016/) (4)
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2016/01/) (4)

*   [►](javascript:void(0))  [2015](http://funcall.blogspot.com/2015/) (8)
    
    *   [►](javascript:void(0))  [September](http://funcall.blogspot.com/2015/09/) (6)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2015/08/) (2)

*   [►](javascript:void(0))  [2014](http://funcall.blogspot.com/2014/) (11)
    
    *   [►](javascript:void(0))  [September](http://funcall.blogspot.com/2014/09/) (4)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2014/08/) (7)

*   [►](javascript:void(0))  [2013](http://funcall.blogspot.com/2013/) (24)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2013/10/) (2)
    
    *   [►](javascript:void(0))  [September](http://funcall.blogspot.com/2013/09/) (3)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2013/08/) (2)
    
    *   [►](javascript:void(0))  [July](http://funcall.blogspot.com/2013/07/) (12)
    
    *   [►](javascript:void(0))  [May](http://funcall.blogspot.com/2013/05/) (1)
    
    *   [►](javascript:void(0))  [April](http://funcall.blogspot.com/2013/04/) (2)
    
    *   [►](javascript:void(0))  [March](http://funcall.blogspot.com/2013/03/) (1)
    
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2013/01/) (1)

*   [►](javascript:void(0))  [2012](http://funcall.blogspot.com/2012/) (14)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2012/08/) (1)
    
    *   [►](javascript:void(0))  [July](http://funcall.blogspot.com/2012/07/) (1)
    
    *   [►](javascript:void(0))  [June](http://funcall.blogspot.com/2012/06/) (1)
    
    *   [►](javascript:void(0))  [April](http://funcall.blogspot.com/2012/04/) (3)
    
    *   [►](javascript:void(0))  [March](http://funcall.blogspot.com/2012/03/) (3)
    
    *   [►](javascript:void(0))  [February](http://funcall.blogspot.com/2012/02/) (2)
    
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2012/01/) (3)

*   [►](javascript:void(0))  [2011](http://funcall.blogspot.com/2011/) (51)
    
    *   [►](javascript:void(0))  [November](http://funcall.blogspot.com/2011/11/) (4)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2011/10/) (9)
    
    *   [►](javascript:void(0))  [September](http://funcall.blogspot.com/2011/09/) (4)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2011/08/) (1)
    
    *   [►](javascript:void(0))  [April](http://funcall.blogspot.com/2011/04/) (5)
    
    *   [►](javascript:void(0))  [March](http://funcall.blogspot.com/2011/03/) (9)
    
    *   [►](javascript:void(0))  [February](http://funcall.blogspot.com/2011/02/) (10)
    
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2011/01/) (9)

*   [►](javascript:void(0))  [2010](http://funcall.blogspot.com/2010/) (57)
    
    *   [►](javascript:void(0))  [December](http://funcall.blogspot.com/2010/12/) (4)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2010/10/) (1)
    
    *   [►](javascript:void(0))  [September](http://funcall.blogspot.com/2010/09/) (1)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2010/08/) (8)
    
    *   [►](javascript:void(0))  [July](http://funcall.blogspot.com/2010/07/) (1)
    
    *   [►](javascript:void(0))  [June](http://funcall.blogspot.com/2010/06/) (8)
    
    *   [►](javascript:void(0))  [May](http://funcall.blogspot.com/2010/05/) (8)
    
    *   [►](javascript:void(0))  [April](http://funcall.blogspot.com/2010/04/) (18)
    
    *   [►](javascript:void(0))  [March](http://funcall.blogspot.com/2010/03/) (4)
    
    *   [►](javascript:void(0))  [February](http://funcall.blogspot.com/2010/02/) (3)
    
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2010/01/) (1)

*   [►](javascript:void(0))  [2009](http://funcall.blogspot.com/2009/) (114)
    
    *   [►](javascript:void(0))  [December](http://funcall.blogspot.com/2009/12/) (5)
    
    *   [►](javascript:void(0))  [November](http://funcall.blogspot.com/2009/11/) (2)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2009/10/) (13)
    
    *   [►](javascript:void(0))  [September](http://funcall.blogspot.com/2009/09/) (10)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2009/08/) (9)
    
    *   [►](javascript:void(0))  [July](http://funcall.blogspot.com/2009/07/) (19)
    
    *   [►](javascript:void(0))  [June](http://funcall.blogspot.com/2009/06/) (6)
    
    *   [►](javascript:void(0))  [May](http://funcall.blogspot.com/2009/05/) (7)
    
    *   [►](javascript:void(0))  [April](http://funcall.blogspot.com/2009/04/) (12)
    
    *   [►](javascript:void(0))  [March](http://funcall.blogspot.com/2009/03/) (21)
    
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2009/01/) (10)

*   [►](javascript:void(0))  [2008](http://funcall.blogspot.com/2008/) (62)
    
    *   [►](javascript:void(0))  [December](http://funcall.blogspot.com/2008/12/) (1)
    
    *   [►](javascript:void(0))  [November](http://funcall.blogspot.com/2008/11/) (2)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2008/10/) (4)
    
    *   [►](javascript:void(0))  [September](http://funcall.blogspot.com/2008/09/) (7)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2008/08/) (13)
    
    *   [►](javascript:void(0))  [July](http://funcall.blogspot.com/2008/07/) (11)
    
    *   [►](javascript:void(0))  [May](http://funcall.blogspot.com/2008/05/) (5)
    
    *   [►](javascript:void(0))  [April](http://funcall.blogspot.com/2008/04/) (7)
    
    *   [►](javascript:void(0))  [March](http://funcall.blogspot.com/2008/03/) (6)
    
    *   [►](javascript:void(0))  [February](http://funcall.blogspot.com/2008/02/) (5)
    
    *   [►](javascript:void(0))  [January](http://funcall.blogspot.com/2008/01/) (1)

*   [►](javascript:void(0))  [2007](http://funcall.blogspot.com/2007/) (61)
    
    *   [►](javascript:void(0))  [December](http://funcall.blogspot.com/2007/12/) (3)
    
    *   [►](javascript:void(0))  [November](http://funcall.blogspot.com/2007/11/) (4)
    
    *   [►](javascript:void(0))  [October](http://funcall.blogspot.com/2007/10/) (5)
    
    *   [►](javascript:void(0))  [September](http://funcall.blogspot.com/2007/09/) (8)
    
    *   [►](javascript:void(0))  [August](http://funcall.blogspot.com/2007/08/) (5)
    
    *   [►](javascript:void(0))  [July](http://funcall.blogspot.com/2007/07/) (8)
    
    *   [►](javascript:void(0))  [June](http://funcall.blogspot.com/2007/06/) (10)
    
    *   [►](javascript:void(0))  [May](http://funcall.blogspot.com/2007/05/) (5)
    
    *   [►](javascript:void(0))  [April](http://funcall.blogspot.com/2007/04/) (13)

*   [►](javascript:void(0))  [2006](http://funcall.blogspot.com/2006/) (1)
    *   [►](javascript:void(0))  [December](http://funcall.blogspot.com/2006/12/) (1)

<table border="0" cellpadding="0" cellspacing="0" class="section-columns columns-2"><tbody><tr><td class="first columns-cell"><div class="sidebar no-items section" id="sidebar-right-2-1"></div></td><td class="columns-cell"><div class="sidebar no-items section" id="sidebar-right-2-2"></div></td></tr></tbody></table>

<table border="0" cellpadding="0" cellspacing="0" class="section-columns columns-2"><tbody><tr><td class="first columns-cell"><div class="foot no-items section" id="footer-2-1"></div></td><td class="columns-cell"><div class="foot no-items section" id="footer-2-2"></div></td></tr></tbody></table>

Powered by [Blogger](https://www.blogger.com/).

