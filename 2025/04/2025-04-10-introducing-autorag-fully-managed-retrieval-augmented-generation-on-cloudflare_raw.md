Title: Introducing AutoRAG: fully managed Retrieval-Augmented Generation on Cloudflare

URL Source: https://blog.cloudflare.com/introducing-autorag-on-cloudflare/

Published Time: 2025-04-07T14:00+00:00

Markdown Content:
2025-04-07

8 min read

![Image 1](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/2SZ1fpLEMXLfjidRspvQ3p/35aaef41cf7231cf349019d54143c00e/Feature_Image.png)

Today we’re excited to announce **AutoRAG** in open beta, a fully managed Retrieval-Augmented Generation (RAG) pipeline powered by Cloudflare, designed to simplify how developers integrate context-aware AI into their applications. RAG is a method that improves the accuracy of AI responses by retrieving information from your own data, and providing it to the large language model (LLM) to generate more grounded responses.

Building a RAG pipeline is a patchwork of moving parts. You have to stitch together multiple tools and services — your data storage, a vector database, an embedding model, LLMs, and custom indexing, retrieval, and generation logic — all just to get started. Maintaining it is even harder. As your data changes, you have to manually reindex and regenerate embeddings to keep the system relevant and performant. What should be a simple “ask a question, get a smart answer” experience becomes a brittle pipeline of glue code, fragile integrations, and constant upkeep.

