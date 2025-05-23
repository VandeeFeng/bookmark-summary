---
title: 网络抓包的技巧
date: 2025-04-13
extra:
  source: https://www.kawabangga.com/posts/6950
  original_title: 网络抓包的技巧
---
## Summary
**摘要**：
本文是“计算机网络实用技术”系列文章之一，重点介绍了网络抓包的重要性以及常用的抓包方式和技巧。文章首先强调了抓包是网络分析的基础，即使无法直接定位问题，精准的抓包也能帮助网络专家快速解决问题。接着详细讲解了 `tcpdump` 命令的用法，包括指定网络接口（`-i`）、使用包过滤表达式（pcap-filter）以及其他常用参数，如不解析主机名（`-n`）、显示详细信息（`-v`）、限制抓包数量（`-c`）、显示MAC地址（`-e`）和展示包内容（`-A`）。同时，分享了通过发送带标记的HTTP请求来定位问题的技巧。此外，文章还介绍了使用Wireshark进行离线分析的方法，通过 `tcpdump` 抓包保存为 `.pcap` 文件，再用 Wireshark 分析。还介绍了使用`tee`命令同时将抓包内容写入文件和标准输出，以及使用 `-s` 参数来限制抓包大小，提高分析效率。文章还强调了抓包位置的重要性，并建议在复杂网络中绘制拓扑图辅助分析。最后，提到了SPAN交换机抓包和RSPAN远程抓包等高级抓包技术。

**要点总结**：

1.  `tcpdump` 是最常用的抓包工具，通过指定接口（`-i`）和过滤表达式可以精确抓取网络数据包。包过滤表达式（pcap-filter）允许用户根据协议、IP地址等条件筛选数据包，提高抓包效率。常用的参数包括 `-n`（不解析主机名）、`-v`（显示详细信息）、`-c`（限制抓包数量）、`-e`（显示MAC地址）和 `-A`（展示包内容）。
2.  通过发送带有特定标记（如 `asdf123`）的 HTTP 请求，可以在多节点的网络中定位问题，尤其是在代理转发的情况下，有助于判断请求是否到达目标节点。这种方法适用于明文协议，通过在请求中加入唯一标识，可以在中间节点进行抓包，从而判断请求是否被正确转发。
3.  Wireshark 是一款强大的离线网络分析工具，可以读取 `tcpdump` 保存的 `.pcap` 文件，并提供重传分析、序列号分析等功能，方便用户进行深入分析。使用 `tcpdump -w file.pcap` 命令可以将抓包数据保存为 `.pcap` 文件，便于后续使用 Wireshark 进行分析。
4.  在抓包分析时，需要明确抓包的位置，并结合网络拓扑图进行分析，尤其是在复杂的网络环境中，发送端和接收端的数据包可能不一致，因此需要多端抓包对比分析。务必注意网卡驱动可能会对数据包进行 offload 处理，导致抓包结果与实际传输的数据包有所差异。
5.  SPAN 交换机抓包和 RSPAN 远程抓包是两种高级抓包技术，通过端口镜像将网络设备上的流量复制到指定端口，然后进行抓包分析。这种方法适用于需要监控特定网络设备的流量情况，但无法直接在其上进行抓包的场景。

## Full Content
Title: 网络抓包的技巧 | 卡瓦邦噶！

URL Source: https://www.kawabangga.com/posts/6950

Markdown Content:
虽然这个系列的文章都是聚焦于如何通过分析网络抓包文件，结合网络知识，来解决实际的问题的，但是分析之前的步骤——**抓包**，也是同样重要！很显然，如果不会抓包，那么网络分析去分析什么呢？

抓得一手好包也是很厉害的！笔者遇到过很多次情况，虽然我们无法直接定位根因，但是同事能够精准地捕获到问题的现象，把问题描述给相关的网络专家，传给他们抓包文件，专家一看到准确的抓包文件，就可以很快解决问题了！

可惜的是，抓包的技巧无法像网络分析那样可以通过文章来出谜题，来让读者小试牛刀。所以，这篇文章就来写一下一些常用的抓包方式和技巧，希望能补齐这一块内容。

Tcpdump
-------

