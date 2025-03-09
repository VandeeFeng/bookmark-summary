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
