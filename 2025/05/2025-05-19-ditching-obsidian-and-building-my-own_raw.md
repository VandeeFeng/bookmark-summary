Title: Ditching Obsidian and building my own

URL Source: https://amberwilliams.io/blogs/building-my-own-pkms

Published Time: 2025-05-05T14:26:24.139Z

Markdown Content:
> "You can’t really know where you are going until you know where you have been." - Maya Angelou.

The age-old mission to capture and make sense of our knowledge and experiences echoes through history, from Thomas Jefferson's Commonplace book detailing his ideas on government to Marcus Aurelius's Meditations saturated with quotations and personal reflections.

However, this pursuit to preserve knowledge isn't without its own set of fears. Are our deepest thoughts private? Are we spending a disproportionate time customizing our notes system than benefiting from it? Will our preferred notes system last the sands of time?

These were the questions that motivated me to step outside conventional offerings and build my own solution. I'm sharing my story here not to prescribe, but to demonstrate it's okay to color outside the lines. Perhaps my journey to create a simple, secure, and lasting 'note vault' will spark ideas for how you can better cultivate your own knowledge garden.

Conventional knowledge gardens
------------------------------

A personal knowledge management systems (PKMS), also known as "second brain" is are central repositories for actively collecting one's meaningful insights, ideas and inspirations encountered throughout life. The benefit of decades of notes accruing and reinforcing knowledge is immense. That is why critically analyzing what you need your PKMS to achieve is crucial.

The most commonly used PKMS or note-taking apps today are Notion, Obsidian, Evernote and Logseq. The problem is that PKMS come and go. Could you see yourself using your note-taking app you use today in 30 years? Probably not. Do you ever have concerns around the privacy of your notes? Are you spending more time setting up your notes system rather than managing your notes? What does an effective and timeless PKMS even look like?

Pulling at a thread
-------------------

My PKMS journey started with Obsidian. For those unfamiliar with Obsidian, it's a digital notebook that lives only on your computer. Its special feature is letting you internally link related notes together similar to Wikipedia. Beyond linking, its true power comes from the huge range of plugins. Out of all the great community plugins, Dataview is my personal favorite. [Dataview](https://obsidian.rocks/dataview-in-obsidian-a-beginners-guide/) is a powerful scripting tool which pulls data from markdown notes to generate tables, graphs, and other insights.

