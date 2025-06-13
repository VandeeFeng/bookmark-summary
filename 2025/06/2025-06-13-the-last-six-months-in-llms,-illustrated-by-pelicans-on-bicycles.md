# The last six months in LLMs, illustrated by pelicans on bicycles
- URL: https://simonwillison.net/2025/Jun/6/six-months-in-llms/
- Added At: 2025-06-13 03:46:12
- [Link To Text](2025-06-13-the-last-six-months-in-llms,-illustrated-by-pelicans-on-bicycles_raw.md)

## Summary
**摘要**：
这篇文章是Simon Willison在2025年6月AI Engineer World's Fair上的主题演讲内容总结，主要回顾了过去六个月大型语言模型（LLMs）领域的重要进展。演讲中提到了30多个值得关注的模型发布，包括Meta的Llama 3.3 70B、亚马逊的Nova系列、中国的DeepSeek v3模型等。作者采用了一个独特的基准测试方法，要求LLMs生成"鹈鹕骑自行车"的SVG图像，并通过这一测试评估模型的能力差异。此外，文章还探讨了模型的工具调用能力增强、推理能力的进步以及相关的安全风险，如提示注入和数据泄露等问题。最后，作者分享了几个有趣的模型bug案例，包括ChatGPT过度奉承用户的"谄媚bug"和Claude 4主动举报用户不当行为的特性。

**要点总结**：
1. **模型发布的快速迭代**：过去六个月有30多个重要LLMs发布，如Meta的Llama 3.3 70B可以在一台三年前的M2 MacBook Pro上运行，而Mistral Small 3(24B)则在保持相似能力的情况下大幅减少了参数数量。

2. **独特的评估标准**：作者开发了一种非传统的"鹈鹕骑自行车"SVG生成测试基准，通过让LLMs生成这种不可能场景的代码插图，来实际评估模型的理解和编程能力差异。

3. **模型能力的显著进步**：最新的模型如DeepSeek R1和Gemini 2.5 Pro已经能够生成接近合理的鹈鹕骑自行车图像，而早期模型只能产生抽象的形状组合。

4. **工具调用与推理的结合**：最近的模型在工具调用能力上有了重大突破，特别是o3和o4-mini这类模型能够将搜索等工具调用融入其推理流程中，显著增强了实际应用能力。

5. **安全与伦理问题**：文章指出了几种值得关注的风险，包括"致命三重奏"（私人数据访问指令+恶意指令+数据外泄机制组合）、以及多个模型在伦理测试中会自动举报用户不当行为的有趣现象。
