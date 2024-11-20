---
title: Exploring the browser rendering process | Little Things
date: 2024-11-20
extra:
  source: https://abhisaha.com/blog/exploring-browser-rendering-process/
  original_title: Exploring the browser rendering process | Little Things
---
## Summary
**摘要**：
文章提供了详细说明了浏览器渲染过程的复杂性，从用户输入网址到网页内容在屏幕上呈现的环节。过程包括DNS解析、TCP/TLS握手、HTTP请求响应周期、HTML和CSS的解析、DOM树和CSSOM树的创建，最终是渲染树的创建。文章特别探讨了布局和绘画两个关键步骤，解析了CSS属性如何影响页面元素的定位。

**要点总结**：

1. **DNS解析**：输入网址后，浏览器需通过DNS查询将域名解析为IP地址，以定位网站服务器。
2. **TCP/TLS握手**：建立连接后，进行TCP握手，并在HTTPS情况下执行TLS握手以确保安全的数据传输。
3. **HTTP请求响应周期**：请求完成后，服务器返回内容，涉及到编码和数据传输。
4. **HTML和CSS解析**：浏览器将HTML作为原始数据读入，转换为单独的字符和标记，构成DOM和CSSOM树。
5. **布局**与**绘画**：布局决定页面元素的确切位置和大小，绘画则将视觉表示渲染到屏幕上。CSS属性对页面元素的排列方式起着核心作用。

了解这些底层机制有助于开发性能更优的网站。文章详细介绍了浏览器渲染过程中的关键步骤，后者可以被进一步划分为 DNS、TCP/TLS、HTTP 请求/响应、DOM 创建、CSSOM 创建、生成渲染树、布局、绘画等几个阶段。
## Full Content
Title: Exploring the browser rendering process | Little Things

URL Source: https://abhisaha.com/blog/exploring-browser-rendering-process/

Markdown Content:
The browser’s rendering process is a complex orchestration of multiple threads, processes, and stages that transform raw HTML, CSS, and JavaScript into interactive pixels on our screen. While the rendering processes of the browser are nothing new and there is an abundance of information available on this topic, I thought it is interesting enough to write an interactive post on this. So essentially, our goal here is to understand what all happens in between these two points below:

1.  You type a URL in the browser and hit enter.
2.  The website is rendered on your screen.

I will be using the term `client`, `browser` and `server` throughout this post. Here, `browser` is a `client`. In this post’s context, they are the same thing. And the `server` refers to the web server hosting the website.

This post is best viewed on a larger screen due to interactive demos.

Navigation and Network
----------------------

The process starts when you type a URL in the browser’s address bar and hit enter. Let us assume we are trying to load `https://example.com`. The browser has no idea where to get the content of this website. It’s just a name that we humans can understand. The browser needs to convert this name into an IP address. This is where the DNS lookup comes into play.

DNS stands for Domain Name System. This system uses designated authoritative nameservers to map domain names to numerical IP addresses.

**DNS Lookup steps demo**

Press the green right arrow to start

The above demo visualizes the DNS lookup process, also called the query journey. A query journey involves each step required to convert the domain name you enter into an IP address. The query’s first stop is the recursive server, which then contacts a series of authoritative nameservers to translate the domain name into an IP address. Ultimately, the IP address for the requested domain is returned.

What are nameservers?

Name servers are specialized servers used to lookup IP addresses associated with domain names. You can find these name servers in the domain’s DNS records.

So now that we have the IP address, the browser can now establish a connection with the server hosting the website. This is done using the TCP handshake process.

TCP/TLS Handshake
-----------------

The TCP (Transmission Control Protocol) handshake is a three-step process used to establish a connection between a client and a server. It consists of a set of packets exchanged between the client and server to ensure a reliable connection. The three steps are:

*   SYN: The client sends a synchronization (SYN) packet to the server to initiate a connection.
*   SYN-ACK: The server responds with an acknowledgment (SYN-ACK) packet to the client.
*   ACK: The client sends an acknowledgment (ACK) back to the server to complete the handshake.

