---
title: 一行代码降低 Vercel 40 倍成本
date: 2024-10-28
extra:
  source: https://www.memfree.me/blog/reduce-vercel-costs
  original_title: 一行代码降低 Vercel 40 倍成本
---
## Summary
**摘要**：
通过在 Next.js 应用中禁用 next/link 组件的预加载功能，本文作者成功将 Vercel 的函数调用次数降低了40倍。问题根源在于预加载功能导致的额外请求增加。在优化后，Vercel 的费用显著降低，节省了成本。文章还介绍了两种进一步优化成本的方法。一种是利用 Cloudflare 的 CDN 功能，通过 cloudflareLoader 来优化 Next.js 中图片的加载方式，从而减少带宽成本。第二种是通过客户端和服务器端操作的平衡，最大限度地利用本地存储与客户端计算能力来优化性能与成本。

**要点总结**：
1. **预加载优化**：通过禁用 next/link 组件的 prefetch 属性，降低了 Vercel 的函数调用次数，降低了成本。
2. **Cloudflare CDN 优化**：使用 cloudflareLoader 在 Next.js 中优化图片加载，实现成本更小的带宽消耗。
3. **性能与成本平衡**：合理利用本地存储减少对服务器请求，尽量利用客户端计算资源，减少成本。
4. **拆分思路**：对于计算密集型任务，考虑分发给设备执行，利用现代设备性能来优化应用性能而不增加成本。
5. **开源项目选择**：挑选适合的 Open Source 项目及工具来降低项目的总体成本，提高应用效率。
## Full Content
Title: Reducing Vercel Costs by 40 Times with Just One Line of Code

URL Source: https://www.memfree.me/blog/reduce-vercel-costs