Obsidian was a great tool for me personally for a long time. But I felt frustrated when I wanted to access my notes on my phone while on-the-go and saw that I had to pay for this feature. Obsidian charges $8 a month to access the same notes across multiple devices. While not a huge amount for such a useful app, it adds up to an eye-watering amount - almost $1,000 if I planned to use Obsidian for a decade. I was surprised at this fee because I thought Obsidian was open-source. I later realized that the Obsidian community plugins are open-source, but Obsidian itself is, in fact, not. These were the same plugins I was spending an inordinate abount of time [personalizing Obsidian with](https://github.com/s-blu/obsidian_dataview_example_vault/blob/b6740b4d8a7e0b408669563e1b3c4028df36e207/20%20Dataview%20Queries/Show%20a%20Goals%20Overview%20with%20progress%20bars%20for%20included%20projects%20and%20overall%20progress.md), rather than being productive.

I started to have concerns about the longevity of the plugins and app itself. Some of you may remember when Evernote aggressively limited free users to [50 notes](https://henry-chong.com/blog/the-downfall-of-evernote/), many users migrated their notes elsewhere. I was one of those users.

After some mental gymnastics weighing if I should continue with Obsidian, I found solace when asking myself _"Can I see myself using this in 20 years?"_. I couldn't. The thought of cyclically migrating notes from one PKMS to another every 5 years, as I had done from Evernote to Notion to Obsidian, made me feel tired. So I grabbed some coffee and began my search for the digital equivalent of the [Svalbard Global Seed Vault](https://en.wikipedia.org/wiki/Svalbard_Global_Seed_Vault), but for my notes.

My perfect note vault
---------------------

Key requirements were that my new PKMS needed to be easy to use, offer a plugin-like experience and be secure. Privacy and security were paramount. I didn't want my innermost thoughts being exposed to a [23andMe data leak](https://en.wikipedia.org/wiki/23andMe_data_leak) scenario. Data security aside, I have a hard time trusting for-profit companies will keep their hands out of the cookie jar. I can imagine there's a killing to be made from targeted advertisements online using your notes or for them to be used to train AI. I wanted to know with certainty that I control my data. Entrusting a company to store my notes for free, couldn't give me that assurance.

Being a full-stack software engineer, the answer was obvious. I should step outside the commercial-PKM ecosystem entirely - I should build my own.

But if it's so obvious, why aren't other developers rolling out their own PKMS? Perhaps I'm the first to discover this or perhaps developers aren't writing about their custom PKMS. My guess is that commercial note-taking apps have larger, more vocal communities that drown out the murmurings of other DIY solutions.

It was here I decided to pull the trigger to build and host my own PKMS. It felt pertinent to write about it so others feel confident to do so too. Spoiler - it sounds like a daunting feat, but in reality it was so comically easy my only regret is that I hadn't done it years ago.

The note vault
--------------

Here's how my PKMS looks as of writing. I can create a note, update it in markdown format and then preview what the note looks like in rendered markdown.

![Image 1: gif using the PKMS's markdown editor](https://notes.holeytriangle.com/assets/0f1cfdfb-ed3d-450e-8701-8ef7a9f2d7a5)

Finally, I can access my notes from my phone too, right where I left off. No monthly fees for this feature either.

![Image 2: Using the PKMS from my phone with a thumbs up sign](https://notes.holeytriangle.com/assets/e12f4587-b8a5-4739-9b16-7e925037ac9b)

Since my PKMS is hosted online to manage notes across devices, I have multiple layers of security to ensure my notes are kept private.

![Image 3: the PKMS's login screen with an empty form](https://notes.holeytriangle.com/assets/c42ab6b2-4eae-4956-b886-50d70aacba70)

And if I ever want to move to greener pastures, all my notes are stored in Markdown so I can export them with two command lines to my terminal. Here's an under-the-hood view of how my notes are stored in the database - just text! [1](https://amberwilliams.io/blogs/building-my-own-pkms#1)

![Image 4: shows the markdown output from a database query](https://notes.holeytriangle.com/assets/2847aa38-5356-4e1d-80d9-feb5e738eee2)

Benefits of a note vault
------------------------

I've found that consistently collecting and reviewing valuable information promotes a deeper engagement with ideas. As a result, I've noticed my memory improving, and I started seeing surprising links between seemingly unrelated topics. Plus, it's created this incredible record of my learning and personal growth.

I found Ryan Holiday's take on the [Commonplace Book](https://ryanholiday.net/how-and-why-to-keep-a-commonplace-book/) particularly insightful for efficiently using a PKM. While Ryan advocates for analog notes, the same principles can be applied to digital notes. While physical writing has its merits, digital notes provide superior search capabilities and flexible organization. Ryan himself states how impracticability of a physical PKMS - "Because mine is a physical box with literally thousands of cards, I don’t carry the whole thing with me".

![Image 5: Illustration featuring a system for filing notes](https://notes.holeytriangle.com/assets/85ba3989-f61c-4f4f-8764-b1f8c267cbaa)

Image sourced from Houghton Library, Public domain, via Wikimedia Commons

And that's the beauty of a digital PKMS – it all fits on my phone!

Additonally, now with AI code generation creating custom PKMS plugins are more accessible than ever before. No longer do we need to install a random developer's plugin that sends our private thoughts who knows where. We can vibe-code our own or use open-source tooling. I used to use an Obsidian plugin to pull uncompleted tasks from todo checklists that were scattered around various notes, but after 10 minutes of prompting Anthropic's Claude, I had my own private equivalent tool.

A look inside
-------------

Using essentially a wrapper around a database made creating my PKMS easy. This wrapper does the heavy lifting, keeping things simple and secure. I went with an open-source platform called [Directus](https://directus.io/), which can be used as a PKMS amongst other things such as a CMS. Directus has authentication and security layers already included, so I was able to start using it in less than a day.

For readers who have worked with SQL databases or docker containers - I wrote a [step-by-step guide on building my own PKMS with Directus](https://amberwilliams.io/blogs/the-last-note-system).

A final note
------------

I’ve always believed that, much like a garden, how we manage our own knowledge system needs cultivation and continuity to flourish. My own knowledge garden was cultivated from a deep dive into the subject of note systems, driven by a search for a solution to those nagging frustrations I think many of us feel with commercialized systems.

A knowledge garden isn't always straightforward, and I'll be the first to admit I’ve been guilty of spending considerably more time fiddling with a system, rather than actually using it. It's easy to fall into analysis paralysis with these system as well as become plagued with paranoia worrying about privacy. So for any system to stick, it has to be genuinely secure and simple.

There isn't a one-size-fits-all approach to a sizeable amount of things in life, knowledge management being one of these. Inquisitive individuals are likely to be rewarded for exploring different avenues, even unconventional ones, as they lead to a system tailored to one's personal way of thinking and working.

The path I eventually took, building my own, put an end to exhausting cyclical migrations. It helped me reclaim control over my privacy, and significantly cut down on recurring costs. Especially because it's ran from [my own VPS](https://amberwilliams.io/blogs/vps-for-web-apps). Commercial apps certainly offer out-of-the-box convenience, but by stepping back and focusing on what mattered to me, I found a way that worked profoundly better. [Here's how I built my PKMS step-by-step](https://amberwilliams.io/blogs/the-last-note-system).

After dogfooding my PKMS for over a year now, I'm capturing and connecting ideas more efficiently than I ever managed with commercial apps. While I sometimes miss the community around commercial apps, I'm hopeful I'll find a niche community of like minded individuals one day.

If my PKMS journey has resonated with you, or if you're on a similar path, I'd genuinely love to connect. You can find me at any of the socials in the footer.

* * *
