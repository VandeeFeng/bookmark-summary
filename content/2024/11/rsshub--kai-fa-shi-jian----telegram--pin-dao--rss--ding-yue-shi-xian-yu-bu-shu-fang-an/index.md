---
title: RSSHub 开发实践 - Telegram 频道 RSS 订阅实现与部署方案
date: 2024-11-18
extra:
  source: https://www.pseudoyu.com/zh/2024/11/18/rsshub_telegram_channel_integration/
  original_title: RSSHub 开发实践 - Telegram 频道 RSS 订阅实现与部署方案
---
## Summary
**摘要**：
本文详细介绍了在RSSHub中，通过Telegram官方API及MTProxy实现特定Telegram频道更新订阅的具体实践与部署方案。文章首先提到了与其他开源项目合作的背景，进而针对Telegram频道RSS订阅实现的新策略，包括战术层面的考虑和操作步骤。内容从解决常见问题到集成Telegram API实际应用，再到如何配置MTProxy代理以维持请求发送的身份一致性的详尽说明。最后推荐Docker Compose部署的方式，并提供Zeabur平台上可视化部署模板的链接。整体结构清晰，覆盖面广，旨在满足有需求的开发者对实践流程的全面理解。

**要点总结**：
- **Telegram订阅集成的策略**：针对无法通过网页预览捕获的Telegram频道，作者介绍了从API角度实现通道RSS内容抓取的方法，首先查阅Telegram API文档寻找到online API的可能使用点，确定了为数百万订阅者提供法源制定的有效解决方案。
- **Telegram API获取方法**：通过 Telegram `Bot API`，及配置Telegram账号下的`App`来获取`api_id`与`api_hash`，结合后续自定义脚本获取Telegram`session`，确保API与场均请求由同一批设备/IP发出，解决分布式环境下的服务扩容与API限制作业问题。
- **MTProxy的使用**：为了达到不同运行环境间客户端IP保持一致的限制，作者引入并指导部署了MTProxy（一种Telegram专用代理服务），其其细节包括模板仓库、环境变量配置等，确保RSSHub实例与API操作间的相互兼容性，并增强了部署灵活性。
- **安全与便捷的部署方案**：推荐通过Docker Compose部署框架进行部署实践，明确列出需要配置的环境变数以整合Telegram相关组件与代理端口等信息，简化配置和优化安全性。
- **实例验证与门户平台**：作者提供了基于个人公开实例的URL示例，用于订阅特定频道内容的演示与验证，鼓励在RSSHub仓库中提议问题或与社区互动以获得技术支持与反馈，具体实施中的挑战及技术细节在社区中得到了维持。
## Full Content
Title: RSSHub 开发实践 #01：Telegram 频道 RSS 订阅实现与部署方案

URL Source: https://www.pseudoyu.com/zh/2024/11/18/rsshub_telegram_channel_integration/

Published Time: 2024-11-18T17:30:16+08:00

Markdown Content:
前言
--

