---
title: Why "alias" is my last resort for aliases
date: 2025-03-08
extra:
  source: https://evanhahn.com/why-alias-is-my-last-resort-for-aliases/
  original_title: Why "alias" is my last resort for aliases
---
## Summary
**摘要**：
作者分享了自己使用 alias 的经验，最初使用 alias 是为了简化常用命令，例如将 `git` 简化为 `g`。但随着时间的推移，作者发现使用 `$PATH` 中的脚本来实现 alias 更有优势。脚本的优点包括：无需重新加载配置文件，修改后立即生效；可以选择编程语言，不局限于 Zsh；有更大的工作空间，可以编写更复杂的逻辑；以及更强的可移植性，方便在不同 Shell 之间切换。但是，alias 也有其优点，例如拥有特殊的权限，可以实现脚本无法实现的功能；能够保留命令补全功能；可以条件性地定义，以及更容易绕过。此外，alias 在简洁性和性能方面也略胜一筹。虽然 alias 和脚本各有优劣，但作者更倾向于使用脚本，因为它们的功能更强大。

**要点总结**：

1.  **脚本无需重新加载配置文件：** 当使用脚本作为别名时，对脚本的修改（如创建、更新或删除）会立即生效，无需像使用 `alias` 命令那样手动重新加载 `.zshrc` 文件。这提高了迭代效率，使得更改别名更加便捷。

2.  **脚本可以选择编程语言：** 使用脚本作为别名，可以选择任何编程语言来编写脚本，而不仅限于 Zsh。作者举例，其 `note` 脚本使用 Python 编写，而 `sleepybear` 脚本则根据 Linux 或 macOS 系统选择不同的休眠逻辑。

3.  **脚本有更大的工作空间：** 脚本提供了更大的空间来编写复杂的逻辑，这对于需要处理多种情况或包含较多代码的别名非常有用。例如，作者的 `sleepybear` 脚本，用脚本更容易编码在不同系统上的休眠逻辑，如果用`alias`命令则难以实现。

4.  **Alias拥有特殊权限：** `alias` 和 shell 函数拥有脚本无法实现的特殊权限。例如，可以使用 `alias` 来纠正常见的拼写错误，或者使用 shell 函数根据前一个命令的退出状态发出声音提示。这些功能是脚本无法直接实现的。

