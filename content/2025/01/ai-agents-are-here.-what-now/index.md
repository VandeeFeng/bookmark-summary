---
title: AI Agents Are Here. What Now
date: 2025-01-17
extra:
  source: https://huggingface.co/blog/ethics-soc-7
  original_title: AI Agents Are Here. What Now
---
## Summary
**摘要**：
本文探讨了AI代理的概念及其对社会的影响，分析了其伦理价值观、利益和风险。AI代理的核心特征是能够在数字世界中执行与部署者目标一致的动作，其显著特点是能够组合执行多种任务，而无需人类干预。文章强调了充分考虑AI代理潜在风险的重要性，尤其是系统控制权增强可能带来的风险。通过检视AI代理提供的各种价值（如准确度、协助性、稳定性等），文章突出了在开发AI代理过程中面临的道德挑战，呼吁避免完全自主的AI代理开发，并推荐了多种发展方向，如开发强悍的评估框架、改善交互效果分析、促进透明性提升、推动开源参与以及关注公益。

**要点总结**：
- **AI代理概览**：AI代理是能够在数字世界中执行动作并与用户目标一致的智能体，它们能够执行多种任务而不受人类干预，这是一个系统性转变。
- **AI代理风险与挑战**：AI代理开发中的关键风险包括安全风险、信任滥用、隐私侵犯、信任不适当等，同时也讨论了LTM误解导致的错误信息风险。
- **AI代理的伦理与应用分析**：文章深入探讨了AI代理在不同维度上的价值和风险，强调了值导向的伦理分析的重要性。
- **在Hugging Face平台的应用**：Hugging Face通过发布生态系统工具、教程、概念指南、用户界面、代码代码编辑和agent工具，促进了AI代理的开发和使用，同时强调了价值导向设计的必要性。
- **未来发展建议**：文章提议了规范评估机制、改善效果分析、增强透明度、加强开源合作、增强交互效果、推动更开放讨论与对齐公众利益的逐步发展方向。 

### 开发严谨评估机制，关注AI代理社会影响和效果的演变。
### 深入研究AI代理对社会经济环境的影响，包括个体、组织、经济和环境层面。
### 研究AI代理互动的连锁反应及其对用户目标的潜在影响。
### 改进透明度和披露机制，确保用户清楚知道正在与AI代理互动，并理解其自主程度。
### 推动开源合作，通过共享架构和评估标准，促进广泛的参与，促进公开讨论，确保价值一致性。
### 关注代理未来的多模态训练方向，预测AI代理模型将成为聚合执行多种任务的一体化模式。
## Full Content
Title: AI Agents Are Here. What Now?

URL Source: https://huggingface.co/blog/ethics-soc-7

