Title: Collecting replies to tweets using JavaScript

URL Source: https://til.simonwillison.net/twitter/collecting-replies

Markdown Content:
I ran [a survey](https://twitter.com/simonw/status/1843290729260703801) on Twitter the other day to try and figure out what people mean when they use the term "agents" with respect to AI.

It ended up getting over 200 replies... and then I realized that Twitter no longer shows replies to logged-out users, and the Twitter API now charges for read-access to tweets.

I figured out a trick for extracting the replies to a tweet using the browser console. It works by scraping the DOM for the tweets that are visible on the page, using the handy `data-testid` attributes that Twitter presumably uses for test automation.

Since Twitter implements infinite scrolling the script runs every 500ms to see if new tweets have appeared, de-duplicating them based on the `href` of the tweet.

So paste this script into a page, scroll down until you reach the end of the replies and then run `copy(window.tweets)` to copy the resulting JSON to the clipboard.

Here's [example output](https://gist.github.com/simonw/bdc7b894eedcfd54f0a2422ea8feaa80) in JSON format - each tweet looks like this:

{
  "datetime": "2024-10-07T14:02:11.000Z",
  "username": "simonw",
  "tweet": "Let’s see if we can crowdsource a robust definition of “agent” (with respect to AI and LLMs) that fits in a <\=280 character tweet\\n\\nReply to this with your best attempt, then scroll through the replies and fave the ones that makes sense to you",
  "href": "https://twitter.com/simonw/status/1843290729260703801",
  "likes": 524,
  "impressions": 0,
  "retweets": 71
}

(That impressions number is wrong because the script doesn't work against the large tweet at the top of the page, I haven't bothered to fix that.)

The script
----------

window.tweets \= window.tweets || \[\];
let seenHrefs \= new Set();

function extractNumber(el, selector) {
  const element \= el.querySelector(selector);
  if (element && element.getAttribute) {
    const match \= element.getAttribute("aria-label").match(/(\\d+)/);
    return match ? parseInt(match\[0\], 10) : 0;
  }
  return 0;
}

function collectTweets() {
  // Ditch any <span\>…</span\> elements
  document.querySelectorAll("span").forEach((span) \=\> span.textContent.trim() \=== "…" && span.remove());
  Array.from(document.querySelectorAll("\[data-testid=tweet\]"), (el) \=\> {
    const datetime \= el.querySelector("time")?.dateTime || "";
    const username \= el.querySelector('\[data-testid="User-Name"\] a')?.href.split("/").slice(\-1)\[0\] || "";
    const tweet \= el.querySelector('\[data-testid="tweetText"\]')?.innerText || "";
    const href \= el.querySelector("time")?.closest("a")?.href || "";
    const likes \= extractNumber(el, '\[data-testid="like"\]');
    const impressions \= extractNumber(el, '\[aria-label\*="View post analytics"\]');
    const retweets \= extractNumber(el, '\[aria-label\*="Repost"\]');
    return { datetime, username, tweet, href, likes, impressions, retweets };
  }).forEach((tweetObj) \=\> {
    // Filter out tweets with previously seen hrefs and add new ones to window.tweets
    if (!seenHrefs.has(tweetObj.href)) {
      seenHrefs.add(tweetObj.href);
      window.tweets.push(tweetObj);
    }
  });
}

setInterval(collectTweets, 500);

// Run copy(window.tweets) later to copy collected tweets to the clipboard

I built this with a bit of help from Claude - [transcript here](https://gist.github.com/simonw/49eb5c7128d44151e5851b79cc488baa).

Feeding those to an LLM
-----------------------

I fed the collected tweets to an LLM (Google's [gemini-exp-1206](https://simonwillison.net/2024/Dec/6/gemini-exp-1206/)) and asked it this question:

> `Group these into a set of definitions that illustrate the various different shapes of definition. For each of your definitions include quotes of the tweets that support that definition. Answer in markdown`

I used this command:

curl 'https://gist.githubusercontent.com/simonw/bdc7b894eedcfd54f0a2422ea8feaa80/raw/9a76a9a33d16b8c5a8c036e0d92c2cb9bf83267c/tweets.json' | \\
  llm -m gemini-exp-1206 -s 'Group these into a set of definitions that illustrate the various different shapes of definition. For each of your definitions include quotes of the tweets that support that definition. Answer in markdown'

Here's the response I got: [https://gist.github.com/simonw/beaa5f90133b30724c5cc1c4008d0654](https://gist.github.com/simonw/beaa5f90133b30724c5cc1c4008d0654)

Created 2024-10-08T20:29:51-07:00, updated 2024-12-10T18:22:50-08:00 · [History](https://github.com/simonw/til/commits/main/twitter/collecting-replies.md) · [Edit](https://github.com/simonw/til/blob/main/twitter/collecting-replies.md)
