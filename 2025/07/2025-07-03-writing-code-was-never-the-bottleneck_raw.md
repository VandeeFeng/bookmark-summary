Title: Writing Code Was Never The Bottleneck

URL Source: https://ordep.dev/posts/writing-code-was-never-the-bottleneck

Published Time: 2025-06-30T00:00:00+00:00

Markdown Content:
For years, I’ve felt that writing lines of code _was never_ the bottleneck in software engineering.

The actual bottlenecks were, and still are, **code reviews**, **knowledge transfer** through mentoring and pairing, **testing**, **debugging**, and the human overhead of **coordination and communication**. All of this wrapped inside the labyrinth of tickets, planning meetings, and agile rituals.

These processes, meant to drive quality, often slow us down more than the act of writing code itself because they require thought, shared understanding, and sound judgment.

Now, with LLMs making it easy to generate working code faster than ever, a new narrative has emerged: that writing code _was_ the bottleneck, and we’ve finally cracked it.

But that’s **not quite right**.

The marginal cost of adding new software is approaching **zero**, especially with LLMs. But what is the price of _understanding_, _testing_, and _trusting_ that code? **Higher than ever**.

* * *

LLMs shift the workload — they don’t remove it
----------------------------------------------

Tools like Claude can speed up initial implementation. Still, the result is often more code flowing through systems and more pressure on the people responsible for reviewing, integrating, and maintaining it.

This becomes especially clear when:

*   It’s unclear whether the author fully understands what they submitted.
*   The generated code introduces unfamiliar patterns or breaks established conventions.
*   Edge cases and unintended side effects aren’t obvious.

We end up in a situation where code is more straightforward to produce but more complex to verify, which doesn’t necessarily make teams move faster overall.

It’s not a new challenge. Developers have long joked about **“copy-paste engineering”**, but the velocity and scale that LLMs enable have **amplified those copy-paste habits**.

* * *

Understanding code is still the hard part
-----------------------------------------

> _“The biggest cost of code is understanding it — not writing it.”_

LLMs reduce the time it takes to produce code, but they haven’t changed the amount of effort required to reason about behavior, identify subtle bugs, or ensure long-term maintainability. That work can be even more challenging when reviewers struggle to distinguish between generated and handwritten code or understand why a particular solution was chosen.

* * *

Teams still rely on trust and shared context
--------------------------------------------

Software engineering has always been collaborative. It depends on **shared understanding**, **alignment**, and **mentoring**. However, when code is generated faster than it can be discussed or reviewed, teams risk falling into a mode where **quality is assumed rather than ensured**. That creates stress on reviewers and mentors, potentially slowing things down in more subtle ways.

* * *

LLMs are powerful — but they don’t fix the fundamentals
-------------------------------------------------------

There’s real value in faster prototyping, scaffolding, and automation. But LLMs don’t remove the need for **clear thinking**, **careful review**, and **thoughtful design**. If anything, those become even more important as more code gets generated.

Yes, the cost of writing code has indeed dropped. But the cost of making sense of it together as a team **hasn’t**.

**That’s still the bottleneck. Let’s not pretend it isn’t.**
