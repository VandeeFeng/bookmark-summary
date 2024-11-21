---
title: llms.txt—a proposal to provide information to help LLMs use websites
date: 2024-11-21
extra:
  source: https://www.answer.ai/posts/2024-09-03-llmstxt.html?_hsmi=334907283
  original_title: llms.txt—a proposal to provide information to help LLMs use websites
---
## Summary
**摘要**：
我们提议在设计供语言模型阅读的网站上添加`/llms.txt`文件，供语言模型获取相关信息时使用。`llms.txt`文件列出了模型可能想要获取的信息（如链接），帮助构建与网站相关的语言模型提示所需背景信息。`llms.txt`文件可以包含外部和内部链接，链接的内容适用于主题，并适合直接由语言模型摄入。通过`/llms.txt`文件，网站作者可以通过列出最相关并适用于语言模型的上下文内容，为模型提供交互指导。

**要点总结**：
1. **目标与实施**：添加`/llms.txt`文件到网站，旨在改善语言模型以获取特定网站背景信息的过程，通过具备上下文链接的定制文件e提供标准化与结构化的信息源。

2. **受益者与用途**：扩展了网站用途，不仅面向人类读者，同时也针对大型语言模型提供信息，提升如软件开发与文档等场合的效率。

3. **设计原理与改进**：认识到语言模型通常偏好更精简且接近专家阅读内容的信息格式，能够快速处理大量信息，因此强调集纳关键数据的必要性。

4. **示范工具与系统**：举例介绍了允许多用途整合的工具和技术，包括为`llms.txt`文件设计的解析工具及实例，及支持链接版网页内容的通用机制。

5. **实现方法与扩展**：采用自由扩展方式与特定案例说明 `llms.txt`格式，如 `FastHTML` 等项目的示例，系统地展示通过 `.md` 格式的细化结构增强信息查询能力。
## Full Content
Title: /llms.txt—a proposal to provide information to help LLMs use websites – Answer.AI

URL Source: https://www.answer.ai/posts/2024-09-03-llmstxt.html?_hsmi=334907283

