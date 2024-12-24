---
title: Hello emacs.tv
date: 2024-12-24
extra:
  source: https://lmno.lol/alvaro/hello-emacstv
  original_title: Hello emacs.tv
---
## Summary
**摘要**：
作者在 2024 年 12 月 23 日发布的文章中讨论了与 Sacha Chua 有关的 Emacs 社区活动和项目发展。Sacha Chua 指出了构建一个类似于 Ruby Video 的 Emacs 视频索引的创意，并提议使用简单的文本解决方案，例如 org mode。随后，Sacha 分享了 Emacs 视频源的初步dump，这促使作者编写代码将这个 org feed 转化为 web 界面，诞生了“emacs.tv”项目。此项目使用 org feed 并具备多种集成方式，提供了可视化的 Emacs 相关视频资源。作者对该项目进行了初步实现，并表示对于未来可能性及改进提出了进一步请求，包括内容提交、标签优化以及用户反馈，旨在提升内容丰富度和项目质量。

**要点总结**：
1. **项目起源**：基于 Sacha Chua 的提议和请求，作者开发了以 org feed 为基础的“emacs.tv”项目，旨在创建一个动态的 Emacs 视频索引。
2. **设计与集成**：“emacs.tv”具备组织和呈现 Emacs 相关视频资源的能力，支持不同的集成方式，旨在与社区共享资源，提升可访问性和用户体验。
3. **初步成功与社区参与**：作者展示了项目的初步实现情况，强调内部已经存在丰富的视频资源，鼓励社区成员提交并优化内容。
4. **呼吁反馈与改进**：项目目前处于初始阶段，作者呼吁社区成员提供内容、标签乃至技术建议，以促进项目的发展和完善。
5. **公共政策**：最后，作者简述了与“emacs.tv”项目相关的隐私政策及服务条款，强调了合规性与社区使用条款。
## Full Content
Title: Hello emacs.tv

URL Source: https://lmno.lol/alvaro/hello-emacstv

Markdown Content:
December 23, 2024A few days ago, [Sacha Chua](https://sachachua.com/blog/) mentioned how [cool it would be to have an Emacs video index](https://social.sachachua.com/@sacha/statuses/01JF94JQQNNRXMTKN3Y1774TFP) like [Ruby Video](https://www.rubyvideo.dev/topics). I mentioned how I had similarly considered a low-tech solution, maybe powered by plain text (bonus points for [org mode](https://orgmode.org/) of course).

A little later, Sacha [shared a preliminary video feed dump](https://social.sachachua.com/@sacha/statuses/01JFG5T3C6E88362DRDZN9ANA6), in org! With that, I wrote the [first experiment to render the org feed](https://indieweb.social/@xenodium/113682069315989397) and [emacs.tv](https://emacs.tv/) was born.

![Image 3](https://xenodium.com/images/hello-emacstv/screenshot.png)

[emacs.tv](https://emacs.tv/) is merely a few days old. Powered by an org feed (rendered client-side), but we can fetch and render in all sorts of ways. [emacs.tv](https://emacs.tv/) brings it to the web, though I'm sure we can come up with all sorts of Emacs integrations. A new major mode? Or maybe convert the org feed to rss and plug into [elfeed](https://github.com/skeeto/elfeed)?

This is what a feed entry looks like:

```
* EmacsConf.org: How we use Org Mode and TRAMP to organize and run a multi-track conference :emacsconf:emacsconf2023:org:tramp:
:PROPERTIES:
:DATE: 2023-12-03
:URL: https://emacsconf.org/2023/talks/emacsconf
:MEDIA_URL: https://media.emacsconf.org/2023/emacsconf-2023-emacsconf--emacsconforg-how-we-use-org-mode-and-tramp-to-organize-and-run-a-multitrack-conference--sacha-chua--main.webm
:YOUTUBE_URL: https://www.youtube.com/watch?v=uTregv3rNl0
:TOOBNIX_URL: https://toobnix.org/w/eX2dXG3xMtUHuuBz4fssGT
:TRANSCRIPT_URL: https://media.emacsconf.org/2023/emacsconf-2023-emacsconf--emacsconforg-how-we-use-org-mode-and-tramp-to-organize-and-run-a-multitrack-conference--sacha-chua--main.vtt
:SPEAKERS: Sacha Chua
:SERIES: EmacsConf 2023
:END:
```

We need your help
-----------------

As mentioned, this is a new project. It's a good start, but it can only get better with your help.

### Submit more content

Sacha kickstarted a [wonderful video feed,](https://raw.githubusercontent.com/emacstv/emacstv.github.io/refs/heads/main/videos.org) a collection of 1715 videos as of today. We need more. Are your published videos missing? Reckon other videos should be listed? Please help by [submitting](https://github.com/emacstv/emacstv.github.io#add-videos) new entries.

### Improve our tagging

Many of the listed videos could use more tags. Please help us by tagging content in [video.org](https://raw.githubusercontent.com/emacstv/emacstv.github.io/refs/heads/main/videos.org) and submit a [pull request](https://github.com/emacstv/emacstv.github.io/pulls).

### Take it for a spin

Or maybe just take [emacs.tv](https://emacs.tv/) for a spin and [give us some feedback](https://github.com/emacstv/emacstv.github.io/issues).

Happy holidays! 🎄☃️

  

[privacy policy](https://lmno.lol/blog/privacy-policy) · [terms of service](https://lmno.lol/blog/terms-of-service)

