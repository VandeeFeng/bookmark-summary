Title: 在 Proxy 环境中使用 GitHub SSH 的 git 操作

URL Source: https://blog.inoki.cc/2025/03/08/GitHub-ssh-connection-behind-proxy/index.html

Markdown Content:
Inoki
 Earth
 Home
 Archives
 Tags
 Books
 Links
 About
Board
Welcome to Inoki's Blog. You can find my work on IME, Embedded System an more on here.
Recent Posts

在 Proxy 环境中使用 GitHub SSH 的 git 操作

2025-03-08

弹指十年间

2024-06-08

Android bootloader analysis -- ABL(2)

2024-04-20

Android bootloader analysis -- ABL(3)

2024-04-20

Ollama 架构解析

2024-04-16

Tag Cloud
ABL AI ARM ASIX Aboot Algorithm Android Bare Metal Bootloader Bug C++ Chrome OS Cloud Input Computer Graphics Craft Cross Compile Cuda Debian Debug Docker Dynamic Programming EDK2 EFI Embedded System FFmpeg GBDK GDB GitHub Go HTTP Hardware Hash Heterogeneous Computing IBus IME IoT JTAG KDE KDE Connect KDE Frameworks LLM Leetcode Linux Linux Driver LoRa LoRaWAN Man OpenCL Pack Proxy Python QUIC Qemu Qt Raspberry Pi Ray Tracing Router Rust SDDM SDR SDXL SSH Source Code Stable Diffusion System UART USB Ubuntu VSCode Visual Studio Vulkan WSL Win 10 ARM Win 10 IoT Windows XBL epoll git iOS ibus-libpinyin macOS ollama openwrt private sysfs 中文 硬件 翻译 驱动
Tags
ABL13
AI1
ARM3
ASIX2
Aboot3
Algorithm1
Android15
Bare Metal2
Bootloader15
Bug3
C++1
Chrome OS1
Cloud Input4
Computer Graphics1
Craft2
Cross Compile3
Cuda1
Debian1
Debug2
Docker1
Dynamic Programming1
EDK21
EFI1
Embedded System5
FFmpeg2
GBDK2
GDB1
GitHub1
Go2
HTTP1
Hardware3
Hash1
Heterogeneous Computing1
IBus5
IME1
IoT5
JTAG1
KDE2
KDE Connect8
KDE Frameworks2
LLM2
Leetcode1
Linux23
Linux Driver3
LoRa5
LoRaWAN5
Man1
OpenCL1
Pack1
Proxy1
Python2
QUIC1
Qemu1
Qt2
Raspberry Pi5
Ray Tracing1
Router3
Rust1
SDDM1
SDR4
SDXL1
SSH1
Source Code2
Stable Diffusion1
System1
UART1
USB4
Ubuntu2
VSCode1
Visual Studio1
Vulkan1
WSL1
Win 10 ARM1
Win 10 IoT2
Windows2
XBL1
epoll1
git1
iOS1
ibus-libpinyin4
macOS1
ollama2
openwrt1
private4
sysfs1
中文54
硬件4
翻译34
驱动1
Categories
AI3
LLM2
Stable Diffusion1
Algorithm1
Hash1
Bug3
Cuda1
Docker1
Linux Driver1
WSL1
Build1
Chinese1
Chrome OS1
Computer Graphics1
Vulkan1
Dairy4
Data Structure1
Algorithm1
EDK21
Embedded System9
Cross Compile3
Router3
IoT2
Win 10 IoT2
Raspberry Pi6
FFmpeg2
GBDK2
Hardware3
IME1
Inoki Home Made1
Qt1
EFI1
KDE2
Craft1
Blueprints1
KDE Connect8
中文1
KDE Frameworks2
Leetcode1
Dynamic Programming1
Linux24
Android15
Bootloader11
Driver1
Wayland3
man1
7-Miscellanea1
sysfs1
Linux Driver2
LoRa5
Modern C++1
Network1
Proxy1
OpenCL1
Package1
Debian1
Programming Language2
Python2
Protocol2
Qt1
Rust1
SDR4
Source Code4
Linux Driver2
USB-Net2
Python2
System1
Utility1
Build tool1
Translation19
Chinese19
USB4
VSCode1
iOS1
ibus-libpinyin4
硬件4
在 Proxy 环境中使用 GitHub SSH 的 git 操作
 2025-03-08  GitHub, Proxy, SSH, git  Comments Word Count: 833(words) Read Count: 3(minutes)