`tcpdump` 命令是我们最常用的抓包工具了[1](https://www.kawabangga.com/posts/6950#11d6fd20-d360-49ff-b3ea-4a44c5e1c6a8)。

`tcpdump -i eth0 icmp and host 1.1.1.1`

这个命令就可以抓取到所有通过 `eth0` 去 ping `1.1.1.1` 这个地址的包。

`-i eth0` 的意思是抓取指定的 interface，如果不指定，tcpdump 会默认选择一个。但是推荐每次都指定好这个参数，这样就没有不确定性了。如果使用 `-i any` 就可以抓取所有常规端口（文档的原文是 _all regular network interfaces_），但是什么属于「常规端口」就取决于操作系统的实现了。所以，建议也是如果要抓取多个 interface 来分析的话，就多开几个 tcpdump 进程，这样更加稳定一些。

这个参数非常有用，比如，在定位 ARP 问题的时候，我们需要确定每一个物理接口收发 ARP 的情况，就可以开多个进程分别 dump 每一个 interface 的网络；在定位 Linux 网络栈不通的情况时[2](https://www.kawabangga.com/posts/6950#df4e0646-6976-4f41-a992-edf9273ff2f8)，比如有 macvlan，vlan，veth 等复杂的 driver，可以用 tcpdump 对每一个接口 dump，看下包丢在哪里。

`icmp and host 1.1.1.1` 这个就是包过滤的表达式了，`icmp` 表示只抓取 `icmp` 协议，`host 1.1.1.1` 表示只抓取 src ip 或者 dst ip 是 `1.1.1.1` 的包。这种包过滤表达式其实是 pcap-filter(7)[3](https://www.kawabangga.com/posts/6950#5747172c-0905-4332-b1b9-5940cb15c596) 提供的，所以要想看语法是怎么定义的，看 pcap-filter 的文档就可以了。pcap-filter 支持的语法很灵活，能做的事情很多，基本上想抓什么样的包都可以写出来。但是我们没有必要把所有的语法都记住，因为常用的抓包都是比较简单的。可以找一个 tcpdump exmaple[4](https://www.kawabangga.com/posts/6950#0ffdc330-dc9c-4815-a605-33bd5bb0c542) 看一下，基本就够用了。其次，我们一般不会直接从 tcpdump 就分析出来问题原因，所以这个语法最重要的作用是**把我们想要的包抓到**，然后为了抓包性能更高，抓包文件更小，我们想要对抓包定义的更精确一些。其实，多抓一些包也没有什么问题，如果不确定怎么过滤出来 TCP SYN+ACK 的包，那不妨就把所有的 SYN 包全抓到，然后再用 Wireshark 这种工具来分析吧。最后，我们现在有 AI 了，用 AI 来写 pcap-filter 也是一个不错的方法，因为这种语法难写，但是很容易验证正确性。

Tcpdump 一些常用的其他参数如下：

*   `-n` 不解析主机名和端口号，保留原始的数字
*   `-v`, `-vv`, `-vvv` v 越多表示输出的信息越详细
*   `-c 5` 表示抓到 5 个包之后就退出
*   `-e` 显示二层的 link layer header，这样就可以看到 MAC 地址了
*   `-Q` 可以指定抓包方向，可以选的有 `in`, `out`, `inout`
*   `-A` 可以展示包的内容，tcpdump 默认是只根据不同的协议展示 header 信息的。在线上排查问题的时候，我们往往需要通过特殊请求的关键字来定位到单个请求的情况进行排查，这样 -A 展示出来包的内容就格外有用。

[![Image 1](https://www.kawabangga.com/wp-content/uploads/2025/04/tcpdump-A-1024x339.png)](https://www.kawabangga.com/wp-content/uploads/2025/04/tcpdump-A.png)

通过 -A 参数来抓取特定的 HTTP 请求

这里分享一个特殊的技巧，就是**发标记请求来定位问题**。比如 A 通过 B 代理发请求给 C，现在网络不通，我们要定位 B 收到了请求没有，才知道是 B 的问题还是 C 的问题。但是 B 本身就有很多线上流量，怎么知道 A 发送的请求到达 B 了没有呢？我们可以在 B 进行 tcpdump：`tcpdump -i eth0 tcp | grep asdf123 -A 10`，然后我们从 A 发送一个请求：`curl http://host-C.com/asdf123`。`asdf123` 就是我们在请求里面放上的标记，如果 B 能够正常转发，我们就可以 match 到这个请求。当然了，这种技巧只适用于 HTTP 这种明文协议。

Wireshark 离线分析
--------------

有些问题很难直接在 tcpdump 的终端分析出来问题，比如涉及 sequence number 分析的，重传分析之类的，我们需要人工对比 seq number，真是一项费眼睛的工作！所以如上所说，我们也经常在机器上用 tcpudmp 抓包保存成 `.pcap` 文件，下载到本地用 Wireshark 分析。Wireshark 就可以自动根据 sequence number 告诉我们重传等信息了！

[![Image 2](https://www.kawabangga.com/wp-content/uploads/2025/04/tcpdump-retrans-and-dup-info-1024x404.png)](https://www.kawabangga.com/wp-content/uploads/2025/04/tcpdump-retrans-and-dup-info.png)

Wireshark 可以展示出来 Dup ACK 和 Retransmission 等信息

具体的操作方式是，用 `tcpdump -i eth0 -w file.pcap icmp` 来进行抓包，`-w file.pcap` 表示把抓包文件保存为 `file.pcap`，抓包结束后，就可以把这个文件用 rsync 或者 scp 下载到本地，用 Wireshark 打开了。

`.pcap` 文件是一种标准的二进制抓包文件[5](https://www.kawabangga.com/posts/6950#1342cb09-464b-47f4-bffb-f159efd288f0)，很多抓包分析工具都支持这种格式的解析，比如 tcpdump, wireshark, scapy 等等，如果想写代码进行更加定制化的分析，也可以用已有的库[6](https://www.kawabangga.com/posts/6950#0fd0a454-5481-42cc-b0e4-39c9ccb5bf92)解析，就如同用 json 库来解析 json 文件一样。

[![Image 3](https://www.kawabangga.com/wp-content/uploads/2025/04/tshark-pcap-file-1024x661.png)](https://www.kawabangga.com/wp-content/uploads/2025/04/tshark-pcap-file.png)

使用 wireshark 的命令行工具 tshark 可以解析二进制 pcap 文件到 json 格式

使用 `-w` 写入文件的时候有一个小问题，就是 tcpdump 原本的到终端的输出没有了。有两种方式可以解决，第一种是用 tcpdump 自带的 `--print` 功能：

`tcpdump -i eth0 -w file.pcap --print`

`--print` 会让 tcpdump 把内容输出到屏幕，即使当前使用了 `-w` 参数。

第二种就是用 `tee`，在写入文件的同时，也写入到 stdout。

`tcpdump -i eth0 -U -w - | tee test.pcap | tcpdump -r -`

其中，第一个 tcpdump 把抓包文件写入到 stdout（`-w stdout`，注意其中的 `-U` 表示按照 packet buffer，即来一个 packet 就输出一个到 stdout，而不是等 buffer 满了才进行输出），然后 `tee` 这里做了分流，把 stdin（tcpdump 的 stdout）同时输出到文件和 stdout。由于这里的 stdout 是 tcdpump 输出的二进制抓包内容，所以我们需要再用 tcpdump 解析这个二进制内容，`-r -` 表示从 stdin 读入。

还有一个技巧是 `-s` 参数，默认情况下 tcpdump 会保存所有抓到的内容，但是在分析某些问题的时候，尤其是 TCP 性能问题，我们其实不需要 TCP 传输的 payload 内容，只看 TCP 包的 header（序列号部分）就知道传输的速度了，所以可以用 `-s 40` 来只抓取前 40 个 bytes，有了 IP header 和 TCP header，就足够分析了。（如果担心有 TCP option 的存在，可以用 `-s 54`）

其他的一些经验
-------

**知道包是从哪里抓到的，很重要**。在排查问题的时候，拿到抓包文件，应该第一时间确认抓包的位置。否则，就可能连自己看到的问题是现象还是根因都分不清楚。建议在复杂的结构中画一个拓扑图来对照分析，在定位 Linux 网络栈的问题时，如果接口拓扑非常复杂，也建议画一个拓扑图来分析。

**可以从网络的多端抓包对照分析**。发送端的抓包不一定等于接受端，尤其分析 TCP 问题的时候。可以同时在发送端和接收端进行抓包，然后对照分析。

在使用 tcpdump 的时候，要尤其注意，我们抓到的包已经经过了网卡驱动的处理，网卡驱动经常会帮 CPU 做一些 offload 的工作，比如把可能因网卡的 GRO/LRO 等特性，导致多个小包在抓包时被合并为一个较大的数据包，或者网卡帮助卸载了 vlan tag 等，我们用 tcpdump 抓到的包不一定是真正在网络上传输的包[7](https://www.kawabangga.com/posts/6950#3df8c14c-6060-453c-a33a-3f92d496241b)。要格外注意。

SPAN 交换机抓包和RSPAN 远程抓包
---------------------

除了我们熟悉的 Linux 抓包，其实网络设备上也可以抓包的。我们一般叫它「端口镜像」技术，故名思义，原理就是把网络设备的一个端口的流量全部复制到另一个端口，而另一个端口连接的就是我们的抓包程序。

1.  文档的主页：[https://www.tcpdump.org/manpages/tcpdump.1.html](https://www.tcpdump.org/manpages/tcpdump.1.html) [↩︎](https://www.kawabangga.com/posts/6950#11d6fd20-d360-49ff-b3ea-4a44c5e1c6a8-link)
2.  [Keepalived 脑裂问题排查](https://www.kawabangga.com/posts/6781) [↩︎](https://www.kawabangga.com/posts/6950#df4e0646-6976-4f41-a992-edf9273ff2f8-link)
3.  pcap-filter 文档在这里：[https://www.tcpdump.org/manpages/pcap-filter.7.html](https://www.tcpdump.org/manpages/pcap-filter.7.html) [↩︎](https://www.kawabangga.com/posts/6950#5747172c-0905-4332-b1b9-5940cb15c596-link)
4.  比如这一个：[https://danielmiessler.com/blog/tcpdump](https://danielmiessler.com/blog/tcpdump) [↩︎](https://www.kawabangga.com/posts/6950#0ffdc330-dc9c-4815-a605-33bd5bb0c542-link)
5.  IETF 的文件规范定义：[https://www.ietf.org/archive/id/draft-gharris-opsawg-pcap-01.html](https://www.ietf.org/archive/id/draft-gharris-opsawg-pcap-01.html) [↩︎](https://www.kawabangga.com/posts/6950#1342cb09-464b-47f4-bffb-f159efd288f0-link)
6.  Python 可以使用 scapy ([https://scapy.readthedocs.io/en/latest/usage.html#reading-pcap-files](https://scapy.readthedocs.io/en/latest/usage.html#reading-pcap-files))读取 pcap 文件，golang 可以使用这个库进行解析：[https://pkg.go.dev/github.com/google/gopacket/pcap](https://pkg.go.dev/github.com/google/gopacket/pcap) [↩︎](https://www.kawabangga.com/posts/6950#0fd0a454-5481-42cc-b0e4-39c9ccb5bf92-link)
7.  参考 [有关 MTU 和 MSS 的一切](https://www.kawabangga.com/posts/4983) 一文中，「道理我都懂，但是我的抓的包怎么大？？」 [↩︎](https://www.kawabangga.com/posts/6950#3df8c14c-6060-453c-a33a-3f92d496241b-link)

\==计算机网络实用技术 目录==
-----------------

这篇文章是计算机网络实用技术系列文章中的一篇，这个系列正在连载中，我计划用这个系列的文章来分享一些网络抓包分析的实用技术。这些文章都是总结了我的工作经历中遇到的问题，经过精心构造和编写，每个文件附带抓包文件，通过实战来学习网路分析。

**如果本文对您有帮助，欢迎扫博客右侧二维码打赏支持，正是订阅者的支持，让我公开写这个系列成为可能，感谢！**

_没有链接的目录还没有写完，敬请期待……_

1.  [序章](https://www.kawabangga.com/posts/6097)
2.  [抓包技术以及技巧](https://www.kawabangga.com/posts/6950)
3.  [理解网络的分层模型](https://www.kawabangga.com/posts/6295)
4.  [数据是如何路由的](https://www.kawabangga.com/posts/6919)
5.  网络问题排查的思路和技巧
6.  [不可以用路由器？](https://www.kawabangga.com/posts/6178)
7.  [网工闯了什么祸？](https://www.kawabangga.com/posts/6286)
8.  [网络中的环路和防环技术](https://www.kawabangga.com/?p=6291)
9.  [延迟增加了多少？](https://www.kawabangga.com/?p=6372)
10.  [TCP 延迟分析](https://www.kawabangga.com/?p=6378)
11.  [压测的时候 QPS 为什么上不去？](https://www.kawabangga.com/posts/6910)
12.  [压测的时候 QPS 为什么上不去？答案和解析](https://www.kawabangga.com/posts/6937)
13.  [重新认识 TCP 的握手和挥手](https://www.kawabangga.com/?p=6383)
14.  [重新认识 TCP 的握手和挥手：答案和解析](https://www.kawabangga.com/posts/6467)
15.  [TCP 下载速度为什么这么慢？](https://www.kawabangga.com/posts/6570)
16.  [TCP 长肥管道性能分析](https://www.kawabangga.com/posts/6616)
17.  后记：学习网络的一点经验分享

与本博客的其他页面不同，本页面使用 [署名-非商业性使用-禁止演绎 4.0 国际](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh-hans) 协议。  

  

* * *

