# The Cursed Art of Streaming HTML
- URL: https://rinici.de/posts/streaming-html
- Added At: 2025-03-08 02:57:33
- [Link To Text](2025-03-08-the-cursed-art-of-streaming-html_raw.md)

## Summary
**摘要**：
作者介绍了一种利用 HTML 流式传输创建实时更新的方法，类似于 WebSocket 或 SSE，但无需 JavaScript。文章展示了如何通过简单的 HTML 结构和后端技术（如 Node.js 的 `res.write()`）实现一个简易的实时聊天应用。该应用使用 iframe 嵌入聊天历史记录和消息发送表单，并通过 Express 框架处理消息的发送和接收。文章还提到了使用 EventEmitter 在服务器端广播消息。虽然这种方法存在页面无法完成加载的问题，但作者提供了一个 JavaScript 片段作为临时解决方案，以确保页面在没有 JavaScript 的情况下也能正常工作，从而实现了渐进增强的用户体验。

**要点总结**：
1.  **HTML 流式传输**: 类似于 WebSocket 或 SSE，允许服务器向客户端实时推送 HTML 片段，无需等待整个页面加载完成。这种技术可以用于创建动态更新的 Web 页面。
2.  **`Connection: keep-alive`**: 现代浏览器在请求 HTML 时通常使用 `Connection: keep-alive`，允许服务器在同一连接上持续发送数据，这为 HTML 流式传输提供了基础。
3.  **iframe 嵌入**: 通过使用 iframe 嵌入聊天历史和消息发送表单，可以将页面的不同部分独立加载和更新，避免整个页面重新加载，提高用户体验。
4.  **后端技术实现**: 使用 Node.js 的 `res.write()` 函数可以实现服务器端的 HTML 流式传输。通过设置 `Content-Type` 为 `text/html`，服务器可以逐步向客户端发送 HTML 内容。
5.  **消息广播与资源管理**: 使用 EventEmitter（或更优的广播频道）在服务器端广播消息，并在客户端断开连接时移除监听器，可以有效管理服务器资源，避免资源泄漏。

