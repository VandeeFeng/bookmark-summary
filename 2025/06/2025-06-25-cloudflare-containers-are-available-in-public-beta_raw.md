Title: Containers are available in public beta for simple, global, and programmable compute

URL Source: https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/

Published Time: 2025-06-24T16:00:22.197Z

Markdown Content:
2025-06-24

6 min read

![Image 1](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/LMNkP0jBIJwYeaNwiLhqU/804dab58f328e8a30069f81793d47bec/image1.png)

We’re excited to announce that [Cloudflare Containers](https://blog.cloudflare.com/cloudflare-containers-coming-2025/) are now available in beta for all users on paid plans.

You can now run new kinds of applications alongside your Workers. From media and data processing at the edge, to backend services in any language, to CLI tools in batch workloads — Containers open up a world of possibilities.

Containers are tightly integrated with Workers and the rest of the developer platform, which means that:

*   Your workflow stays **simple**: just define a Container in a few lines of code, and run`wrangler deploy`, just like you would with a Worker.

*   Containers are **global:**as with Workers, you just deploy to Region:Earth. No need to manage configs across 5 different regions for a global app.

*   You can **use the right tool for the job**: routing requests between Workers and Containers is easy. Use a Worker when you need to be ultra light-weight and scalable. Use a Container when you need more power and flexibility.

*   Containers are **programmable**: container instances are spun up on-demand and controlled by Workers code. If you need custom logic, just write some JavaScript instead of spending time chaining together API calls or writing Kubernetes operators.

Want to try it today? Deploy your first Container-enabled Worker:

[![Image 2: Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/containers-template)

A tour of Containers
--------------------

Let’s take a deeper look at Containers, using an example use case: code sandboxing.

Let’s imagine that you want to run user-generated (or AI-generated) code as part of a platform you’re building. To do this, you want to spin up containers on demand. Each user needs their own isolated container, the users are distributed globally, and you need to start each container quickly so the users aren’t waiting.

You can set this up easily on Cloudflare Containers.

#### Configuring a Container

In your Worker, use the [Container class](https://github.com/cloudflare/containers) and [wrangler.jsonc](https://developers.cloudflare.com//workers/wrangler/configuration/#containers) to declare some basic configuration, such as your Container’s default port, a sleep timeout, and which image to use, then route to it via the Worker.

For each unique ID passed to the Container’s binding, Cloudflare will spin up a new Container instance and route requests to it. When a new instance is requested, Cloudflare picks the best location across our global network where we’ve pre-provisioned a ready-to-go container. This means that you can deploy a container close to an end user no matter where they are. And the initial container start takes just a few seconds. You don’t have to worry about routing, provisioning, or scaling.

This example Worker will route requests to a unique container instance for each sandbox ID given at the path `/sandbox/ID` and will be handled by standard Worker JavaScript otherwise:

```
export class MyContainer extends Container {
  defaultPort = 8080; // The default port for the container to listen on
  sleepAfter = '5m'; // Sleep the container if no requests are made in this timeframe
}

export default {
  async fetch(request, env) {
    const pathname = new URL(request.url).pathname;

    // handle request with an on-demand container instance
    if (pathname.startsWith('/sandbox/')) {
      const sessionId = pathname.split("/")[2]
      const containerInstance = getContainer(env.CONTAINER_SANDBOX, sessionId)
      return await containerInstance.fetch(request);
    }

    // handle request with my Worker code otherwise
    return myWorkerRequestHandler(request);
  },
};
```

#### Familiar and easy development workflow with `wrangler dev`

To configure which container image to use, you can provide an image URL in wrangler config or a path to a local Dockerfile.

This config tells wrangler to use a locally defined image:

```
"containers": [
  {
    "class_name": "ContainerSandbox",
    "image": "./Dockerfile",
    "max_instances": 80,
    "instance_type": "basic"
  }
]
```

When developing your application, you just run `wrangler dev` and the container image will be automatically built and routable via your local Worker. This makes it easy to iterate on container code while making changes to your Worker at the same time. When you want to rebuild your image, just press “R” on your keyboard from your terminal running `wrangler dev`, and the Container is rebuilt and restarted.

#### Shipping your Container-enabled Worker to production with `wrangler deploy`

When it’s time to deploy, just run `wrangler deploy`. Wrangler will push your image to your account, then it will be provisioned in various locations across Cloudflare’s global network.

You don’t have to worry about “artifact management”, or distribution, or auth, or jump through hoops to integrate your container with Workers. You just write your code and deploy it.

#### Observability is built-in

Once your Container is in production, you have the visibility you need into how things are going, with end-to-end observability.

From the Cloudflare dashboard, you can easily track status and resource usage across Container instances with built-in metrics:

![Image 3](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/1cMDL8qejpD9TnaVYgKeLD/cf42573c1315f0364c0d225bb77a76af/image4.png)
And if you need to dive deeper, you can dig into logs, which will be retained in the Cloudflare UI for seven days or [pushed to an external sink](https://developers.cloudflare.com/logs/about/) of your choice:

![Image 4](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/2AusbmokynDaErssVFyu4A/3bb617ff9c2e488cdaee20612cb6bd15/image3.png)
#### Try it yourself

Want to give it a shot? Check out [this example Worker for running sandboxed code](https://github.com/craigsdennis/sandboxing-day-containers) in a Container, and deploy it with one click.

Or better yet, if you have an image sitting around that you’ve been dying to deploy to Cloudflare, you can get started with [our docs here](https://developers.cloudflare.com//containers/get-started/).

A world of possibilities
------------------------

We’re excited about all the new types of applications that are now possible to build on Workers. We’ve heard many of you tell us over the years that you would love to run your entire application on Cloudflare, if only you could deploy this one piece that needs to run in a container.

Today, you can run libraries that you couldn't run in Workers before. For instance, try [this Worker that uses FFmpeg to convert video to a GIF](https://github.com/megaconfidence/wifski/).

Or you can [run a container as part of a cron job](https://github.com/mikenomitch/cron-container). Or deploy a [static frontend with a containerized backend](https://github.com/mikenomitch/static-frontend-container-backend). Or even run a [Cloudflare Agent that uses a Container to run Claude Code](https://github.com/ghostwriternr/claude-code-containers) on your behalf.

The [integration with the rest of the Developer Platform](https://blog.cloudflare.com/cloudflare-containers-coming-2025/#integrating-with-more-of-cloudflares-developer-platform) makes Containers even more powerful: [use Durable Objects](https://blog.cloudflare.com/cloudflare-containers-coming-2025/#durable-objects-as-programmable-sidecars) for state management, [Workflows](https://developers.cloudflare.com/workflows/), [Queues](https://developers.cloudflare.com/queues/), and [Agents](https://agents.cloudflare.com/) to compose complex behaviors, [R2](https://developers.cloudflare.com/r2/) to store Container data or media, and more.

Pricing and packaging
---------------------

As with the rest of our Cloudflare developer products, we wanted to apply the same principles to our developer platform with transparent pricing that scales up and down with your usage.

Today, you can select from the following instances at launch (and yes, we plan to add larger instances over time):

**Name****Memory****CPU****Disk**
dev 256 MiB 1/16 vCPU 2 GB
basic 1 GiB 1/4 vCPU 4 GB
standard 4 GiB 1/2 vCPU 4 GB

You only pay for what you use —charges start when a request is sent to the container or when it is manually started. Charges stop after the container instance goes to sleep, which can happen automatically after a timeout. This makes it easy to scale to zero, and allows you to get high utilization even with bursty traffic.

Containers are billed for every 10ms that they are actively running at the following rates, with monthly amounts included in _Workers Standard_:

*   **Memory**: $0.0000025 per GiB-second, with 25 GiB-hours included

*   **CPU**: $0.000020 per vCPU-second, with 375 vCPU-minutes included

*   **Disk** $0.00000007 per GB-second, with 200 GB-hours included

Egress from Containers is priced at the following rates, with monthly amounts included in _Workers Standard_:

*   North America and Europe: $0.025 per GB with 1 TB included

*   Australia, New Zealand, Taiwan, and Korea: $0.050 per GB with 500 GB included

*   Everywhere else: $0.040 per GB with 500 GB included

See [our previous blog post](https://blog.cloudflare.com/cloudflare-containers-coming-2025/#pay-for-what-you-use-and-use-the-right-tool) for a more in-depth look into pricing with an example app.

What’s coming next?
-------------------

With today’s release, we’ve only just begun to scratch the surface of what Containers will do on Workers. This is the first step of many towards our vision of a simple, global, and highly programmable Container platform.

We’re already thinking about what’s next, and wanted to give you a preview:

*   **Higher limits and larger instances** – We currently limit your concurrent instances to 40 total GiB of memory and 40 total vCPU. This is enough for some workloads, but many users will want to go higher — a lot higher. Select customers are already scaling well into the thousands of concurrent containers, and we want to bring this ability to more users. We will be raising our limits over the coming months to allow for more total containers and larger instance sizes.

*   **Global autoscaling and latency-aware routing** – Currently, containers are addressed by ID and started on-demand. For many use cases, users want to route to one of many stateless container instances deployed across the globe, then autoscale live instances automatically. Autoscaling will be activated with a single line of code, and will enable easy routing to the nearest ready instance.

```
class MyBackend extends Container {
  defaultPort = 8080;
  autoscale = true; // global autoscaling on - new instances spin up when memory or CPU utilization is high
}

// routes requests to the nearest ready container and load balance globally
async fetch(request, env) {
  return getContainer(env.MY_BACKEND).fetch(request);
}
```

*   **More ways to communicate between Containers and Workers** – We will be adding more ways for your Worker to communicate with your container and vice versa. We will add an `exec` command to run shell commands in your instance and handlers for HTTP requests _from_ the container to Workers. This will allow you to more easily extend your containers with functionality from the entire developer platform, reach out to other containers, and programmatically set up each container instance.

```
class MyContainer extends Container {
  // sets up container-to-worker communication with handlers
  handlers = {
    "example.cf": "handleRequestFromContainer"
  };

  handleRequestFromContainer(req) {
    return new Response("You are responding from Workers to a Container request to a specific hostname")
  }

  // use exec to run commands in your container instance
  async cloneRepo(repoUrl) {
    let command = this.exec(`git clone ${repoUrl}`)
    await command.print()
  }  
}
```

*   **Further integrations with the Developer Platform** – We will continue to integrate with the developer platform with first-party APIs for our various services. We want it to be dead simple to mount [R2 buckets](https://developers.cloudflare.com/r2/), reach [Hyperdrive](https://developers.cloudflare.com/hyperdrive/), access [KV](https://developers.cloudflare.com/kv/), and more.

And we are just getting started. Stay tuned for more updates this summer and over the course of the entire year.

Try Containers today
--------------------

The first step is to deploy your own container. Run `npm create cloudflare@latest -- --template=cloudflare/templates/containers-template` or click the button below to deploy your first Container to Workers.

[![Image 5: Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/containers-template)

We’re excited to see all the ways you will use Containers. From new languages and tools, to simplified Cloudflare-only architectures, to advanced programmatic control over container creation, you now have the ability to do even more on the Developer Platform. It is just a wrangler deploy away.

Cloudflare's connectivity cloud protects [entire corporate networks](https://www.cloudflare.com/network-services/), helps customers build [Internet-scale applications efficiently](https://workers.cloudflare.com/), accelerates any [website or Internet application](https://www.cloudflare.com/performance/accelerate-internet-applications/), [wards off DDoS attacks](https://www.cloudflare.com/ddos/), keeps [hackers at bay](https://www.cloudflare.com/application-security/), and can help you on [your journey to Zero Trust](https://www.cloudflare.com/products/zero-trust/).

Visit [1.1.1.1](https://one.one.one.one/) from any device to get started with our free app that makes your Internet faster and safer.

To learn more about our mission to help build a better Internet, [start here](https://www.cloudflare.com/learning/what-is-cloudflare/). If you're looking for a new career direction, check out [our open positions](https://www.cloudflare.com/careers).

[Cloudflare Workers](https://blog.cloudflare.com/tag/workers/)[Containers](https://blog.cloudflare.com/tag/containers/)[Developers](https://blog.cloudflare.com/tag/developers/)[AI](https://blog.cloudflare.com/tag/ai/)
