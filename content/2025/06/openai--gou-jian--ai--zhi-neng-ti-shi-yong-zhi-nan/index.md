---
title: OpenAI- 构建 AI 智能体实用指南
date: 2025-06-18
extra:
  source: https://baoyu.io/translations/a-practical-guide-to-building-agents
  original_title: OpenAI- 构建 AI 智能体实用指南
---
## Summary
**摘要**：
OpenAI发布的《构建AI智能体实用指南》深入探讨了AI智能体的定义、构建方法和应用场景。智能体作为一种新兴软件范式，能够独立代表用户完成任务，其核心在于大型语言模型(LLM)驱动的推理能力、工具使用和工作流管理。指南详细介绍了智能体的三大构建基石：模型作为大脑提供推理能力，工具扩展行动边界，指令定义行为准则。文章强调了采取渐进式架构策略的重要性，建议从单一智能体系统起步，再根据需求拓展至多智能体协作模式。同时，安全性和可控性是智能体应用中不可忽视的部分，指南提出了分层防御体系和人工监督机制。最后展望了未来智能体将推动业务转型，形成相互连接的智能体生态系统。

**要点总结**：
1. **AI智能体的本质特征**：智能体与传统软件根本区别在于它们能够接管整个工作流程并自主执行，实现从"辅助执行"到"代理执行"的转变。通过"智能体循环"持续评估状态、调用工具并与目标比对，赋予其处理非确定性场景的能力。

2. **适用场景评估标准**：智能体特别适合三类场景：需要复杂决策制定的工作流、依赖难以维护规则系统的业务，以及涉及非结构化数据处理的任务。这些场景的核心挑战都在于自动化"认知劳动"而非简单程序性任务。

3. **三位一体的构建基础**：
   - 模型选择采用"从高到低"策略，先用最强模型建立基线；
   - 工具设计分为数据检索、动作执行和编排三类，须符合模块化原则；
   - 指令编写需遵循工程化方法，包括任务分解、使用模板和处理边界情况。

4. **安全与可控性机制**：构建分层防御体系包含相关性分类器、安全分类器、PII过滤器等多种防护手段；同时明确定义人工干预触发条件，如高风险操作或低置信度情况，形成完整的安全保障。
## Full Content
Title: OpenAI: 构建 AI 智能体实用指南

URL Source: https://baoyu.io/translations/a-practical-guide-to-building-agents