Markdown Content:
[Back to Articles](https://huggingface.co/blog)

*   [Introduction](https://huggingface.co/blog/ethics-soc-7#introduction "Introduction")
    
*   [What is an AI agent?](https://huggingface.co/blog/ethics-soc-7#what-is-an-ai-agent "What is an AI agent?")
    *   [Overview](https://huggingface.co/blog/ethics-soc-7#overview "Overview")
        
    *   [The Spectra of AI Agents](https://huggingface.co/blog/ethics-soc-7#the-spectra-of-ai-agents "The Spectra of AI Agents")
        
*   [Risks, Benefits, and Uses: A Values-Based Analysis](https://huggingface.co/blog/ethics-soc-7#risks-benefits-and-uses-a-values-based-analysis "Risks, Benefits, and Uses: A Values-Based Analysis")
    *   [Value: Accuracy](https://huggingface.co/blog/ethics-soc-7#value-accuracy "Value: Accuracy")
        
    *   [Value: Assistiveness](https://huggingface.co/blog/ethics-soc-7#value-assistiveness "Value: Assistiveness")
        
    *   [Value: Consistency](https://huggingface.co/blog/ethics-soc-7#value-consistency "Value: Consistency")
        
    *   [Value: Efficiency](https://huggingface.co/blog/ethics-soc-7#value-efficiency "Value: Efficiency")
        
    *   [Value: Equity](https://huggingface.co/blog/ethics-soc-7#value-equity "Value: Equity")
        
    *   [Value: Humanlikeness](https://huggingface.co/blog/ethics-soc-7#value-humanlikeness "Value: Humanlikeness")
        
    *   [Value: Interoperability](https://huggingface.co/blog/ethics-soc-7#value-interoperability "Value: Interoperability")
        
    *   [Value: Privacy](https://huggingface.co/blog/ethics-soc-7#value-privacy "Value: Privacy")
        
    *   [Value: Relevance](https://huggingface.co/blog/ethics-soc-7#value-relevance "Value: Relevance")
        
    *   [Value: Safety](https://huggingface.co/blog/ethics-soc-7#value-safety "Value: Safety")
        
    *   [Value: Scientific Progress](https://huggingface.co/blog/ethics-soc-7#value-scientific-progress "Value: Scientific Progress")
        
    *   [Value: Security](https://huggingface.co/blog/ethics-soc-7#value-security "Value: Security")
        
    *   [Value: Speed](https://huggingface.co/blog/ethics-soc-7#value-speed "Value: Speed")
        
    *   [Value: Sustainability](https://huggingface.co/blog/ethics-soc-7#value-sustainability "Value: Sustainability")
        
    *   [Value: Trust](https://huggingface.co/blog/ethics-soc-7#value-trust "Value: Trust")
        
    *   [Value: Truthfulness](https://huggingface.co/blog/ethics-soc-7#value-truthfulness "Value: Truthfulness")
        
*   [AI Agents at HF](https://huggingface.co/blog/ethics-soc-7#ai-agents-at-hf "AI Agents at HF")
    
*   [Recommendations & What Comes Next](https://huggingface.co/blog/ethics-soc-7#recommendations--what-comes-next "Recommendations &amp; What Comes Next")
    

[![Image 29: Huggy the Pooh](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/190_ethics-soc-7/huggy_the_pooh.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/190_ethics-soc-7/huggy_the_pooh.png)

[](https://huggingface.co/blog/ethics-soc-7#introduction)Introduction
---------------------------------------------------------------------

The sudden, rapid advancement of LLM capabilities – such as writing fluent sentences and achieving increasingly high scores on benchmarks – has led AI developers and businesses alike to look towards what comes next: What game-changing technology is just on the horizon? One technology very recently taking off is “AI agents”, systems that can take actions in the digital world aligned with a deployer’s goals. Most of today’s AI agents are built by incorporating large language models (LLMs) into larger systems that can perform multiple functions. A fundamental idea underlying this new wave of technology is that computer programs no longer need to function as human-controlled tools, confined to specialized tasks: They can now combine multiple tasks without human input.

This transition marks a fundamental shift to systems capable of creating context-specific plans in non-deterministic environments. Many modern AI agents do not merely perform pre-defined actions, but are designed to analyze novel situations, develop relevant goals, and take previously undefined actions to achieve objectives.

In this piece, we briefly overview what AI agents are and detail the ethical values at play, documenting tradeoffs in AI agent benefits and risks. We then suggest paths forward to bring about a future where AI agents are as beneficial as possible for society. For an introduction to the technical aspects of agents, [please see our recent developer blogpost](https://huggingface.co/blog/smolagents). For an introduction to agents written before modern generative AI (that is largely still applicable today) please see [Wooldridge and Jennings, 1995](https://core.ac.uk/download/pdf/1498750.pdf).

Our analysis reveals that risks to people increase with a system’s level of autonomy: The more control a user cedes, the more risks arise from the system. Particularly concerning are risks for the **safety** of individuals that arise from the same benefits that motivate AI agent development, such as freeing developers from having to predict all actions a system may take. Further compounding the issue, some safety harms open the door for other types of harm – such as harms of [privacy](https://huggingface.co/blog/ethics-soc-7#value-privacy) and [security](https://huggingface.co/blog/ethics-soc-7#value-security) – and inappropriate [trust](https://huggingface.co/blog/ethics-soc-7#value-trust) in unsafe systems enables a snowball effect of yet further harms. As such, we recommend that fully autonomous AI agents are not developed. For example, AI agents that can write and execute their own code, beyond constrained code options controlled by the developer, will be endowed with the ability to override all human control. In contrast, semi-autonomous AI agents may have benefits that outweigh risks, depending on the level of autonomy, the tasks available to the system, and the nature of individuals’ control over it. We now turn to these topics in-depth.

[](https://huggingface.co/blog/ethics-soc-7#what-is-an-ai-agent)What is an AI agent?
------------------------------------------------------------------------------------

### [](https://huggingface.co/blog/ethics-soc-7#overview)Overview

There is no clear consensus on what an “AI agent” is, but a commonality across recently introduced AI agents is that they are “agentic”, that is, they act with some level of **autonomy**: given the specification of a goal, they can decompose it into subtasks and execute each without direct human intervention. For example, an ideal AI agent could respond to a high-level request such as “help me write better blogposts” by independently breaking this task down into retrieving writing on the web that is similar to your previous blog topics; creating documents with outlines for new blog posts; and providing initial writing within each. Recent work on AI agents has made possible software with a broader range of functionality and more flexibility in how it can be used than in the past, with recent systems deployed for everything from organizing meetings ([example1](https://www.lindy.ai/template-categories/meetings), [example2](https://zapier.com/agents/templates/meeting-prep-assistant), [example3](https://www.ninjatech.ai/product/ai-scheduling-agent), [example4](https://attri.ai/ai-agents/scheduling-agent)) to creating personalized social media posts ([example](https://www.hubspot.com/products/marketing/social-media-ai-agent)), without explicit instructions on how to do so.

All recently introduced AI agents we’ve surveyed for this newsletter are built on machine learning models, and most specifically use **large language models** (LLMs) to drive their actions, which is a new, novel approach for computer software. Aside from being built on machine learning, today’s AI agents share similarities with those in the past, and in some cases realize [previous theoretical ideas of what agents might be like](https://core.ac.uk/download/pdf/1498750.pdf): acting with autonomy, demonstrating (perceived) social ability, and appropriately balancing reactive and proactive actions.

These characteristics have gradations: Different AI agents have different levels of capabilities, and may work in isolation or in concert with other agents towards a goal. As such, AI agents may be said to be more or less autonomous (or _agentic_), and the extent to which something is an agent may be viewed on a continuous spectrum. This fluid notion of AI agent has led to recent confusions and misunderstandings about what AI agents are, which we hope to bring some clarity to here. A table detailing the varying levels of AI agent is provided below.

| Agentic Level | Description | Who's in Control | What that's Called | Example Code |
| --- | --- | --- | --- | --- |
| ☆☆☆☆ | Model has no impact on program flow | 👤 The developer controls all possible functions a system can do and when they are done. | Simple processor | `print_llm_output(llm_response)` |
| ★☆☆☆ | Model determines basic control flow | 👤 The developer controls all possible functions a system can do; the system controls when to do each. | Router | `if llm_decision(): path_a() else: path_b()` |
| ★★☆☆ | Model determines how function is executed | 👤 💻 The developer controls all possible functions a system can do and when they are done; the system controls how they are done. | Tool call | `run_function(llm_chosen_tool, llm_chosen_args)` |
| ★★★☆ | Model controls iteration and program continuation | 💻 👤 The developer controls high-level functions a system can do; the system controls which to do, when, and how. | Multi-step agent | `while llm_should_continue(): execute_next_step()` |
| ★★★★ | Model writes and executes new code | 💻 The developer defines high-level functions a system can do; the system controls all possible functions and when they are done. | Fully autonomous agent | `create_and_run_code(user_request)` |

_Table 1. One example of how systems using machine-learned models, such as LLMs, can be more or less agentic. Systems can also be combined in "multiagent systems," where one agent workflow triggers another, or multiple agents work collectively toward a goal.  
Adapted from [smolagent blog post](https://huggingface.co/blog/smolagents), with changes tailored for this blog post._

From an ethics perspective, it is also useful to understand the continuum of autonomy in terms of how control is ceded from people and given to machines. The more autonomous the system, the more we cede human control.

Throughout this piece, we use some anthropomorphising language to describe AI agents, consistent with the language that is currently used to describe them. [As was also noted in historic scholarship](https://core.ac.uk/download/pdf/1498750.pdf), describing AI agents using mentalistic language ordinarily applied to humans – such as having knowledge, beliefs, and intentions – can be an issue for appropriately informing users about system abilities. For better or worse, such language serves as an abstraction tool to gloss over more precise details of the technology. Understanding this is critical when grappling with the implications of what these systems are and the role they may play in peoples’ lives: The use of mentalistic language describing AI agents does not entail that these systems have a mind.

### [](https://huggingface.co/blog/ethics-soc-7#the-spectra-of-ai-agents)The Spectra of AI Agents

AI agents vary on a number of interrelated dimensions:

*   **Autonomy:** Recent “agents” can take at least one step without user input. The term “agent” is currently used to describe everything from single-step prompt-and-response systems ([citation](https://blogs.microsoft.com/blog/2024/10/21/new-autonomous-agents-scale-your-team-like-never-before/)) to multi-step customer support systems ([example](https://www.lindy.ai/solutions/customer-support)).
*   **Proactivity:** Related to autonomy is proactivity, which refers to the amount of goal-directed behavior that a system can take without a user directly specifying the goal ([citation](https://core.ac.uk/download/pdf/1498750.pdf)). An example of a particularly “proactive” AI agent is a system that monitors your refrigerator to determine what food you are running out of, and then purchases what you need for you, without your knowledge. [Smart thermostats](https://en.wikipedia.org/wiki/Smart_thermostat) are proactive AI agents that are being increasingly adopted in peoples’ homes, automatically adjusting temperature based on changes in the environment and patterns that they learn about their users’ behavior ([example](https://www.ecobee.com/en-us/smart-thermostats/)).
*   **Personification:** An AI agent may be designed to be more or less like a specific person or group of people. Recent work in this area ([example1](https://arxiv.org/abs/2411.10109), [example2](https://www.researchgate.net/publication/387362519_Multi-Agent_System_for_Emulating_Personality_Traits_Using_Deep_Reinforcement_Learning), [example3](https://medium.com/@damsa.andrei/ai-with-personality-prompting-chatgpt-using-big-five-values-def7f050462a)) has focused on designing systems after the Big Five personality traits – Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism as a “psychological framework” ([citation](https://smythos.com/artificial-intelligence/conversational-agents/conversational-agent-frameworks/#:~:text=The%20OCEAN%20Model%3A%20A%20Framework%20for%20Digital%20Personality&text=OCEAN%20stands%20for%20Openness%2C%20Conscientiousness,feel%20more%20authentic%20and%20relatable.)) for AI. At the end of this spectrum would be “digital twins”, ([example non-agentic digital twin](https://www.tavus.io/)). There are currently not agentic digital twins that we are aware of. Why creating agentic digital twins is particularly problematic has recently been discussed by [the ethics group at Salesforce](https://www.salesforce.com/blog/ai-agent-design/), among others ([example](https://www.technologyreview.com/2024/11/26/1107309/we-need-to-start-wrestling-with-the-ethics-of-ai-agents/)).
*   **Personalization:** AI agents may use language or perform actions that are aligned to a user’s individual needs, for example, to make [investment recommendations](https://www.zendesk.com/blog/ai-agents/) based on current market patterns and investments a user has made in the past.
*   **Tooling:** AI agents also have varying amounts of additional resources and tools they have access to. For example, the initial wave of AI agents accessed search engines to answer queries, and further tooling has since been added to allow them to manipulate other tech products, like documents and spreadsheets ([example1](https://huggingface.co/blog/gemini.google.com), [example2](https://copilot.microsoft.com/)).
*   **Versatility:** Related to above is how diverse the actions that an agent can take are. This is a function of:
    *   **Domain specificity:** How many different domains an agent can operate in. For example, just email, versus email alongside online calendars and documents.
    *   **Task specificity:** How many different types of tasks the agent may perform. For example, scheduling a meeting by creating a calendar invite in participants’ calendars ([example](https://attri.ai/ai-agents/scheduling-agent)), versus additionally sending reminder emails about the meeting and providing a summary of what was said to all participants when it’s over ([example](https://www.nyota.ai/)).
    *   **Modality specificity:** How many different modalities that an agent can operate in – text, speech, video, images, forms, code. Some of the most recent AI agents are created to be highly multimodal ([example](https://deepmind.google/technologies/project-mariner/))), and we predict that AI agent development will continue to increase multimodal functionality.
    *   **Software specificity:** How many different types of software the agent can interact with, and at what level of depth.
*   **Adaptibility:** Similar to versatility is the extent to which a system can update its action sequences based on new information or changes in context. This is also described as being “dynamic” and “context-aware”.
*   **Action surfaces:** The places where an agent can do things. Traditional chatbots are limited to a chat interface; chat-based agents may additionally be able to surf the web and access spreadsheets and documents ([example](https://huggingface.co/blog/copilot.microsoft.com/)), and may even be able to do such tasks via controlling items on your computer’s graphical interface, such as by moving around the mouse ([example1](https://huggingface.co/blog/DigiRL), [example2](https://github.com/MinorJerry/WebVoyager), [example2](https://www.anthropic.com/news/3-5-models-and-computer-use)). There have also been physical applications, such as using a model to power robots ([example](https://deepmind.google/discover/blog/shaping-the-future-of-advanced-robotics/)).
*   **Request formats:** A common theme across AI agents is that a user should be able to input a request for a task to be completed, without specifying fine-grained details on how to achieve it. This can be realized with low-code solutions ([example](https://huggingface.co/blog/smolagents)), with human language in text, or with voiced human language ([example](https://play.ai/)). AI agents whose requests can be provided in human language are a natural progression from recent successes with LLM-based chatbots: A chat-based “AI agent” goes further than a chatbot because it can operate outside of the chat application.
*   **Reactivity:** This characteristic refers to how long it takes an AI agent to complete its action sequence: Mere moments, or a much longer span of time. A forerunner to this effect can be seen with modern chatbots. For example, ChatGPT responds in mere milliseconds, while Qwen QwQ takes several minutes, iterating through different steps labelled as “Reasoning”.
*   **Number:** Systems can be single-agent or multi-agent, meeting needs of users by working together, in sequence, or in parallel.

[](https://huggingface.co/blog/ethics-soc-7#risks-benefits-and-uses-a-values-based-analysis)Risks, Benefits, and Uses: A Values-Based Analysis
----------------------------------------------------------------------------------------------------------------------------------------------

To examine AI agents through an ethical lens, we break down their risks and benefits according to the different values espoused in recent AI agent research and marketing. These are not exhaustive, and are in addition to the risks, harms, and benefits that have been documented for the technology that AI agents are based on – [such as LLMs](https://dl.acm.org/doi/10.1145/3442188.3445922). We intend this section to contribute to the understanding of how to develop AI agents, providing information on the benefits and risks in different development priorities. These values might also inform evaluation protocols (such as red-teaming).

### [](https://huggingface.co/blog/ethics-soc-7#value-accuracy)Value: Accuracy

*   🙂 **Potential Benefits:** By grounding in trusted data, agents can be more accurate than when operating from pure model output alone. This may be done via rule-based approaches or machine learning approaches such as RAG, and time is ripe for novel contributions for ensuring accuracy.
*   😟 **Risks:** The backbone of modern AI agents is generative AI, which does not distinguish between real and unreal, fact and fiction. For example, large language models are designed to construct text that looks like fluent language – meaning they often produce content that sounds right, but is very wrong. Applied within an AI agent, LLM output could lead to incorrect social media posts, investment decisions, meeting summaries, etc.

### [](https://huggingface.co/blog/ethics-soc-7#value-assistiveness)Value: Assistiveness

*   🙂 **Potential Benefits:** Agents are ideally assistive for user needs, supplementing (not supplanting) people. Ideally, they can help increase a user’s [speed](https://huggingface.co/blog/ethics-soc-7#value-speed) in completing tasks and their [efficiency](https://huggingface.co/blog/ethics-soc-7#value-efficiency) in finishing multiple tasks simultaneously. Assistive agents may also augment capabilities to minimize negative outcomes, such as an AI agent that helps a blind user navigate busy staircases. AI agents that are well-developed to be assistive could offer their users more freedom and opportunity, help to improve their users’ positive impact within their organizations, or help users to increase their reach on public platforms.
*   😟 **Risks:** When agents replace people – such as when AI agents are used instead of people at work – this can create job loss and economic impacts that drive a further divide between the people creating technology and the people who have provided data for the technology (often without consent). Further, assistiveness that is poorly designed could lead to harms from overreliance or inappropriate [trust](https://huggingface.co/blog/ethics-soc-7#value-trust).

### [](https://huggingface.co/blog/ethics-soc-7#value-consistency)Value: Consistency

One idea discussed for AI agents is that they can help with consistency, as they can be less affected than people by their surrounding environment. This can be good or bad. We are not aware of rigorous work on the nature of AI agent consistency, although related work has shown that the LLMs many AI agents are based on is highly inconsistent ([citation1](https://www.medrxiv.org/content/10.1101/2023.08.03.23293401v2), [citation2](https://arxiv.org/abs/2405.01724)). Measuring AI agent consistency will require the development of new evaluation protocols, especially in sensitive domains

*   🙂 **Potential Benefits:** AI agents are not “affected” by the world in a way that humans are, with inconsistencies caused by mood, hunger, sleep level, or biases in the perception of people (although AI agents perpetuate biases based on the human content they were trained on). Multiple companies have highlighted consistency as a key benefit of AI agents ([example1](https://www.salesforce.com/agentforce/what-are-ai-agents), [example2](https://www.oracle.com/artificial-intelligence/ai-agents/)).
*   😟 **Risks:** The generative component of many AI agents introduces inherent variability in outcomes, even across similar situations. This might affect [speed](https://huggingface.co/blog/ethics-soc-7#value-speed) and [efficiency](https://huggingface.co/blog/ethics-soc-7#value-efficiency), as people must uncover and address an AI agent’s inappropriate inconsistencies. Inconsistencies that go unnoticed may create [safety](https://huggingface.co/blog/ethics-soc-7#value-safety) issues. Consistency may also not always be desirable, as it can come in tension with [equity](https://huggingface.co/blog/ethics-soc-7#value-equity). Maintaining consistency across different deployments and chains of actions will likely require an AI agent to record and compare its different interactions – which brings with it risks of surveillance and [privacy](https://huggingface.co/blog/ethics-soc-7#value-privacy).

### [](https://huggingface.co/blog/ethics-soc-7#value-efficiency)Value: Efficiency

*   🙂 **Potential Benefits:** A selling point of AI agents is that they can help people to be more efficient – e.g., they’ll organize your documents for you, so you can focus on spending more time with your family or pursuing work you find rewarding.
*   😟 **Risks:** A potential drawback is that they may make people less efficient, as trying to identify and fix errors that agents introduce – which may be a complex cascade of issues due to agents’ ability to take multiple sequential steps – can be time-consuming, difficult, and stressful.

### [](https://huggingface.co/blog/ethics-soc-7#value-equity)Value: Equity

AI agents may affect how equitable, fair, and inclusive situations are.

*   🙂 **Potential Benefits:** AI agents can potentially help “level the playing field”. For example, a meeting assistant might display how much time each person has had to speak. This could be used to promote more equal participation or highlight imbalances across gender or location ([example](https://equaltime.io/)).
*   😟 **Risks:** The machine learned models underlying modern AI agents are trained on human data; humans data can be inequitable, unfair, exclusionary and worse. Inequitable system outcomes may also emerge due to sample bias in data collection (for example, overrepresenting some countries).

### [](https://huggingface.co/blog/ethics-soc-7#value-humanlikeness)Value: Humanlikeness

*   🙂 **Potential Benefits:** Systems capable of generating human-like behavior offer the opportunity to run simulations on how different subpopulations might respond to different stimuli. This can be particularly useful in situations where direct human experimentation might cause harm, or when a large volume of simulations help to better solve the experimental question at hand. For example, synthesizing human behavior could be used to predict dating compatibility, or forecast economic changes and political shifts. Another potential benefit currently being researched is that humanlikeness can be useful for ease of communication and even companionship ([example](https://dl.acm.org/doi/abs/10.1145/3213050)).
*   😟 **Risks:** This benefit can be a double-edged sword: Humanlikeness can lead users to **anthropomorphise** the system, which may have negative psychological effects such as overreliance ([citation](https://www.vox.com/future-perfect/367188/love-addicted-ai-voice-human-gpt4-emotion)), [inappropriate trust](https://huggingface.co/blog/ethics-soc-7#value-trust), dependence, and emotional entanglement, leading to anti-social behavior or self-harm ([example](https://www.npr.org/2024/12/10/nx-s1-5222574/kids-character-ai-lawsuit)). There is concern that AI agent social interaction may contribute to loneliness, but see [citation1](https://www.sciencedirect.com/science/article/abs/pii/S0747563203000402), [citation2](https://www.sciencedirect.com/science/article/pii/S245195882100018X) for nuances that may be gleaned from social media use. The phenomenon of uncanny valley adds another layer of complexity - as agents become more humanlike but fall short of perfect human simulation, they can trigger feelings of unease, revulsion, or cognitive dissonance in users.

### [](https://huggingface.co/blog/ethics-soc-7#value-interoperability)Value: Interoperability

*   🙂 **Potential Benefits:** Systems that can operate with others can provide more flexibility and options in what an AI agent can do.
*   😟 **Risks:** However, this can compromise [safety](https://huggingface.co/blog/ethics-soc-7#value-safety) and [security](https://huggingface.co/blog/ethics-soc-7#value-security), as the more an agent is able to affect and be affected by systems outside of its more limited testing environment brings with it increased risk of malicious code and unintended problematic actions. For example, an agent that is connected to a bank account so that it can easily purchase items on behalf of someone would be in a position to drain the bank account. Because of this concern, tech companies have refrained from releasing AI agents that can make purchases autonomously ([citation](https://www.wired.com/story/amazon-ai-agents-shopping-guides-rufus/)).

### [](https://huggingface.co/blog/ethics-soc-7#value-privacy)Value: Privacy

*   🙂 **Potential Benefits:** AI agents may offer some privacy in keeping transactions and tasks wholly confidential, aside from what is monitorable by the AI agent provider.
*   😟 **Risks:** For agents to work according to the user's expectations, the user may have to provide detailed personal information, such as where they are going, who they are meeting with, and what they are doing. For the agent to be able to act on behalf of the user in a personalized way, it may also have access to applications and information sources that can be used to extract further private information (for example, from contact lists, calendars, etc.). Users can easily give up control of their data - and private information about other people - for [efficiency](https://huggingface.co/blog/ethics-soc-7#value-efficiency) (and even more if there is [trust](https://huggingface.co/blog/ethics-soc-7#value-trust) in the agent); if there is a privacy breach, the interconnectivity of different content brought by the AI agent can make things worse. For example, an AI agent with access to phone conversations and social media posting could share highly intimate information to the world.

### [](https://huggingface.co/blog/ethics-soc-7#value-relevance)Value: Relevance

*   🙂 **Potential Benefits:** One motivation for creating systems that are personalized to individual users is to help ensure that their output is particularly relevant and coherent for the users.
*   😟 **Risks:** However, this personalization can amplify existing biases and create new ones: As systems adapt to individual users, they risk reinforcing and deepening existing prejudices, creating confirmation bias through selective information retrieval, and establishing echo-chambers that reify problematic viewpoints. The very mechanisms that make agents more relevant to users - their ability to learn from and adapt to user preferences - can inadvertently perpetuate and strengthen societal biases, making the challenge of balancing personalization with responsible AI development particularly difficult.

### [](https://huggingface.co/blog/ethics-soc-7#value-safety)Value: Safety

*   🙂 **Potential Benefits:** Robotic AI agents may help save people from bodily harm, such as agents that are capable of diffusing bombs, removing poisons, or operating in manufacturing or industrial settings that are hazardous environments for humans.
*   😟 **Risks:** The unpredictable nature of agent actions means that seemingly safe individual operations could combine in potentially harmful ways, creating new risks that are difficult to prevent. (This is similar to [Instrumental Convergence and the paperclip maximizer problem](https://en.wikipedia.org/w/index.php?title=Instrumental_convergence&section=3#Paperclip_maximizer).) It can also be unclear whether an AI agent might design a process that overrides a given guardrail, or if the way a guardrail is specified inadvertently creates further problems. Therefore, the drive to make agents more capable and efficient - through broader system access, more sophisticated action chains, and reduced human oversight - conflicts with safety considerations. Further, access to broad interfaces (for example, GUIs, as discussed in [“Action Surfaces” above](https://huggingface.co/blog/ethics-soc-7#the-spectra-of-ai-agents)) and [humanlike](https://huggingface.co/blog/ethics-soc-7#value-humanlikeness) behavior gives agents the ability to perform actions similar to a human user with their same level of control without setting off any warning systems – such as manipulating or deleting files, impersonating users on social media, or using stored credit card information to make purchases for whatever ads pop up. Still further safety risks emerge from AI agents’ ability to interact with multiple systems and the by-design lack of human oversight for each action they may take. AI agents may collectively create unsafe outcomes.

### [](https://huggingface.co/blog/ethics-soc-7#value-scientific-progress)Value: Scientific Progress

There is currently debate about whether AI agents are a fundamental step forward in AI development at all, or a “rebranding” of technology that we have had for years – deep learning, heuristics, and pipeline systems. Re-introducing the term “agent” as an umbrella term for modern AI systems that share common traits of producing operations with minimal user input is a useful way to succinctly refer to recent AI applications. However, the term carries with it connotations of freedom and agency that suggest a more fundamental change in AI technology has occurred.

All of the listed values in this section are relevant for scientific progress; most of them are provided with details of potential benefits as well as risks.

### [](https://huggingface.co/blog/ethics-soc-7#value-security)Value: Security

*   🙂 **Potential Benefits:** Potential benefits are similar to those for [Privacy](https://huggingface.co/blog/ethics-soc-7#value-privacy).
*   😟 **Risks:** AI agents present serious security challenges due to their handling of often sensitive data (customer and user information) combined with their [safety](https://huggingface.co/blog/ethics-soc-7#value-safety) risks, such as ability to interact with multiple systems and the by-design lack of human oversight for each action they may take. They might share confidential information, even when their goals were set by users acting in good faith. Malicious actors could also potentially hijack or manipulate agents to gain unauthorized access to connected systems, steal sensitive information, or conduct automated attacks at scale. For instance, an agent with access to email systems could be exploited to share confidential data, or an agent integrated with home automation could be compromised to breach physical security.

### [](https://huggingface.co/blog/ethics-soc-7#value-speed)Value: Speed

*   On speed for users:
    *   🙂 **Potential Benefits:** AI agents may help users to get more tasks done more quickly, acting as an additional helping hand for tasks that must be done.
    *   😟 **Risks:** Yet they may also cause more work due to issues in their actions (see [Efficiency](https://huggingface.co/blog/ethics-soc-7#value-efficiency)).
*   On speed of systems:
    *   As with most systems, getting a result quickly can come at the expense of other desirable properties (such as [accuracy](https://huggingface.co/blog/ethics-soc-7#value-accuracy), quality, low cost, etc.). If history sheds light on what will happen next, it may be the case in the future that slower systems will provide better results overall.

### [](https://huggingface.co/blog/ethics-soc-7#value-sustainability)Value: Sustainability

*   🙂 **Potential Benefits:** AI agents may theoretically help address issues relevant to climate change, such as forecasting the growth of wildfires or flooding in urban areas alongside the analysis of traffic patterns, then suggesting optimal routes and methods of transportation in real-time. A future self-driving AI agent may make such routing decisions directly, and could coordinate with other systems for relevant updates.
*   😟 **Risks:** Currently, the machine learning models AI agents are based on bring with them negative environmental impacts, such as carbon emissions ([citation](https://dl.acm.org/doi/pdf/10.1145/3630106.3658542)) and the usage of drinking water ([citation](https://www.theatlantic.com/technology/archive/2024/03/ai-water-climate-microsoft/677602/)). Bigger is not always better ([example](https://huggingface.co/blog/smollm)), and efficient hardware and low-carbon data centers can help reduce this.

### [](https://huggingface.co/blog/ethics-soc-7#value-trust)Value: Trust

*   🙂 **Potential Benefits:** We are not aware of any benefits of AI agents relevant to trust. Systems should be constructed to be worthy of our trust, meaning that they are shown to be [safe](https://huggingface.co/blog/ethics-soc-7#value-safety), [secure](https://huggingface.co/blog/ethics-soc-7#value-security), [reliable](https://huggingface.co/blog/ethics-soc-7#value-consistency), etc.
*   😟 **Risks:** Inappropriate trust leads people to be manipulated, and other risks detailed for [Efficiency](https://huggingface.co/blog/ethics-soc-7#value-efficiency), [Humanlikeness](https://huggingface.co/blog/ethics-soc-7#value-humanlikeness), and [Truthfulness](https://huggingface.co/blog/ethics-soc-7#value-truthfulness). A further risk stems from LLMs’ tendency to create false information (called “hallucinations” or “confabulations”): A system that is right the majority of the time is more likely to be inappropriately trusted when it’s wrong.

### [](https://huggingface.co/blog/ethics-soc-7#value-truthfulness)Value: Truthfulness

*   🙂 **Potential Benefits:** We are not aware of any benefits of AI agents relevant to truthfulness.
*   😟 **Risks:** The deep learning technology AI agents are based off of is well-known to be a source of false information ([citation](https://www.sciencedirect.com/science/article/abs/pii/S1364661324002213%5D)), which can take shape in forms such as as deepfakes or misinformation. AI agents can be used to further entrench such false information, such as by gathering up-to-date information and posting on several platforms. This means that AI agents can be used to provide a false sense of what’s true and what’s false, manipulate people’s beliefs, and widen the impact of non-consensual intimate content. False information propagated by AI agents, personalized for specific people, can also be used to scam them.

[](https://huggingface.co/blog/ethics-soc-7#ai-agents-at-hf)AI Agents at HF
---------------------------------------------------------------------------

At Hugging Face, we have begun introducing the ability for people to build and use AI agents in a number of ways, grounding in values as discussed above. This includes:

*   Our recent release of [smolagents](https://huggingface.co/docs/smolagents/index), which provides tools, tutorials, guided tours, and conceptual guides;
*   The [AI Cookbook](https://huggingface.co/learn/cookbook/index), which contains “recipes” for many kinds of agents:
    *   [Build an agent with tool-calling superpowers 🦸 using Transformers Agents](https://huggingface.co/learn/cookbook/agents)
    *   [Agentic RAG: turbocharge your RAG with query reformulation and self-query! 🚀](https://huggingface.co/learn/cookbook/agent_rag)
    *   [Create a Transformers Agent from any LLM inference provider](https://huggingface.co/learn/cookbook/agent_change_llm)
    *   [Agent for text-to-SQL with automatic error correction](https://huggingface.co/learn/cookbook/agent_text_to_sql)
    *   [Data analyst agent: get your data’s insights in the blink of an eye ✨](https://huggingface.co/learn/cookbook/agent_data_analyst)
    *   [Have several agents collaborate in a multi-agent hierarchy 🤖🤝🤖](https://huggingface.co/learn/cookbook/multiagent_web_assistant)
    *   [Multi-agent RAG System 🤖🤝🤖](https://huggingface.co/spaces/data-agents/jupyter-agent)
*   Our [gradio agent user interface](https://www.gradio.app/main/guides/agents-and-tool-usage), to provide the front-end of agents you build;
*   Our [gradio code-writing agent](https://www.gradio.app/playground), which allows you to try out code ideas in real-time in a coding playground.
*   Jupyter Agent, [an agent to write and execute code inside a Jupyter notebook](https://huggingface.co/spaces/data-agents/jupyter-agent).

[](https://huggingface.co/blog/ethics-soc-7#recommendations--what-comes-next)Recommendations & What Comes Next
--------------------------------------------------------------------------------------------------------------

The current state of the art of AI “agents” point forward in several clear directions:

1.  Rigorous evaluation protocols for agents must be designed. An automated benchmark may be informed by the [different dimensions of AI agents listed above](https://huggingface.co/blog/ethics-soc-7#the-spectra-of-ai-agents). A sociotechnical evaluation may be informed by the [values](https://huggingface.co/blog/ethics-soc-7#risks-benefits-and-uses-a-values-based-analysis).
2.  Effects of AI agents must be better understood. Individual, organizational, economic, and environmental effects of AI agents ought to be tracked and analyzed in order to inform how they should be further developed (or not). This should include analyses of the effects of AI agents on well-being, social cohesion, job opportunity, access to resources, and contributions to climate change.
3.  Ripple effects must be better understood. As agents deployed by one user interact with other agents from other users, and they perform actions based on one another’s outputs, it is currently unclear how their ability to meet the user’s goals will be affected.
4.  Transparency and disclosure must be improved. In order to achieve the positive effects of the values listed above, and minimize their negative effects, it needs to be clear to people when they are talking to an agent and how autonomous it is. Clear disclosure of AI agent interactions requires more than simple notifications – it demands an approach combining technical, design, and psychological considerations. Even when users are explicitly aware they're interacting with an AI agent, they may still experience anthropomorphization or develop unwarranted trust. This challenge calls for transparency mechanisms that operate on multiple levels: clear visual and interface cues that persist throughout interactions, carefully crafted conversation patterns that regularly reinforce the agent's artificial nature, and honest disclosure of the agent's capabilities and limitations in context.
5.  Open source can make a positive difference. The open source movement could serve as a counterbalance to the concentration of AI agent development in the hands of a few powerful organizations. Consistent with the broader discussion on the values of openness, by democratizing access to agent architectures and evaluation protocols, open initiatives can enable broader participation in shaping how these systems are developed and deployed. This collaborative approach not only accelerates scientific progress through collective improvement but also helps establish community-driven standards for [safety](https://huggingface.co/blog/ethics-soc-7#value-safety) and [trust](https://huggingface.co/blog/ethics-soc-7#value-trust). When agent development happens in the open, it becomes harder for any single entity to compromise on relevant and important values like [privacy](https://huggingface.co/blog/ethics-soc-7#value-privacy) and [truthfulness](https://huggingface.co/blog/ethics-soc-7#value-truthfulness) for commercial gain. The transparency inherent in open development also creates natural accountability, as the community can verify agent behavior and ensure that development remains aligned with public interest rather than narrow corporate objectives. This openness is particularly important as agents become more sophisticated and their societal impact grows.
6.  Developers are likely to create more agentic “base models”. This is clearly foreseeable based on current trends and research patterns, not a recommendation we are providing relevant to ethics. Current agent technology utilizes a collection of recent and older techniques in computer science – near-term future research will likely attempt to train agent models as one monolithic general model, a kind of multimodal model++: Trained to perform actions jointly with learning to model text, images, etc.

[](https://huggingface.co/blog/ethics-soc-7#acknowledgements)Acknowledgements
-----------------------------------------------------------------------------

We thank Bruna Trevelin, Orion Penner, and Aymeric Roucher for contributions to this piece.

