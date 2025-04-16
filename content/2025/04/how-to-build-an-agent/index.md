---
title: How To Build An Agent
date: 2025-04-16
extra:
  source: https://ampcode.com/how-to-build-an-agent
  original_title: How To Build An Agent
---
## Summary
**摘要**：
本文作者分享了如何用不到400行代码创建一个功能完善的代码编辑Agent。实现一个Agent的核心要素包括大型语言模型（LLM）、一个循环以及足够的tokens。文章通过逐步构建一个Go项目，展示了如何利用Anthropic API与Claude进行交互，实现Agent的基本功能。首先，创建了一个能与Claude对话的命令行聊天应用。然后，引入了“工具”的概念，通过定义`read_file`、`list_files`和`edit_file`这三个工具，赋予Agent读取文件、列出文件和编辑文件的能力。`read_file`允许Agent读取指定文件的内容，`list_files`让Agent能够列出指定目录下的文件和目录，而`edit_file`则允许Agent通过替换文件中的字符串来修改文件。通过结合使用这些工具，Agent能够完成诸如创建、修改JavaScript文件等复杂任务。作者强调，实现这些功能并不需要复杂的算法或深奥的理论，而是主要依赖于LLM的能力、合理的工具设计以及一定的工程实践。

**要点总结**：

1.  **Agent构建的核心要素**：构建一个代码编辑Agent的核心在于LLM、一个循环以及足够的tokens。LLM负责理解和生成代码，循环用于持续交互和执行任务，而足够的tokens则保证了信息的完整传递。
2.  **工具的概念与实现**：工具是Agent与外部世界交互的桥梁。通过定义工具，Agent可以执行读取文件（`read_file`）、列出文件（`list_files`）和编辑文件（`edit_file`）等操作。每个工具都需要一个名称、描述、输入模式和执行函数。
3.  **`read_file`工具**：该工具允许Agent读取指定路径的文件内容。通过向LLM提供文件内容，Agent可以分析文件内容，从而更好地理解任务需求。
4.  **`list_files`工具**：该工具允许Agent列出指定路径下的文件和目录。通过获取文件列表，Agent可以了解项目的整体结构，从而更好地定位和修改文件。
5.  **`edit_file`工具**：该工具允许Agent通过替换字符串的方式编辑文件。是Agent执行代码修改的核心手段。虽然简单，但结合LLM的理解能力，可以实现复杂的代码编辑任务。通过`edit_file`工具，Agent可以创建新文件、修改现有文件，甚至可以完成代码的rot13解码等复杂任务。
## Full Content
Title: How To Build An Agent | Amp

URL Source: https://ampcode.com/how-to-build-an-agent

Markdown Content:
_or: The Emperor Has No Clothes_

**Thorsten Ball, April 15, 2025**

It’s not that hard to build a fully functioning, code-editing agent.

It seems like it would be. When you look at an agent editing files, running commands, wriggling itself out of errors, retrying different strategies - it seems like there has to be a secret behind it.