5.  **Alias更容易绕过：** 在某些情况下，可能需要临时禁用某个别名。使用 `alias` 定义的别名可以通过反斜杠（`\`）轻松绕过，而脚本则需要使用完整路径或修改 `$PATH` 变量才能禁用。

## Full Content
Title: Why "alias" is my last resort for aliases

URL Source: https://evanhahn.com/why-alias-is-my-last-resort-for-aliases/

Published Time: 2025-03-05T00:00:00+00:00

Markdown Content:
by [Evan Hahn](https://evanhahn.com/)

, updated Mar 6, 2025 (originally posted Mar 5, 2025)

Aliases were one of the first things I added when customizing my dotfiles. For example, here’s a very early alias I defined:

Now, I can run `g` instead of `git`, which saves me a little time for a command I run dozens of times a day!

```
# These two commands are now equivalent:
git status
g status
```

I used to define these aliases with `alias`. After all…I’m defining an alias!

But over time, I think I discovered a better way: **a script in my `$PATH`**.

How it works
------------

In my home directory, I have a folder of scripts called `bin`. For example, here’s a simplified version of `~/bin/g`:

```
#!/usr/bin/env bash
exec git "$@"
```

Running this script basically just runs `git`.

I add this folder to my `$PATH`. (See [Julia Evans’s guide on how to do this](https://jvns.ca/blog/2025/02/13/how-to-add-a-directory-to-your-path/).) In my `.zshrc`, I have a line like this:

```
export PATH="$HOME/bin:$PATH"
```

Now, when I type `g`, it runs that script.

This behaves just like an alias. As before, `g status` and `git status` are equivalent.

```
# These two commands are still the same:
git status
g status
```

This is a lot more verbose than `alias`. So _why do it this way?_

Benefits of scripts over aliases
--------------------------------

Scripts have several advantages over using `alias`:

*   **No reloading; changes are picked up immediately.** When I create, update, or delete an `alias`, I have to reload my `.zshrc`. I do this by opening a new terminal tab or running `source ~/.zshrc`. But with scripts, I don’t have to! I can just edit files in `~/bin` and they’re immediately ready. This makes it easier to iterate.
    
*   **Choice of programming language.** I use Bash for a lot of my scripts, but not all. For example, I have a note-taking script called [`~/bin/note`](https://gitlab.com/EvanHahn/dotfiles/-/blob/42af33e66387598b174694e3c088ba39d823f8ad/home/bin/bin/note) which I didn’t want to write in Bash, so I wrote it in Python instead. With an alias, I’d _have_ to write it in Zsh.
    
*   **More space to work.** Aliases are typically for simple things, like running `git` when you type `g`. But I have some scripts in `~/bin` that are a little more complex. For example, [`~/bin/sleepybear`](https://gitlab.com/EvanHahn/dotfiles/-/blob/42af33e66387598b174694e3c088ba39d823f8ad/home/bin/bin/sleepybear) puts my computer to sleep, which has different logic on Linux versus macOS. It’s easier to encode that logic in a script than an alias. (I could also do this with a shell function.)
    
*   **More portable.** I usually use Zsh, but I _occasionally_ use Bash and am interested in giving [Fish](https://fishshell.com/) another try. If I used aliases, I’d have to manually port things over to my new shell. With a `~/bin` directory, it’s much less work: just add it to my `$PATH` environment variable and I’m done.
    

These benefits are enough to convince to use scripts as my default, even for simple aliases like `g=git`.

Benefits of aliases over scripts
--------------------------------

Scripts are my preference but they aren’t perfect. Everything in programming has tradeoffs!

There are a few things that are better about `alias`:

*   **Special powers.** `alias` and shell functions have special powers that scripts don’t. For example, I [alias `cd..` to `cd ..`](https://gitlab.com/EvanHahn/dotfiles/-/blob/42af33e66387598b174694e3c088ba39d823f8ad/home/zsh/.config/zsh/aliases.zsh#L33) because I make that typo a lot. I also have a shell function, [`boop`](https://gitlab.com/EvanHahn/dotfiles/-/blob/42af33e66387598b174694e3c088ba39d823f8ad/home/zsh/.config/zsh/aliases.zsh#L56-64), which makes a sound based on the exit status of the previous command. As far as I know, a shell script can’t do these things. It can’t change the working directory of the outer process and it doesn’t know other processes’ exit statuses. If it’s difficult/impossible to do with a script, I fall back to an alias or a shell function.
    
*   **Keep your completions.** [pwagland mentioned an advantage of `alias` on Hacker News](https://news.ycombinator.com/item?id=43266323): completions. Aliasing `git` with `alias g=git` will allow completions to work if you type `g <tab>`. This doesn’t work with scripts without some effort.
    
*   **Conditional definition.** It’s harder to conditionally define a file in `~/bin` than it is to conditionally define an alias. For example, I love the `open` command that comes with macOS. On Linux, where it doesn’t exist, [I define an alias with `alias`](https://gitlab.com/EvanHahn/dotfiles/-/blob/42af33e66387598b174694e3c088ba39d823f8ad/home/zsh/.config/zsh/linux.zsh#L13). This alias doesn’t exist on macOS at all because I define it conditionally.
    
*   **Easier to bypass.** I alias `vim` to `nvim`, but _occasionally_ I want to run the real Vim. Bash and Zsh offer [a few ways to bypass aliases](https://unix.stackexchange.com/a/39296/101918); for example, I could run `\vim`. With a shell script in my `$PATH`, I can’t do this. The only way to bypass these is to use the full path, such as `/usr/bin/vim`, to temporarily remove `~/bin` from my `$PATH`, or temporarily move the whole script.
    
*   **Brevity.** When I create a new script, I have to create a new file in `~/bin`, put `#!/usr/bin/env bash` at the top, and make the file executable. This isn’t so bad, but it’s a bit faster to type `alias g=git`. (To make this easier, I wrote [a script called `mksh`](https://gitlab.com/EvanHahn/dotfiles/-/blob/2c9df0139a6960a53a4c490ef3017171d0eedfda/home/bin/bin/mksh) which does this.)
    
*   **Performance.** In an informal test I ran, `alias`es are more than 100× faster. That makes sense; the computer has to find a file in your `$PATH` on disk, parse it, and execute it—slower than just running a command it probably stores in memory. In practice, I have never noticed this performance difference, but maybe I would if I were running `g` hundreds of times a second.
    

Choose your favorite
--------------------

Ultimately, this decision doesn’t make much difference. Both methods—aliases and scripts—are pretty similar. But for me, I default to using scripts because I like what they can do.

