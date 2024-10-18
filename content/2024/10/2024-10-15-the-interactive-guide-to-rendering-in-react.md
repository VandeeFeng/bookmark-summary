# The Interactive Guide to Rendering in React
- URL: https://ui.dev/why-react-renders
- Added At: 2024-10-15 13:41:53
- [Link To Text](2024-10-15-the-interactive-guide-to-rendering-in-react_raw.md)

## TL;DR
React渲染指南简介：React通过调用组件函数更新视图，渲染组件的过程包括创建快照和更新视图两步。根组件渲染初始视图，createRoot函数用于创建根元素。React只在组件状态变化时重新渲染组件，通过检查事件处理函数来确定状态变化。React.memo用于优化渲染，严格模式用于检查应用代码质量。

## Summary
# React 渲染指南

## 什么是渲染

* 渲染：React 调用组件函数以更新视图的过程
* 渲染组件的过程：
 + React 创建组件快照，捕获组件需要更新视图的数据（props、state、事件处理函数等）
 + React 利用快照更新视图

## React 如何渲染

* React 会渲染一个应用的根组件
* 使用 `createRoot` 函数创建应用的根元素
* 根元素渲染初始视图

### createRoot

* `createRoot` 函数接受一个 HTML 元素作为参数，返回一个根元素对象
* 根元素对象有一个 `render` 方法，用于渲染应用的初始视图

## React 何时重新渲染

*React 只会在组件的状态发生变化时重新渲染组件*

* 重新渲染组件时，React 会创建一个新的快照，并更新视图

## React 如何知道组件状态发生变化

* 当事件处理函数被调用时，React 会检查是否更新了组件的状态
* 如果状态发生变化，React 会重新渲染组件及其子组件

## React.memo

* `React.memo` 是一个高阶函数，接受一个组件作为参数，返回一个新的组件
* 新组件只会在其 props 发生变化时重新渲染

## 严格模式 (StrictMode)

* 严格模式是 React 的一种模式，用于检查应用的代码质量
* 在严格模式下，React 会重新渲染组件两次，以确保组件是pure的

### 启用严格模式

* 将 `StrictMode` 组件包裹在应用的根组件外
* 严格模式只在开发模式下有效，在生产模式下会被忽略
