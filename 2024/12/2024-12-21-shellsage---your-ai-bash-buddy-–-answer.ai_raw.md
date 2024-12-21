Title: ShellSage - Your AI Bash Buddy – Answer.AI

URL Source: https://www.answer.ai/posts/2024-12-05-introducing-shell-sage.html

Markdown Content:
The Problem with Terminals
--------------------------

We’ve all been there - staring at the terminal, trying to remember that obscure [`tar`](https://linux.die.net/man/1/tar) command or the right flags for [`ssh`](https://linux.die.net/man/1/ssh). Sure, you could Google it, but then you’re context-switching between documentation, Stack Overflow, and your terminal. Or maybe you’re using an AI assistant like ChatGPT or Claude, but now you’re copying and pasting between windows, losing your terminal context, and getting walls of text that don’t quite fit your specific situation.

This context switching isn’t just inconvenient - it breaks one of the fundamental principles we’ve discovered for effective human-AI collaboration: maintaining shared context. When you copy-paste snippets between windows or try to describe your problem to an AI assistant, you’re creating an artificial barrier between human and machine thinking. We’ve found that the most powerful collaboration happens when both human and AI can see and understand the same complete context, right where the work is happening.

![Image 9](https://www.answer.ai/posts/shell_sage/llm_tar.png)

Me using llm to learn about tar

I found myself in this situation constantly when I discovered Simon Willison’s excellent [`llm`](https://pypi.org/project/llm/) tool. It allows you to chat with an AI assistant right in your terminal. While `llm` is great for many things, it wasn’t quite what I needed for these sysadmin tasks. The responses were often verbose walls of text that required scrolling through my terminal, and they didn’t always warn me about the gotchas that come with powerful commands. Most importantly, it couldn’t see what I was actually doing in my terminal - the context that could help it give me more relevant answers.

This pain point became particularly acute during our development of [SolveIt](https://solveit.fast.ai/) at [Answer.AI](https://answer.ai/). We were juggling multiple sysadmin tasks - setting up [Caddy](https://caddyserver.com/) for reverse proxies, managing [Docker](https://www.docker.com/) containers, configuring [Linux quotas](https://linux.die.net/man/8/xfs_quota) - and the context switching between documentation, our Claude Projects, and the terminal was becoming a real bottleneck. The cognitive load of jumping between these different interfaces was slowing us down and making it harder to learn from our experiences.

What we needed wasn’t just an AI that could recite documentation - we needed a teaching assistant that could see what we were doing, understand our context, and help us learn while solving immediate problems. That’s when [ShellSage](https://github.com/AnswerDotAI/shell_sage) (code named BashBuddy) was born. Here is what the same output looks like with ShellSage for what I asked `llm`:

![Image 10](https://www.answer.ai/posts/shell_sage/ssage_tar.png)

ShellSage giving a more concise and actionable response about the tar command

This also touches on an important point here at [Answer.AI](https://answer.ai/). We believe the future isn’t about AI replacing humans - it’s about humans and AI working together, each bringing their unique strengths to solve problems. ShellSage embodies this philosophy by creating a shared context between you and AI right in your terminal, where many of us spend our working days.

Birth of ShellSage
------------------

What started as a simple script to help me remember bash commands evolved into something much more powerful. The initial idea was straightforward: I wanted the convenience of `llm` but with a focus on teaching rather than just telling. The key insight came when I realized that [`tmux`](https://github.com/tmux/tmux/wiki), which many developers already use for terminal management, could provide the missing context piece.

By integrating with `tmux`’s `capture-pane` functionality, ShellSage could now “see” what I was doing in my terminal. This meant it could understand not just my question, but the entire context of my work. If I was in the middle of debugging a Docker container issue, ShellSage would know that from my terminal history. If I had just encountered an error with a Git command, it could see that too.

This approach of combining AI assistance with terminal awareness turned out to be exactly what we needed. Instead of context-switching between documentation and terminals, we could stay focused on our task while learning proper system administration practices along the way.

The real test came during our intensive development period at Answer.AI. We were constantly setting up new services, configuring servers, and debugging system issues. ShellSage became our go-to tool for navigating these challenges, evolving with each new use case we encountered. What began as a personal utility for remembering commands had grown into a genuine teaching assistant for system administration.

Real-World Example: The Certificate Mystery
-------------------------------------------

Let me share a story that perfectly illustrates how humans and AI can work together to solve complex problems. During the development of SolveIt, Jeremy noticed something odd in our server logs - we were getting probed by potential attackers almost immediately after our servers went live. This was particularly puzzling because we were using random subdomains that should have been impossible to guess.

Here’s what our logs looked like:

```
INFO: "GET /.git/config HTTP/1.1" 404 Not Found
INFO: "GET /.env HTTP/1.1" 404 Not Found
INFO: "GET /wp/v2/users/ HTTP/1.1" 404 Not Found
INFO: "GET /.vscode/sftp.json HTTP/1.1" 404 Not Found
```

Jeremy had an interesting hypothesis: since only our server and Let’s Encrypt should know about these subdomains, could something about the [Let’s Encrypt](https://letsencrypt.org/) certificate process be inadvertently exposing our URLs? He turned to ShellSage to help validate this theory, asking it about Let’s Encrypt’s certificate registration process and potential information exposure.

ShellSage confirmed a crucial detail: Let’s Encrypt certificates are logged in public Certificate Transparency (CT) logs (e.g., [https://crt.sh](https://crt.sh/)), which are searchable and monitored by automated scanning tools. This validation helped Jeremy develop a solution - using wildcard certificates instead of individual subdomain certificates, which he then verified with ShellSage would prevent this kind of information leakage.

This interaction showcases what makes ShellSage special - it’s not about AI solving problems for us, but rather augmenting human intuition and problem-solving. Jeremy’s experience led to the hypothesis, while ShellSage’s knowledge helped validate the theory and confirm the solution’s viability. This kind of human-AI collaboration, where each brings their strengths to the table, is exactly what we’re building towards at Answer.AI.

We’ve reproduced a similar interaction in this [gist](https://gist.github.com/ncoop57/955b14928b5c3a594d6d07538aff687b) to show how this type of collaborative problem-solving works.

How ShellSage Works
-------------------

At its core, ShellSage is deceptively simple - in fact, the initial version clocked in at under 80 lines of code, with most of that being the system prompt that defines its personality and behavior. Even now, at ~150 lines, it’s still mostly system prompts and some autogenerated code and comments. This simplicity comes from a focused design philosophy: instead of trying to make AI do everything, we created a tool that enables effective human-AI collaboration for real-world pain points.

Let’s break down the key components that make this simple tool so effective:

### The Power of tmux

The secret sauce behind ShellSage’s context awareness is `tmux`, a terminal multiplexer that many developers already use for managing terminal sessions. Specifically, we leverage `tmux`’s `capture-pane` functionality, which can grab not just what’s visible in your terminal, but also your scrollback history. This means ShellSage can see:

*   Commands you’ve recently run
*   Their outputs and any error messages
*   The current state of your terminal session
*   Even content from your text editor if configured properly

This deep integration with `tmux` is what enables true human-AI collaboration. Instead of having to copy and paste error messages or describe what you’re trying to do, both you and ShellSage have access to the same context, leading to more natural and effective problem-solving.

### Teaching Through Context

Unlike traditional command generators or AI assistants, ShellSage is designed to teach rather than just tell. When you ask about a command, you’ll get:

*   An explanation of what the command does
*   Why certain flags or options are being used
*   Common variations for different use cases
*   Real examples based on your current context

This approach creates a feedback loop where both human and AI learn from each context. You might try a command, get an error, and then together with ShellSage, understand what went wrong and how to fix it. It’s this kind of iterative, collaborative learning that we believe is the future of human-AI interaction.

The simplicity of ShellSage’s implementation comes from focusing on a specific need - helping humans work better in the terminal - and designing for collaboration rather than automation. By sharing context between human and AI, we’ve created a tool that enhances rather than replaces human capabilities. This aligns perfectly with our philosophy at Answer.AI: the best tools aren’t the ones that do the work for you, but the ones that help you work better.

Who Is ShellSage For?
---------------------

Even the most experienced developers occasionally wrestle with command-line tools. That’s exactly why we built ShellSage - to help both beginners and experienced developers work more effectively in the terminal, whether they’re learning their first commands or managing complex system administration tasks.

### For Beginners

If you’re just starting your journey with the command line, ShellSage acts as a patient teacher. Instead of throwing man pages at you or giving you commands to blindly copy-paste, it explains concepts in context. When you ask about a command, you’ll understand not just what to type, but why you’re typing it.

### For Experienced Developers

Even if you’ve been using the terminal for years, you’ll find ShellSage valuable for:

*   Quickly recalling syntax for less-frequently used commands
*   Understanding system behaviors in complex scenarios
*   Debugging issues with immediate context awareness
*   Learning best practices for system administration tasks

![Image 11](https://www.answer.ai/posts/shell_sage/ssage_nginx.png)

ShellSage helping diagnose problems with nginx

The goal isn’t to replace your knowledge or experience - it’s to augment it. Think of ShellSage as a knowledgeable colleague who’s always ready to help, whether you’re learning your first commands or debugging a complex system issue.

Getting Started
---------------

Getting started with ShellSage is straightforward. First, install it using pip:

ShellSage works best with tmux, which provides the terminal context awareness that makes it so powerful. If you’re not already using `tmux`, you’ll want to install it first (available through most package managers like `apt`, `brew`, or `yum`).

For the best experience, we recommend configuring your terminal editor to keep content visible after exit. For vim users, add this to your `.vimrc`:

```
echo "set t_ti= t_te=" >> ~/.vimrc
```

Next, you will need an [Anthropic API key](https://docs.anthropic.com/en/api/getting-started) and set it as an environment variable:

```
export ANTHROPIC_API_KEY=sk...
```

Once installed, you can start using ShellSage immediately:

```
ssage "How do I compress this directory?" # quotes optional
```

If you’re not using tmux, you can still use ShellSage with the `--NH` flag, though you’ll miss out on some of the context-aware features:

![Image 12](https://www.answer.ai/posts/shell_sage/nh_ssage.png)

ShellSage explaining rsync syntax

One quick note for zsh users: due to how zsh handles question marks, you’ll need to quote your queries that contain them.

What’s Next
-----------

ShellSage is still in its early days, and we’re excited to see how the community uses it. While it’s already proving invaluable for our team’s daily work, we see plenty of opportunities for growth and improvement.

One area we’re particularly interested in is expanding terminal integration options. While tmux is our current focus, we know many developers use different terminal emulators like Wezterm, which offers similar capabilities for capturing terminal context. Supporting these alternatives could make ShellSage more accessible to a broader range of users.

But more importantly, ShellSage represents something bigger - it’s part of Answer.AI’s broader mission to create tools that enable effective human-AI collaboration. We’re currently teaching these principles to our first cohort of 1,000 students in our “How to Solve It with Code” course, where we’re exploring how humans and AI can work together most effectively by sharing context and building on each other’s strengths.

The future of AI isn’t about replacing human intelligence - it’s about augmenting it. At Answer.AI, we’re building tools that put this philosophy into practice, creating simple but powerful solutions that help humans and AI work together more effectively. ShellSage is just one example of this approach, and we’re excited to see how the community helps us evolve it further.

If you’re interested in contributing or have ideas for improvements, check out our [GitHub repository](https://github.com/AnswerDotAI/shell_sage). We’d love to hear your thoughts on how we can make ShellSage even more helpful for your command-line adventures, and how we can better support the future of human-AI collaboration.
