Title: End of An Era | Interactive Storytelling Tools for Writers

URL Source: http://www.erasmatazz.com/personal/self/end-of-an-era.html

Markdown Content:
I recall saying to one of my colleagues at Atari way back in 1982 that I wanted to make a game that would be genuine art. A year later I built a game that was my first experiment in that direction: Gossip. It was a ridiculously simple game in which a player attempted to win favor in a group by calling people and telling them how much you liked or disliked some third party. The underlying concept was that “people like people who like people they like.” For some reason, many players had problems absorbing this simple concept.

Gossip

I later incorporated many of the ideas in Gossip into Excalibur, my first Arthurian game. But Atari collapsed soon after that, and I had to make a living as a freelance game designer. That kept me busy for the rest of the 1980s, but after I published my last game, Balance of the Planet, in 1990, I resolved to come back to the computer-games-as-art goal. I wanted to make another Arthurian game with much greater emphasis on the interpersonal interactions. I knew that my ambitions would take several years to realize, but I felt that the future lay in this direction, so I went ahead. I started building the game, and it went well. I began approaching publishers, and struck out everywhere. They greatly respected my reputation as one of the top game designers in the world, but they had decided that the only games that would sell had to be variations on Doom or Myst.

Then the Markle Foundation came to the rescue with an offer that was to bail me out in the short run and send me down the wrong path in the long run. They offered me $350,000 to build a tool for other people to create interactive storyworlds. The idea appealed to me, so I accepted the offer and went to work. Now, most of the money went to various contractors, even though I designed and wrote all the code. The result was the Erasmatron. I don’t have a screenshot of the Erasmatron user interface. My primary goal was to build software that would permit a storyteller to implement many of the dramatic processes that take place in a story. For example, there was a component that permitted one character to spy on two other characters conversing without being seen. There was an extensive system for managing how information traveled through a group of people and how secrets were kept or broken.

I won’t dwell on Erasmatron, as it evolved into Storytron, but I will note that Erasmatron had no takers. Other than Laura Mixon, nobody ever built anything with Erasmatron.

Storytron

This was the culmination of my effort to build a software development environment for interactive storytelling. It is best understood as Erasmatron with a much superior user interface and considerably better support features.

The central component of Storytron was Deikto, a technology for creating a toy language specific to an interactive storyworld. “Toy language” is my term for a tiny language containing only the words necessary to permit interaction between characters in the storyworld. Toy languages do not need anywhere near as large a vocabulary as a full language. A storyworld for children will have no verbs for sex, higher education, jobs, finance, marriage, alcohol, and many other things. Similarly, a storyworld about corporate politics can dispense with scientific verbs, most economic and financial verbs, verbs for family interactions, and not much about food. A good storyworld designer can, in my estimate, build an adequate toy language for most storyworlds with only a few hundred verbs.

The verbs are the core of the system; the player can build sentences out of the verbs and all the other words in the system. There are words for actors, props, and stages.

This description is growing too large. Storytron technology had many other wonderful features that I won’t describe here. The important point I want to make is that nobody was interested in Storytron. I spread the word about it as well as I could, but I’m no salesman. I spent about ten years on Storytron and a great deal of my money hiring contractors to do some of the work that I couldn’t do. And it was all for nothing. Storytron was just too complicated for the audience. I don’t think that was because it was intrinsically too complicated for anybody to understand. My impression is that there just weren’t any people willing to make the big commitment required to learn how to use Storytron. It was easier to learn than professional programming systems like Eclipse or the Microsoft suite of software development applications. But it demanded more of its users than they were willing to invest.

Siboot

I made one last effort to make Storytron work using Siboot, a concept that I had developed in 1987. I poured my energy into Siboot, and a number of good people helped me, but after I had expended several years on it, I realized that it was crap. The story felt too mechanical. I realized that it needed a boost in the form of the encounter technology that I had developed for the 1987 version, but at that point I was so discouraged that I just couldn’t go on. I gave up on Siboot.

Le Morte d’Arthur

I gave up on Storytron around 2018. It was painful to accept that all the energy, all the creativity, all the sweat I had committed to the project was for naught, but I had no choice. I rested for some months, then in 2020, for my 70th birthday, I realized that I was growing old and would not be able to handle a tough technical challenge for much longer. I therefore decided that the time had come for me to make one last effort, and that effort had to an Arthurian game. I re-read the many Arthurian books I had accumulated during previous efforts, girded my loins, and set to work. I made many changes along the way; the final version of Le Morte d’Arthur was quite unlike the original. But it worked. I knew that, after all these years, I had finally achieved my goal of making genuine interactive art. I was proud, tired, and gratified. Not many people played the storyworld, but I didn’t care. That was the world’s failure, not mine.

I continued to fiddle around with interactive storytelling, discussing issues with a small group of people devoted to the problem. I even made a few attempts to make the technology I used for Le Morte d’Arthur available to others, but, once again, nobody was interested.

