---
title: gRPC vs REST- Understanding gRPC, OpenAPI and REST
date: 2025-01-25
extra:
  source: https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them
  original_title: gRPC vs REST- Understanding gRPC, OpenAPI and REST
---
## Summary
**摘要**：
本文主要探讨了三种常见的API设计模型：REST、gRPC和OpenAPI，并对比了它们各自的特点及其在API设计中的应用场景。文章分析了不同模型的优缺点，旨在帮助开发者选择最适合特定项目需求的API设计方式。主要焦点涵盖了客户端操作流程、技术需求、限制性以及用于内部和公共API实施的优点。

**要点总结**：
1. **REST (Representational State Transfer)**：REST API设计以资源为中心，具有相对简单的接口样式。它们通常使用统一资源标识符（URL）供客户端使用，并且避免了在客户端代码中实现特定格式的URL需求。
2. **gRPC (Google Remote Procedure Call)**：gRPC API设计利用RPC（远程过程调用）模型，基于底层HTTP/2协议。它提供了一种强大的、可靠的接口交互方式，支持现代通信需求。gRPC需要专门的库和工具，并限制了使用传统HTTP库的灵活性。
3. **OpenAPI**：OpenAPI是一种用于描述API的标准语言，它允许在REST模式中自然地嵌入复合的HTTP /专用特性。使用OpenAPI，API设计者可以创建灵活的API，使用已定义的模板和参数动态生成URL。这提供了强大且功能丰富的API管理，但同时增加了设计和实现上的复杂性。
4. **对比及优缺点**：gRPC与OpenAPI在客户端访问模型上相似，但在技术需求、API扩展性和重型软件开发专有性的使用情况上有所差异。gRPC不需要详细了解复杂的URL格式，但要求更为复杂的技术栈。而OpenAPI提供了一种更灵活且功能丰富的方法来定义复杂API，牺牲了一定的通用性和简易性。
5. **选择建议**：是否选择gRPC或OpenAPI取决于API设计的需求、项目规模、应用技术栈、安全性考虑以及资源管理的可用性。对于新项目并考虑构建实体为中心的API，gRPC是一个有利的选项，尤其适合配合SDK（如Google Cloud Endpoints）进行部署。而内部API设计尤其需要高度控制客户端技术栈时，选择gRPC能保证软件栈的整体一致性和框架友好性。
## Full Content
Title: gRPC vs REST: Understanding gRPC, OpenAPI and REST and when to use them in API design

URL Source: https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them

Published Time: 2020-04-11

Markdown Content:
##### Martin Nally

Software Developer and API designer, Apigee

As most software developers no doubt know, there are two primary models for API design: RPC and REST. Regardless of model, most modern APIs are implemented by mapping them in one way or another to the same HTTP protocol. It has also become common for RPC API designs to adopt one or two ideas from HTTP while staying within the RPC model, which has increased the range of choices that an API designer faces. This post tries to explain the choices, and give guidance on how to choose between them.

gRPC is a technology for implementing RPC APIs that uses HTTP 2.0 as its underlying transport protocol. You might expect that gRPC and HTTP would be mutually exclusive, since they are based on opposite conceptual models. gRPC is based on the Remote Procedure Call (RPC) model, in which the addressable entities are procedures, and the data is hidden behind the procedures. HTTP works the inverse way. In HTTP, the addressable entities are “data entities” (called “resources” in the HTTP specifications), and the behaviors are hidden behind the data—the behavior of the system results from creating, modifying, and deleting resources.

In fact, many of the APIs created here at Google and elsewhere combine RPC with a few ideas from HTTP in an interesting way. These APIs adopt an entity-oriented model, as does HTTP, but are defined and implemented using gRPC, and the resulting APIs can be invoked using standard HTTP technologies. We will try to describe how this works, why it might be good for you, and where it might not.

Let's first take a closer look at how HTTP is commonly used for APIs.

The three primary ways to use HTTP for APIs
-------------------------------------------

Most public APIs and many private distributed APIs use HTTP as the transport, at least in part because organizations are accustomed to dealing with the security issues of allowing HTTP traffic on ports 80 and 443.

In my opinion there are three significant and distinct approaches for building APIs that use HTTP. They are:

1.  REST
    
2.  gRPC (and Apache Thrift and others)
    
3.  OpenAPI (and its competitors)
    

### REST

