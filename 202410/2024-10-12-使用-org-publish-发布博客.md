# 使用 org-publish 发布博客
- URL: https://taxodium.ink/org-publish-blog
- Added At: 2024-10-12 18:29:03
- [Link To Text](2024-10-12-使用-org-publish-发布博客_raw.md)

## TL;DR
作者分享了更新博客的过程，其中讨论到从hexo到VuePress、再到Emacs、org-mode 和Hugo的转变，最后使用 org-publish 简化博客内容，提升加载速度和可维护性，着重介绍了 org-publish 的配置和使用。

## Summary
**简介**  
文章讲述了作者使用org-publish工具更新博客的过程。作者从 markdown 写博客Hexo 发布开始， 后逐渐学习和使用了 VuePress、Emacs、org-mode 和 Hugo。最近，作者使用 org-publish 发布博客，旨在简化博客内容、加快加载速度和更容易维护。

**相比之前的变化**

*   简化博客内容，没有主题和模板
*   只需要 Emacs 即可完成博客的编写和构建
*   使用 Emacs 内置的包转换 org 文件
*   设置字体颜色、字体大小、链接颜色、行间距和行宽等样式

**org-publish 的使用**

*   定义任务，指定处理文件和处理方式
*   可以单独执行任务或串联任务
*   遇到的问题：构建后代码块高亮、页眉页脚设置、RSS 设置、缓存问题等

**示例代码**

*   org-publish 的完整配置代码

**一些缺点**

*   执行 org-publish 时可能会阻塞 Emacs
*   依赖 Emacs，集成 CI/CD 相对麻烦

**其他**

*   使用 YASnippet 设置 org 文件共用内容
*   TODO 列表：复用 HTML 头部、优化 RSS 内容等
