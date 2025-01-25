Title: The 7 Most Influential Papers in Computer Science History

URL Source: https://terriblesoftware.org/2025/01/22/the-7-most-influential-papers-in-computer-science-history/

Published Time: 2025-01-22T18:52:59+00:00

Markdown Content:
Before we begin, let me be clear: yes, this _is_ a subjective list. It’s not meant to end the debate — but to start it. These seven papers (sorted by date) stand out to me mostly because of their impact in today’s world. Honestly, each one deserves a blog post (or even a book!) of its own — but let’s keep it short for now. If your favorite doesn’t show up here, don’t worry, stick around for the bonus section at the end, where I’ll call out a few more that came _this_ close to making the main list. So let’s dive in!

###   
**1\. “On Computable Numbers, with an Application to the Entscheidungsproblem” (1936)**

**Author:** Alan Turing

It’s the 1930s, and a “programmable machine” sounds like something out of a sci-fi novel. Then along comes Alan Turing, laying the groundwork for what computers can theoretically do. He sketches out a hypothetical “Turing Machine,” proving that, if something is computable at all, a machine (in principle) can handle it.

#### **The big idea**

Turing’s simple model — just a tape, a head for reading/writing, and a finite set of states, turned into the granddaddy of all modern computation. It defined what’s solvable (and what’s not) in a purely mechanical sense, basically giving us the “rules of the game” for digital problem-solving.

#### **Why it matters today**

Every single programming language, every single piece of code out there, is playing by Turing’s rules. Even when we talk about quantum computing, we’re still referencing the boundaries Turing described. That’s a huge testament to the power of one paper published in the mid-1930s.

#### **Learn more**