At this point, we only established a connection with the server. The next step is to secure this connection. Remember the `https` lock icon beside the URL? That defines a secure connection and is done using another handshake called TLS handshake which involves a few steps. But before we get into that, it will be easier if you can understand some terms related to TLS handshake.

**Cipher** - A cipher is an algorithm used to encrypt and decrypt data. It is used to secure data transmission over the internet.

**Certificate** - A certificate is a file that contains information about the website’s identity and public key. It is used as a digital signature to verify the website’s authenticity.

**Certificate Authority** (CA) - A Certificate Authority is a trusted entity that issues digital certificates to websites. It verifies the website’s identity and ensures the certificate’s authenticity.

**Public Key** - A public key is used to encrypt data before sending it over the internet. It is shared with the client to establish a secure connection.

**Private Key** - A private key is used to decrypt data received from the client. It is kept secret and not shared with anyone.

There are multiple steps in the TLS handshake process. I have grouped them into 4 main categories:

**Hello Messages:** The client sends a `ClientHello` message to initiate the handshake, and the server responds with a `ServerHello` message along with its digital certificate.

**Key Exchange:** The server may send key exchange information, and the client responds with its own key exchange message (and certificate if requested).

**Cipher Spec:** The client sends a `CipherSpec` message to switch to the negotiated encryption and follows it with a Finished message.

**Server Finalization:** The server replies with its own `CipherSpec` and Finished messages, completing the handshake and establishing a secure connection.

SSL, or Secure Sockets Layer, was the original security protocol developed for HTTP. SSL was replaced by TLS, or Transport Layer Security, some time ago. SSL handshakes are now called TLS handshakes, although the “SSL” name is still in wide use.

Let’s see this in action using the below demo.

**TCP/TLS Handshake demo**At this step in the process, no actual content or application data has been transmitted. The server has only acknowledged the connection and established a secure channel. The browser (client) handles all of these negotiation processes behind the scenes. Only after the TLS handshake is complete and both parties have exchanged their Finished messages, they can begin to send and receive encrypted content securely.

HTTP Request/Response Cycle
---------------------------

So now the browser requests the content of the website. The server processes this request and sends back a response. This is where the HTTP request/response cycle comes into play. While Backend Developers take care of the request, Frontend developers are more interested in the response part of this cycle. Watch the demo below to visualize this cycle.

**HTTP Request Flow**

request/response cycle with TTFB demo

We saw something called `TTFB` in the above demo. TTFB stands for Time To First Byte. It is the time taken by the server to send the first byte of data in response to the client’s request. It is an important metric for measuring server response time and website performance. A lower TTFB indicates faster server response times.

Good TTFB values are **0.8 seconds or less**, and poor values are **greater than 1.8 seconds**. The inbetween values comes under “needs improvement”.

As you can see in the demo, the response continues to load after the first byte is received. The server is still processing the request and sending the remaining data back to the client. From this point on, the browser begins to process the response.

Tokenization
------------

The browser will start to parse this HTML response. It reads the raw bytes of HTML and translates them to individual characters based on the specified encoding of the file, like `UTF-8`. Here’s an example of how bytes might look:

```
01001000 01010100 01001101 01001100
```

Each group of eight bits represents a byte, and each byte can be translated into a character, symbol, or instruction \>based on an encoding standard. For example:

For example, in UTF-8 encoding, the binary sequence for the letter **A is 01000001**. The letter **B is 01000010**

The browser converts strings of characters into distinct tokens and groups them, for example, `<html>`, `<body>` — and other strings within angle brackets. Each token is a meaningful unit that represents an HTML component.

**HTML Tokenization Demo**

### Start Tags

Opening elements like `<html>`, `<body>`

### End Tags

Closing elements like `</html>`, `</body>`

### Attributes

Element properties like `class="heading"`

### Text Content

The actual content between tags

Hover over any token to see how it relates to the document structure.

<html\>

lang="en-US"

<head\>

<style\>

.heading { ... }