AutoRAG removes that complexity. With just a few clicks, it delivers a fully-managed RAG pipeline end-to-end: from ingesting your data and automatically chunking and embedding it, to storing vectors in Cloudflare’s [Vectorize](https://developers.cloudflare.com/vectorize/) database, performing semantic retrieval, and generating high-quality responses using [Workers AI](https://developers.cloudflare.com/workers-ai/). AutoRAG continuously monitors your data sources and indexes in the background so your AI stays fresh without manual effort. It abstracts away the mess, letting you focus on building smarter, faster applications on Cloudflare’s developer platform. Get started today in the [Cloudflare Dashboard](https://dash.cloudflare.com/?to=/:account/ai/autorag)!

### Why use RAG in the first place?

LLMs like Llama 3.3 from Meta are powerful, but they only know what they’ve been trained on. They often struggle to produce accurate answers when asked about new, proprietary, or domain-specific information. System prompts providing relevant information can help, but they bloat input size and are limited by context windows. Fine-tuning a model is expensive and requires ongoing retraining to keep up to date.

RAG solves this by retrieving relevant information from your data source at query time, combining it with the user’s input query, and feeding both into the LLM to generate responses grounded with your data. This makes RAG a great fit for AI-driven support bots, internal knowledge assistants, semantic search across documentation, and other use cases where the source of truth is always evolving.

![Image 2](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/5zrM30iI2E1ZlmTQvAsx0D/fcef1f00b048a147fc3bc459895cc19c/1.png)

### What’s under the hood of AutoRAG?

AutoRAG sets up a RAG pipeline for you, using the building blocks of Cloudflare’s developer platform. Instead of you having to write code to create a RAG system using [Workers AI](https://developers.cloudflare.com/workers-ai/), [Vectorize](https://developers.cloudflare.com/vectorize/), and [AI Gateway](https://developers.cloudflare.com/ai-gateway/), you just create an AutoRAG instance and point it at a data source, like an [R2](https://developers.cloudflare.com/r2/) storage bucket.

Behind the scenes, AutoRAG is powered by two processes: **indexing** and **querying**.

*   **Indexing** is an asynchronous process that runs in the background. It kicks off as soon as you create an AutoRAG, and automatically continues in cycles — reprocessing new or updated files after each previous job completes. During indexing, your content is transformed into vectors optimized for semantic search.
    
*   **Querying** is a synchronous process triggered when a user sends a search request. AutoRAG takes the query, retrieves the most relevant content from your vector database, and uses it to generate a context-aware response using an LLM.
    

Let’s take a closer look at how they work.

#### Indexing process

When you connect a data source, AutoRAG automatically ingests, transforms, and stores it as vectors, optimizing it for semantic search when querying:

1.  **File ingestion from data source:** AutoRAG reads directly from your data source. Today, it supports integration with Cloudflare R2, where you can store documents like PDFs, images, text, HTML, CSV, and more for processing. _Check out the_ [**_RAG to riches in 5 minutes tutorial below_**](https://blog.cloudflare.com/introducing-autorag-on-cloudflare/#rag-to-riches-in-under-5-minutes) _to learn how you can use Browser Rendering to parse webpages to use within your AutoRAG._
    
2.  **Markdown conversion:** AutoRAG uses [Workers AI’s Markdown Conversion](https://developers.cloudflare.com/workers-ai/markdown-conversion/) to convert all files into structured Markdown. This ensures consistency across diverse file types. For images, Workers AI is used to perform object detection followed by vision-to-language transformation to convert images into Markdown text.
    
3.  **Chunking:** The extracted text is chunked into smaller pieces to improve retrieval granularity.
    
4.  **Embedding:** Each chunk is embedded using Workers AI’s embedding model to transform the content into vectors.
    
5.  **Vector storage:** The resulting vectors, along with metadata like source location and file name, are stored in a Cloudflare’s Vectorize database created on your account.
    

![Image 3](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/5UK62iIO747BOe7JgazkBP/19a65b75cc4ad6b7fba31bff301cc133/Indexing.png)

#### Querying process

When an end user makes a request, AutoRAG orchestrates the following:

1.  **Receive query from AutoRAG API:** The query workflow begins when you send a request to either the AutoRAG’s AI Search or Search endpoint.
    
2.  **Query rewriting (optional):** AutoRAG provides the option to rewrite the input query using one of Workers AI’s LLMs to improve retrieval quality by transforming the original query into a more effective search query.
    
3.  **Embedding the query:** The rewritten (or original) query is transformed into a vector via the same embedding model used to embed your data so that it can be compared against your vectorized data to find the most relevant matches.
    
4.  **Vector search in Vectorize:** The query vector is searched against stored vectors in the associated Vectorize database for your AutoRAG.
    
5.  **Metadata + content retrieval:** Vectorize returns the most relevant chunks and their metadata. And the original content is retrieved from the R2 bucket. These are passed to a text-generation model.
    
6.  **Response generation:** A text-generation model from Workers AI is used to generate a response using the retrieved content and the original user’s query.
    

The end result is an AI-powered answer grounded in your private data — accurate, and up to date.

![Image 4](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/7ueRtSqcc6BcQL27SyFMzi/30712fdf3a50115f9560f6c3e82f76db/3.png)

### RAG to riches in under 5 minutes

Most of the time, getting started with AutoRAG is as simple as pointing it to an existing R2 bucket — just drop in your content, and you're ready to go. But what if your content isn’t already in a bucket? What if it’s still on a webpage or needs to first be rendered dynamically by a frontend UI? You're in luck, because with the [**Browser Rendering API**](https://developers.cloudflare.com/browser-rendering/), you can crawl your own websites to gather information that powers your RAG. The Browser Rendering REST API is now **generally available**, offering endpoints for common browser actions including extracting HTML content, capturing screenshots, and generating PDFs. Additionally, a crawl endpoint is coming soon, making it even easier to ingest websites.

In this walkthrough, we’ll show you how to take your website and feed it into AutoRAG for Q&A. We’ll use a Cloudflare Worker to render web pages in a headless browser, upload the content to R2, and hook that into AutoRAG for semantic search and generation.

#### Step 1. Create a Worker to fetch webpages and upload into R2

We’ll create a Cloudflare Worker that uses Puppeteer to visit your URL, render it, and store the full HTML in your R2 bucket. If you already have an R2 bucket with content you’d like to build a RAG for then you can skip this step.

1.  Create a new Worker project named `browser-r2-worker` by running:
    

```
npm create cloudflare@latest -- browser-r2-worker
```

For setup, select the following options:

*   _What would you like to start with?_ Choose Hello World Starter.
    
*   _Which template would you like to use?_ Choose Worker only.
    
*   _Which language do you want to use?_ Choose TypeScript.
    

2\. Install `@cloudflare/puppeteer`, which allows you to control the Browser Rendering instance:

```
npm i @cloudflare/puppeteer
```

3\. Create a new R2 bucket named `html-bucket` by running:

```
npx wrangler r2 bucket create html-bucket
```

4\. Add the following configurations to your Wrangler configuration file, so your Worker can use browser rendering and your new R2 bucket:

```
{
	"compatibility_flags": ["nodejs_compat"],
	"browser": {
		"binding": "MY_BROWSER"
	},
	"r2_buckets": [
		{
			"binding": "HTML_BUCKET",
			"bucket_name": "html-bucket",
		}
	],
}
```

5\. Replace the contents of src/index.ts with the following skeleton script:

```
import puppeteer from "@cloudflare/puppeteer";

// Define our environment bindings
interface Env {
	MY_BROWSER: any;
	HTML_BUCKET: R2Bucket;
}

// Define request body structure
interface RequestBody {
	url: string;
}

export default {
	async fetch(request: Request, env: Env): Promise<Response> {
		// Only accept POST requests
		if (request.method !== 'POST') {
return new Response('Please send a POST request with a target URL', { status: 405 });
		}

		// Get URL from request body
		const body = await request.json() as RequestBody;
		// Note: Only use this parser for websites you own
		const targetUrl = new URL(body.url); 

		// Launch browser and create new page
		const browser = await puppeteer.launch(env.MY_BROWSER);
		const page = await browser.newPage();

		// Navigate to the page and fetch its html
		await page.goto(targetUrl.href);
		const htmlPage = await page.content();

		// Create filename and store in R2
		const key = targetUrl.hostname + '_' + Date.now() + '.html';
		await env.HTML_BUCKET.put(key, htmlPage);

		// Close browser
		await browser.close();

		// Return success response
		return new Response(JSON.stringify({
			success: true,
			message: 'Page rendered and stored successfully',
			key: key
		}), {
			headers: { 'Content-Type': 'application/json' }
		});
	}
} satisfies ExportedHandler<Env>;
```

6\. Once the code is ready, you can deploy it to your Cloudflare account by running:

```
npx wrangler deploy
```

7\. To test your Worker, you can use the following cURL request to fetch the HTML file of a page. In this example we are fetching this blog page to upload into the html-bucket bucket:

```
curl -X POST https://browser-r2-worker.<YOUR_SUBDOMAIN>.workers.dev \
-H "Content-Type: application/json" \
-d '{"url": "https://blog.cloudflare.com/introducing-autorag-on-cloudflare"}'
```

#### Step 2. Create your AutoRAG and monitor the indexing

Now that you have created your R2 bucket and filled it with your content that you’d like to query from, you are ready to create an AutoRAG instance:

1.  In your [Cloudflare dashboard](https://dash.cloudflare.com/?to=/:account/ai/autorag), navigate to AI \> AutoRAG
    
2.  Select Create AutoRAG and complete the setup process:
    
    1.  **Select the R2 bucket** which contains your knowledge base, in this case, select the `html-bucket`.
        
    2.  **Select an embedding model** used to convert your data to vector representation. It is recommended to use the Default.
        
    3.  **Select an LLM** to use to generate your responses. It is recommended to use the Default.
        
    4.  **Select or create an AI Gateway** to monitor and control your model usage.
        
    5.  **Name your AutoRAG** as `my-rag`.
        
    6.  **Select or create a Service API token** to grant AutoRAG access to create and access resources in your account.
        
3.  Select Create to spin up your AutoRAG.
    

Once you’ve created your AutoRAG, it will automatically create a Vectorize database in your account and begin indexing the data. You can view the progress of your indexing job in the Overview page of your AutoRAG. The indexing time may vary depending on the number and type of files you have in your data source.

![Image 5](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/5qgy5VRqvKjBhdmSZ4riEE/e7dc59a4c615838704d9ec323bfdabfa/4.png)

#### Step 3. Test and add to your application

Once AutoRAG finishes indexing your content, you’re ready to start asking it questions. You can open up your AutoRAG instance, navigate to the Playground tab, and ask a question based on your uploaded content, like “What is AutoRAG?”.

Once you’re happy with the results in the Playground, you can integrate AutoRAG directly into the application that you are building. If you are using a Worker to build your application, then you can use the AI binding to directly call your AutoRAG:

```
{
  "ai": {
    "binding": "AI"
  }
}
```

Then, query your AutoRAG instance from your Worker code by calling the `aiSearch()` method. Alternatively you can use the `Search()` method to get a list of retrieved results without an AI generated response.

```
const answer = await env.AI.autorag('my-rag').aiSearch({
   query: 'What is AutoRAG?'
});
```

For more information on how to add AutoRAG into your application, go to your AutoRAG then navigate to Use AutoRAG for more instructions.

### Start building today

During the open beta, AutoRAG is **free to enable**.

AutoRAG is built entirely on top of Cloudflare’s Developer Platform, using the same tools you’d reach for if you were building a RAG pipeline yourself. When you create an AutoRAG instance, it provisions and runs on top of Cloudflare resources within your own account. These created resources are **billed as part of your Cloudflare usage**.These resources include:

*   [**R2**](https://developers.cloudflare.com/r2/)**:** stores your source data.
    
*   [**Vectorize**](https://developers.cloudflare.com/vectorize/)**:** stores vector embeddings and powers semantic retrieval.
    
*   [**Workers AI**](https://developers.cloudflare.com/workers-ai/)**:** converts images to Markdown, generates embeddings, rewrites queries, and generates responses.
    
*   [**AI Gateway**](https://developers.cloudflare.com/ai-gateway/)**:** tracks and controls your model’s usage.
    

To help manage resources during the beta, each account is limited to **10 AutoRAG** instances, with up to **100,000 files** **per AutoRAG**.

### What’s on the roadmap?

We’re just getting started with AutoRAG, and we have more planned throughout 2025 to make it more powerful and flexible. Here are a few things we’re actively working on:

*   **More data source integrations:** We’re expanding beyond R2, with support for new input types like direct website URL parsing (powered by browser rendering) and structured data sources like Cloudflare [D1](https://developers.cloudflare.com/d1/).
    
*   **Smarter, higher-quality responses:** We’re exploring built-in reranking, recursive chunking, and other processing techniques to improve the quality and relevance of generated answers.
    

These features will roll out incrementally, and we’d love your feedback as we shape what’s next. AutoRAG is built to evolve with your use cases so stay tuned.

### Try it out today!

Get started with AutoRAG today by visiting the [Cloudflare Dashboard](https://dash.cloudflare.com/?to=/:account/ai/autorag), navigate to AI \> AutoRAG, and select Create AutoRAG. Whether you’re building an AI-powered search experience, an internal knowledge assistant, or just experimenting with LLMs, AutoRAG gives you a fast and flexible way to get started with RAG on Cloudflare’s global network. For more details, refer to the [Developer Docs](https://developers.cloudflare.com/autorag). Also, try out the [Browser Rendering API](https://developers.cloudflare.com/browser-rendering/) that is now generally available for your browser action needs.

We’re excited to see what you build, and we’re here to help. Have questions or feedback? Join the conversation on the [Cloudflare Developers Discord](https://discord.com/channels/595317990191398933/1356674457355423895).

Cloudflare's connectivity cloud protects [entire corporate networks](https://www.cloudflare.com/network-services/), helps customers build [Internet-scale applications efficiently](https://workers.cloudflare.com/), accelerates any [website or Internet application](https://www.cloudflare.com/performance/accelerate-internet-applications/), [wards off DDoS attacks](https://www.cloudflare.com/ddos/), keeps [hackers at bay](https://www.cloudflare.com/application-security/), and can help you on [your journey to Zero Trust](https://www.cloudflare.com/products/zero-trust/).

Visit [1.1.1.1](https://one.one.one.one/) from any device to get started with our free app that makes your Internet faster and safer.

To learn more about our mission to help build a better Internet, [start here](https://www.cloudflare.com/learning/what-is-cloudflare/). If you're looking for a new career direction, check out [our open positions](https://www.cloudflare.com/careers).

[Developer Week](https://blog.cloudflare.com/tag/developer-week/)[AI](https://blog.cloudflare.com/tag/ai/)[Auto Rag](https://blog.cloudflare.com/tag/auto-rag/)[Browser Rendering](https://blog.cloudflare.com/tag/browser-rendering/)[Developer Platform](https://blog.cloudflare.com/tag/developer-platform/)[Developers](https://blog.cloudflare.com/tag/developers/)
