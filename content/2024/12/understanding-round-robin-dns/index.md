---
title: Understanding Round Robin DNS
date: 2024-12-14
extra:
  source: https://blog.hyperknot.com/p/understanding-round-robin-dns
  original_title: Understanding Round Robin DNS
---
## Summary
**摘要**：
文章详细探讨了Round Robin DNS的工作原理以及发生在不同浏览器和CDN在选取服务器时的行为差异。主要展示了在同一配置下，来自不同服务器的数据如何通过这个DNS策略均衡分发到用户终端。浏览器和CDN在连接服务器时采用不同的策略，一些浏览器如Chrome和Safari在选定服务器后可能会保持连接多段时间，而Safari较为准确地选择了最近的服务器。Cloudflare在客户端IP基础上做出默认选择，但在服务器离线时并未察觉并及时切换服务器。文章最后批判了Cloudflare在服务器离线检测和选择上的不足之处，并提到了存在的潜在问题和改进方向。

**要点总结**：
1. **Round Robin DNS的工作原理**：在Round Robin DNS中，为同一子域指定多个服务器，从而能够实现负载均衡，并能自动检测离线的服务器。
2. **浏览器对服务器的选择**：浏览器和CDN在连接服务器时采用的算法不同。Chrome可能会随机选择服务器，且极少数情况下显示随机切换卫生，而Safari表现更为准确，优先选择距离最近的服务器。
3. **Cloudflare的局限性**：Cloudflare在客户端IP基础上进行选择，但在服务器离线时未能及时察觉并切换至其他可用服务器，存在明显的后台行为不足和开发模糊之处。
4. **离线服务器的检测与处理**：文章提到浏览器和CDN在面对离线服务器时能快速处理并实现服务器切换，相比之下，Cloudflare的离线服务器处理机制表现出缺陷。
5. **改善与批评**：作者对Cloudflare在离线服务器检测和自动选择低位延迟服务器上存在不足之处提出批评，并指出潜在改进的空间，强调检测离线服务器及切换至低延迟服务器的重要性。

---

Markdown格式如下：
- Round Robin DNS的工作原理
- 浏览器对服务器的选择差异
- Cloudflare的局限性：未及时检测离线服务器
- 离线服务器的检测与处理：浏览器和CDN的部分机制更优
- 改善与批评：对Cloudflare的性能改进提出建议
## Full Content
Title: Understanding Round Robin DNS

URL Source: https://blog.hyperknot.com/p/understanding-round-robin-dns

Published Time: 2024-10-26T12:29:33+00:00

