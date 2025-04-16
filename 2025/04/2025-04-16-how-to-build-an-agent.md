# How To Build An Agent
- URL: https://ampcode.com/how-to-build-an-agent
- Added At: 2025-04-16 03:15:38
- [Link To Text](2025-04-16-how-to-build-an-agent_raw.md)

## Summary
**摘要**：
本文作者分享了如何用不到400行代码创建一个功能完善的代码编辑Agent。实现一个Agent的核心要素包括大型语言模型（LLM）、一个循环以及足够的tokens。文章通过逐步构建一个Go项目，展示了如何利用Anthropic API与Claude进行交互，实现Agent的基本功能。首先，创建了一个能与Claude对话的命令行聊天应用。然后，引入了“工具”的概念，通过定义`read_file`、`list_files`和`edit_file`这三个工具，赋予Agent读取文件、列出文件和编辑文件的能力。`read_file`允许Agent读取指定文件的内容，`list_files`让Agent能够列出指定目录下的文件和目录，而`edit_file`则允许Agent通过替换文件中的字符串来修改文件。通过结合使用这些工具，Agent能够完成诸如创建、修改JavaScript文件等复杂任务。作者强调，实现这些功能并不需要复杂的算法或深奥的理论，而是主要依赖于LLM的能力、合理的工具设计以及一定的工程实践。

**要点总结**：

1.  **Agent构建的核心要素**：构建一个代码编辑Agent的核心在于LLM、一个循环以及足够的tokens。LLM负责理解和生成代码，循环用于持续交互和执行任务，而足够的tokens则保证了信息的完整传递。
2.  **工具的概念与实现**：工具是Agent与外部世界交互的桥梁。通过定义工具，Agent可以执行读取文件（`read_file`）、列出文件（`list_files`）和编辑文件（`edit_file`）等操作。每个工具都需要一个名称、描述、输入模式和执行函数。
3.  **`read_file`工具**：该工具允许Agent读取指定路径的文件内容。通过向LLM提供文件内容，Agent可以分析文件内容，从而更好地理解任务需求。
4.  **`list_files`工具**：该工具允许Agent列出指定路径下的文件和目录。通过获取文件列表，Agent可以了解项目的整体结构，从而更好地定位和修改文件。
5.  **`edit_file`工具**：该工具允许Agent通过替换字符串的方式编辑文件。是Agent执行代码修改的核心手段。虽然简单，但结合LLM的理解能力，可以实现复杂的代码编辑任务。通过`edit_file`工具，Agent可以创建新文件、修改现有文件，甚至可以完成代码的rot13解码等复杂任务。
