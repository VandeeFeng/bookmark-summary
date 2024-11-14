---
title: Fcitx 最佳配置实践
date: 2024-11-14
extra:
  source: https://manateelazycat.github.io/2024/11/13/fcitx-best-config/
  original_title: Fcitx 最佳配置实践
---
## Summary
**摘要**：
本文主要介绍了如何在Linux环境下配置Fcitx输入法以获得最佳使用体验。内容涵盖了安装Fcitx及其匹配组件、设置GTK和QT环境参数以避免打字太快出现漏字的问题、安装并配置Fcitx皮肤、以及安装和设置白霜输入法。通过这些步骤，用户可以优化Fcitx输入法的性能和使用体验。最后，文章指引用户如何在Emacs中集成白霜输入法，实现高效的文字输入。

**要点总结**：
1. **安装Fcitx5输入法组件**：确保安装`fcitx5`、`fcitx5-gtk`、`fcitx5-qt`、`fcitx5-configtool`、`fcitx5-rime`和`fcitx5-im`，尤其注意到安装`fcitx5-gtk`和`fcitx5-qt`以修正打字时快速输入导致漏字的问题。将`GTK_IM_MODULE`、`QT_IM_MODULE`和`XMODIFIERS`环境变量设置为`fcitx`。

2. **Fcitx5输入法皮肤配置**：在`.xprofile`中添加指定的环境变量配置，推荐使用命令安装`fcitx5-skin-adwaita-dark`皮肤包，并修改`classicui.conf`文件进行个性化调整，包括禁用横向候选列表、避免字体随DPI缩放、设置字体大小和主题等。

3. **安装并配置白霜输入法**：通过Clone方式安装白霜拼音包到正确的目录下，并按步骤调整默认配置，包括修改候选词显示策略和候选数量，以改进输入流畅性。切换回Fcitx目录并完成各种配置的复制。

4. **处理误输入的拼音**：通过清理或更新`en.dict.yaml`文件来自定义和处理用户误输入的拼音，通过保存配置文件并重启Fcitx来解决误输入带来的干扰。

5. **Emacs中集成白霜输入法**：通过安装`posframe`加强候选词显示，下载并配置`emacs-rime`插件，设置rime相关选项，如设置用户数据目录、指定字体样式以及使用`posframe`显示候选词，确保Emacs与白霜输入法之间的协调工作。

总之，通过按部就班地遵循上述配置步骤，用户能够显著提高Fcitx输入法的性能和使用满意度，无论是在Linux系统上使用Fcitx作为整体输入解决方案，还是在Emacs等文本编辑器中结合白霜输入法专门优化输入体验。
## Full Content
Title: Fcitx 最佳配置实践 2024-11-13

URL Source: https://manateelazycat.github.io/2024/11/13/fcitx-best-config/

Markdown Content:
Linux 下最爽的输入法就是 Fcitx 了， 但是没有配置好， 就会出现各种各样的问题， 比如打太快漏字这种问题。

今天把所有博客关于 Fcitx 的配置都整理成一篇， 方便我自己和大家以后用。

### 安装 Fcitx5 输入法

安装 Fcitx5 软件包：

```
sudo pacman -S fcitx5 fcitx5-gtk fcitx5-qt fcitx5-configtool fcitx5-rime librime
```

*   fcitx5: 输入法基础框架主程序
*   fcitx5-gtk: GTK 程序的支持， 必须安装， 修复打字太快漏字的问题
*   fcitx5-qt: QT5 程序的支持， 必须安装， 修复打字太快漏字的问题
*   fcitx5-configtool: 图形化配置工具
*   fcitx5-rime: RIME 输入法
*   fcitx5-im: 输入法设置工具
*   librime: rime 相关库， 下面的 emacs-rime 会用到

然后将下面的内容粘贴到 ~/.xprofile

```
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```

重新登录即可。

备注：

*   需要安装 `fcitx5-gtk` 和 `fcitx5-qt` 并写入上面 IM 设置， 不然打字太快会发生漏字的现象， 就是拼音没有变成汉字而是直接插入输入框中。
*   附加组件: 粘贴板和快速输入模块的快捷键去掉， 避免和 Emacs 按键冲突

