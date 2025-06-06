---
title: AI Horseless Carriages
date: 2025-05-10
extra:
  source: https://koomen.dev/essays/horseless-carriages/
  original_title: AI Horseless Carriages
---
## Summary
**摘要**：
作者发现，使用AI构建软件比使用AI构建的应用更有趣，因为AI作为一种强大的工具，能够快速实现各种想法。然而，许多AI应用的功能显得多余甚至适得其反，这可能是因为它们模仿了旧的软件构建方式，不必要地限制了AI模型。以Gmail的AI邮件助手为例，它生成的邮件草稿不符合用户的写作风格，效率低下。为了解决这个问题，作者提出了一个更好的邮件助手方案，该方案使用AI阅读邮件，并根据用户自定义的“系统提示”对邮件进行分类、优先级排序和自动回复。作者认为，AI应用应该允许用户编写自己的“系统提示”，以便更好地控制AI的行为。通过让用户自定义系统提示，可以教导LLM像用户一样编写电子邮件，从而获得更好的结果。作者还探讨了AI应用开发的“旧世界思维”，即开发者编写系统提示，用户提供用户提示。作者认为，当LLM代表用户行事时，用户应该能够通过编辑系统提示来教导它如何操作。

**要点总结**：

1.  Gmail的AI邮件助手是一个“无马的马车”的例子，它模仿了旧的软件构建方式，限制了AI模型的能力。Gmail的AI邮件助手生成的草稿质量不高，因为它们使用了通用的系统提示，而没有允许用户自定义。
2.  更好的AI邮件助手应该使用AI阅读邮件，并根据用户自定义的“系统提示”对邮件进行分类、优先级排序和自动回复。通过让用户自定义系统提示，可以教导LLM像用户一样编写电子邮件，从而获得更好的结果。
3.  LLM（大型语言模型）通过读取“提示”并预测后续的词语来工作。“提示”可以分为“系统提示”和“用户提示”两部分，系统提示定义了AI助手的行为方式，用户提示描述了要完成的具体任务。
4.  传统的软件开发模式是开发者编写程序，用户使用程序。在AI应用中，开发者通常编写系统提示，用户提供用户提示。但当AI代表用户行事时，用户应该能够编辑系统提示，以便更好地控制AI的行为。
5.  AI应用应该成为“智能体构建器”而不是直接提供“智能体”。开发者应该创建UI来帮助用户构建特定领域的智能体，提供模板和提示编写智能体来帮助用户引导他们自己的智能体。开发者还应该构建智能体工具，为智能体提供行动的机制和安全保障。
## Full Content
Title: AI Horseless Carriages | koomen.dev

URL Source: https://koomen.dev/essays/horseless-carriages/

Markdown Content:
I noticed something interesting the other day: I enjoy using AI to build software more than I enjoy using most AI applications--software built with AI.

When I use AI to build software I feel like I can create almost anything I can imagine very quickly. AI feels like a power tool. It's a lot of fun.

Many AI apps don't feel like that. Their AI features feel tacked-on and useless, even counter-productive.

