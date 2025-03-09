---
title: Cutting-edge web scraping techniques at NICAR
date: 2025-03-09
extra:
  source: https://simonwillison.net/2025/Mar/8/cutting-edge-web-scraping/
  original_title: Cutting-edge web scraping techniques at NICAR
---
## Summary
**摘要**：
本文是作者在NICAR 2025会议上关于网络数据抓取研讨会的讲义。研讨会主要关注利用LLM（大型语言模型）最新发展实现的、不为人知的抓取技巧。研讨会包含四个部分：构建Git scraper（一个在GitHub Actions中自动记录资源随时间变化的抓取器）、使用浏览器内JavaScript和shot-scraper提取有用信息、使用LLM（通过OpenAI和Google Gemini）从非结构化网站提取结构化数据，以及使用Google AI Studio进行视频抓取。作者为本次研讨会发布了几个新工具，包括git-scraper-template（用于快速搭建Git scrapers的模板存储库）、LLM schemas（为LLM工具添加结构化schema支持）和shot-scraper har（用于将页面存档为HTML Archive文件，但因时间关系从研讨会中删除）。此外，作者还设计了一种有趣的方式来分发API密钥，即使用Claude构建一个网页，通过 passphrase 创建加密消息，然后与用户分享URL和passphrase来解锁加密消息。

**要点总结**：
1.  **Git scraper的构建与应用**：Git scraper是一种自动化抓取工具，它在GitHub Actions中运行，能够记录特定资源随时间的变化。通过Git scraper，用户可以追踪网站内容的更新，并将这些更新以版本控制的方式存储在Git仓库中，方便日后查阅和分析。
2.  **浏览器内JavaScript和shot-scraper的信息提取**：该方法利用浏览器内置的JavaScript引擎，结合shot-scraper工具，直接在网页上提取所需的信息。shot-scraper是一个命令行工具，它可以截取网页的屏幕截图，并提取网页中的文本、链接和其他数据。
3.  **LLM在非结构化数据提取中的应用**：大型语言模型（LLM），如OpenAI和Google Gemini，被用于从非结构化的网站中提取结构化数据。LLM具有强大的自然语言处理能力，可以理解网页上的文本内容，并将其转换为结构化的数据格式，例如JSON或CSV。作者专门为LLM工具添加了结构化schema支持，使得数据提取更加规范和高效。
4.  **视频抓取技术**：利用Google AI Studio进行视频内容的抓取和分析。Google AI Studio提供了一系列人工智能工具，可以用于识别视频中的对象、场景和活动，并将这些信息提取出来。
5.  **API密钥的安全分发**：作者创新地使用Claude构建了一个加密消息的网页，参与者可以通过 passphrase 解锁API密钥。这种方法提高了API密钥分发的安全性，防止了密钥泄露的风险。

## Full Content
Title: Cutting-edge web scraping techniques at NICAR

URL Source: https://simonwillison.net/2025/Mar/8/cutting-edge-web-scraping/

Markdown Content:
**[Cutting-edge web scraping techniques at NICAR](https://github.com/simonw/nicar-2025-scraping/blob/main/README.md)**. Here's the handout for a workshop I presented this morning at [NICAR 2025](https://www.ire.org/training/conferences/nicar-2025/) on web scraping, focusing on lesser know tips and tricks that became possible only with recent developments in LLMs.

For workshops like this I like to work off an extremely detailed handout, so that people can move at their own pace or catch up later if they didn't get everything done.

The workshop consisted of four parts:

> 1.  Building a [Git scraper](https://simonwillison.net/2020/Oct/9/git-scraping/) - an automated scraper in GitHub Actions that records changes to a resource over time
> 2.  Using in-browser JavaScript and then [shot-scraper](https://shot-scraper.datasette.io/) to extract useful information
> 3.  Using [LLM](https://llm.datasette.io/) with both OpenAI and Google Gemini to extract structured data from unstructured websites
> 4.  [Video scraping](https://simonwillison.net/2024/Oct/17/video-scraping/) using [Google AI Studio](https://aistudio.google.com/)

I released several new tools in preparation for this workshop (I call this "NICAR Driven Development"):

*   [git-scraper-template](https://github.com/simonw/git-scraper-template) template repository for quickly setting up new Git scrapers, which I [wrote about here](https://simonwillison.net/2025/Feb/26/git-scraper-template/)
*   [LLM schemas](https://simonwillison.net/2025/Feb/28/llm-schemas/), finally adding structured schema support to my LLM tool
*   [shot-scraper har](https://shot-scraper.datasette.io/en/stable/har.html) for archiving pages as HTML Archive files - though I cut this from the workshop for time

I also came up with a fun way to distribute API keys for workshop participants: I [had Claude build me](https://claude.ai/share/8d3330c8-7fd4-46d1-93d4-a3bd05915793) a web page where I can create an encrypted message with a passphrase, then share a URL to that page with users and give them the passphrase to unlock the encrypted message. You can try that at [tools.simonwillison.net/encrypt](https://tools.simonwillison.net/encrypt) - or [use this link](https://tools.simonwillison.net/encrypt#5ZeXCdZ5pqCcHqE1y0aGtoIijlUW+ipN4gjQV4A2/6jQNovxnDvO6yoohgxBIVWWCN8m6ppAdjKR41Qzyq8Keh0RP7E=) and enter the passphrase "demo":

![Image 1: Screenshot of a message encryption/decryption web interface showing the title "Encrypt / decrypt message" with two tab options: "Encrypt a message" and "Decrypt a message" (highlighted). Below shows a decryption form with text "This page contains an encrypted message", a passphrase input field with dots, a blue "Decrypt message" button, and a revealed message saying "This is a secret message".](https://static.simonwillison.net/static/2025/encrypt-decrypt.jpg)

