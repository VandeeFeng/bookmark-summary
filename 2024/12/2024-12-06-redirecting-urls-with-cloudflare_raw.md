Title: Redirecting URLs with CloudFlare

URL Source: https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/

Markdown Content:
![Image 9: Christian Kjær in a casual setting :)](https://codethoughts.io/images/me-casual.jpg)

Christian Kjær

3 min read

·

31\. July 2024

·

[cloudflare](https://codethoughts.io/tags/cloudflare/)

I recently moved my blog from [https://codetalk.io](https://codetalk.io/) (now my commercial site) to [https://codethoughts.io](https://codethoughts.io/). This of course also meant, that everything linking to my old blog was now broken, which is not the best experience for any readers that I might have 😅

Initially I considered setting up rewrite rules somewhere for each individual post, but then thought of a much smarter way, using CloudFlare’s _Redirect Rules_, to instead redirect all direct links to posts and throw them to the new location on codethoughts.io.

The documentation for these rules are a bit sparse, so I thought I’d share how I did. First though, let’s set some context:

*   The base domain changed from [https://codetalk.io](https://codetalk.io/) —\> [https://codethoughts.io](https://codethoughts.io/)
*   All posts live under the `/posts/` path on the domain
*   All post slugs are identical in dates and names
*   We no longer have a `.html` ending on the new blog (i.e. what previously might have been `https://codetalk.io/posts/a-blog-post.html` would now be `https://codetalk.io/posts/a-blog-post/`)
*   We’re on the free CloudFlare plan, so there’s a limit to which expressions we can use

Let’s take a look at how we do this:

*   [Catching our requests on codetalk.io](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/#catching-our-requests-on-codetalk-io)
*   [Redirecting to the new location](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/#redirecting-to-the-new-location)

[Catching our requests on codetalk.io](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/#catching-our-requests-on-codetalk-io)
-------------------------------------------------------------------------------------------------------------------------------------------------------

First, we’ll navigate to the relevant place in CloudFlare

*   Go into the CloudFlare dashboard
*   Select your domain (e.g. codetalk.io)
*   Expand Rules in the sidebar
*   Select Redirect Rules
*   Create a new rule
*   Give it an appropriate name, and make sure to select _Custom filter expression._

In my case here, I specifically want to limit the logic to when the `URI Path` starts with the value `/posts`. CloudFlare will neatly demonstrate that this rule will generate the expression:

```
(starts_with(http.request.uri.path, "/posts"))
```

In the Dashboard console it will look something like this:

[![Image 10: The Redirect Rules entry for catching incoming requests](https://codethoughts.io/processed_images/Screenshot_2024-07-08_at_16.18.43.543fca2cd79242e5.png)](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/Screenshot_2024-07-08_at_16.18.43.png)

The Redirect Rules entry for catching incoming requests

The Redirect Rules entry for catching incoming requests

[Redirecting to the new location](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/#redirecting-to-the-new-location)
---------------------------------------------------------------------------------------------------------------------------------------------

Now that we have caught the relevant incoming requests, let’s transform the old format into our new format.

We want to do a dynamic redirect to the new location, in the new format which is lowercase and without any `.html` at the end.

Let’s set up a redirect rule of type `Dynamic`, give it a status code of HTTP 301 (i.e. "Moved Permanently”) and use the following expression:

```
concat("https://codethoughts.io", substring(lower(http.request.uri.path), 0,-5))
```

Breaking this down from inner-to-outer, what we are doing:

*   Grab the `http.request.uri.path` part of the request (e.g. `/posts/a-blog-post.html` of `https://codetalk.io/posts/a-blog-post.html`)
*   Lowercase the value (e.g. `/posts/A-Blog-Post.html` becomes `/posts/a-blog-post.html`)
*   Remove the last 5 characters by taking the `substring` from the start, `0`, to 5 characters back from the last character, `-5` (e.g. `/posts/a-blog-post.html` becomes `/posts/a-blog-post`)
*   Finally, concatenate our new and rewritten URI path together with the new domain using `concat` (e.g. `/posts/a-blog-post` becomes `https://codethoughts.io/posts/a-blog-post`)

We’re avoiding any complex rewrite expressions, such as regex, because it’s a) not actually needed and b) not available on the free plan.

In the Dashboard console it will look something like this:

[![Image 11: The Redirect Rules entry for dynamically redirecting the incoming requests](https://codethoughts.io/processed_images/Screenshot_2024-07-08_at_16.17.27.82877b6820694331.png)](https://codethoughts.io/posts/2024-07-31-redirecting-urls-with-cloudflare/Screenshot_2024-07-08_at_16.17.27.png)

The Redirect Rules entry for dynamically redirecting the incoming requests

The Redirect Rules entry for dynamically redirecting the incoming requests

Hope that helps if you’re ever running into the same!

👉 [Let me know what you think over on Medium](https://codethoughts.medium.com/redirecting-urls-with-cloudflare-91a8f85cefdd) or in the comments below 👇