### 安装 Fcitx5 输入法皮肤

```
yay -S fcitx5-skin-adwaita-dark
```

然后修改配置文件 ~/.config/fcitx5/conf/classicui.conf

```
# 横向候选列表
Vertical Candidate List=False

# 禁止字体随着 DPI 缩放， 避免界面太大
PerScreenDPI=False

# 字体和大小， 可以用 fc-list 命令来查看使用
Font="Noto Sans Mono 13"

# Gnome3 风格的主题
Theme=adwaita-dark
```

备注： 我比较喜欢仓耳今楷， 上面的 Font 可以换成 `TsangerJinKai03-6763 15`

### 安装白霜拼音

上面的步骤只是把 Fcitx 的核心和皮肤搞定了， 但是 Fcitx 默认的词库非常难用, 流畅的输入需要安装白霜输入法。

使用下面的命令拷贝白霜拼音的所有 rime 配置到 fcitx 的 rime 配置目录下

```
git clone https://github.com/gaboolic/rime-frost --depth=1
```

#### 修改默认配置

切换到 rime-ice 目录， 做下面三个操作:

1.  grep 目录下所有`- { when: paging, accept: comma, send: Page_Up }` 和 `- { when: has_menu, accept: period, send: Page_Down }` 内容， 去掉注释
2.  grep `page_size`, 把 8 换成 9 即可

```
sed -i 's/# \(- { when: \(paging\|has_menu\), accept: \(comma\|period\), send: Page_\(Up\|Down\) }\)/\1/' default.yaml

sed -i 's/page_size: 5/page_size: 9/' default.yaml
```

前两个操作是实现逗号、 句号翻页， 后面一个操作是更改候选词的数量

#### 更新到 Fcitx 目录

调整完上面配置后， 进行下面拷贝操作

```
cp -r ./rime-ice/* ~/.config/fcitx/rime/
cp -r ./rime-ice/* ~/.local/share/fcitx5/rime
```

*   ~/.config/fcitx/rime/: 这个目录主要是 Emacs 的 emacs-rime 插件会读取
*   ~/.local/share/fcitx5/rime: 这个目录是 Fcitx 读取的， 用于外部软件使用白霜输入法

#### 删除误输入的拼音

有时候我们会不小心把拼音确认了， 这样这些拼音就会变成第一个候选词， 影响拼音后面对应的中文候选词。

Fcitx 的用户自定义英文候选词都会自动记录到下面配置文件中：

~/.local/share/fcitx5/rime/en\_dicts/en.dict.yaml ~/.config/fcitx/rime/en\_dicts/en.dict.yaml

找到误输入的字符串， 保存配置文件重启 Fcitx 即可。

### 安装 emacs-rime

这一节讲的是怎么让 Emacs 可以使用上白霜输入法。

首先安装 [posframe](https://github.com/tumashu/posframe), posframe 可以让侯选词显示在光标处， 所以建议安装。

然后下载 emacs-rime:

```
git clone https://github.com/DogLooksGood/emacs-rime
```

把 emacs-rime 目录放到 `load-path` 下， 添加以下配置:

```
(require 'rime)

;;; Code:
(setq rime-user-data-dir "~/.config/fcitx/rime")

(setq rime-posframe-properties
      (list :background-color "#333333"
            :foreground-color "#dcdccc"
            :font "WenQuanYi Micro Hei Mono-14"
            :internal-border-width 10))

(setq default-input-method "rime"
      rime-show-candidate 'posframe)
```

上面的配置分别设置 emacs-rime 读取 RIME 配置的路径、 UI 细节和使用 posframe 来显示候选词。

重启 Emacs 后， 调用 `toggle-input-method` 命令来尝试输入中文。

[白霜拼音](https://github.com/gaboolic/rime-frost) 主页有一些输入用例， 如果你打同样的拼音可以补全相同的中文候选词， 就证明已经成功用上了白霜拼音。

