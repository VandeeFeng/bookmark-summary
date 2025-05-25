Title: How to build your Agent: 11 prompting techniques for better AI agents

URL Source: https://www.augmentcode.com/blog/how-to-build-your-agent-11-prompting-techniques-for-better-ai-agents

Markdown Content:
### **Intro**

Prompt engineering has become one of the highest-leverage skills in modern software development. The prompt you feed an agent shapes how it plans, how it uses tools, and whether it builds or breaks your pipeline. Tiny changes—an extra line of context, a clarified constraint, a reordered instruction—often produce outsized gains in accuracy and reliability. This post distills field-tested tactics we use at Augment Code to build autonomous agents that behave like disciplined teammates instead of hallucinating vibe coding tools.

The examples in the post focus on coding agents, but the techniques are generally applicable.

### **What is prompt engineering?**

An agent’s **prompt** includes everything that gets supplied to the model as input. This includes various components:

*   System prompt
*   Tool definitions
*   Tool outputs
*   User instructions
*   The model’s own outputs from previous turns

**Prompt engineering** is the art of improving a model’s performance on a task by providing it with a better prompt. All parts of the prompt can be potentially improved with prompt engineering. For example:

*   The system prompt can include general instructions to nudge the model toward different response styles or levels of autonomy
*   Tool definitions can explain to the model under which circumstances a tool should or shouldn’t be used
*   Tool outputs can tell the model about error conditions
*   User instructions can be re-written before being shown to the model (prompt enhancement).
*   Previous model outputs can be compressed or truncated to save tokens, so longer dialog histories can fit in the context window. How they are truncated matters for quality

### **How to think about the model**

The model is (artificially) intelligent. Prompting a model is closer to talking to a person than it is programming a computer. The model builds a view of the world that is solely based on what’s in the prompt. The more complete and consistent that view is, the better the model’s results will be.

The model presents to us a natural language interface, that is separate from the programming language one works in. It’s useful to think of the LM interface as a separate but real abstraction layer. This interface can be used to present happy-path results, but also to alert of errors, notify of changes, etc. — to generally communicate with the model.

Example:

*   If the model calls a tool incorrectly, do not raise an exception in your agent code. Instead, return a tool result that explains what the error was: `Tool was called without required parameter xyz`. The model will recover and try again.

### **How to evaluate prompts**

