---
title: On inheritance and subtyping
date: 2025-03-21
extra:
  source: https://blog.frankel.ch/on-inheritance/
  original_title: On inheritance and subtyping
---
## Summary
**摘要**：
作者回顾了自己学习Java作为职业生涯的第一门语言的经历，以及后来接触到的多种编程语言，这些经历让他对继承的概念有了更广阔的理解。文章探讨了Java中继承与子类型的紧密联系，即子类型实现了“IS A”关系，例如Rabbit类是Mammal类的子类型，从而继承了Mammal类的行为。接着，文章分析了Go语言在没有子类型的情况下如何实现继承，通过鸭子类型，如果一个结构体实现了接口的相同函数，那么它就隐式地实现了该接口。随后，文章深入研究了Python中继承的实现方式，包括子类型和基于类型的继承，以及通过实现`iter()`和`next()`等“魔法方法”实现的鸭子类型。最后，文章提到了PEP 544协议，它通过引入Protocol类，使得Python可以为自定义类提供静态鸭子类型。作者总结说，面向对象编程、继承和子类型等概念在不同语言中可能有不同的含义，理解这些差异对于用目标语言编写地道的代码至关重要，同时，熟悉不同于已知语言的特性，可以拓宽对编程的整体理解。

**要点总结**：
1.  Java中继承与子类型紧密相关，子类型通过“IS A”关系实现继承，例如`Rabbit`类是`Mammal`类的子类型，因此`Rabbit`实例可以像`Mammal`实例一样使用。这意味着在需要`Mammal`类型参数的方法中，可以传入`Rabbit`类型的实例。

2.  Go语言通过鸭子类型实现继承，即使没有显式的子类型关系，只要一个结构体实现了接口所需的所有方法，它就被认为是该接口的实现。例如，如果`Rabbit`结构体实现了`Animal`接口的`feed()`方法，那么`Rabbit`就被认为是`Animal`。

3.  Python同时支持显式继承和鸭子类型。显式继承类似于Java，通过子类继承父类的特性。鸭子类型则通过实现特定的“魔法方法”（如`__iter__()`和`__next__()`）来实现，使得类可以表现出某种类型的行为，例如，实现这两个方法的类可以被迭代。

4.  Python的PEP 544协议引入了静态鸭子类型，允许为自定义类定义“魔法方法”，从而实现隐式继承。通过继承`Protocol`类，类中定义的方法可以被其他类通过鸭子类型来实现，使得类型检查更加灵活。

5.  理解不同编程语言中继承和子类型的不同实现方式对于编写符合语言习惯的代码至关重要。学习新语言时，应特别关注那些在已知语言中不存在的特性，这有助于拓宽对编程的整体理解。

## Full Content
Title: On inheritance and subtyping

URL Source: https://blog.frankel.ch/on-inheritance/

Published Time: 2025-01-26T00:00:00+00:00

Markdown Content:
This website uses cookies to ensure you get the best experience on our website. Learn more
Got it!
A Java geek
ME
BOOKS
SPEAKING
MENTIONS
FOCUS
JAN 26, 2025
/
PROGRAMMING
,
CODING
,
OOP
On inheritance and subtyping

Java is the first language I learned in my career. Its structure is foundational in my early years of understanding programming concepts. After going through several other languages with very different approaches, I’ve widened my point of view. Today, I want to reflect on the idea of inheritance.

Inheritance in Java

In Java, the idea of inheritance is tightly coupled with the concept of subtyping. Subtyping is the implementation of a IS A relationship. For example, the Rabbit class is a subtype of the Mammal class. Henceforth, a Rabbit instance has all the behaviour of a Mammal: it inherits the behaviour.

Because of this, you can pass a Rabbit instance when a method calls for a Mammal parameter or return a Rabbit instance when a method return type is Mammal. If you’ve learned Java, .Net, or anything remotely similar, that’s how you see inheritance, and it becomes the new normal.

It is explicit inheritance.

class Animal {
    void feed();
}

class Rabbit extends Animal {                     
}
	Because a Rabbit IS A Animal, it can feed()
Inheritance in Go

When I first looked at Go, I was amazed that it does not have subtyping while still providing inheritance. Go uses duck typing:

If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is.

If a Go struct implements the same functions as an interface, it implicitly implements the interface.

type Animal interface {
    feed()                                        
}

type Rabbit struct {
}

func (rabbit Rabbit) feed() {                     
    // feeds
}
	An Animal can feed
	Because a feed() function exists that takes a Rabbit as a parameter, Rabbit implements Animal

