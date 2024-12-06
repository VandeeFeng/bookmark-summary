---
title: Redirecting URLs with CloudFlare
date: 2024-12-06
extra:
  source: https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/
  original_title: Redirecting URLs with CloudFlare
---
## Summary
**摘要**：
Christian Kjær迁移了博客，并在CloudFlare门户解决旧链接造成的问题。他采用CloudFlare的“重定向规则”将旧博客的链接重定向至新地址，避免了为每个帖子编写重写规则。Key steps 包括：
1. 将基域名从`codetalk.io`更改到`codethoughts.io`。
2. 在`/posts/`路径下托管所有帖子。
3. 告别旧版HTML链接结束符。
4. 在CloudFlare的“重定向规则”中创建规则，首先捕获请求，接着重新导向至新位置。
5. 使用`Dynamic`规则重定向，利用`lower()`、`substring()`和`concat()`函数对路径进行修正以适配新格式。

**要点总结**：
1. **切换环境**：详细阐述博客迁移到新域名codethoughts.io及调整路径结构（移除HTML扩展名）的过程。
2. **云防火墙整合**：重点介绍在云防火墙Dashboard中创建重定向规则的步骤，并利用特定路径表达式（`/posts/`）选择性捕获请求。
3. **实现重定向**：以具体表达式`concat("https://codethoughts.io", substring(lower(http.request.uri.path), 0,-5))`实现动态重定向，对路径进行Lowercase化和调整，简化URL结构。
4. **基于免费计划**：说明项目运行在免费计划下，利用可适用规则进行构建，说明避免使用复杂规则如正则表达式的原因。
5. **测试与反馈**：建议用户通过Medium或者评论区与作者互动，从而测试和制定改进方案。
## Full Content
Title: Redirecting URLs with CloudFlare

URL Source: https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/

Markdown Content:
![Image 9: Christian Kjær in a casual setting :)](https://codethoughts.io/images/me-casual.jpg)

Christian Kjær

3 min read

·

31\. July 2024

·

[cloudflare](https://codethoughts.io/tags/cloudflare/)

I recently moved my blog from [https://codetalk.io](https://codetalk.io/) (now my commercial site) to [https://codethoughts.io](https://codethoughts.io/). This of course also meant, that everything linking to my old blog was now broken, which is not the best experience for any readers that I might have 😅

Initially I considered setting up rewrite rules somewhere for each individual post, but then thought of a much smarter way, using CloudFlare’s _Redirect Rules_, to instead redirect all direct links to posts and throw them to the new location on codethoughts.io.

The documentation for these rules are a bit sparse, so I thought I’d share how I did. First though, let’s set some context:

*   The base domain changed from [https://codetalk.io](https://codetalk.io/) —\> [https://codethoughts.io](https://codethoughts.io/)
*   All posts live under the `/posts/` path on the domain
*   All post slugs are identical in dates and names
*   We no longer have a `.html` ending on the new blog (i.e. what previously might have been `https://codetalk.io/posts/a-blog-post.html` would now be `https://codetalk.io/posts/a-blog-post/`)
*   We’re on the free CloudFlare plan, so there’s a limit to which expressions we can use

Let’s take a look at how we do this:

*   [Catching our requests on codetalk.io](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/#catching-our-requests-on-codetalk-io)
*   [Redirecting to the new location](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/#redirecting-to-the-new-location)

[Catching our requests on codetalk.io](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/#catching-our-requests-on-codetalk-io)
-------------------------------------------------------------------------------------------------------------------------------------------------------

First, we’ll navigate to the relevant place in CloudFlare

*   Go into the CloudFlare dashboard
*   Select your domain (e.g. codetalk.io)
*   Expand Rules in the sidebar
*   Select Redirect Rules
*   Create a new rule
*   Give it an appropriate name, and make sure to select _Custom filter expression._

In my case here, I specifically want to limit the logic to when the `URI Path` starts with the value `/posts`. CloudFlare will neatly demonstrate that this rule will generate the expression:

```
(starts_with(http.request.uri.path, "/posts"))
```

In the Dashboard console it will look something like this:

[![Image 10: The Redirect Rules entry for catching incoming requests](https://codethoughts.io/processed_images/Screenshot_2024-07-08_at_16.18.43.543fca2cd79242e5.png)](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/Screenshot_2024-07-08_at_16.18.43.png)

The Redirect Rules entry for catching incoming requests

The Redirect Rules entry for catching incoming requests

[Redirecting to the new location](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/#redirecting-to-the-new-location)
---------------------------------------------------------------------------------------------------------------------------------------------

Now that we have caught the relevant incoming requests, let’s transform the old format into our new format.

We want to do a dynamic redirect to the new location, in the new format which is lowercase and without any `.html` at the end.

Let’s set up a redirect rule of type `Dynamic`, give it a status code of HTTP 301 (i.e. "Moved Permanently”) and use the following expression:

```
concat("https://codethoughts.io", substring(lower(http.request.uri.path), 0,-5))
```

Breaking this down from inner-to-outer, what we are doing:

*   Grab the `http.request.uri.path` part of the request (e.g. `/posts/a-blog-post.html` of `https://codetalk.io/posts/a-blog-post.html`)
*   Lowercase the value (e.g. `/posts/A-Blog-Post.html` becomes `/posts/a-blog-post.html`)
*   Remove the last 5 characters by taking the `substring` from the start, `0`, to 5 characters back from the last character, `-5` (e.g. `/posts/a-blog-post.html` becomes `/posts/a-blog-post`)
*   Finally, concatenate our new and rewritten URI path together with the new domain using `concat` (e.g. `/posts/a-blog-post` becomes `https://codethoughts.io/posts/a-blog-post`)

We’re avoiding any complex rewrite expressions, such as regex, because it’s a) not actually needed and b) not available on the free plan.

In the Dashboard console it will look something like this:

[![Image 11: The Redirect Rules entry for dynamically redirecting the incoming requests](https://codethoughts.io/processed_images/Screenshot_2024-07-08_at_16.17.27.82877b6820694331.png)](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/Screenshot_2024-07-08_at_16.17.27.png)

The Redirect Rules entry for dynamically redirecting the incoming requests

The Redirect Rules entry for dynamically redirecting the incoming requests

Hope that helps if you’re ever running into the same!

👉 [Let me know what you think over on Medium](https://codethoughts.medium.com/redirecting-urls-with-cloudflare-91a8f85cefdd) or in the comments below 👇

