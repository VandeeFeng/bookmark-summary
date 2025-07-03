---
title: 用 Glance 打造家庭服务器仪表盘
date: 2025-07-03
extra:
  source: https://sspai.com/post/100683
  original_title: 用 Glance 打造家庭服务器仪表盘
---
## Summary
**摘要**：
文章介绍了作者使用Glance打造家庭服务器仪表盘的经验，重点阐述了Glance作为信息面板的优势和定制化方法。作者从基本特点入手，详细说明了Glance的轻便、易部署、高自由度和移动优化等特性。接着介绍了数据获取的三种主要方式：API接口、本地数据和爬虫/RSS获取，并提供了多种数据处理和托管的方法。在样式定制方面，文章分享了直接修改现有组件、复制现成样式等方法。此外，还介绍了如何通过iframe嵌入图表和其展示信息的技巧。最后，作者以个人体验收尾，强调了让个人数据"活"起来的重要性。

**要点总结**：
1. **Glance作为统一信息面板的优势**：轻量级、易部署、高度可定制且对移动设备友好，相比传统"工程味"仪表盘更注重用户体验和美观度。
2. **多种数据来源获取方法**：包括直接调用本地/云端API接口、处理本地存储的文件数据，以及使用爬虫技术或RSS获取网页信息。
3. **三种简便的JSON数据托管方案**：利用Glance内置的静态资源目录、通过nginx代理静态文件，以及使用n8n自动化工具处理并返回数据。
4. **灵活的样式定制方案**：可以直接修改现有组件样式、复制现成网页样式代码获取灵感，甚至使用AI工具生成所需CSS样式。
5. **高级图表展示方案**：通过iframe嵌入Chartbrew或Grafana生成的图表，直接在面板中展示复杂数据可视化效果。
## Full Content
Title: 信息归处，一目了然：用 Glance 打造家庭服务器仪表盘 - 少数派

URL Source: https://sspai.com/post/100683

Published Time: 2025-07-02T07:09:14.000Z

Markdown Content:
这几年在自己家庭服务器上部署的服务已趋于稳定，变化不大，但始终缺少一个统一的入口，我希望这个入口除了基础的书签导航功能、显示服务器运行状态之外，还能将各个服务的定制化摘要信息也展现出来。在[Glance](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fglanceapp%2Fglance)出现之前，我被社区里的各类 Dashboard 应用一一劝退，大多因为颜值不合口味或是扩展性差，谁会愿意每天盯着工程味十足的仪表盘呢，又有多少人会在意每个 Docker 占用了多少 CPU 内存带宽？而 **Glance 是第一个让我有动力去使用和折腾的信息面板**。

