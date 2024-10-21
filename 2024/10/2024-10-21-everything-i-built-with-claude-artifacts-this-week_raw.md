Title: Everything I built with Claude Artifacts this week

URL Source: https://simonwillison.net/2024/Oct/21/claude-artifacts/

Markdown Content:
21st October 2024

I’m a huge fan of Claude’s **Artifacts** feature, which lets you prompt [Claude](https://claude.ai/) to create an interactive Single Page App (using HTML, CSS and JavaScript) and then view the result directly in the Claude interface, iterating on it further with the bot and then, if you like, copying out the resulting code.

I was digging around in my [Claude activity export](https://support.anthropic.com/en/articles/9450526-how-can-i-export-my-claude-ai-data) (I built a [claude-to-sqlite](https://github.com/simonw/claude-to-sqlite) tool to convert it to SQLite I could explore it in [Datasette](https://datasette.io/)) and decided to see how much I’d used artifacts [in the past week](https://github.com/simonw/claude-to-sqlite/issues/2#issuecomment-2425658909). It was more than I expected!

Being able to spin up a full interactive application—sometimes as an illustrative prototype, but often as something that directly solves a problem—is a remarkably useful tool.

Here’s most of what I’ve used Claude Artifacts for in the past seven days. I’ve provided prompts or a full transcript for nearly all of them.

*   [URL to Markdown with Jina Reader](https://simonwillison.net/2024/Oct/21/claude-artifacts/#url-to-markdown-with-jina-reader)
*   [SQLite in WASM demo](https://simonwillison.net/2024/Oct/21/claude-artifacts/#sqlite-in-wasm-demo)
*   [Extract URLs](https://simonwillison.net/2024/Oct/21/claude-artifacts/#extract-urls)
*   [Clipboard viewer](https://simonwillison.net/2024/Oct/21/claude-artifacts/#clipboard-viewer)
*   [Pyodide REPL](https://simonwillison.net/2024/Oct/21/claude-artifacts/#pyodide-repl)
*   [Photo Camera Settings Simulator](https://simonwillison.net/2024/Oct/21/claude-artifacts/#photo-camera-settings-simulator)
*   [LLM pricing calculator](https://simonwillison.net/2024/Oct/21/claude-artifacts/#llm-pricing-calculator)
*   [YAML to JSON converter](https://simonwillison.net/2024/Oct/21/claude-artifacts/#yaml-to-json-converter)
*   [OpenAI Audio](https://simonwillison.net/2024/Oct/21/claude-artifacts/#openai-audio)
*   [QR Code Decoder](https://simonwillison.net/2024/Oct/21/claude-artifacts/#qr-code-decoder)
*   [Image converter and downloader](https://simonwillison.net/2024/Oct/21/claude-artifacts/#image-converter-and-downloader)
*   [HTML Entity Escaper](https://simonwillison.net/2024/Oct/21/claude-artifacts/#html-entity-escaper)
*   [text-wrap-balance-nav](https://simonwillison.net/2024/Oct/21/claude-artifacts/#text-wrap-balance-nav)
*   [ARES Phonetic Alphabet Converter](https://simonwillison.net/2024/Oct/21/claude-artifacts/#ares-phonetic-alphabet-converter)
*   [This is so useful, and so much fun!](https://simonwillison.net/2024/Oct/21/claude-artifacts/#this-is-so-useful-and-so-much-fun-)

#### URL to Markdown with Jina Reader [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#url-to-markdown-with-jina-reader)

I got frustrated at how hard it was to copy and paste the entire text of a web page into an LLM while using Mobile Safari. So I built a simple web UI that lets me enter a URL, calls the [Jina Reader API](https://jina.ai/reader) to generate Markdown (which uses Puppeteer under the hood) and gives me that Markdown with a convenient “Copy” button.

Try it out: [https://tools.simonwillison.net/jina-reader](https://tools.simonwillison.net/jina-reader) ([Code](https://github.com/simonw/tools/blob/main/jina-reader.html))

![Image 1: Jina Reader - URL field, Markdown selected in a select box, Submit button. Then a box showing Markdown extracted from the page with a Copy to Clipboard button. Then a frame showing a preview of the rendered Markdown.](https://static.simonwillison.net/static/2024/claude-artifacts/jina-reader.jpg)

I wrote [more about that project here](https://simonwillison.net/2024/Oct/14/my-jina-reader-tool/?uu).

#### SQLite in WASM demo [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#sqlite-in-wasm-demo)

A Hacker News [conversation about SQLite’s WASM build](https://news.ycombinator.com/item?id=41851051#41851788) lead me to the [@sqlite.org/sqlite-wasm](https://www.npmjs.com/package/@sqlite.org/sqlite-wasm) package on NPM, and I decided to knock together a quick interactive demo.

![Image 2: Pelican Sightings in Half Moon Bay - a textarea with select * from pelican sightings, an execute query button and a table displaying 5 matching rows.](https://static.simonwillison.net/static/2024/claude-artifacts/sqlite-wasm.jpg)

Try it out here: [tools.simonwillison.net/sqlite-wasm](https://tools.simonwillison.net/sqlite-wasm)

[Code](https://github.com/simonw/tools/blob/main/sqlite-wasm.html), [Claude transcript](https://gist.github.com/simonw/677c3794051c4dfeac94e514a8e5b697)

I found myself wanting to extract all of the underlying URLs that were linked to from a chunk of text on a web page. I realized the fastest way to do that would be to spin up an artifact that could accept rich-text HTML pastes and use an HTML parser to extract those links.

![Image 3: Extract URLs tool. Content pasted. URLs extracted. Shows a list of extracted URLs.](https://static.simonwillison.net/static/2024/claude-artifacts/extract-urls.jpg)

[https://tools.simonwillison.net/extract-urls](https://tools.simonwillison.net/extract-urls)

[Code](https://github.com/simonw/tools/blob/main/extract-urls.html), [Claude transcript](https://gist.github.com/simonw/0a7d0ddeb0fdd63a844669475778ca06)

#### Clipboard viewer [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#clipboard-viewer)

Messing around with a tool that lets you paste in rich text reminded me that the browser clipboard API is a fascinating thing. I decided to build a quick debugging tool that would let me copy and paste different types of content (plain text, rich text, files, images etc) and see what information was available to me in the browser.

![Image 4: Clipboard format viewer. Paste here or anywhere on the page. Shows text/html with a fragment of HTML, text/plain with some text and Clipboard Event Information showing event type paste and formats available text/html and text/plain](https://static.simonwillison.net/static/2024/claude-artifacts/clipboard-viewer.jpg)

[https://tools.simonwillison.net/clipboard-viewer](https://tools.simonwillison.net/clipboard-viewer)

[Code](https://github.com/simonw/tools/blob/main/clipboard-viewer.html), [Claude transcript](https://gist.github.com/simonw/5393dd81fcabc9f854e8bbec205e7e1e)

#### Pyodide REPL [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#pyodide-repl)

I didn’t put a lot of effort into this one. While poking around with Claude Artifacts in the browser DevTools I spotted this CSP header:

`content-security-policy: default-src https://www.claudeusercontent.com; script-src 'unsafe-eval' 'unsafe-inline' https://www.claudeusercontent.com https://cdnjs.cloudflare.com https://cdn.jsdelivr.net/pyodide/; connect-src https://cdn.jsdelivr.net/pyodide/; worker-src https://www.claudeusercontent.com blob:; style-src 'unsafe-inline' https://www.claudeusercontent.com https://cdnjs.cloudflare.com https://fonts.googleapis.com; img-src blob: data: https://www.claudeusercontent.com; font-src data: https://www.claudeusercontent.com; object-src 'none'; base-uri https://www.claudeusercontent.com; form-action https://www.claudeusercontent.com; frame-ancestors https://www.claudeusercontent.com https://claude.ai https://preview.claude.ai https://claude.site https://feedback.anthropic.com; upgrade-insecure-requests; block-all-mixed-content`

The `https://cdn.jsdelivr.net/pyodide/` in there caught my eye, because it suggested that the Anthropic development team had deliberately set it up so [Pyodide](https://pyodide.org/)—Python compiled to WebAssembly—could be loaded in an artifact.

I got Claude to spin up a very quick demo to prove that this worked:

![Image 5: Pyodide Python REPL -   3 + 4 returns 7. A textarea to enter python code and a Run button.](https://static.simonwillison.net/static/2024/claude-artifacts/pyodide-repl.jpg)

[https://claude.site/artifacts/a3f85567-0afc-4854-b3d3-3746dd1a37f2](https://claude.site/artifacts/a3f85567-0afc-4854-b3d3-3746dd1a37f2)

I’ve not bothered to extract this one to my own `tools.simonwillison.net` site yet because it’s purely a proof of concept that Pyodide can load correctly in that environment.

#### Photo Camera Settings Simulator [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#photo-camera-settings-simulator)

I was out on a photo walk and got curious about whether or not JavaScript could provide a simulation of camera settings. I didn’t get very far with this one (prompting on my phone while walking along the beach)—the result was buggy and unimpressive and I quickly lost interest. It did expose me to the [Fabric.js](http://fabricjs.com/) library for manipulating canvas elements though.

![Image 6: Photo Camera Settings Simulator. An image has been selected - but only the corner of the image displays with some buggy broken resize handles. Three sliders at the bottom show Exposure, Contrast and SAturation.](https://static.simonwillison.net/static/2024/claude-artifacts/photo-settings.jpg)

[https://claude.site/artifacts/e645c231-8c13-4374-bb7d-271c8dd73825](https://claude.site/artifacts/e645c231-8c13-4374-bb7d-271c8dd73825)

#### LLM pricing calculator [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#llm-pricing-calculator)

This one I _did_ finish. I built this pricing calculator as part of my experiments with [Video scraping using Google Gemini](https://simonwillison.net/2024/Oct/17/video-scraping/), because I didn’t trust my own calculations for how inexpensive Gemini was! Here are [detailed notes](https://simonwillison.net/2024/Oct/17/video-scraping/#bonus-calculator) on how I built that.

![Image 7: Screenshot of LLM Pricing Calculator interface. Left panel: input fields for tokens and costs. Input Tokens: 11018, Output Tokens: empty, Cost per Million Input Tokens: $0.075, Cost per Million Output Tokens: $0.3. Total Cost calculated: $0.000826 or 0.0826 cents. Right panel: Presets for various models including Gemini, Claude, and GPT versions with their respective input/output costs per 1M tokens. Footer: Prices were correct as of 16th October 2024, they may have changed.](https://static.simonwillison.net/static/2024/llm-pricing-calculator.jpg)

[https://tools.simonwillison.net/llm-prices](https://tools.simonwillison.net/llm-prices)

#### YAML to JSON converter [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#yaml-to-json-converter)

I wanted to remind myself how certain aspects of YAML syntax worked, so I span up a quick YAML to JSON converter tool that shows the equivalent JSON live as you type YAML.

![Image 8: YAML to JSON converter. In the top textarea is YAML. Below it is pretty-printed JSON output.](https://static.simonwillison.net/static/2024/claude-artifacts/yaml-json.jpg)

[https://claude.site/artifacts/ffeb439c-fc95-428a-9224-434f5f968d51](https://claude.site/artifacts/ffeb439c-fc95-428a-9224-434f5f968d51)

#### OpenAI Audio [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#openai-audio)

This is my most interesting artifact of the week. I was exploring OpenAI’s new Audio APIs and decided to see if I could get Claude to build we a web page that could request access to my microphone, record a snippet of audio, then base64 encoded that and send it to the OpenAI API.

Here are [the full details on how I built this tool](https://simonwillison.net/2024/Oct/18/openai-audio/).

![Image 9: Screenshot of the OpenAI Audio tool. A start recording button is visible, and a 00:00 timer, and a playback audio element. There is a textarea for a prompt and a Submit to API button.](https://static.simonwillison.net/static/2024/openai-audio-card.jpg)

[https://tools.simonwillison.net/openai-audio](https://tools.simonwillison.net/openai-audio)

Claude Artifacts can’t make API requests to external hosts directly, but it can still spin up enough of a working version that it’s easy to take that, move it to different hosting and finish getting it working.

I wrote more about this API pattern in [Building a tool showing how Gemini Pro can return bounding boxes for objects in images](https://simonwillison.net/2024/Aug/26/gemini-bounding-box-visualization/).

#### QR Code Decoder [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#qr-code-decoder)

I was in a meeting earlier this week where one of the participants shared a slide with a QR code (for joining a live survey tool). I didn’t have my phone with me, so I needed a way to turn that QR code into a regular URL.

[https://tools.simonwillison.net/qr](https://tools.simonwillison.net/qr)

Knocking up this QR decoder in Claude Artifacts took just a few seconds:

> `Build an artifact (no react) that lets me paste in a QR code and displays the decoded information, with a hyperlink if necessary`

\[ ... \]

> `have a file open box that also lets you drag and drop and add a onpaste handler to the page that catches pasted images as well`

[Full conversation here](https://gist.github.com/simonw/c2b0c42cd1541d6ed6bfe5c17d638039).

#### Image converter and downloader [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#image-converter-and-downloader)

Another very quick prototype. On Hacker News someone demonstrated a neat idea for a tool that let you drop photos onto a page and it would bake them into the page as base64 URLs such that you could “save as HTML” and get a self-contained page with a gallery.

I [suggested they could add](https://news.ycombinator.com/item?id=41876750#41880857) a feature that generated a “Download link” with the new page baked in—useful on mobile phones that don’t let you “Save as HTML”—and got Claude to knock up a quick prototype:

![Image 10: Image converter and page downloader - I've selected an image and there is now a Download Page link below that image.](https://static.simonwillison.net/static/2024/claude-artifacts/image-converter-and-downloader.jpg)

In this case I shared the code in [a Gist](https://gist.github.com/egeozcan/b27e11a7e776972d18603222fa523ed4) and then used the new-to-me `https://gistpreview.github.io/?GIST_ID_GOES_HERE` trick to render the result:

[https://gistpreview.github.io/?14a2c3ef508839f26377707dbf5dd329](https://gistpreview.github.io/?14a2c3ef508839f26377707dbf5dd329)

[gistpreview](https://github.com/gistpreview/gistpreview.github.io) turns out to be a really quick way to turn a LLM-generated demo into a page people can view.

#### HTML Entity Escaper [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#html-entity-escaper)

Another example of on-demand software: I needed to escape the HTML entities in a chunk of text on my phone, so I got Claude to build me a tool for that:

![Image 11: HTML entity escaper. In the input box I have typed in text with some double quotes. The output box has those correctly escaped, and a copy to clipboard button.](https://static.simonwillison.net/static/2024/claude-artifacts/html-entities.jpg)

[https://claude.site/artifacts/46897436-e06e-4ccc-b8f4-3df90c47f9bc](https://claude.site/artifacts/46897436-e06e-4ccc-b8f4-3df90c47f9bc)

Here’s the prompt I used:

> `Build an artifact (no react) where I can paste text into a textarea and it will return that text with all HTML entities - single and double quotes and less than greater than ampersand - correctly escaped. The output should be in a textarea accompanied by a "Copy to clipboard" button which changes text to "Copied!" for 1.5s after you click it. Make it mobile friendly`

#### text-wrap-balance-nav [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#text-wrap-balance-nav)

Inspired by [Terence Eden](https://shkspr.mobi/blog/2024/10/you-can-use-text-wrap-balance-on-icons/) I decided to do a quick experiment with the `text-wrap: balance` CSS property. I got Claude to build me an example nav bar with a slider and a checkbox. I [wrote about that here](https://simonwillison.net/2024/Oct/20/you-can-use-text-wrap-balance-on-icons/).

![Image 12: Animated demo. A navigation menu with 13 items - things like Home and About and Services and a products. These are wrapped on four lines with 4, 4, 4 and then 1 item. Selecting the enable text-wrap: balances checkbox changes that to 3, 4, 3, 3 - a slider also allows the number of visible items to be changed to see the effect that has](https://static.simonwillison.net/static/2024/text-wrap-balance.gif)

[https://tools.simonwillison.net/text-wrap-balance-nav](https://tools.simonwillison.net/text-wrap-balance-nav)

#### ARES Phonetic Alphabet Converter [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#ares-phonetic-alphabet-converter)

I was volunteering as a HAM radio communications operator for [the Half Moon Bay Pumpkin Run](https://hmbpumpkinfest.com/featured-exhibits/great-pumpkin-run.html) and got nervous that I’d mess up using the phonetic alphabet—so I had Claude build me this tool:

![Image 13: ARES PHonetic Alphabet Converter. I have entered the text Cleo is a lobster. After clicking the Convert button I get the output Charlie Lima Echo Oscar (Space) India Sierra (Space) Alpha (Space) Lima Oscar Sierra Tango Echo Romeo](https://static.simonwillison.net/static/2024/claude-artifacts/phonetic-alphabet.jpg)

[https://claude.site/artifacts/aaadab20-968a-4291-8ce9-6435f6d53f4c](https://claude.site/artifacts/aaadab20-968a-4291-8ce9-6435f6d53f4c)

[Claude transcript here](https://gist.github.com/simonw/6ad4133c93e22df4c0ce731fdd7a2a91). Amusingly it built it in Python first, then switched to JavaScript after I reminded it that I wanted “an interactive web app”.

#### This is so useful, and so much fun! [#](https://simonwillison.net/2024/Oct/21/claude-artifacts/#this-is-so-useful-and-so-much-fun-)

As you can see, I’m a _heavy_ user of this feature—I just described 14 projects produced in a single week. I’ve been using artifacts since they were released [on 20th June](https://simonwillison.net/2024/Jun/20/claude-35-sonnet/) (alongside the excellent Claude 3.5 Sonnet, still my daily-driver LLM) and I’m now at a point where I fire up a new interactive artifact several times a day.

I’m using artifacts for idle curiosity, rapid prototyping, library research and to spin up tools that solve immediate problems.

Most of these tools took less than five minutes to build. A few of the more involved ones took longer than that, but even the OpenAI Audio one took [11:55am to 12:07pm](https://gist.github.com/simonw/0a4b826d6d32e4640d67c6319c7ec5ce) for the first version and [12:18pm to 12:27pm](https://gist.github.com/simonw/a04b844a5e8b01cecd28787ed375e738) for the second iteration—so 21 minutes total.

Take a look at my [claude-artifacts](https://simonwillison.net/tags/claude-artifacts/) tag for even more examples, including [SVG to JPG/PNG](https://simonwillison.net/2024/Oct/6/svg-to-jpg-png/), [Markdown and Math Live Renderer](https://simonwillison.net/2024/Sep/21/markdown-and-math-live-renderer/) and [Image resize and quality comparison](https://simonwillison.net/2024/Jul/26/image-resize-and-quality-comparison/).

I also have a [dashboard](https://simonwillison.net/2024/Oct/21/dashboard-tools/) of every post that links to my [tools.simonwillison.net](https://tools.simonwillison.net/) site, and the underlying [simonw/tools](https://github.com/simonw/tools) GitHub repo includes more unlisted tools, most of which link to their Claude conversation transcripts in their commit history.

I’m beginning to get a little frustrated at their limitations—in particular the way artifacts are unable to make API calls, submit forms or even link out to other pages. I’ll probably end up spinning up my own tiny artifacts alternative based on everything I’ve learned about them so far.

If you’re _not_ using artifacts, I hope I’ve given you a sense of why they’re one of my current favourite LLM-based tools.