*   [https://www.cs.virginia.edu/~robins/Turing\_Paper\_1936.pdf](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf)
*   [https://en.wikipedia.org/wiki/Turing%27s\_proof](https://en.wikipedia.org/wiki/Turing%27s_proof)
*   [https://www.youtube.com/watch?v=dNRDvLACg5Q](https://www.youtube.com/watch?v=dNRDvLACg5Q)

###   
**2\. “A Mathematical Theory of Communication” (1948)**

**Author:** Claude Shannon

Now that Turing showed us what machines can (and can’t) do, how do we actually move information around? Enter Claude Shannon, who basically invented [information theory](https://en.wikipedia.org/wiki/Information_theory) so we could talk about bits, entropy, and noisy channels in a rigorous way.

#### **The big idea**

Shannon took the abstract notion of “information” and turned it into something a little _bit_ (pun intended) more measurable. This helped us figure out how to pack data more efficiently (compression) and how to protect it from errors (error-correcting codes), whether we’re sending signals into space or streaming Netflix on a Friday night.

#### **Why it matters today**

Every single time you send a text, stream a video, or call your mom on FaceTime, you’re using Shannon’s ideas. Without them, you’d be dealing with a lot more scrambled audio and jumbled data, trust me.

#### ****Learn more****

*   [https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)
*   [https://en.wikipedia.org/wiki/A\_Mathematical\_Theory\_of\_Communication](https://en.wikipedia.org/wiki/A_Mathematical_Theory_of_Communication)
*   [https://www.youtube.com/watch?v=b6VdGHSV6qg](https://www.youtube.com/watch?v=b6VdGHSV6qg)
*   [https://www.youtube.com/watch?v=kP0zi5lX-Fo](https://www.youtube.com/watch?v=kP0zi5lX-Fo)

###   
**3\. “A Relational Model of Data for Large Shared Data Banks” (1970)**

**Author:** Edgar F. Codd

So, we can compute and communicate — awesome. But eventually, we’re buried under mountains of data. Edgar F. Codd saw this coming and introduced the relational model, which is basically the reason we’re able to store and query data.

#### **The big idea**

Codd said, “Let’s store data in tables and manipulate it with logical operations.” This might sound obvious now, but at the time it was revolutionary. His blueprint led to SQL and the huge family of relational databases that power, oh, basically every bank, retail website, and enterprise system you can imagine.

#### **Why it matters today**

Even in the NoSQL era, the underlying concepts of how we organize data (tables, schemas, consistency) trace right back to Codd. If you ever wrote a SQL query in your life — it’s all thanks to him.

#### **Learn more**

*   [https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf)
*   [https://en.wikipedia.org/wiki/Codd%27s\_12\_rules](https://en.wikipedia.org/wiki/Codd%27s_12_rules)

###   
**4\. “The Complexity of Theorem-Proving Procedures” (1971)**

**Author:** Stephen A. Cook

Now that we’re storing data efficiently, what about the computation itself? Turns out some problems are just…painfully hard. Stephen Cook’s paper introduced NP-completeness, a concept that basically says, “Yep, some tasks are so difficult that even supercomputers sweat.”

#### **The big idea**

Cook showed that the [Boolean satisfiability problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem) (SAT) is NP-complete, meaning if you magically solve SAT quickly, you’ve instantly cracked a whole bunch of other seemingly impossible problems. This created a universal language for talking about problem difficulty.

#### **Why it matters today**

Whenever you see “NP-hard” in a problem description, or wonder why route optimization kills your CPU, that’s Cook’s legacy. It led to huge developments in algorithms, cryptography, and the hunt for efficient solutions (or at least decent approximations).

#### **Learn more**

*   [https://www.inf.unibz.it/~calvanese/teaching/14-15-tc/material/cook-1971-NP-completeness-of-SAT.pdf](https://www.inf.unibz.it/~calvanese/teaching/14-15-tc/material/cook-1971-NP-completeness-of-SAT.pdf)
*   [https://en.wikipedia.org/wiki/P\_versus\_NP\_problem](https://en.wikipedia.org/wiki/P_versus_NP_problem)
*   [https://www.youtube.com/watch?v=dJUEkjxylBw](https://www.youtube.com/watch?v=dJUEkjxylBw)

###   
**5\. “A Protocol for Packet Network Intercommunication” (1974)**

**Authors:** Vinton G. Cerf and Robert E. Kahn

Great, we have tough problems to solve and data to store — but how do we hook all these computers together? Cerf and Kahn’s TCP turned isolated networks into an interconnected web, letting data hop around the planet in tiny packets.

### **The big idea**

They created a universal language for different networks to talk. Packets get split up, zipped through various routes, and reassembled on the other side. This flexibility opened the door for global connectivity — no single monolithic network required.

### **Why it matters today**

Short answer? Pretty much the entire internet. Whenever you browse the web, send an email, or securely log in to your bank’s website, you’re leaning on TCP/IP to move those bits around reliably. Sure, some real-time applications might use UDP, but the core idea of IP-based networking — laid out by Cerf and Kahn — still unites all our devices under one global network.

### **Learn more**

*   [https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf](https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf)
*   [https://www.youtube.com/watch?v=PG9oKZdFb7w](https://www.youtube.com/watch?v=PG9oKZdFb7w)

###   
**6\. “Information Management: A Proposal” (1989)**

**Author:** Tim Berners-Lee

And speaking of TCP/IP — once machines could talk to each other easily, Tim Berners-Lee asked, “How about we make this thing friendly for everyone?” That’s where the World Wide Web was born.

### **The big idea**

Berners-Lee pitched a global hypertext system, complete with hyperlinks, URLs, and HTTP. Suddenly, documents around the world were no longer isolated; they were “webbed” together, turning the internet into something normal people (not just scientists) could navigate.

### **Why it matters today**

We live on the web. Whether it’s social media, online shopping, or reading obscure blog posts at 3 a.m., the seeds of it all came from this straightforward proposal. It changed how we share knowledge forever.

### Learn more

*   [https://cds.cern.ch/record/369245/files/dd-89-001.pdf](https://cds.cern.ch/record/369245/files/dd-89-001.pdf)
*   [https://time.com/21039/tim-berners-lee-web-proposal-at-25/](https://time.com/21039/tim-berners-lee-web-proposal-at-25/)
*   [https://www.youtube.com/watch?v=qJNrvVv7SdU](https://www.youtube.com/watch?v=qJNrvVv7SdU)

###   
**7\. “The Anatomy of a Large-Scale Hypertextual Web Search Engine” (1998)**

**Authors:** Sergey Brin and Larry Page

Once Berners-Lee’s web blew up, it became a jungle of links, pages, and cat memes. Sergey Brin and Larry Page decided to tame that jungle. Their approach, based on link analysis, evolved into the search engine we now call “Google.”

### **The big idea**

They introduced PageRank, which viewed links as votes of confidence rather than just a new dimension to count keywords. The result was a seismic jump in relevant search results, making the web feel, well…searchable.

### ****Why it matters today****

Type a question into Google and get an instant answer? That’s PageRank (and a lot of subsequent innovation) at work. It redefined how we navigate information online and kicked off a new era of data-driven tech—ads, analytics, machine learning, you name it.

### Learn more

*   [https://snap.stanford.edu/class/cs224w-readings/Brin98Anatomy.pdf](https://snap.stanford.edu/class/cs224w-readings/Brin98Anatomy.pdf)
*   [https://en.wikipedia.org/wiki/PageRank](https://en.wikipedia.org/wiki/PageRank)
*   [https://www.youtube.com/watch?v=v7n7wZhHJj8&t=184s](https://www.youtube.com/watch?v=v7n7wZhHJj8&t=184s)

* * *

Bonuses (5 That Almost Made the List)
-------------------------------------

1\. **“Recursive Functions of Symbolic Expressions and Their Computation by Machine” (1960) – John McCarthy**

Introduced Lisp and the functional programming style that still sneaks into modern languages and frameworks.

2\. **“Go To Statement Considered Harmful” (1968) – Edsger Dijkstra**

A short but fiery editorial that argued **goto** leads to messy, unstructured code, sparking the structured programming revolution.

3\. **“Time, Clocks, and the Ordering of Events in a Distributed System” (1978) – Leslie Lamport**

You can’t sync real clocks perfectly in distributed systems, so you need logical ones. This is a must-read if you’re into distributed computing.

4\. ****“No Silver Bullet—Essence and Accident in Software Engineering” (1986) – Fred Brooks****

Brooks argued that there’s no single magical fix for the inherent complexity of software development. Decades later, as we chase the “next big thing” in frameworks or methodologies, his message remains a sobering reminder that some problems are just hard.

5\. **“Attention Is All You Need” (2017) – Vaswani et al.**

The transformer architecture behind GPT and other big-name AI models. If you’re impressed by large language models, here’s your blueprint.

**Conclusion**
--------------

These days, we’re flooded with new stuff: fresh languages, mind-blowing AI breakthroughs, quantum leaps, and the JavaScript framework of the week. It’s all super exciting, but here’s the thing: foundations matter. Without them, we’re just piling on new toys without fully understanding the ground we’re building on. The papers in this post are a reminder of where our core concepts — data structures, algorithms, the very web — came from.