There isn’t. It’s an LLM, a loop, and enough tokens. It’s what we’ve been saying on the [podcast](https://ampcode.com/podcast) from the start. The rest, the stuff that makes Amp so addictive and impressive? Elbow grease.

But building a small and yet highly impressive agent doesn’t even require that. You can do it in less than 400 lines of code, most of which is boilerplate.

I’m going to show you how, right now. We’re going to write some code together and go from zero lines of code to “oh wow, this is… a game changer.”

I _urge_ you to follow along. No, really. You might think you can just read this and that you don’t have to type out the code, but it’s less than 400 lines of code. I need you to _feel_ how little code it is and I want you to see this with your own eyes in your own terminal in your own folders.

Here’s what we need:

*   [Go](https://go.dev/)
*   [Anthropic API key](https://console.anthropic.com/settings/keys) that you set as an environment variable, `ANTHROPIC_API_KEY`

Pencils out!
------------

Let’s dive right in and get ourselves a new Go project set up in four easy commands:

```
mkdir code-editing-agent
cd code-editing-agent
go mod init agent
touch main.go
```

Now, let’s open `main.go` and, as a first step, put a skeleton of things we need in it:

```
package main

import (
	"bufio"
	"context"
	"fmt"
	"os"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	scanner := bufio.NewScanner(os.Stdin)
	getUserMessage := func() (string, bool) {
		if !scanner.Scan() {
			return "", false
		}
		return scanner.Text(), true
	}

	agent := NewAgent(&client, getUserMessage)
	err := agent.Run(context.TODO())
	if err != nil {
		fmt.Printf("Error: %s\n", err.Error())
	}
}

func NewAgent(client *anthropic.Client, getUserMessage func() (string, bool)) *Agent {
	return &Agent{
		client:         client,
		getUserMessage: getUserMessage,
	}
}

type Agent struct {
	client         *anthropic.Client
	getUserMessage func() (string, bool)
}
```

Yes, this doesn’t compile yet. But what we have here is an `Agent` that has access to an `anthropic.Client` (which, by default, looks for `ANTHROPIC_API_KEY`) and that can get a user message by reading from stdin on the terminal.

Now let’s add the missing `Run()` method:

```
// main.go

func (a *Agent) Run(ctx context.Context) error {
	conversation := []anthropic.MessageParam{}

	fmt.Println("Chat with Claude (use 'ctrl-c' to quit)")

	for {
		fmt.Print("\u001b[94mYou\u001b[0m: ")
		userInput, ok := a.getUserMessage()
		if !ok {
			break
		}

		userMessage := anthropic.NewUserMessage(anthropic.NewTextBlock(userInput))
		conversation = append(conversation, userMessage)

		message, err := a.runInference(ctx, conversation)
		if err != nil {
			return err
		}
		conversation = append(conversation, message.ToParam())

		for _, content := range message.Content {
			switch content.Type {
			case "text":
				fmt.Printf("\u001b[93mClaude\u001b[0m: %s\n", content.Text)
			}
		}
	}

	return nil
}

func (a *Agent) runInference(ctx context.Context, conversation []anthropic.MessageParam) (*anthropic.Message, error) {
	message, err := a.client.Messages.New(ctx, anthropic.MessageNewParams{
		Model:     anthropic.ModelClaude3_7SonnetLatest,
		MaxTokens: int64(1024),
		Messages:  conversation,
	})
	return message, err
}
```

It’s not a lot, is it? 90 lines and the most important thing about is this loop in `Run()` that lets us talk to Claude. But that’s already the heartbeat of this program.

And for a heartbeat, it’s pretty straightforward: we first print a prompt, ask the user to type something, add it to the conversation, send it to Claude, add Claude’s response to the conversation, print the response, and around we go.

This is every AI chat application you’ve ever used, except it’s in the terminal.

Let’s run it:

```
export ANTHROPIC_API_KEY="this is the last time i will tell you to set this"

# Download the dependencies
go mod tidy
# Run it
go run main.go
```

Then you can just talk to Claude, like this:

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: Hey! I'm Thorsten! How are you?

Claude: Hi Thorsten! I'm doing well, thanks for asking. It's nice to meet you. How are you doing today? Is there something I can help you with?

You: Can you come up with any horse-related nicknames that make fun of my first name?

Claude: I can try to come up with some playful horse-related nicknames based on "Thorsten": \* Thorough-bred Thorsten \* Trotsten \* Thorsten the Stallion \* Neighsten \* Horseten \* Thorsten the Galloper \* Saddle-sten \* Thorsten of the Mane \* Canter-sten \* Thorsteed These are meant to be lighthearted - I hope they give you a chuckle!

You:

Notice how we kept the same conversation going over multiple turns. It remembers my name from the first message. The `conversation` grows longer with every turn and we send the whole conversation every time. The server — Anthropic’s server — is stateless. It only sees what’s in the `conversation` slice. It’s up to us to maintain that.

Okay, let’s move on, because the nicknames suck and this is not an agent yet. What’s an agent? Here’s [my definition](https://youtu.be/J1-W9O3n7j8?t=72): an LLM with _access to tools_, giving it the ability to modify something outside the context window.

A First Tool
------------

An LLM with _access to tools_? What’s a tool? The basic idea is this: you send a prompt to the model that says it should reply in a certain way if it wants to use “a tool”. Then you, as the receiver of that message, “use the tool” by executing it and replying with the result. That’s it. Everything else we’ll see is just abstraction on top of it.

Imagine you’re talking to a friend and you tell them: “in the following conversation, wink if you want me to raise my arm”. Weird thing to say, but an easy concept to grasp.

We can already try it without changing any of our code.

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: You are a weather expert. When I ask you about the weather in a given location, I want you to reply with \`get\_weather(<location\_name\>)\`. I will then tell you what the weather in that location is. Understood?

Claude: I understand your instructions. When you ask me about the weather in a specific location, I will reply with \`get\_weather(<location\_name\>)\`. Then you'll provide me with the weather information for that location, and I can discuss it further with you. I'm ready whenever you'd like to ask about the weather somewhere.

You: Hey, what's the weather in Munich?

Claude: get\_weather(Munich)

We told Claude to wink with `get_weather` when it wants to know about the weather. The next step is to raise our arm and reply with “result of the tool”:

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: hot and humid, 28 degrees celcius

Claude: Thank you for providing that information. The current weather in Munich is hot and humid at 28 degrees Celsius (about 82 degrees Fahrenheit). These are fairly warm conditions for Munich, especially with the added humidity which can make it feel even warmer than the temperature indicates. If you're in Munich or planning to visit, it would be good to stay hydrated, wear light clothing, and perhaps plan indoor activities during the hottest parts of the day. The combination of heat and humidity can be quite uncomfortable, particularly if you're not accustomed to such weather. Would you like to know about the weather in any other location?

That worked very well, on first try, didn’t it?

These models are trained and fine-tuned to use “tools” and they’re very eager to do so. By now, 2025, they kinda “know” that they don’t know everything and can use tools to get more information. (Of course that’s not precisely what’s going on, but it’s good enough an explanation for now.)

To summarize, all there is to tools and tool use are two things:

1.  You tell the model what tools are available
2.  When the model wants to execute the tool, it tells you, you execute the tool and send the response up

To make (1) easier, the big model providers have built-in APIs to send tool definitions along.

Okay, now let’s build our first tool: `read_file`

The `read_file` tool
--------------------

In order to define the `read_file` tool, we’re going to use the types that the Anthropic SDK suggests, but keep in mind: under the hood, this will all end up as strings that are sent to the model. It’s all “wink if you want me to use `read_file`“.

Each tool we’re going to add will require the following:

*   A name
*   A description, that tells the model what the tool does, when to use it, when to not use it, what it returns and so on.
*   An input schema, that describes as a JSON schema, what inputs this tool expects and in which form
*   A function that actually executes the tool with the input the model sends to us and returns the result

So let’s add that to our code:

```
// main.go

type ToolDefinition struct {
	Name        string                         `json:"name"`
	Description string                         `json:"description"`
	InputSchema anthropic.ToolInputSchemaParam `json:"input_schema"`
	Function    func(input json.RawMessage) (string, error)
}
```

Now we give our `Agent` tool definitions:

```
// main.go

// `tools` is added here:
type Agent struct {
	client         *anthropic.Client
	getUserMessage func() (string, bool)
	tools          []ToolDefinition
}

// And here:
func NewAgent(
	client *anthropic.Client,
	getUserMessage func() (string, bool),
	tools []ToolDefinition,
) *Agent {
	return &Agent{
		client:         client,
		getUserMessage: getUserMessage,
		tools:          tools,
	}
}

// And here:
func main() {
    // [... previous code ...]
	tools := []ToolDefinition{}
	agent := NewAgent(&client, getUserMessage, tools)

    // [... previous code ...]
}
```

And send them along to the model in `runInference`:

```
// main.go

func (a *Agent) runInference(ctx context.Context, conversation []anthropic.MessageParam) (*anthropic.Message, error) {
	anthropicTools := []anthropic.ToolUnionParam{}
	for _, tool := range a.tools {
		anthropicTools = append(anthropicTools, anthropic.ToolUnionParam{
			OfTool: &anthropic.ToolParam{
				Name:        tool.Name,
				Description: anthropic.String(tool.Description),
				InputSchema: tool.InputSchema,
			},
		})
	}

	message, err := a.client.Messages.New(ctx, anthropic.MessageNewParams{
		Model:     anthropic.ModelClaude3_7SonnetLatest,
		MaxTokens: int64(1024),
		Messages:  conversation,
		Tools:     anthropicTools,
	})
	return message, err
}
```

There’s a bunch of type shenanigans going on and I’m not too good in Go-with-generics yet so I’m not going to try to explain `anthropic.String` and `ToolUnionParam` to you. But, really, I swear, it’s very simple:

We send along our tool definitions, on the server Anthropic then wraps these definitions in [this system prompt](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview#tool-use-system-prompt) (which isn’t much), which it adds to our `conversation`, and the model then replies in a specific way if it wants to use that tool.

Alright, so tool definitions are being sent along, but we haven’t defined a tool yet. Let’s do that and define `read_file`:

```
// main.go

var ReadFileDefinition = ToolDefinition{
	Name:        "read_file",
	Description: "Read the contents of a given relative file path. Use this when you want to see what's inside a file. Do not use this with directory names.",
	InputSchema: ReadFileInputSchema,
	Function:    ReadFile,
}

type ReadFileInput struct {
	Path string `json:"path" jsonschema_description:"The relative path of a file in the working directory."`
}

var ReadFileInputSchema = GenerateSchema[ReadFileInput]()

func ReadFile(input json.RawMessage) (string, error) {
	readFileInput := ReadFileInput{}
	err := json.Unmarshal(input, &readFileInput)
	if err != nil {
		panic(err)
	}

	content, err := os.ReadFile(readFileInput.Path)
	if err != nil {
		return "", err
	}
	return string(content), nil
}

func GenerateSchema[T any]() anthropic.ToolInputSchemaParam {
	reflector := jsonschema.Reflector{
		AllowAdditionalProperties: false,
		DoNotReference:            true,
	}
	var v T

	schema := reflector.Reflect(v)

	return anthropic.ToolInputSchemaParam{
		Properties: schema.Properties,
	}
}
```

That’s not much, is it? It’s a single function, `ReadFile`, and two descriptions the model will see: our `Description` that describes the tool itself (`"Read the contents of a given relative file path. ..."`) and a description of the single input parameter this tool has (`"The relative path of a ..."`).

The `ReadFileInputSchema` and `GenerateSchema` stuff? We need that so that we can generate a JSON schema for our tool definition which we send to the model. To do that, we use the `jsonschema` package, which we need to import and download:

```
// main.go

package main

import (
	"bufio"
	"context"
    // Add this:
	"encoding/json"
	"fmt"
	"os"

	"github.com/anthropics/anthropic-sdk-go"
    // Add this:
	"github.com/invopop/jsonschema"
)
```

Then run the following:

`go mod tidy`

Then, in the `main` function, we need to make sure that we use the definition:

```
func main() {
    // [... previous code ...]
	tools := []ToolDefinition{ReadFileDefinition}
    // [... previous code ...]
}
```

Time to try it!

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: what's in main.go?

Claude: I'll help you check what's in the main.go file. Let me read it for you.

You:

Wait, what? Ho, ho, ho, it wants to use the tool! Obviously the output will be slightly different for you, but it certainly sounds like Claude knows that it can read files, right?

The problem is that we don’t listen! When Claude winks, we ignore it. We need to fix that.

Here, let me show you how to do that in a single, quick, surprisingly-agile-for-my-age move by replacing our `Agent`’s `Run` method with this:

```
// main.go

func (a *Agent) Run(ctx context.Context) error {
	conversation := []anthropic.MessageParam{}

	fmt.Println("Chat with Claude (use 'ctrl-c' to quit)")

	readUserInput := true
	for {
		if readUserInput {
			fmt.Print("\u001b[94mYou\u001b[0m: ")
			userInput, ok := a.getUserMessage()
			if !ok {
				break
			}

			userMessage := anthropic.NewUserMessage(anthropic.NewTextBlock(userInput))
			conversation = append(conversation, userMessage)
		}

		message, err := a.runInference(ctx, conversation)
		if err != nil {
			return err
		}
		conversation = append(conversation, message.ToParam())

		toolResults := []anthropic.ContentBlockParamUnion{}
		for _, content := range message.Content {
			switch content.Type {
			case "text":
				fmt.Printf("\u001b[93mClaude\u001b[0m: %s\n", content.Text)
			case "tool_use":
				result := a.executeTool(content.ID, content.Name, content.Input)
				toolResults = append(toolResults, result)
			}
		}
		if len(toolResults) == 0 {
			readUserInput = true
			continue
		}
		readUserInput = false
		conversation = append(conversation, anthropic.NewUserMessage(toolResults...))
	}

	return nil
}

func (a *Agent) executeTool(id, name string, input json.RawMessage) anthropic.ContentBlockParamUnion {
	var toolDef ToolDefinition
	var found bool
	for _, tool := range a.tools {
		if tool.Name == name {
			toolDef = tool
			found = true
			break
		}
	}
	if !found {
		return anthropic.NewToolResultBlock(id, "tool not found", true)
	}

	fmt.Printf("\u001b[92mtool\u001b[0m: %s(%s)\n", name, input)
	response, err := toolDef.Function(input)
	if err != nil {
		return anthropic.NewToolResultBlock(id, err.Error(), true)
	}
	return anthropic.NewToolResultBlock(id, response, false)
}
```

Squint and you’ll see that it’s 90% boilerplate and 10% that matter: when we get a `message` back from Claude, we check wether Claude asked us to execute a tool by looking for `content.Type == "tool_use"`, if so we hand over to `executeTool`, lookup the tool by name in our local registry, unmarshal the input, execute it, return the result. If it’s an error, we flip a boolean. That’s it.

(Yes, there is a loop in a loop, but it doesn’t matter.)

We execute the tool, send the result back up to Claude, and ask again for Claude’s response. Truly: that’s _it_. Let me show you.

Mise-en-place, run this:

`echo 'what animal is the most disagreeable because it always says neigh?' >> secret-file.txt`

That creates a `secret-file.txt` in our directory, containing a mysterious riddle.

In that very same directory, let’s run our new tool-using agent, and ask it to look at the file:

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: Claude, buddy, help me solve the riddle in the secret-file.txt file

Claude: I'll help you solve the riddle in the secret-file.txt file. Let me first read the contents of this file to see what the riddle is.

tool: read\_file({"path":"secret-file.txt"})

Claude: Great! I've found the riddle. The answer to the riddle is: \*\*A horse\*\* The riddle is playing on wordplay where "neigh" (the sound a horse makes) sounds like "nay" (a way to say "no" or disagree with something). So horses are described as disagreeable because they always say "neigh/nay" - implying they're always disagreeing.

You:

Let’s take a deep breath and say it together. Ready? Here we go: _holy shit_. You just give it a tool and it… _uses it when it thinks it’ll help solve the task_. Remember: we didn’t say _anything_ about “if a user asks you about a file, read the file”. We also didn’t say “if something looks like a filename, figure out how to read it”. No, none of that. We say “help me solve the thing in this file” and Claude realizes that it can read the file to answer that and off it goes.

Of course, we _can_ be specific and really nudge it towards a tool, but it basically does it all on its own:

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: What's going on in main.go? Be brief!

Claude: I'll check the main.go file to see what's going on.

tool: read\_file({"path":"main.go"})

Claude: Based on my review, main.go implements a Claude AI assistant agent that can use tools. Here's a brief summary: - It creates a command-line chat interface with Claude using the Anthropic Go SDK - Implements a tool system with a single "read\_file" tool for reading file contents - Manages the conversation flow with Claude, handling both regular text responses and tool use requests - When Claude requests to use a tool, the agent executes it and returns the results - The program loops continuously to maintain a conversation until the user exits The code essentially builds a simple CLI-based chatbot that can interact with the file system when requested by Claude.

You:

Spot on. Okay, now that we know how to make Claude use tools, let’s add a few more.

The `list_files` tool
---------------------

If you’re anything like me, the first thing you do when you log into a new computer is to get your bearings by running `ls` — list files.

Let’s give Claude the same ability, a tool to list files. And here’s the complete implementation of a `list_files` tool:

```
// main.go

var ListFilesDefinition = ToolDefinition{
	Name:        "list_files",
	Description: "List files and directories at a given path. If no path is provided, lists files in the current directory.",
	InputSchema: ListFilesInputSchema,
	Function:    ListFiles,
}

type ListFilesInput struct {
	Path string `json:"path,omitempty" jsonschema_description:"Optional relative path to list files from. Defaults to current directory if not provided."`
}

var ListFilesInputSchema = GenerateSchema[ListFilesInput]()

func ListFiles(input json.RawMessage) (string, error) {
	listFilesInput := ListFilesInput{}
	err := json.Unmarshal(input, &listFilesInput)
	if err != nil {
		panic(err)
	}

	dir := "."
	if listFilesInput.Path != "" {
		dir = listFilesInput.Path
	}

	var files []string
	err = filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		relPath, err := filepath.Rel(dir, path)
		if err != nil {
			return err
		}

		if relPath != "." {
			if info.IsDir() {
				files = append(files, relPath+"/")
			} else {
				files = append(files, relPath)
			}
		}
		return nil
	})

	if err != nil {
		return "", err
	}

	result, err := json.Marshal(files)
	if err != nil {
		return "", err
	}

	return string(result), nil
}
```

Nothing fancy here: `list_files` returns the list of files and directories in the current folder. There’s a thousand optimizations we could (and probably should) make if this were a serious effort, but since I just want to show you what’s in the wizard’s hat, this is fine.

One thing to note: we return a list of strings and we denote directories with a trailing slash. That’s not required, it’s just something I just decided to do. There’s no fixed format. Anything goes as long as Claude can make sense of it and whether it can you need to figure out by experimentation. You could also prepend each directory with `"directory: "` or return a Markdown document with two headers: `"directories"` and `"files"`. There’s a ton of options and which one you chose depends on what Claude can make the most sense of, how many tokens it requires, how fast it is to generate and read, and so on.

Here, we just want to create a small `list_files` tool and the easiest option wins.

Of course we need to tell Claude about `list_files` too:

```
// main.go

func main() {
	// [... previous code ...]

	tools := []ToolDefinition{ReadFileDefinition, ListFilesDefinition}

	// [... previous code ...]
}
```

And that’s it. Let’s ask Claude what it can see in this directory.

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: what do you see in this directory?

Claude: I'll help you see what's in the current directory. Let me list the files and directories for you.

tool: list\_files({})

Claude: I can see several files and directories in the current directory: 1. Git-related files and directories: - \`.git/\` directory with various Git configuration and tracking files - \`.gitignore\` file 2. Go project files: - \`main.go\` - the main Go source code file - \`go.mod\` - Go module definition file - \`go.sum\` - Go module checksum file 3. Documentation: - \`blogpost.md\` - a markdown file, likely containing blog content 4. Environment configuration: - \`.envrc\` - likely an environment configuration file Would you like me to examine the contents of any specific file from this list?

You:

Works! It can read the directory.

But here’s the thing: Claude knows how to combine these tools. We just need to prompt it in a way that provokes it:

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: Tell me about all the Go files in here. Be brief!

Claude: I'll examine the Go files in the current directory for you. Let me check what files are available first.

tool: list\_files({})

Claude: I found a Go file in the current directory. Let me examine it:

tool: read\_file({"path":"main.go"})

tool: read\_file({"path":"go.mod"})

Claude: Here's a brief overview of the Go files in this project: \*\*main.go\*\*: - Implements a Claude AI agent that can interact with the local filesystem - Uses the Anthropic SDK for Go to communicate with Claude AI models - Provides two tools: \`read\_file\` and \`list\_files\` that allow Claude to read file contents and list directory contents - Manages a conversation flow between the user and Claude, handling tool execution when Claude needs to access files \*\*go.mod\*\*: - Defines the module dependencies - Main dependencies are the Anthropic SDK for Go and a JSON schema library - Uses Go 1.24.1 This appears to be a simple terminal-based application that allows users to chat with Claude while giving the AI access to read local files and list directories.

You:

First it used the `list_files` and then it called `read_file` twice with the Go-related files that I asked it about.

Just… just like we would, right? I mean, here, what would you do if I ask you what version of Go we use in this project? Here’s what Claude does for me:

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: What go version are we using in this project?

Claude: I'll help you find the Go version being used in this project. Let me check the files to locate where the Go version might be specified.

tool: list\_files({})

Claude: I can see there's a Go project here with several important files like \`go.mod\`, \`go.sum\`, and \`main.go\`. Let me check the \`go.mod\` file first, as it typically contains the Go version information.

tool: read\_file({"path":"go.mod"})

Claude: According to the \`go.mod\` file, this project is using Go version 1.24.1.

Claude looks at the directory, looks at `go.mod`, and has the answer.

We’re at around 190 lines of code now. Let that sink in. Once you have, let’s add another tool.

Let it `edit_file`
------------------

The last tool we’re going to add is `edit_file` — a tool that lets Claude edit files.

“Holy shit”, you’re thinking now, “this is where the rubber hits the road, this is where he pulls the rabbit out of the hat.” Well, let’s see, shall we?

First, let’s add a definition for our new `edit_file` tool:

```
// main.go

var EditFileDefinition = ToolDefinition{
	Name: "edit_file",
	Description: `Make edits to a text file.

Replaces 'old_str' with 'new_str' in the given file. 'old_str' and 'new_str' MUST be different from each other.

If the file specified with path doesn't exist, it will be created.
`,
	InputSchema: EditFileInputSchema,
	Function:    EditFile,
}

type EditFileInput struct {
	Path   string `json:"path" jsonschema_description:"The path to the file"`
	OldStr string `json:"old_str" jsonschema_description:"Text to search for - must match exactly and must only have one match exactly"`
	NewStr string `json:"new_str" jsonschema_description:"Text to replace old_str with"`
}

var EditFileInputSchema = GenerateSchema[EditFileInput]()
```

That’s right, I again know what you’re thinking: “string replacement to edit files?” That’s right. Claude 3.7 loves replacing strings, so we’re going to implement `edit_file` by telling Claude it can edit files by replacing existing text with new text.

Now here’s the implementation of the `EditFile` function in Go:

```
func EditFile(input json.RawMessage) (string, error) {
	editFileInput := EditFileInput{}
	err := json.Unmarshal(input, &editFileInput)
	if err != nil {
		return "", err
	}

	if editFileInput.Path == "" || editFileInput.OldStr == editFileInput.NewStr {
		return "", fmt.Errorf("invalid input parameters")
	}

	content, err := os.ReadFile(editFileInput.Path)
	if err != nil {
		if os.IsNotExist(err) && editFileInput.OldStr == "" {
			return createNewFile(editFileInput.Path, editFileInput.NewStr)
		}
		return "", err
	}

	oldContent := string(content)
	newContent := strings.Replace(oldContent, editFileInput.OldStr, editFileInput.NewStr, -1)

	if oldContent == newContent && editFileInput.OldStr != "" {
		return "", fmt.Errorf("old_str not found in file")
	}

	err = os.WriteFile(editFileInput.Path, []byte(newContent), 0644)
	if err != nil {
		return "", err
	}

	return "OK", nil
}
```

It checks the input parameters, it reads the file (or creates it if it exists), and replaces the `OldStr` with `NewStr`. Then it writes the content back to disk and returns `"OK"`.

What’s missing still is `createNewFile`, which is just a tiny helper function that would be 70% shorter if this wasn’t Go:

```
func createNewFile(filePath, content string) (string, error) {
	dir := path.Dir(filePath)
	if dir != "." {
		err := os.MkdirAll(dir, 0755)
		if err != nil {
			return "", fmt.Errorf("failed to create directory: %w", err)
		}
	}

	err := os.WriteFile(filePath, []byte(content), 0644)
	if err != nil {
		return "", fmt.Errorf("failed to create file: %w", err)
	}

	return fmt.Sprintf("Successfully created file %s", filePath), nil
}
```

And… we’re ready, but are _you_? Are you ready to let it rip?

Thought so, let’s do this. Let’s tell Claude to create a new FizzBuzz function in JavaScript.

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: hey claude, create fizzbuzz.js that I can run with Nodejs and that has fizzbuzz in it and executes it

Claude: I'll create a fizzbuzz.js file that you can run with Node.js. First, let me check if the file already exists:

tool: list\_files({})

Claude: I don't see a fizzbuzz.js file, so I'll create one with a classic FizzBuzz implementation. This program will print numbers from 1 to 100, but for multiples of 3 it will print "Fizz", for multiples of 5 it will print "Buzz", and for numbers that are multiples of both 3 and 5 it will print "FizzBuzz".

tool: edit\_file({"path":"fizzbuzz.js","old\_str":"","new\_str":"/\*\*\\n \* FizzBuzz implementation in JavaScript\\n \* Prints numbers from 1 to 100, but:\\n \* - For multiples of 3, print \\"Fizz\\" instead of the number\\n \* - For multiples of 5, print \\"Buzz\\" instead of the number\\n \* - For multiples of both 3 and 5, print \\"FizzBuzz\\"\\n \*/\\n\\nfunction fizzBuzz(n) {\\n for (let i = 1; i <\= n; i++) {\\n let output = '';\\n \\n if (i % 3 === 0) output += 'Fizz';\\n if (i % 5 === 0) output += 'Buzz';\\n \\n console.log(output || i);\\n }\\n}\\n\\n// Execute FizzBuzz for numbers 1 to 100\\nconsole.log('Running FizzBuzz:');\\nfizzBuzz(100);"}

Claude: I've created a fizzbuzz.js file that you can run with Node.js. The program: 1. Defines a function called \`fizzBuzz\` that takes a parameter \`n\` for the upper limit 2. Loops from 1 to n (set to 100 in the execution) 3. For each number: - If it's divisible by 3, it adds "Fizz" to the output - If it's divisible by 5, it adds "Buzz" to the output - If it's divisible by both, it adds both resulting in "FizzBuzz" - If it's not divisible by either 3 or 5, it outputs the number itself 4. The script automatically executes the function for numbers 1 to 100 You can run this script using Node.js with the following command in your terminal: node fizzbuzz.js This will output the FizzBuzz sequence from 1 to 100 to your console.

Right?! It’s impressive, isn’t it? And that’s the _most basic implemenation_ of `edit_file` — of an agent in general — you can probably come up with.

But, did it work? Yes, it did:

tool: $ node fizzbuzz.js Running FizzBuzz: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 \[...\]

Amazing. But hey, let’s have it actually _edit_ a file and not just create one.

Here’s what Claude does when I ask it to “Please edit the `fizzbuzz.js` so that it only prints until 15”:

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: Please edit fizzbuzz.js so that it only prints until 15

Claude: I'll edit the fizzbuzz.js file to print only until 15 instead of its current limit. First, let me check the current content of the file to understand what changes are needed.

tool: read\_file({"path":"fizzbuzz.js"})

Claude: I can see that the file currently runs FizzBuzz up to 100. I'll modify it to only run up to 15 instead by changing the parameter in the fizzBuzz function call.

tool: edit\_file({"path":"fizzbuzz.js","old\_str":"// Execute FizzBuzz for numbers 1 to 100\\nconsole.log('Running FizzBuzz:');\\nfizzBuzz(100);","new\_str":"// Execute FizzBuzz for numbers 1 to 15\\nconsole.log('Running FizzBuzz:');\\nfizzBuzz(15);"})

Claude: I also need to update the comment at the top of the file to reflect this change:

tool: edit\_file({"path":"fizzbuzz.js","old\_str":"/\*\*\\n \* FizzBuzz implementation in JavaScript\\n \* Prints numbers from 1 to 100, but:","new\_str":"/\*\*\\n \* FizzBuzz implementation in JavaScript\\n \* Prints numbers from 1 to 15, but:"})

Claude: The changes have been successfully made to the fizzbuzz.js file. The program will now: 1. Only print FizzBuzz from 1 to 15 (instead of 1 to 100) 2. The documentation has been updated to reflect this change The function itself remains the same, as it takes a parameter to determine the upper limit, and we've simply changed that parameter from 100 to 15.

It reads the file, it edits the file to change the how long it runs, _and_ then it also edits the file to update the comment at the top.

And it still works:

```
$ node fizzbuzz.js
Running FizzBuzz:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

Okay, let’s do one more and ask it to do the following:

> Create a congrats.js script that rot13-decodes the following string ‘Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!’ and prints it

Maybe a tall order. Let’s see:

$ go run main.go

Chat with Claude (use 'ctrl-c' to quit)

You: Create a congrats.js script that rot13-decodes the following string 'Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!' and prints it

Claude: I'll create a congrats.js script that decodes the ROT13-encoded string and prints it. ROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet. Let me create this file for you:

tool: edit\_file({"path":"congrats.js","old\_str":"","new\_str":"/\*\*\\n \* A script to decode a ROT13-encoded string and print the result\\n \*/\\n\\nfunction rot13Decode(encodedStr) {\\n return encodedStr.replace(/\[a-zA-Z\]/g, function(char) {\\n // Get the character code\\n const charCode = char.charCodeAt(0);\\n \\n // Handle uppercase letters\\n if (charCode \>\= 65 && charCode <\= 90) {\\n return String.fromCharCode(((charCode - 65 + 13) % 26) + 65);\\n }\\n \\n // Handle lowercase letters\\n if (charCode \>\= 97 && charCode <\= 122) {\\n return String.fromCharCode(((charCode - 97 + 13) % 26) + 97);\\n }\\n \\n // Return non-alphabetic characters as is\\n return char;\\n });\\n}\\n\\nconst encodedMessage = 'Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!';\\nconst decodedMessage = rot13Decode(encodedMessage);\\n\\nconsole.log(decodedMessage);"})

Claude: I've created a JavaScript file called congrats.js that: 1. Defines a \`rot13Decode\` function that takes an encoded string and applies the ROT13 cipher to decode it 2. Takes the provided string 'Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!' 3. Decodes it using the function 4. Prints the decoded message to the console You can run this script using Node.js by typing \`node congrats.js\` in your terminal. The script will decode and display the hidden congratulatory message!

Does it work? Let’s try it:

```
$ node congrats.js
Congratulations on building a code-editing agent!
```

It does!

Isn’t this amazing?
-------------------

If you’re anything like all the engineers I’ve talked to in the past few months, chances are that, while reading this, you have been waiting for the rabbit to be pulled out of the hat, for me to say “well, in reality it’s much, much harder than this.” But it’s not.

This is essentially all there is to the inner loop of a code-editing agent. Sure, integrating it into your editor, tweaking the system prompt, giving it the right feedback at the right time, a nice UI around it, better tooling around the tools, support for multiple agents, and so on — we’ve built all of that in Amp, but it didn’t require moments of genius. All that was required was practical engineering and elbow grease.

These models are incredibly powerful now. 300 lines of code and three tools and now you’re to be able to talk to an alien intelligence that edits your code. If you think “well, but we didn’t really…” — go and try it! Go and see how far you can get with this. I bet it’s a lot farther than you think.

_That_’s why we think everything’s changing.

