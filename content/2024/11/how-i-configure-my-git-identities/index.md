---
title: How I configure my Git identities
date: 2024-11-26
extra:
  source: https://benji.dog/articles/git-config/
  original_title: How I configure my Git identities
---
## Summary
**摘要**：
本文作者介绍了如何利用 Git 的高级配置功能，特别是一些条件性配置方法，来高效地管理多个 Git 身份和 SSH 密钥。文章详细解释了如何通过 `includeIf` 条件段落来根据代码仓库实际位置更改 Git 配置，并说明如何利用 `hasconfig` 来指定性地修改配置项根据仓库的远程 URL 来实现对不同服务和组织代码库的配置差异。对于如何通过 SSH 配置使用不同的 SSH 密钥进行仓库的克隆、拉取和推送，作者也列举了例子，包括如何在 `~/.ssh/config` 文件中设置含有多个 host 存储库与对应 SSH 密钥链接的配置。

**要点总结**：
- **配置管理入口**：作者介绍了利用 `includeIf` 语句的条件性包含功能，在 dotfiles 中创建与特定代码路径相关的 Git 配置部分。
- **远程 URL 条件配置**：通过 `hasconfig` 条件实现对 Git 配置的更细粒度管理，以自动化根据远程 URL 来应用不同的 Git 配置。
- **多代码库下 Git 密钥管理问题**：当工作涉及多个代码仓库和多个使用不同 GitHub 帐户时，如何在不同环境（如工作与个人）间实现 Git 身份和 SSH 证书的切换，以适配不同的身份验证需求。
- **SSH 多数实例设置与解析**：展示如何在 `~/.ssh/config` 文件内配置多个实例来管理不同的远程主机（GitHub、GitLab、git.sr.ht 等不同平台），实现对单一或特定组织代码仓库的专用 SSH 实例，简化仓库访问过程中的 SSH 密钥切换操作。

综上所述，本文的中心观点是通过合理利用 Git 和 SSH 的配置管理功能，实现代码仓库与对应身份和访问权限的一致性匹配，从而高效地管理多个高频率使用的代码库及其相关的认证机制。
## Full Content
Title: How I configure my Git identities

URL Source: https://benji.dog/articles/git-config/

Markdown Content:
> **Note**: I've had this post drafted for 3 YEARS!!! It's finally time to publish it.

I like to mess with my [dotfiles](https://github.com/benjifs/dotfiles) and every so often, I find out about a new way to do things and I spend more time than I should learning how to use it.

A few years ago I learned about [includeIf](https://git-scm.com/docs/git-config#_includes) for including specific files if some condition was met for `git`. The example that I first saw was doing:

```
[includeIf "gitdir:~/code/**"]
  path = ~/.config/git/personal
[includeIf "gitdir:~/work/**"]
  path = ~/.config/git/work
```

So that `~/.config/git/personal` is only included for `git` directories under `~/code` and `~/.config/git/work` is only included for directories under `~/work`. The contents of those included files varies but usually it contains your git identity, signing keys, etc. Here's an example of what that could look like:

```
[user]
  name = benji
  email = benji@work.com
  signingkey = ~/.ssh/work.id_ed25519.pub
```

That works pretty well but I usually organize all my code in `~/workspace` regardless of whether its personal, **work-1**, **work-2**, etc. I wanted to be able to configure git depending on where that repo actually lives instead of where the directory is in my machine. Then I found out about [hasconfig:remote.\*.url:](https://git-scm.com/docs/git-config#Documentation/git-config.txt-codehasconfigremoteurlcode)!

This makes it so that I can configure git conditionally if the given remote URL exists for that directory I'm currently working in.

A few examples of what I do is:

```
[includeIf "hasconfig:remote.*.url:git@github.com:orgname/**"]
  path = ~/.config/git/config-gh-org

[includeIf "hasconfig:remote.*.url:git@github.com:*/**"]
  path = ~/.config/git/config-gh

[includeIf "hasconfig:remote.*.url:git@gitlab.com:*/**"]
  path = ~/.config/git/config-gl

[includeIf "hasconfig:remote.*.url:git@git.sr.ht:*/**"]
  path = ~/.config/git/config-srht
```

Now if I'm in a directory where the remote matches `github.com:orgname/**` it would use `~/.config/git/config-gh-org`, otherwise it uses the general config file for any other GitHub repo.

* * *

While that handles git identities, I still need to configure SSH keys separately to be able to `pull` and `push` to remotes. The simple version of my `~/.ssh/config` looks like this:

```
Host gitlab.com
Hostname gitlab.com
User git
IdentityFile ~/.ssh/gitlab.id_ed25519

Host github.com
Hostname github.com
User git
IdentityFile ~/.ssh/github.id_ed25519
```

The only problem with this is that in order to use a different `IdentityFile` for the same `Hostname` so that I could use a different key for repos under `github.com/orgname`, I'd have to use a different value for `Host`. So in my case I would add the following to my `~/.ssh/config`:

```
Host gh-work
Hostname github.com
User git
IdentityFile ~/.ssh/work.id_ed25519
```

Finally, to use that `Host` when I'm looking for a repo in `github.com/orgname`, I would add the following to my git config:

```
[url "gh-work:orgname"]
  insteadOf = git@github.com:orgname
```

So when I `clone`, `pull`, or `push` a repo that's under my work's org account I can do:

```
git clone git@github.com:orgname/project
```

and `insteadOf` would replace `github.com:orgname` with `gh-work:orgname` so that it uses the right info from my SSH config. It's a neat trick which I saw referenced in this [article](https://www.kenmuse.com/blog/ssh-and-multiple-git-credentials/#git).

* * *

Are there any issues with this approach? Is there a better way to do this? I'm not sure so please let me know as I'd love to learn and I'll update this post accordingly.

References
----------

*   [https://fundor333.com/post/2021/advance-git-config-and-ssh-config/](https://fundor333.com/post/2021/advance-git-config-and-ssh-config/)
*   [https://www.kenmuse.com/blog/ssh-and-multiple-git-credentials/#git](https://www.kenmuse.com/blog/ssh-and-multiple-git-credentials/#git)
*   [https://garrit.xyz/posts/2023-10-13-organizing-multiple-git-identities](https://garrit.xyz/posts/2023-10-13-organizing-multiple-git-identities)
*   [https://stevenharman.net/configure-ssh-keys-for-multiple-github-accounts](https://stevenharman.net/configure-ssh-keys-for-multiple-github-accounts)

