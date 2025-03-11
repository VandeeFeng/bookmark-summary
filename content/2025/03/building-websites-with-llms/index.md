---
title: Building Websites With LLMS
date: 2025-03-11
extra:
  source: https://blog.jim-nielsen.com/2025/lots-of-little-html-pages/
  original_title: Building Websites With LLMS
---
## Summary
**摘要**：
作者分享了最近博客更新的设计和开发过程中的一些想法，他开始反思过去构建页面时，依赖JavaScript为现有文档添加交互效果的习惯性做法。随着跨文档视图过渡技术的日益普及，作者发现，相比于构建由JavaScript驱动的、渐进增强的页面内交互，直接构建多个HTML页面并通过链接进行跳转反而更加高效。作者称这种方法为“大量小型HTML页面”。在构建诸如展开式导航菜单、页面内搜索或内容过滤等渐进增强功能时，作者会首先考虑是否能通过链接到一个独立的HTML页面来实现，而不是使用JavaScript注入内容。通过为每个交互创建一个独立的HTML页面，然后利用CSS过渡效果，可以用更少的工作量实现比JavaScript更好的用户体验。作者分享了两个例子，一是使用静态站点生成器为不同标准的帖子列表创建单独的HTML页面，并通过CSS视图过渡实现平滑切换；二是将导航和搜索功能也设计为跳转到新的HTML页面，而不是使用JavaScript动态生成内容。这种方法简化了开发，降低了维护成本，并且充分利用了Web的特性，将页面内的交互视为简单的HTML页面导航，从而避免了过度依赖客户端JavaScript。

**要点总结**：
1.  **反思传统开发模式**：作者重新审视了过去依赖JavaScript构建页面交互的习惯，开始思考是否有更简单的方法。
    *   过去，开发者们习惯于使用JavaScript为现有文档添加交互效果，但作者发现这种方式有时会增加开发的复杂度和维护成本。
2.  **提出“大量小型HTML页面”方法**：作者提出了一种新的开发思路，即使用多个小型HTML页面来实现页面交互，而不是依赖JavaScript。
    *   这种方法的核心思想是将复杂的页面交互拆分成多个简单的HTML页面，并通过链接将它们连接起来。每个页面只负责处理一个特定的交互功能，从而降低了单个页面的复杂性。
3.  **利用CSS视图过渡**：作者强调使用CSS视图过渡来实现页面之间的平滑切换，从而提升用户体验。
    *   CSS视图过渡是一种现代Web技术，它允许开发者在页面切换时创建流畅的动画效果。通过使用CSS视图过渡，作者能够在使用多个HTML页面的同时，保持用户体验的连贯性。
4.  **举例说明**：作者分享了两个具体的例子，包括使用静态站点生成器实现内容过滤和导航功能。
    *   在内容过滤的例子中，作者为不同标准的帖子列表创建了单独的HTML页面，并通过CSS视图过渡实现平滑切换。在导航功能的例子中，作者将导航菜单设计为一个独立的HTML页面，用户点击导航图标后会跳转到该页面。
5.  **强调易于维护和利用Web特性**：作者认为这种方法易于维护，并且能够更好地利用Web的特性。
    *   由于每个HTML页面只负责处理一个特定的交互功能，因此维护起来更加简单。此外，通过将页面交互视为简单的HTML页面导航，作者能够更好地利用Web的特性，避免过度依赖客户端JavaScript。
## Full Content
Title: Building Websites With LLMS

URL Source: https://blog.jim-nielsen.com/2025/lots-of-little-html-pages/

Markdown Content:
And by LLMS I mean: (L)ots of (L)ittle ht(M)l page(S).

I recently shipped some updates to my blog. Through the design/development process, I had some insights which made me question my knee-jerk reaction to building pieces of a page as JS-powered interactions on top of the existing document.

With cross-document view transitions getting broader and broader support, I’m realizing that building in-page, progressively-enhanced interactions is _more_ work than simply building two HTML pages and linking them.

I’m calling this approach “lots of little HTML pages” in my head. As I find myself trying to build progressively-enhanced features with JavaScript — like a fly-out navigation menu, or an on-page search, or filtering content — I stop and ask myself: “Can I build this as a separate HTML page triggered by a link, rather than JavaScript-injected content built from a button?”

I kinda love the results. I build separate, small HTML pages for each “interaction” I want, then I let CSS transitions take over and I get something that feels better than its JS counterpart for way less work.

Allow me two quick examples.

Example 1: Filtering
--------------------

Working on my homepage, I found myself wanting a list of posts filtered by some kind of criteria, like:

*   The most recent posts
*   The ones being trafficked the most
*   The ones that’ve had lots of Hacker News traffic in the past

My first impulse was to have a list of posts you can filter with JavaScript.

But the more I built it, the more complicated it got. Each “list” of posts needed a slightly different set of data. And each one had a different sort order. What I thought was going to be “stick a bunch of `<li>`s in the DOM, and show hide some based on the current filter” turned into lots of `data-x` attributes, per-list sorting logic, etc. I realized quickly this wasn’t a trivial, progressively-enhanced feature. I didn’t want to write a bunch of client-side JavaScript for what would take me seconds to write on “the server” (my static site generator).

Then I thought: Why don’t I just do this with my static site generator? Each filter can be its own, separate HTML page, and with CSS view transitions I’ll get a nice transition effect for free!

Minutes later I had it all working — mostly, [I had to learn a few small things about aspect ratio in transitions](https://blog.jim-nielsen.com/2025/aspect-ratio-in-css-view-transitions/) — plus I had fancy transitions between “tabs” for free!

![Image 1: Animated gif showing a link that goes to a new document and the list re-shuffles and re-sorts its contents in an animated fashion.](https://cdn.jim-nielsen.com/blog/2025/lots-of-small-html-filter-transitions.gif)

This really feels like a game-changer for simple sites. If you can keep your site simple, it’s easier to build traditional, JavaScript-powered on-page interactions as small, linked HTML pages.

Example 2: Navigation
---------------------

This got me thinking: maybe I should do the same thing for my navigation?

Usually I think “Ok, so I’ll have a hamburger icon with a bunch of navigational elements in it, and when it’s clicked you gotta reveal it, etc." And I thought, “What if it’s just a new HTML page?”[\[1\]](https://blog.jim-nielsen.com/2025/lots-of-little-html-pages/#fn:1)

Because I’m using a static site generator, it’s really easy to create a new HTML page. A few minutes later and I had it. No client-side JS required. You navigate to the “Menu” and you get a page of options, with an “x” to simulate closing the menu and going back to where you were.

![Image 2: Anitmated gif of a menu opening on a website (but it’s an entirely new HTML page).](https://cdn.jim-nielsen.com/blog/2025/lots-of-small-html-menu.gif)

I liked it so much for my navigation, I did the same thing with search. Clicking the icon doesn’t use JavaScript to inject new markup and animate things on screen. Nope. It’s just a link to a new page with CSS supporting a cross-document view transition.

![Image 3](https://cdn.jim-nielsen.com/blog/2025/lots-of-small-html-search.gif)

Granted, there are some trade-offs to this approach. But on the whole, I really like it. It was so easy to build and I know it’s going to be incredibly easy to maintain!

I think this is a good example of leveraging the grain of the web. It’s _really_ easy to build a simple website when you can shift your perspective to viewing on-page interactivity as simple HTML page navigations powered by cross document CSS transitions (rather than doing all of that as client-side JS).

