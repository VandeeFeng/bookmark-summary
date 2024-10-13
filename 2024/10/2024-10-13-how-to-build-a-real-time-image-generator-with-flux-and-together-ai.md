# How to build a real-time image generator with Flux and Together AI
- URL: https://www.together.ai/blog/how-to-build-a-real-time-image-generator-with-together-ai
- Added At: 2024-10-13 17:25:34
- [Link To Text](2024-10-13-how-to-build-a-real-time-image-generator-with-flux-and-together-ai_raw.md)

## TL;DR
本文介绍了如何使用Flux和Together AI构建实时图像生成器。文中一步步指导读者从文本输入框开始创建一个图像生成器。包括 React 前端、Node.js 后端和使用 Together AI 的 Turbo endpoint 以及 Flux.1 [schnell] 模型来生成图像。

## Summary
**如何使用Flux和Together AI构建实时图像生成器**

### **概述**
使用Together AI的Turbo endpoint和Flux.1 [schnell]模型从文本生成实时图像

### **构建前端**

#### **设置文本输入**

*   使用React state控制文本输入
*   将文本输入作为textarea呈现

示例代码：
```jsx
function Page() {
  let [prompt, setPrompt] = useState('');

  return (
    <textarea
      value={prompt}
      onChange={(e) => setPrompt(e.target.value)}
      placeholder="Describe your image..."
    />
  );
}
```

#### **使用 React Query 发送 API 请求**

*   使用`useQuery` Hook发送API请求
*   将文本输入作为参数传递给API请求

示例代码：
```jsx
function Page() {
  const [prompt, setPrompt] = useState('');

  const { data } = useQuery({
    queryKey: [prompt],
    queryFn: async () => {
      let res = await fetch('/api/generateImage', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });
      let json = await res.json();

      return json;
    },
    enabled: !!prompt.trim(),
    staleTime: Infinity,
    retry: false,
  });

  return (
    // ...
  );
}
```

### **构建后端**

#### **创建 API 路由**

*   创建一个新的API路由来处理图像生成请求
*   使用Together AI的Node SDK发送请求

示例代码：
```javascript
// app/api/generateImage/route.js
import Together from "together-ai";

let together = new Together();

export async function POST(req) {
  let json = await req.json();

  let response = await together.images.create({
    prompt: json.prompt,
    model: "black-forest-labs/FLUX.1-schnell",
    width: 1024,
    height: 768,
    steps: 3,
    response_format: "base64",
  });

  return Response.json(response.data[0]);
}
```

### **优化和扩展**

#### **防抖**

*   使用防抖功能来减少API请求的次数
*   使用`useDebounce` Hook来实现防抖

示例代码：
```jsx
function Page() {
  const [prompt, setPrompt] = useState("");
  const debouncedPrompt = useDebounce(prompt, 300); // 防抖时间为300毫秒

  const { data } = useQuery({
    queryKey: [debouncedPrompt],
    // ...
  });

  return (
    // ...
  );
}
```

#### **使用种子生成图像**

*   使用种子来生成图像
*   使用`seed`选项来指定种子值

示例代码：
```javascript
let response = await together.images.create({
  prompt: json.prompt,
  model: "black-forest-labs/FLUX.1-schnell",
  width: 1024,
  height: 768,
  steps: 3,
  response_format: "base64",
  seed: 123 // 指定种子值
});
```
