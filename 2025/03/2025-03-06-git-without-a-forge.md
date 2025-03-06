# Git without a forge
- URL: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/git-no-forge/
- Added At: 2025-03-06 04:19:35
- [Link To Text](2025-03-06-git-without-a-forge_raw.md)

## Summary
**摘要**：
作者阐述了自己为何不使用 Git forge（如 GitLab 或 GitHub）来托管其开源项目代码的原因，而是选择使用“裸”Git 仓库。文章首先解释了如何与这种“裸”Git仓库交互，强调通过电子邮件发送 patch 仍然是可行的方案，并详细列出了作者个人对于接收 patch 的偏好顺序：首选包含 patch 的 Git 仓库 URL 和分支名称，其次是增量 Git bundle，再次是 `git format-patch` 生成的 patch 文件，然后是由 `git diff` 生成的 diff 文件，最不希望收到 `git send-email` 的输出。 接着，作者深入探讨了不使用 Git forge 的理由，包括对代码托管平台运营者的信任问题、Git forge 软件的笨重性、用户账户管理的繁琐、以及 Git forge 强加的工作流模式。此外，作者还提到了“纯粹的惯性”也是一个原因，以及明确表示不愿使用 GitHub，理由是 GitHub 不是自由软件，存在单点故障风险。最后，作者也承认了使用 Git forge 将所有交互公开化的优点，并表达了对结合两者优点的新系统的期望。

**要点总结**：

1.  **与“裸”Git 仓库交互的方式**：当没有“pull request”按钮时，可以通过电子邮件向作者发送包含代码更改的仓库 URL 或 patch 文件。作者最倾向于接收指向包含 patch 的 Git 仓库 URL 和分支名称的链接，因为这节省了空间，并简化了审查和合并流程。

2.  **增量 Git bundle 的优势**：Git bundle 是一种将整个 Git 仓库或其增量更改包装成单个文件的方式。增量 bundle 只包含原仓库没有的对象，文件小、二进制格式，作者很喜欢这种方式，可以使用git rebase命令，更好地处理冲突。

3.  **不信任第三方托管平台**：作者出于对代码安全的考虑，选择将代码托管在信任的朋友维护的服务器上，而不是大型商业公司提供的 Git forge 平台。托管平台的管理层变动可能导致信任风险。

4.  **Git forge 的工作流限制**：Git forge 强制用户使用其自带的 bug 追踪系统和 pull request 流程，作者希望自主选择适合自己项目的工作流，而不是被平台所限制，作者希望先决定如何处理patches和bug报告，然后再决定使用什么软件最好地满足这些需求。

5.  **避免形成技术垄断**：作者不愿使用 GitHub 是因为它不是自由软件，且 GitHub 的市场主导地位有形成技术垄断的风险。技术垄断由单一公司控制是很危险的，作者更倾向于贡献于互联网的分布式发展，而不是中心化。