Markdown Content:
> _Much of this content is copied from the [llms.txt proposal](https://llmstxt.org/). See that link for more details, examples, and tools for using llms.txt files._

Summary
-------

We propose adding a `/llms.txt` file to websites that are designed for reading by language models, not just humans. `llms.txt` is a file that outlines the information that a model may want to retrieve (with links) when assembling context for LLM prompts relevant to a website. Here’s an [example llms.txt file](https://docs.fastht.ml/llms.txt).

The `llms.txt` file may contain both external and internal links, which are curated to be appropriate for the subject matter, and suitable for direct ingestion by LLMs. The problem this solves is that today, constructing the right context for LLMs based on a website is ambiguous — do you:

1.  Crawl the sitemap and include every page, trying to automatically format into an LLM-friendly form?
2.  Selectively include external links in addition to the sitemap?
3.  For specific domains like software documentation should you also try to include all the source code?

Site authors know best, and can provide a list of content that an LLM should use. We do not prescribe exactly how you should assemble and format the context. We’re only proposing a standard where authors can outline the most pertinent and LLM-friendly context, and tools can later assemble and format that context in a form suitable for the application. `llms.txt` is programmatically parseable.

We also propose making an LLM-friendly version of web pages available at a URL adds an `.md` suffix to the regular address—for instance, here is a [regular HTML docs page](https://docs.fastht.ml/tutorials/by_example.html), along with exact same URL but with [a .md extension](https://docs.fastht.ml/tutorials/by_example.html.md). For an example of how these can work together, here’s [a custom GPT](https://chatgpt.com/g/g-rnbNNmdz6-answers-about-answer-ai) which answers questions about Answer.AI using the information from [Answer.AI’s llms.txt](https://www.answer.ai/llms.txt).

Background
----------

Today websites are not just used to provide information to people, but they are also used to provide information to large language models. For instance, language models are often used to enhance development environments used by coders, with many systems including an option to ingest information about programming libraries and APIs from website documentation.

Providing information for language models is a little different to providing information for humans, although there is plenty of overlap. Language models generally like to have information in a more concise form. This can be more similar to what a human expert would want to read. Language models can ingest a lot of information quickly, so it can be helpful to have a single place where all of the key information can be collated.

[![Image 1: llms.txt logo](https://www.answer.ai/posts/llms-logo.png)](https://www.answer.ai/posts/llms-logo.png "llms.txt logo")

llms.txt logo

We propose that those interested in providing LLM-friendly content add a `/llms.txt` file to their site. This is a markdown file that provides brief background information and guidance, along with links to markdown files (which can also link to external sites) providing more detailed information. This can be used, for instance, in order to provide information necessary for coders to use a library, or as part of research to learn about a person or organization and so forth. You are free to use the `llms.txt` logo on your site to indicate your support if you wish.

llms.txt markdown is human and LLM readable, but is also in a precise format allowing fixed processing methods (i.e. classical programming techniques such as parsers and regex). For instance, there is an [llms-txt](https://www.answer.ai/intro.html) project providing a CLI and Python module for parsing `llms.txt` files and generating LLM context from them. There is also a [sample JavaScript](https://www.answer.ai/llmstxt-js.html) implementation.

We furthermore propose that pages on websites that have information that might be useful for LLMs to read provide a clean markdown version of those pages at the same URL as the original page, but with `.md` appended. (URLs without file names should append `index-commonmark.md` instead.)

The [FastHTML project](https://fastht.ml/) follows these two proposals for its documentation. For instance, here is the [FastHTML docs llms.txt](https://docs.fastht.ml/llms.txt). And here is an example of a [regular HTML docs page](https://docs.fastht.ml/tutorials/by_example.html), along with exact same URL but with [a .md extension](https://docs.fastht.ml/tutorials/by_example.html.md). Note that all [nbdev](https://nbdev.fast.ai/) projects now create .md versions of all pages by default, and all Answer.AI and fast.ai software projects using nbdev have had their docs regenerated with this feature—for instance, see the [markdown version](https://fastcore.fast.ai/docments.html.md) of [fastcore’s docments module](https://fastcore.fast.ai/docments.html).

This proposal does not include any particular recommendation for how to process the file, since it will depend on the application. For example, FastHTML automatically builds a new version of two markdown files including the contents of the linked URLs, using an XML-based structure suitable for use in LLMs such as Claude. The two files are: [llms-ctx.txt](https://docs.fastht.ml/llms-ctx.txt), which does not include the optional URLs, and [llms-ctx-full.txt](https://docs.fastht.ml/llms-ctx-full.txt), which does include them. They are created using the [`llms_txt2ctx`](https://llmstxt.org/intro.html#cli) command line application, and the FastHTML documentation includes information for users about how to use them.

llms.txt files can be used in various scenarios. For software libraries, they can provide a structured overview of documentation, making it easier for LLMs to locate specific features or usage examples. In corporate websites, they can outline organizational structure and key information sources. Information about new legislation and necessary background and context could be curated in an `llms.txt` file to help stakeholders understand it.

llms.txt files can be adapted for various domains. Personal portfolio or CV websites could use them to help answer questions about an individual. In e-commerce, they could outline product categories and policies. Educational institutions might use them to summarize course offerings and resources.

Format
------

At the moment the most widely and easily understood format for language models is Markdown. Simply showing where key Markdown files can be found is a great first step. Providing some basic structure helps a language model to find where the information it needs can come from.

The `llms.txt` file is unusual in that it uses Markdown to structure the information rather than a classic structured format such as XML. The reason for this is that we expect many of these files to be read by language models and agents. Having said that, the information in `llms.txt` follows a specific format and can be read using standard programmatic-based tools.

The `llms.txt` file spec is for files located in the root path `/llms.txt` of a website (or, optionally, in a subpath). A file following the spec contains the following sections as markdown, in the specific order:

*   An H1 with the name of the project or site. This is the only required section
*   A blockquote with a short summary of the project, containing key information necessary for understanding the rest of the file
*   Zero or more markdown sections (e.g. paragraphs, lists, etc) of any type except headings, containing more detailed information about the project and how to interpret the provided files
*   Zero or more markdown sections delimited by H2 headers, containing “file lists” of URLs where further detail is available
    *   Each “file list” is a markdown list, containing a required markdown hyperlink `[name](url)`, then optionally a `:` and notes about the file.

Here is a mock example:

```
# Title

> Optional description goes here

Optional details go here

## Section name

- [Link title](https://link_url): Optional link details

## Optional

- [Link title](https://link_url)
```

Note that the “Optional” section has a special meaning—if it’s included, the URLs provided there can be skipped if a shorter context is needed. Use it for secondary information which can often be skipped.

To create effective `llms.txt` files, consider these guidelines: Use concise, clear language. When linking to resources, include brief, informative descriptions. Avoid ambiguous terms or unexplained jargon. Run a tool that expands your `llms.txt` file into an LLM context file and test a number of language models to see if they can answer questions about your content.

