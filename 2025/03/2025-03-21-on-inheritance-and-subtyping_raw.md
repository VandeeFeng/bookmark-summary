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
