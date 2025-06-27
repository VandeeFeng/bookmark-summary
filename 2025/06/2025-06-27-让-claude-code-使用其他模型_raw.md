Title: 让 Claude Code 使用其他模型 - Nekonull's Garden

URL Source: https://nekonull.me/share/claude-code-3rd-party-model/

Published Time: Sun, 22 Jun 2025 13:24:39 GMT

Markdown Content:
##### 2025/06/22 19:43 | [hack](https://nekonull.me/tags/hack)[llm](https://nekonull.me/tags/llm)

* * *

最近在尝试各类 agent 项目，大部分都支持使用任何 OpenAI 兼容 API 格式的模型提供商，但是作为这个流派最著名的 Claude Code 却只能用自家模型。自家模型其实也不错，但是对我这种无法在生产环境使用，只是用来自己探索和 side project 的场景下太贵了。搜了下似乎没有人介绍过如何让 Claude Code 和非官方模型配合使用，于是决定记录下。

这一方法的核心是 [Claude Bridge](https://github.com/badlogic/lemmy/tree/main/apps/claude-bridge) 这个项目。实现上，和任何计算机科学问题的解决方式一样，加了一个中间层。具体而言，是 patch 了 node 的 fetch 方法，拦截所有向 Anthropic 官方的请求，转换成标准的 OpenAI 格式（其实是作者自己的一个统一 format），调用指定的提供商，在流式响应的时候再转换回 Claude 的 SSE 格式。

1.   安装依赖

```
# 官方的 claude-code
npm install -g @anthropic-ai/claude-code

# claude-bridge
npm install -g @mariozechner/claude-bridge
```

1.   准备 API Key 提供脚本

这一步参考了 Claude Code 的一个 issue [How can I use my API key without signing in?](https://github.com/anthropics/claude-code/issues/441)，以及这篇文章 [Setting up Claude-Code with API Key](https://przbadu.hashnode.dev/setting-up-claude-code-with-api-key)。

本步骤解决的问题是，Claude Code 默认情况下只能以 Claude 账号的形式登录（重定向到官方登录页），但不能在不登入账号的情况下直接使用 API Key 发起请求。然而实际上有办法绕过这一限制，只需要创建一个 `apiKeyHelper` 即可。

首先在 `~/.claude/settings.json` 中增加如下内容。（文件没有的话可以先创建）

```
{
  "apiKeyHelper": "~/.claude/anthropic_key.sh"
}
```

然后创建 `~/.claude/anthropic_key.sh`，填入如下内容：

```
echo "sk_your_anthropic_api_key"
```

（因为我们会用第三方模型提供商，所以这里可以随便填写）

最后给让这个 shell 脚本可执行。

```
chmod +x ~/.claude/anthropic_key.sh
```

1.   运行 Claude Code

用目标提供商和模型替换命令中的参数即可。第一个 openai 参数是提供商格式，也可以换成 gemini 等。详情请参考 Claude Bridge 的 readme 文件。

```
claude-bridge openai {{model_name}} --baseURL {{base_url}} --apiKey {{api_key}}
```

当然这一方法也不是万能的，有一些已知限制：

1.   token 计数不准
2.   不能输入图片
3.   网络搜索/fetch 不可用
4.   thinking/reasoning 部分可能无法被正常解析

（之后可能会写一篇文章对比不同的 agent，但是得看有没有时间了…）
