Title: 手把手带你打造一个媲美 macOS 的 Linux 生产力系统

URL Source: https://www.sqlsec.com/2024/10/ubuntu.html

Published Time: 2024-10-11T02:23:25.000Z

Markdown Content:
别再羡慕人家 macOS 精美的界面了，Linux 同样也可以做到这么精致丝滑的交互体验，还在等什么！？赶紧让 Linux 作为你的主力系统吧～

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%86%99%E5%9C%A8%E5%89%8D%E9%9D%A2 "写在前面")写在前面
----------------------------------------------------------------------------------------------

国光我这一个月安装了很多个 Linux 发行版系统且都深度体验了一下，尝试过 Arch Linux 也试过 Kali Linux，桌面用过激进的 Hyprland 也用过传统的 GNOME，还有花里胡哨的 DDE，最终还是老老实实的选择了 Kubuntu 24.04：

![Image 1](https://image.3001.net/images/20241001/1727787584_66fbf240a47dde267dc2a.png)

为什么选择了 Kubuntu 24.04 主要有以下几个原因：

1.  基于 Ubuntu LTS 24.04 版本，稳定的同时学习门槛也比较低
2.  Kubuntu 自带的是 KDE 5 桌面，这个桌面目前可拓展性很强
3.  KDE6 桌面不兼容 Latte Dock，失去了模仿 MacOS 的精髓

![Image 2](https://image.3001.net/images/20241001/1727786757_66fbef054be7039e15369.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E7%B3%BB%E7%BB%9F%E5%AE%89%E8%A3%85 "系统安装")系统安装
----------------------------------------------------------------------------------------------

本次安装使用的是双系统方案，如果你的硬盘足够大的话，这也是国光比较推荐的方案，毕竟打游戏的话还得是 Windows 系统呀！

安装的时候建议先选择默认的【英文语言、】然后选择【正常模式】安装，毕竟我们是要当作主力系统来使用的：

![Image 3](https://image.3001.net/images/20241001/1727790609_66fbfe11bcefe47334305.png)

磁盘这块是重点，如果你要是双系统的话，建议最好还是自己【手动划分磁盘分区】：

![Image 4](https://image.3001.net/images/20241001/1727790672_66fbfe50e853b071c5e43.png)

我的从 2TB 的硬盘划分出 800多GB 用来安装 Linux，具体的磁盘划分细节如下：

![Image 5](https://image.3001.net/images/20241001/1727790912_66fbff4024932120fdb6a.png)

最后看下我总的设置细概览吧：

![Image 6](https://image.3001.net/images/20241001/1727791547_66fc01bb5ba3fdca1383b.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%9F%BA%E6%9C%AC%E5%87%86%E5%A4%87 "基本准备")基本准备
----------------------------------------------------------------------------------------------

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%9B%B4%E6%96%B0%E6%BA%90 "更新源")更新源
-----------------------------------------------------------------------------------

```
# 切换 root 用户
sudo -i

# 备份更新源
mv /etc/apt/sources.list /etc/apt/sources.list.bak

# 添加 Ubuntu 24.04 中科大源
echo "deb https://mirrors.ustc.edu.cn/ubuntu/ noble main restricted universe multiverse" >> /etc/apt/sources.list
echo "deb https://mirrors.ustc.edu.cn/ubuntu/ noble-security main restricted universe multiverse" >> /etc/apt/sources.list
echo "deb https://mirrors.ustc.edu.cn/ubuntu/ noble-updates main restricted universe multiverse" >> /etc/apt/sources.list
echo "deb https://mirrors.ustc.edu.cn/ubuntu/ noble-backports main restricted universe multiverse" >> /etc/apt/sources.list

# 刷新一下看看速度
apt update
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%9F%BA%E6%9C%AC%E5%B7%A5%E5%85%B7 "基本工具")基本工具
----------------------------------------------------------------------------------------------

既然有更新源的话，安装一些 Geek 必备的工具吧：

```
# 经典必备
sudo apt install curl wget git vim

# netstat 网络外联分析
sudo apt install net-tools

# traceroute 链路追踪
sudo apt install traceroute
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%B8%AD%E6%96%87%E8%BE%93%E5%85%A5 "中文输入")中文输入
----------------------------------------------------------------------------------------------

首先安装好中文语言环境相关的依赖包：

```
sudo apt install fcitx5-frontend-gtk2 fonts-arphic-ukai fonts-arphic-uming fonts-noto-cjk-extra language-pack-zh-hans libreoffice-help-zh-cn libreoffice-l10n-zh-cn
```

然后将语言更改为：【简体中文】

![Image 7](https://image.3001.net/images/20241001/1727786491_66fbedfbd11d8d3899064.png)

更改完成后重启或者注销系统生效，手动添加 【Pinyin】输入法：

![Image 8](https://image.3001.net/images/20241001/1727787003_66fbeffb0f7b0ef19e7e1.png)

因为搜狗输入法官方目前还不支持 Fctix5 输入法框架，我们不能为了个输入法开倒车去安装 Fctix4 吧：

![Image 9](https://image.3001.net/images/20241001/1727787083_66fbf04b4393ef68ceae1.png)

所以这里参考了这篇文章：[fcitx5\_customizer —— 一个让 Fcitx5 更符合简中用户使用习惯的优化脚本](http://www.debuggerx.com/2023/09/20/fcitx5-customizer/)

只需要一条命令即可优化我们的 Fctix5 输入法：

```
# 在线运行并使用推荐配置
curl -sSL https://www.debuggerx.com/fcitx5_customizer/fcitx5_customizer.sh | bash -s -- recommend
```

大家可以根据自己的喜好来自行配置：

![Image 10](https://image.3001.net/images/20241001/1727790179_66fbfc635f24727f49248.png)

后续我们可以在设置里面自行更好输入法皮肤：

![Image 11](https://image.3001.net/images/20241002/1727827075_66fc8c83730021e6b92f3.png)

推荐使用简约大气的 Dracula 皮肤，这样配置后，我们自带的这个输入法已经变得很丝滑了，还要啥搜狗输入法呀！

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%AF%AD%E8%A8%80%E7%8E%AF%E5%A2%83 "语言环境")语言环境
----------------------------------------------------------------------------------------------

我们手动编辑语言环境文件 ，确保都是中文状态：

```
sudo vim /etc/default/locale
```

编辑后的内容如下：

```
LANG=zh_CN.UTF-8
LC_ADDRESS=zh_CN.UTF-8
LC_IDENTIFICATION=zh_CN.UTF-8
LC_MEASUREMENT=zh_CN.UTF-8
LC_MONETARY=zh_CN.UTF-8
LC_NAME=zh_CN.UTF-8
LC_NUMERIC=zh_CN.UTF-8
LC_PAPER=zh_CN.UTF-8
LC_TELEPHONE=zh_CN.UTF-8
LC_TIME=zh_CN.UTF-8
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%88%87%E6%8D%A2%E6%A1%8C%E9%9D%A2 "切换桌面")切换桌面
----------------------------------------------------------------------------------------------

Kubuntu 24.04 自带的 KDE 5 默认使用的 X11 桌面协议，这个 X11 桌面协议真的是老古董来，源于上个世纪 80 年代，虽然目前兼容性还不错，但是时代变了。所以我们需要拥抱 wayland 协议，这样可以有更丝滑的桌面使用体验、更健全的触控板手势支持、更精美精致的 HiDPi 画面缩细节、更好的高分辨率高刷新率显示器的支持、更优雅高效的桌面运行工作效率……

话不多说，我们直接开始安装：

```
sudo apt install plasma-workspace-wayland
```

安装好的话重启一下系统，再次登录的时候，登录界面左下角选择 Wayland 协议的桌面会话就可以了，这样你就可以体验到更加丝滑的 Linux 桌面体验了。

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%BE%93%E5%85%A5%E5%85%BC%E5%AE%B9 "输入兼容")输入兼容
----------------------------------------------------------------------------------------------

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%A7%A3%E5%86%B3%E5%91%8A%E8%AD%A6 "解决告警")解决告警
----------------------------------------------------------------------------------------------

只是发现我们使用 wayland 协议的话，Fcitx 小企鹅输入法开始告警了：

![Image 12](https://image.3001.net/images/20241001/1727794846_66fc0e9e4c1c100a644cf.png)

那么根据提示设置一下：

![Image 13](https://image.3001.net/images/20241002/1727826697_66fc8b0928f2a5a91e728.png)

注销或者重启后发现新的告警：

![Image 14](https://image.3001.net/images/20241001/1727794995_66fc0f334b8020277b83e.png)

```
检测到设置了 GTK_IM_MODULE 和 QT_IM_MODULE 而且 Wayland 输入法前端正在正常工作。推荐不设置 GTK_IM_MODULE 和 QT_IM_MODULE 从而使用 Wayland 输入法前端。更多信息请参见 https://fcitx-im.org/wiki/Using_Fcitx_5_on_Wayland#KDE_Plasma
```

根据官方的提示这是因为为了兼容 X11 协议应用，这个 Kubuntu 的环境变量全局里面自定义了这些值：

```
$ env |grep fcitx
GTK_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
SDL_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
```

而 Fcitx5 官方提醒是不需要设置这 3 个变量值的：

```
GTK_IM_MODULE & QT_IM_MODULE & SDL_IM_MODULE
```

如果是在 XWayland 兼容模式下运行的应用，只需设置：

```
XMODIFIERS=@im=fcitx
```

如果是 chromium/electron 这类应用，建议设置下面这些启动参数：

```
--enable-features=UseOzonePlatform --ozone-platform=wayland --enable-wayland-ime
```

所以解决方法就是手动去取消这 3 各环境变量：

```
# 切换 root 用户
sudo -i

# 覆写 /etc/environment 环境变量
echo "unset GTK_IM_MODULE" >> ~/.profile
echo "unset QT_IM_MODULE" >> ~/.profile
echo "unset SDL_IM_MODULE" >> ~/.profile
```

这样就解决了 Wayland 告警了。

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BA%94%E7%94%A8%E4%BC%98%E5%8C%96 "应用优化")应用优化
----------------------------------------------------------------------------------------------

这样设置后原生对 wayland 支持友好的应用输入法应该都是工作在最佳状态的，比如 Firefox 火狐浏览器等，但是一些保守一点的应用， 输入法的光标和面板明显存在偏移，所以他们还是需要我们给他们设置一下变量的，比如正在编写本文的 Typora 应用，我们手动在应用程序菜单中找到 Typora 图标，然后右键点击【编辑应用程序】，向下图这样，手动把之前取消的环境变量单独给他加回去即可：

```
GTK_IM_MODULE=fcitx SDL_IM_MODULE=fcitx QT_IM_MODULE=fcitx
```

![Image 15](https://image.3001.net/images/20241002/1727829834_66fc974a797eb7c3974dd.png)

这样 Typora 的输入法也就可以工作在最佳状态了。

后续其他输入感觉怪怪的，有问题的应用都可以模仿这样来操作。

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%BD%BF%E7%94%A8%E6%8A%80%E5%B7%A7 "使用技巧")使用技巧
----------------------------------------------------------------------------------------------

Linux 下的 fcitx5 输入法有常用的使用快捷键技巧如下：

| 快捷键组合 | 说明 |
| --- | --- |
| \`空格 | 切换输入法 |
| 左 Shift | 临时切换输入法 |

但是有些网友可能发现，使用 `左 Shift ` 临时切换输入法经常不工作，但有时候却正常工作，经过几天的使用国光总结发现如下规律：

在要输入的应用里面先手动使用 `Ctrl + 空格` 切换输入法后，就可以正常的使用 `左 Shift ` 临时切换输入法了，后面的体验和 Windows 下是同样丝滑的。

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%93%8D%E4%BD%9C%E4%BC%98%E5%8C%96 "操作优化")操作优化
----------------------------------------------------------------------------------------------

工欲善其事，必先利其器，我们基本操作优化前先来学习一下 KDE5 默认的基础快捷键和触控板手势的使用：

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BF%AB%E6%8D%B7%E9%94%AE "快捷键")快捷键
-----------------------------------------------------------------------------------

KDE 也自带来很多高效的快捷键，下面记录分享一下国光我常用的键盘快捷键：

| 快捷键 | 说明 |
| --- | --- |
| Super（Windows 键） | 打开应用程序菜单栏 |
| F11 | 应用全屏 |
| Super + W 或者 鼠标左上角触发角 | 打开所有工作区视图 |
| Super + E | 打开文件管理器 |
| Super + L | 锁屏 |
| Ctrl + Alt + Del | 打开提出菜单 |
| Super + D 或者 Ctrl + F12 | 显示桌面 |
| Alt + Tab | 切换下一个窗口 |
| Alt + Shift + Tab | 切换上一个窗口 |
| Ctrl + Super + 左右方向键 | 左右切换工作区 |
| Alt + Space | 打开 KRunner 搜索框 |
| Ctrl + Alt + T | 打开默认终端 |
| Super + 方向键 | 上下左右移动窗口 |
| Alt + F4 | 关闭当前窗口 |
| Super + Pgup | 最大化窗口 |
| Super + Pgdn | 最小化窗口 |
| Super + 加号 | 局部画面放大镜 |
| Super + 减号 | 局部画面缩小镜 |
| PrtSc | 调用 Spectacle 全屏截图 |
| Super + PrtSc | 调用 Spectacle 当前窗口截图 |
| Shift + Super + PrtSc | 调用 Spectacle 选区域截图 |

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%A7%A6%E6%8E%A7%E6%9D%BF "触控板")触控板
-----------------------------------------------------------------------------------

作为笔记本用户，触控板手势也是必不可少，下面是 KDE5 的触控板基本手势：

| 触控板手势 | 说明 |
| --- | --- |
| 双指轻点 | 右键 |
| 双指滚动 | 页面上下滚动 |
| 三指左右滚动 | 切换工作区 |
| 四指左右滚动 | 切换工作区 |
| 四指上滑 | 打开所有工作区视图 |
| 四指下滑 | 当开当前工作区所有窗口视图 |
| 四指捏合 | 打开所有工作区和窗口视图 |

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%9E%9C%E5%91%B3%E4%BC%98%E5%8C%96 "果味优化")果味优化
----------------------------------------------------------------------------------------------

如果你是一个 macOS 资深用户，可以将鼠标和触控板也逐步像 macOS 工作方式靠齐：

![Image 16](https://image.3001.net/images/20241002/1727830389_66fc99751f610dcdd4d29.png)

触控板设置细节如下：

![Image 17](https://image.3001.net/images/20241002/1727830452_66fc99b4a7ea29be65ae3.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%95%B0%E5%AD%97%E9%94%AE%E7%9B%98 "数字键盘")数字键盘
----------------------------------------------------------------------------------------------

如果你的笔记本设备自带数字小键盘的花、话，建议在设置里开启数字小键盘：

![Image 18](https://image.3001.net/images/20241007/1728306664_6703dde8a2ed6650ad7cb.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E9%94%AE%E7%9B%98%E5%93%8D%E5%BA%94 "键盘响应")键盘响应
----------------------------------------------------------------------------------------------

【设置】-【输入设备】-【键盘】可以根据自己的喜好提高一下键盘光标的移动速度，这样敲很长的命令的时候，使用方向键移动光标会更加丝滑：

![Image 19](https://image.3001.net/images/20241003/1727959332_66fe91242774f4ea8e1f1.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%BB%A3%E7%90%86%E5%B7%A5%E5%85%B7 "代理工具")代理工具
----------------------------------------------------------------------------------------------

工欲善其事，必先利其器。在国内的环境，要像优雅的配置你的 Linux 系统的话，代理工具是必不可少的，所有就在基本配置后直接开了各代理配置的专题。

「Watt Toolkit」是一个开源跨平台免费且多功能 Steam 工具箱。表面上是个游戏加速器，实际上也可以代理 Github 等国外常见的网站了，官网地址为：[https://steampp.net](https://steampp.net/)

官方的自动化安装脚本可以很方便的直接安装：

```
curl -sSL https://steampp.net/Install/Linux.sh | bash
```

选择默认的路径创建对应的快捷方式：

![Image 20](https://image.3001.net/images/20241003/1727923482_66fe051abd19fe28c6d30.png)

手动给我们的 hosts 文件添加权限：

```
sudo chmod a+w /etc/hosts
```

这样就可以直接启动加速了，原理是修改 hosts 文件：

![Image 21](https://image.3001.net/images/20241007/1728284990_6703893ee3c465a59c1f4.jpg)

但是实际上访问 Github 还是会发现提示证书相关存在问题：

![Image 22](https://image.3001.net/images/20241003/1727924076_66fe076cc5f470d843b5f.png)

我们参考官方的解决方法就可以了：[Linux 证书导入教程](https://steampp.net/liunxSetupCer)

找到证书本地文件夹的位置：

![Image 23](https://image.3001.net/images/20241003/1727924274_66fe0832064385bf2143c.png)

直接导入到火狐浏览器即可：

![Image 24](https://image.3001.net/images/20241003/1727924376_66fe0898c4c9638a3cb46.png)

这样即可使用火狐浏览器优雅的访问 Github 了吗：

![Image 25](https://image.3001.net/images/20241003/1727924428_66fe08cc26d243e76a1e5.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#Clash-Verge "Clash Verge")Clash Verge
-----------------------------------------------------------------------------------

官方项目地址：[https://github.com/clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)

[release](https://github.com/clash-verge-rev/clash-verge-rev/releases) 下载安装最新的 deb 包，使用 gdebi 安装即可：

```
# 直接使用 gdebi 安装
sudo gdebi clash-verge_1.7.7_amd64.deb 

# 但是提醒了
此软件包不可安装
Dependency is not satisfiable: libwebkit2gtk-4.0-37
```

根据[官方文档](https://www.clashverge.dev/faq/linux.html)发现，原来 Ubuntu 24.0 需要额外安装 `libwebkit2gtk` 和 `libjavascriptcoregtk` 依赖，根据架构下载对应版本并安装。

| 依赖 | 下载地址 |
| --- | --- |
| `libwebkit2gtk` | [libwebkit2gtk-4.0-37\_2.43.3-1\_amd64.deb](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/dependencies/libwebkit2gtk-4.0-37_2.43.3-1_amd64.deb) |
| `libjavascriptcoregtk` | [libjavascriptcoregtk-4.0-18\_2.43.3-1\_amd64.deb](https://github.com/clash-verge-rev/clash-verge-rev/releases/download/dependencies/libjavascriptcoregtk-4.0-18_2.43.3-1_amd64.deb) |

```
sudo gdebi libjavascriptcoregtk-4.0-18_2.43.3-1_amd64.deb
sudo gdebi libwebkit2gtk-4.0-37_2.43.3-1_amd64.deb 
```

后面如果遇到一些网络棘手的问题，可以尝试打开 Clash 的 Tun 模式，这样代理更简单透彻一点：

![Image 26](https://image.3001.net/images/20241003/1727935871_66fe357fe3526bf73c8f0.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#Shadowsocks-Electron "Shadowsocks Electron")Shadowsocks Electron
--------------------------------------------------------------------------------------------------------------

星火商店里面还保留着这个经典的老牌资源：spk://store/network/shadowsocks-electron

国光测试了 SSR 订阅链接正常解析工作，如果担心 Clash 暴露你的出口 IP 的话，大家不妨试试看这个：

![Image 27](https://image.3001.net/images/20241008/1728398812_670545dceca3b50af63ef.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#proxychains4 "proxychains4")proxychains4
--------------------------------------------------------------------------------------

Linux 下的命令行代理工具，也是内网渗透常用的工具：

```
sudo apt install proxychains4
```

配置文件路径为：

```
sudo vim /etc/proxychains4.conf
```

测试以下代理效果：

```
proxychains4 curl https://www.google.com
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%9E%9C%E5%91%B3%E7%BE%8E%E5%8C%96 "果味美化")果味美化
----------------------------------------------------------------------------------------------

[](https://www.sqlsec.com/2024/10/ubuntu.html#Kvantum "Kvantum")Kvantum
-----------------------------------------------------------------------

Kvantum 是一个高度可定制的开源主题引擎，专为基于 Qt 的应用程序设计。它允许用户通过 SVG（可缩放矢量图形）文件定义和应用复杂的主题，以改变应用程序的外观。

安装也比较简单：

```
sudo add-apt-repository ppa:papirus/papirus
sudo apt update
sudo apt install qt5-style-kvantum qt5-style-kvantum-l10n qt5-style-kvantum-themes
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#WhiteSur-kde "WhiteSur-kde")WhiteSur-kde
--------------------------------------------------------------------------------------

因为 macOS Big Sur 后的外观样式基本上差不多，所有我们这次借助的是 [WhiteSur-kde](https://github.com/vinceliuice/WhiteSur-kde) 项目，安装也很简单：

```
git clone https://github.com/vinceliuice/WhiteSur-kde
cd WhiteSur-kde
./install.sh
```

然后在设置里面选择我们刚刚安装好的主题即可，国光为自己更偏好于暗黑色的主题：

![Image 28](https://image.3001.net/images/20241003/1727970456_66febc98e57a92a3b161a.png)

这样基本上外观有个雏形了：

![Image 29](https://image.3001.net/images/20241007/1728284951_67038917d62e84c124210.jpg)

[](https://www.sqlsec.com/2024/10/ubuntu.html#WhiteSur-icon-theme "WhiteSur-icon-theme")WhiteSur-icon-theme
-----------------------------------------------------------------------------------------------------------

为了更逼真，我们需要安装 macOS 相关的图标主题，安装也比较简单：

```
git clone https://github.com/vinceliuice/WhiteSur-icon-theme
cd WhiteSur-icon-theme
./install.sh 
```

配置完成后在设置里面启用这个图标，这样整体效果已经很接近 macOS 了：

![Image 30](https://image.3001.net/images/20241007/1728284936_67038908156741874824a.jpg)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E9%BC%A0%E6%A0%87%E5%85%89%E6%A0%87%E6%A0%B7%E5%BC%8F "鼠标光标样式")鼠标光标样式
--------------------------------------------------------------------------------------------------------------------

鼠标光标样式国光我比较推荐：[Capitaine Cursors](https://store.kde.org/p/1148692)，其中 r4 版本是对高分辨率屏幕和 KDE 比较友好，所以为最终选择的是 `capitaine-cursors-light-r4.tar.gz` 版本的光标样式：

![Image 31](https://image.3001.net/images/20241004/1728007116_66ff4bccf36b3e3929a69.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#Latte-Dock "Latte Dock")Latte Dock
--------------------------------------------------------------------------------

macOS 另一个外观特征就是 Dock 了，好在 KDE5 下有大名鼎鼎的 [Latte Dock](https://github.com/KDE/latte-dock) 可以使用，我们安装也比较简单：

```
sudo apt install latte-dock 
```

但是安装好直接使用的话，各种细节还是差点意思：

![Image 32](https://image.3001.net/images/20241004/1728007660_66ff4decbad78f39be84b.png)

然后右键 Latte Dock，选择【配置 Latte Dock】- 【布局编辑器】找到右下角【导入】-【从 KDE 在线商店导入】，本次使用的是和我们主题配套的 WhiteSur latte 外观样式：

![Image 33](https://image.3001.net/images/20241004/1728009141_66ff53b5d560504794822.png)

整体的效果如下：

![Image 34](https://image.3001.net/images/20241004/1728009077_66ff5375c42ded178a05a.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%8C%82%E4%BB%B6%E6%8E%A8%E8%8D%90 "挂件推荐")挂件推荐
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%8C%82%E4%BB%B6%E6%A6%82%E8%A7%88 "挂件概览")挂件概览

| 挂件名称 | 挂件说明 |
| --- | --- |
| [Kpple Menu](https://store.kde.org/p/1384156) | 仿 macOS 的左上角下拉菜单 |
| [Window Title Applet](https://store.kde.org/p/1274218) | 菜单栏显示窗口标题 |
| [Control Centre](https://github.com/Prayag2/kde_controlcentre) | 仿 macOS 控制中心 |
| [Launchpad Plasma](https://store.kde.org/p/1364064/) | 仿 macOS 程序坞 |
| [CatWalk](https://store.kde.org/p/2055225) | 猫猫跑步展示 CPU 的负载状态 |
| [Power Monitor](https://store.kde.org/p/1466838) | 显示笔记本的电池的功耗 |
| [Translator](https://store.kde.org/p/1395666) | 菜单栏翻译插件 |
| [Fokus](https://store.kde.org/p/1308861) | 菜单栏番茄钟插件 |
| [Thermal Monitor](https://store.kde.org/p/2070765) | 菜单栏温度监控 |
| [Resources Monitor - fork](https://store.kde.org/p/1527636) | 数据可视化展示常用的性能数据 |
| [Netspeed Widget](https://store.kde.org/p/998895) | 菜单栏网络数据监控显示 |
| [Latte SideBar Button](https://store.kde.org/p/1365044) | 召唤调出 latte dock 的侧边栏 |
| [HTML Clock](https://store.kde.org/p/1473016) | HTML 风格的简约时钟 |

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%8C%82%E4%BB%B6%E4%BC%98%E5%8C%96 "挂件优化")挂件优化

*   **Window Title Applet**

下面是更接近 macOS 的设置细节：

![Image 35](https://image.3001.net/images/20241004/1728010003_66ff57133487f7cf77580.png)

*   **Control Centre**

从 Github 下载 [https://github.com/Prayag2/kde\_controlcentre/releases/download/0.1.0/kde\_controlcentre0.1.0.tar.gz](https://github.com/Prayag2/kde_controlcentre/releases/download/0.1.0/kde_controlcentre0.1.0.tar.gz) 文件，然后使用命令行手动安装：

```
kpackagetool5 -i kde_controlcentre0.1.0.tar.gz 
```

*   **CatWalk**

因为已经有其他的插件可以显示 CPU 占用率了，为了界面的简洁，我这里只推荐使用猫猫图标：

![Image 36](https://image.3001.net/images/20241004/1728055531_670008ebc0946262ed298.png)

*   **Resources Monitor - fork**

默认的这个可视化性能监控的字体太小了，建议我们自己单独设置大一点：

![Image 37](https://image.3001.net/images/20241006/1728194985_670229a94a61dd370d9ad.png)

*   **Netspeed Widget**

![Image 38](https://image.3001.net/images/20241006/1728196465_67022f7194aff8db4268b.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%8F%B3%E4%BE%A7%E9%9D%A2%E6%9D%BF "右侧面板")右侧面板
----------------------------------------------------------------------------------------------

我们借助 Latte Dock 可以实现 macOS 侧边栏的类似效果。首先需要确保安装好【[Latte SideBar Button](https://store.kde.org/p/1365044)】插件，这样才可以调出侧边栏。

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%B7%BB%E5%8A%A0%E9%9D%A2%E6%9D%BF "添加面板")添加面板

首先编辑我们当前 Latte Dock 的配置，手动在【右侧】添加一个【两端对齐】的【空面板】：

![Image 39](https://image.3001.net/images/20241006/1728198740_6702385494495b62bb1c4.png)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E9%9D%A2%E6%9D%BF%E8%A1%8C%E4%B8%BA "面板行为")面板行为

鼠标找到我们刚刚添加的面板，右键【编辑面板】，类型保持为默认的【面板】然后先点亮【吸附于顶部】和【吸附于底部】，然后选择【自动隐藏侧边栏】，根据需要勾选一些自己喜好的选项：

![Image 40](https://image.3001.net/images/20241007/1728284909_670388eda14822923d796.jpg)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E9%9D%A2%E6%9D%BF%E5%A4%96%E8%A7%82 "面板外观")面板外观

这块国光的调教参数如下：

![Image 41](https://image.3001.net/images/20241007/1728284893_670388ddc6682cf5fc367.jpg)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E9%9D%A2%E6%9D%BF%E7%89%B9%E6%95%88 "面板特效")面板特效

面板特效建议安装【Dash To Panel】任务指示装饰：

![Image 42](https://image.3001.net/images/20241007/1728284878_670388ce1495c44508e67.jpg)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E9%9D%A2%E6%9D%BF%E6%8C%82%E4%BB%B6 "面板挂件")面板挂件

经过大量测试， 最终国光侧边面板布局顺序从上到下为：[HTML Clock](https://store.kde.org/p/1473016) - 日历 - 性能监控数据

首先添加【[HTML Clock](https://store.kde.org/p/1473016)】挂件，然后设置为图上显示比较齐全的布局，然后【启用此小程序的着色】：

![Image 43: image-20241006153622801](https://www.sqlsec.com/imgs/image-20241006153622801.png)

接着下面我们添加一个系统自带的日历插件，日历不建议开启【启用此小程序的着色】：

![Image 44](https://image.3001.net/images/20241007/1728284861_670388bdae427f8da6165.jpg)

最后下面添加小程序分组：

![Image 45](https://image.3001.net/images/20241006/1728200626_67023fb2b8d653b316987.png)

国光这里是分别在小程序分组里面拖入添加了：总 CPU 使用情况、内存使用情况和网络速度，不建议开启【启用此小程序的着色】，其他细节分别都是【折线图】，不勾选【显示标题】具体的传感器大家也可以根据自己的喜好来。

*   **CPU 负载**

![Image 46](https://image.3001.net/images/20241006/1728201924_670244c4d6b19e28f28e5.png)

*   **内存使用**

![Image 47](https://image.3001.net/images/20241006/1728203124_67024974a048b5c57b359.png)

*   **网络监控**

![Image 48](https://image.3001.net/images/20241006/1728203271_67024a073a93bb5491c43.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%95%B4%E4%BD%93%E6%95%88%E6%9E%9C "整体效果")整体效果
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#Kvantum-1 "Kvantum")Kvantum

首先我们在应用程序风格里面选择【kvantum】：

![Image 49](https://image.3001.net/images/20241004/1728052795_66fffe3be00f313e538c3.png)

接着打开【Kvantum管理器】先通过【变更/删除主题】选择 macOS 风格的【WhiteSurDark】主题，然后点击【应用此主题】：

![Image 50](https://image.3001.net/images/20241004/1728051910_66fffac6ec62bbf365668.png)

接着在【配置当前主题】里能开的特效基本上都开满：

![Image 51](https://image.3001.net/images/20241004/1728052676_66fffdc463c88b12fecb9.png)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%B8%83%E5%B1%80%E6%8E%92%E5%88%97 "布局排列")布局排列

顶部菜单栏的整体布局从左到右的布局排列如下：

[Kpple Menu](https://store.kde.org/p/1384156) - [Window Title](https://store.kde.org/p/1274218) - 全局菜单 - 面板间隙 - 虚拟桌面切换器 - [Fokus](https://store.kde.org/p/1308861) - [Translator](https://store.kde.org/p/1395666) - [CatWalk](https://store.kde.org/p/2055225) - [Thermal Monitor](https://store.kde.org/p/2070765) - [Power Monitor](https://store.kde.org/p/1466838) - [Resources Monitor - fork](https://store.kde.org/p/1527636) - 网络速度 - [Netspeed Widget](https://store.kde.org/p/998895) - 系统托盘 - 剪贴板 - 音频音量 - 蓝牙 - 网络 - 电池和亮度 - 搜索 - [Control Centre](https://github.com/Prayag2/kde_controlcentre) - 数字时钟 - [Ltte SideBar Button](https://store.kde.org/p/1365044)

系统托盘国光我建议，能隐藏的都隐藏，我们需要什么可以单独添加到菜单栏里面，系统托盘就应该专职做好托盘相关的工作：

![Image 52](https://image.3001.net/images/20241005/1728059516_6700187ca383264464cc1.png)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%A4%96%E8%A7%82%E7%BB%86%E8%8A%82 "外观细节")外观细节

*   【全局主题】-【WhiteSur-dark】
*   【全局主题】-【应用程序风格】-【kvantum】
*   【全局主题】-【Plasma视觉风格】-【WhiteSur暗黑苹果】
*   【全局主题】-【窗口装饰元素】-【[Sweet-Dark-transparent](https://store.kde.org/p/1286856)】
*   【全局主题】-【颜色】-【WhiteSurDark】
*   【全局主题】-【图标】-【WhiteSu-dark】
*   【全局主题】-【光标】-【Capitaine Cursors Light】
*   【全局主题】-【欢迎屏幕】-【Orchis-dark】
*   【全局主题】-【启动屏幕】-【apple-mac-plymouth】

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%A1%8C%E9%9D%A2%E7%89%B9%E6%95%88 "桌面特效")桌面特效

这个国光为建议，只要都可以接受，这些能开的都全开了：

![Image 53](https://image.3001.net/images/20241007/1728284828_6703889c53a2d33f658e5.jpg)

其中窗口透明度要单独设置一下，这样整体虚化的颜值会更高一点：

![Image 54](https://image.3001.net/images/20241004/1728055169_67000781ad56daa568b5a.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E7%B3%BB%E7%BB%9F%E5%A2%9E%E5%BC%BA "系统增强")系统增强
----------------------------------------------------------------------------------------------

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E9%A9%B1%E5%8A%A8%E5%AE%8C%E5%96%84 "驱动完善")驱动完善
----------------------------------------------------------------------------------------------

默认情况下我这个笔记本（机械革命 无界 15X ）的在 Linux 下是没有这个国产以太网卡驱动的，好在官网提供了驱动的下载链接：

[以太网网卡芯片-裕太微电子股份有限公司](https://www.motor-comm.com/product/ethernet-control-chip)

![Image 55](https://image.3001.net/images/20241007/1728284807_67038887c946b2107157a.jpg)

驱动安装很简单，安装好编译驱动的依赖，然后直接执行脚本就行了：

```
# 切换 root 用户
sudo -i

# 执行驱动安装脚本
./yt_nic_install.sh
```

![Image 56](https://image.3001.net/images/20241007/1728284788_670388747875c8f0e7b38.jpg)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%88%AA%E5%9B%BE%E5%A2%9E%E5%BC%BA "截图增强")截图增强
----------------------------------------------------------------------------------------------

Kubuntu 自带的 Spectacle 截图也还算不错，但是还算没有 [Snipaste](https://zh.snipaste.com/) 强大和丝滑，唯一要注意的就是这个截图软件自带的快捷键很多和 KDE 桌面的快捷键冲突了，所以需要自己设置来避开：

![Image 57](https://image.3001.net/images/20241007/1728284771_6703886302c93a21582e6.jpg)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E9%BC%A0%E6%A0%87%E5%A2%9E%E5%BC%BA "鼠标增强")鼠标增强
----------------------------------------------------------------------------------------------

在 Discover 商店里下载安装 【Piper】可以很方便的自定义管理我们的鼠标，这样侧键就可以完全利用起来了：

![Image 58](https://image.3001.net/images/20241007/1728284750_6703884e4b4cfedd52c8a.jpg)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%88%86%E7%B1%BB%E5%88%86%E7%BA%A7 "分类分级")分类分级
----------------------------------------------------------------------------------------------

KDE 自带的应用分类不满足国庆，建议大家重新分类，我们可以借助 KDE 自带的【KDE 菜单编辑器】来实现应用的分类：

![Image 59](https://image.3001.net/images/20241007/1728284731_6703883bf0ba7e979ee7c.jpg)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%B5%81%E9%87%8F%E7%9B%91%E6%8E%A7 "流量监控")流量监控
----------------------------------------------------------------------------------------------

[OpenSnitch](https://github.com/evilsocket/opensnitch) 是一个 GNU/Linux 交互式应用程序防火墙，其灵感来自 Little Snitch。

```
# 安装守护进程
sudo gdebi opensnitch_1.6.6-1_amd64.deb

# 守护进程设置开机自启
sudo systemctl enable --now opensnitch.service

# 安装图形化界面
sudo gdebi python3-opensnitch-ui_1.6.6-1_all.deb                     
```

这样所有应用程序流量你都可以了如指掌：

![Image 60](https://image.3001.net/images/20241009/1728435696_6705d5f0e19d42da3ba04.png)

这种感觉才是真正 Linux 的感觉，所有流量我全都要搞清楚：

![Image 61](https://image.3001.net/images/20241009/1728435896_6705d6b8335f86667035f.jpg)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%96%87%E4%BB%B6%E4%BC%A0%E9%80%81 "文件传送")文件传送
----------------------------------------------------------------------------------------------

不必羡慕苹果的隔空投送生态，借助开源项目 [localsend](https://github.com/localsend/localsend) 我们也可以轻松实现，安装很简单，[官网直接下载](https://localsend.org/zh-CN/download?os=linux) deb 安装包即可：

```
sudo gdebi LocalSend-1.15.4-linux-x86-64.deb
```

![Image 62](https://image.3001.net/images/20241011/1728604270_6708686e402a63c4ff57c.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#Code-Server "Code Server")Code Server
-----------------------------------------------------------------------------------

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B "安装教程")安装教程
----------------------------------------------------------------------------------------------

官方项目的 [Release](https://github.com/coder/code-server/releases) 直接下载最新的 deb 包安装即可：

```
sudo gdebi code-server_4.93.1_amd64.deb
```

默认的配置存放在：

```
cat ~/.config/code-server/config.yaml
```

直接启动即可运行 Code Server：

```
code-server
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#CrossOver "CrossOver")CrossOver
-----------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%AE%89%E8%A3%85%E7%AE%80%E4%BB%8B "安装简介")安装简介

如果你真的打算使用 Linux 作为主力系统，且又不想开虚拟机运行一些必要的 exe，这个时候可以了解一下 [CrossOver](https://www.codeweavers.com/)，默认会有十几天试用期，足够大家体验了：

![Image 63](https://image.3001.net/images/20241011/1728655330_67092fe22046bc720383d.png)

如果真的用的习惯的话，可以考虑咸鱼上花 80多元买个正版激活码，如果买了激活码还是无法提示注册失败等原因的话，我们可以像下面这样手动去官网下载许可证文件，然后放到 CrossOver 下面这个目录即可：

```
/opt/cxoffice/etc
```

![Image 64](https://image.3001.net/images/20241011/1728655529_670930a980333a3aafafd.jpg)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%BD%AF%E4%BB%B6%E5%AF%B9%E6%AF%94 "软件对比")软件对比

下面是通过 CrossOver 运行的 Audacity 和官方打包的 AppImage 版本对比，发现这个付费的 CrossOver 还是很值得的：

![Image 65](https://image.3001.net/images/20241011/1728656174_6709332e1360487da7bf0.png)

左边是付费的 CrossOver ，右边为官方打包的 AppImage 版本 ，可以看出来 CrossOver 的体验还是和 Windows 无限接近的，更加细腻。

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%BD%AF%E4%BB%B6%E6%95%88%E6%9E%9C "软件效果")软件效果
----------------------------------------------------------------------------------------------

下面列举一些在 CrossOver 下工作良好的软件截图：

*   **网易云音乐**

![Image 66](https://image.3001.net/images/20241012/1728699930_6709de1a5af8581afa492.jpg)

*   **Notepad++**

![Image 67](https://image.3001.net/images/20241012/1728714741_670a17f58596c2387e153.png)

*   **ResourceHacker**

![Image 68](https://image.3001.net/images/20241012/1728715193_670a19b9ee4b49c23b7b9.png)

*   ### [](https://www.sqlsec.com/2024/10/ubuntu.html#Firefox-%E6%B8%97%E9%80%8F%E4%BE%BF%E6%90%BA%E7%89%88 "Firefox 渗透便携版")Firefox 渗透便携版
    

![Image 69](https://image.3001.net/images/20241012/1728715363_670a1a634b8dcc69abe01.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%91%BD%E4%BB%A4%E7%8E%AF%E5%A2%83 "命令环境")命令环境
----------------------------------------------------------------------------------------------

默认的 bash shell 太素来，所有建议使用 zsh shell 环境，现在的 Kali Linux 默认 zsh shell 环境了，确实 zsh 支持的插件更丰富，更可以提高我们命令输入的效率。

```
# 安装 zsh
sudo apt install zsh

# 更改默认shell为zsh
chsh -s /bin/zsh

# 安装 oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

注销或者重启后会生效 zsh 为默认的 shell

zsh 的经典插件推荐安装：

```
# 目录快速调整切换
sudo apt install autojump

# 自动建议提示接下来可能要输入的命令
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions

# 命令语法检测
git clone https://github.com/zsh-users/zsh-syntax-highlighting $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```

在 `~/.zshrc` 中配置启用这些插件：

```
plugins=(git autojump zsh-autosuggestions zsh-syntax-highlighting)
```

其他 `~/.zshrc` 功能配置：

```
# 关掉 URL 反斜杠转义
DISABLE_MAGIC_FUNCTIONS="true"

# 禁用 on my zsh 自动更新
zstyle ':omz:update' mode disabled
```

细心的小伙伴肯定会发现我们切换到 root 发现依然是 bash shell，这对于强迫症来说就有点难受了。

我们也来给 root 用户配置一下 zsh shell，首先手动在 root 用户下将 zsh 设置为默认的 shell：

```
# 切换 root
sudo -i

# 设置 root 用户默认 shell 为 zsh
chsh --shell /bin/zsh
```

接着切换到普通用户，使用软连接，链接 我们普通用户 home下的的 zsh 配置：

```
sudo ln -s $HOME/.oh-my-zsh /root/.oh-my-zsh
sudo ln -s $HOME/.zshrc /root/.zshrc
```

基本上没问题了，但是依然提示了一些警告信息：

![Image 70](https://image.3001.net/images/20241007/1728281440_67037b60ebc4a7a2b6f89.png)

在 `~/.zshrc` 中添加配置即可关闭告警：

```
ZSH_DISABLE_COMPFIX="true"
```

这样我们的 root 用户也可以丝滑的使用 zsh 啦：

![Image 71](https://image.3001.net/images/20241007/1728281557_67037bd576245f5a5313c.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%91%BD%E4%BB%A4%E7%BE%8E%E5%8C%96 "命令美化")命令美化
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%AD%97%E4%BD%93%E5%AE%89%E8%A3%85 "字体安装")字体安装

为了下面我们花里胡哨的配置下的图标都正常显示，我们这里建议先提前把我们的终端配置好字体。

带图标字体下载地址：[Nerd Fonts - Iconic font aggregator, glyphs/icons collection, & fonts patcher](https://www.nerdfonts.com/font-downloads)

![Image 72](https://image.3001.net/images/20241007/1728284697_6703881999db07373eb25.jpg)

其实下载第一个【0xProtoNerdFont 】字体效果就已经挺不错的了，当然大家可以自己尝试去体验看看更多其他的字体。

字体安装也比较简单，直接右键点击【安装】，安装为【系统字体】即可：

![Image 73](https://image.3001.net/images/20241007/1728284674_67038802d51cf9c56e20a.jpg)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E7%BB%88%E7%AB%AF%E9%85%8D%E7%BD%AE "终端配置")终端配置

内置的方案是只读的不可编辑，所有我们需要自己创建一个自己的配置方案：

![Image 74](https://image.3001.net/images/20241007/1728284649_670387e9d54e90d774d9a.jpg)

大家根据自己的喜好配置来就行了，我这里只强调配置一下我们上面刚刚安装好的字体：

![Image 75](https://image.3001.net/images/20241007/1728283853_670384cd03fbc989d1e97.jpg)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%8A%B1%E9%87%8C%E8%83%A1%E5%93%A8 "花里胡哨")花里胡哨

本次使用我之前的项目来配置：[https://github.com/sqlsec/fastfetch](https://github.com/sqlsec/fastfetch)

Fastfetch 是一个类似 [neofetch](https://github.com/dylanaraps/neofetch) 的工具，用于获取系统信息并漂亮地显示它。它主要用 C 语言编写，并考虑了性能和可定制性。本项目是一个 Fastfetch 轮子，主要是集成了宝可梦显示和其他系列的恶搞图片，目前只在 Linux 和 macOS 平台下测试过。

首先安装 Fastfetch

```
sudo add-apt-repository ppa:zhangsongcui3371/fastfetch
sudo apt update
sudo apt install fastfetch
```

然后安装终端下的宝可梦：

```
git clone https://gitlab.com/phoneybadger/pokemon-colorscripts.git
cd pokemon-colorscripts
sudo ./install.sh

# 测试是否正常工作
pokemon-colorscripts -r --no-title
```

导入我们的配置文件：

```
# 备份原有的配置文件（执行失败的话也没关系 说明没默认配置）
mv $HOME/.config/fastfetch $HOME/.config/fastfetch.bak

# 进入 .config 目录
cd $HOME/.config

# 下载并解压然后删除
wget https://github.com/sqlsec/fastfetch/releases/download/v0.1/fastfetch-for-Linux.zip
unzip fastfetch-for-Linux.zip && rm fastfetch-for-Linux.zip
```

最终花里胡哨的 fastfetch 效果如下：

![Image 76](https://image.3001.net/images/20241007/1728284423_670387073223a2aa8613c.jpg)

如果需要 root 用户也使用花里胡哨的 fastfetch 的话，可用使用软连接，链接 我们普通用户 home下的的对应文件件夹配置：

```
sudo ln -s $HOME/.config/fastfetch  /root/.config/fastfetch
```

为了每次打开 zsh 都有不一样的随即宝可梦出现，我们可以手动追加 zsh 配置：

```
echo "pokemon-colorscripts -r --no-title" >> ~/.zshrc
```

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%B8%BB%E9%A2%98%E7%BE%8E%E5%8C%96 "主题美化")主题美化

#### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%B8%8B%E8%BD%BD%E5%AE%89%E8%A3%85%E4%B8%BB%E9%A2%98 "下载安装主题")下载安装主题

本次使用的大名鼎鼎的 powerlevel10k 主题，首先将主题 git clone 到我们的主题目录下：

```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

在 `~/.zshrc` 中配置启用新的主题：

```
ZSH_THEME="powerlevel10k/powerlevel10k"
```

#### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%B8%BB%E9%A2%98%E9%85%8D%E7%BD%AE%E5%90%91%E5%AF%BC "主题配置向导")主题配置向导

重载 zsh 终端会自动进入 powerlevel10k 主题的配置向导：

```
zsh
```

根据向导的提示回答 y 或者 n 即可，下面是向导问的几个问题：

```
# 这看起来像菱形吗？
Does this look like a diamond (rotated square)?

# 这看起来像一个锁吗？
Does this look like a lock?

# 这看起来像一个向上的箭头吗？
Does this look like an upwards arrow?

# 这些图标都正常显示放在 x 之间，没有重叠吗？
Do all these icons fit between the crosses?
```

问完问题后选择终端前面的提示样式，国光我这里肯定选择了最酷炫的 Rainbow 样式：

![Image 77](https://image.3001.net/images/20240911/1726012803_66e0dd83710d11cd53dc1.png)

编码这块推荐使用更标准先进的 Unicode 编码：

![Image 78](https://image.3001.net/images/20240911/1726013006_66e0de4e1055993f8a9f7.png)

其他的设置细节根据大家自己的喜好来就行，国光我就不一一列举了：

![Image 79](https://image.3001.net/images/20240911/1726014778_66e0e53a2b4dbbbc017d4.png)

如果期间又不小心配置错误的话，可以运行：

```
p10k configure
```

重新走一步配置向导。

#### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%A7%A3%E5%86%B3%E5%91%8A%E8%AD%A6%E9%97%AE%E9%A2%98 "解决告警问题")解决告警问题

配置完主题后重新加载 zsh 会发现有告警信息：

![Image 80](https://image.3001.net/images/20240911/1726023084_66e105aca679f4b62d3ac.png)

发现原来是我们这一步配置有问题：

![Image 81](https://image.3001.net/images/20240911/1726023524_66e1076486f554cd42257.png)

我们手动编辑 `.p10k.zsh` 配置文件：

![Image 82](https://image.3001.net/images/20240911/1726023804_66e1087c78331dcfbcdff.png)

最终我们的命令行终端效果如下：

![Image 83](https://image.3001.net/images/20241007/1728285803_67038c6b191a2bb94c9cc.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%BF%9C%E7%A8%8B%E7%8E%AF%E5%A2%83 "远程环境")远程环境
----------------------------------------------------------------------------------------------

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E7%A9%BF%E9%80%8F%E5%B7%A5%E5%85%B7 "穿透工具")穿透工具
----------------------------------------------------------------------------------------------

本章节主要是借助 ZeroTier 来进行穿透环境搭建，属于国光我的个人生产力搭配，网友们可以了解一下，不一定非要照抄作业。

首先我们需要借助 [xubiaolin/docker-zerotier-planet: 一分钟私有部署zerotier-planet服务 (github.com)](https://github.com/xubiaolin/docker-zerotier-planet) 项目来搭建自己的 ZeroTier 中转服务器，每个自己的私服都有自己对应的 planet 文件，我们使用不同的 planet 文件即可连接不同的 ZeroTier 服务。

首先我们本地需要安装好官方的 ZeroTier 客户端：

```
curl -s https://install.zerotier.com | sudo bash
```

安装完成后，使用直接设置开机自启然后加入网络即可：

```
# 设置 zerotier 开机自启
systemctl enable zerotier-one.service

# 备份官方的 planet 文件
sudo mv /var/lib/zerotier-one/planet /var/lib/zerotier-one/planet.bak

# 下载替换你的 plant
xxxxxxx 此处省略 xxxxxxxx

# 启动 zerotier 服务
systemctl start zerotier-one.service
```

另一个客户端我们使用 Docker 版本的：

```
docker run --name zerotier-one --device=/dev/net/tun --net=host --cap-add=NET_ADMIN --cap-add=SYS_ADMIN -v /home/x-x/Documents/Tools/zerotier:/var/lib/zerotier-one --restart=always -d zerotier/zerotier
```

其中 `/home/x-x/Tools/zerotier/` 设置为你自己的本地文件夹。

因为两个 ZeroTier 的客户端端口会有冲突，必定只能运行 1 个，所以我们需要手动修改 Docker 的端口为其他端口：

```
vim /var/lib/zerotier-one/local.conf
```

这里国光我修改为了 9333 端口：

![Image 84](https://image.3001.net/images/20240923/1727055472_66f0c670d0f6410f0d523.png)

设置完成后就可以同时使用 2 个 ZeroTier 的不同 planet 了 ：

![Image 85](https://image.3001.net/images/20240923/1727055562_66f0c6caaa3a1fbba0f9d.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#SSH-Server "SSH Server")SSH Server
--------------------------------------------------------------------------------

Kubuntu 默认只有 SSH 客户端，所有想要其他设备远程我们自己的话，还得安装 SSH 服务端：

```
# 安装 SSH Server
sudo apt install openssh-server

# SSH 服务开机自启
sudo systemctl enable ssh.service 
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83 "虚拟环境")虚拟环境
----------------------------------------------------------------------------------------------

[](https://www.sqlsec.com/2024/10/ubuntu.html#QEMU-KVM "QEMU-KVM")QEMU-KVM
--------------------------------------------------------------------------

QEMU 是 Linux 下原生的虚拟化方案，体验还是非常非常丝滑的，Ubuntu 安装的话也比较简单：

```
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients cinst bridge-utils virt-manager virt-viewer
```

开机自启和启动 libvirt 服务：

```
sudo systemctl enable libvirtd
sudo systemctl start libvirtd
```

当前用户添加到 `libvirt` 和 `kvm` 组，以便不需要使用 root 权限进行管理：

```
sudo usermod -aG libvirt $(whoami)
sudo usermod -aG kvm $(whoami)
```

重启系统生效功能更改。

使用 `virt-manager` 打开虚拟系统管理器，图形化界面操作还是比较简单的 ，我们可以创建一个自己的 Windows 虚拟机。

![Image 86](https://image.3001.net/images/20241007/1728293237_6703a975efd3d19a832b4.png)

手动添加一个 SATA CDROM 的设备类型，源路径指向我们的系统镜像：

![Image 87](https://image.3001.net/images/20241007/1728293812_6703abb4ccf6906a27921.png)

然后引导菜单里面勾选我们刚刚添加的 CD 光盘镜像，再次开机即可直接安装系统了：

![Image 88: image-20241007173602755](https://image.3001.net/images/20241007/1728293764_6703ab846a75273092d78.png)

为了提高虚拟机的性能和使用体验，我们还需要安装 virtio 驱动（类似于 Vmware 的虚拟机增强工具）

官方的 virtio 下载地址为：[https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/](https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/)

我们选择最新版本的 virtio-win.iso 下载，然后挂载到虚拟机里面运行【virtio-win-guest-tools.exe】安装即可：

![Image 89](https://image.3001.net/images/20241007/1728301194_6703c88a7072bd7dd62a7.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#Docker "Docker")Docker
--------------------------------------------------------------------

Ubuntu 使用官方自动安装脚本可以很方便的安装 Docker：

```
# 自动安装脚本
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

# 将当前用户添加到 docker 用户组里
sudo groupadd docker
sudo usermod -aG docker `whoami`

# 重启生效
reboot

# 检验版本输出是否正常
docker version
```

Docker 安装完成后那么开始准备安装 Docker Compose 了，首先去[官方项目](https://github.com/docker/compose/releases)查看最新的稳定版为多少，然后手动下载最新版本 赋予执行权限即可：

```
# 下载我写这篇文章的最新版本 2.29.7
sudo curl -L "https://github.com/docker/compose/releases/download/v2.29.7/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 赋予执行权限
sudo chmod +x /usr/local/bin/docker-compose

# 查看 Docker-compose 版本
$ docker-compose version
Docker Compose version v2.29.7
```

完整完成后配置一下 Docker 的开机自启：

```
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

Docker 其实挺简单的，国光我之前也做了一些笔记，比如：[Docker温故知新](https://www.sqlsec.com/2019/10/docker2.html)，其实 Docker 这块更多的还得靠自己去实操，成长会更快！

[](https://www.sqlsec.com/2024/10/ubuntu.html#Waydroid "Waydroid")Waydroid
--------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B-1 "安装教程")安装教程

[Waydroid](https://waydro.id/) 使用 Linux 命名空间（user、pid、uts、net、mount、ipc）在容器中运行完整的 Android 系统，并在任何基于 GNU/Linux 的平台（arm、arm64、x86 x86\_64）上提供 Android 应用程序。

```
# 导入 repo 源头、
curl https://repo.waydro.id | sudo bash

# 安装 waydroid
sudo apt install waydroid -y
```

默认点击下一步，在点击 Download 前建议 Clash 开启 TUN 模式下载安装：

![Image 90](https://image.3001.net/images/20241008/1728402314_6705538a92ed22b17b1a1.png)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%98%BE%E7%A4%BA%E7%95%8C%E9%9D%A2 "显示界面")显示界面

默认显示的界面有点胖胖的，很不舒服，我们可以修改 hyprland 的配置文件来自定义启动界面大小：

```
waydroid prop set persist.waydroid.width 480
waydroid prop set persist.waydroid.height 900
```

重启 waydroid 生效：

```
waydroid session stop
```

如果要移动窗口，使用 Super + 鼠标来移动。

### [](https://www.sqlsec.com/2024/10/ubuntu.html#ARM-%E8%BD%AC%E8%AF%91 "ARM 转译")ARM 转译

这个模拟器虽然很丝滑，但是默认情况下是没法跑 ARM APK 的，而国内很少有原生的 x86 APP，所以还是有必要安装一下 ARM 相关的转译的依赖的。

```
# 下载拷贝项目
git clone https://github.com/casualsnek/waydroid_script
cd waydroid_script

# 使用 3.8.20 的 pyenv 虚拟环境
pyenv local 3.8.20

# 更新一下最新的 pip
python -m pip install --upgrade pip -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple 

# 安装脚本相关的依赖
python -m pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

运行脚本：

```
sudo -i
python main.py
```

命令行图形化界面我的选项供大家参考：

![Image 91](https://image.3001.net/images/20241009/1728404129_67055aa1e8b28a6951b55.png)

这样就可以正常打开我们常用的 APP 了：

![Image 92](https://image.3001.net/images/20240918/1726635632_66ea5e70e6ff8469ae881.jpg)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%9F%BA%E6%9C%AC%E7%94%A8%E6%B3%95 "基本用法")基本用法

```
# 当前会话关机
waydroid session stop

# 重启 waydroid 服务
sudo systemctl restart waydroid-container.service 
```

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BC%80%E5%8F%91%E6%B5%8B%E8%AF%95 "开发测试")开发测试

```
# 安装 adb 开发工具
apt install adb

# 安装 apk 包
waydroid app install  /xxx/xxx/xx.apk

# adb 使用 IP 连接 （关于本机查看）
adb connect 192.168.x.x:5555
```

手动安装 BP 证书：

```
# 对 BP 证书进行转换
openssl x509 -inform DER -in cacert.der -out cacert.pem

# 计算 BP 证书 hash
cert_hash=$(openssl x509 -subject_hash_old -in cacert.pem | head -1)

# 创建证书文件夹
sudo mkdir -p /var/lib/waydroid/overlay/system/etc/security/cacerts/

# 导入证书
sudo cp cacert.pem /var/lib/waydroid/overlay/system/etc/security/cacerts/${cert_hash}.0
```

或者借助 [waydroid\_script](https://github.com/casualsnek/waydroid_script) 项目，直接导入证书也可以：

```
sudo python3 main.py install mitm --ca-cert cacert.pem
```

接着手动将模拟器设置本地的代理：

```
adb shell settings put global http_proxy "ip:port" 
```

如果取消代理则使用下面命令：

```
adb shell settings delete global global_http_proxy_host
adb shell settings delete global global_http_proxy_port
adb shell settings delete global http_proxy
```

这样就可以正常抓包测试了。

[](https://www.sqlsec.com/2024/10/ubuntu.html#Genymotion "Genymotion")Genymotion
--------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%9F%BA%E6%9C%AC%E5%AE%89%E8%A3%85 "基本安装")基本安装

Genymotion 下载安装很简单，直接[官网下载](https://www.genymotion.com/product-desktop/download/)对应的安装包即可（默认安装在当前目录，安装前提前准备好目录）：

```
chmod +x genymotion-3.7.1-linux_x64.bin    
./genymotion-3.7.1-linux_x64.bin 
```

记得注册一下对应的账号，虽然是免费版本的：

![Image 93](https://image.3001.net/images/20241011/1728603102_670863de9543d6dd4b36d.png)

表面上不支持开启 root 权限：

![Image 94](https://image.3001.net/images/20240926/1727352565_66f54ef5905c1ee800d5c.png)

实际上手动进 adb 发现还是可以直接切换到 root 用户的：

![Image 95](https://image.3001.net/images/20240926/1727352696_66f54f78b651fe7ecae86.png)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#ARM-%E8%BD%AC%E8%AF%91-1 "ARM 转译")ARM 转译

这个模拟器虽然很丝滑，但是默认情况下是没法跑 ARM APK 的，而国内很少有原生的 x86 APP，所以还是有必要安装一下 ARM 相关的转译的依赖的。

本次转译借助：[https://github.com/niizam/Genymotion\_A11\_libhoudini](https://github.com/niizam/Genymotion_A11_libhoudini) 项目来实现，下面是一些操作细节：

打开 Android 11 模拟器，下面直接在命令行下操作

```
# 进入 adb 切换 root 用户，将系统根目录挂载为可读写
adb shell
su
mount -o rw,remount /

# 写入内容
echo 'ro.product.cpu.abilist=x86_64,x86,arm64-v8a,armeabi-v7a,armeabi
ro.product.cpu.abilist32=x86,armeabi-v7a,armeabi
ro.product.cpu.abilist64=x86_64,arm64-v8a
ro.vendor.product.cpu.abilist=x86_64,x86,arm64-v8a,armeabi-v7a,armeabi
ro.vendor.product.cpu.abilist32=x86,armeabi-v7a,armeabi
ro.vendor.product.cpu.abilist64=x86_64,arm64-v8a
ro.odm.product.cpu.abilist=x86_64,x86,arm64-v8a,armeabi-v7a,armeabi
ro.odm.product.cpu.abilist32=x86,armeabi-v7a,armeabi
ro.odm.product.cpu.abilist64=x86_64,arm64-v8a
ro.dalvik.vm.native.bridge=libhoudini.so
ro.enable.native.bridge.exec=1
ro.enable.native.bridge.exec64=1
ro.dalvik.vm.isa.arm=x86
ro.dalvik.vm.isa.arm64=x86_64
ro.zygote=zygote64_32' | tee -a /system/build.prop >> /system/vendor/build.prop
```

从官方的 [Release](https://github.com/niizam/Genymotion_A11_libhoudini/releases) 页面下载 system.zip，直接拖入到模拟器中，根据提示直接确认刷入：

![Image 96](https://image.3001.net/images/20240926/1727353341_66f551fd1982c8d3c6238.png)

刷入完成后直接重启模拟器即可。

这样就可以正常打开我们常用的 APP 了：

![Image 97](https://image.3001.net/images/20240926/1727353751_66f553974ba4df44bde46.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83 "开发环境")开发环境
----------------------------------------------------------------------------------------------

[](https://www.sqlsec.com/2024/10/ubuntu.html#Git "Git")Git
-----------------------------------------------------------

如果要使用 Github 协作项目的话，那么 GitHub 会根据我们本地的 Git 配置去箱显示对应的 commit 记录的头像：

```
# 配置邮箱 
➜ git config --global user.email "[email protected]"

# 配置用户名
➜ git config --global user.name "国光"
```

下图中间两个 commit 记录没有头像的原因就是没有配置上述邮箱的问题造成的：

[![Image 98: img](https://image.3001.net/images/20230711/16890783436308.jpg)](https://image.3001.net/images/20230711/16890783436308.jpg)

[](https://www.sqlsec.com/2024/10/ubuntu.html#Java "Java")Java
--------------------------------------------------------------

无论是 [Oracle JDK](https://www.oracle.com/hk/java/technologies/downloads/) 还是 Linux 自带的 OpenJDK，我们都可以先自己安装一遍，多多益善。有了 [jenv](https://github.com/jenv/jenv) 我们全部都可以灵活的切换。

*   [**OracleJDK - JDK8**](https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html)

经典的 JDK8 肯定是要安装一下的：

```
# 解压到/usr/lib/目录下
sudo tar -zxvf jdk-8u411-linux-x64.tar.gz -C /usr/lib/

# 编辑/etc/profile 配置文件
sudo vim /etc/profile
```

末尾添加如下内容：

```
JAVA_HOME=/usr/lib/jdk1.8.0_411
PATH=$JAVA_HOME/bin:$PATH
CLASSPATH=$JAVA_HOME/jre/lib/ext:$JAVA_HOME/lib/tools.jar
export PATH JAVA_HOME CLASSPATH
```

配置完成后重新加载一下配置文件生效：

```
# 重新载入配置文件
source /etc/profile

# 验证是否安装成功
java -version
```

*   [**OracleJDK - JDK17**](https://www.oracle.com/hk/java/technologies/downloads/#java17)

```
# 官网下载 deb 包直接安装
sudo gdebi jdk-17_linux-x64_bin.deb

# 默认安装的路径为
/usr/lib/jvm/jdk-17.0.12-oracle-x64/
```

*   [**OracleJDK - JDK21**](https://www.oracle.com/hk/java/technologies/downloads/#java21)

```
# 官网下载 deb 包直接安装
sudo gdebi jdk-21_linux-x64_bin.deb

# 默认安装的路径为
/usr/lib/jvm/jdk-21.0.4-oracle-x64/
```

*   [**OracleJDK - JDK23**](https://www.oracle.com/hk/java/technologies/downloads/#java23)

```
# 官网下载 deb 包直接安装
sudo gdebi jdk-23_linux-x64_bin.deb

# 默认安装的路径为
/usr/lib/jvm/jdk-23-oracle-x64/
```

*   OpenJDK 系列

```
# 路径为：/usr/lib/jvm/java-8-openjdk-amd64/
sudo apt install openjdk-8-jdk 

# 路径为：/usr/lib/jvm/java-11-openjdk-amd64/
sudo apt install openjdk-11-jdk 

# 路径为：/usr/lib/jvm/java-17-openjdk-amd64/
sudo apt install openjdk-17-jdk 

# 路径为：/usr/lib/jvm/java-21-openjdk-amd64/
sudo apt install openjdk-21-jdk 
```

虽然我们可以使用系统自带的：

```
update-alternatives --config java
```

简单高效地切换系统范围内的默认 Java 版本，但是不支持项目目录级别的 Java 版本管理：

![Image 99](https://image.3001.net/images/20241009/1728484736_67069580684149550b243.png)

这个时候我们可以考虑更加灵活的 `jenv` 了，可以在全局、用户级别以及项目级别管理和切换 Java 版本。

安装 jenv 不算复杂：

```
# 克隆项目
git clone https://github.com/jenv/jenv.git ~/.jenv

# 手动追加 zshrc 配置文件
echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(jenv init -)"' >> ~/.zshrc
```

下面是基本的用法：

```
# 查看当前的 Java 版本
jenv version

# 手动添加本地的 Java Home 路径
jenv add /usr/lib/jdk1.8.0_411/
jenv add /usr/lib/jvm/jdk-17.0.12-oracle-x64/
jenv add /usr/lib/jvm/jdk-21.0.4-oracle-x64/
jenv add /usr/lib/jvm/jdk-23-oracle-x64/
jenv add /usr/lib/jvm/java-8-openjdk-amd64/
jenv add /usr/lib/jvm/java-11-openjdk-amd64/
jenv add /usr/lib/jvm/java-17-openjdk-amd64/
jenv add /usr/lib/jvm/java-21-openjdk-amd64/

# 列出目前 jenv 所有可切换管理的版本
jenv versions

#global 全局设置 一般不建议改变全局设置
➜ jenv global <java 版本>

# shell 会话设置 只影响当前的shell会话
➜ jenv shell <java 版本>
# 取消 shell 会话的设置
➜ jenv shell --unset

# local 本地设置 只影响所在文件夹
➜ jenv local <java 版本>
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#Cargo "Cargo")Cargo
-----------------------------------------------------------------

Cargo 是 [Rust](https://www.rust-lang.org/) [_包管理器_](https://doc.rust-lang.org/cargo/appendix/glossary.html#package-manager)。Cargo 会下载 Rust 软件包的依赖项，编译你的包，制作可分发的包，并将它们上传到 [crates.io](https://crates.io/)

Ubuntu 上安装也比较简单：

```
curl https://sh.rustup.rs -sSf | sh
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#Redis "Redis")Redis
-----------------------------------------------------------------

```
# 搭建 redis 服务器
docker run --name redis-server -p 6379:6379 -d redis:7.2

# 安装 redis 客户端
sudo apt install redis-tools
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#Python "Python")Python
--------------------------------------------------------------------

主要是利用 pyenv 项目来管理我们的 Python 版本，项目地址为：[https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

具体用法大家自己去看官方文档，我这里只简单记录一点点：

```
# 安装 pyenv
curl https://pyenv.run | bash
```

手动编辑 .zshrc 配置文件，末尾追加：

```
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

简单的 pyenv 用法：

```
# 查看已经安装的Python版本
➜ pyenv versions

# 查看当前的 Python 版本
➜ pyenv version

# 查看可安装的版本
➜ pyenv install -l

# 安装与卸载 pypy3.8-7.3.11
➜ pyenv install pypy3.8-7.3.11
➜ pyenv uninstall pypy3.8-7.3.11
```

版本切换确实很方便，所安装的版本都在 `~/.pyenv/versions` 目录下：

```
# global 全局设置 一般不建议改变全局设置
➜ pyenv global <python版本>

# shell 会话设置 只影响当前的shell会话
➜ pyenv shell <python版本>
# 取消 shell 会话的设置
➜ pyenv shell --unset

# local 本地设置 只影响所在文件夹
➜ pyenv local <python版本>
```

pyenv 的 global、local、shell 的优先级关系是：shell \> local \> global

如果 pyenv 安装常见的 Python 版本出现告警的话，手动安装一下常见的依赖：

```
sudo apt install -y \
    build-essential \
    libbz2-dev \
    libssl-dev \
    libreadline-dev \
    libsqlite3-dev \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libffi-dev \
    liblzma-dev \
    tk-dev \
    uuid-dev \
    libgdbm-dev \
    libgdbm-compat-dev
```

如果需要 root 用户也使用 pyenv 的话，可用使用软连接，链接 我们普通用户 home下的的 .pyenv 文件夹配置：

```
sudo ln -s $HOME/.pyenv /root/.pyenv
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#Node-js "Node.js")Node.js
-----------------------------------------------------------------------

国光我 Nodejs 用的不多，主要就用来跑跑 Hexo 博客和使用 Gitbook 来写点知识点，又因为 Node.js 版本也比较凌乱，所以这里主要是通过 nvm 来进行配置管理。

```
# 安装 nvm
➜ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# 将下面的配置编辑追加到 .zshrc 配置中（如果有的话 不用重复添加）
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# 查看版本信息
➜ zsh
➜ nvm --version
0.40.3

# 查看当前 node 的版本
➜ nvm version 

# 安装最新稳定版 node
➜ nvm install stable

# 列出所有远程服务器的版本
➜ nvm ls-remote

# 安装指定版本
➜ nvm install v18.20.4
➜ nvm install <version>

# 列出所有已安装的版本
➜ nvm ls

# 卸载指定的版本
➜ nvm uninstall <version>

# 切换使用指定的版本node
➜ nvm use <version>

# 显示当前的版本
➜ nvm current
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#MySQL "MySQL")MySQL
-----------------------------------------------------------------

为了不干扰我们的宿主机环境，建议使用 Docker 来运行 MySQL 服务器：

```
docker run --name mysql -e MYSQL_ROOT_PASSWORD=P@ssw0rd -d -p 3306:3306 mysql:8.0.39-debian
```

安装 mysql 客户端：

```
sudo apt install mysql-client
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#Hexo "Hexo")Hexo
--------------------------------------------------------------

快速简约强大的博客框架：

```
# 安装 hexo
npm install hexo-cli -g

# Hexo 基础命令
➜ hexo clean    # 清除缓存
➜ hexo g        # 生成静态文件
➜ hexo s        # 启动 Hexo 服务
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#MkDocs "MkDocs")MkDocs
--------------------------------------------------------------------

[MkDocs](https://github.com/mkdocs/mkdocs) 是有一个优雅的写文档神器，使用 Python 安装很方便：

```
# 安装 mkdocs
➜ pip install mkdocs

# 安装 material 主题
➜ pip install mkdocs-material
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#JetBrains "JetBrains")JetBrains
-----------------------------------------------------------------------------

JetBrains 系列之间官网下载专业旗舰版的安装就行了：

```
# 给 pycharm 创建快捷方式
sudo ln -s /home/x-x/Documents/Softs/pycharm-2024.2.3/bin/pycharm /usr/local/bin/pycharm

# 给 idea 创建快捷方式
sudo ln -s /home/x-x/Documents/Softs/idea-IU-242.23339.11/bin/idea /usr/local/bin/idea
```

对应的我们自己创建好菜单应用程序图标：

![Image 100](https://image.3001.net/images/20241011/1728613146_67088b1a499fdfe72129d.png)

作为一个安全从业者，其实根本不需要找网上的盗版破解资源，我们直接利用正版服务器的指纹，即可找到网上很多的正版服务器：

![Image 101](https://image.3001.net/images/20241011/1728613320_67088bc8cbf0f0346ecc4.png)

直接激活就好了：

![Image 102](https://image.3001.net/images/20241011/1728613116_67088afc73f4dd5e56c4c.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%AE%89%E5%85%A8%E7%8E%AF%E5%A2%83 "安全环境")安全环境
----------------------------------------------------------------------------------------------

因为时间和精力有限，这部分只列举一些典型的安全工具，后面大家可以在工作和实战中逐步完善打造自己的安全系统。

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%B8%BB%E6%9C%BA%E6%8E%A2%E6%B5%8B "主机探测")主机探测
----------------------------------------------------------------------------------------------

```
# 安装  nmap 与 ncat
sudo apt install nmap ncat

# 安装扫描速度更快的 masscan
sudo apt install masscan

# 使用 ARP 协议来发现本地网络上的 IPv4 主机并指纹识别
sudo apt install arp-scan
➜ arp-scan --localnet
Interface: en0, type: EN10MB, MAC: c8:89:f3:b3:24:1d, IPv4: 10.1.1.180
Starting arp-scan 1.10.0 with 256 hosts (https://github.com/royhills/arp-scan)
10.1.1.1	00:0c:29:7c:19:2f	VMware, Inc.
10.1.1.10	a0:36:9f:89:ad:30	Intel Corporate
10.1.1.11	00:0c:29:b1:fa:11	VMware, Inc.
10.1.1.100	00:11:32:fa:6e:7c	Synology Incorporated
10.1.1.218	a8:a1:59:9f:57:aa	ASRock Incorporation
10.1.1.128	ec:4d:3e:86:cb:2e	Beijing Xiaomi Mobile Software Co., Ltd
10.1.1.199	78:11:dc:7d:d5:9a	XIAOMI Electronics,CO.,LTD

# go 编写的快速高效的端口扫描工具
➜ brew install naabu
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#SQL-%E6%B3%A8%E5%85%A5 "SQL 注入")SQL 注入
------------------------------------------------------------------------------------

```
# sqlmap 足矣
sudo apt install sqlmap
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E7%9B%AE%E5%BD%95%E6%89%AB%E7%A0%81 "目录扫码")目录扫码
----------------------------------------------------------------------------------------------

```
# dirsearch 足矣
sudo apt install dirsearch
```

发现直接运行会报错：

```
➜ dirsearch                                                 
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict
URL target is missing, try using -u <url>
```

这是因为和 Ubuntu 自带的 Python 冲突了，不要慌，我们有 pyenv 之间全局替换一下 Python 版本即可：

```
pyenv global 3.8.8
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%96%87%E4%BB%B6%E5%88%86%E6%9E%90 "文件分析")文件分析
----------------------------------------------------------------------------------------------

```
# binwalk CTF MISC 神器
sudo apt install binwalk
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8 "移动安全")移动安全
----------------------------------------------------------------------------------------------

```
# adb 安装
sudo apt install android-platform-tools-base 
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%AF%86%E7%A0%81%E7%A0%B4%E8%A7%A3 "密码破解")密码破解
----------------------------------------------------------------------------------------------

```
# 密码破解神器
sudo apt install hashcat

# 经典老牌的 UNIX 密码破解工具
sudo apt install john

# WiFi 无线安全必备
sudo apt install aircrack-ng
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%B5%81%E9%87%8F%E5%88%86%E6%9E%90 "流量分析")流量分析
----------------------------------------------------------------------------------------------

```
# wireshark 蓝队溯源必备
sudo apt install wireshark
```

Wireshark 同样在 Wayland 协议下使用 KDE 自带的全局菜单插件的话，菜单也不正常显示，我们让其手动工作在 x11 模式下，添加如下环境变量：

```
QT_QPA_PLATFORM=xcb GTK_IM_MODULE=fcitx SDL_IM_MODULE=fcitx QT_IM_MODULE=fcitx
```

这样 Wireshark 即可正常工作了。

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E9%9F%B3%E9%A2%91%E5%88%86%E6%9E%90 "音频分析")音频分析
----------------------------------------------------------------------------------------------

Audacity 是经典的音频分析软件，使用系统自带的 Discover 商店即可安装，如果安装后打不开的话，不妨切换来源再试试看：

![Image 103](https://image.3001.net/images/20241010/1728571066_6707e6baea5d30065f086.png)

成功运行的截图证明：

![Image 104](https://image.3001.net/images/20241010/1728571917_6707ea0db681675e21b1b.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%8E%8B%E7%BC%A9%E5%88%86%E6%9E%90 "压缩分析")压缩分析
----------------------------------------------------------------------------------------------

星火商店可以直接安装 ARCHPR 经典的压缩包破解工具：

![Image 105](https://image.3001.net/images/20241011/1728607401_670874a982ac0f270ac16.png)

目前在 Wine 环境下工作良好：

![Image 106](https://image.3001.net/images/20241011/1728607469_670874ed785baae20897f.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#JADX "JADX")JADX
--------------------------------------------------------------

[JADX](https://github.com/skylot/jadx) 可以很方便的分析 Jar 和 Android APK，安装好 Java 即可直接打开：

![Image 107](https://image.3001.net/images/20241011/1728608039_6708772720dd23bfc74bd.png)

我们来手动创建一个 JADX 的快捷方式，方便下次直接打开：

![Image 108](https://image.3001.net/images/20241011/1728608270_6708780e6d875e9fa4ac5.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#Yakit "Yakit")Yakit
-----------------------------------------------------------------

[Yakit](https://github.com/yaklang/yakit) 确实也是国产里面比较不错安全软件，值得一试。Linux 安装也比较简单，直接 [Release](https://github.com/yaklang/yakit/releases) 下载封装好的 AppImage 即可。

![Image 109](https://image.3001.net/images/20241011/1728615643_670894db45ecfcbaa7441.png)

目前在 Linux 上工作良好：

![Image 110](https://image.3001.net/images/20241011/1728615620_670894c444eb8ab9d9aae.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#Goby "Goby")Goby
--------------------------------------------------------------

[Goby](https://gobysec.net/) 也是一个不错的国产扫描器，Linux 下工作也很丝滑：

![Image 111](https://image.3001.net/images/20241011/1728616845_6708998db81faa0172ee0.png)

官方的脚本安装即可：

```
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
```

首次运行需要初始化一下：

```
➜ msfconsole

 ** Welcome to Metasploit Framework Initial Setup **
    Please answer a few questions to get started.


Would you like to use and setup a new database (recommended)? y
```

![Image 112](https://image.3001.net/images/20241010/1728572689_6707ed1133fc0e1261c28.png)

好像国内大家玩 Metasploit Pro 的不多，国光打包相关的[资源](https://www.sqlsec.com/download/Metasploit_Pro+Crack_Ubuntu_Debian.zip)大家自取。安装完成后手动再运行一些 Creak 里面的破解脚本：

![Image 113](https://image.3001.net/images/20241011/1728627019_6708c14b53fa31b1cf8ec.png)

因为这个 Pro 启动有点慢，所以每次开机后得确保相关服务都正常运行：

```
sudo systemctl list-units --type=service --all|grep metasploit
```

![Image 114](https://image.3001.net/images/20241011/1728628714_6708c7ea5bdfa4cde9092.png)

然后浏览器访问：

```
https://127.0.0.1:3790/
```

首次使用设置一下用户信息，因为有点复杂，大家一定要记好了：

![Image 115](https://image.3001.net/images/20241011/1728628819_6708c853da5431d2280ba.png)

相当于是一个 MSF 图形化界面，官方配备了一些自动化扫描功能：

![Image 116](https://image.3001.net/images/20241011/1728635447_6708e23736d6f2cc57d8e.jpg)

当然 Metasploit Pro 也是自带 msfconsole 的，对比一下，确实多了不少辅助测试模块：

![Image 117](https://image.3001.net/images/20241011/1728634816_6708dfc028c1be65a18d0.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#Burp-Suite "Burp Suite")Burp Suite
--------------------------------------------------------------------------------

首先在 [BP 官网下载](https://portswigger.net/burp/releases)最新的 Pro 安装包：

![Image 118](https://image.3001.net/images/20240918/1726636169_66ea6089dff612cee1f82.png)

```
chmod +x burpsuite_pro_linux_v2024_8_1.sh
./burpsuite_pro_linux_v2024_8_1.sh
```

全部默认回车安装下去就行：

![Image 119](https://image.3001.net/images/20240918/1726636333_66ea612d07244af72734e.png)

如果是带界面版本的话，可以先全部默认路径安装：

![Image 120](https://image.3001.net/images/20241010/1728573202_6707ef129ebc970c6fbcf.png)

下载最新版本的[注册机](https://github.com/h3110w0r1d-y/BurpLoaderKeygen)，拷贝到 BP 的安装目录下：

```
mv BurpLoaderKeygen_v1.17.jar ~/BurpSuitePro
```

直接运行注册机：

```
~/BurpSuitePro/jre/bin/java -jar ~/BurpSuitePro/BurpLoaderKeygen_v1.17.jar
```

点击`Run`，输入许可证然后选择**手动激活**即可：

![Image 121](https://image.3001.net/images/20240918/1726637037_66ea63ed29f26f2d6724f.png)

为了日后方便使用，直接修改`~/BurpSuitePro/BurpSuitePro.vmoptions`, 增加以下参数：

```
--add-opens=java.base/java.lang=ALL-UNNAMED
--add-opens=java.base/java.lang=ALL-UNNAMED
--add-opens=java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED
--add-opens=java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED
--add-opens=java.base/jdk.internal.org.objectweb.asm.Opcodes=ALL-UNNAMED
-javaagent:BurpLoaderKeygen_v1.17.jar
-noverify
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%BD%AF%E4%BB%B6%E8%B5%84%E6%BA%90 "软件资源")软件资源
----------------------------------------------------------------------------------------------

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%8E%88%E4%BA%BA%E4%BB%A5%E6%B8%94 "授人以渔")授人以渔
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#Discover "Discover")Discover

`Discover` 是 KDE Plasma 桌面环境的图形化软件管理工具，支持多种软件包格式和源，包括 Snap 包。首次使用建议也顺便安装一下 Flatpak 软件包的后端程序，这样后续我们可以使用 Discove 搜索、安装和管理来自 Flatpak 软件源（如 Flathub）的应用程序。

![Image 122](https://image.3001.net/images/20241003/1727930794_66fe21aa3722f451160b3.png)

首次使用 Discover 安装一些 snap 等一些资源软件可能存在汉字乱码的问题：

![Image 123](https://image.3001.net/images/20241003/1727933817_66fe2d795ed820eb1b885.png)

部分应用重启一下即可解决乱码问题了，少数应用还可能存在汉字乱码，所有整体 KDE 自带的 Discover 软件中心确实不太适合国人使用。

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E9%BA%92%E9%BA%9F%E8%B5%84%E6%BA%90 "麒麟资源")麒麟资源

国内大力推广普及信创系统，所有我们也可以白嫖麒麟系统他们打包好的常用软件，直接下载对应的 deb 包安装即可。

下载资源的地址：[https://software.openkylin.top/openkylin/yangtze/pool/all/](https://software.openkylin.top/openkylin/yangtze/pool/all/)

本方法是评论区网友 **like** 分享的：

![Image 124](https://image.3001.net/images/20241003/1727932793_66fe2979574afc73bc015.png)

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%98%9F%E7%81%AB%E5%95%86%E5%BA%97 "星火商店")星火商店

星火应用商店是国内打造的，专为 Linux 用户设计的应用商店，旨在解决 Linux 生态下应用分散、难以获取的问题。

官网地址：[https://www.spark-app.store/](https://www.spark-app.store/)

安装方法，官方项目的 [release 下载](https://gitee.com/spark-store-project/spark-store/releases)最新的 deb 包安装即可：

```
sudo gdebi spark-store_4.3.0-fix5.1_amd64.deb
```

![Image 125](https://image.3001.net/images/20241003/1727936508_66fe37fcc8ef7e083161d.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E7%B3%BB%E7%BB%9F%E5%A2%9E%E5%BC%BA-1 "系统增强")系统增强
------------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BA%94%E7%94%A8%E6%A6%82%E8%A7%88 "应用概览")应用概览

| 软件名称 | 下载安装方式 | 说明 |
| --- | --- | --- |
| PCManFM-Qt File Manager | Discover 商店 | 更简约一点的文件管理器 |
| Files | Discover 商店 | 另一款极简的文image-20241011163009383件管理器 |
| Piper | Discover 商店 | 鼠标侧建自定义 |
| Nautilus scripts manager | Discover 商店 | GNOME 下默认的文件管理器 |

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%B8%8B%E8%BD%BD%E5%B7%A5%E5%85%B7 "下载工具")下载工具
----------------------------------------------------------------------------------------------

| 软件名称 | 下载安装方式 | 说明 |
| --- | --- | --- |
| Motrix | [星火商店](spk://store/network/motrix) | 好用的多线程下载工具 |
| 迅雷 | [麒麟资源](https://software.openkylin.top/openkylin/yangtze/pool/all/) | 极简版的迅雷下载工具 |
| 阿里云盘 | [星火商店](spk://store/network/com.aliyundrive.spark) | Wine 环境下工作良好 |
| 百度网盘 | [星火商店](spk://store/network/baidunetdisk) | 垃圾百度云官方居然有 Linux 客户端 |
| 天翼云盘 | [星火商店](spk://store/network/com.cloud.21cn) | 三线网盘居然也有 Linux 客户端 |
| 夸克网盘 | [星火商店](spk://store/network/cn.quarkclouddrive.spark) | 目前体验还算不错的国产网盘。 |
| 蓝奏云盘 | [星火商店](spk://store/network/com.lanzou.spark) | 好像不怎么盈利，感觉随时可能跑路倒闭 |

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%B5%8F%E8%A7%88%E5%99%A8 "浏览器")浏览器
-----------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BA%94%E7%94%A8%E6%A6%82%E8%A7%88-1 "应用概览")应用概览

| 浏览器名称 | 下载安装方式 | 说明 |
| --- | --- | --- |
| Chromium | [星火商店](spk://store/network/chromium-linux) | 开源版本的 Chrome 浏览器 |
| Google Chrome | [星火商店](spk://store/network/google-chrome-stable) | 浏览器里永远的第一梯队 |
| Microsoft Edge | [星火商店](spk://store/network/microsoft-edge-stable) | Edge 浏览器近几年发展的也不错 |
| Vivaldi | [星火商店](spk://store/network/vivaldi-stable) | 挺个性的基于 Chromium 内核的浏览器 |
| Yadex Browser | [官网下载](https://browser.yandex.com/) | 俄罗斯那边的浏览器，也是基于 Chromium 内核 |
| 深度浏览器 | [星火商店](spk://store/network/org.deepin.browser) | 基于玲珑应用反向打包的深度浏览器 |
| Tor 浏览器 | [星火商店](spk://store/network/org.torbrowser.spark) | 关注暗网威胁情报必备 |

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%BD%93%E9%AA%8C%E4%BC%98%E5%8C%96 "体验优化")体验优化

自带的 FireFox 火狐浏览器在 KDE 的 Wayland 模式下工作很完美，支持双指捏合缩放也支持中文输入法，但是 Chrome 和 Edge 还是需要我们配置一下的。

*   **FireFox**

自带的 Firefox 和我们的主题外观样式格格不入，所以需要我们来优化定制一下外观：

```
git clone  https://github.com/vinceliuice/WhiteSur-firefox-theme.git
cd WhiteSur-firefox-theme
./install.sh
```

![Image 126](https://image.3001.net/images/20241006/1728213752_670272f8573f125d2bbf2.png)

*   **Google Chrome**

```
cat /usr/share/applications/google-chrome.desktop|grep Exec                                             
Exec=/usr/bin/google-chrome-stable --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime %U
Exec=/usr/bin/google-chrome-stable --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime
Exec=/usr/bin/google-chrome-stable --incognito --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime
```

*   **Chromium**

```
cat /usr/share/applications/chromium-linux.desktop |grep Exec

Exec=/usr/bin/chromium-linux --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime %U
```

*   **Microsoft Edge**

```
cat /usr/share/applications/microsoft-edge.desktop| grep Exec                                           
Exec=/usr/bin/microsoft-edge-stable --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime %U
Exec=/usr/bin/microsoft-edge-stable --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime
Exec=/usr/bin/microsoft-edge-stable --inprivate --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime
```

*   **Yandex Browser**

```
cat /usr/share/applications/yandex-browser.desktop| grep Exec                                     
Exec=/usr/bin/yandex-browser-beta --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime %U
Exec=/usr/bin/yandex-browser-beta --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime
Exec=/usr/bin/yandex-browser-beta --incognito --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime
```

*   **Vivaldi Browser**

```
cat /usr/share/applications/vivaldi-stable.desktop| grep Exec                                           
Exec=/usr/bin/vivaldi-stable --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime %U
Exec=/usr/bin/vivaldi-stable --new-window --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime
Exec=/usr/bin/vivaldi-stable --incognito --enable-features=UseOzonePlatform --ozone-platform=wayland --ozone-platform-hint=auto --enable-wayland-ime
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%8A%9E%E5%85%AC%E7%A4%BE%E4%BA%A4 "办公社交")办公社交
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BA%94%E7%94%A8%E6%A6%82%E8%A7%88-2 "应用概览")应用概览

| 软件名称 | 下载安装方式 | 说明 |
| --- | --- | --- |
| QQ | [官网下载](https://im.qq.com/linuxqq/index.shtml) | 腾讯 QQ 的 Linux 版本做的真不错 |
| 微信 | [星火商店](spk://store/chat/store.spark-app.wechat-linux-spark) | 腾讯微信现在也开始有 Linux 版本了 |
| 飞书 | [星火商店](spk://store/chat/bytedance-feishu-stable) | 字节出品必属精品，Wayland 协议下工作很棒 |
| 钉钉 | [星火商店](spk://store/chat/com.alibabainc.dingtalk) | 不得不说，钉钉的市场占有率也挺高的 |
| 腾讯会议 | [星火商店](spk://store/chat/wemeet) | 办公软件，可以不用，但不能没有 |
| Telegram | Discover 商店 | 暗网威胁情报监控必备 |

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%BD%93%E9%AA%8C%E4%BC%98%E5%8C%96-1 "体验优化")体验优化

*   **微信**

如果你的屏幕分辨率很高的话，那么这个 Linux 微信的界面就有一点点小了，我们需要手动添加节目缩放变量来优化使用体验，下面表示应用界面缩放 1.5 倍：

```
QT_SCALE_FACTOR=1.5
```

而且发现 Fcitx5 的中文输入也不正常，所以需要我们手动编辑一下微信的启动图标属性：

```
sudo vim ~/.local/share/applications/store.spark-app.wechat-linux-spark.desktop
```

修改后的内容如下：

```
Exec=env QT_SCALE_FACTOR=1.5 GTK_IM_MODULE="fcitx" QT_IM_MODULE="fcitx" SDL_IM_MODULE="fcitx" /opt/apps/store.spark-app.wechat-linux-spark/files/launch.sh
```

这样我们的微信使用体验基本上和 Windows 下是没有什么区别的了。

*   **腾讯会议**

Wayland 协议下腾讯会议居然不让打开，直接弹窗告警了：

![Image 127](https://image.3001.net/images/20241005/1728140977_670156b13453bc91ee7ab.png)

编辑腾讯会议的启动脚本：

```
sudo vim /opt/wemeet/wemeetapp.sh
```

手动找到判断 wayland 协议的判断语句，在其上面添加如下内容来让应用强制走 X11 显示协议：

```
export XDG_SESSION_TYPE=x11
export QT_QPA_PLATFORM=xcb
unset WAYLAND_DISPLAY
```

![Image 128](https://image.3001.net/images/20241005/1728141834_67015a0a1f903048c4d62.png)

同理，高分辨率屏幕下的腾讯会议也比较小且不支持中文输入，我们手动调整一下缩放比例，添加如下的环境变量：

```
QT_SCALE_FACTOR=1.5 GTK_IM_MODULE=fcitx QT_IM_MODULE=fcitx SDL_IM_MODULE=fcitx
```

![Image 129](https://image.3001.net/images/20241005/1728142088_67015b081e462195a16be.png)

但是由于 X11 工作环境下 Wayland 安全性问题，目前腾讯视频是没法读取共享屏幕的，所以真的要用腾讯视频分享屏幕的话，还是老老实实使用虚拟机，或者尝试用用非常强大的飞书吧！

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E6%96%87%E6%A1%A3%E5%8A%9E%E5%85%AC "文档办公")文档办公
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BA%94%E7%94%A8%E6%A6%82%E8%A7%88-3 "应用概览")应用概览

| 软件名称 | 下载安装方式 | 说明 |
| --- | --- | --- |
| Typora | [官网下载](https://typora.io/#linux) | Typora 是国光我用来写 MarkDown 的主力 |
| WPS Office | [星火商店](spk://store/office/wps-office) | WPS Office Linux 下挺干净流畅的 |

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%BD%93%E9%AA%8C%E4%BC%98%E5%8C%96-2 "体验优化")体验优化

*   **Typora**

前面已经提到过了，Typora 在 Wayland 下中文输入也有问题，我们手动添加下面的环境变量即可：

```
GTK_IM_MODULE=fcitx SDL_IM_MODULE=fcitx QT_IM_MODULE=fcitx
```

*   **WPS Office**

WPS Office 提示缺失了一些字体：

![Image 130](https://image.3001.net/images/20241007/1728310603_6703ed4be507912070921.png)

字体我们可以去这个项目下载：[https://github.com/dv-anomaly/ttf-wps-fonts](https://github.com/dv-anomaly/ttf-wps-fonts) 然后找到这些 ttf 字体，手动右键点击【安装】即可。

同样 WPS 中文输入也有问题，我们手动添加下面的环境变量即可：

```
GTK_IM_MODULE=fcitx QT_IM_MODULE=fcitx SDL_IM_MODULE=fcitx
```

![Image 131](https://image.3001.net/images/20241007/1728311686_6703f1864f091521146cf.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E7%94%9F%E4%BA%A7%E6%95%88%E7%8E%87 "生产效率")生产效率
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BA%94%E7%94%A8%E6%A6%82%E8%A7%88-4 "应用概览")应用概览

| 软件名称 | 下载安装方式 | 说明 |
| --- | --- | --- |
| Planify | [Flathub](https://flathub.org/apps/io.github.alainm23.planify) | 简约高颜值的 todolist |
| Super Productivity | [官方项目](https://github.com/johannesjo/super-productivity) | 类似于 Windows To Do |

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%BB%A3%E7%A0%81%E5%BC%80%E5%8F%91 "代码开发")代码开发
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BA%94%E7%94%A8%E6%A6%82%E8%A7%88-5 "应用概览")应用概览

| 软件名称 | 下载安装方式 | 说明 |
| --- | --- | --- |
| Visual Studio Code | [官网下载](https://code.visualstudio.com/docs/?dv=linux64_deb) | 可能是目前最强的代码编辑器了 |
| Sublime Text | [官网下载](https://www.sublimetext.com/download) | 轻量化的代码编辑器 |
| PyCharm | [官网下载](https://www.jetbrains.com/pycharm/download/?section=linux) | 这才是真正的编译器 |
| IDEA | [官网下载](https://www.jetbrains.com/zh-cn/idea/download/?section=linux) | 这才是真正的编译器 |
| Navicat Premium Lite | [官网下载](https://www.navicat.com.cn/download/navicat-premium-lite) | Nvicat 官方出的免费版本的 足够用了 |
| Tiny RDM | [官网下载](https://redis.tinycraft.cc/) | 开源高颜值的 Redis 客户端 |

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%BD%93%E9%AA%8C%E4%BC%98%E5%8C%96-3 "体验优化")体验优化

*   **Visual Studio Code**

Visual Studio Code 中文输入有问题，我们手动添加下面的环境变量即可：

```
GTK_IM_MODULE=fcitx SDL_IM_MODULE=fcitx QT_IM_MODULE=fcitx
```

*   **Sublime Text**

默认的 Sublime Text 4180 是试用版本，我们可以简单的来进行破解一下。定位到可执行文件的路径为：

```
/opt/sublime_text/sublime_text
```

使用在线网站，[https://hexed.it](https://hexed.it/) 点击打开文件，选择上一步的 sublime\_text 执行文件，在搜索栏输入

```
80 79 05 00 0F 94 C2
```

替换为：

```
C6 41 05 01 B2 00 90
```

![Image 132](https://image.3001.net/images/20241008/1728362907_6704b99b9409a7d6d71a4.png)

重新导出替换原有的 sublime\_text 即可破解成功：

![Image 133](https://image.3001.net/images/20241008/1728391455_6705291f707212fb1f072.png)

下面附上此次 Sublime Text 4180 版本的破解后的文件：[sublime\_text](https://www.sqlsec.com/download/sublime_text)

如果你在 KDE5 下使用全局菜单插件使用 Sublime Text 这种应用的话，标题是正常无法显示的，这是因为工作在 Wayland 协议下的问题，目前 KDE5 版本中这个 BUG 估计是不会修复了，所以我们可以手动指定 x11 的环境变量：

```
GDK_BACKEND=x11 GTK_IM_MODULE=fcitx SDL_IM_MODULE=fcitx QT_IM_MODULE=fcitx
```

同时记得关闭 sublime 的自动更新：

![Image 134](https://image.3001.net/images/20241008/1728392176_67052bf0974310c1d1e4e.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E8%99%9A%E6%8B%9F%E8%BF%9C%E7%A8%8B "虚拟远程")虚拟远程
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BA%94%E7%94%A8%E6%A6%82%E8%A7%88-6 "应用概览")应用概览

| 软件名称 | 下载安装方式 | 说明 |
| --- | --- | --- |
| KRDC | KDE 自带 | KDE 自带的 RDP 远程客户端，但需要自己动手优化一下 |
| Remmina | [官网安装](https://remmina.org/how-to-install-remmina/#ubuntu) | Remmina 目前算是 Linux 远程工具第一梯队了 |
| VirtualBox | [官网安装](https://www.virtualbox.org/wiki/Linux_Downloads) | Linux 平台上开源免费的虚拟机方案 |
| Docker Desktop | [官网安装](https://docs.docker.com/desktop/install/linux/ubuntu/) | 图形化 Docker 容器管理 |
| Terminus | [官网下载](https://termius.com/download/linux) | 一个颜值很高的远程工具 |
| MobaXterm（Wine） | [星火商店](spk://store/development/net.mobatek.mobaxterm) | Windows 下好用的远程工具 |
| Tabby | [星火商店](spk://store/development/tabby-terminal) | 开源高颜值的终端 |

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%BD%93%E9%AA%8C%E4%BC%98%E5%8C%96-4 "体验优化")体验优化

*   **KRDC**

默认在 Wayland 显示协议下，KRDC 还无法正常工作，最新版本的 KRDC 可能已经解决这个问题了，但是我们的 Kubuntu 24.04 的 KDE5 的版本的 KRDC 版本太老：

![Image 135](https://image.3001.net/images/20241007/1728307848_6703e2884a2ac9765254a.png)

但是我们可以编辑应用程序，强制让 KRDC 走 X11 协议来工作：

![Image 136](https://image.3001.net/images/20241007/1728307959_6703e2f7df3b519224a30.png)

```
XDG_SESSION_TYPE=x11 QT_QPA_PLATFORM=xcb
```

这样 KRDC 就可以正常工作了：

![Image 137](https://image.3001.net/images/20241007/1728308099_6703e383c079dbcdc55a1.jpg)

*   **Remmina**

Ubuntu 24.04 自带的 Remmina 版本不是很新，所以打开后发现界面还不是中文的，可以根据官方文档手动添加 ppa 源，安装最新版本的 Remmina，这样界面就变成中文的了：

```
sudo apt-add-repository ppa:remmina-ppa-team/remmina-next
sudo apt update
sudo apt install remmina remmina-plugin-rdp remmina-plugin-secret
```

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%AA%92%E4%BD%93%E8%AE%BE%E8%AE%A1 "媒体设计")媒体设计
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BA%94%E7%94%A8%E6%A6%82%E8%A7%88-7 "应用概览")应用概览

| 软件名称 | 下载安装方式 | 说明 |
| --- | --- | --- |
| ImageMagick | Discover 商店 | ImageMagick 是 Linux 上经典的图像处理工具 |
| Gimp | [星火商店](spk://store/image_graphics/gimp-spark) | GIMP 是一款强大的图像处理软件 |
| Adobe PhotoShop CS6 | [星火商店](spk://store/image_graphics/com.photoshopcs6.deepin) | 虽然这个 PhotoShop 有点老，但又不是不能用 |
| Image Viewer | Discover 商店 | 支持直接查看和导出 macOS 的 ICNS 格式图标 |

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%BD%93%E9%AA%8C%E4%BC%98%E5%8C%96-5 "体验优化")体验优化

*   **激活 PhotoShop**

1.  备份好默认的 amtlib.dll 文件，路径为 ~/.deepinwine/Deepin-CS6/drive\_c/Program Files/Adobe/Adobe Photoshop CS6/amtlib.dll
2.  下载[带注册信息的 amtlib.dll 文件](https://storage.deepin.org/thread/20230808113052649_amtlib.dll%EF%BC%88PS-CS6%E6%BF%80%E6%B4%BB%E6%9B%BF%E6%8D%A2%E6%96%87%E4%BB%B6%EF%BC%89.zip?_gl=1*naabbj*_ga*MTAyNTQ2ODcyNS4xNzI3OTQwNjEw*_ga_QHZ7DPPD2D*MTcyNzk0MDYxMC4xLjAuMTcyNzk0MDYxMC4wLjAuMA..)替换到上面的目录下即完成破解激活

![Image 138](https://image.3001.net/images/20241003/1727941090_66fe49e28f2d94a2b0962.png)

[](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BD%B1%E9%9F%B3%E5%A8%B1%E4%B9%90 "影音娱乐")影音娱乐
----------------------------------------------------------------------------------------------

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E5%BA%94%E7%94%A8%E6%A6%82%E8%A7%88-8 "应用概览")应用概览

| 软件名称 | 下载安装方式 | 说明 |
| --- | --- | --- |
| Steam | [星火商店](spk://store/games/steam-launcher) | Steam 里面的 Linux 游戏还是不少的 |
| 网易云音乐 | [星火商店](spk://store/music/netease-cloud-music) | 星火商店的版本安装比较省心，但每日推荐这些功能不正常 |
| YesPlayMusic | [官方项目](https://github.com/qier222/YesPlayMusic/releases) | 高颜值的第三方网易云播放器 |
| PotPlayer | [星火商店](spk://store/video/org.potplayer.spark) | Windows 平台下移植过来的优秀的视频播放器 |
| VLC 媒体播放器 | `apt install vlc` | 老牌开源的媒体播放器 |
| MPV 媒体播放器 | `apt install mpv` | Linux 下简约且强大的媒体播放器 |
| OBS Studio | `apt install obs-studio ` | 非常强大的直播以及录制视频的专业软件 |

### [](https://www.sqlsec.com/2024/10/ubuntu.html#%E4%BD%93%E9%AA%8C%E4%BC%98%E5%8C%96-6 "体验优化")体验优化

*   **网易云音乐image-20241011163009383**

如果你的屏幕分辨率很高的话，那么这个 Linux 上的网易云音乐界面就有一点点小了，我们需要手动添加节目缩放变量来优化使用体验，下面表示应用界面缩放 1.5 倍：

```
QT_SCALE_FACTOR=1.5
```

找到应用程序菜单，编辑网易云音乐的应用程序，手动添加上面的环境变量即可。

因为网易云官方不维护的原因，这个官方客户端理论上是没法正常密码登陆账号的，但是支持扫码登陆，除了个性推荐不能正常使用以外，其他功能貌似也都支持工作：

![Image 139](https://image.3001.net/images/20241005/1728140174_6701538e10c8199631cea.png)