Markdown Content:
[](https://www.memfree.me/blog/reduce-vercel-costs#origin)Origin
----------------------------------------------------------------

Received a warning from Vercel 2 days ago

Received a warning from Vercel 1 day ago

Today, another warning from Vercel

[](https://www.memfree.me/blog/reduce-vercel-costs#analysis)Analysis
--------------------------------------------------------------------

First, let's take a look at the data for Vercel's `Edge Middleware invocations`, `Function Invocation`, and `Edge Requests` usage.

![Image 1: Vercel Edge Request](https://utfs.io/f/vbtdRXZo1BHw1u78rQZywGtriuBSm5T9xUf4Oq08YVRXlcQe)

![Image 2: Vercel Function Invocation](https://utfs.io/f/vbtdRXZo1BHwp5NbXBKnhCPiefYnbogNz87vQWA96qLBl3Vt)

![Image 3: Vercel Edge Middleware](https://utfs.io/f/vbtdRXZo1BHwusa3u9R8Pa2gmZHpslWzObuD1KkS9iYh7I4G)

You may notice that starting from October 13, various metrics experienced a nearly 10 to 50 times surge every day. However, the UV and PV data I obtained from umami only shows anomalies for October 14, indicating that the recent 4 days of edge requests and function requests do not align with the actual traffic data.

After clicking on the link in Vercel's email about [how to optimize Edge Requests](https://vercel.com/docs/pricing/networking#optimizing-edge-requests), Vercel provided three optimization points:

1.  Identify frequent remounts
2.  Over-polling or data fetching
3.  **Reduce prefetching**: **While prefetching can improve perceived page navigation performance, it also increases the number of requests to your website. Consider reducing the amount of prefetching, for instance, using prefetch="false" on the Link component in frameworks like Next.js**.

Upon seeing the third point, combined with my recent code changes and recent strategies for reducing costs in NextJS, I immediately realized that the likely problem was the prefetching by the next/link component.

In recent days, I added a showcase and feature section to the [MemFree AI UI Generator](https://www.memfree.me/generate-ui) page, with the showcase containing 9 Links and the feature section also containing 9 Links.

So, I promptly submitted a code change to disable prefetch for all next link components. Here’s the code commit: [Disable next link prefetchs Beta](https://github.com/memfreeme/memfree/commit/a2ec1a7261d541f5b462e8876efc83209d22a8e4), while also disabling the previous manual prefetch for the Pricing Page, which is documented in this code commit: [Remove pricing page prefetch](https://github.com/memfreeme/memfree/commit/3f3aa71751135026434f62cd92b01a71e646cb14).

[](https://www.memfree.me/blog/reduce-vercel-costs#optimization-results-request-count-reduced-by-40-times)Optimization Results: Request Count Reduced by 40 Times
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

After going live, the results were quite remarkable:

![Image 4: Vercel Function Invocation Optimization](https://utfs.io/f/vbtdRXZo1BHwsBEsWkXRna6lLJgB9bjzc20V3r8DXdmvkTwy)

The time period shown in the image is from 3 PM to after 8 PM Beijing time.

At the same time, the real UV and PV data is as follows:

![Image 5: MemFree UV PV](https://utfs.io/f/vbtdRXZo1BHw4cylWUAzBxdLbRwCfYlDGH2q8TPEhXjgWepm)

**From the chart, it is evident that the PV data at 3 PM is a quarter of that at 8 PM, while the Function Invocation count is 10 times that at 8 PM, meaning that simply disabling prefetching for a next link resulted in a 40-fold reduction in Function Invocation counts.**

Some may ask if disabling Link's prefetch affects performance significantly. From the actual online performance of MemFree, the impact on performance is virtually negligible.

Thus, if you encounter exceeding the free limits on Vercel's Function Invocation and Edge Requests, consider optimizing with next link's prefetch="false".

Today, regarding cost optimization on Vercel, I would like to share two other optimization points that I have deeply felt recently:

[](https://www.memfree.me/blog/reduce-vercel-costs#cloudflareloader--cloudflare-cdn-optimization-for-next-image-bandwidth-costs)cloudflareLoader + Cloudflare CDN Optimization for Next Image Bandwidth Costs
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In [MemFree AI UI Generator](https://www.memfree.me/generate-ui), I stored 9 videos introducing the features on Cloudflare R2. Later, when implementing the showcase's images, I also conveniently stored them on Cloudflare R2, which has CDN acceleration enabled by default for images and videos, allowing for fast access.

To optimize the Largest Contentful Paint on mobile devices, I needed to optimize the loading of the first image in the showcase using Next's Image component. The core code is as follows:

However, I found that Next's Image component would cache images from the CDN again, which is actually unnecessary, and Cloudflare does not charge for traffic, while Vercel does. To solve this problem, we will utilize Cloudflare's transform-images service and define a cloudflareLoader in NextJs.

You may refer to:

[Cloudflare transform-images Integrate with frameworks](https://github.com/memfreeme/memfree/commit/3f3aa71751135026434f62cd92b01a71e646cb14).

I previously thought that the next/image component had no effect on network images, which is why I did not use next image in the network images of MemFree's AI Search. Had I used it, my costs would have increased significantly.

[](https://www.memfree.me/blog/reduce-vercel-costs#balancing-cost-and-performance-with-server-actions-and-server-components)Balancing Cost and Performance with Server Actions and Server Components
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

React's Server Actions and Server Components offer many advantages, and many templates and examples from Vercel heavily rely on Server Actions and Server Components. While Server Actions + Server Components + Vercel’s caching can indeed achieve excellent performance, we must not overlook the cost factor.

There are two points to note:

1.  **Everyone should make use of the browser's Local Storage as much as possible to reduce requests to the server.** This remains true regardless of how technology evolves, as Local Storage offers the best performance for free. Server requests on Vercel’s serverless platform incur costs. For example, regarding historical messages in AI Search or AI Chat, many examples from Vercel entirely rely on server-side operations, which can significantly drive up database costs. In such typical cases, we can opt to cache data in the browser's Local Storage. The caching code for historical messages in MemFree can be found at [MemFree Search local-history](https://github.com/memfreeme/memfree/blob/main/frontend/lib/store/local-history.ts).
2.  **Everyone should leverage the computing power of computers and mobile devices as much as possible**, as this computing power continues to grow stronger and remains free. Although server-side computation and rendering come with various advantages, we have to pay extra for them. For example, in implementing the AI UI Generator feature for MemFree recently, one of the most time-consuming problems I encountered was **how to achieve efficient rendering of React + TailWind + Shadcn UI components**. I researched and considered 7 or 8 different solutions, with two main ideas being server-side rendering and client-side rendering. However, due to the cost issues associated with server-side rendering, I eliminated that option. In client-side rendering, many open-source projects used codesandbox, but its performance is poor and rendering is slow. Ultimately, I decided to **build an efficient React + TailWind + Shadcn UI component rendering solution from scratch using MemFree**. I will share the specific ideas and plans later, with the core code being found here [MemFree React Preview Code](https://github.com/memfreeme/memfree/tree/main/frontend/components/code).

I hope this sharing is helpful to everyone. MemFree will continue to use Vercel and will share more experiences in reducing Vercel costs in the future. Feel free to follow MemFree's Twitter.

