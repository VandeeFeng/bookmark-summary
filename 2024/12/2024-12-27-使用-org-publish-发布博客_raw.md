Title: 使用 org-publish 发布博客

URL Source: https://taxodium.ink/org-publish-blog.html

Markdown Content:
目录
--

*   [动机](https://taxodium.ink/org-publish-blog.html#84028fac-1594-46e7-af48-35b2ce7b955f)
*   [相比之前的变化](https://taxodium.ink/org-publish-blog.html#3327ca5c-29c5-4e47-9794-c899dddb0c04)
*   [org-publish 的使用](https://taxodium.ink/org-publish-blog.html#6c1456b6-fe60-46a6-bcc0-df51a55113ec)
*   [org-publish 的完整代码](https://taxodium.ink/org-publish-blog.html#5c1bdfcb-aae9-4313-8f2b-cbbfbf23f7c8)
*   [一些缺点](https://taxodium.ink/org-publish-blog.html#7c8e8d68-1d39-4b29-bbf0-d2c235f93943)
*   [Tricks](https://taxodium.ink/org-publish-blog.html#91e2995e-e98c-48c0-8d06-e62f704cc3eb)
    *   [Snippet](https://taxodium.ink/org-publish-blog.html#6ab69c9d-68fa-4fb3-881a-19c7923a2e65)
    *   [内容的收起展开](https://taxodium.ink/org-publish-blog.html#e54adc1f-1183-438d-90c6-6f5789edd6de)
    *   [行内图片的插入](https://taxodium.ink/org-publish-blog.html#aff9d448-171b-4528-bd68-86124edf11ce)
*   [TODO Todo](https://taxodium.ink/org-publish-blog.html#169fa4fb-5d6c-4560-9c66-2a8d89d2c56f)
*   [Refs](https://taxodium.ink/org-publish-blog.html#ac3d4dcc-6a00-4860-99b4-89905b893ab6)

博客经历过几次更新，最开始的时候是用 markdown 写博客，然后用 [Hexo](https://hexo.io/) 发布。

然后学习了 Vue，又尝试用 [VuePress](https://vuepress.vuejs.org/) 发布，它们都是托管在 [Github Pages](https://pages.github.com/) 上。

后来接触了 [Emacs](https://www.gnu.org/software/emacs/)，就从 markdown 迁移到了 [org-mode](https://orgmode.org/)，然后使用 [Hugo](https://gohugo.io/) [1](https://taxodium.ink/org-publish-blog.html#fn.1)发布。

因为 GitHub 直连变慢了，所以将内容托管到了 [Vercel](https://vercel.com/) 和 [Netlify](https://www.netlify.com/)。

最近将博客又更新了一下，使用 [org-publish](https://orgmode.org/manual/Publishing.html) 进行博客的发布，主要是让博客加载相对快一些，维护起来更简单一些。

动机
--

相比之前的变化
-------

*   极大的简化了博客内容，没有主题，没有模板，只有博客内容的 org 文件、css 文件、字体、图片，以及最终转换出来的 HTML 文件
*   博客的编写、构建只需要 Emacs 就能完成（以及 [Browsersync](https://browsersync.io/) 用于本地查看构建的 HTML）
*   转换后就是标准的 HTML，而且是使用 Emacs 内置的包转换 org 文件，理论上 org 的特性应该都能转换
*   按照 [better mother fucking website](http://bettermotherfuckingwebsite.com/) 和 [the best mother fucking website](https://thebestmotherfucking.website/) 的建议，设置了字体颜色，字体大小，链接颜色，行间距，行宽等，比默认的浏览器样式好阅读一些
*   使用 [Atkinson Hyperlegible](https://www.brailleinstitute.org/freefont/) 字体，让一些容易混淆的字符更容易区分

总而言之，就是清爽了很多，兼容性也应该不错。

org-publish 的使用
---------------

org-publish 的使用有点像 [gulp](https://gulpjs.com/)，你可以定义很多个任务，每个任务指定处理什么文件，怎么处理，处理之后放到什么地方。

你可以单独地执行某个任务，也可以将任务串联起来执行。

过程中碰到的几个问题：

**构建后代码块的高亮**

高亮的颜色是基于 Emacs 当前的主题的，而我的博客整体是亮色的，因此需要 Emacs 中也使用亮色的主题才能得到合适的高亮颜色。

为此写了 `spike-leung/apply-theme-when-publish` 用于在执行 `org-publish` 的时候切换主题。

**RSS 的设置**

[ox-rss](https://github.com/emacsmirror/ox-rss) 可以生成 RSS 文件，但它是针对一个 org 文件的，对于多个 org 文件，它会分别生成 RSS。

但是我需要的是把多个 org 文件生成为一个 RSS 文件。

不过别人已经踩过坑，按照 [Org mode blogging: RSS feed](https://writepermission.com/org-blogging-rss-feed.html) 中的方法实现了。

具体来说就是遍历所有的 org 文件，将他们的内容插入到一个 rss.org 文件中，再基于 rss.org 使用 ox-rss 去生成 RSS 文件。

[Org mode blogging: RSS feed](https://writepermission.com/org-blogging-rss-feed.html) 的实现会把整个 org 文件的内容插入到 rss.org 中。

但是如果内容很多时，Emacs 会崩溃，我目前是改成只插入标题，后面再研究一下如何优化。

如果执行 RSS 构建后，发现新写的文章不在 RSS 中，也可能是缓存问题，可以尝试：

*   删除 `org-publish-timestamp-directory` 中 RSS 的 cache
*   删除博客相关的 buffer 试试（或者删除全部 buffer）
*   检查一下是不是 `:exclude` 正则表达式写得有问题

**index 文件的设置**

设置 `:makeindex t` 可以生成 index 文件，需要在 org 文件中设置 `#+INDEX` keyword。

但是生成的文件名固定是 theindex.org, 并且会按照文章标题首个字进行索引，看起来很怪，最后用 sitemap 替代了。

现在看到的 [Home](https://taxodium.ink/index.html) 其实就是一个 sitemap。

`#+date` **的设置**

原来 Hugo 生成的日期 (2023-05-31T13:38:39+08:00) 在转换成 sitemap 的时候似乎不能识别，

于是改成 org 的日期格式 (<2023-05-31 Wed\>)，这样 sitemap 就能正常按照时间排序了。

**缓存问题**

执行 org-publish 之后，会在 `org-publish-timestamp-directory` 指定的目录下生成缓存，有时调整了页眉页脚，可能需要清除缓存才能看到效果。

不过可以执行 `C-u M-x org-publish` 忽略缓存进行构建。

:time-stamp-file nil

设置 `:time-stamp-file nil` 可以避免每次执行 org-publish 的时候都往 HTML 插入最新的时间戳，导致每次变更的文件很多。

`:html-head` ， `:html-preamble` ， `:html-postamble` 的复用

最开始定义 `org-publish-project-alist` ， 我是这么写的，导致一直无法使用变量抽象一些公用的 string：

(defconst spike-leung/html-head "
  <link rel=\\"stylesheet\\" href=\\"../styles/style.css\\" type=\\"text/css\\"/\>
  <link rel=\\"icon\\" href=\\"/favicon.ico\\" type=\\"image/x-icon\\"\>
  "
  "\`:html-head' for \`org-publish'.")

(setq org-publish-project-alist
      '(("orgfiles"
         :base-directory "~/git/taxodium/post"
         :base-extension "org"
         :html-head ,spike-leung/html-head
         ;; ... 还有其他很多设置
         )))

我在这里用的是 `'` 去定义， `'` 在 elisp 中的作用是：

> The special form quote returns its single argument, as written, without evaluating it.
> 
> This provides a way to include constant symbols and lists, which are not self-evaluating objects, in a program.
> 
> [Quoting](https://www.gnu.org/software/emacs/manual/html_node/elisp/Quoting.html)

因此 `,spike-leung/html-head` 会被当作一个常量，而不会被执行， 而 `,spike-leung/html-head` 这个字符串 `:html-head` 并不认识。

要让 `,spike-leung/html-head` 被执行，需要将 `'` 换成 `` ``` :

    (defconst spike-leung/html-head "
      <link rel=\\"stylesheet\\" href=\\"../styles/style.css\\" type=\\"text/css\\"/\>
      <link rel=\\"icon\\" href=\\"/favicon.ico\\" type=\\"image/x-icon\\"\>
      "
      "\`:html-head' for \`org-publish'.")

    (setq org-publish-project-alist
\-          '(("orgfiles"
+          \`(("orgfiles"
             :base-directory "~/git/taxodium/post"
             :base-extension "org"
             :html-head ,spike-leung/html-head
             ;; ... 还有其他很多设置
             )))

> Backquote constructs allow you to quote a list, but selectively evaluate elements of that list.
> 
> In the simplest case, it is identical to the special form quote (described in the previous section; see [Quoting](https://www.gnu.org/software/emacs/manual/html_node/elisp/Quoting.html)).
> 
> …
> 
> The special marker ‘,’ inside of the argument to backquote indicates a value that isn’t constant.
> 
> The Emacs Lisp evaluator evaluates the argument of ‘,’, and puts the value in the list structure.
> 
> [Backquote](https://www.gnu.org/software/emacs/manual/html_node/elisp/Backquote.html)

`` ``` 和 `'` 的不同是，它会执行 list 里面的内容， 这样 `,spike-leung/html-head` 就会被执行并返回对应的 string，满足 `:html-head` 的需要。

org-publish 的完整代码
-----------------

以下代码可以作为参考，最新的请看 [init-org-publish.el](https://github.com/Spike-Leung/emacs.d/blob/main/lisp/my-lisp/init-org-publish.el)。

init-org-publish.el

;;; init-org-publish.el --- org publish config for my blog -\*- lexical-binding: t -\*-
;;; Commentary:
;;; Code:

(maybe-require-package 'ox-rss)

(defun spike-leung/apply-theme-when-publish (&rest args)
  "Switch theme when do \`org-publish'.
ARGS will pass to \`org-publish'."
  (let ((current-theme (car custom-enabled-themes)))
    (load-theme 'modus-operandi-tinted t)
    (apply args)
    (when current-theme
      (disable-theme 'modus-operandi-tinted)
      (enable-theme current-theme)
      (load-theme current-theme :no-confirm))))

(advice-add 'org-publish :around #'spike-leung/apply-theme-when-publish)

(defun spike-leung/get-org-keyword (keyword)
  "Get the value of the given KEYWORD in the current Org file."
  (let ((keywords (org-collect-keywords (list keyword))))
    (if-let ((value (car (cdr (assoc keyword keywords)))))
        value
      (format "No %s found" keyword))))

(defun spike-leung/org-publish-find-date (file project)
  "Extract \`#+date\` form org file.
FILE is org file name.
PROJECT is the current project.
"
  (with-temp-buffer
    (insert-file-contents file)
    (org-mode)
    (spike-leung/get-org-keyword "DATE")))

(defun spike-leung/sitemap-format-entry (entry style project)
  "自定义网站地图条目格式，添加日期信息。"
  (let\* ((filename (org-publish--expand-file-name entry project))
         (date (spike-leung/org-publish-find-date filename project)))
    (format "%s %s"
            (org-publish-sitemap-default-entry entry style project)
            (if date
                date
              "long time ago..."))))

;; @see: https://writepermission.com/org-blogging-rss-feed.html
(defun rw/org-rss-publish-to-rss (plist filename pub-dir)
  "Publish RSS with PLIST, only when FILENAME is 'rss.org'.
PUB-DIR is when the output will be placed."
  (if (equal "rss.org" (file-name-nondirectory filename))
      (org-rss-publish-to-rss plist filename pub-dir)))

(defun rw/format-rss-feed (title list)
  "Generate RSS feed as a string.
TITLE is the RSS feed title and LIST contains files to include."
  (concat "#+TITLE: " title "\\n\\n" (org-list-to-subtree list)))

(defun rw/format-rss-feed-entry (entry style project)
  "Format ENTRY for the RSS feed.
ENTRY is a file name.  STYLE is either 'list' or 'tree'.
PROJECT is the current project."
  (cond ((not (directory-name-p entry))
         (let\* ((title (org-publish-find-title entry project))
                (date (format-time-string "%Y-%m-%d" (org-publish-find-date entry project)))
                (link (concat (file-name-sans-extension entry) ".html")))
           (with-temp-buffer
             (insert (format "%s\\n" title))
             (insert ":PROPERTIES:\\n:RSS\_PERMALINK: " link "\\n:PUBDATE: " date "\\n:END:\\n")
             (insert (format "%s" title))
             (buffer-string))
           ))
        ((eq style 'tree)
         ;; Return only last subdir.
         (file-name-nondirectory (directory-file-name entry)))
        (t entry)))

(defconst spike-leung/html-head "
<link rel=\\"stylesheet\\" href=\\"../styles/style.css\\" type=\\"text/css\\"/\>
<link rel=\\"icon\\" href=\\"/favicon.ico\\" type=\\"image/x-icon\\"\>
"
  "\`:html-head' for \`org-publish'.")

(defconst spike-leung/html-preamble "
 <nav\>
  <ul\>
    <li\><a href=\\"/index.html\\"\>Home</a\></li\>
    <li\><a href=\\"/about.html\\"\>About</a\></li\>
    <li\><a href=\\"/rss.xml\\"\>RSS</a\></li\>
    <li\><a href=\\"https://github.com/Spike-Leung/taxodium/tree/org-publish\\"\>GitHub</a\></li\>
  </ul\>
</nav\>
"
  "\`:html-preamble' for \`org-publish'." )

(defconst spike-lenng/html-postamble "
<p class=\\"author\\"\>Author: <a href=\\"mailto:l-yanlei@hotmail.com\\"\>%a</a\></p\>
<p class=\\"date\\"\>Date: %d</p\>
<p class=\\"license\\"\>License: <a href=\\"https://www.creativecommons.org/licenses/by-nc/4.0/deed.zh-hans\\"\>CC BY-NC 4.0</a\></p\>
<script src=\\"https://utteranc.es/client.js\\" repo=\\"Spike-Leung/taxodium\\" issue-term=\\"pathname\\" theme=\\"github-light\\" crossorigin=\\"anonymous\\" async\></script\>
"
  "\`:html-postamble' for \`org-publish'.")

(setq org-publish-project-alist
      \`(("orgfiles"
         :base-directory "~/git/taxodium/post"
         :base-extension "org"
         :publishing-directory "~/git/taxodium/publish"
         :publishing-function org-html-publish-to-html
         :section-numbers nil
         :with-toc t
         :with-tags t
         :time-stamp-file nil
         :html-head ,spike-leung/html-head
         :html-preamble ,spike-leung/html-preamble
         :html-postamble ,spike-lenng/html-postamble
         :exclude "rss.org"
         :auto-sitemap t
         :sitemap-filename "index.org"
         :sitemap-title "Taxodium"
         :sitemap-format-entry spike-leung/sitemap-format-entry
         :sitemap-sort-files anti-chronologically
         :author "Spike Leung"
         :email "l-yanlei@hotmail.com")

        ("sitemap"
         :base-directory "~/git/taxodium/post"
         :base-extension "org"
         :publishing-directory "~/git/taxodium/publish"
         :publishing-function org-html-publish-to-html
         :time-stamp-file nil
         :html-head ,spike-leung/html-head
         :html-preamble ,spike-leung/html-preamble
         :include ("index.org")
         :exclude ".\*"
         :html-postamble nil)

        ("rss"
         :base-directory "~/git/taxodium/post"
         :base-extension "org"
         :exclude "about\\\\|index"
         :publishing-directory "~/git/taxodium/publish"
         :publishing-function rw/org-rss-publish-to-rss
         :html-postamble nil
         :section-numbers nil
         :with-toc nil
         :rss-extension "xml"
         :html-link-home "https://taxodium.ink"
         :html-link-use-abs-url t
         :auto-sitemap t
         :sitemap-filename "rss.org"
         :sitemap-title "Taxodium"
         :sitemap-sort-files anti-chronologically
         :sitemap-function rw/format-rss-feed
         :sitemap-format-entry rw/format-rss-feed-entry
         :author "Spike Leung"
         :email "l-yanlei@hotmail.com")

        ("website" :components ("orgfiles" "sitemap" "rss"))))

(provide 'init-org-publish)
;;; init-org-publish.el ends here

一些缺点
----

*   在执行 org-publish 时，如果内容多，可能会很慢，此时会阻塞 Emacs，不能做其他事情
*   由于依赖 Emacs，[Netlify](https://www.netlify.com/) 等平台上没有开箱即用的构建命令，集成 CI/CD 相对麻烦
*   还不知道如何 Hot Reload，所以预览编辑后的效果不是很方便，总是需要先执行一次构建

Tricks
------

### Snippet

为了方便，可以通过 [YASnippet](https://github.com/joaotavora/yasnippet) 或其他方式，设置 org 文件共用内容。

例如这是我用于[写周刊的 snippet](https://github.com/Spike-Leung/emacs.d/blob/windows/snippets/org-mode/weekly):

weekly snippet

\# -\*- mode: snippet -\*-
# name: weekly
# key: weekly
# group: blog
# --

#+title: Weekly#$1
#+INDEX: weekly!#$1
#+date: \`(format-time-string "<%Y-%m-%d %a\>" (current-time))\`
#+lastmod: \`(format-time-string "<%Y-%m-%d %a %H:%M\>" (current-time))\`
#+author: Spike Leung
#+email: l-yanlei@hotmail.com
#+description: ""
#+tags: weekly


\* News | Article
$0
\* Tutorial

\* Code

\* Cool Bit

\* Tool | Library

\* Music

### 内容的收起展开

需要开启 `org-html-html5-fancy` ([13.9.3 HTML doctypes ¶](https://orgmode.org/manual/HTML-doctypes.html))，从而可以使用 [<details\>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)

(setq org-html-html5-fancy t)
(setq org-html-doctype "html5")

然后就可以这么用：

#+begin\_details
#+HTML: <summary\>Demo Code</summary\>
#+begin\_src JavaScript
console.log('Hello world!')
#+end\_src
#+end\_details

### 行内图片的插入

如果你想在文字中间插入一张图片![Image 3: avatar.jpg](https://taxodium.ink/images/org-publish-blog/avatar.jpg)，同时你希望控制图片的大小，可以这样：

#+ATTR\_HTML: :class inline-image
如果你想在文字中间插入一张图片\[\[file:./images/org-publish-blog/avatar.jpg\]\]，同时你希望控制图片的大小，可以这样：

然后在 CSS 中通过类名设置样式：

img.inline-image {
  width: 1em;
  height: 1em;
  vertical-align: -3.5px;
}

TODO Todo
---------

*   `[X]` 复用 `:html-head` ， `:html-preamble` 等
*   `[ ]` 优化 RSS 的内容
*   `[ ]` 针对 weekly 单独设置 RSS
*   `[X]` 增加搜索功能 -\> [search](https://taxodium.ink/search.html)，使用 [pagefind](https://github.com/CloudCannon/pagefind) 实现，不过对于中文有的分词分的不是很好，可能搜索不到，凑合用着
*   `[ ]` 实现 CI/CD
*   `[X]` 在不同机器执行 publish 的时候，ID 总是会变化 -\> 每个 heading 都设置 `CUSTOM_ID` ，而不是自动生成，避免不同机器上由于没有缓存，导致变化。
    *   导出是通过 `ox-html.el` 实现的，其中，heading 是通过 `org-html-headline` 实现
    *   ID 通过 `org-html--reference` 返回，如果存在 `CUSTOM_ID` 则会使用它，如果不存在则使用 `org-export-get-reference` 生成 ID，这个方法会搜索 `:internal-references` 和 `:crossrefs` 判断是否存在缓存，如果存在则复用。
*   `[ ]` 编写 Elisp，方便创建当前博客文章对应的图片目录，以及插入图片的 snippets

Refs
----

Date: 2024-09-27 Fri 00:00

Last Modified: 2024-12-06 Fri 00:02

License: [CC BY-NC 4.0](https://www.creativecommons.org/licenses/by-nc/4.0/deed.zh-hans)