![Image 1](https://cdnfile.sspai.com/2025/06/30/6508c3d646fc15ad9b0215a9e05b9d3f.png?imageView2/2/format/webp)

工程味的仪表盘

我一直认为，**NAS、家庭服务器或是自托管服务常谈的「数据掌握在自己手里」的口号，不只是简单地让数据换了个地方躺着，更大的意义是获得了对数据的完全支配权，可以让自己的赛博资产「活」起来**。譬如，随机播放 Immich 相册的精选照片、提醒待办家务、显示电子阅读里的金句、聚合各个网站的未读消息等等，这一切在 Glance 面板里，一目了然。我想通过介绍自己使用 Glance 的经验，为读者提供一些灵感，去寻找数据自主的快乐。

![Image 2](https://cdnfile.sspai.com/2025/06/30/a9e4a0aaf1964b1a7a3172fce82e7387.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

我的 Glance 仪表盘

当然，还是得简单介绍一下 Glance 的基本特点，自己总结的 Glance 最吸引我的特性：

*   快速轻便：Golang 编写，单个二进制文件，跨平台（Linux、Windows、macOS、freebsd、openbsd），十分容易部署，即使没有服务器也可以在自己的电脑上运行；
*   入门快速，使用官方提供的单个 yaml 配置文件即可快速架起服务，无需多余配置，对一个信息面板来说，能快速看到成品会激发让后续折腾的动力（反例就是 Homeassistant）；
*   易于定制，自由度高，颜值高，可以轻松快速地制作自己的小组件；
*   针对移动设备进行了优化。

![Image 3](https://cdnfile.sspai.com/2025/06/30/b6d4f0599d04efa458c8709f9c247156.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

丰富的官方组件

![Image 4](https://cdnfile.sspai.com/2025/06/30/b121eab1f41982b1c7abd83c6c034042.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

丰富的社区组件

![Image 5](https://cdnfile.sspai.com/2025/06/30/ee0df9dfe49cbe307e5d1dc1ec18a00e.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

可自定义主题

![Image 6](https://cdnfile.sspai.com/2025/06/30/e637211e6ed1a1efeb8850ee82351d63.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

移动端布局

因为其高自由度，Glance 可以显示任何我们想展示的信息，我们也可以将其定制成书签导航页、游戏主题 HUB，服务器监控面板等等。

![Image 7](https://cdnfile.sspai.com/2025/06/30/5be322644175e84c786055070078156a.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

Vishal@Discord

![Image 8](https://cdnfile.sspai.com/2025/06/30/d24dd49e52ec14ffaa81f5d00e7bb493.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

DarkXero@Discord

![Image 9](https://cdnfile.sspai.com/2025/06/30/f40db63718325f48d438b1c9a0fe939d.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

SelfishShellfish@Discord

Glance 的部署和使用方法可以查阅官方仓库，一些琐碎的基础设置也可以移步我的博客文章《[HomeServer 仪表盘新欢——Glance](https://sspai.com/link?target=https%3A%2F%2Fosnsyc.top%2Fposts%2Flaunch-glance%2F)》查看。此文还是聚焦于如何深度定制自己的 Glance 信息面板。

方法概述
----

Glance 的官方组件只需简单复制配置文件即可使用，定制化面板的核心是它的 `custom-api`组件。在 `custom-api` 组件的 `template` 配置中，我们通过编写 html 模板来自定义显示内容，并通过 css 对样式进行配置。官方仓库[glanceapp/community-widgets](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fglanceapp%2Fcommunity-widgets)提供了大量社区贡献的第三方组件，我的仓库也提供了十余种自定义的组件：[osnsyc/glance-widgets](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fosnsyc%2Fglance-widgets)。我们直接复制这些配置文件至 `glance.yml` 中即可生效，使用非常便捷。

对于一个最小化的典型 `custom-api` 组件，我们需提供 `url`和 `template` 数据，Glance 会通过 `url` 获取数据，并将数据处理成 JSON 格式；通过 `template` 提取出关键信息并渲染成 CSS 指定的样式，形成一个小模块显示在 Glance 面板中。我们要做的就是数据的获取、逻辑的编写和样式的定义。

![Image 10](https://cdnfile.sspai.com/2025/06/30/7037fe1c81d9f4947027addf450ca7f1.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)
数据的来源
-----

数据的来源总结为三个类别，API 接口，本地数据和其它（RSS、爬虫、逆向）。此阶段的目的是将信息加工成 JSON 格式数据。

### API 接口

这是最简单的数据获取途径。大多数开源的自托管软件，都会提供友好的 API 接口，我们在本地也能不受限制地调用，例如相册软件 Immich、数据探针 Netdata、Glances、健康检测 Healtchecks、多维表格 Baserow、RSS 阅读软件 TTRSS 等等。那么一般流程就是：在应用内生成 TOKEN -> 查看 API 文档通过 ENDPOINT 访问想要的数据 -> 在 Glance 内处理应答数据。整个流程不需要花费我们太多的时间即可实现。例如：

*   通过 Immich 的 API，设定过滤条件，在结果中随机获取图片显示在 Glance 中，我们还可以对图片进一步加工处理，成为自己的」每日 Memos「；
*   通过 Glances 探针显示服务器的资源利用率、温度等；
*   通过 Healtchecks 显示各项后台服务的运行状态；
*   通过 Baserow 将近期待处理的家务列举出来；
*   通过 TTRSS 显示 RSS 订阅数据、错误报告。

![Image 11](https://cdnfile.sspai.com/2025/06/30/b7eecfb89b6ea1e3e60542ff5897bc83.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

通过本地 API 接口实现的小组件

对于外部应用数据，成熟且开放的服务商也会提供 API 由用户使用，比如：

*   [Steam API](https://sspai.com/link?target=https%3A%2F%2Fsteamcommunity.com%2Fdev)，我们可以获取 Steam 新闻、统计数据、用户信息；
*   [GitHub API](https://sspai.com/link?target=https%3A%2F%2Fdocs.github.com%2Fen%2Frest%2Fabout-the-rest-api%2Fabout-the-rest-api%3FapiVersion%3D2022-11-28)，我们可以查看个人数据、提醒、活动等等信息；
*   [Cloudflare API](https://sspai.com/link?target=https%3A%2F%2Fdevelopers.cloudflare.com%2Fapi%2F)，我们可以查看账户信息、提醒、日志、计费等等信息；
*   [NASA Open APIs](https://sspai.com/link?target=https%3A%2F%2Fapi.nasa.gov%2F)，著名的每日天文图片就是从这里获得；
*   [OpenF1 API](https://sspai.com/link?target=https%3A%2F%2Fopenf1.org%2F)，提供实时和历史 Formula 1 数据

![Image 12](https://cdnfile.sspai.com/2025/06/30/068934bc1269d13895253471a4653964.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

NASA Open APIs

我们可以通过搜索 `xxx api` 查找所需服务的 API，网络上也有很多人提供了免费 API 接口，如[GitHub/public-apis](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fpublic-apis%2Fpublic-apis)[GitHub/free-api](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Ffangzesheng%2Ffree-api)。当然，很多服务商/软件并不提供官方的 API，但由于现代 Web 前后端分离特点，我们可以通过浏览器的开发者模式分析网站的数据访问端点。我们在 Github 上也可以很容易地搜索到别人打包好的非官方 API，在服务器上部署后即可很便捷地调用。

![Image 13](https://cdnfile.sspai.com/2025/06/30/bc5f3a3862ee76aad4cad4ff0c50b876.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)
在我的 Glance 面板中，有以下例子：

*   通过 Qobuz 的官方 API 提取显示近期指定类型的新专辑；
*   通过分析 Twikoo 的请求，提取出新鲜的评论信息；
*   通过分析少数派的请求，提取出实时的阅读量、关注者、充电数，并将数据保存在本地通过图表绘制趋势（详见」图表与样式章节「）；

![Image 14](https://cdnfile.sspai.com/2025/06/30/923bbe6059fdb43410caab430e686c00.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

非官方 API 实现的小组件

### 本地数据

我们在 Homeserver 中已经部署了诸如 Nextcloud、Resilio、Syncthing、Calibre 这样的服务，在服务器端保存了大量个人数据，可以提取本地文件的数据并显示在 Glance 中。以」显示个人最近阅读「信息卡为例，我在服务器端使用的服务为 Calibre+CalibreWeb，移动端为 MoonReader，同步则使用 MoonReader 内的 Webdav 完成，Webdav 由 Nextcloud 提供。那么服务器的 Nextcloud 文件夹内会有一个 `/.Moon+/Cache` 文件夹，存储有 `.po`和 `.an`文件，记录 MoonReader 的阅读进度、笔记和批注。我们使用[osnsyc/MoonReader](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fosnsyc%2FMoonReader_tools)工具将最新的阅读条目读取出来并输出 JSON 格式数据供 Glance 调用。

![Image 15](https://cdnfile.sspai.com/2025/06/30/1bdf51d23178ce427010436b09f049fc.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

MoonReader 到 Glance 的数据流

### RSS、爬虫等

对于封闭在应用内的信息，可以使用爬虫、逆向等手段获取，但需要付出的技术成本较高。而 RSSHUB 提供了现成的大量路由，对于 RSSHUB 中已经存在的路由，我们可以使用 n8n 转换为 JSON 格式的数据，使用`RSS Feed Trigger`节点自动获取一条最新的 RSS 订阅，使用`RSS Read`节点则可以获取所有 RSS 条目。

![Image 16](https://cdnfile.sspai.com/2025/06/30/7270282c5b318770832fa3cb6a762895.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

n8n 的 RSS Read 节点

我们也可以使用 n8n、[huginn](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fhuginn%2Fhuginn)这样的自动化软件来监控一些简单的网页，提取出关键信息显示在 Glance 中。以[汽油价格网](https://sspai.com/link?target=http%3A%2F%2Fwww.qiyoujiage.com%2Fzhejiang.shtml)为例，使用 n8n 的 `extractHtmlContent` 节点，通过浏览器开发者模式拾取指定样式标记的值，组装成 JSON 数据即可供 Glance 调用。

![Image 17](https://cdnfile.sspai.com/2025/06/30/9006035795b7b3128d2f0036f1f55b55.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

n8n 实现油价数据抓取

JSON 数据的便捷托管方式
--------------

我们通过上述的各种手段获取了想要的数据，Glance 如何访问它们呢？有很多种办法可以托管我们的 JSON 数据并供 Glance 查询，基于我们已有或者常用的服务，可以使用以下三种方法：glance/asset 静态托管，nginx 静态代理，n8n 自动化流程。当然我们也可以使用 Baserow、[typicode/json-server](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Ftypicode%2Fjson-server)、[adnanh/webhook](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fadnanh%2Fwebhook)甚至 python flask 库来自己编写一个简单的后端。但以下方法简单实用，无需额外的服务支持。

### glance/asset静态托管

`/asset`是 Glance 存放静态资源的路径，我们可以直接将 JSON 文件放在该路径下，然后使用`custom-api`的`url`设置为`http://YOUR_GLANCE_URL:PORT/asset/xx.json`，再设置好`template`即可。

此方法无需依赖其它服务，是最为便捷的方法，但`http://YOUR_GLANCE_URL:PORT/asset/`路径下的文件无需认证即可访问，在公网环境下有信息泄露的风险，注意不要存放敏感数据。

### nginx 静态代理

为了公网访问，在构建自己的 Homeserver 时大都会选择反代服务，如 nginx，traefik 等。我们可以用这些代理应用来代理静态 JSON 文件，以 nginx 为例，nginx 的地址为`http://NGINX_URL:NGINX_PORT`，我们将 JSON 文件存储在 nginx 的`html/glance`文件夹下，Glance 即可通过`http://NGINX_URL:NGINX_PORT/glance/xxx.json`获取 JSON 文件。

### n8n

前文也提到了使用 n8n 来做自动化流程，我们可以使用`Webhook`节点来触发流程，并直接将 JSON 格式的数据`Respond to Webhook`节点回复给 Glance；也可以将处理好的 JSON 数据存在本地，在 n8n 中由`Webhook`节点触发，通过`File`节点读取本地 JSON 文件，再用`Respond to Webhook`节点回复给 Glance。

自定义样式
-----

在`custom-api`组件的`template`配置中，我们通过编写 html 模板来自定义显示内容，并通过 css 对样式进行配置。css 样式可以直接写在`template`中，也可以写在`custom-style.css`文件内。好学的读者可以花一点时间了解一下 css 的用法，我们希望整个仪表盘风格统一，因此并不会使用很复杂的样式，但也可以偷懒地使用以下三种方法：

一，修改现有的 custom-widget 样式，在[glanceapp/community-widgets](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fglanceapp%2Fcommunity-widgets)仓库中，直接复制他人的代码，将显示内容替换成自己的数据，即可呈现一致的样式。

二，寻找现成组件与样式。在[Uiverse.io](https://sspai.com/link?target=https%3A%2F%2Fuiverse.io%2F)，[CodePen](https://sspai.com/link?target=https%3A%2F%2Fcodepen.io%2F)等网站上，有很多现成的组件，我们可以直接复制 html 和 css 代码到我们的 Glance 配置文件中使用。

![Image 18](https://cdnfile.sspai.com/2025/06/30/c0a92731b81cc0b928418166fca57d5b.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

uiverse.io

![Image 19](https://cdnfile.sspai.com/2025/06/30/aa8ab1158caf6fc8cb5ca6df9a7e1763.gif)

将代码直接复制进 Glance

三，寻找自己的喜欢的网站样式，通过浏览器的开发者模式`ctrl+shift+c`，直接选择页面上需要元素，在开发者工具的`样式`栏中查看复制 css 代码。我们还可以在 Glance 页面上使用开发者模式，对样式进行快速修改和预览。

![Image 20](https://cdnfile.sspai.com/2025/06/30/a9e6bcd11dc3d140b314fd80f90be824.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

浏览器的开发者模式

最后，我们也可以使用大模型，将想要的样式图发给它，直接生成 css 代码。

![Image 21](https://cdnfile.sspai.com/2025/06/30/5f1dc799f5e42a145a97bc6be99ecb6c.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)
图表与 iframe
----------

Glance 目前还没有图表组件供我们自定义图表，我们可以借助其它服务来生成图表并以 iframe 嵌入 Glance 中，[Chartbrew](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fchartbrew%2Fchartbrew)提供了一个易用的 UI 来帮助我们生成图表，设置简单，图表美观，但图表种类只支持柱形图、折线图、饼图和雷达图。如果 Chartbrew 不足以满足我们的要求，可以使用[Grafana](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana) 并安装[Business Charts](https://sspai.com/link?target=https%3A%2F%2Fvolkovlabs.io%2Fplugins%2Fbusiness-charts%2F)插件，其嵌入了 Apache ECharts，极大地丰富了图表的样式，还可以与图表进行交互。以下示例是路由的实时流量图 (netdata in openwrt)、家里植物的旭日图 (from self-hosted baserow)、少数派阅读统计 (from python crawler)。Grafana 和 Business Charts 插件的详细使用例程可以查阅我的博客文章《[用 Grafana 和 Echarts 实现可嵌入使用的 iframe 图表](https://sspai.com/link?target=https%3A%2F%2Fosnsyc.top%2Fposts%2Fgrafana-echarts-iframe%2F)》，相信在大模型的加持下，每个人都可以无障碍地做出自己满意的图表。

![Image 22](https://cdnfile.sspai.com/2025/06/30/87da9a0df0c7f9cbc764d34be9ece3b3.gif)

实时带宽图

![Image 23](https://cdnfile.sspai.com/2025/06/30/ebdfb493f91003b87ce993afd3aa4035.gif)

可交互旭日图

![Image 24](https://cdnfile.sspai.com/2025/06/30/6374baab3a59d2ad305d09b58d01856c.gif)

可交互折线图

iframe 响应相对较慢，最近，我也尝试了直接在 Glance 中嵌入 ECharts，目前已经初步成功工作了。要在 Glance 的 yaml 文件中配置 ECharts 并不是明智之举，数据的输入要严格遵守 ECharts 所需的配置格式，因此 n8n 仍然是最容易的方法：使用 API 获得数据后，通过 Code 节点组织成 ECharts 所需格式，通过 Webhook 传给 Glance。项目地址为[GitHub - osnsyc/glance-echarts](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2Fosnsyc%2Fglance-echarts)

![Image 25](https://cdnfile.sspai.com/2025/06/30/7a07adc92172a6bbe60694065c1630d8.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

通过 glance-echarts 实现的复杂图表

我们还可以把其它网页以 iframe 嵌入 Glance，比如将 Microbin 嵌入，并修改其 css 文件使之颜色与 Glance 统一。我们就无需跳转至新窗口来使用 Microbin 了。

![Image 26](https://cdnfile.sspai.com/2025/06/30/6b9c14f8cf1b4e4574ad87b00c830495.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

堆叠组件、iframe 嵌入 Microbin

写在最后
----

作为一篇技术向的文章，结尾来一段感慨式的总结可能显得有些矫情。但成文之际，发现我在少数派的第一篇文章《[家庭服务器除了存储还能做什么？聊聊我的部署思路](https://sspai.com/post/82512)》阅读量已经 10 万 + 了，很开心呀。期间也有人希望我多写点 Home Server 的内容 1，思来想去，发现没啥好写的，网络上也充斥着大量模板式的依赖 Docker 的应用安装教程，很是无趣。原想以「让个人数据『活』起来」为主题写写体会，但最终还是写成了这样一篇以 Glance 为载体的思路心得，以实例作为展示，还是更鲜活的，也算是 2025 年版的《家庭服务器除了部署「XX Alternative」还能做什么》吧。

![Image 27](https://cdnfile.sspai.com/2025/06/30/8d86dc5af61a2ac7748fdf9fc02fb7db.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1/format/webp)

