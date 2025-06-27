# 让 Claude Code 使用其他模型
- URL: https://nekonull.me/share/claude-code-3rd-party-model/
- Added At: 2025-06-27 06:56:09
- [Link To Text](2025-06-27-让-claude-code-使用其他模型_raw.md)

## Summary
**摘要**：文章介绍了如何让Claude Code使用非官方的第三方模型提供商的方法。首先指出市面上大多数agent项目都支持OpenAI兼容API格式的模型提供商，但Claude Code只能使用自家模型的问题。作者通过使用Claude Bridge项目作为中间层，实现了请求格式的转换：拦截对Anthropic官方的请求，转换成OpenAI格式后调用第三方提供商，再将响应转换回Claude格式。文章详细说明了安装步骤、API Key配置方法和运行命令，并给出了这种方法的适用场景和已知限制，包括token计数不准、不能输入图片等功能限制。这种方法主要适合个人探索和side project使用，无法满足生产环境的所有需求。

**要点总结**：
1. 通过Claude Bridge项目实现Claude Code调用第三方模型：该项目作为中间层转换请求格式，拦截官方请求转成OpenAI格式调用第三方服务，再将流式响应转回Claude格式。
2. 安装依赖的具体步骤：需要分别安装官方的claude-code和claude-bridge两个npm包才能实现该功能。
3. API Key配置方法：通过在设置文件中指定apiKeyHelper脚本路径，并创建可执行脚本输出API Key（实际可使用任意值）来绕过官方登录限制。
4. 运行时的参数配置：使用claude-bridge命令时需要指定提供商格式、模型名称、API Key等参数，支持多种提供商格式。
5. 该方法存在的功能性限制：包括token计数不准、不支持图片输入、网络搜索功能不可用以及thinking/reasoning部分可能无法解析等问题。
