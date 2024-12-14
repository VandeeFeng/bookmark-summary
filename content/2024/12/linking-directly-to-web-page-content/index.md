---
title: Linking Directly to Web Page Content
date: 2024-12-14
extra:
  source: https://alfy.blog/2024/10/19/linking-directly-to-web-page-content.html
  original_title: Linking Directly to Web Page Content
---
## Summary
**摘要**：
文章讨论了一种下一代的链接技术——文本片段，这是对现有 web 平台的增强，使得可以直接链接到网页中的特定文本内容，而无需添加锚点。文本片段通过在 URL 结尾添加特殊语法实现这一功能，浏览器会根据这部分内容搜索网页上的对应文本，然后滚动到并高亮显示文本。文本片段的语法用于定位特定文本，并允许设定文本前缀、文本起始及结束位置和文本后缀等信息。不同的浏览器对文本片段有不同支持，并有各自特色的高亮表现方式。文章还指出，所有的现代浏览器都支持文本片段功能，只是个别浏览器的扩展功能暂时不完善。文章最后提到了这个功能的优势、未来的应用方向，并感谢了两位专家与开发者对文本片段技术和资源的贡献。

**要点总结**：
1. **功能概述**：文本片段是一种让用户能够精确链接到网页特定文本内容的新型 web 技术。使用/z/特殊格式添加在 URL 结尾，浏览器根据这部分内容搜索页面内的文本并高亮显示。文本片段允许设置文本前缀、开始与结束位置和后缀，用以满足在多匹配文本中定位的需求。
2. **语法结构**：提供的文本片段 URL 结构为 https://example.com/page.html#:~:text=[prefix-,textStart[,textEnd][,-suffix]，其中包括 URL 的 webs 格式化部分、文本分隔符、文本前缀、文本起始与结束、以及文本后缀等元素。可通过替换文本实例来实现特定文本的强化定位。
3. **高亮机制与浏览器兼容性**：文本片段格式通过计算结果来确定文本高亮，并根据不同浏览器特性显示高亮效果。Chrome 是唯一支持直接方法获取可发现内容的浏览器（如元素隐藏或不可见内容），而其他部分浏览器，如 SafariChrome 支持的文本片段特性需要通过原生方法或扩展实现，总之浏览器对于该功能的支持和发展存在差异。
4. **通信与应用**：文章强调文本片段优势，如提升网站导航和综合优化用户体验、减少负载并扩展可用范围至新生成的应用和服务器。同时文章为文本片段技术和资源提供链接，鼓励持续探索与应用这种下一代链接技术。
5. **技术贡献及未来发展**：文章特别感谢了在文本片段技术发展与内容创建中做出的贡献者，包括专攻这一技术的专家与开发者。总体展现了对未来优化和广泛应用持乐观态度设想，期待文本片段技术的技术完善，以实现更广泛深入的链接和扩展网站功能，未来可能向用户友好的界面和功能增强方向发展。
## Full Content
Title: Smarter than 'Ctrl+F': Linking Directly to Web Page Content

URL Source: https://alfy.blog/2024/10/19/linking-directly-to-web-page-content.html

Published Time: 2024-10-19T03:00:00+03:00