Late in 2024 I happened upon a mention of Narrascope, an annual conference for interactive fiction held once every June. I knew of the conference from previous references, and it occurred to me that I had one last shot at making interactive storytelling technology available to the world. The attendees of Narrascope were not the techie types I had previously dealt with. These were mostly storytellers, weaker on the technology but stronger on the storytelling side. I decided to make my technology available to them, but to do so I would have to strip away all the technical complexity. I set to work building a web page that could edit storyworlds, using HTML, CSS, Javascript, and JSON. My programming powers were fading fast. Time and time again I would send my friend Dave Walker an email declaring that Javascript (or something else) was utterly broken, incapable of executing the simplest program without errors. Dave would ask to see the source code and I would present it to him with detailed notes proving that my code was perfect and Javascript was broken. He’d call me, we’d discuss it, and eventually he’d say something like, “Where did you terminate the loop beginning at line 563?” There would be a long silence, followed by the tiniest “Oh” from me. I’d thank him for his help and hang up. A week later, I’d be fuming again about another fundamental flaw in Javascript.

Narrascope had accepted my lecture proposal, as well as my request to deliver a workshop on my technology. I spent dozens of hours working on the lecture; my lectures have always been top-notch and I wasn’t about to scrimp on this one. I made scores of nifty-keen images to illustrate my points. When will people learn that text doesn’t belong on a slide???

Meanwhile, I struggled with the program. I didn’t quite get it finished, but it was workable and users could readily see that it was close to completion.

On the big day I arrived at the airport at 5:00 AM to catch the early flight. We sat on the tarmac for an hour because of a mechanical problem, at which point I realized that I could not possibly make a crucial connection. I had to abort the trip to Narrascope and deliver the lectures via video, which turned out to be disastrous.

This was my last-gasp effort to stimulate progress in interactive storytelling. "Once more, into the breach!” I had told myself. Now, more than a week after I delivered my spiel, not one person has answered my call for emails expressing some interest in my technology. Once again, my efforts were in vain.

And so it is time for me to admit that, after all those decades of work, I have failed, with the single exception of Le Morte d’Arthur. When I designed for myself, I succeeded. When I designed for others, I failed. It’s time to throw in the towel and leave interactive storytelling to others. I don’t think that the world is ready. I feel like Charles Babbage, who invented the programmable computer in 1850. It used gears, levers, and cams and was brilliant. But the world had no need for programmable computers in 1850, so he never got the funding to build his invention. I’m nowhere near as smart as Charles Babbage, but my life dimly echoed his.

I realized that my opus magnus, Le Morte d’Arthur, is a metaphorical autobiography of sorts. At the least, it expresses my experience working on interactive storytelling. Here is Merlin’s final conversation with Arthur:

Merlin: Yes, Arthur, you failed. The Britons were exterminated as a race.

Arthur: But I thought I had done well!

Merlin:Indeed you did. Your sacrifice inspired all. You became a myth, and your story reverberated through the ages.You'd be surprised at the magnificence of the mythological Arthur. I doubt you'd recognize him.Did you know that you pulled Excalibur right out of the stone in which it was embedded?

Arthur:That's not true!

Merlin:Of course not! It's a myth. It's the story you created.

Arthur:But how could I have failed, Merlin? What was my mistake?

Merlin:You made no mistake. You led your people admirably.

Arthur:Then how did I fail to save my people?

Merlin:Don't you remember our conversation during which you realized that the Saxons were outbreeding your people Come, come, Arthur, do you truly believe that you control the world?Do you harbor the conceit that one man can change the flow of Fate?

Arthur:Well, no, but still, could I not...

Merlin:You judge yourself by an impossible standard.You were certainly courageous. You attempted feats no one thought possible, and you accomplished many of those impossible feats.But courage, skill, and determination cannot overcome simple facts.You were doomed to face ever-larger numbers of Saxons every year.In the end, the goal you sought, to throw back the invaders, was hopeless.There were too many of them and too few Britons.Your purpose was noble, and your achievements astounding, but you simply could not foil Fate.Oh, don't feel so bad. Don't you remember what I tried to teach you all through the years?Your life is a story, and you made a story fit for future generations. You left a fine story, a noble story that has inspired countless generations.

Arthur:But I failed in my most important goal: to save my people!

Merlin:No! What you did was an inspiration.You fought against impossible odds and held off defeat for decades.You showed humanity that there is greatness in fighting the hopeless fight.Most men stumble through life clinging to their mediocrity.You demonstrated that it is better to aim high and fail than to yield to the cruelties of Fate.You led a worthy life, Arthur, and the world is a better place because of the story you lived.How many men can say that?

The time has come to close this chapter of my life. Perhaps I shall write a book summarizing my findings. Perhaps I shall not.