I do dislike Go for its error-handling approach, but I was of two minds about implicit implementation. On one side, I understood it was a new concept, and I tried to stay open-minded; on the other hand, I think things are always better explicit than implicit, either in software development or real life.

Inheritance in Python

Python is the most interesting language I know of regarding inheritance.

Subtyping and type-based inheritance have been present in Python since its inception.

class Animal:
    def feed(self):                               
        pass                                      

class Rabbit(Animal):                             
    pass
	An Animal can feed
	There are no abstract classes nor interfaces in Python, only classes
	Because a Rabbit IS A Animal, it can feed()

In this regard, Python works the same as Java in terms of inheritance. Python also offers duck typing, which I described as magic methods. For example, to make something iterable, e.g., that can return an iterator, you only need to implement iter() and next():

class SingleValueIterable():

    done = False

    def __init__(self, value):
        self.value = value

    def __iter__(self):                           
        return self

    def __next__(self):                           
        if self.done:
            raise StopIteration
        else:
            self.done = True
            return self.value


svi = SingleValueIterable(5)
sviter = iter(svi)                                

for x in sviter:
    print(x)                                      
	Duck typing methods
	Create an Iterator - Pythons knows how since we implemented the methods above
	Print 5

The problem with this duck typing approach is that it works only for Python’s predefined magic methods. What if you want to offer a class that a third party could inherit from implicitly?

class Animal:

    def feed():
        pass


class Rabbit:

    def feed():
        pass

In the above snippet, Rabbit is not an Animal, much to our chagrin. Enter PEP 544, titled Protocols: Structural subtyping (static duck typing). The PEP solves the impossibility of defining magic methods for our classes. It defines a simple Protocol class: once you inherit from it, methods defined in the class become eligible for duck typing, hence the name - static duck typing.

from typing import Protocol

class Animal(Protocol):                           

    def feed():                                   
        pass


class Rabbit:

    def feed():                                   
        pass


class VenusFlytrap:

    def feed():                                   
        pass
	Inherit from Protocol
	Because Animal is a Protocol, any class that defines feed() becomes an Animal, for better or worse
Conclusion

Object-oriented programming, inheritance, and subtyping may have specific meanings that don’t translate into other languages, depending on the first language you learn. Java touts itself as an Object-Oriented language and offers the complete package. Go isn’t an OO language, but it still offers subtyping via duck typing. Python offers both explicit and implicit inheritance but no interfaces.

You learn a new programming language by comparing it with the one(s) you already know. Knowing a language’s features is key to writing idiomatic code in your target language. Familiarize yourself with features that don’t exist in your known languages: they will widen your understanding of programming as a whole.

 To go further:
Inheritance (object-oriented programming)
Duck typing
Python Protocol
Follow me  Follow me 
Nicolas Fränkel

Nicolas Fränkel is a technologist focusing on cloud-native technologies, DevOps, CI/CD pipelines, and system observability. His focus revolves around creating technical content, delivering talks, and engaging with developer communities to promote the adoption of modern software practices. With a strong background in software, he has worked extensively with the JVM, applying his expertise across various industries. In addition to his technical work, he is the author of several books and regularly shares insights through his blog and open-source contributions.

Read More
— A Java geek —
Programming
The pitfall of implicit returns
Conclusion of Exercises in Programming Style
Exercises in MapReduce Style
See all 21 posts →
FEB 2, 2025
DEVPOD
REMOTE DEVELOPMENT ENVIRONMENT
CLOUD DEVELOPMENT ENVIRONMENT
CLOUD
Remote Development made simple with DevPod

I come relatively late to the subject of Remote Development Environments (also known as Cloud Development Environments). The main reason is that I haven’t worked in a development team for over six years. However, I’m now working for Loft Labs, and we have a RDE product: DevPod. I wanted to understand our value proposition as I’ll be at FOSDEM operating the DevPod booth. The problem As a former developer, I vividly remember the pain of setting up each developer’s develo

 NICOLAS FRÄNKEL
JAN 19, 2025
METRICS
PLAYWRIGHT
BROWSER AUTOMATION
My first steps with Playwright

In my previous company, I developed a batch job that tracked metrics across social media, such as Twitter, LinkedIn, Mastodon, Bluesky, Reddit, etc. Then I realized I could duplicate it for my own 'persona'. The problem is that some media don’t provide an HTTP API for the metrics I want. Here are the metrics I want on LinkedIn: I searched for a long time but found no API access for the metrics above. I scraped the metrics manually every morning for a long time and finally decided to au

 NICOLAS FRÄNKEL
A Java geek © 2008-2025
v. 022010bbf87bacd9fcaa398a78d78a240e9bb637/9468160199
Latest Posts

