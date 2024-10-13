# 使用 org-publish 发布博客
- URL: https://taxodium.ink/org-publish-blog
- Added At: 2024-10-13 17:35:26
- [Link To Text](2024-10-13-使用-org-publish-发布博客_raw.md)

## TL;DR
本文总结了使用 org-publish 发布博客的简化内容和维护经验。它介绍了相比之前的变化，包括博客内容和构建的简化、Emacs 内置的转换特性以及一些为了更好阅读而设置的样式。文章也讨论了 org-publish 的使用，包括定义任务、执行任务以及遇到的问题和完整代码。最后，总结了一些 org-publish 的缺点和其他包括共用内容、优化 RSS 内容、增加搜索功能等 TODO 项。

## Summary
### 总结博客

#### 动机
使用 org-publish 发布博客，旨在简化博客内容和维护。

#### 相比之前的变化
*   极大简化博客内容，去掉主题和模板，只保留博客内容的 org 文件、css 文件、字体、图片，以及最终转换出来的 HTML 文件。
*   博客的编写、构建只需要 Emacs 就能完成，使用 Browsersync 本地查看构建的 HTML。
*   转换后就是标准的 HTML，并且是使用 Emacs 内置的包转换 org 文件，理论上 org 的特性应该都能转换。
*   根据 better mother fucking website 和 the best mother fucking website 的建议，设置了字体颜色、字体大小、链接颜色、行间距、行宽等，使其比默认的浏览器样式更好阅读。
*   使用 Atkinson Hyperlegible 字体，让一些容易混淆的字符更容易区分。

#### Org-publish 的使用
*   定义多个任务，每个任务指定处理什么文件，怎么处理，处理之后放到什么地方。
*   可以单独地执行某个任务，也可以将任务串联起来执行。

#### 遇到的问题
*   **构建后代码块的高亮**：需要写一个函数切换主题，以获得合适的高亮颜色。
*   **页眉页脚的设置**：自定义 HTML 头、页眉、页脚需要传入字符串，抽象成变量或函数复用时需要注意。
*   **RSS 的设置**：生成 RSS 文件需要将多个 org 文件合并成一个 RSS 文件。
*   **缓存问题**：执行 org-publish 后，需要清除缓存才能看到更新。

#### Org-publish 的完整代码
见文章附录。

#### 一些缺点
*   执行 org-publish 时可能会很慢，导致 Emacs 阻塞不能做其他事情。
*   缺乏开箱即用的构建命令，集成 CI/CD 需要额外配置。

#### 其他
*   可以通过 YASnippet 或其他方式设置 org 文件共用内容。
*  TODO：复用 HTML 头、页眉、页脚；优化 RSS 的内容；增加搜索功能；实现 CI/CD。