The least-commonly used API model is REST—only a small minority of APIs are designed this way, even though the word REST is used (or abused) more broadly. A signature characteristic of this style of API is that clients do not construct URLs from other information—they just use the URLs that are passed out by the server as-is. This is how the browser works—it does not construct the URLs it uses from piece parts, and it does not understand the website-specific formats of the URLs it uses; it just blindly follows the URLs that it finds in the current page received from the server, or that were bookmarked from previous pages or are entered by the user. The only parsing of a URL that a browser does is to extract the information required to send an HTTP request, and the only construction of URLs that a browser does is to form an absolute URL from relative and base URLs. If your API is a REST API, then your clients never have to understand the format of your URLs and those formats are not part of the API specification given to clients1.

REST APIs can be very simple. Lots of additional technologies have been invented for use with REST APIs—for example JSON API, ODATA, HAL, Siren or JSON Hyper-Schema and others—but you don't need any of those to do REST well.

### gRPC

A second model for using HTTP for APIs is illustrated by gRPC. gRPC uses HTTP/2 under the covers, but HTTP is not exposed to the API designer. gRPC-generated stubs and skeletons hide HTTP from the client and server too, so nobody has to worry how the RPC concepts are mapped to HTTP—they just have to learn gRPC.

The way a client uses a gRPC API is by following these three steps:

1.  Decide which procedure to call
    
2.  Calculate the parameter values to use (if any)
    
3.  Use a code-generated stub to make the call, passing the parameter values
    

### OpenAPI

Probably the most popular way of designing RPC APIs that use HTTP is to use specification languages like OpenAPI (formerly known as the Swagger specification).

A signature characteristic of the OpenAPI style of API is that clients use the API by constructing URLs from other information. The way a client uses an OpenAPI API is by following these three steps:

1.  Decide which OpenAPI URL path template to use
    
2.  Calculate the parameter values to use (if any)
    
3.  Plug the parameter values into the URL path template and send an HTTP request.
    

It should be immediately obvious that an API that works this way is not a REST API. The OpenAPI method of using HTTP requires clients to have detailed knowledge of the format of the URLs they use in requests and to construct URLs that conform to that format from other information. This is the opposite of the way a REST API works, where clients are completely blind to the formats of the URLs they use, and never have to construct them. The model supported by OpenAPI is very popular and successful and is one of the most important options available to API designers—the fact that the OpenAPI model is not REST does not diminish its usefulness or importance.

The second observation you will probably make is that the client model for using an OpenAPI API is very similar to the client model for using a gRPC API. Where a gRPC client chooses a procedure to call, an OpenAPI client chooses a URL path template to use. gRPC and OpenAPI clients both calculate parameter values. Where a gRPC client uses a stub procedure to combine the parameters with the procedure signature and make the call, an OpenAPI client inserts the parameter values into the URL path template and issues an HTTP request. The detail is different but the overall model is very similar. OpenAPI also includes tools that will optionally generate a client stub procedure in the client programming language that hides these details, making the client experience of the two even more similar.

One way to explain the close similarity between the client models of gRPC and OpenAPI is to consider OpenAPI to be a language for specifying a classic RPC API with a custom mapping to HTTP requests. If you accept that idea, then gRPC and OpenAPI are both RPC interface definition languages (IDLs), with the essential difference between them being that OpenAPI exposes the details of the underlying HTTP transport to the client and allows the API designer to control the mapping, while gRPC hides all the HTTP details using a predefined mapping.

Even if you don't accept the idea that the fundamental API model used by OpenAPI is just good old-fashioned RPC, it is hard to deny that there are some obvious parallels between the two, and they are both distinct from REST. Either way, I think the parallels help motivate the more detailed comparison that follows.

Each of these approaches has some benefits and drawbacks—we'll explore all three and leave you with some thoughts on how to decide which one is best for your application.

Look how easy and obvious RPC is!
---------------------------------

