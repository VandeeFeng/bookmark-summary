---
title: Hallucinations in code are the least dangerous form of LLM mistakes
date: 2025-03-03
extra:
  source: https://simonwillison.net/2025/Mar/2/hallucinations-in-code/
  original_title: Hallucinations in code are the least dangerous form of LLM mistakes
---
## Summary
**摘要**：
文章作者指出，开发者在使用LLM生成代码时遇到的“幻觉”问题，即LLM创造不存在的方法或库，实际上是所有LLM错误中危害最小的。真正的风险在于LLM产生的代码中那些不会被编译器或解释器立即发现的错误。当运行LLM生成的代码时，任何虚构的方法都会立即报错，可以自行修复或反馈给LLM进行修正。与散文中的幻觉相比，代码具有强大的事实核查机制：运行代码，验证其是否有效，甚至可以利用ChatGPT Code Interpreter等工具实现LLM自动纠错。作者认为，手动测试代码至关重要，即使代码看起来完美且无错误，也不能保证其正确性。要避免LLM代码带来的问题，需要积极地测试代码，培养良好的手动QA技能。如果LLM生成的代码中频繁出现幻觉，可以尝试更换模型、学习如何使用上下文，或选择成熟的技术。作者还批评了那些认为审查LLM代码不如自己编写代码快的人，指出他们忽略了阅读、理解和审查他人代码的重要性，而LLM恰好可以帮助我们练习这些技能。

**要点总结**：

1.  **LLM代码幻觉是危害最小的错误**：当LLM生成不存在的方法或库时，程序会立即报错。这种错误很容易被发现和纠正，相比之下，LLM在其他领域产生的错误可能更难被察觉。

2.  **运行和测试代码至关重要**：不能仅仅依靠代码的外观或LLM的自信回答来判断其正确性。必须通过实际运行代码来验证其功能，手动测试代码是避免潜在问题的关键手段。

3.  **LLM无法取代软件专业人员**：尽管LLM可以生成看起来很棒的代码，但人工测试确保代码按预期运行仍然至关重要。编写代码后，需要运行来证明代码的有效性。

4.  **减少代码幻觉的技巧**：可以通过尝试不同的模型（如Claude 3.7 Sonnet、OpenAI的o3-mini-high和GPT-4o与代码解释器），向LLM提供相关库的示例代码，或选择长期使用的成熟库来减少幻觉。

5.  **提升代码审查能力**：审查LLM生成的代码是学习和提高代码阅读、理解和审查技能的绝佳途径。与其抱怨审查代码耗时，不如将其视为提升自身技能的机会。

## Full Content
Title: Hallucinations in code are the least dangerous form of LLM mistakes

URL Source: https://simonwillison.net/2025/Mar/2/hallucinations-in-code/

Markdown Content:
2nd March 2025

A surprisingly common complaint I see from developers who have tried using LLMs for code is that they encountered a hallucination—usually the LLM inventing a method or even a full software library that doesn’t exist—and it crashed their confidence in LLMs as a tool for writing code. How could anyone productively use these things if they invent methods that don’t exist?

Hallucinations in code **are the least harmful hallucinations you can encounter from a model**.

The real risk from using LLMs for code is that they’ll make mistakes that _aren’t_ instantly caught by the language compiler or interpreter. And these happen _all the time_!

The moment you run LLM generated code, any hallucinated methods will be instantly obvious: you’ll get an error. You can fix that yourself or you can feed the error back into the LLM and watch it correct itself.

Compare this to hallucinations in regular prose, where you need a critical eye, strong intuitions and well developed fact checking skills to avoid sharing information that’s incorrect and directly harmful to your reputation.

With code you get a powerful form of fact checking for free. Run the code, see if it works.

In some setups—[ChatGPT Code Interpreter](https://simonwillison.net/tags/code-interpreter/), [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), any of the growing number of “agentic” code systems that write and then execute code in a loop—the LLM system itself will spot the error and automatically correct itself.

If you’re using an LLM to write code without even running it yourself, _what are you doing?_

Hallucinated methods are such a tiny roadblock that when people complain about them I assume they’ve spent minimal time learning how to effectively use these systems—they dropped them at the first hurdle.

My cynical side suspects they may have been looking for a reason to dismiss the technology and jumped at the first one they found.

My less cynical side assumes that nobody ever warned them that you have to put a lot of work in to learn how to get good results out of these systems. I’ve been exploring [their applications for writing code](https://simonwillison.net/tags/ai-assisted-programming/) for over two years now and I’m still learning new tricks (and new strengths and weaknesses) almost every day.

#### Manually testing code is essential [#](https://simonwillison.net/2025/Mar/2/hallucinations-in-code/#qa)

Just because code looks good and runs without errors doesn’t mean it’s actually doing the right thing. No amount of meticulous code review—or even comprehensive automated tests—will demonstrably prove that code actually does the right thing. You have to run it yourself!

Proving to yourself that the code works is your job. This is one of the many reasons I don’t think LLMs are going to put software professionals out of work.

LLM code will usually look fantastic: good variable names, convincing comments, clear type annotations and a logical structure. This can lull you into a false sense of security, in the same way that a gramatically correct and confident answer from ChatGPT might tempt you to skip fact checking or applying a skeptical eye.

The way to avoid _those_ problems is the same as how you avoid problems in code by other humans that you are reviewing, or code that you’ve written yourself: you need to actively exercise that code. You need to have great manual QA skills.

A general rule for programming is that you should _never_ trust any piece of code until you’ve seen it work with your own eye—or, even better, seen it fail and then fixed it.

Across my entire career, almost every time I’ve assumed some code works without actively executing it—some branch condition that rarely gets hit, or an error message that I don’t expect to occur—I’ve later come to regret that assumption.

#### Tips for reducing hallucinations [#](https://simonwillison.net/2025/Mar/2/hallucinations-in-code/#tips)

If you really are seeing a deluge of hallucinated details in the code LLMs are producing for you, there are a bunch of things you can do about it.

*   Try different models. It might be that another model has better training data for your chosen platform. As a Python and JavaScript programmer my favorite models right now are Claude 3.7 Sonnet with thinking turned on, OpenAI’s o3-mini-high and GPT-4o with Code Interpreter (for Python).
*   Learn how to use the context. If an LLM doesn’t know a particular library you can often fix this by dumping in a few dozen lines of example code. LLMs are incredibly good at imitating things, and at rapidly picking up patterns from very limited examples. Modern model’s have increasingly large context windows—I’ve recently started using Claude’s new [GitHub integration](https://support.anthropic.com/en/articles/10167454-using-the-github-integration) to dump entire repositories into the context and it’s been working extremely well for me.
*   Chose [boring technology](https://boringtechnology.club/). I genuinely find myself picking libraries that have been around for a while partly because that way it’s much more likely that LLMs will be able to use them.

I’ll finish this rant with a related observation: I keep seeing people say “if I have to review every line of code an LLM writes, it would have been faster to write it myself!”

Those people are loudly declaring that they have under-invested in the crucial skills of reading, understanding and reviewing code written by other people. I suggest getting some more practice in. Reviewing code written for you by LLMs is a great way to do that.

* * *

_Bonus section_: I asked Claude 3.7 Sonnet "extended thinking mode" to review an earlier draft of this post—"`Review my rant of a blog entry. I want to know if the argument is convincing, small changes I can make to improve it, if there are things I've missed.`". It was quite helpful, especially in providing tips to make that first draft a little less confrontational! Since you can share Claude chats now [here’s that transcript](https://claude.ai/share/685cd6d9-f18a-47ef-ae42-e9815df821f1).

