# Cutting-edge web scraping techniques at NICAR
- URL: https://simonwillison.net/2025/Mar/8/cutting-edge-web-scraping/
- Added At: 2025-03-09 01:32:25
- [Link To Text](2025-03-09-cutting-edge-web-scraping-techniques-at-nicar_raw.md)

## Summary
**摘要**：
本文是作者在NICAR 2025会议上关于网络数据抓取研讨会的讲义。研讨会主要关注利用LLM（大型语言模型）最新发展实现的、不为人知的抓取技巧。研讨会包含四个部分：构建Git scraper（一个在GitHub Actions中自动记录资源随时间变化的抓取器）、使用浏览器内JavaScript和shot-scraper提取有用信息、使用LLM（通过OpenAI和Google Gemini）从非结构化网站提取结构化数据，以及使用Google AI Studio进行视频抓取。作者为本次研讨会发布了几个新工具，包括git-scraper-template（用于快速搭建Git scrapers的模板存储库）、LLM schemas（为LLM工具添加结构化schema支持）和shot-scraper har（用于将页面存档为HTML Archive文件，但因时间关系从研讨会中删除）。此外，作者还设计了一种有趣的方式来分发API密钥，即使用Claude构建一个网页，通过 passphrase 创建加密消息，然后与用户分享URL和passphrase来解锁加密消息。

**要点总结**：
1.  **Git scraper的构建与应用**：Git scraper是一种自动化抓取工具，它在GitHub Actions中运行，能够记录特定资源随时间的变化。通过Git scraper，用户可以追踪网站内容的更新，并将这些更新以版本控制的方式存储在Git仓库中，方便日后查阅和分析。
2.  **浏览器内JavaScript和shot-scraper的信息提取**：该方法利用浏览器内置的JavaScript引擎，结合shot-scraper工具，直接在网页上提取所需的信息。shot-scraper是一个命令行工具，它可以截取网页的屏幕截图，并提取网页中的文本、链接和其他数据。
3.  **LLM在非结构化数据提取中的应用**：大型语言模型（LLM），如OpenAI和Google Gemini，被用于从非结构化的网站中提取结构化数据。LLM具有强大的自然语言处理能力，可以理解网页上的文本内容，并将其转换为结构化的数据格式，例如JSON或CSV。作者专门为LLM工具添加了结构化schema支持，使得数据提取更加规范和高效。
4.  **视频抓取技术**：利用Google AI Studio进行视频内容的抓取和分析。Google AI Studio提供了一系列人工智能工具，可以用于识别视频中的对象、场景和活动，并将这些信息提取出来。
5.  **API密钥的安全分发**：作者创新地使用Claude构建了一个加密消息的网页，参与者可以通过 passphrase 解锁API密钥。这种方法提高了API密钥分发的安全性，防止了密钥泄露的风险。

