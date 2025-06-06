# Why "alias" is my last resort for aliases
- URL: https://evanhahn.com/why-alias-is-my-last-resort-for-aliases/
- Added At: 2025-03-08 02:55:47
- [Link To Text](2025-03-08-why-alias-is-my-last-resort-for-aliases_raw.md)

## Summary
**摘要**：
作者分享了自己使用 alias 的经验，最初使用 alias 是为了简化常用命令，例如将 `git` 简化为 `g`。但随着时间的推移，作者发现使用 `$PATH` 中的脚本来实现 alias 更有优势。脚本的优点包括：无需重新加载配置文件，修改后立即生效；可以选择编程语言，不局限于 Zsh；有更大的工作空间，可以编写更复杂的逻辑；以及更强的可移植性，方便在不同 Shell 之间切换。但是，alias 也有其优点，例如拥有特殊的权限，可以实现脚本无法实现的功能；能够保留命令补全功能；可以条件性地定义，以及更容易绕过。此外，alias 在简洁性和性能方面也略胜一筹。虽然 alias 和脚本各有优劣，但作者更倾向于使用脚本，因为它们的功能更强大。

**要点总结**：

1.  **脚本无需重新加载配置文件：** 当使用脚本作为别名时，对脚本的修改（如创建、更新或删除）会立即生效，无需像使用 `alias` 命令那样手动重新加载 `.zshrc` 文件。这提高了迭代效率，使得更改别名更加便捷。

2.  **脚本可以选择编程语言：** 使用脚本作为别名，可以选择任何编程语言来编写脚本，而不仅限于 Zsh。作者举例，其 `note` 脚本使用 Python 编写，而 `sleepybear` 脚本则根据 Linux 或 macOS 系统选择不同的休眠逻辑。

3.  **脚本有更大的工作空间：** 脚本提供了更大的空间来编写复杂的逻辑，这对于需要处理多种情况或包含较多代码的别名非常有用。例如，作者的 `sleepybear` 脚本，用脚本更容易编码在不同系统上的休眠逻辑，如果用`alias`命令则难以实现。

4.  **Alias拥有特殊权限：** `alias` 和 shell 函数拥有脚本无法实现的特殊权限。例如，可以使用 `alias` 来纠正常见的拼写错误，或者使用 shell 函数根据前一个命令的退出状态发出声音提示。这些功能是脚本无法直接实现的。

5.  **Alias更容易绕过：** 在某些情况下，可能需要临时禁用某个别名。使用 `alias` 定义的别名可以通过反斜杠（`\`）轻松绕过，而脚本则需要使用完整路径或修改 `$PATH` 变量才能禁用。