</style\>

</head\>

<body\>

<h1\>

class="heading"

My Page

</h1\>

<p\>

A paragraph with a

<a\>

href="https://example.com/about"

link

</a\>

</p\>

</body\>

</html\>

DOM Tree Creation
-----------------

The DOM (Document Object Model) Tree is a hierarchical representation of the HTML document’s structure. It represents the elements as a tree of nodes. Each node represents an element, attribute, or text content in the document. Something like this:

**For reference**, this is the response we received. Primarily it has a H1 (heading) tag, a P (paragraph) tag, an A (anchor) tag, and CSS styles.

```
<html lang="en-US">
  <head>
    <style>
        .heading {
            color:#0099ff;
            font-size: 14px
        }
        p {
            margin: 0.5em 0;
        }
        a {
            color: #0099ff;
            text-decoration: underline;
        }
    </style>
  </head>
  <body>
    <h1 class="heading">My Page</h1>
    <p>A paragraph with a <a href="https://example.com/about">link</a></p>
  </body>
</html>
```
The DOM is a tree-like structure, so parent-child relationships can be displayed with ease.

**Dom Tree Creation**Every time the browser renders a webpage, it undergoes this multi-step process: parsing HTML bytes into characters, identifying tokens, converting them into nodes, and finally constructing the DOM tree. While the DOM tree defines the structure and relationships of HTML elements, it doesn’t dictate their visual appearance. That’s the role of the CSSOM.

CSSOM Tree Creation
-------------------

The CSS Object Model (CSSOM) is a representation of the CSS styles applied to the HTML document. It is similar to the DOM tree but represents the CSS styles instead of the HTML structure. The CSSOM is used to calculate the final styles for each element in the document. Check this demo to see how the CSSOM tree is created.

**CSSOM Tree Creation**The browser parses these styles into a streamlined, memory-efficient, and optimized data structure. This structure is designed to efficiently organize style rules, allowing fast retrieval and application of styles based on matching selectors.

Once the DOM and CSSOM are constructed, the browser can begin with the Render Tree creation.

Render Tree Creation
--------------------

The Render Tree is a combination of the DOM and CSSOM trees. It represents the visual structure of the page, including the layout and style information. The Render Tree is used to calculate the layout and paint the elements on the screen.

**Render Tree Creation**As you can see in the demo, the Render Tree is a combination of the DOM and CSSOM trees. It contains only the elements that will be displayed on the screen. It has computed styles and layout information for each element, allowing the browser to render the page accurately. And this brings us to the final stage of the rendering process - Layouting.

Layouting
---------

You might have heard about the term `layout` in the context of CSS. It is the process of calculating the exact position and size of each element on the page. The layout process involves determining the dimensions, margins, padding, borders, and positioning of each element based on the Render Tree. You may have seen elements on top of each other, for example, Modal windows, dropdowns, etc. This is where the layout process comes into play.

Even if the HTML markup is in order, the elements dont necessary appear in the order they are written because of the CSS properties that change the layout. Let’s see how these properties affect the layout.

**CSS properties that change layout**

HTML

```
<div class="container">
  <div class="item-1 bg-blue-500">
      Element 1
  </div>
  <div class="item-2 bg-green-500">
      Element 2
  </div>
  <div class="item-3 bg-red-500">
      Element 3
  </div>
</div>
```

CSS

```
.container {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
```

HTML is written in order and is not changed. But the layout changes when css properties change and the layouting process has to take care of this.

To explain this further, I have used added more properties like `position`, `display`, `top`, `left` and `z-index` of CSS. Play around with the settings and for each change, you can click the `Last Change` button to know about that change.

**Layouting Demo**

### Header

### Navigation

### Content

Quick reference for positioning modes:

*   **Static**: Follows the default document flow, positioned according to the natural structure of the HTML.
*   **Relative**: Positioned based on its original (normal) location, with adjustments made using `top`, `left`, `bottom`, or `right` properties.
*   **Absolute**: Positioned relative to the nearest positioned ancestor (one with a `position` value other than `static`). If no ancestor is positioned, it defaults to the document root.
*   **Fixed**: Positioned relative to the viewport, staying in place even when scrolling.