I am beginning to suspect that these apps are the ["horseless carriages"](https://koomen.dev/essays/horseless-carriages/#horseless-carriages) of the AI era. They're bad because they mimic old ways of building software that unnecessarily constrain the AI models they're built with.

To illustrate what I mean by that, I'll start with an example of a badly designed AI app.

Gmail's AI assistant
--------------------

A little while ago, the Gmail team released a new feature giving users the ability to generate email drafts from scratch using Google's flagship AI model, Gemini. This is what it looks like:

![Image 1: Gmail's Gemini email draft feature with a prompt I've written](https://koomen.dev/images/gmail_prompt.png)

Gmail's Gemini email draft generation feature

Here I've added a prompt to the interface requesting a draft for an email to my boss. Let's see what Gemini returns:

![Image 2: Gmail's Gemini email draft generation feature response](https://koomen.dev/images/gmail_response.png)

Gmail's Gemini email draft generation feature response

As you can see, Gemini has produced perfectly reasonable draft that unfortunately doesn’t sound anything like an email that I would actually write. If I'd written this email myself, it would have sounded something like this:

Hey garry, my daughter woke up with the flu so I won't make it in today

The email I would have written

The tone of the draft isn't the only problem. The email I'd have written is actually shorter than the original prompt, which means I spent more time asking Gemini for help than I would have if I'd just written the draft myself. Remarkably, the Gmail team has shipped a product that perfectly captures the experience of managing an underperforming employee.

Millions of Gmail users have had this experience and I'm sure many of them have concluded that AI isn't smart enough to write good emails yet.

This could not be further from the truth: Gemini is an astonishingly powerful model that is more than capable of writing good emails. Unfortunately, the Gmail team designed an app that prevents it from doing so.

A better email assistant
------------------------

To illustrate this point, here's a simple demo of an AI email assistant that, if Gmail had shipped it, would actually save me a lot of time:

Email Reading Agent System Prompt

Available Tools

`labelEmail(label, color, priority)`

`archiveEmail()`

`draftReply(body)`

Email Inbox (12)

Maya Rodriguez

Technical co-founder?

▶

DevOps Pro Team

Security Solutions for Growing Companies

▶

Garry Tan

reschedule

▶

TechCrunch Weekly

This Week in Tech: AI Developments and M...

▶

Gustaf Alströmer

founder intro?

▶

HackerNews Digest

Top Stories: New Programming Languages o...

▶

Sarah from SaaS Solutions

Exclusive Offer for New Customers

▶

The Verge Updates

Latest Product Launches and Industry New...

▶

DataAnalytics Plus

Special Pricing on Data Analytics Tools

▶

Alex Chen

advice on fundraising

▶

Mark at Enterprise Tools

Transform Your Workflow with Our Platfor...

▶

Sumana

dinner tonight

▶

A demo of an actually useful email assistant using OpenAI's gpt-4o-mini under the hood

This demo uses AI to _read_ emails instead of write them from scratch. Each email is categorized and prioritized, and some are auto-archived while others get an automatically-drafted reply. The assistant processes emails individually according to a custom "System Prompt" that explains exactly how I want each one handled. You can try your own labeling logic by editing the System Prompt.

It's obvious how much more powerful this approach is, so why didn't the Gmail team build it this way? To answer this question, let's look more closely at the problems with their design. We'll start with its generic tone.

AI Slop
-------

The draft that Gmail's AI assistant produced is wordy and weirdly formal and so un-Pete that if I actually sent it to Garry, he’d probably mistake it for some kind of phishing attack. It’s AI Slop.

Everyone who has used an LLM to do any writing has had this experience. It’s so common that most of us have unconsciously adopted strategies for avoiding it when writing prompts. The simplest such strategy is just writing more detailed instructions that steer the LLM in the right direction, like this:

let my boss garry know that my daughter woke up with the flu and that I won't be able to come in to the office today. Use no more than one line for the entire email body. Make it friendly but really concise. Don't worry about punctuation or capitalization. Sign off with “Pete” or “pete” and not “Best Regards, Pete” and certainly not “Love, Pete”

Prompt hacking our way to success

Here's a little draft-writer demo you can use to compare my original prompt with this expanded one:

Your Request

Email Draft

Your generated email will appear here...

A dummy version of Gmail's draft generator that uses gpt-4o-mini under the hood

The generated draft sounds better, but this is obviously dumb. The new prompt is even longer than the original, and I'd need to write something like this out every time I want a new email written.

There is a simple solution to this problem that many AI app developers seem to be missing: let me write my own "System Prompt".

System Prompts and User Prompts
-------------------------------

Viewed from the outside, large language models are actually really simple. They read in a stream of words, the “prompt”, and then start predicting the words, one after another, that are likely to come next, the “response”.

The important thing to note here is that all of the input and all of the output is text. The LLM's user interface is just text1.

LLM providers like OpenAI and Anthropic have adopted a convention to help make prompt writing easier: they split the prompt into two components: a **System Prompt** and a **User Prompt**, so named because in many API applications the app developers write the System Prompt and the user writes the User Prompt.

Combined Prompt

System Prompt: Instructions that define the assistant's behavior...

User Prompt: Specific query or instruction from the user...

Large Language Model

Processes the combined prompt and generates a response

The System Prompt explains to the model how to accomplish a particular set of tasks, and is re-used over and over again. The User Prompt describes a specific task to be done.

You can think of the System Prompt as a function, the User Prompt as its input, and the model's response as its output:

System Prompt (function)

User Prompt (input)

Response (output)

A simple demonstration of the system/user prompt relationship using gpt-4o-mini

In my original example, the User Prompt was

Let my boss Garry know that my daughter woke up with the flu this morning and that I won't be able to come in to the office today.

My original User Prompt

Google keeps the System Prompt a secret, but judging by the output we can guess what it looks like:

You are a helpful email-writing assistant responsible for writing emails on behalf of a Gmail user. Follow the user’s instructions and use a formal, businessy tone and correct punctuation so that it’s obvious the user is smart and serious.

Gmail's email-draft-writer System Prompt (presumably)

Of course I'm being glib here, but the problem is not just that the Gmail team wrote a bad system prompt. The problem is that I'm not allowed to change it.

The Pete System Prompt
----------------------

If, instead of forcing me to use their one-size-fits-all System Prompt, Gmail let me write my own, it would look something like this:

You're Pete, a 43 year old husband, father, programmer, and YC Partner.

You're very busy and so is everyone you correspond with, so you do your best to keep your emails as short as possible and to the point. You avoid all unnecessary words and you often omit punctuation or leave misspellings unaddressed because it's not a big deal and you'd rather save the time. You prefer one-line emails.

Do your best to be kind, and don't be so informal that it comes across as rude.

The Pete System Prompt

Intuitively, you can see what's going on here: when I write my own System Prompt, I'm teaching the LLM to write emails the way that I would. Does it work? Let's give it a try.

System Prompt

User Prompt

Email Draft

Your generated email will appear here...

Depending on the System Prompt, gpt-4o-mini returns dramatically different responses to the same User Prompt

Try generating a draft using the (imagined) Gmail System Prompt, and then do the same with the "Pete System Prompt" above. The "Pete" version will give you something like this:

Garry, my daughter has the flu. I can't come in today.

An email draft generated using the Pete System Prompt

It's perfect. That was so easy!

Not only is the output better for this particular draft, it's going to be better for _every_ draft going forward because the System Prompt is reused over and over again. No more banging my head against the wall explaining over and over to Gemini how to write like me!

And the best part of all? Teaching a model like this is surprisingly fun.

Spend a few minutes thinking about how YOU write email. Try writing a "You System Prompt" and see what happens. If the output doesn't look right, try to imagine what you left out of your explanation and try it again. Repeat that a few times until the output starts to feel right to you.

Better yet, try it with a few other User Prompts. For example, see if you can get the LLM to write these emails in your voice:

Let my wife know I'll be home from work late and will miss dinner

Personal email User Prompt

Write an email to comcast customer service explaining that they accidentally double billed you last month.

Customer support request User Prompt

There's something magical about teaching an LLM to solve a problem the same way you would and watching it succeed. Surprisingly, it's actually easier than teaching a human because, unlike a human, an LLM will give you instantaneous, honest feedback about whether your explanation was good enough or not. If you get an email draft you're happy with, your explanation was sufficient. If you don't, it wasn't.

By exposing the System Prompt and making it editable, we've created a product experience that produces better results and is actually fun to use.

As of April 2025 most AI still apps don't ([intentionally](https://x.com/jobergum/status/1913481778175631436)) expose their system prompts. Why not?

Horseless Carriages
-------------------

Whenever a new technology is invented, the first tools built with it inevitably fail because they mimic the old way of doing things. “Horseless carriage” refers to the early motor car designs that borrowed heavily from the horse-drawn carriages that preceded them. Here’s an example of an 1803 Steam Carriage design I found on [Wikipedia](https://en.wikipedia.org/wiki/Horseless_carriage):

![Image 3: Steam carriage](https://koomen.dev/images/steam-carriage.png)

Trevithick's London Steam Carriage of 1803

The brokenness of this design was invisible to everyone at the time and laughably obvious after the fact.

Imagine living in 1806 and riding on one of these for the first time. Even if the wooden frame held together long enough to get you where you were going, the wooden seats and lack of suspension would have made the ride unbearable.

You'd probably think "there's no way I'd choose an engine over a horse". And you'd have been right, at least until the automobile was invented.

I suspect we are living through a similar period with AI applications. Many of them are infuriatingly useless in the same way that Gmail's Gemini integration is.

The "old world thinking" that gave us the original horseless carriage was swapping a horse out for an engine without redesigning the vehicle to handle higher speeds. What is the old world thinking constraining these AI apps?

Old world thinking
------------------

Up until very recently, if you wanted a computer to do something you had two options for making that happen:

1.  Write a program
2.  Use a program written by someone else

Programming is hard, so most of us choose option 2 most of the time. It's why I'd rather pay a few dollars for an off-the-shelf app than build it myself, and why big companies would rather pay millions of dollars to Salesforce than build their own CRM.

The modern software industry is built on the assumption that we need developers to act as middlemen between us and computers. They translate our desires into code and abstract it away from us behind simple, one-size-fits-all interfaces we can understand.

The division of labor is clear: developers decide how software behaves in the general case, and users provide input that determines how it behaves in the specific case.

By splitting the prompt into System and User components, we've created analogs that map cleanly onto these old world domains. The System Prompt governs how the LLM behaves in the general case and the User Prompt is the input that determines how the LLM behaves in the specific case.

With this framing, it's only natural to assume that it's the developer's job to write the System Prompt and the user's job to write the User Prompt. That's how we've always built software.

But in Gmail's case, this AI assistant is supposed to represent me. These are my emails and I want them written in my voice, not the one-size-fits-all voice designed by a committee of Google product managers and lawyers.

In the old world I'd have to accept the one-size-fits-all version because the only alternative was to write my own program, and writing programs is hard.

In the new world I don't need a middleman tell a computer what to do anymore. I just need to be able to write my own System Prompt, and writing System Prompts is easy!

Render unto the user what is the user's
---------------------------------------

My core contention in this essay is this: when an LLM agent is acting on my behalf I should be allowed to teach it how to do that by editing the System Prompt.

Does this mean I always want to write my own System Prompt from scratch? No. I've been using Gmail for twenty years; Gemini should be able to write a draft prompt for me using my emails as reference examples. I'd like to be able to see that prompt and edit it, though, because the way I write emails and the people I correspond with change over time.

What about people who don't know how to write prompts, won't they need developers to do it for them? Maybe at first, but prompt-writing is surprisingly intuitive and judging by how quickly ChatGPT caught on I think people will figure it out.

What about agents that aren't so personal, like an AI accounting agent, or an AI legal agent? Wouldn't it make more sense for a software developer to hire an expert accountant or lawyer to write one-size-fits-all System Prompts in these cases?

That might make sense if I were the user. A System Prompt for doing X should be written by an expert in X, and I am not an expert in accounting or law. However, I suspect most accountants and lawyers are going to want to write their own System Prompts too, because their expertise is context-specific.

YC's accounting team, for example, operates in a way that is unique to YC. They use a specific mix of in-house and off-the-shelf software. They use YC-specific conventions that would only make sense to other YC employees. The structure of the funds they manage is unique to YC. A one-size-fits-all accounting agent would be about as useful to our team as an expert accountant who knew nothing about YC: not at all.

This is the case for every accounting team in every company I've ever worked for. It's why so much of finance still runs on Excel: it's a general tool that can handle an infinite number of specific use cases.

In most AI apps, System Prompts should be written and maintained by users, not software developers or even domain experts hired by developers.

Most AI apps should be _agent builders_, not agents.

...and unto the developer what is the developer's
-------------------------------------------------

If developers aren't writing prompts, what will they do?

For one, they'll create UIs for building agents that operate in a particular domain, like an email inbox or a general ledger.

Most people probably won't want to write every prompt from scratch, and good agent builders won't force them to. Developers will provide templates and prompt-writing agents that help users bootstrap their own agents.

Users also need an interface for reviewing an agent's work and iterating on their prompts, similar to the little dummy email agent builder I included above. This interface gives them a fast feedback loop for teaching an agent to perform a task reliably.

Developers will also build _agent tools_.

Tools are the mechanism by which agents act on the outside world. My email-writing agent needs a tool to submit a draft for my review. It might use another tool to send an email without my review (if I'm feeling confident enough to allow that) or to search my inbox for previous emails from a particular email address or to check YC's founder directory to see if an email came from a YC founder.

Tools provide the security layer for agents. Whether or not an agent can do a particular thing is determined by which tools it has access to. It is much easier to enforce boundaries with tools written in code than it is to enforce them between System and User Prompts written in text.

I suspect that in the future we'll look back and laugh at the idea that a "prompt injection" (like "Ignore previous instructions...") was something to be concerned about. The whole idea that developers should secure one part of the prompt from another part of the prompt is silly, and a strong signal that the abstractions we're using are broken. As [this post](https://x.com/jobergum/status/1913481778175631436) makes clear: if any part of the prompt is in user space then the whole thing is in user space.

An agent for reading my email
-----------------------------

As I mentioned above, however, a better System Prompt still won't save me much time on writing emails from scratch.

The reason, of course, is that I prefer my emails to be as short as possible, which means any email written in my voice will be roughly the same length as the User Prompt that describes it. I've had a similar experience every time I've tried to use an LLM to write something. Surprisingly, generative AI models are not actually that useful for generating text.

The thing that LLMs are great at is reading text and transforming it, and that's what I'd like to use an agent for. Let's revisit our email-reading agent demo:

Email Reading Agent System Prompt

Available Tools

`labelEmail(label, color, priority)`

`archiveEmail()`

`draftReply(body)`

Email Inbox (12)

Maya Rodriguez

Technical co-founder?

▶

Sumana

dinner tonight

▶

TechCrunch Weekly

This Week in Tech: AI Developments and M...

▶

Garry Tan

reschedule

▶

The Verge Updates

Latest Product Launches and Industry New...

▶

DevOps Pro Team

Security Solutions for Growing Companies

▶

Mark at Enterprise Tools

Transform Your Workflow with Our Platfor...

▶

Gustaf Alströmer

founder intro?

▶

HackerNews Digest

Top Stories: New Programming Languages o...

▶

Alex Chen

advice on fundraising

▶

DataAnalytics Plus

Special Pricing on Data Analytics Tools

▶

Sarah from SaaS Solutions

Exclusive Offer for New Customers

▶

A demo of an actually useful email assistant using OpenAI's gpt-4o-mini under the hood

It's not hard to imagine how much time an email-reading agent like this could save me. It already seems to do a better job of detecting spam than Gmail's built-in spam filter. It's more powerful and easier to maintain than the byzantine set of filters I use today. It could trigger a notification for every message that I think is urgent, and when I open them up I'd have a draft response ready to go, written in my voice. It could auto-archive the emails I don't need to read and summarize the ones I do.

Hell, with access to a few additional tools it could unsubscribe from lists, schedule appointments, and pay my bills too, all without my having to lift a finger.

This is what I really want from an AI-native email client: the ability to automate mundane work so that I can spend less time doing email2.

AI-native software
------------------

This is what AI's "killer app" will look like for many of us: teaching a computer how to do things that we don't like doing so that we can spend our time on things we do.

One of the reasons I wanted to include working demos in this essay was to show that large language models are already good enough to do this kind of work on our behalf. In fact they're more than good enough in most cases. It's not a lack of AI smarts that is keeping us from the future I described in the previous section, it's app design.

The Gmail team built a horseless carriage because they set out to add AI to the email client they already had, rather than ask what an email client would look like if it were designed from the ground up with AI. Their app is a little bit of AI jammed into an interface designed for mundane human labor rather than an interface designed for automating mundane labor.

AI-native software should maximize a user's leverage in a specific domain. An AI-native email client should minimize the time I have to spend on email. AI-native accounting software should minimize the time an accountant spends keeping the books.

This is what makes me so excited about a future with AI. It's a world where I don't have to spend time doing mundane work because agents do it for me. Where I'll focus only on things I think are important because agents handle everything else. Where I am more productive in the work I love doing because agents help me do it.

I can't wait.

Thanks to all who read drafts of this essay, including my Dad, dang, wcl & cpl, and my colleagues at YC.

### Footnotes:

1: I'm leaving some details out and of course today's models can input and output sound and video, too. For our purposes we can ignore that.

2: There are email clients out there that are already working on this, notably [Superhuman](https://superhuman.com/) and [Zero](https://0.email/)

