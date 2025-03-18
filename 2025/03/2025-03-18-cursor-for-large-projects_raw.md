Title: Cursor for Large Projects

URL Source: https://getstream.io/blog/cursor-ai-large-projects/

Published Time: 2025-03-05T11:58:26

Markdown Content:
With all this "vibe" coding, many devs think that [Cursor](https://www.cursor.com/) and [Claude](https://www.anthropic.com/news/introducing-claude) are just for prototypes. While Cursor is great at writing new code, it’s also very effective at structuring code, standardizing, refactoring, and maintaining large projects. It’s super exciting since you can build software 5-30x faster.

This guide shares my workflow for Cursor and how to use it for large projects. For context, here at Stream, we power [chat](https://getstream.io/chat/), [activity feeds](https://getstream.io/activity-feeds/), and [video](https://getstream.io/video/) for over a billion end users. ~800k lines of Go code.

Engineering jobs are not going away anytime soon. In fact, we’re hiring faster than ever before—[Golang engineers/lead/staff/director](https://jobs.ashbyhq.com/stream/69536de0-6349-4394-a1a0-ea2ec0ede945?utm_source=Yv9pv9nvqM) in Amsterdam/Boulder/remote.

Cursor – Edit, Test Loop
------------------------

The key to [effective AI usage](https://getstream.io/chat/solutions/ai-integration/) is a good edit and test loop. You typically want the AI to write the code, write the test, and then execute this test while fixing any bugs it finds. Only after the AI has completed these steps do I typically start to review.

Let’s go over the basics of this edit loop.

### Step 1 - Cursor Setup/Agent mode

You want to use the Agent mode (cmd + I) + Claude 3.7 sonnet. (note the little dropdown bottom left). The agent mode will continuously call Claude until the goal has been achieved. So, it will search files, look up more context, run tests, install packages, etc.

![Image 1](https://stream-blog-v2.imgix.net/blog/wp-content/uploads/d40148d7a174bb048d9439ecd99cc610/image7.png?auto=format&auto=compress)

### Step 2 - Docs for AI

The example above is a bit simplified. Typically, you want a docs folder teaching the AI best practices for the common tasks you do on your codebase. For instance

*   How do I write a test?
*   How do I set up a new database model and apply migrations?
*   How do I create a new controller/ state layer etc?

We keep a separate docs folder for AI. It looks something like this.

![Image 2](https://stream-blog-v2.imgix.net/blog/wp-content/uploads/69ce0c6d6d06ed344d71b47c3fbb209b/image3.png?auto=format&auto=compress)It’s pretty similar to how you would train your engineering team. But we keep separate AI docs so it’s easy to course-correct AI when it gets something wrong.

### Step 3 - Enable Yolo mode in the settings

You want to enable Yolo mode so Cursor can run tests without asking for confirmation. Optionally you can allow only the commands you frequently use for running tests, etc.

![Image 3](https://stream-blog-v2.imgix.net/blog/wp-content/uploads/cba8b6092266e8f4a171ff3215b6f6ee/image2.png?auto=format&auto=compress)

### Step 4 - Cursor/Claude runs the test (This is the key part)

This is the key part. You want to tell Cursor to run the test. Because it’s running the test, it will detect mistakes it made while generating the code.

![Image 4](https://stream-blog-v2.imgix.net/blog/wp-content/uploads/2be0b14b1258afa43926e64445ce4d27/image5.png?auto=format&auto=compress)Of course, AI isn’t perfect; it will miss some things, but with this testing loop, the results are far better than just generating code.

### For frontend/ other platforms

I’m using Cursor primarily for Golang. But you can set up a system similar to front-end development. Check out [BrowserTools](https://browsertools.agentdesk.ai/installation) by [@tedx\_ai](https://x.com/tedx_ai) for screenshots and console integrations. You can find more MCP options here: [https://cursor.directory/mcp](https://cursor.directory/mcp). I haven’t seen good MCP options yet for Android, Swift, Flutter, and React Native development.

Cursor - Project Files
----------------------

The edit/test loop is the key to effective cursor usage. Another important workflow is creating project files.

### Project Steps

Here’s an example of a project file for creating message Bookmarking/reminders

![Image 5](https://stream-blog-v2.imgix.net/blog/wp-content/uploads/ea475ee66b467b94217be9dec226f765/image4.png?auto=format&auto=compress)Note how each step references the relevant docs. You could also do this with cursor rules, but I prefer to specify the right doc most of the time manually.

### Project Validation Check

Now when you have this project file. You can also use AI to check your spec for issues. Our project-check file will review the models to see if the instructions clarify the primary key. For controller steps, it will ask you to clarify the desired permissions. So you can use AI to validate the instructions to the AI, which is kinda crazy. 🙂

### Generating Project Files

Of course you can also use AI to generate your project description. You give it an example project description file and ask it to generate something similar for a different feature. Grok is probably the best model for this at the moment. You can combine it with deepsearch to further clarify your project needs as well.

**Integrate LLMs fast!** Our UI components are perfect for any [AI chatbot interface](https://getstream.io/chat/solutions/ai-integration/) right out of the box. Try them today and launch tomorrow!

### Git is Your Checkpoint - Rinse & Repeat

Cursor has a built-in checkpoint system but I prefer not to use it. Git works better for me. To reset your workspace you can use:

```
git stash --include-untracked # stash all changes including things that are not tracked  
git stash pop # recover the last stash  
git clean -fd # remove all files that are not committed (careful with this one)
```

So, if Claude goes off the tracks, simply reset and try again. This is also why you keep a project file. It makes it very easy to start again with different docs/ best practices etc.

Other Cursor & Claude tips
--------------------------

When working with Cursor we learned that taking specific steps and applying certain tips dramatically improves the quality of the output generated by Cursor.

### Limit the steps in a Cursor Composer Window

Sometimes, I’ll run 5-7 steps in a single composer window. The longer you keep the conversation going the more likely Claude will forget part of the instructions. So create a new cursor agent window at times.

### Cursor Setup Tips

*   In the Cursor settings, you can add docs. This is particularly useful for less frequently used packages, which Claude by default doesn’t know much about
*   MCP integration with linear or other tools is pretty cool
*   / add open files to context is very convenient

![Image 6](https://stream-blog-v2.imgix.net/blog/wp-content/uploads/a8eb576487a7dcb4f1199b82c58bb227/image1.png?auto=format&auto=compress)

### Goland

Cursor is amazing for its AI features. I run Goland side by side for debugging, refactoring, and general editor design. You will probably also need to do that for things like iOS/Android development, etc., where an editor with strong tooling is hard/impossible to fully replace.

### Cursor Tools

There is a cool cursor tools project [https://github.com/eastlondoner/cursor-tools](https://github.com/eastlondoner/cursor-tools) by @EastlondonDev. Cursor tools enables browser usage, large context windows, docs, and planning capabilities.

### Cursor Rules

You can add rules to Cursor in the settings, which enables you to automatically include docs. As an example:

![Image 7](https://stream-blog-v2.imgix.net/blog/wp-content/uploads/c71790442657dcd41d599e7e6ed5d2d3/image6.png?auto=format&auto=compress)There is a directory of [common cursor rules.](https://cursor.directory/)

### Code Standardisation

It feels almost human because if you use confusing names, duplicate implementations, etc., AI will get confused. So, you want to have clean, standardized code to have the highest success rate with AI.

### Check Everything

If you assign work to a junior engineer, you would double-check everything. You should treat AI similarly and know what every bit of the code does.

Refactoring, Docs & Search
--------------------------

It's not just code generation. You can also use Cursor & Claude for docs, search and refactoring.

### Refactoring Example

You can make complex adjustments, to hundreds of files at once. If it's a simple change I still prefer Goland's refactoring tools. But for complex changes this can save days of work.  
![Image 8](https://stream-blog-v2.imgix.net/blog/wp-content/uploads/f9696d4b86d688c4fdb004bde69dc124/image2.png?auto=compress%2Cformat&fit=scale&h=289&ixlib=php-3.3.0&w=1024&wpsize=large)

### Search & Docs

Every large codebase eventually has parts that are hard to understand. You can ask Cursor to write docs for you to help explain it.  
![Image 9](https://stream-blog-v2.imgix.net/blog/wp-content/uploads/7fdbf4a003cf9fa4b111c1ecf8fd9feb/image1.png?auto=compress%2Cformat&fit=scale&h=282&ixlib=php-3.3.0&w=1024&wpsize=large)

### Tech & Understanding

When you run into some part of the codebase where you don't understand the underlying tech, you also can use it as an alternative to Google/Stackoverflow  
![Image 10](https://stream-blog-v2.imgix.net/blog/wp-content/uploads/a1338cbec5bdfc74418572fd5a5eec08/image3.png?auto=compress%2Cformat&fit=scale&h=282&ixlib=php-3.3.0&w=1024&wpsize=large)

Conclusion
----------

Cursor is an amazing tool not just for prototypes but also for maintaining large projects. To use it effectively:

*   Setup a generate/ test/ run test cycle. So the AI self-corrects
*   Create a project plan and have the AI check and improve this plan
*   Finetune your Cursor setup and get used to the different workflow
*   It's not just code generation. You can refactor, create docs and use it as a powerful search engine

With the right setup, you can work 5-30 times faster. I especially love that, as an engineer, you can focus more on the harder problems while the AI generates all the basics. I hope this guide helps. If you have more tips, share them [with Stream on X](https://x.com/getstream_io), and I’ll add them to the article.

P.S.—We’re hiring for Go engineers. ([Staff/Lead/Director Golang, Amsterdam/Boulder/Skopje/Remote](https://jobs.ashbyhq.com/stream/69536de0-6349-4394-a1a0-ea2ec0ede945?utm_source=Yv9pv9nvqM))
