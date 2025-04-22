# This blog is hosted on a Nintendo Wii
- URL: https://blog.infected.systems/posts/2025-04-21-this-blog-is-hosted-on-a-nintendo-wii/
- Added At: 2025-04-22 03:29:14
- [Link To Text](2025-04-22-this-blog-is-hosted-on-a-nintendo-wii_raw.md)

## Summary
**摘要**：
作者分享了他将自己的博客托管在一台任天堂Wii上的实验。他提到自己一直对在非通用硬件上运行通用操作系统很感兴趣，并列举了一些例子，如PS3上的Yellow Dog Linux和PS2 Linux。作者发现NetBSD系统对Wii有良好的支持，并决定尝试在其上部署一个实际的生产环境。他从EMF Camp 2024 Swap Shop购得一台Wii，并使用Wilbrand漏洞安装Homebrew Channel，然后安装了NetBSD。作者通过USB键盘设置了SSH，并安装了`pkgin`包管理器，用于安装`lighttpd`等必要软件。由于Wii的性能限制，作者使用Caddy作为反向代理来处理TLS加密，并将LLM爬虫的请求过滤掉，以减轻Wii的负担。他还设置了状态监控页面，展示Wii的系统资源使用情况。实验结果表明，Wii作为Web服务器在性能上存在限制，但通过优化和反向代理可以满足基本需求。Wii的功耗约为18W，每月电费成本较低。总的来说，这次实验比作者预期的更成功，虽然存在一些缺点，但仍然很有趣，并能带来学习机会。

**要点总结**：
1.  **在非通用硬件上运行通用操作系统的兴趣**：作者一直对在非常规硬件上运行通用操作系统抱有浓厚的兴趣，之前的PS3 Linux和Dreamcast Linux的经历也印证了这一点。这次选择任天堂Wii，也是出于同样的探索精神。
2.  **NetBSD对Wii的良好支持**：在众多嵌入式Linux发行版中，NetBSD对Wii的支持是最新的，这让作者看到了将其用于实际生产环境的可能性。作者提到，NetBSD 10.1是最新稳定版本，甚至每日构建版本也支持Wii。
3.  **利用Homebrew Channel安装NetBSD**：作者通过Wilbrand漏洞，在Wii上安装了Homebrew Channel，相当于为Wii解锁了权限，使其能够运行未经官方认证的自制程序。然后，他将包含NetBSD系统的SD卡插入Wii，通过Homebrew Channel启动NetBSD系统。
4.  **使用Caddy作为反向代理**：由于Wii的PowerPC 750处理器性能有限，无法有效处理大量的加密连接，作者使用了Caddy作为反向代理服务器，分担了TLS加密和证书管理的压力。Caddy作为一个中间层，接收客户端的HTTPS请求，解密后将HTTP请求转发给Wii，极大地降低了Wii的计算负担。
5.  **功耗和成本分析**：作者对Wii的功耗进行了测试，得出结论是Wii在空闲状态下大约消耗18W的电力。按照英国的电价计算，每月的电费大约为3.47英镑，这甚至比许多云服务提供商提供的虚拟专用服务器(VPS)还要便宜。
