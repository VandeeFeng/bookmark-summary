# Redirecting URLs with CloudFlare
- URL: https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/
- Added At: 2024-12-06 05:55:59
- [Link To Text](2024-12-06-redirecting-urls-with-cloudflare_raw.md)

## Summary
**摘要**：
Christian Kjær迁移了博客，并在CloudFlare门户解决旧链接造成的问题。他采用CloudFlare的“重定向规则”将旧博客的链接重定向至新地址，避免了为每个帖子编写重写规则。Key steps 包括：
1. 将基域名从`codetalk.io`更改到`codethoughts.io`。
2. 在`/posts/`路径下托管所有帖子。
3. 告别旧版HTML链接结束符。
4. 在CloudFlare的“重定向规则”中创建规则，首先捕获请求，接着重新导向至新位置。
5. 使用`Dynamic`规则重定向，利用`lower()`、`substring()`和`concat()`函数对路径进行修正以适配新格式。

**要点总结**：
1. **切换环境**：详细阐述博客迁移到新域名codethoughts.io及调整路径结构（移除HTML扩展名）的过程。
2. **云防火墙整合**：重点介绍在云防火墙Dashboard中创建重定向规则的步骤，并利用特定路径表达式（`/posts/`）选择性捕获请求。
3. **实现重定向**：以具体表达式`concat("https://codethoughts.io", substring(lower(http.request.uri.path), 0,-5))`实现动态重定向，对路径进行Lowercase化和调整，简化URL结构。
4. **基于免费计划**：说明项目运行在免费计划下，利用可适用规则进行构建，说明避免使用复杂规则如正则表达式的原因。
5. **测试与反馈**：建议用户通过Medium或者评论区与作者互动，从而测试和制定改进方案。