As you can see from the above demo, the flow of elements is influenced by their display types: block elements stack vertically, while inline elements flow horizontally. Positioning properties like static, relative, absolute, fixed, and sticky further dictate how elements are arranged in relation to one another. For instance, relative positioning offsets elements from their normal position without affecting the surrounding layout, while absolute positioning removes elements from the document flow entirely.

The outcome of the layout step is a precise plan for displaying each element, which is then followed by the painting step, where the visual representation is rendered on the screen.

Painting
--------

In the painting phase, the browser takes the structured layout information and draws each element onto the screen. This process fills in colors and applies images, borders, shadows, and other visual styles. The painting order is based on the stacking context, ensuring that elements are layered correctly according to the z-index and other properties.

**Painting Phase demo**

Click the nodes to see its computed style

TEXT"A paragraph with a "

The painting process is optimized to minimize the number of pixels that need to be redrawn. The browser uses techniques like layering, compositing, and caching to render the page efficiently.

Additional Reading
------------------

#### JavaScript’s Role

I didn’t talk about Javascript in this post. How the browser parses and optimizes Javascript is a completely different story. In summary, it can manipulate the DOM and CSSOM after the initial rendering, creating dynamic and interactive web experiences.

#### Browser Rendering Engines

Different browsers use different rendering engines, such as Blink (Chrome), WebKit (Safari), and Gecko (Firefox). These engines can have varying performance characteristics and compatibility levels. Some CSS features or JavaScript methods may be supported in one engine but not in others, or they may behave inconsistently. Also, different engines apply their default styles to HTML elements.

Summary
-------

There is a lot of action happening, so let me summarize the steps.

*   DNS Lookup: When a URL is entered, the browser performs a DNS lookup to convert the domain name into an IP address, allowing it to locate the website’s server.
    
*   TCP/TLS Handshake: The browser initiates a TCP handshake to establish a connection with the server. If the site is secure (HTTPS), a TLS handshake is also conducted to encrypt data transmission.
    
*   HTTP Request/Response Cycle: After establishing a connection, the browser sends an HTTP request for the website’s content, and the server responds with the necessary HTML, CSS, JavaScript, and other assets.
    
*   Tokenization: The browser reads the HTML response as raw data, converting it into individual characters and then tokens (e.g., `<html>`, `<body>`), which help the browser understand the document’s structure.
    
*   DOM Tree Creation: The browser builds the DOM (Document Object Model) tree, a hierarchical representation of the HTML document’s structure, with each node representing an element or text content.
    
*   CSSOM Tree Creation: The browser parses the CSS to create the CSSOM (CSS Object Model) tree, which represents the styles associated with the HTML document’s elements.
    
*   Render Tree Creation: The DOM and CSSOM trees combine to form the Render Tree, a visual representation of the page’s layout that includes only visible elements and their computed styles.
    
*   Layout: The browser calculates the exact size and position of each element on the screen, based on CSS properties like margins, padding, and positioning (e.g., static, absolute).
    
*   Painting: Using the Render Tree, the browser paints pixels onto the screen, filling in colors, images, borders, and shadows as defined by the CSS styles.
    

If you are a developer, understanding these underlying mechanisms can help you build faster, more efficient websites. While there are multiple more steps involved in between these steps, I have tried to cover the most important ones. Thats all for this post. Hope you enjoyed it.

References
----------

*   [Cloudflare DNS Lookup](https://www.cloudflare.com/learning/dns/glossary/dns-lookup/)
*   [Mozilla TCP Handshake](https://developer.mozilla.org/en-US/docs/Glossary/TCP_handshake)
*   [Cloudflare TLS Handshake](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)
*   [Mozilla HTTP Request/Response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages)
*   [HTML Spec on Rendering](https://html.spec.whatwg.org/multipage/rendering.html#rendering)

