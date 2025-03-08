Title: Paper: Ironies of Automation

URL Source: https://ferd.ca/notes/paper-ironies-of-automation.html

Markdown Content:
I can't believe I had not yet posted notes about this absolute classic and fundamental paper from Lisanne Bainbridge titled [Ironies of Automation](https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf). The author has a website where she posted [her own revision of it](https://www.complexcognition.co.uk/2021/06/ironies-of-automation.html) almost 40 years after publication, and it's worth giving it a glance. It has over 1800 citations, its own Wikipedia page, and is just an unavoidable part of any literature that concerns itself with automation.

The core thesis of the paper is that automated systems always end up being human-machine systems regardless, and even as you automate more and more, human factors keep being of critical importance. The examples in it come from control processes in industry and flight deck automation, but are still very much applicable today. The paper is demonstrating this with a long list of ironies, and then some methods to try and tackle them.

At the center of it all are two basic requirements of automated processes: the need for someone to monitor whether the automation is behaving correctly, and the need for someone to take over if it does not. These two requirements are fundamentally clashing with some things we use automation for.

The first reason for this comes from cognitive and manual skills, both of which erode over time when not used. You can consider higher expertise as having the ability to operate more efficiently and in a smoother way. When your operators spend all their time monitoring a process and they finally need to intervene, their skills may have eroded to the point they are less experienced than they really are.

Specifically, the better the automated process is, the more unusual (and rarer) the conditions in which your operator will need to take over will be. This means that you should expect your operators to be more skilled the better your automation is, because they'll handle trickier situations with far less practice.

This is also true of cognitive actions where skills are better developed when you have quick, frequent feedback. So when you are first rolling out your automation, your operators are probably carrying solid skills that have been honed through more manual processes. But after a certain time, your next generation of operators will not have had the benefit of fast-feedback to the same extent and you may end up having to expect them not to be able to do as much, as effectively. The recall of which action best handles a situation will need to be more deliberate, less automatic, and slower.

Speaking of which, because your operators will be monitoring rare anomalies, vigilance will be an issue; people only look at data they regularly use and so you'll need automated alerts. But the more complex the system and the faster the required corrective action, the more alerts you might need; the more alerts you have, the more confusing the situation might become (I've posted notes on alert design before).

This segues nicely into a serious irony: people automate processes with the expectation that the automation will work better than people, yet people will be asked to find and correct errors with the automation:

> if the decisions can be fully specified then a computer can make them more quickly, taking into account more dimensions and using more accurately specified criteria than a human operator can. There is therefore no way in which the human operator can check in real-time that the computer is following its rules correctly. One can therefore only expect the operator to monitor the computer's decisions at some meta-level, to decide whether the computer's decisions are 'acceptable'. If the computer is being used to make the decisions because human judgement and intuitive reasoning are not adequate in this context, then which of the decisions is to be accepted? The human monitor has been given an impossible task.

Similarly, a process that has automation aiming to assist an operator by covering and self-correcting may hide underlying problematic conditions in ways that once the automation reaches its limits, trends become apparent once they are already beyond control.

The implication here is that if humans are your fallback, your automated system should ideally be running at a pace convenient for people:

> If the human operator must monitor the details of computer decision making then, ironically, it is necessary for the computer to make these decisions using methods and criteria, and at a rate, which the operator can follow, even when this may not be the most efficient method technically. If this is not done then when the operator does not believe or agree with the computer be will be unable to trace back through the system's decision sequence to see how far he does agree.

In terms of failures, Bainbridge recommends that manual shutdowns be your preferred way of dealing with issues: stop things, look, understand, fix, resume. This isn't always possible however (think of nuclear power plants, or of airplanes in flight). For slow failures, the operator can likely buy time with thoroughly practised responses that become almost like a reflex, but for fast failures that propagate faster than people can act, you need to invest in making automated reliable responses. If you can't or the consequences are too bad, she simply advises that you shouldn't build that system.

To keep people apt and current, she recommends that operators frequently run some steps manually just to remain familiar. If that isn't acceptable, she suggests working with simulators. The gotcha here is that if you want fast automated actions, the simulator must be high fidelity and support dynamic situations. She adds:

> Unknown faults cannot be simulated, and system behaviour may not be known for faults which can be predicted but have not been experienced \[...\] No one can be taught about unknown properties of the system, but they can be taught to practise solving problems within the known information. It is inadequate to expect the operator to react to unfamiliar events solely by consulting operating procedures. These cannot cover all the possibilities, so the operator is expected to monitor them and fill in the gaps. However, it is ironic to train operators in following instructions and then put them in the system to provide intelligence.

Another irony is that therefore, the most automated systems covering the most use cases are specifically those that require the most investment in training.

Whenever criteria other than raw efficiency are needed, Bainbridge predicts that human involvement will be required, particularly when the public wouldn't accept high-risk systems without a human component. This makes her state that framing humans and machines as teammates is pretty much the only way to go, but there are tricky ways to go. For example, while the computers could give the human a list of actions, if the computer is trusted for that part it should also be trusted for automating those it can rather than just asking the other to execute them.

In terms of "correcting" "human error", she mentions that it's better to put checks on effects of actions, rather than on whether specific actions are taken whenever acceptable, because it leaves room for the operators and practitioners to pick and alter strategies to meet their goals, for example. She covers some material about the use of electronic displays and how they could compare with direct hardware monitors in industrial processes, and mentions issues around how context-sensitive operating modes can be and how they may call to different processes (skills, rules, and knowledge).

She concludes that the problem does connect to team work, and that one must remain aware of the costs of production pressures:

> The human being must know which tasks the computer is dealing with and how, Otherwise the same problems arise as in human teams in which there is no clear allocation of responsibility.
> 
> \[...\]
> 
> Humans working without time-pressure can be impressive problem solvers. The difficulty remains that they are less effective when under time pressure. I hope this paper has made clear both the irony that one is not by automating necessarily removing the difficulties, and also the possibility that resolving them will require even greater technological ingenuity than does classic automation.
