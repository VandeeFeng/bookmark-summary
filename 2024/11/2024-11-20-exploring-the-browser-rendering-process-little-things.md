# Exploring the browser rendering process | Little Things
- URL: https://abhisaha.com/blog/exploring-browser-rendering-process/
- Added At: 2024-11-20 02:27:19
- [Link To Text](2024-11-20-exploring-the-browser-rendering-process-little-things_raw.md)

## Summary
**摘要**：
文章提供了详细说明了浏览器渲染过程的复杂性，从用户输入网址到网页内容在屏幕上呈现的环节。过程包括DNS解析、TCP/TLS握手、HTTP请求响应周期、HTML和CSS的解析、DOM树和CSSOM树的创建，最终是渲染树的创建。文章特别探讨了布局和绘画两个关键步骤，解析了CSS属性如何影响页面元素的定位。

**要点总结**：

1. **DNS解析**：输入网址后，浏览器需通过DNS查询将域名解析为IP地址，以定位网站服务器。
2. **TCP/TLS握手**：建立连接后，进行TCP握手，并在HTTPS情况下执行TLS握手以确保安全的数据传输。
3. **HTTP请求响应周期**：请求完成后，服务器返回内容，涉及到编码和数据传输。
4. **HTML和CSS解析**：浏览器将HTML作为原始数据读入，转换为单独的字符和标记，构成DOM和CSSOM树。
5. **布局**与**绘画**：布局决定页面元素的确切位置和大小，绘画则将视觉表示渲染到屏幕上。CSS属性对页面元素的排列方式起着核心作用。

了解这些底层机制有助于开发性能更优的网站。文章详细介绍了浏览器渲染过程中的关键步骤，后者可以被进一步划分为 DNS、TCP/TLS、HTTP 请求/响应、DOM 创建、CSSOM 创建、生成渲染树、布局、绘画等几个阶段。
