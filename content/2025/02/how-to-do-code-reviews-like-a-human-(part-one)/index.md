---
title: How to Do Code Reviews Like a Human (Part One)
date: 2025-02-28
extra:
  source: https://mtlynch.io/human-code-reviews-1/
  original_title: How to Do Code Reviews Like a Human (Part One)
---
## Summary
**摘要**：
本文探讨了如何像人一样进行代码审查，强调了代码审查不仅是技术过程，也是社交过程。文章首先指出了当前代码审查实践的不足，即过分关注查找缺陷而忽略了沟通和人际关系。作者建议采用一系列技巧来改进代码审查，包括：利用自动化工具减少人工干预，例如使用持续集成工具(如Travis、CircleCI)进行代码构建和测试，使用代码格式化工具(如ClangFormat、gofmt)统一代码风格，以及使用代码检查工具(如pyflakes、JSLint)来识别未使用的导入或变量；通过制定代码风格指南来避免风格争论，确保代码风格的一致性；立即开始代码审查，避免作者因等待审查而阻塞工作；从高层次入手，逐步细化审查，避免作者被大量的低层次反馈淹没；通过提供代码示例，减轻作者的负担，展示审查者的慷慨；避免使用“你”字，以减少作者的防御心理；将反馈意见表达为请求而非命令，给作者自主感；以及将审查意见与原则联系起来，增加客观性。

**要点总结**：
1.  利用自动化工具处理重复性任务：将代码构建、测试、格式化和检查等任务交给计算机完成，可以节省审查者的时间和精力，使其能够专注于更重要的代码逻辑和功能性问题。
2.  通过代码风格指南解决代码风格争议：制定明确的代码风格指南，可以避免在代码审查过程中因代码风格问题产生争论，提高审查效率，同时保证团队代码风格的统一性，从而提升代码的可读性和可维护性。
3.  及时开始代码审查，避免延误：快速响应代码审查请求，可以避免作者因等待审查结果而耽误工作，同时鼓励作者提交更小、更集中的代码变更，从而使代码审查过程更加高效。
4.  代码审查反馈意见应委婉客观：在提供代码审查反馈时，应避免使用“你”等人称代词，尽量将反馈表达为请求或建议，并结合代码原则或团队规范进行解释，以减少作者的抵触情绪，促进更有效的沟通和协作。

## Full Content
Title: How to Do Code Reviews Like a Human (Part One)

URL Source: https://mtlynch.io/human-code-reviews-1/

Published Time: 2017-10-12T00:00:00+00:00

Markdown Content:
Lately, I’ve been reading articles about best practices for code reviews. I notice that these articles focus on finding bugs to the exclusion of almost every other component of a review. Communicating issues you discover in a constructive and professional way? Irrelevant! Just identify all the bugs, and the rest will take care of itself.

So I had a revelation: if this works for code, why not romance? With that, I’m announcing my new ebook to help developers with their love lives:

[![Image 1: ebook cover](https://mtlynch.io/human-code-reviews-1/book-cover.png)](https://mtlynch.io/human-code-reviews-1/book-cover.png)

My revolutionary ebook teaches you **proven techniques** for maximizing the number of deficiencies you find in your partner. The ebook does **not** cover:

*   Communicating issues to your partner with empathy and understanding.
*   Helping your partner address their weaknesses.

Based on my reading of code review literature, those parts of a relationship are _obvious_ and _not worth discussing_.

Does this sound like a good ebook to you? I’m assuming you just yipped “Nonononono!”

So, why is that the way we talk about code reviews?

I can only assume the articles I’ve read are from the future, where all developers are robots. In that world, your teammates welcome thoughtlessly-worded critiques of their code because processing such information warms their cold, robot hearts.

I’m going to make the bold assumption that you want to improve code reviews in the present, where your teammates are humans. I’ll make the even bolder assumption that a positive relationship with your colleagues is an end in itself and not simply a variable you adjust to minimize your cost-per-defect. How would your review practices change under these circumstances?

In this article, I discuss techniques that treat the code review as not only a technical process but a social one as well.

What is a code review? [🔗︎](https://mtlynch.io/human-code-reviews-1/#what-is-a-code-review)
--------------------------------------------------------------------------------------------

The term “code review” can refer to a range of activities, from simply reading some code over your teammate’s shoulder to a 20-person meeting where you dissect code line by line. I use the term to refer to a process that’s formal and written, but not so heavyweight as a series of in-person code inspection meetings.

[![Image 2: Code review flow](https://mtlynch.io/human-code-reviews-1/flowchart.png)](https://mtlynch.io/human-code-reviews-1/flowchart.png)

The participants in a code review are the **author**, who writes the code and sends it for review, and the **reviewer**, who reads the code and decides when it’s ready to be merged in to the team’s codebase. A review can have multiple reviewers, but I assume for simplicity that you are the sole reviewer.

Before the code review begins, the author must create a **changelist**. This is a set of changes to source code that the author wants to merge in to the team’s codebase.

A review begins when the author sends their changelist to the reviewer. Code reviews happen in **rounds**. Each round is one complete round-trip between the author and reviewer: the author sends changes, and the reviewer responds with written feedback on those changes. Every code review has one or more rounds.

The review ends when the reviewer **approves** the changes. This is commonly referred to as giving LGTM, shorthand for “looks good to me.”

Why is this hard? [🔗︎](https://mtlynch.io/human-code-reviews-1/#why-is-this-hard)
----------------------------------------------------------------------------------

If a programmer sends you a changelist that they think is awesome, and you write them an extensive list of reasons why it’s not, that’s a sensitive message to get across.

> That’s one reason I don’t miss IT, because programmers are very unlikable people… In aviation, for example, people who greatly overestimate their level of skill are all dead.
> 
> \-Philip Greenspun, co-founder of ArsDigita, excerpted from [_Founders at Work_](https://smile.amazon.com/Founders-Work-Stories-Startups-Early/dp/1430210788/)

It’s easy for an author to interpret criticism of their code as an implication that they are an incompetent programmer. Code reviews are an opportunity to share knowledge and make informed engineering decisions. But that can’t happen if the author perceives the discussion as a personal attack.

As if this wasn’t difficult enough, you also have the challenge of conveying your thoughts in writing, where the risk of miscommunication is higher. The author can’t hear your tone of voice or see your body language, so it’s even more important to articulate your feedback carefully. To an author who’s feeling defensive, an innocuous note like, “You forgot to close the file handle,” can read as, “I can’t _believe_ you forgot to close the file handle! You’re such an idiot.”

Techniques [🔗︎](https://mtlynch.io/human-code-reviews-1/#techniques)
---------------------------------------------------------------------

1.  [Let computers do the boring parts](https://mtlynch.io/human-code-reviews-1/#let-computers-do-the-boring-parts)
2.  [Settle style arguments with a style guide](https://mtlynch.io/human-code-reviews-1/#settle-style-arguments-with-a-style-guide)
3.  [Start reviewing immediately](https://mtlynch.io/human-code-reviews-1/#start-reviewing-immediately)
4.  [Start high level and work your way down](https://mtlynch.io/human-code-reviews-1/#start-high-level-and-work-your-way-down)
5.  [Be generous with code examples](https://mtlynch.io/human-code-reviews-1/#be-generous-with-code-examples)
6.  [Never say “you”](https://mtlynch.io/human-code-reviews-1/#never-say-you)
7.  [Frame feedback as requests, not commands](https://mtlynch.io/human-code-reviews-1/#frame-feedback-as-requests-not-commands)
8.  [Tie notes to principles, not opinions](https://mtlynch.io/human-code-reviews-1/#tie-notes-to-principles-not-opinions)

### Let computers do the boring parts [🔗︎](https://mtlynch.io/human-code-reviews-1/#let-computers-do-the-boring-parts)

Between interruptions like meetings and emails, the time you have available to focus on code is scarce. Your mental stamina is in even shorter supply. Reading a teammate’s code is cognitively taxing and requires a high level of concentration. Don’t squander these resources on tasks a computer can do, especially when a computer can do them better.

Whitespace errors are an obvious example. Compare how much effort it takes for a human reviewer to find an indenting mistake and work with the author to correct it as opposed to just using an automated formatting tool:

| Effort required with a human reviewer | Effort required with a formatting tool |
| --- | --- |
| 
1.  Reviewer searches for whitespace issues and finds incorrect indentation.
2.  Reviewer writes a note calling out the incorrect indentation.
3.  Reviewer rereads their note to make sure that it's worded in a clear, non-accusatory way.
4.  Author reads the note.
5.  Author corrects the code indentation.
6.  Reviewer verifies that the author addressed their note properly.

 | Nothing! |

The right side is empty because the author uses a code editor that automatically formats the whitespace every time they hit “Save.” At worst, the author sends their code out for review, and the [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) solution reports that the whitespace is incorrect. The author fixes the issue without the reviewer ever having to care.

Look for mechanical tasks in your code reviews that you can automate away. Here are the common ones:

| Task | Automated solution |
| --- | --- |
| Verify the code builds | Continuous integration solution, such as [Travis](https://travis-ci.com/) or [CircleCI](https://circleci.com/). |
| Verify automated tests pass | Continuous integration solution, such as [Travis](https://travis-ci.com/) or [CircleCI](https://circleci.com/). |
| Verify code whitespace matches team style | Code formatter, such as [ClangFormat](https://clang.llvm.org/docs/ClangFormat.html) (C/C++ formatter) or [gofmt](https://golang.org/cmd/gofmt/) (Go formatter). |
| Identify unused imports or unused variables | Code linters, such as [pyflakes](https://pypi.python.org/pypi/pyflakes) (Python linter) or [JSLint](http://jslint.com/help.html) (JavaScript linter). |

Automation helps you make more meaningful contributions as a reviewer. When you can ignore a whole class of issues, such as the ordering of `imports` or naming conventions for source filenames, it allows you to focus on more interesting things like functional errors or weaknesses in readability.

Automation benefits the author as well. It allows them to discover careless mistakes in seconds instead of hours. The instant feedback makes it easier to learn from and cheaper to fix because the author still has the relevant context in their head. Plus, if they have to hear about a dumb mistake they made, it’s much easier on their ego if they hear it from a computer instead of from you.

Work with your team to build these automated checks directly into the code review workflow (e.g., [pre-commit hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) in Git or [webhooks](https://developer.github.com/webhooks/) in GitHub). If the review process requires the author to run these checks manually, you forfeit most of the benefit. The author will invariably forget on occasion which forces you to continue reviewing for the simple issues that automation is meant to handle instead.

### Settle style arguments with a style guide [🔗︎](https://mtlynch.io/human-code-reviews-1/#settle-style-arguments-with-a-style-guide)

Arguments about style are a waste of time in reviews. Consistent style is certainly important, but a code review is not the time to bicker about where to put the curly braces. The best way to excise style debates from your reviews is by keeping a style guide.

[![Image 3: A typical style argument](https://mtlynch.io/human-code-reviews-1/style-argument.png)](https://mtlynch.io/human-code-reviews-1/style-argument.png)

A good style guide defines not only superficial elements like naming conventions or whitespace rules but also how to use the features of the given programming language. JavaScript and Perl, for example, are packed with functionality — they offer many ways to implement the same logic. A style guide defines The One True Way of doing things so that you don’t end up with half your team using one set of language features while the other half uses a totally different set of features.

Once you have a style guide, you don’t have to waste review cycles arguing with the author about whose naming conventions are best. Just defer to the style guide and move on. If your style guide doesn’t specify a convention about a particular issue, it’s generally not worth arguing about. If you encounter a style issue your guide doesn’t cover and it’s important enough to discuss, hash it out with your team. Then, record the decision in your style guide so you never have to have that discussion again.

**_Option 1: Adopt an existing style guide_**

If you search online, you can find published style guides ripe for the taking. [Google’s style guides](https://google.github.io/styleguide/) are the most well-known, but you can find others if this style doesn’t suit you. By adopting an existing guide, you inherit the benefits of a style guide without the substantial costs of creating one from scratch.

The downside is that organizations optimize their style guides for their own particular needs. For example, Google’s style guides are conservative about [using new language features](https://google.github.io/styleguide/cppguide.html#C++11) because they have an enormous codebase with code that has to run on everything from a home router to the latest iPhone. If you’re a four-person startup with a single product, you may choose to be more aggressive in using cutting-edge language features or extensions.

**_Option 2: Create your own style guide incrementally_**

If you don’t want to adopt an existing guide, you can create your own. Every time a style argument arises during a code review, raise the question to your whole team to decide what the official convention should be. When you reach agreement, codify that decision in your style guide.

I prefer to keep my team’s style guide as Markdown under source control (e.g., [GitHub pages](https://pages.github.com/)). That way, any changes to the style guide go through the normal review process — someone has to explicitly approve the change, and everyone on the team has a chance to raise concerns. Wikis and Google Docs are acceptable options as well.

**_Option 3: The hybrid approach_**

By combining options 1 and 2, you can adopt an existing style guide as your base, and then maintain a local style guide to extend or override the base. A good example of this is the [Chromium C++ style guide](https://chromium.googlesource.com/chromium/src/+/HEAD/styleguide/c++/c++.md). It uses [Google’s C++ style guide](https://google.github.io/styleguide/cppguide.html) as a base, but makes its own changes and additions on top of it.

### Start reviewing immediately [🔗︎](https://mtlynch.io/human-code-reviews-1/#start-reviewing-immediately)

Treat code reviews as a high priority. When you’re actually reading the code and giving feedback, take your time, but _start_ your review immediately — ideally, within minutes.

[![Image 4: A code review relay race](https://mtlynch.io/human-code-reviews-1/relay.png)](https://mtlynch.io/human-code-reviews-1/relay.png)

If a teammate sends you a changelist, it likely means that they are blocked on other work until your review is complete. In theory, source control systems allow the author to branch, continue working, and then forward-merge changes from the review into their new branch. In reality, there are about four developers total who can do that efficiently. It takes everyone else so long to untangle three-way diffs that it can cancel out any progress made waiting for the review to come back.

When you start reviews immediately, you create a virtuous cycle. Your review turnaround becomes purely a function of the size and complexity of the author’s changelist. This incentivizes authors to send small, narrowly-scoped changelists. These are easier and more pleasant for you to review, so you review them faster, and the cycle continues.

Imagine that your teammate implements a new feature that requires 1,000 lines of code changes. If they know you can review a 200-line changelist in about 2 hours, they can break their feature into changelists of about 200 lines each and get the whole feature checked in within a day or two. If, however, you take a day to do all code reviews, regardless of size, now it takes a week to get that feature checked in. Your teammate doesn’t want to sit around for a week, so they’re incentivized to send larger code reviews, like 500-600 lines each. These are more costly to review and yield poorer feedback because it’s more difficult to keep context on a 600-line change than a 200-line change.

The absolute maximum turnaround on a review round should be one business day. If you’re struggling with a higher-priority issue and can’t complete a round of review in under a day, let your teammate know and give them the opportunity to reassign it to someone else. If you’re forced to decline reviews more than about once per month, it likely means that your team needs to reduce its pace so that you can maintain sane development practices.

### Start high level and work your way down [🔗︎](https://mtlynch.io/human-code-reviews-1/#start-high-level-and-work-your-way-down)

The more notes you write in a given review round, the more you risk making the author feel overwhelmed. The exact limit varies by developer, but the danger zone generally begins in the range of 20-50 notes in a single round of review.

If you’re worried about drowning the author in a sea of notes, restrict yourself to high-level feedback in the early rounds. Focus on issues like redesigning a class interface or splitting up complex functions. Wait until those issues are resolved before tackling lower-level issues, such as variable naming or clarity of code comments.

Your low-level notes might become moot once the author integrates your high-level notes. By deferring them to a later round, you save yourself the nontrivial work of writing carefully-worded comments calling out the issues, and you spare the author from processing unnecessary notes. This technique also segments the layers of abstraction you focus on during the review, helping you and the author work through the changelist in a clear, systematic way.

### Be generous with code examples [🔗︎](https://mtlynch.io/human-code-reviews-1/#be-generous-with-code-examples)

In an ideal world, the code author would be thankful for every review they receive. It’s an opportunity for them to learn, and it protects them from mistakes. In reality, there are a number of external factors that could cause the author to perceive the review negatively and resent you for giving them notes. Maybe they’re under pressure to meet a deadline, so anything other than your instant, rubber-stamp approval feels like obstruction. Maybe you haven’t worked together much, so they don’t trust that your feedback is well-intentioned.

A great way to make an author feel good about the review process is to find opportunities to give them gifts during the review. And what’s the gift all developers love to receive? Code examples, of course.

[![Image 5: Receiving the gift of code](https://mtlynch.io/human-code-reviews-1/code-gift.png)](https://mtlynch.io/human-code-reviews-1/code-gift.png)

If you lighten the author’s load by writing out some of the changes you’re suggesting, you demonstrate that you are generous with your time as a reviewer.

For example, imagine that you have a colleague who is not familiar with the [list comprehensions](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/) feature of Python. They send you a code review that includes these lines:

```
urls = []
for path in paths:
  url = 'https://'
  url += domain
  url += path
  urls.append(url)
```

Responding, “Can we simplify this with a list comprehension?” will annoy them because now they have to spend 20 minutes researching something they’ve never used before.

They will be much happier to receive a note like the following:

> Consider simplifying with a list comprehension like this:
> 
> ```
> urls = ['https://' + domain + path for path in paths]
> ```

This technique is not limited to one-liners. I’ll often create my own branch of the code to demonstrate a large proof of concept to the author, such as breaking up a large function or adding a unit test to cover an additional edge case.

Reserve this technique for clear, uncontroversial improvements. In the list comprehension example above, few developers would object to an 83% reduction in lines of code. In contrast, if you write a lengthy example to demonstrate a change that is “better” based on your own personal taste (e.g., style changes), code examples make you look pushy instead of generous.

Limit yourself to two or three code examples per review round. If you start writing the author’s whole changelist for them, it signals that you don’t think they’re capable of writing their own code.

### Never say “you” [🔗︎](https://mtlynch.io/human-code-reviews-1/#never-say-you)

This one is going to sound weird, but hear me out: never use the word “you” in a code review.

The decisions you reach in a review should be based on what makes the code better rather than who came up with the idea. Your teammate put significant effort into their changelist and is likely proud of the work they did. Their natural reaction to hearing criticism of their work is to feel defensive and protective.

Word your feedback in a way that minimizes the risk of raising your teammate’s defenses. Be clear that you’re critiquing the code, not the coder. When an author sees “you” in a comment, it brings their focus away from the code and back to themselves. This increases the risk that they’ll take your criticism personally.

Consider this harmless comment:

> You misspelled ‘successfully.’

The author can interpret that note in two very different ways:

*   **Interpretation 1**: Hey, good buddy! You misspelled ‘successfully.’ But I still think you’re smart! It was probably just a typo.
*   **Interpretation 2**: You misspelled ‘successfully,’ dumbass.

Contrast this with a note that omits “you”:

> sucessfully -\> successfully

The latter note is a simple correction and not a judgment of the author.

Fortunately, it’s easy to rewrite your feedback to avoid the word “you.”

**_Option 1: Replace ‘you’ with ‘we’_**

> Can **you** rename this variable to something more descriptive, like `seconds_remaining`?

becomes:

> Can **we** rename this variable to something more descriptive, like `seconds_remaining`?

“We” reinforces the team’s collective responsibility for the code. The author may move on to a different company and so might you, but the team who owns this code will remain in one form or another. It can sound silly to say “we” when it’s clearly something you expect the author to do themselves, but silly is better than accusatory.

[![Image 6: Moving couch cartoon](https://mtlynch.io/human-code-reviews-1/move-couch.png)](https://mtlynch.io/human-code-reviews-1/move-couch.png)

**_Option 2: Remove the subject from the sentence_**

Another way to avoid using “you” is to use a shorthand that omits the subject from the sentence:

> **Suggest renaming** to something more descriptive, like `seconds_remaining`.

You can achieve a similar effect with the [passive voice](https://en.wikipedia.org/wiki/English_passive_voice). I generally avoid the passive voice like the plague in my technical writing, but it can be a helpful way of writing around “you”:

> This variable **should be renamed** to something more descriptive, like `seconds_remaining`.

An additional option is to phrase it as a question, beginning with “what about…” or “how about…”:

> **What about renaming** this variable to something more descriptive, like `seconds_remaining`?

### Frame feedback as requests, not commands [🔗︎](https://mtlynch.io/human-code-reviews-1/#frame-feedback-as-requests-not-commands)

Code reviews require more tact and care than usual communication because there’s a high risk of derailing the discussion into a personal argument. You would expect reviewers to dial up their politeness in reviews, but bizarrely I’ve found them to go the opposite direction. Most people never say to a co-worker, “Hand me that stapler, then fetch me a soda.” But I’ve seen numerous reviewers frame feedback with similarly pushy commands, such as, “Move this class to a separate file.”

Err on the side of being annoyingly gentle in your feedback. Frame your notes as requests or suggestions, not commands.

Compare the same note framed in two different ways:

| Feedback framed as command | Feedback framed as request |
| --- | --- |
| Move the `Foo` class to a separate file. | Can we move the `Foo` class to a separate file? |

People like to feel in control of their own work. Making a request of the author gives them a sense of autonomy.

Requests also make it easier for the author to push back politely. Maybe they have a good reason for their choice. If you frame your feedback as a command, any pushback from the author comes across as disobedience. If you frame your feedback as a request or a question, the author can simply answer you.

Compare how combative the conversation seems depending on how the reviewer frames their initial note:

| Feedback framed as command (Combative) | Feedback framed as request (Cooperative) |
| --- | --- |
| **Reviewer**: Move the `Foo` class to a separate file.  
**Author**: I don’t want to do that because then it’s far away from the `Bar` class. Clients will almost always use the two together. | **Reviewer**: Can we move the `Foo` class to a separate file?  
**Author**: We could, but then it’s far away from the `Bar` class, and clients will generally use these two classes together. What do you think? |

See how much more civil the conversation becomes when you ~construct imaginary dialog to prove your point~ frame your notes as requests instead of commands?

### Tie notes to principles, not opinions [🔗︎](https://mtlynch.io/human-code-reviews-1/#tie-notes-to-principles-not-opinions)

When you give the author a note, explain both your suggested change and the _reason_ for the change. Instead of saying, “We should split this class into two,” it’s better to say, “Right now, this class is responsible for both downloading the file and parsing it. We should split it up into a downloader class and parsing class per the [single responsibility principle](https://en.wikipedia.org/wiki/Single_responsibility_principle).”

Grounding your notes in principles frames the discussion in a constructive way. When you cite a specific reason, like, “We should make this function private to minimize the class’ public interface,” the author can’t simply respond, “No, I prefer it my way.” Or rather, they _can_, but it would look silly because you demonstrated how the change satisfies a goal, and they just stated a preference.

Software development is both an art and science. You can’t always articulate exactly what is wrong with a piece of code in terms of established principles. Sometimes code is just ugly or unintuitive, and it’s hard to pin down why. In these cases, explain what you can, but keep it objective. If you say, “**I** found this hard to understand,” that’s at least an objective statement, as opposed to, “**this is** confusing,” which is a value judgment and may not be true for every person.

Provide supporting evidence where possible in the form of links. The relevant section of your team’s style guide is the best link you can provide. You can also link to documentation for the language or library. Highly-upvoted [StackOverflow](https://stackoverflow.com/) answers can work as well, but the farther you stray from authoritative documentation, the shakier your evidence becomes.

Part two [🔗︎](https://mtlynch.io/human-code-reviews-1/#part-two)
-----------------------------------------------------------------

If you enjoyed this post, check out [the second half of this article](https://mtlynch.io/human-code-reviews-2/), which focuses on bringing reviews to a successful close without ugly conflict. It includes techniques for:

*   Handling excessively large code reviews,
*   Recognizing opportunities to give praise,
*   Respecting the scope of a review, and
*   Mitigating stalemates.

### **[How to Do Code Reviews Like a Human (Part two)](https://mtlynch.io/human-code-reviews-2/)** [🔗︎](https://mtlynch.io/human-code-reviews-1/#how-to-do-code-reviews-like-a-human-part-twohuman-code-reviews-2)

* * *

_Edited by [Samantha Mason](https://www.samanthamasonfreelancer.com/). Illustrations by Loraine Yow. Thanks to [@global4g](https://twitter.com/global4g) for providing valuable feedback on an early draft of this post._