Markdown Content:
For [OpenFreeMap](https://openfreemap.org/), I'm using servers behind Round Robin DNS. In this article, I'm trying to understand how browsers and CDNs select which one to use.

Normally, when you are serving a website from a VPS like Digital Ocean or Hetzner, you add a single A record in your DNS provider's control panel.

[![Image 34](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15591e83-689a-4821-8309-919e0528a434_768x140.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15591e83-689a-4821-8309-919e0528a434_768x140.png)

This means that rr-direct.hyperknot.com will serve data from 5.223.46.55.

In Round Robin DNS, you specify multiple servers for the same subdomain, like this.

[![Image 35](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c97e110-0b2c-429b-b764-acb2331afa7e_792x268.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0c97e110-0b2c-429b-b764-acb2331afa7e_792x268.png)

This allows you to share the load between multiple servers, as well as to automatically detect which servers are offline and choose the online ones.

It's an amazingly simple and elegant solution that avoids using Load Balancers. It's also free, and you can do it on any DNS provider, whereas Load Balancing solutions can get really expensive (even on Cloudflare, which is otherwise very reasonably priced).

I became obsessed with how it works. I mean, on the surface, everything is elegant, but how does a browser decide which server to connect to?

In theory, there is an [RFC 8305](https://datatracker.ietf.org/doc/html/rfc8305) called Happy Eyeballs (also linking to [RFC 6724](https://datatracker.ietf.org/doc/html/rfc6724#section-6)) about how the client should sort addresses before connecting.

Now, this is definitely above my experience level, but [this section](https://datatracker.ietf.org/doc/html/rfc8305#section-4) seems like the closest to answering my question:

> If the client is stateful and has a history of expected round-trip times (RTTs) for the routes to access each address, it SHOULD add a Destination Address Selection rule between rules 8 and 9 that prefers addresses with lower RTTs.

So in my understanding, it's basically:

*   Checking if servers are online/offline
    
*   Sort the online ones according to ping times
    

Let's see how it works in practice.

I created 3 VPSs around the world: one in the US, one in the EU, and one in Singapore. I made 3 proxied and 3 non-proxied A records in Cloudflare.

[![Image 36](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13e623d8-a8c8-44e9-ad80-0e61b53323f6_1186x516.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13e623d8-a8c8-44e9-ad80-0e61b53323f6_1186x516.png)

They run nginx with a config like this:

```
server {
    server_name rr-direct.hyperknot.com rr-cf.hyperknot.com;

    # this is basically a wildcard block
    # so /a/b/c will return the same color.png file
    location / {
        root /data;
        rewrite ^ /color.png break;
    }

    location /server {
        alias /etc/hostname;
        default_type text/plain;
    }
}
```

So they serve a color.png, which is a 1px red/green/blue PNG file, as well as their hostname, which is test-eu/us/sg.

[I made a HTML test page](https://assets.openfreemap.com/share/2024-10/rr.html), which fills a 10x10 grid with random images.

The server colors are the following:

*   US - green
    
*   EU - blue
    
*   SG - red
    

Important: I'm testing from Europe; the EU server is much closer to me than US or especially the SG one. I should be seeing blue boxes!

Chrome selects somewhat randomly between all locations, but once selected, it sticks with it. It re-evaluates the selection after a few hours. In this case, it was stuck with SG for hours, even though it is by far the slowest server for me.

[![Image 37](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82985913-6f42-4fd2-b009-61fedac5294f_958x570.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82985913-6f42-4fd2-b009-61fedac5294f_958x570.png)

Also, an interesting behavior on Chrome was when not using HTTP/2: it can sometimes choose randomly between two servers, creating a pattern like this. Here it's choosing between EU and US randomly.

[![Image 38](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36c86eaa-335c-4ceb-af52-e4db28fefcf4_958x570.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36c86eaa-335c-4ceb-af52-e4db28fefcf4_958x570.png)

Behaves similarly to Chrome, selects a location randomly on startup and then sticks with it. If I restart the browser, it picks a different random location.

[![Image 39](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67cfbcbe-87f8-4d83-a46e-a970b4f34fd7_958x570.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67cfbcbe-87f8-4d83-a46e-a970b4f34fd7_958x570.png)

To my biggest surprise, Safari always selects the closest server correctly. Even if it goes offline for a while, after a few refreshes, it always finds the EU server again!

[![Image 40](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa86d8b48-6660-4c76-b063-b10c73ec6fee_958x570.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa86d8b48-6660-4c76-b063-b10c73ec6fee_958x570.png)

Curl also works correctly. First time it might not, but if you run the command twice, it always corrects to the nearest server.

If you have multiple VPSs around the world, try this command via ssh and see which one gets selected:

```
curl https://rr-direct.hyperknot.com/server
test-us

curl https://rr-direct.hyperknot.com/server
test-eu
```

Cloudflare picks a random location based on your client IP and then sticks with it. (It behaves like client\_ip\_hash modulo server\_num or similar.)

As you have seen in the images, the right-side rectangle is always green. On my home IP, no matter what I do, Cloudflare goes to the US server. Curl shows the same.

```
curl https://rr-cf.hyperknot.com/server
test-us
```

Now, if I go to my mobile hotspot, it always connects to the EU server.

If I log into some VPSes and run the same curl command, I can see this behavior across the world. Every VPS gets connected to a totally random location around the world, but always the same.

```
curl https://rr-cf.hyperknot.com/server
test-sg
```

So what happens when one of the servers is offline? Say I stop the US server:

```
service nginx stop
```

[![Image 41](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4261f746-b85e-4407-bf6e-d01c5962e7bb_958x570.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4261f746-b85e-4407-bf6e-d01c5962e7bb_958x570.png)

[![Image 42](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb15577b7-7255-4c5f-bb86-0a66ed463bce_958x570.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb15577b7-7255-4c5f-bb86-0a66ed463bce_958x570.png)

[![Image 43](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F03015118-9864-4c4b-ab35-9e04b42b08f3_958x570.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F03015118-9864-4c4b-ab35-9e04b42b08f3_958x570.png)

```
curl https://rr-direct.hyperknot.com/server
test-eu
```

As you can see, all clients correctly detect it and choose an alternative server.

Actually, they do this fallback so well that if I turn off the server while they are loading, they correct within < 1 sec! Here is an animation of the 50x50 version of the same grid, on Safari:

And what about Cloudflare? As you can see in the screenshots above, Cloudflare does **not** detect an offline server. It keeps accessing the server it decided for your IP, regardless of whether it's online or offline.

If the server is offline, you are served offline. In curl, it returns:

```
curl https://rr-cf.hyperknot.com/server
error code: 521
```

I've been trying to understand what this behavior is, and I highly suspect it's a **bug** in their network. One reference I found in their [documentation](https://developers.cloudflare.com/fundamentals/basic-tasks/protect-your-origin-server/#zero-downtime-failover) is this part:

[![Image 44](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86323993-bbaa-4d0b-b21c-72c2b44a2fcc_1388x622.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86323993-bbaa-4d0b-b21c-72c2b44a2fcc_1388x622.png)

Based on this documentation - and by common sense as well - I believe Cloudflare should also behave like browsers and curl do.

1.  At the very least, offline servers should be detected.
    
2.  Moreover, it would also be really nice if the server with the lowest latency were selected, like in Safari!
    

I mean, currently, if you have one server in the US and one in New Zealand, exactly 50% of your US users will be served from New Zealand, which makes no sense. Also, for Safari users, it's actually slower compared to not using Cloudflare!

There is a [HN discussion now](https://news.ycombinator.com/item?id=41955912), where both the CEO and the CTO of Cloudflare replied!

Note 1: I've tried my best to understand articles **[1](https://t.co/MefximeFqU)**, **[2](https://t.co/IlYL4Emgz7)**, **[3](https://t.co/GKE4mdUiNH)** which Matthew Prince **[pointed out to me](https://x.com/eastdakota/status/1850103009826554285)** on X. As I understand, they are referring to Cloudflare servers as "servers", not users' servers behind A records. Also, I couldn't find anything related to Round Robin DNS.

Note 2: If you have any idea **how I can keep running** this experiment without paying for 3 VPS-es around the world, please comment below. I'd love to keep it running. Is there a serverless platform that supports HTTPS and Round Robin DNS?

#### Discussion about this post