Markdown Content:
![Image 1](https://baoyu.io/uploads/2025-06-17/1750175444445.png)

第一部分：AI 智能体导论
-------------

### 1.1 重新定义自动化：什么是 AI 智能体？

在探讨构建智能体的具体方法之前，必须首先建立一个清晰、准确的定义。AI 智能体（Agent）代表了一种新兴的软件范式，其核心特征在于能够以高度的独立性代表用户完成任务 1。这标志着与传统软件的根本性区别。传统软件，即便是集成了自动化工作流的系统，其本质上是作为用户的工具，旨在简化和加速由用户主导的操作流程。而智能体则能够接管整个工作流，并自主地执行，从而将自动化从“辅助执行”提升到“代理执行”的层面 3。

一个工作流（Workflow）被定义为实现用户目标所必须执行的一系列步骤，无论目标是解决客户服务问题、预订餐厅，还是生成一份复杂的分析报告 1。智能体的独特之处在于，它利用大型语言模型（LLM）作为其核心的推理和决策引擎，来

_控制工作流的执行_ 2。这使其能够超越简单的、单轮次的问答交互。那些集成 LLM 但未用其控制工作流执行的应用，例如纯粹的聊天机器人、单步翻译工具或情感分类器，并不属于智能体的范畴 1。

一个真正的智能体系统，集成了推理、记忆、工具使用和工作流管理等多种能力 4。它在一个被称为“智能体循环”（Agentic Cycle）或“运行循环”（Run Loop）的模式下运作 1。在此循环中，智能体持续地评估其当前状态和已有信息，判断是否需要通过调用工具来获取更多上下文或执行某个动作，并将其进展与最终目标进行比对 5。这个循环会一直持续，直到满足某个预设的退出条件，例如任务成功完成、发生无法处理的错误、调用了某个特定的终止工具，或达到了最大交互轮次限制 1。

这种架构赋予了智能体处理非确定性场景的卓越能力。在这些场景中，智能体可以：

*   **处理模糊性并做出决策**：在信息不完整或指令不明确的情况下，智能体能够进行推理，并做出合理的判断 3。

*   **动态修正路线**：当执行路径遇到障碍或偏离目标时，智能体能够识别问题并调整其策略 5。

*   **识别任务完成状态**：智能体能够自主判断其行为是否已经达成了用户的最终目标 5。

*   **适时请求人类介入**：在遇到其能力范围之外的难题或高风险决策时，智能体能够主动暂停执行，并将控制权移交给人类操作员 5。

这种从“执行指令”到“实现意图”的转变，是 AI 智能体带来的最深刻的范式革命。它意味着人与软件的交互模式发生了根本性的变化。用户的角色从一个亦步亦趋的“操作者”，转变为一个设定目标、定义边界和处理异常的“监督者”。因此，在智能体系统中，强大的人机协同（Human-in-the-Loop, HITL）机制不仅是一项安全功能，更是这种全新人机交互模型不可或缺的组成部分 4。软件开始拥有“代理权”（Agency），而人类的价值则更多地体现在战略指导、最终决策和对复杂例外的处理上。这对于未来的用户界面设计、企业团队的组织结构，乃至员工的技能要求，都将产生深远的影响。

### 1.2 何时构建智能体：适用场景识别

尽管 AI 智能体功能强大，但并非所有自动化任务都需要或适合采用智能体架构。在投入资源构建之前，至关重要的是对应用场景进行审慎评估，以确认该场景确实需要智能体级别的推理能力。在许多情况下，一个设计良好的传统确定性解决方案可能更为高效和稳健 3。智能体特别适用于那些传统基于规则的自动化方法难以应对或效果不佳的工作流 2。

该指南明确指出了三类最适合应用智能体的典型场景：

1.   **复杂的决策制定 (Complex Decision-Making)**：这类场景需要超越简单规则的、带有细微差别的判断力。例如，在客户支持领域，处理复杂的退款申请。一个传统的规则引擎可能只能基于“购买时间是否超过 30 天”这类硬性标准进行判断。而一个 AI 智能体则能像一位经验丰富的调查员，综合考虑客户的忠诚度、历史投诉记录、产品问题的性质以及对话中的情绪等多种非结构化信息，从而做出更为合理和人性化的决策 3。另一个例子是支付欺诈分析，智能体能够评估上下文，识别微妙的行为模式，发现那些不符合任何预设规则但仍然可疑的交易 3。

2.   **难以维护的规则系统 (Difficult-to-Maintain Rules)**：许多企业的核心业务流程依赖于庞大、复杂且相互交织的规则集。随着业务的发展，这些规则系统变得异常笨重，每一次更新都可能牵一发而动全身，导致成本高昂且极易引入错误 1。例如，对供应商进行安全审查，需要核对数十种合规性文件和政策条款，这些规则会随着法规的变化而频繁更新。使用智能体，可以将这些分散的政策文档作为上下文，让智能体在每次审查时动态地进行理解和应用，而不是硬编码到脆弱的规则引擎中 2。

3.   **非结构化数据处理 (Unstructured Data Processing)**：传统软件在理解和处理电子邮件、对话记录、PDF 文档、图片等非结构化数据方面能力有限 5。而许多关键业务工作流，如保险理赔处理，恰恰严重依赖于对此类数据的解读 2。理赔流程通常需要从事故报告、医疗记录、维修报价单和客户沟通邮件中提取关键信息并进行综合评估。智能体能够利用其强大的自然语言和多模态理解能力，自动完成这些信息的提取、关联和初步判断，从而极大地提升处理效率和准确性 7。

这三类场景的共同点在于，它们的核心挑战都源于自动化“认知劳动”，而不仅仅是“程序性任务”。传统自动化擅长处理基于结构化数据的、逻辑路径明确的“if-then-else”式任务 3。然而，上述场景中的核心工作——无论是退款审批的“权衡”、合规审查的“解读”，还是理赔处理的“综合分析”——都涉及到对上下文的理解、多因素的权衡以及最终的判断，这些都属于认知劳动的范畴。LLM 作为智能体的核心，其设计初衷正是为了处理自然语言和非结构化信息中蕴含的模糊性和复杂性 6。因此，智能体技术精准地切入了传统自动化难以触及的“判断”与“解读”环节。从战略层面看，选择在这些领域部署智能体，不仅仅是对单个工作流的优化，更是对企业最核心、最复杂的运营模式的一次根本性变革。这预示着智能体的实施应被视为一项由业务领导层驱动的战略举措，因为它直接关系到企业的核心业务逻辑和市场竞争力。

第二部分：智能体的构建基石
-------------

构建一个功能强大且稳定可靠的智能体，需要建立在三个紧密协作的核心组件之上。这些组件共同定义了智能体的身份、能力和行为准则 4。

### 2.1 核心组件概述：模型、工具与指令

一个设计精良的智能体由三大基本支柱构成，它们分别是：模型（Model）、工具（Tools）和指令（Instructions）2。

1.   **模型 (Model)**：这是智能体的“大脑”，通常是一个大型语言模型（LLM）。它负责驱动整个工作流，承担着核心的推理、分析、决策和语言生成任务 4。模型的性能直接决定了智能体的“智商”上限。

2.   **工具 (Tools)**：这是智能体的“双手”，使其能够与外部世界进行交互。工具本质上是智能体可以调用的外部函数或 API，用于执行特定的动作或从外部数据源（如数据库、网站、内部系统）获取信息 4。

3.   **指令 (Instructions)**：这是智能体的“行为准则”和“行动指南”。它是一套结构化的、以自然语言编写的提示（Prompts），用于明确定义智能体的目标、角色、行为边界、约束条件以及安全护栏 4。

这种三位一体的架构并非偶然，而是对现代软件工程中“关注点分离”（Separation of Concerns）原则的深刻应用。这一设计思想带来了巨大的工程优势：

*   **将“思考”与“行动”分离**：通过将推理核心（模型）与具体能力（工具）解耦，系统获得了极高的灵活性。开发者可以独立地升级或更换模型（例如，在原型验证后，将昂贵的 GPT-4o 模型更换为更经济、更快速的专用模型），而无需重写与工具交互的逻辑代码 1。

*   **将“能力”与“策略”分离**：通过将工具与指令解耦，系统的可维护性得到极大提升。工具作为标准化的、可复用的能力模块，可以被多个不同的智能体共享 1。而业务逻辑、操作策略和安全约束则被封装在指令中，业务人员或产品经理可以更新指令来调整智能体的行为，而无需触碰底层的代码实现 4。

这种模块化的设计哲学，不仅简化了单个智能体的开发和维护，更为一个可扩展的、协作式的智能体生态系统奠定了基础。可以预见，未来可能会出现一个“智能体组件市场”。在这个市场中，企业可以开发和共享经过严格测试和认证的专用“工具”（如一个标准的 SAP 系统集成工具），而提示工程师则可以设计和销售针对特定行业（如符合 HIPAA 标准的医疗客服智能体）的高度优化的“指令”模板。这种模块化是智能体技术从定制化项目走向规模化应用的关键。

### 2.2 选择驱动核心：模型 (LLM)

模型的选择是智能体构建过程中的一个战略性决策，它直接影响智能体的性能、成本和响应速度。OpenAI 的指南提出了一套有别于传统成本优化思维的、被称为“从高到低”（Start Smart）的模型选择方法论 1。

该方法论的核心思想是：在原型设计和基线测试阶段，应首先使用**当前可用的最强大的模型**（例如 GPT-4o）来构建智能体 2。这样做的目的，是为了建立一个性能基准（Performance Baseline）。通过使用能力最强的模型，可以最大限度地确保智能体能够成功完成任务，从而验证工作流设计、工具定义和指令清晰度的有效性 1。

这种策略看似有悖于常规的成本控制直觉，但在 AI 开发初期却至关重要。在智能体开发中，最大的不确定性并非来自执行效率，而是来自**推理能力**——即“这个复杂的任务是否有可能被自动化？”。如果从一开始就使用一个能力较弱的模型，当智能体执行失败时，开发者将面临一个难以诊断的困境：失败的原因是指令不够清晰，是工具存在缺陷，还是模型本身就不够“聪明”？这个混杂的变量使得问题排查变得异常困难。

反之，通过从最强模型入手，开发者实际上是在测试中消除或最小化了“模型能力不足”这一变量。如果在这种最优配置下智能体仍然失败，那么问题几乎可以肯定地归结为指令或工具的设计缺陷——这是一个更具体、更易于解决的工程问题。这种方法论首先验证了项目的“可行性”，然后再去优化“经济性”，从而有效地为项目早期阶段去风险，避免团队因过早使用能力不足的模型进行测试而错误地放弃一个本有潜力的应用场景。

一旦通过最强模型成功建立了性能基准，并利用评估框架（Evals）量化了其表现，下一步就是进行迭代优化。开发者可以尝试将系统中部分或全部任务替换为更小、更快或成本更低的模型，然后再次运行评估，观察其性能是否仍在可接受的范围内 1。并非所有任务都需要顶级模型的推理能力。一个复杂的智能体系统可能会采用异构模型部署策略：例如，由一个强大的“主管”智能体负责顶层规划和决策，而将一些相对简单的子任务，如意图分类或数据格式化，交由更小、更快的模型来处理 1。这种数据驱动的优化过程，使得团队能够在性能、延迟和成本三者之间找到最佳的平衡点 2。

### 2.3 扩展能力边界：工具 (Tools)

如果说模型是智能体的“大脑”，那么工具就是连接这个大脑与现实世界的“神经系统”和“四肢”。工具赋予了智能体超越其内部知识、与外部环境互动的能力，无论是为了获取决策所需的上下文，还是为了在真实世界中执行动作 5。

为了让智能体能够高效、准确地使用工具，工具本身的设计必须遵循一系列最佳实践。每个工具都应该被视为一个独立的、可复用的软件模块，拥有清晰的文档、详尽的测试和明确的版本管理 1。良好的文档（通常包括工具的名称、功能描述、输入参数和预期输出）对于智能体至关重要，因为它能帮助 LLM 理解在何种情况下、以何种方式调用该工具才是合适的 5。这类似于人类开发者阅读 API 文档的过程，工具描述的质量直接决定了智能体调用工具的准确性和可靠性。因此，“工具定义”本身成为了一门融合了软件开发与提示工程的新兴关键技能。

指南将工具大致分为三种类型，每种类型服务于不同的目的 3：

1.   **数据检索工具 (Data Retrieval Tools)**：这类工具的主要职责是从外部源获取信息，为智能体的决策提供事实依据和上下文。它们是“只读”的，不会改变外部系统的状态。常见的例子包括：查询数据库、读取本地文件（如 PDF 或 CSV）、搜索内部知识库或公共互联网。

2.   **动作执行工具 (Action Execution Tools)**：这类工具用于在外部系统中执行具体操作，通常会改变系统的状态。它们是智能体将决策转化为实际影响的媒介。常见的例子包括：发送电子邮件、在 CRM 系统中创建或更新客户记录、向代码库提交代码、调用下游微服务。

3.   **编排工具 (Orchestration Tools)**：这是一个更高级的概念，即一个智能体本身可以被封装成一个工具，供另一个“上级”智能体调用。这使得构建层级化、模块化的多智能体系统成为可能，是实现复杂工作流拆解和协作的关键。

值得一提的是，对于那些没有提供现代 API 的遗留系统（Legacy Systems），智能体同样有办法与之交互。它可以依赖于“计算机使用模型”（Computer-use Models），这通常指代基于计算机视觉（Computer Vision）或类似于机器人流程自动化（RPA）的技术，让智能体能够像人类一样，通过识别和操作图形用户界面（GUI）来与这些应用程序进行交互 1。

以下表格清晰地展示了这三类工具的定义及示例。

#### 表 1: 智能体工具分类与示例

工具类型 (Tool Type)描述 (Description)示例 (Examples)
**数据检索 (Data Retrieval)**从外部源获取信息以提供上下文，不改变外部系统状态。- query_database(sql_query) - read_pdf(file_path) - search_knowledge_base(query) - get_weather(location)
**动作执行 (Action Execution)**在外部系统中执行操作，可能会改变其状态。- send_email(recipient, subject, body) - update_crm_record(record_id, data) - execute_code(code_block) - book_restaurant(name, time, party_size)
**编排 (Orchestration)**将其他智能体作为可调用工具，用于分派和协调复杂任务。- triage_support_ticket(ticket_details) (调用一个专门的支持分诊智能体) - translate_text_to_multiple_languages(text) (调用多个并行的翻译智能体)

“编排工具”这一概念的提出，预示着软件系统组合方式的深刻变革。它模糊了传统确定性 API 服务与新型非确定性智能体服务之间的界限。在未来，开发者可以构建一个混合工作流，无缝地调用一个简单的数据库查询工具，然后将结果传递给一个专业的分析智能体（它本身也是一个工具），最后再使用另一个工具发送通知邮件。所有这些不同类型的服务都被统一在标准的“工具”接口之下，这将极大地简化复杂系统的构建，是通往真正强大和可扩展的智能系统的关键一步。

### 2.4 定义行为准则：指令 (Instructions)

指令是智能体三大基石中承载业务逻辑和行为策略的部分。高质量的指令对于智能体的成功至关重要，它能够显著减少模糊性，提升决策质量，确保工作流顺畅执行，并有效降低错误率 3。编写指令的过程，应当被视为一项严谨的工程活动，其重要性不亚于编写代码。

为了打造出高效、可靠的指令集，指南推荐了以下几项核心的最佳实践：

1.   **利用现有文档 (Leverage Existing Documentation)**：在许多企业中，规范化的业务流程早已存在于各种文档中，如标准操作程序（SOPs）、客户支持脚本、常见问题解答（FAQs）或内部政策手册。一个高效的起点是将这些经过验证的、人类可读的文档，转化为智能体可以理解和执行的、清晰的、分步骤的指令 1。例如，可以将知识库中的一篇文章，直接改编为处理特定客户问题的一套指令 1。这种方法确保了智能体的行为与企业既有的、成熟的业务流程保持一致。

2.   **明确化与任务分解 (Be Explicit and Break Down Tasks)**：LLM 在处理宏大、模糊的目标时容易产生困惑。因此，必须将复杂的任务分解为一系列更小、更具体、更易于管理的步骤。指令中应使用清晰、无歧义的动词来描述行为。例如，指令“获取订单信息”就远不如“首先，询问用户的订单号”来得明确和可执行 2。此外，指令中应明确告知智能体在特定步骤应该使用哪个工具，这有助于确保确定性的步骤保持确定性，并防止模型在不应使用工具的场合产生幻觉 5。

3.   **使用提示模板 (Use Prompt Templates)**：为了提高指令的可扩展性、可维护性和个性化能力，强烈建议使用带有参数化变量的提示模板 4。例如，可以设计一个通用的客户服务问候语模板：“

您好，您是{{company}}的客户{{name}}，您成为我们的客户已有{{tenure}}。您最常遇到的问题是关于{{categories}}。请问候用户，感谢他们的长期支持，并为他们提供清晰有效的帮助。”在运行时，系统可以将从 CRM 中获取的真实数据（如 company="ABC 科技", name="李明"等）动态注入到模板中，生成高度个性化的指令 7。

4.   **处理边界情况 (Handle Edge Cases)**：一个健壮的系统必须能够妥善处理预期之外的输入和异常情况。指令的设计者需要预见性地识别出已知的边界情况，并为智能体提供清晰的处理指南 3。例如，指令中应包含“如果用户没有提供订单号，应如何礼貌地追问”或“如果查询的商品库存不足，应如何向用户解释并推荐替代品”等 fallback 逻辑 7。

将指令的编写视为“指令即代码”（Instructions as Code）的实践，是走向专业化智能体开发的关键。这意味着，指令文本应与应用程序代码一样，被存储在版本控制系统（如 Git）中，接受同行评审（Peer Review），并拥有一套配套的评估测试集（Evals）。这样做可以确保对指令的任何修改都有迹可循，并且不会意外地导致智能体行为的退化。这一过程也催生了对新型复合型人才的需求——“AI 流程工程师”或“智能体行为设计师”。他们不仅需要深刻理解业务流程，还要具备将其分解为逻辑步骤，并最终用 LLM 能够精确理解的语言进行“编码”的能力。

第三部分：智能体架构与编排
-------------

当单个智能体的能力不足以应对复杂的业务流程时，就需要引入更高层次的架构设计——编排（Orchestration）。编排是指协调一个或多个智能体以完成共同目标的过程。

### 3.1 编排策略：从简单到复杂

在智能体系统架构的设计上，指南给出了一个明确且重要的建议：**采取增量演进的策略** 1。开发者应极力避免在一开始就尝试构建一个拥有复杂架构和完全自主能力的终极多智能体系统。实践证明，从一个简单的单一智能体系统入手，在真实场景中进行验证，然后根据实际需求逐步增加其复杂性，是通往成功的更可靠路径 2。

这种“从简到繁”的策略，其背后有着深刻的技术考量。一个核心原因是为了有效管理智能体的“认知负荷”（Cognitive Load）5。LLM 的上下文窗口和推理能力是有限的。当一个智能体被赋予过多的工具，或者其指令集变得异常复杂时，它在每一步决策时所要面对的“可能性空间”就会急剧膨胀。这会导致智能体更容易产生困惑、行为变得不可预测，甚至出现事实性错误（幻觉）。

通过从一个拥有专注任务和有限工具集的单一智能体开始，开发者可以有效地约束其决策空间，使得智能体的行为更容易被预测、评估和调试 5。只有当业务需求的复杂性确实超出了单个智能体的承载能力，导致其性能下降时，才应该考虑引入更复杂的架构，即多智能体系统。这是一种由性能和需求驱动的、务实的架构设计方法。

总体而言，智能体的编排模式可以分为两大类：单一智能体系统（Single-agent systems）和多智能体系统（Multi-agent systems）1。

### 3.2 单一智能体系统

单一智能体系统是最基础、也是最推荐的起点 2。

其架构非常直观：一个 LLM 模型，配备一套为其任务量身定制的工具和指令集 1。整个系统在一个“运行循环”（Run Loop）中工作。智能体接收用户输入后，开始在这个循环中进行思考和行动：它可能会调用一个工具来获取信息，然后根据返回的信息进行下一步推理，再调用另一个工具来执行动作，如此往复，直到达到某个预设的退出条件，例如成功完成任务或遇到无法解决的错误 1。

这种模式的优势在于其简单性和可管理性。尽管结构简单，但通过不断增加新的工具，单一智能体的能力边界可以被持续扩展，从而应对越来越复杂的任务，而无需过早地引入多智能体编排所带来的额外复杂性 1。对于绝大多数初期的智能体应用场景而言，一个精心设计的单一智能体系统已经足够强大。

从软件架构的角度看，一个处于运行循环中的单一智能体，其行为模式非常类似于一个“有状态的微服务”（Stateful Microservice）。传统的无状态 API 在完成一次请求 - 响应后便会“忘记”所有上下文。而单一智能体则在其“运行实例”（Run）的生命周期内，持续维护着一个状态，这个状态包含了对话历史、之前的工具调用记录以及中间的思考过程 1。这个“运行实例”可以被看作一个需要被管理、监控和在必要时持久化的长时会话或事务。理解其“有状态”的本质，有助于开发者更好地将其集成到现有的、更广泛的软件生态系统中。

### 3.3 多智能体系统

当工作流的复杂性超出了单个智能体的“认知负荷”时——例如，任务需要截然不同的专业知识领域，或者需要管理的工具数量过多——就应转向多智能体系统 5。

多智能体系统的核心优势在于实现了更高层次的“关注点分离”。通过将一个庞大而复杂的任务分解给多个更小、更专注的智能体，每个智能体都只需要关心自己负责的领域。这使得单个智能体更容易被开发、验证、测试和优化 5。同时，这些高度模块化的智能体也更易于被组合，以支持更动态、更灵活的工作流。

指南重点介绍了两种主流的多智能体编排模式 4：

1.   **主管模式 (Manager Pattern)**：这是一种层级化的、中心化的编排模式。系统中存在一个“主管”（Manager）或“编排者”（Orchestrator）智能体，它负责理解任务的总体目标，并将其分解为多个子任务。然后，它像一个项目经理一样，将这些子任务“委派”给多个专门的“下属”（Worker）智能体去执行。这些下属智能体对于主管来说，就是其可以调用的“工具”4。主管会调用下属智能体，等待它们返回结果，最后将所有结果综合起来，形成最终的解决方案 5。一个典型的例子是：一个“旅行规划主管”智能体，接收到“预订去夏威夷的家庭旅行”的指令后，会分别调用一个“机票预订”智能体和一个“酒店预订”智能体，在收到它们各自的预订成功确认后，再将完整的行程单返回给用户。

2.   **去中心化模式 (Decentralized Pattern)**：这是一种点对点的、分布式的编排模式。系统中没有一个中心化的主管。取而代之的是，一群对等（Peer）的智能体，它们各自拥有独特的专长，并且“知道”彼此的存在和能力 4。在这种模式下，工作流的控制权可以在智能体之间进行“传递”或“交接”。当一个智能体判断当前任务的后续步骤超出了自己的能力范围，但正好是另一个智能体的专长时，它就会将整个工作流的控制权以及所有必要的上下文信息，移交给那个更合适的智能体，然后自己则终止运行 5。一个经典的例子是：一个“客户接待”智能体负责初步 triage。当它判断出用户的请求是一个复杂的技术支持问题时，它就会将整个对话无缝地移交给一个“技术支持”智能体来继续处理。

这两种编排模式实际上是现实世界中人类组织结构的镜像。**主管模式**类似于一个经典的项目团队：项目经理（主管智能体）不亲自编写代码或进行设计，而是协调和集成不同专家（下属智能体）的工作成果。这种模式非常适合那些可以被并行处理，或需要综合多种不同信息才能完成的任务。而**去中心化模式**则更像一条工厂的流水线，或者企业内部的部门间工作交接流程：销售部门（接待智能体）完成客户资格审查后，将整个案子完整地移交给实施部门（专家智能体）。这种模式最适合那些线性的、由不同阶段的专家序贯处理的流程。

因此，在两种模式之间做出选择，并不仅仅是一个技术决策，更是一个业务流程的设计决策。工程师需要与业务分析师紧密合作，精确地描绘出他们试图自动化的真实世界流程。选择错误的编排模式，可能会导致智能体之间通信效率低下、出现流程瓶颈，或者最终无法有效地解决用户的根本问题。

第四部分：确保安全、可靠与可控
---------------

在将 AI 智能体部署到生产环境时，安全性、可靠性和可控性是不可妥协的基石。一个无法被信任的智能体，无论其功能多么强大，都是没有商业价值的。

### 4.1 安全护栏：构建分层防御体系

智能体的安全设计绝不能是事后添加的补丁，而必须是贯穿于设计、开发和部署全过程的核心考量。指南强调，应采用一种“分层防御”（Layered Defense）或“深度防御”（Defense in Depth）的策略来系统性地管理风险 2。

这一理念源自成熟的网络安全实践。在网络安全领域，单一的防御措施（如一道防火墙）被认为是脆弱的。一个健壮的系统会部署多层、多样化的防护，如防火墙、入侵检测系统、访问控制、数据加密等，形成一个纵深防御体系。同样，对于 AI 智能体，也不能仅仅依赖于一条简单的提示指令（如“请做一个有益无害的助手”）。

一个分层的防御体系意味着，即使某一层防护被绕过或失效，后续的层面仍有机会捕获和阻止风险。例如，系统可以部署多重独立的检查机制：首先，一个基于 LLM 的相关性分类器可以过滤掉与任务无关的恶意输入；接着，一个基于规则的过滤器可以拦截掉包含特定敏感词或格式（如信用卡号）的内容；然后，在调用工具前，系统会评估该工具的风险等级，对于高风险操作要求额外授权；最后，在智能体生成最终响应后，一个输出验证模块会检查其内容是否符合品牌语调和合规要求 3。

这种设计哲学承认任何单一的安全机制都可能存在漏洞，并通过冗余和多样化的检查来弥补这一不足。此外，安全护栏的构建也应是一个迭代的过程。开发者应从一些已知的、通用的风险（如数据隐私和品牌声誉风险）入手，建立起基础的防护层。然后，在持续的测试和实际运行中，一旦发现新的漏洞或攻击模式，就应立即设计并增加新的、更具针对性的护栏 3。

### 4.2 护栏的类型与实现

一个全面的分层防御体系通常由多种不同类型和机制的护栏组合而成。以下是该指南中提到的几种关键护栏类型及其实现方式 4：

*   **相关性分类器 (Relevance Classifiers)**：确保智能体的行为和响应始终保持在其预设的功能范围和主题之内，防止其被引导去执行无关或恶意的任务。

*   **安全分类器 (Safety Classifiers)**：用于检测和拦截有害、不安全、不道德或违反使用政策的输入和输出。这通常可以通过调用专门的安全模型（如 OpenAI 的 Moderation API）来实现。

*   **PII 过滤器 (PII Filters)**：防止个人身份信息（Personally Identifiable Information）在交互过程中被无意中泄露或记录。简单的实现可以基于正则表达式（Regex）来匹配常见的 PII 格式（如电子邮件地址、电话号码），而更高级的实现则可以利用专门的 LLM 或命名实体识别（NER）模型进行更精准的检测。

*   **基于规则的过滤器 (Rules-Based Filters)**：虽然简单，但非常有效。可以通过设置关键词黑名单（如禁止“删除所有数据”）、限制输入长度或使用正则表达式来拦截许多已知的攻击模式。

*   **工具风险评估 (Tool Risk Assessment)**：并非所有工具的风险等级都相同。系统应为每个工具分配一个风险评级（如：低、中、高）。对于调用高风险工具（如 issue_large_refund 或 delete_database_record）的请求，系统可以自动进行门控，要求必须得到人类操作员的审查和批准后才能执行。

*   **输出验证 (Output Validation)**：在将智能体的最终响应呈现给用户之前，进行最后一道检查。这可以确保输出的格式正确（例如，是合法的 JSON），并且内容符合企业的品牌语调、风格指南和法律合规要求。

*   **审计 (Auditing)**：详细记录智能体的所有行为，包括其内部思考过程、工具调用历史和最终输出。这些日志对于事后的问题排查、安全事件分析和系统持续改进至关重要。

下表对这些关键的护栏机制进行了更详细的梳理。

#### 表 2: 安全护栏机制详解

护栏类型 (Guardrail Type)目的 (Purpose)实现方法 (Implementation Method)
**相关性分类器 (Relevance Classifier)**确保智能体的交互保持在预定的话题和功能范围内。- 使用一个独立的、经过微调的 LLM 来对用户输入或智能体草稿响应进行分类。 - 基于关键词或主题模型进行简单分类。
**安全分类器 (Safety Classifier)**检测和阻止不安全、不道德或违反政策的内容。- 调用 OpenAI Moderation API。 - 使用内部训练的内容安全分类模型。
**PII 过滤器 (PII Filter)**防止个人身份信息（如姓名、电话、地址）被处理或泄露。- 使用基于正则表达式（Regex）的规则来识别常见格式。 - 使用专门的 LLM 或 NER（命名实体识别）模型进行更精确的检测和脱敏。
**工具风险评估 (Tool Risk Assessment)**在执行高风险操作前进行门控或寻求批准。- 为每个工具在定义时附加风险等级元数据（如：risk_level='high'）。 - 在智能体运行时，检查待调用工具的风险等级，并根据预设策略触发相应流程（如人工审批）。
**输出验证 (Output Validation)**确保最终输出符合格式、品牌语调和合规性要求。- 使用 Pydantic 等库来验证结构化输出的模式。 - 使用另一个 LLM 来评估响应的语调、风格是否符合品牌指南。

从一个更宏观的视角看，这套复杂的护栏体系可以被视为一个为智能体量身打造的“免疫系统”。基于规则的过滤器就像是生物体的皮肤，提供了第一道简单而广泛的物理屏障。LLM 驱动的分类器则像是先天免疫系统，能够更智能地识别和应对各种威胁模式。而最终的人工干预机制，则扮演了适应性免疫系统的角色——一种高度智能的响应，专门用于处理那些自动化系统无法应对的新型或高风险威胁。这一比喻揭示了智能体安全是一个动态、演进的挑战，它需要的不是一套一成不变的静态规则，而是一个能够持续监控、响应和适应（通过根据过往的失败案例添加新护栏）的、有生命力的运营体系。这预示着“AI 安全运营”（AISecOps）将成为企业中一个至关重要的新职能。

### 4.3 人工监督与干预机制

即使拥有最完善的自动化护栏，也必须承认，当前的 AI 智能体并非完美无缺。它们仍然可能在面对前所未见的模糊情境时感到困惑，或者在需要执行高风险、不可逆的操作时带来隐患。因此，在系统中规划并内置清晰的人工监督与干预机制（Human-in-the-Loop, HITL）是部署生产级智能体的一项基本要求，在早期部署阶段尤其如此 4。

HITL 不仅仅是一个用于处理失败的“降级方案”，它更是一个建立组织内部和外部用户信任的核心机制。直接将关键业务流程完全交由一个全新的自主系统来处理，对于大多数企业而言，是一个难以接受的高风险决策。通过引入 HITL，智能体在初期可以扮演一个强大的“超级助理”角色：它负责完成决策前的所有信息收集、分析和准备工作，然后将一个准备就绪的行动方案提交给人类进行最终的审查和批准。

这种模式使得企业可以在一个安全、可控的环境中，验证智能体的推理逻辑和执行效果。随着时间的推移，当智能体的表现被反复证明是可靠和值得信赖的之后，企业便可以逐步提高其自主权，例如，将需要人工审批的退款金额上限从 100 元提升到 500 元。这种渐进式的信任建立和授权过程，是推动智能体在风险厌恶型环境中成功落地的关键策略 3。

为了使 HITL 机制能够有效运作，系统需要定义明确的、可自动触发人类介入的**升级触发器**（Escalation Triggers）。指南建议了以下几种常见的触发条件 4：

1.   **失败阈值 (Failure Thresholds)**：当智能体在执行任务时，连续多次出现同样的错误，例如反复错误地调用同一个工具，或者多次无法正确理解用户的意图时，系统应自动暂停智能体的运行，并将当前情境升级给人类操作员。这可以防止智能体陷入无效的循环，浪费资源并导致糟糕的用户体验。

2.   **高风险操作 (High-Stakes Operations)**：对于那些具有重大影响、不可逆转或涉及敏感数据的操作，应默认需要人工批准。例如，任何涉及大额退款、删除生产数据、修改客户核心财务信息或访问高度机密文档的请求，都应自动路由到人工审核队列。

3.   **低置信度或不确定性 (Low Confidence or Ambiguity)**：可以对智能体进行专门的指令训练，使其能够识别自己感到“不确定”的状态。当智能体评估认为自己对当前情况的理解不足，或者其决策的置信度低于某个预设阈值时，它应该主动地向用户或内部操作员请求帮助，而不是冒险做出可能错误的猜测。

第五部分：结论与展望
----------

### 5.1 总结：构建生产级智能体的关键要素

本指南系统性地阐述了构建可靠、可控且能在生产环境中创造价值的 AI 智能体所涉及的核心原则和实践方法。其核心思想可以归结为一套相互关联、缺一不可的综合性方法论。

成功的智能体构建，并非源于某项单一技术的突破，而是建立在一个稳固的、由多个要素构成的基础之上。这包括：

*   **一个强大的技术基石**：由三驾马车共同驱动——一个能力足够强大的**模型**作为推理核心，一套定义清晰、功能完备的**工具**作为其与世界交互的桥梁，以及一套明确、无歧义的**指令**作为其行为的根本大法 3。

*   **一种明智的架构演进路径**：遵循从**单一智能体**到**多智能体**的渐进式发展策略。始终从最简单的可行方案入手，在真实的用户反馈和业务需求驱动下，审慎地增加系统的复杂性，并通过合理的**编排模式**（如主管模式或去中心化模式）来管理这种复杂性 2。

*   **一套不可或缺的保障体系**：将安全与信任置于设计的中心，通过构建**分层的安全护栏**来抵御已知和未知的风险，并设计清晰的**人工监督与干预机制**，确保在关键时刻人类始终拥有最终的控制权 3。

贯穿所有这些要素的 overarching theme，是一条**迭代式开发**的黄金法则：从小处着手，快速验证，用真实用户和真实数据来检验智能体的价值和表现，然后在此基础上稳步地扩展其能力边界和自主程度 3。

这套方法论并非一份零散的“技巧清单”，而是一个逻辑严密、内在统一的开发哲学。三大基石（模型、工具、指令）定义了智能体的“**是什么**”（What）。编排模式（单一、主管、去中心化）定义了智能体系统的“**怎么做**”（How）。而保障体系（护栏、HITL）则定义了智能体行为的“**不能做什么**”（Constraints）。这三个维度相互交织、深度关联：工具集的复杂性会影响指令的编写难度；高风险工具的存在决定了必须部署何种类型的护栏；而选择不同的编排模式，则会对智能体间的通信和责任划分提出截然不同的要求。一个成功的智能体系统，正是在这三个维度之间取得了精妙和谐的平衡。

### 5.2 未来展望：智能体驱动的业务转型

AI 智能体标志着一个自动化新纪元的开启。它们的能力已经超越了简单的任务执行，开始深入到业务流程的核心，通过其独特的推理能力来处理模糊性，并以高度的自主性执行横跨多个系统的复杂、多步骤工作流 3。

展望未来，随着智能体技术的不断成熟和成本的进一步降低，行业焦点将逐渐从构建用于解决离散工作流的“孤立智能体”，转向创建由众多专业智能体组成的、相互连接的“智能体生态系统”。我们可以预见，未来可能会出现一个“供应链管理智能体集群”，或者一个“客户全生命周期管理智能体网络”。在这个生态系统中，不同的智能体各司其职——有的负责市场数据分析，有的负责潜在客户沟通，有的负责订单处理，有的负责售后支持——它们协同工作，共同管理和优化整个业务职能。

本指南中所阐述的各项原则——模块化的组件设计、标准化的工具接口、清晰的编排模式以及健壮的安全框架——正是构建这个宏伟蓝图所必需的“语法规则”。它们为我们迎接一个由互联、智能的系统所驱动的未来，奠定了坚实的基础。

#### Works cited

1.   A practical guide to building agents - OpenAI, accessed June 17, 2025, [https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)

2.   How to Build AI Agents: A Detailed, Practical Guide from OpenAI, accessed June 17, 2025, [https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/](https://www.maginative.com/article/how-to-build-ai-agents-a-detailed-practical-guide-from-openai/)

3.   OpenAI Releases Practical Guide to Building Intelligent Agents (with Resources) - AIbase, accessed June 17, 2025, [https://www.aibase.com/news/17299](https://www.aibase.com/news/17299)

4.   OpenAI Releases a Practical Guide to Building LLM Agents for Real ..., accessed June 17, 2025, [https://www.marktechpost.com/2025/04/17/openai-releases-a-practical-guide-to-building-llm-agents-for-real-world-applications/](https://www.marktechpost.com/2025/04/17/openai-releases-a-practical-guide-to-building-llm-agents-for-real-world-applications/)

5.   OpenAI's Agent building guide - summary - DEV Community, accessed June 17, 2025, [https://dev.to/ivor/openais-agent-building-guide-summary-56jg](https://dev.to/ivor/openais-agent-building-guide-summary-56jg)

6.   OpenAI Releases Practical Guide to Building LLM Agents for Real ..., accessed June 17, 2025, [https://babl.ai/openai-releases-practical-guide-to-building-llm-agents-for-real-world-workflows/](https://babl.ai/openai-releases-practical-guide-to-building-llm-agents-for-real-world-workflows/)

7.   OpenAI's Practical Guide to Building AI Agents · AI Automation Society - Skool, accessed June 17, 2025, [https://www.skool.com/ai-automation-society/openais-practical-guide-to-building-ai-agents](https://www.skool.com/ai-automation-society/openais-practical-guide-to-building-ai-agents)

8.   A Distilled version of the "A Practical Guide To Building Agents" : r/ChatGPTPro - Reddit, accessed June 17, 2025, [https://www.reddit.com/r/ChatGPTPro/comments/1k33txk/a_distilled_version_of_the_a_practical_guide_to/](https://www.reddit.com/r/ChatGPTPro/comments/1k33txk/a_distilled_version_of_the_a_practical_guide_to/)

