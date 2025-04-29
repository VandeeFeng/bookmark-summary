# Categorize Your Dependencies
- URL: https://antfu.me/posts/categorize-deps
- Added At: 2025-04-29 03:33:47
- [Link To Text](2025-04-29-categorize-your-dependencies_raw.md)

## Summary
**摘要**：
本文探讨了在项目开发中依赖项分类的问题，指出传统的`dependencies`和`devDependencies`分类方式已不足以清晰表达依赖项的用途。作者认为，这种分类最初是为Node.js库设计的，但随着前端项目的复杂性增加，工具为了提供更好的开发者体验而重载了这两种分类的含义，导致其用途变得模糊。为了更清晰地表达依赖项的用途，作者建议采用更细粒度的分类方式，例如`test`、`lint`、`build`、`frontend`等。并介绍了pnpm的Catalogs功能，它允许在monorepo工作区中集中管理和共享依赖项版本，通过命名目录可以实现更灵活的依赖项分类，方便版本升级和依赖项变更审查。同时，作者还分享了为pnpm Catalogs开发的VS Code扩展PNPM Catalog Lens，以及对taze、eslint-plugin-pnpm等工具的适配，以提供更好的工具支持。最后，作者展望了依赖项分类在Vite、unbuild等工具中的应用，以及在漏洞报告和代码检查方面的潜力，并鼓励大家尝试这种新的依赖项管理方式。

**要点总结**：
1.  **传统依赖分类的局限性**：文章指出，`dependencies`和`devDependencies`这两种分类方式在现代前端项目中已经无法准确描述依赖项的用途，工具为了提供更好的开发者体验而重载了这两种分类的含义，导致其用途变得模糊，无法清晰表达依赖项的真实作用。
2.  **更细粒度的依赖分类建议**：作者建议采用更细粒度的依赖分类方法，例如`test`（测试依赖）、`lint`（代码检查依赖）、`build`（构建依赖）、`frontend`（前端依赖）等，以便更清晰地表达每个依赖项的用途，从而提高项目的可维护性和可理解性。
3.  **pnpm Catalogs 的引入与应用**：介绍了pnpm的Catalogs功能，它允许在monorepo工作区中集中管理和共享依赖项版本。通过命名目录，可以实现更灵活的依赖项分类，并可以在`pnpm-workspace.yaml`文件中添加注释，为团队成员提供更多上下文信息，方便版本升级和依赖项变更审查。
4.  **PNPM Catalog Lens VS Code 扩展**：为了解决使用pnpm Catalogs后在`package.json`中无法直观查看依赖项版本的问题，开发了一款名为PNPM Catalog Lens的VS Code扩展，该扩展可以在`package.json`中内联显示已解析的版本，并为每个命名类别添加不同的颜色，方便识别。
5.  **未来展望与工具集成**：展望了依赖分类在Vite、unbuild等工具中的应用，例如Vite可以更精确地控制依赖优化，unbuild可以更灵活地控制外部化和内联，以及在漏洞报告和代码检查方面提供更有价值的上下文信息。同时，作者也分享了对taze、eslint-plugin-pnpm等工具的适配，以提供更好的工具支持。