最近在参与 [Follow](https://follow.is/) 以及 [RSSHub](https://github.com/DIYgod/RSSHub) 这两个开源项目的一些开发维护工作，因为牵扯到与很多订阅源的“斗智斗勇”，有一些很有意思的开发实践，于是开了这个新坑系列记录下来。

本篇是这几周使用 Telegram 官方 API 与 MTProxy 来实现对 TG 频道更新的开发实践与完整配置部署教程。

![Image 1: follow_telegram_channel](https://image.pseudoyu.com/images/follow_telegram_channel.png)

Follow 中提供了一种便捷的订阅信息源的方式，例如用户可以输入对应的 Telegram 频道名称来订阅某个频道的更新，这样就无须跳转到各个频道里去逐个查看，这一部分特性依赖的是背后 RSSHub 的实现。

![Image 2: rsshub_homepage](https://image.pseudoyu.com/images/rsshub_homepage.png)

RSS (Really Simple Syndication) 是一个古早的信息聚合标准，它通过统一的数据格式，让用户能够便捷地订阅和获取网站更新。然而，随着社交媒体和移动互联网的兴起，原生支持 RSS 的网站正在减少。

而 RSSHub 秉持着"万物皆可 RSS"的理念，通过开源社区的力量将包括 Telegram、YouTube、播客在内的众多现代内容平台转换为标准的 RSS 格式，让用户能够重新掌控自己的信息获取方式，远离算法推荐的干扰。

RSSHub 中现在包含了上千个平台，针对不同平台和类别也都有着包括但不限于网页爬虫、官方接口、逆向 API 调用等多种处理方式，能够涵盖绝大多数我们日常使用到的信息源，也非常适合作为对平台的一些加密算法和反爬机制学习的实践，例如下文所要介绍的 Telegram 频道 RSS 订阅的实现。

### Telegram 网页预览

![Image 3: yu_channel_online_preview](https://image.pseudoyu.com/images/yu_channel_online_preview.png)

由于 Telegram 提供了频道的网页预览功能，例如可以通过 [t.me/s/pseudoyulife](https://t.me/s/pseudoyulife) 这一链接直接查看我自己频道的更新，因此 RSSHub 很早之前就实现了通过抓取网页上的内容并转换为 RSS 格式的方式集成了对 Telegram 频道更新的订阅。

![Image 4: telegram_channel_reorx_preview](https://image.pseudoyu.com/images/telegram_channel_reorx_preview.png)

然而后来许多用户反馈说部分频道抓不到，去测试了一下，发现 Telegram 用一种黑盒的机制来限制了部分频道的网页预览功能，例如我一直在订阅的「[Reorx’s Forge](https://t.me/s/reorx_share)」以及「[Newlearnerの自留地](https://t.me/s/NewlearnerChannel)」等频道，当使用 `/s` 来访问页面时会被强制重定向，提示需要打开客户端来查看内容，因此对于这类频道我们没办法直接抓取到内容并转化为 RSS。

### Telegram APIs

为了解决这一问题， 我又去查了 Telegram 的官方文档，发现他们将 API 分为以下几种：

*   [Bot API](https://core.telegram.org/api#bot-api)
*   [TDLib](https://core.telegram.org/api#tdlib-build-your-own-telegram)
*   [Gateway API](https://core.telegram.org/api#gateway-api)
*   [Telegram API](https://core.telegram.org/api#telegram-api)

其中 Telegram API 中的有一个 [channels.getMessages](https://core.telegram.org/method/channels.getMessages) 方法可以返回某个频道的消息，可以满足我们的需求，具体的实现逻辑在 RSSHub 代码仓库 —— [lib/routes/telegram/channel.ts](https://github.com/DIYgod/RSSHub/blob/master/lib/routes/telegram/channel.ts) 和 [lib/routes/telegram/tglib](https://github.com/DIYgod/RSSHub/tree/master/lib/routes/telegram/tglib) 这两部分，有兴趣的朋友可以看一下代码。

#### 创建 Telegram App

![Image 5: manage_telegram_application](https://image.pseudoyu.com/images/manage_telegram_application.png)

使用 Telegram API 需要访问 [telegram core](https://my.telegram.org/)，通过手机号登录。

![Image 6: api_development_config](https://image.pseudoyu.com/images/api_development_config.png)

点击 API development tools 模块，创建一个 Telegram Application（详见「[Creating your Telegram Application](https://core.telegram.org/api/obtaining_api_id)」）。

![Image 7: telegram_api_id_hash](https://image.pseudoyu.com/images/telegram_api_id_hash.png)

在 App configuration 模块，我们能够获取到 `api_id`、`api_hash` 两个参数，记录下值，后续会用到。

#### 获取 Telegram Session

使用 Telegram API 新建一个 client 的流程比较严格，需要通过 SMS 验证手机号登录，在代码中交互获取使用并不现实，因为我们需要预先创建 client 并且获取其 session，后续直接通过 session 来使用 api。

![Image 8: get_telegram_session](https://image.pseudoyu.com/images/get_telegram_session.png)

拉取脚本「[pseudoyu/telegram-api-scripts](https://github.com/pseudoyu/telegram-api-scripts)」后，先运行 `npm i` 或 `pnpm i` 安装依赖，然后运行 `npm run start` 或 `node index.js`，按照提示输入 `api_id` 和 `api_hash` 和手机号（需要和申请 Telegram App 时的手机号一致），通过短信或 Telegram App 获取验证码后即可在命令行输出获取 session。

需要注意的是，由于我们后续需要在 RSSHub 服务中使用这个 session，尽量在 RSSHub 服务部署的同一服务器上运行脚本获取 session，这样能避免 Telegram 对于 IP、设备的一些限制。

> 注：如果 RSSHub 是使用的 Serverless 平台或其他方式，则也可以通过额外配置 MTProxy 的方式来保持 IP 一致，后文会详细说明。

#### （可选） 使用 MTProxy 保持 IP 一致

之前在 Follow 的 RSSHub 实例上添加了 Telegram API 相关逻辑和配置后，过一会儿就会报一个 `AuthKeyDuplicatedError` 错误，查看了一下很多开发者也遇到过 —— 「[AuthKeyDuplicatedError Eror problem #1488](https://github.com/LonamiWebs/Telethon/issues/1488)」，猜测是由于我们的 RSSHub 实例是 k8s 集群部署的，会从不同的机器调用 Telegram API，因而受到了一些限制。

于是又开始找针对这一情况的解决方案，发现 Telegram 提供了一种叫 MTProxy 的专属代理协议，可以通过部署一个 MTProxy Server 来代理所有的 API 请求，这样能够保障不同机器发送的请求都来自同一个 IP。

找到了「[Dofamin/MTProxy-Docker](https://github.com/Dofamin/MTProxy-Docker)」这个项目，拉取仓库后，新建一个 `.env` 文件，添加这一环境变量（默认的官方代码已经不怎么维护，这个版本添加了一些补丁）：

```
MTPROTO_REPO_URL=https://github.com/GetPageSpeed/MTProxy
```

`SECRET` 也可以选择自定义的值，`IP` 不填写则会自动通过 `curl ifconfig.co` 获取本机 IP，其他环境变量可以查看仓库的 `README.md` 文件自行修改。

配置完成后，运行 `docker compose up -d` 启动，代理服务则运行在 `<IP>:8443` 上。

> 注：如果 RSSHub 是通过 Docker、Docker Compose 等方式单实例进行部署，且能够保障在同一台部署机器上运行脚本获取 Session，则可以跳过这个代理步骤。

经过了上述的服务部署，我们获取了以下信息：

*   Telegram API 的 `api_id` 和 `api_hash`
*   Telegram 的 `session` 字符串
*   MTProxy 的 `SECRET`、`IP`、`PORT`

这时可以开始部署/更新我们的 RSSHub 实例了，具体可以根据[文档](https://docs.rsshub.app/deploy/)选择不同的方式，例如 Docker、Docker Compose、Serverless 等。

推荐通过 Docker Compose 的方式来部署，比较便于维护，需要在 `docker-compose.yml` 中添加如下变量：

```
environment:
  - TELEGRAM_API_ID=<Telegram API ID>
  - TELEGRAM_API_HASH=<Telegram API Hash>
  - TELEGRAM_PROXY_SECRET=<MTProxy SECRET>
  - TELEGRAM_SESSION=<Telegram Session>
  - TELEGRAM_PROXY_HOST=<MTProxy IP，如 123.123.123.123>
  - TELEGRAM_PROXY_PORT=8443
```

我是通过自己维护的[模板](https://zeabur.com/templates/X46PTP?referralCode=pseudoyu)部署在 Zeabur 平台上的，可视化部署，比较易用，只需要在部署完成后在 `Variables` 模块中添加以下变量并重启服务即可生效：

```
TELEGRAM_API_ID=<Telegram API ID>
TELEGRAM_API_HASH=<Telegram API Hash>
TELEGRAM_PROXY_SECRET=<MTProxy SECRET>
TELEGRAM_SESSION=<Telegram Session>
TELEGRAM_PROXY_HOST=<MTProxy IP，如 123.123.123.123>
TELEGRAM_PROXY_PORT=8443
```

#### 测试

![Image 9: yu_rsshub_homepage](https://image.pseudoyu.com/images/yu_rsshub_homepage.png)

经过上述步骤后，我们拥有了自己添加了 Telegram 相关配置的 RSSHub 实例，访问主页显示如上页面即部署成功，可以通过 `<RSSHub URL>/telegram/channel/<Channel Name>` 来订阅 Telegram 频道。

例如可以通过我的公开实例 [https://rsshub.pseudoyu.com/telegram/channel/NewlearnerChannel](https://rsshub.pseudoyu.com/telegram/channel/NewlearnerChannel) 来订阅「[Newlearnerの自留地](https://t.me/s/NewlearnerChannel)」频道。

总结
--

本篇记录了通过 Telegram API 在 RSSHub 中实现对部分受限制频道的更新订阅的开发实践与部署方案，受限于平台，方案可能会在未来某个时刻失效，我们也会持续研究更稳定的解决方案，使用中有任何问题可以留言或在 RSSHub 仓库中提 Issue 反馈/交流。

