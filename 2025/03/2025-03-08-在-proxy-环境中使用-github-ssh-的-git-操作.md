# 在 Proxy 环境中使用 GitHub SSH 的 git 操作
- URL: https://blog.inoki.cc/2025/03/08/GitHub-ssh-connection-behind-proxy/index.html
- Added At: 2025-03-08 10:46:24
- [Link To Text](2025-03-08-在-proxy-环境中使用-github-ssh-的-git-操作_raw.md)

## Summary
**摘要**：
本文主要介绍了在特定网络环境下，当GitHub的SSH端口（22）被封禁时，如何通过其他方式使用SSH协议进行git操作。通常，HTTP_PROXY、HTTPS_PROXY和ALL_PROXY环境变量只对HTTPS协议的git操作有效，对SSH无效。针对这种情况，文章提出了三种解决方案：一是手动在git clone或git pull命令中使用ssh.github.com并指定端口为443；二是修改SSH配置文件（~/.ssh/config），将github.com别名设置为ssh.github.com并使用443端口；三是配置SOCKS5代理，使SSH通过代理连接GitHub。作者建议根据实际网络环境选择最适合的方法，以确保可以顺利访问GitHub，进行正常的代码仓库操作。

**要点总结**：

1.  **问题背景：** 在某些网络环境下，GitHub的SSH 22端口可能被封禁，导致无法正常使用SSH协议进行git操作，通常公司网络环境也可能存在类似情况。
2.  **HTTPS连接的局限性：**  HTTP_PROXY、HTTPS_PROXY 和 ALL_PROXY 仅对 HTTPS 协议的 git 操作有效，无法解决 SSH 端口被封禁的问题，使用HTTPS协议需要配置GitHub的login集成或者使用token来进行私有仓库操作。
3.  **解决方案一：手动指定SSH连接** 通过直接在git命令中使用`ssh://git@ssh.github.com:443/your-repo.git`来指定使用443端口进行SSH连接，绕过22端口的限制。但这种方法需要修改所有用到的仓库地址。
4.  **解决方案二：修改SSH配置文件** 修改`~/.ssh/config`文件，将`github.com`的HostName设置为`ssh.github.com`，Port设置为443，User设置为git, 使得SSH连接GitHub时自动使用443端口。这样可以全局生效，无需每次手动指定。
5.  **解决方案三：使用SOCKS5代理** 通过设置SOCKS5代理，让SSH通过代理服务器连接GitHub。需要在`~/.ssh/config`文件中配置`ProxyCommand`，指定本地SOCKS5代理的地址和端口。同时，也可以使用 `GIT_SSH_COMMAND` 环境变量来修改默认 SSH 连接命令。
