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
