Title: How to build a real-time image generator with Flux and Together AI

URL Source: https://www.together.ai/blog/how-to-build-a-real-time-image-generator-with-together-ai

Markdown Content:
[BlinkShot](https://www.blinkshot.io/) is an app that generates images from text in real-time. It’s built using Together’s [new Turbo endpoint](https://www.together.ai/blog/flux-api-is-now-available-on-together-ai-new-pro-free-access-to-flux-schnell) for the FLUX.1 \[schnell\] model from Black Forest Labs.

![Image 1](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67097a84ed693764053c9181_67097967947cd6cd61691b96_astronaut-blinkshot.webp)

blinkshot.io example

In this post, you’ll learn how to build the core parts of BlinkShot. The app is [open-source](https://github.com/Nutlope/blinkshot) and built with Next.js, Shadcn, and React Query, but Together’s API can be used with any language or framework.

Building the prompt input
-------------------------

BlinkShot’s core interaction is a text area where the user can enter their prompt:

![Image 2](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67097c782b70f5e02681e90d_67097c469c34f243d2ac5303_Image%2520from%2520Notion.png)

In our page, we’ll render a textarea and control it using some new React state:

```
function Page() {
  let [prompt, setPrompt] = useState(''); 

  return (
    <textarea
      value={prompt}
      onChange={(e) => setPrompt(e.target.value)}
      placeholder="Describe your image..."
    />
  );
}
```

‍

Because FLUX on Together is so fast, instead of having a submit button, we can generate images in real-time as the user types.

To pull this off, we’ll bring in `useQuery` from React Query, and use the `queryKey` prop so it fires off a new API request every time our `prompt` state changes:

```
function Page() {
  const [prompt, setPrompt] = useState('');

  const { data } = useQuery({
    queryKey: [prompt], // re-fire whenever prompt changes
    queryFn: async () => {
      let res = await fetch('/api/generateImage', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });
      let json = await res.json();

      return json;
    },
    enabled: !!prompt.trim(),
    staleTime: Infinity,
    retry: false,
  });

  // `data` will contain the generated image
}
```

‍

If we open the network tab start typing in the text area, we’ll see our React app firing a request after each keystroke:

![Image 3](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/67097de8ea2ce0573a461e67_67097dc8575c7f7b887562c5_Image%2520(1).webp)

Our frontend is ready! Next, let’s add an API route to generate the image.

Generating an image in an API route
-----------------------------------

To create our API route, we’ll make a new `app/api/generateImage/route.js` file:

```
// app/api/generateImage/route.js
export async function POST(req) {
  let json = await req.json();

  console.log(json.prompt);
}
```

‍

If we open our terminal and enter some text, we’ll see the user’s prompt logged in our server console. We’re ready to send it to Together to generate an image!

Let’s install Together’s node SDK:

`npm i together-ai`

and use together.images.create to generate an image with FLUX \[schnell\]:

```
// app/api/generateImage/route.js
import Together from "together-ai";

let together = new Together();

export async function POST(req) {
  let json = await req.json();

  let response = await together.images.create({
    prompt: json.prompt,
    model: "black-forest-labs/FLUX.1-schnell",
    width: 1024,
    height: 768,
    steps: 3,
    response_format: "base64",
  });

  return Response.json(response.data[0]);
}
```

‍

We’re passing “base64” as the `response_format`  which our React app will be able to display without us having to store the image anywhere.

Let’s update our React code to display the Base64 image using a [Data URL](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data):

```
function Page() {
  const [prompt, setPrompt] = useState('');

  const { data } = useQuery({
    queryKey: [prompt],
    queryFn: async () => {
      let res = await fetch('/api/generateImage', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });
      let json = await res.json();

      return json;
    },
    enabled: !!prompt.trim(),
    staleTime: Infinity,
    retry: false,
  });

  return (
    <>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Describe your image..."
      />
	    
      {/* Render the generated image */}
      {data && (
        <img src={`data:image/png;base64,${data.b64_json}`} />
      )}
    </>
  );
}
```

‍

Now if we enter a prompt, we’ll see an image appear!

![Image 4](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/670982b116787929ba3c1737_6709814e9e02a8f91c6bbc7d_cat.webp)

If you keep typing, the image will update in real-time using the latest prompt. React Query takes care of discarding stale prompt values, making it a great fit for this use-case.

Debouncing our API requests
---------------------------

Currently our React app fires a new API request for every single character. This causes the UI to show images immediately, even if the user hasn’t finished their prompt.

Let’s debounce the API request so that it only fires once the user has paused typing for 300 milliseconds.

The `@uidotdev/usehooks` library has a `useDebounce` hook, so let’s install the package:

`npm i @uidotdev/usehooks`

and update our code to use debouncedPrompt as the queryKey:

```
function Page() {
  const [prompt, setPrompt] = useState("");
  const debouncedPrompt = useDebounce(prompt, 300); // debounce by 300ms

  const { data } = useQuery({
    queryKey: [debouncedPrompt], // update the queryKey
    queryFn: async () => {
      let res = await fetch("/api/generateImages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });
      let json = await res.json();

      return json;
    },
    enabled: !!debouncedPrompt.trim(), // ...and enabled
    staleTime: Infinity,
    retry: false,
  });

  return (
    <>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Describe your image..."
      />

      {data && <img src={`data:image/png;base64,${data.b64_json}`} />}
    </>
  );
}
```

‍

Now our app only generates a new image once our user has paused typing, which makes for a more pleasant UX.

Refining the image
------------------

The `steps` option of `images.create` controls the number of generation steps:

```
let response = await together.images.create({
	prompt: json.prompt,
  model: "black-forest-labs/FLUX.1-schnell",
  width: 1024,
  height: 768,
  steps: 3, // number of generation steps
  response_format: "base64",
});
```

‍

The more steps you use, the higher quality the generated image will be, but the longer it will take to generate.

Here are some examples of the same image created with 1, 2, or 3 generation steps.

An airplane:

![Image 5](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/670982b116787929ba3c1720_67098236dce655f30ec7dbaa_1.webp)

Praying hands:

![Image 6](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/670982b116787929ba3c171d_67098242ea2ce0573a4a9a0d_2.webp)

A businessman:

![Image 7](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/670982b116787929ba3c1719_670982520442b15a6ea0a2ac_3.webp)

Someone dunking a basketball:

![Image 8](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/670982b116787929ba3c1723_6709826696f78026704950b8_4.webp)

In BlinkShot, we found 3 steps to be a good compromise of quality and speed.

Building off of prior images with seed
--------------------------------------

The `images.create` command also has a `seed` option, which can be used for deterministic image generations:

```
let response = await together.images.create({
  prompt: json.prompt,
  model: "black-forest-labs/FLUX.1-schnell",
  width: 1024,
  height: 768,
  steps: 3,
  response_format: "base64",
  seed: 123 // reproduce a generation for a given prompt
});
```

‍

By default it’s random, but if you pass in a fixed number, the same prompt will regenerate the same image for that number.

BlinkShot uses seed for its Consistency mode. By specifying a fixed seed, later generated images more closely resemble earlier ones.

As an example, let’s take these three prompts:

*   “a horse”
*   “a horse that’s black”
*   “a horse that’s black with a rider”

Here’s what we get when we generate images from them with no seed:

![Image 9](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/6709835d2f072da30d2f58a3_6709833130716b8d86bdafb8_11.webp)

And here’s what we get if we generate images using a seed of 123:

![Image 10](https://cdn.prod.website-files.com/650c3b59079d92475f37b68f/6709835d2f072da30d2f588a_67098340e061575553582629_12.webp)

As you can see, the images build off of each other when there’s a consistent seed.

Going beyond BlinkShot
----------------------

The speed FLUX \[schnell\] is incredibly exciting — being able to generate images instantaneously unlocks a whole new class of web apps.

BlinkShot is open-source, so [check out the code](https://github.com/Nutlope/blinkshot) to learn more and get inspired to build your own real-time image apps.

When you’re ready to start generating high-quality images in your own apps, [sign up for Together AI](https://api.together.ai/) today, get $5 for free to start out, and make your first query in minutes!
