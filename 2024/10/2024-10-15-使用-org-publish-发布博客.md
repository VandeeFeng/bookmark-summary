# 使用 org-publish 发布博客
- URL: https://taxodium.ink/org-publish-blog
- Added At: 2024-10-15 08:22:41
- [Link To Text](2024-10-15-使用-org-publish-发布博客_raw.md)

## TL;DR
作者将博客从 Markdown 迁移到 Emacs 的 org-mode，并使用 org-publish 进行发布。这种方式简化了博客内容和维护，提供了更好的兼容性和阅读体验。文章详细介绍了 org-publish 的使用方法、配置和注意事项，但也提到了其缺点，如执行慢和集成 CI/CD 麻烦。

## Summary
使用 org-publish 发布博客
===========================

动机
----

作者将博客从 Markdown 迁移到了 Emacs 的 org-mode，并且尝试了多种不同的博客发布方式，最终发现 org-publish 不仅简化了博客的内容和维护，也提供了更好的兼容性和阅读体验。

相比之前的变化
--------------

*   简化了博客内容，只有 org 文件、css 文件、字体和图片
*   使用 Emacs 内置的包转换 org 文件，维护起来更简单
*   按照 Better Mother Fucking Website 和 The Best Mother Fucking Website 的建议设置了字体颜色、字体大小、链接颜色、行间距和行宽等样式
*   使用 Atkinson Hyperlegible 字体，让一些容易混淆的字符更容易区分

org-publish 的使用
---------------

org-publish 的使用方法如下：

*   定义任务，每个任务指定处理什么文件，怎么处理，处理之后放到什么地方
*   可以单独地执行某个任务，也可以将任务串联起来执行
*   需要解决的一些问题包括：
	+ 构建后代码块的高亮
	+ 页眉页脚的设置
	+ RSS 的设置
	+ 缓存问题
	+ 复用 :html-head 等

org-publish 的完整代码
-----------------

具体代码请参考 [init-org-publish.el](https://github.com/Spike-Leung/emacs.d/blob/main/lisp/my-lisp/init-org-publish.el)。

一些缺点
----

*   在执行 org-publish 时，如果内容多，可能会很慢，此时会阻塞 Emacs，不能做其他事情
*   由于依赖 Emacs，Netlify 等平台上没有开箱即用的构建命令，集成 CI/CD 相对麻烦

其他
--

其他一些注意事项包括：

*   可以通过 YASnippet 或其他方式，设置 org 文件共用内容
*   每个任务可以设置不同的样式和选项

TODO Todo
---------

未完成的任务包括：

*   复用 :html-head 等
*   优化 RSS 的内容
*   针对 weekly 单独设置 RSS
*   增加搜索功能
*   实现 CI/CD
