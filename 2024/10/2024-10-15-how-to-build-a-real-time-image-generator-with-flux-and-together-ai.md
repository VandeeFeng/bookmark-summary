# How to build a real-time image generator with Flux and Together AI
- URL: https://www.together.ai/blog/how-to-build-a-real-time-image-generator-with-together-ai
- Added At: 2024-10-15 10:36:01
- [Link To Text](2024-10-15-how-to-build-a-real-time-image-generator-with-flux-and-together-ai_raw.md)

## TL;DR
使用 Flux 和 Together AI，可以创建实时图像生成器。通过使用 React 和 Together AI 的 API，可以实现实时图像生成。用户可以在输入框中输入 prompt，应用程序会实时生成图像。同时，可以使用 Debounce 降低 API 请求频率，提高应用程序性能。应用程序还支持控制图像生成步数和随机性。

## Summary
**如何使用 Flux 和 Together AI 创建实时图像生成器**

**概述**

*   文中介绍了如何使用 Flux 和 Together AI 创建实时图像生成器
*   基于 BlinkShot 应用程序的源代码，展示了如何使用 React 和 Together AI 的 API 实现实时图像生成

**创建 Prompt 输入框**

*   BlinkShot 的核心交互是输入框，用户可以在其中输入 prompt
*   使用 React state 控制输入框的值
*   使用 `useQuery` Hook 从 React Query 中获取数据

**实时生成图像**

*   使用 Together AI 的 API 生成图像
*   将 prompt 传递给 API，并获取生成的图像
*   使用 Data URL 在页面中展示图像

**添加 API 路由**

*   创建新的 API 路由来处理图像生成请求
*   使用 Together AI 的 node SDK 生成图像

**优化图像生成**

*   使用 `steps` 选项控制图像生成步数
*   使用 `seed` 选项控制图像生成的随机性

**使用 Debounce**

*   使用 `useDebounce` Hook 延迟 API 请求
*   降低 API 请求频率，提高应用程序性能

**示例**

*   生成图像示例
*   控制图像生成步数示例
*   控制图像生成随机性示例

**结论**

*   使用 Flux 和 Together AI 可以创建实时图像生成器
*   通过优化图像生成和使用 Debounce，可以提高应用程序性能
*   BlinkShot 的源代码可以作为参考，帮助您创建自己的实时图像生成应用程序