上次回国，发现墙又高了：GitHub 的 SSH 端口（22）现在会完全被阻断，导致无法正常使用 SSH 协议进行 git clone、git pull 等操作。

事实上，封禁 22 端口在公司网络环境中也可能是一个很普遍的操作，用于禁止员工随意使用 ssh 登录不受控的机器。

这种情况下，GitHub 官方是推荐使用 HTTPS 协议进行克隆的，但是需要配置 GitHub 的 login 集成或者是使用 token 来进行私有仓库的操作。但如果仍然希望使用 SSH，可以参考本文的做法，仅此记录一下。

问题现象

首先可以测试一下 SSH 是不是被阻断了，当你尝试使用 SSH 连接 GitHub 时，执行以下命令：

1

	
$ ssh -T git@github.com


如果遇到连接超时或被拒绝的情况，那么就是被阻断了，同时 HTTP_PROXY、HTTPS_PROXY 和 ALL_PROXY 仅对 HTTPS 协议的 git 操作有效，并不会对 SSH 协议的 git 操作生效。

在这种情况下，GitHub 提供了基于 HTTPS（443）端口的 SSH 协议的连接方式，可以绕开针对 SSH 22 端口的封禁。

如果改用 443 端口上的 SSH 连接可以成功的话（说明不是基于协议识别封禁的）：

1
2
3

	
$ ssh -T -p 443 git@ssh.github.com
# Hi USERNAME! You've successfully authenticated, but GitHub does not
# provide shell access.


那么就可以采用这种方式。

方案 1：手动更改 SSH 命令

在 git clone 或 git pull 等命令中手动使用 ssh.github.com 并指定 SSH 端口为 443。例如：

1

	
git clone ssh://git@ssh.github.com:443/your-repo.git


或者在已有的仓库中修改远程 URL：

1

	
git remote set-url origin ssh://git@ssh.github.com:443/your-repo.git


但这就需要对所用到的仓库都进行修改，太麻烦了。

方案 2：修改 SSH 配置文件

你也可以直接修改 SSH 配置文件（~/.ssh/config），让 SSH 将 github.com 直接当作 ssh.github.com 的别名来连接 GitHub，并自动使用 443 端口。

编辑 ~/.ssh/config（如果文件不存在，可以手动创建）：

1
2
3
4
5
6

	
echo "
Host github.com
  Hostname ssh.github.com
  Port 443
  User git
" >> ~/.ssh/config


然后测试 SSH 连接：

1

	
$ ssh -T git@github.com


如果输出如下信息，说明配置成功：

1
2

	
# Hi USERNAME! You've successfully authenticated, but GitHub does not
# provide shell access

方案 3：强制使用 SOCKS5 代理进行 SSH 连接

如果你不想使用 ssh.github.com，并且已经在本地配置了 SOCKS5 代理，可以让 git SSH 通过代理连接 GitHub。

在 ~/.ssh/config 文件中添加以下内容：

1
2
3

	
Host github.com
  Hostname github.com
  ProxyCommand nc -X 5 -x 127.0.0.1:1080 %h %p


其中 127.0.0.1:1080 是本地 SOCKS5 代理的地址，根据你的代理工具调整。

也可以使用 GIT_SSH_COMMAND 环境变量来修改默认 SSH 连接命令，详情可参考 git 的文档。

结论

如果当前网络封禁了 22 端口时，你可以通过以下三种方法绕过针对 GitHub 的封锁：

直接使用 ssh://git@ssh.github.com:443/your-repo.git 进行 Git 操作。
修改 ~/.ssh/config，让 GitHub 连接自动走 ssh.github.com 的 443 端口。
使用 SOCKS5 代理，让 SSH 通过代理访问 GitHub。

你可以根据自己的网络环境选择最适合的方法，确保顺畅地访问 GitHub。

Permanent Link： https://blog.inoki.cc/2025/03/08/GitHub-ssh-connection-behind-proxy/
	
InokiComputer Scientist
Ph.D in Computer Science, major in Embedded System and AI.