Markdown Content:
Historically, we could link to a certain part of the page only if that part had an ID. All we needed to do was to link to the URL and add the _document fragment_ (ID). If we wanted to link to a certain part of the page, we needed to anchor that part to link to it. This was until we were blessed with the **[Text fragments](https://wicg.github.io/scroll-to-text-fragment/)**!

### What are Text fragments?

Text fragments are a powerful feature of the modern web platform that allows for precise linking to specific text within a web page without the need to add an anchor! This feature is complemented by the `::target-text` CSS pseudo-element, which provides a way to style the highlighted text.

Text fragments work by appending a special syntax to the end of a URL; just like we used to append the ID after the hash symbol (`#`). The browser interprets this part of the URL, searches for the specified text on the page, and then scrolls to and highlights that text if it supports text fragments. If the user attempts to navigate the document by pressing tab, the focus will move on to the next focusable element after the text fragment.

### How can we use it?

Here’s the basic syntax for a text fragment URL:

```

https://example.com/page.html#:~:text=[prefix-,]textStart[,textEnd][,-suffix]

```

Following the hash symbol, we add this special syntax `:~:` also known as _fragment directive_ then `text=` followed by:

1.  `prefix-`: A text string preceded by a hyphen specifying what text should immediately precede the linked text. This helps the browser to link to the correct text in case of multiple matches. This part is not highlighted.
2.  `textStart`: The beginning of the text you’re highlighting.
3.  `textEnd`: The ending of the text you’re highlighting.
4.  `-suffix`: A hyphen followed by a text string that behaves similarly to the prefix but comes after the text. Aslo helpful when multiple matches exist and doesn’t get highlighted with the linked text.

For example, the following link:

```

https://developer.mozilla.org/en-US/docs/Web/URI/Fragment/Text_fragments#:~:text=without%20relying%20on%20the%20presence%20of%20IDs

```

This text fragment we are using is “without relying on the presence of IDs” but it’s [encoded](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent). If you follow [this link](https://developer.mozilla.org/en-US/docs/Web/URI/Fragment/Text_fragments#:~:text=without%20relying%20on%20the%20presence%20of%20IDs), it should look like the following:

![Image 14: Screenshot from Google Chrome showing how highlighted text fragment look in Google Chrome](https://alfy.blog/images/2024/02/screenshot-01.png)

We can also highlight a range of text by setting the `startText` and the `endText`. Consider the following example from the same URL:

```

https://developer.mozilla.org/en-US/docs/Web/URI/Fragment/Text_fragments#:~:text=using%20particular,don't%20control

```

The text fragment we are using is “using particular” followed by a comma then “don’t control”. If you follow [this link](https://developer.mozilla.org/en-US/docs/Web/URI/Fragment/Text_fragments#:~:text=using%20particular,don't%20control), it should look like the following:

![Image 15: Screenshot from Google Chrome showing highlighted text fragment with start text and end text](https://alfy.blog/images/2024/02/screenshot-02.png)

We can also highlight multiple texts by using ampersands. Consider the following:

```

https://developer.mozilla.org/en-US/docs/Web/URI/Fragment/Text_fragments#:~:text=using%20particular&text=it%20allows

```

If you follow [this link](https://developer.mozilla.org/en-US/docs/Web/URI/Fragment/Text_fragments#:~:text=using%20particular&text=it%20allows), it should look like the following:

![Image 16: Screenshot from Google Chrome showing different highlighted text fragment](https://alfy.blog/images/2024/02/screenshot-03.png)

One of the interesting behaviors about text fragments, is if you’re linking to hidden content that’s discoverable through _find-in-page_ feature (e.g. children of element with hidden attribute set to `until-found` or content of a closed details element), the hidden content will become visible. Let’s look at this behavior by linking to [this article](https://www.scottohara.me/blog/2022/09/12/details-summary.html) from Scott O’Hara’s blog. The blog contains the details element that is closed by default.

![Image 17: Screenshot from Scott O'Hara's blog showing a details section](https://alfy.blog/images/2024/02/screenshot-04.png)

If we [linked to the text fragment](https://www.scottohara.me/blog/2022/09/12/details-summary.html#:~:text=Oh%20hi%20there.%20Forget%20your%20summary,%20didja) inside the details element, it will open automatically:

```

https://www.scottohara.me/blog/2022/09/12/details-summary.html#:~:text=Oh%20hi%20there.%20Forget%20your%20summary,%20didja

```

![Image 18: Screenshot from Scott O'Hara's blog showing a details section and it opens because it matches the text fragment inside the details section](https://alfy.blog/images/2024/02/screenshot-05.png)

**Note** that this behavior is **only available in Google Chrome** as it’s the only browser to support discoverable content.

### Styling highlighted fragments

If the browser supports text fragments, we can change the style of the highlighted text by using the `::target-text` pseudo-element

```
::target-text {
    background-color: yellow;
}
```

Note that we are only allowed to change the following properties:

*   color
*   background-color
*   text-decoration and its associated properties (including text-underline-position and text-underline-offset)
*   text-shadow
*   stroke-color, fill-color, and stroke-width
*   custom properties

### Browser support and fallback behaviour

Text fragments are currently [supported in all the browsers](https://caniuse.com/mdn-html_elements_a_text_fragments). The pseudo-element `::target-text` is not yet supported is Safari but it’s now available in the Technology Preview version. If this feature is not supported in the browser, it will degrade gracefully and the page will load without highlighting or scrolling to the text.

The default style for the highlight is different based on the browser. The color of the highlight is different across the different browsers. The highlighted area is bigger in Safari spanning the whole line-height. In Firefox and Chrome, only the text is highlighted and the spaces between the lines are empty.

![Image 19: Demonstration of the differences in text highlight between the different browsers](https://alfy.blog/images/2024/02/comparison.png)

We can detect if the feature is supported or not using `document.fragmentDirective`. It will return an empty FragmentDirective object, if supported or will return undefined if it’s not.

### Closing thoughts

My first encounter with text fragments was through links generated by Google Search results. Initially, I assumed it was a Chrome-specific feature and not part of a broader web standard. However, I soon realized that this functionality was actually built upon the open web, available to any browser that chooses to implement it.

I’d love to see this feature used more broadly, particularly by responsible generative AI systems. Imagine AI that can provide direct, context-sensitive links to the exact content you’re interested in, using text fragments for precise references. This would not only increase transparency but also improve the user experience when navigating AI-generated content.

Looking ahead, it would be fantastic if text fragments were more accessible to all users, not just those with technical knowledge. What if browsers offered built-in features that allowed non-technical users to highlight text and generate links to specific paragraphs with ease? This could be through a native browser feature or even a simple browser extension—either way, it would make deep linking a breeze for everyone.

Finally, I’d like to express my sincere thanks to [Hannah Olukoye](https://hannaholukoye.com/) and [Jens Oliver Meiert](https://meiert.com/) for the time they’ve taken to share their invaluable feedback and corrections.

### Update, 20th Oct, 2024

It turns out that the ability to generate a link to a specific piece of text is already built into Chromium-based browsers, as [Hostam Sultan](https://x.com/HosamSultan_) [clarified on X](https://x.com/HosamSultan_/status/1847768998349328553) (formerly Twitter). If you’re using Chrome, simply highlight some text, right-click, and you’ll find the “Copy link to highlight” option in the context menu.

### Additional resources

*   URL Fragment Text Directives - [W3C Draft Community Group Report](https://wicg.github.io/scroll-to-text-fragment/)
*   Text Fragments: [MDN](https://developer.mozilla.org/en-US/docs/Web/URI/Fragment/Text_fragments)
*   Style Highlights: [CSSWG Draft](https://drafts.csswg.org/css-pseudo/#highlight-styling)
*   Support for Text Fragments: [CanIUse](https://caniuse.com/mdn-html_elements_a_text_fragments)