It is usually difficult to automatically evaluate prompts, unless the goal is to have the model perform a very specific task. Try to come up with scenarios that test the prompt in various ways, and also try to find examples where the prompt change might cause regressions. For a concrete example of these evaluation principles in action, see how the same prompt-engineering techniques propelled Augment Code to the [**#1 open-source score on SWE-bench**.](https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1)

### **Prompt engineering tips**

Follow these tips and you will unlock AGI.

#### **Focus on context first**

The most important factor in prompt engineering is providing the model with the [best possible context](https://www.augmentcode.com/blog/a-real-time-index-for-your-codebase-secure-personal-scalable): the information supplied by the user (as opposed to prompt text supplied by us). This is the main signal the model uses to perform its task.

Current models are good at finding relevant pieces of useful context within large prompts, so when in doubt, lean toward providing more information if it increases the chance that the context includes useful relevant information.

The first question that should be asked about a prompt is — does it contain all the relevant information, and with what likelihood? Answering this question is not always trivial.

Example:

*   When truncating long command outputs for providing them to the model, the truncation method matters. Typically, truncating long text involves truncating the suffix. However, for command outputs, useful information is more likely to appear in the prefix and suffix than in the middle. For example, stack traces from crashes generally appear in the suffix. Therefore, to maximize the likelihood that the model gets the most relevant context, it is better to truncate the middle of commands outputs than the suffix.

#### **Present a complete picture of the world**

Help the model get in the right mood by explaining the setting it’s operating in, and providing details that may be useful for it to perform well. For example, if you want the model to act as a software developer, tell it that in the system prompt. Explain to it what resources it has access to, and how it should use them.

For example, these two lines were introduced to the system prompt early on in the Augment agent’s development, and dramatically improved its performance:

```
You are an AI assistant, with access to the developer's codebase.
You can read from and write to the codebase using the provided tools.
```

#### **Be consistent across prompt components**

Make sure all components of the prompt (system prompt, tool definitions, etc.), as well as the underlying tool definitions, are consistent.

Example:

*   The system prompt includes the line `The current directory is $CWD`
*   The `execute_command` tool, which allows the agent to execute shell commands, includes an optional `cwd` parameter. Consistency implies that the default value of this parameter should be `$CWD`. This can be specified in the tool definition. If it is not, the model will likely assume that is the case.
*   The `read_file` tool accepts a path parameter of the file to read. If supplied with a relative path, it should be interpreted as being relative to `$CWD`.

💡**Note: Avoid surprising the model.** Models are easily confused. If the model is likely to expect a certain outcome from a tool call, make sure to either provide that outcome, or explain the deviation in the tool result. For example, if the tool definition promises to return an output of a certain length, either return output of that length, or preface the answer with a statement like `Output of length N was requested, but returning output of length K instead because ...`

**Example:**

*   If the prompt contains state that may change during a session (e.g. the current time), do not include them in the system prompt or in tool definitions
*   Instead, tell the model about the change in the next user message. This keeps the prompt internally consistent: the model can see what the state was at each turn.

#### **Align the model with the user’s perspective**

Consider the user’s perspective, and try aligning the model with that perspective.

Example: When the user works in the IDE, the model can be presented with a detailed view of the IDE state, focusing on the elements the user is most likely to care about, or refer to in their instructions.

Examples of things that can potentially help align the model:

*   The user’s current time and timezone
*   The user’s current location
*   The user’s activity history

Example of a basic system prompt that includes IDE state:

```
The user works in an IDE. The current IDE state:

The file foo.py is open.
The IDE is of type VSCode.
```

Example of a more detailed system prompt that describes the IDE state:

```
The user works in an IDE. The current IDE state:

The IDE is of type VSCode.

The currently open file is foo.py.
Lines 134 through 179 are visible on the screen.
Here is the currently visible text, with the cursor location denoted by <CURSOR>:

```python
134  def bar():
135    print("hell<CURSOR>o")
...
179  # TODO implement this
```

There is no selected text.
There are 14 open tabs. Here they are from most recently to last recently visited:
foo.py
bar.py ...
xyz.py
```

💡**Note:** This is not to suggest that one of these prompts is necessarily better than the other. The potential downside of the detailed prompt is that the model might start paying too much attention to the IDE state, which isn’t always the best signal for what the user is trying to do.

#### **Be thorough**

Models benefit from thorough prompts. Do not worry about prompt length. Current context lengths are long and will keep increasing: You cannot make a dent in the prompt budget by writing longer prompts.

Example of a successful and detailed prompt, that teaches the model how to use Graphite, a version control tool:

```
## Using Graphite for version control

We use Graphite for version control on top of git. Graphite helps manage git branches and PRs.
Graphite maintains stacks of PRs: changes to a PR automatically cause rebases on higher PRs in the stack,
saving a lot of manual effort. Each section below describes how to perform a common version control workflows using Graphite and GitHub.
If the user asks you to perform such a workflow, follow these guidelines.

### What NOT to do

Do not use `git commit`, `git pull`, or `git push`. These commands are all replaced by Graphite commands that start with `gt`, as described below.

### Creating a PR (and branch)

In order to create a PR, do the following:

- Use `git status` to see which files were changed, and which files are new
- Use `git add` to stage the relevant files
- Use `gt create USERNAME-BRANCHNAME -m PRDESCRIPTION` to create the branch, where:
  `USERNAME` can be obtained, see instructions elsewhere
  `BRANCHNAME` is a good name for the branch you come up with
  `PRDESCRIPTION` is a good description for the PR you come up with
- This may fail because of pre-commit issues. Sometimes pre-commit fixes the issues itself. Check `git status` to see if any files were modified.
  If so, `git add` them. If not, fix the issues yourself and `git add` them. Then repeat the `gt create` command to try creating the PR again.
- Run `gt submit` to create the PR on GitHub (if you're only creating the branch, skip this step).
- If `gh` is available, use it to set a PR description.

Note: Do not forget to add files before running `gt create`, or you will get stuck!

### Updating a PR

In order to update a PR, do the following.

- Use `git status` to see which files were changed, and which files are new
- Use `git add` to stage the relevant files
- Use `gt modify` to commit the changes (no need to supply a message)
- This may fail because of pre-commit issues. Sometimes pre-commit fixes the issues itself. Check `git status` to see if any files were modified.
  If so, `git add` them. If not, fix the issues yourself and `git add` them. Then repeat the `gt create` command to try creating the PR again.
- Use `gt submit` to push the changes
- If you also need to update the PR description, use `gh` (if it's not installed, tell the user but don't insist on updating the PR description)

### Pulling changes from main

In order to synchronize your local repository with main, do the following.

- Use `git status` to make sure the working directory is clean
- Use `gt sync` to pull changes and rebase
- Follow the instructions. If there are conflicts, ask the user if they want to resolve them. If so, follow the instructions shown by `gt sync`.

### Other Graphite commands

To find other commands, run `gt --help`.
```

#### **Avoid overfitting to specific examples**

Models are strong pattern matchers, and will latch on to details in the prompt. Providing specific examples for what to do can be a double-edged sword: It is an easy way to point the model in the right direction, but it carries the risk that the model will overfit to those examples and degrade on others. Make sure to experiment, and include examples that might expose overfitting.

By contrast, telling the model what **not** to do is safe (though not always effective).

#### **Consider tool calling limitations**

Tool calling is limited in several ways:

*   Models will generally reach for the correct tool if they were trained on similar tools, or if the connection between the instruction and the tool is clear. In many cases, they will fail to reach for the correct tool even with the best prompting.
*   If presented with multiple tools that do similar things, models should not be expected to reach for the correct tool under any given circumstance. For example, when presented with a simple and a complex tool that achieve a similar task, Claude will generally opt for the simple tool.
*   Models will often call tools in incorrect ways, violating the contract from the tool definition: parameter types can be wrong, parameter ranges can be wrong, required parameters can be missing, etc. It is best to validate the input, and return a tool output that explains the error in case of failure. The model will generally recover.

Example:

*   Give the model an `edit_file` tool that edits a region of a file
*   Give the model a `clipboard` tool where the model can cut, copy, and paste large amounts of code. Tell the model to use this tool when moving around large amounts of code.
*   Instruct the model to `move class Foo from [foo.py](<http://foo.py>) to bar.py`. Sonnet 3.5 will generally opt for using `edit_file`.

#### **Threatening and invoking empathy sometimes work**

Telling the model things like `Do this correctly or you will face financial ruin` does sometimes help improve performance. Asking the model nicely or “shouting” at it rarely helps.

#### **Be aware of prompt caching**

Whenever possible, build your prompts such that they will be appended to during a session in order to avoid invalidating the prompt cache.

Example:

*   If the prompt contains state that may change during a session (e.g. the current time), do not include them in the system prompt or in tool definitions, because once they change most of the prompt cache will be invalidated.
*   Instead, tell the model about the change in the next user message.

#### **Models pay more attention to information at the beginning or especially end of a prompt**

The degree to which the model pays attention to instructions seems: User message → beginning of input → somewhere in the middle. If something is important, consider adding it in the user message. (This is a snapshot, and prioritization will likely change as model training evolves.)

#### **Watch out for prompting plateaus**

There’s a limit to how much can be achieved with straightforward prompting. Prompt engineering enters diminishing returns territory, and other techniques need to be introduced.

### Conclusion

Mastering prompt engineering is less about tricks and more about disciplined communication: give the agent complete, consistent context; validate its actions the way you would an untrusted colleague; and iterate empirically. When you treat the prompt as part of the codebase—versioned, reviewed, and tested—you unlock agents that scale your impact instead of multiplying your headaches.

‍