Here is an example from a popular [blog post](https://www.freecodecamp.org/news/rest-is-the-new-soap-97ff6c09896d/) that extols the virtues of RPC (we'll come back to this blog post later):

The blogger says that many people find it easy to define an RPC API for this problem, but struggle to figure out how to solve the same problem using HTTP, wasting a lot of time and energy without realizing any benefit to their project. I agree. One reason is that designing an API on top of HTTP is a skill that has to be learned, and there are many options.

Using the REST model is also easy and obvious
---------------------------------------------

Since we have designed many APIs using REST, it seems just as obvious to us how to express this example in REST. Here is what I would do:

The username, contact\_email, password, account\_URL, and other bits of data supplied by the client are just simple JSON name/value pairs in the request body. I left out the details of what is in the headers, and how the results are returned, because it's all explained in the HTTP specifications—there aren't really choices or decisions to make.

All the identifiers passed between the client and the server in both directions are URLs—there are no identifiers in the API that are not also URLs. Whenever one resource includes a reference to another, that reference is expressed using the other resource's URL. This technique is called hypertext, or hypermedia—if your API does not use URLs this way, it is not using the REST model, since hypertext linking is a signature feature that distinguishes REST from other models2. RPC APIs also express relationships between entities by including the identifiers of one entity in another entity, but those identifiers are not URLs that can be used directly without requiring additional information.

Advantages of REST
------------------

The claimed advantages of REST are basically those of the world wide web itself, like stability, uniformity, and universality. They are documented elsewhere, and REST is anyway a minority interest, so we won't dwell on them too much here. An exception is the entity-orientation inherent in the HTTP/REST model. This feature is of special interest because it has been widely discussed and adopted by proponents of non-REST models like gRPC and OpenAPI.

In my experience, entity-oriented models are simpler, more regular, easier to understand, and more stable over time than simple RPC models. RPC APIs tend to grow organically as one procedure after another is added, each one implementing an action that the system can perform.

An entity-oriented model provides an overall organization for the system's behaviors. For example, we are all familiar with the entity model of online shopping, with its products, carts, orders, accounts, and so on. If that capability were expressed using only RPC procedures, it would result in a long, unstructured list of procedures for browsing catalogs of products, adding them to carts, checking out, tracking deliveries, and returning products.

The list quickly becomes overwhelming, and it's difficult to achieve coherence between the procedure definitions. One way to bring structure and order to the list is to model all the behaviors using a standard set of procedures for each entity type. HTTP is inherently entity-oriented, but you can also add entity-orientation to RPC, as discussed later. Grouping procedures by entity type is also one of the key ideas of object-oriented languages.

How you use OpenAPI
-------------------

In OpenAPI, you define things called paths. An OpenAPI path looks like this in YAML:

APIs that define paths like these expose the values of {petId} to the client in various places in the API, and require the client to use an appropriate path definition in order to convert the {petId} value (and other values) into a URL that can be used in HTTP requests.

Expressing and using IDs this way is an alternative to the hypertext link that is a signature idea of REST.

OpenAPI calls the variables in these paths "parameters" and the combination of a path and an HTTP method is called an operation—similar terminology to RPC systems.

_**OpenAPI's use of URL templates with parameters can be viewed as a way to express RPC-like concepts with custom mappings to HTTP.**_

OpenAPI advantages and disadvantages
------------------------------------

In my opinion, OpenAPI has two fundamental characteristics that account for its success. The first is that the OpenAPI model is similar to the traditional RPC model with which most programmers are familiar and comfortable. The model also fits well with the concepts of the programming languages they use. The second reason is that it allows programmers to define a custom mapping of those RPC concepts to HTTP requests. This second characteristic brings with it both benefits and problems. The primary benefit is that clients can access the API using only standard HTTP technologies. This is especially important for public APIs because it means that the API is accessible from almost all programming languages and environments without requiring the client to adopt any additional technology. A disadvantage is that it can require significant effort to design the HTTP details—witness all the guidance on the web on what you should and shouldn't do, much of it contradictory—and further effort by the consumer to learn it.

When might gRPC be a better option than OpenAPI?
------------------------------------------------

Your design challenge for APIs described with OpenAPI is to define a combination of URL paths and HTTP methods to represent your "operations" and their "parameters." This can be tricky work, because there are lots of options. It is not clear that it is a good use of time and energy for most projects. Frustrations resulting from this approach are described with passion in the blog post comparing SOAP to REST by Pascal Chambon that we mentioned before, which also supplied the RPC example we opened with.

Chambon's post contains some misinformation and misunderstanding, and most of the [reaction to his post](https://philsturgeon.uk/api/2017/12/18/rest-confusion-explained/) focused on correcting that, but Chambon's mistakes actually add support to his main point, which is that designing your own mapping of RPC-like concepts onto HTTP is fairly complicated and difficult.

Most of the advice that was offered in response to Chambon's blog post promoted REST as an alternative to the RPC-like model that Chambon and most other people are familiar with. This is certainly an option—the simple REST example that we described at the beginning of this post is a minimalist's take on how exactly to do that.

Another option for Chambon is to keep his basic RPC model, but use gRPC instead of OpenAPI to express it. This avoids the complexity of defining a custom mapping of the API to HTTP. The RPC model has shown much more enduring popularity than any alternative, and if API designers are going to use an RPC-like model anyway, then they should weigh all the available technologies for doing that.

gRPC benefits
-------------

gRPC expresses an RPC API in an [interface description language](https://en.wikipedia.org/wiki/Interface_description_language) (IDL) that benefits from a long tradition of RPC IDLs that includes DCE IDL, Corba IDL, and many others. gRPC's IDL provides a simpler and more direct way of defining remote procedures than OpenAPI's approach of using URL paths, their parameters, and the HTTP methods that are used with them.

gRPC uses HTTP/2 under the covers, but gRPC does not expose any of HTTP/2 to the API designer or API user. gRPC has already made all the decisions on how to layer the RPC model on top of HTTP so you don't have to—those decisions are built into the gRPC software and generated code. This makes life simpler for API designers and clients. By contrast, OpenAPI requires API designers to specify the details of how the RPC model is expressed on top of HTTP for their specific API, and the client of the API has to learn that detail. An important advantage of the OpenAPI approach is that it lets API clients use standard HTTP tools and technologies, which for many API designers justifies the effort.

Regardless of how your API uses HTTP, it is likely that you will want to create client-side programming libraries in various languages for programmers to use. These programming libraries will take the form of procedures (possibly called functions or methods, depending on the programming language). One of gRPC's most attractive characteristics is that it is very good at generating client-side programming libraries that are intuitive for programmers to use and execute efficiently. OpenAPI can also generate client-side programming libraries, but I find the gRPC version simpler and more obvious, probably because its IDL only has to express RPC concepts and does not have to simultaneously describe a mapping of those concepts to HTTP.

APIs specified in gRPC are also simple to implement on the server side. Because of the frameworks, libraries, and code-generation that gRPC provides, it may be simpler to create the server implementation of a gRPC method than to write a standard HTTP request handler that parses incoming requests and calls the right implementation functions, despite the many frameworks that aim to help with that.

Another characteristic of gRPC is good performance. gRPC uses a binary payload that is efficient to create and to parse, and it exploits HTTP/2 for efficient management of connections. Of course, you can also use binary payloads and HTTP/2 directly without using gRPC, but this requires you and your clients to master more technology.

gRPC also avoids the problem that even the best HTTP-based APIs don't implement the whole HTTP protocol, which requires API providers and clients to figure out how to specify and learn which subset of HTTP is supported by a particular API. This is a problem for both REST and OpenAPI APIs. gRPC avoids this problem by requiring the client and the server to both adopt special software that implements the complete gRPC protocol. We hope gRPC succeeds in keeping that protocol stable for at least 25 years as HTTP has done, so that clients don't break when servers are upgraded and vice versa.

How do you combine the entity-oriented model with RPC?
------------------------------------------------------

Regardless of whether you are using gRPC or OpenAPI, the trick to using RPC in an entity-oriented way is to constrain the RPC method definitions to only those that map easily to the standard entity operations (Create, Retrieve, Update and Delete, often called CRUD3, plus List) for each resource type.

To use RPC in an entity-oriented style, you reverse the usual RPC thought process—instead of starting with procedure definitions, you start by defining your resource types, and then make RPC method definitions corresponding to the common entity operations on those types plus any additional operations you find necessary.

Using RPC in an entity-oriented style depends on teaching people a constrained usage pattern. In practice we see that APIs that are designed this way are sometimes a blend of entity-oriented and procedure-oriented concepts, which undermines some of the benefits.

So what are the downsides of gRPC?
----------------------------------

Every technology has downsides and limitations. We’ve already discussed some of OpenAPI's.

A popular feature of HTTP APIs is that clients can use them and servers can implement them using only general-purpose and widely available technologies. API calls can easily be made by simply typing URLs into a browser, or issuing cURL commands in a terminal window or in a bash script. Programmers can access or implement an HTTP API using no more technology than a basic HTTP library. In contrast, gRPC requires special software on both the client and the server. gRPC-generated code has to be incorporated into client and server build processes—this may be onerous to some, especially those who are used to working in dynamic languages like Javascript or Python where the build process, at least on development machines, may be non-existent. The Google [Cloud Endpoints](https://cloud.google.com/endpoints/docs/grpc/transcoding) product enables gRPC APIs to be accessed via HTTP and JSON without special software, which restores many options for clients, but not everyone wants to or is able to use Cloud Endpoints or find or build an equivalent.

It’s simple to write a bot that crawls the entirety of a REST API without metadata4, similarly to the way a browser or a web bot can crawl the entire HTML web. You can’t do this with an RPC-style API, regardless of whether it’s described using gRPC or OpenAPI, because RPC gives each entity type a different API that requires custom software or metadata to use it. In practice it usually isn't critical to be able to write general-purpose API clients, although it can be useful.

HTTP APIs are often proxied to add security features, perform input validation, map data formats, and solve many other problems. This typically requires adding, removing or modifying headers, and parsing and even modifying the body. Proxies use a combination of standard and custom headers to achieve this. These features are commonly implemented using products like Apigee Edge that do not require traditional programming skills or the kind of software development environments that can easily integrate gRPC. I think it would be much harder to do this sort of proxying for gRPC, and I am not aware of it being commonly done.

Using an entity-oriented approach with gRPC is mostly useful for new-builds—you won't find it easy to retrofit to an existing RPC API.

gRPC does not define a standard mechanism to prevent loss of data when two clients try to update the same resource at the same time, so if you use gRPC, you will likely have to invent your own. HTTP defines standard Etag and If-Match headers for this purpose—most of the HTTP APIs we design use these headers.

Nor does gRPC define a mechanism for making partial updates, so you will likely have to invent your own. HTTP defines a method—PATCH—for partial updates but does not say what a patch should look like or how to apply it. There are two additional IETF standards that fill this gap for JSON: [JSON merge patch](https://tools.ietf.org/html/rfc7386) and [JSON patch](https://tools.ietf.org/html/rfc6902). The first is simpler to use but does not handle all cases, particularly updates of arrays; the second handles more cases but is more complex to use. Most of the recent HTTP APIs I have built implement both standards and let the client choose; the Kubernetes API works this way too.

### Conclusion

There are a few APIs that use the same REST hypertext model used by the HTML web. They aim to inherit the core qualities of the HTML web, like stability, uniformity, and universality. If you already know how to design APIs this way, or are motivated to learn, then this is a fine approach. This is my own preference.

APIs that are described with OpenAPI are based on concepts analogous to those of RPC, but with a custom mapping to HTTP. This approach allows clients to access the resulting API using only commonly-available HTTP technologies, but it also adds additional design choices to these APIs, which can make them more difficult to design and build and more difficult to learn.

If you are considering using OpenAPI for an API, you should also consider the option of designing and implementing it using gRPC. The fundamental API models of the two are comparable and gRPC avoids the need to invent your own mapping onto HTTP.

Regardless of whether you use gRPC or OpenAPI for your API, you can obtain some, but not all, of the benefits of a REST API if you organize the API in an entity-oriented style, standardize the names of your procedures (for example by sticking to the verbs create, retrieve, update, delete and list), and impose other naming conventions. gRPC will bring some other benefits of its own. Using gRPC is especially attractive if one of the following is true:

*   You can use a product like Cloud Endpoints so that your clients are not forced to adopt gRPC technologies just because you did.
    
*   The API is internal, where you control the technology choices of all the clients as well as the server.
    

If you adopt gRPC in place of OpenAPI or REST, you should at least be aware of the much more limited opportunity to augment or remediate the API's behaviors in proxies, especially those implemented using API management tools like Apigee Edge or its competitors. Depending on how and where you intend to use gRPC, this may or may not be a problem.

As with most design challenges, there are many factors to consider and tradeoffs to be made. Hopefully this discussion has helped explain some of the ways in which HTTP and RPC-style APIs match up against one another.

_Special thanks to Nandan Sridhar and Marsh Gardiner for their contributions to this post._

* * *

1\. Some REST APIs allow clients to append a query to a base URL, in which case clients need to understand the query syntax supported by the server in the query portion of the URL, although they don't need to know the format of the rest of the URL. Some REST API designers allow queries to be encoded in URL paths, in which case their query URLs start to look like the OpenAPI-style URLs discussed below.  
2. Some REST commentators say that in order to claim compliance with the REST model you have to also implement something akin to HTML forms in JSON, but almost all would agree that if hypertext links are not a prominent feature of the API then it is not REST.  
3. Even in strictly entity-oriented APIs we sometimes come across the need for a fifth operation that we think of as "translate" or "convert". Translate takes in one entity and produces another without creating a persistent resource. HTTP doesn't have a special method for this operation, so we have to use POST for both "create" and "translate". Sometimes we also use POST for retrieve to get around limitations on URL length, usually for URLs that include queries.  
4. With a small amount of extra work on the server you can let the browser itself crawl a REST API.

Posted in

*   [API Management](https://cloud.google.com/blog/products/api-management)
*   [Application Development](https://cloud.google.com/blog/products/application-development)
*   [Apigee](https://cloud.google.com/blog/products/apigee)

