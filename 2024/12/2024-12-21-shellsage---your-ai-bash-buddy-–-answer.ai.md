# ShellSage - Your AI Bash Buddy – Answer.AI
- URL: https://www.answer.ai/posts/2024-12-05-introducing-shell-sage.html
- Added At: 2024-12-21 09:55:30
- [Link To Text](2024-12-21-shellsage---your-ai-bash-buddy-–-answer.ai_raw.md)

## Summary
**摘要**：
本文主要介绍了一个名为ShellSage的新工具，旨在解决在命令行界面（CLI）操作中的困难，特别是反复查阅文档、错误处理和与AI助手之间的上下文切换问题。ShellSage与llm工具类似，前者通过集成`tmux`来增强了上下文理解能力，允许它观察并与人类协同完成任务。项目背后的理念是促进人类与AI的协作，而不是取代人类，旨在为人类和AI提供共享上下文的工作环境。通过内嵌AI的建议和解释，ShellSage帮助用户在解决实际问题时学习正确的系统管理实践。

**要点总结**：
- **ShellSage的背景**：ShellSage是由Answer.AI开发的，旨在解决CLI使用中上下文切换的困难，通过实现AI与人类工作协同，共享相同工作环境中的上下文信息。
- **发展动力**：开发背景是Answer.AI自身开发者在开发复杂的系统如SolveIt时遇到的上下文切换问题，希望能有一个工具能保持人类和AI间的上下文同步。
- **功能实现**：ShellSage通过与`tmux`集成，获得终端的上下文信息，结合AI技术，实现了对实时操作的理解和协作，提供简洁的、针对性的回答，同时增强人类在问题解决过程中的学习能力。
- **应用实例**：通过与AI一起验证信息泄漏的可能原因（如LeetCode证书相关的CT日志问题），ShellSage展现了其在问题联合解决中的价值。
- **目标用户**：ShellSage面向所有技术级别，从首次接触命令行的开发者到有多年使用终端经验的高级开发者，通过提供背景信息、上下文理解和案例分享，帮助各种用户更有效地解决问题。
- **启动和运行**：安装ShellSage需要具有`tmux`的支持，对于不使用`tmux`的用户，可以使用`--NH`标志，但会失去部分上下文理解功能；对于命令行新手，ShellSage提供详细的使用指南，通过实例展示如何使用。
