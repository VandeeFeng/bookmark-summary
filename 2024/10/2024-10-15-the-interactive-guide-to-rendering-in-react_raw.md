Title: The Interactive Guide to Rendering in React

URL Source: https://ui.dev/why-react-renders

Markdown Content:
React, in its purest form, is a library for building user interfaces. It's so simple that the entire mental model can be represented as a formula, `v = f(s)` – where your view is simply a function of your state.

Diagram showing that view = function(state)tateunctioniewv\=fs)(

Though this equation gives us a simple mental model for how React works, there's one aspect of the equation that still, after all these years, seems to confuse people. Exactly _when_ and _how_ is `f` invoked? Or said differently, exactly _when_ and _how_ does React update the view?

Many blog posts, conference talks, and tweet threads have been dedicated to this seemingly simple topic. And yet, for some reason, it's still a topic that even experienced React developers have some (often unknown) misconceptions about.

To better answer this, instead of starting with _how_ or _when_, let's go back one step further and start from first principles. First, _what_ is **rendering**?

### What is rendering?

Put simply, rendering is just a fancy way of saying that React calls your ~function~ component with the intent of eventually updating the View.

When React renders a component, two things happen.

First, React creates a snapshot of your component which captures everything React needs to update the view at that particular moment in time. props, state, event handlers, and a description of the UI (based on those props and state) are all captured in this snapshot.

From there, React takes that description of the UI and uses it to update the View.

Animated diagram that shows React taking a snapshot of a component and then using the snapshot to update the viewCOMPONENTVIEWSNAPSHOT

In order to get the starting UI for your application, React will do an initial render, starting at the `root` of your application.

🦷

#### **createRoot**

When we say `root`, we literally mean `root`.

To create a `root`, you first get the HTML element you want to mount your React app to, pass that to React DOM's `createRoot` function, then call `root.render`, passing it a React element which React will use as the starting point to get the initial UI of your application.

import { createRoot } from "react-dom/client";

import App from "./App";

const rootElement \= document.getElementById("root");

const root \= createRoot(rootElement);

root.render(<App /\>);

Unless you're building a React app from scratch, this is usually done for you by whatever generates your app (e.g. `create-react-app`, `create-next-app`, Codesandbox, etc.).

Of course, this initial render is the most uninteresting one. Without the ability to re-render, React would be mostly useless. It's how React treats all subsequent renders that's what makes it more interesting.

That naturally leads us to our next question, _when_ exactly does React re-render a component?

Looking back to our `v = f(s)` equation, your intuition might be that `f` is invoked whenever `s` changes. That would make sense. We wouldn't want to recalculate the `View` unless the `State` had changed. In fact, it's as simple as that.

### When does React re-render?

React will only re-render when the state of a component changes

This may be surprising, but it's true. The only thing that can trigger a re-render of a component in React is a state change.

With that, we now have our final , _how_ does React actually know when the state of a component has changed? At this point it's fairly trivial and, once again, it has to do with our snapshot.

When an event handler is invoked, that event handler has access to the props and state as they were in the moment in time when the snapshot .

From there, if the event handler contains an invocation of `useState`'s updater function **and** React sees that the new state is different than the state in the snapshot, React will trigger a re-render of the component – creating a new snapshot and updating the view.

Interactive diagram showing an event handler updating the state, triggering a re-render of the component and updating the viewhandleToggleCOMPONENTVIEWSNAPSHOT

At this point, you have a high-level, theoretical mental model for how React renders, and then re-renders whenever state changes. That's nice, and it makes for some fun visuals, but like any mental model, it's only helpful in as much as it can withstand the stress test of reality.

Let's say we wanted a simple app that allowed a user to click a button and toggle different "greetings" – something like this.

To do this, we'll stick all our greetings in an array, and then we'll have a piece of state that keeps track of the index of the greeting we want to display.

We'll then have a `button` that when it's clicked, will either increment `index` or reset it back to `0` if we've reached the end of the array.

Now whenever our `button` is clicked, our `handleClick` event handler will run. The state (`index`) inside of `handleClick` will be the same as the state in the most recent snapshot. From there, React sees there's a call to `setIndex` and that the value passed to it is different than the state in the snapshot – triggering a re-render.

That's a lot of words. Here's what it would look like if we visualized it.

Interactive diagram showing an event handler updating the state, triggering a re-render of the component and updating the viewhandleClickCOMPONENTVIEWSNAPSHOT012HELLOHOLABONJOUR, TYLERNEXT GREETING

* * *

Let's look at another example (without the visuals now).

In this code, when the `button` is clicked, what gets alerted?

Don't trick yourself into thinking that all of a sudden things are now somehow different or more complex than they were prior to you seeing this example. The same rules apply.

We know that when our `handleClick` event handler runs, it has access to the props and state as they were in the moment in time when the snapshot was created – in that moment, `status` was `clean`. Therefore, when we alert `status`, we get `clean`.

Now click the `button` again. You'll notice that because our previous `button` click triggered a re-render and created a new snapshot with the `status` of `dirty`, on any clicks after the initial click we get `dirty`.

* * *

Let's try another one. What happens when we click the `button` in this example?

When the button is clicked, React runs our event handler and sees that we invoke an updater function inside of it. From there, it calculates the new state to be `0`. It then notices the new state, `0`, is the same as the state in the snapshot, `0`. Therefore, React does not trigger a re-render and the snapshot and View remain the same.

Again, React will only re-render if the event handler contains an invocation of `useState`'s updater function (✅) **and** React sees that the new state is different than the state in the snapshot (❌).

* * *

How about this one. What will `count` be after the `button` is clicked?

Again, we know that when our `handleClick` event handler runs, it has access to the props and state as they were in the moment in time when the snapshot was created – in that moment, `count` was `0`.

So eventually, once React is done calculating the new state, it'll see that the new state, `1`, is different than the state in the snapshot, `0`. From there, React will re-render the component, creating a new snapshot and updating the View.

Once you understand how rendering works, these kind of questions become trivial to walk through. But there is one question that may have come up after looking at the last example.

How many times will the `Counter` component re-render when the button is clicked?

Your intuition might be that React will re-render for every updater function it encounters, so 3 times in our example.

const handleClick \= () \=\> {

setCount(0 + 1)

setCount(0 + 1)

setCount(0 + 1)

}

Thankfully, that's not right since it would lead to a lot of unnecessary re-renders.

Instead, React will only re-render after it's taken into account every updater function inside of the event handler and it's sure what the final state is. So in our example, React will only re-render **once** per click.

🧑‍🏭

#### **Batching: How React Calculates State**

React only re-rendering once it's taken into account every updater function inside of the event handler implies that React has some sort of internal algorithm it uses to calculate the new state. React refers to this algorithm as "batching".

Thankfully, it's pretty straight forward.

Whenever React encounters multiple invocations of the same updater function (e.g. `setCount` in our example), it will keep track of each of them, but only the result of the last invocation will be used as the new state.

const handleClick \= () \=\> {

setCount(1)

setCount(2)

setCount(3)

}

So in this example, the new state will of course be `3`.

Now it's uncommon, but there is a way to tell React to use the value of the previous invocation of the updater function instead of replacing it. To do that, you pass the updater function a function itself that will take in the value from the most recent invocation as its argument.

const handleClick \= () \=\> {

setCount(1)

setCount(2)

setCount((c) \=\> c + 3)

}

In this example, `c` will be `2` since that's what was passed to the most recent invocation of `setCount` before our callback function ran. Therefore, the final state will be `2` + `3`, or `5`.

What about this one?

const handleClick \= () \=\> {

setCount(1)

setCount((c) \=\> c + 3)

setCount(7)

setCount((c) \=\> c + 10)

}

Let's walk through it.

The state will be `1`, then it will be `1` + `3`, or `4`, then it will be `7`, then it will be `7` + `10`, or `17`.

Notice that we don't use `4` in the third invocation even though that's what was returned in the second invocation. That's because we're just telling React to forget everything it knew and use `7` as the new state.

Another way to think about our code above is like this.

const handleClick \= () \=\> {

setCount((c) \=\> 1)

setCount((c) \=\> c + 3)

setCount((c) \=\> 7)

setCount((c) \=\> c + 10)

}

Where React just ignores the previous value unless you explicitly use it.

* * *

Are you having yet? Let's look at another example.

After clicking on our `button` 3 times, what will the UI show, what will be logged to the console, and how many times will App have re-rendered?

The first time the `button` is clicked, the UI will show `1, 2`, the console will show `{ linear: 0, exponential: 1 }`, and the `App` component will have re-rendered once.

The second time the `button` is clicked, the UI will show `2, 4`, the console will show `{ linear: 1, exponential: 2 }`, and the `App` component will have re-rendered twice.

And the third time the `button` is clicked, the UI will show `3, 8`, the console will show `{ linear: 2, exponential: 4 }`, and the `App` component will have re-rendered three times.

This example not only , but it also shows us another interesting aspect of how React re-renders. That is, React will only re-render **once** per event handler, even if that event handler contains updates for multiple pieces of state.

This is yet another example of how React will only re-render a component when it absolutely has to. With that in mind, let's take a look at another example that may surprise you.

* * *

Let's start with our `Greeting` code from earlier.

Now let's say we wanted to make our `Greeting` component a little more welcoming. To do that, we'll create and render a `Wave` component inside of `Greeting` that will add a 👋 emoji in the top right of the UI.

Very welcoming. Notice anything peculiar about how our app works, though? Before you play with it, try to guess _when_ our nested `Wave` component will re-render.

Your intuition is probably thinking **never**. After all, if React truly only re-renders when it absolutely has to, why would `Wave` ever re-render since it doesn't accept any props and has no state?

I've added a log to `Wave` so we can see when it renders. Go ahead and try it now.

Notice that `Wave` re-renders whenever we click the `button` (changing the `index` state inside of `Greeting`). This may not be intuitive, but it demonstrates an important aspect of React. Whenever state changes, React will re-render the component that owns that state **and** all of its child components – regardless of whether or not those child components accept any props.

Interactive diagram that shows a component’s state changing and React re-rendering it and all its child componentschange()update()update

I get this may seem like a strange default. Shouldn't React only re-render child components if their props change? Anything else seems like a waste.

First, React is _very_ good at rendering. If you have a performance problem, the reality is it's rarely because of .

Second, the assumption that React should only re-render child components if their props change works in a world where React components are _always_ pure functions and props are the only thing these components need to render. The problem, as anyone who has built a real world React app knows, is that isn't _always_ the case.

To be a pragmatic tool and not just a philosophical one we discuss in computer science courses, React provides some to break out of its normal `v = fn(s)` paradigm. We'll cover these later in the course, but know that we can't just assume a component should only re-render when its props change.

Third, if you do have an expensive component and you want that component to opt out of this default behavior and _only_ re-render when its props change, you can use React's `React.memo` higher-order component.

`React.memo` is a function that takes in a React component as an argument and returns a new component that will only re-render if its props change.

Now, regardless of how many times we click our `button`, `Wave` will only render once, on the initial render.

But again, even when dealing with child components, our mental model holds strong. Any time a React component renders, regardless of why or where it's located in the component tree, React creates a snapshot of the component which captures everything React needs to update the view at that particular moment in time. props, state, event handlers, and a description of the UI (based on those props and state) are all captured in this snapshot.

From there, React takes that description of the UI and uses it to update the View.

* * *

Now you may have heard of React's `StrictMode` component. It's React's way of saying "What if we took this really simple mental model and just totally blew it up?"

That's an exaggeration, but it does change things just a _little_ bit.

Whenever you have `StrictMode` enabled, React will re-render your components an extra time.

All our examples until this point have had strict mode **disabled**, for obvious reasons. But so you can see it in action, here's our `Wave` example now in `StrictMode`.

Notice that every time we click the button, our app renders **twice**.

This may seem strange, but `StrictMode` makes sure your app is resilient to re-renders and that your components are pure. If not, it'll become obvious when React renders the 2nd time.

Regardless of if React renders once or 100 times, because your view should be a function of your state, it shouldn't matter. `StrictMode` helps you make sure that's the case.

The way you enable `StrictMode` is by wrapping it around your `App` like this.

import { StrictMode } from 'react';

import { createRoot } from 'react-dom/client';

const root \= createRoot(

document.getElementById('root')

);

root.render(

<StrictMode\>

<App /\>

</StrictMode\>

);

Similar to creating your `root`, unless you're building a React app from scratch, this is usually done for you by whatever generates your app.

Now one last question you probably have, doesn't this have performance implications? Yes, but React will only respect `StrictMode` when you're in `development` mode. In `production`, it'll be ignored.

Now that you know about `StrictMode`, we'll include a toggle on every code preview that'll allow you to toggle it on and off.
