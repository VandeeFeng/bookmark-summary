Title: Writing an LLM from scratch, part 8 -- trainable self-attention

URL Source: https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention

Published Time: 2025-03-04T21:30:00+0000

Markdown Content:
Archives

Categories

Blogroll

This is the eighth post in my trek through [Sebastian Raschka](https://sebastianraschka.com/)'s book "[Build a Large Language Model (from Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)". I'm blogging about bits that grab my interest, and things I had to rack my brains over, as a way to get things straight in my own head -- and perhaps to help anyone else that is working through it too. It's been almost a month since my [last update](https://www.gilesthomas.com/2025/02/llm-from-scratch-7-coding-self-attention-part-2) -- and if you were suspecting that I was [blogging about blogging](https://www.gilesthomas.com/2025/02/blogging-in-the-age-of-ai) and spending time getting [LaTeX working on this site](https://www.gilesthomas.com/2025/02/adding-maths-to-the-blog) as procrastination because this next section was always going to be a hard one, then you were 100% right! The good news is that -- as so often happens with these things -- it turned out to not be all that tough when I really got down to it. Momentum regained.

> If you found this blog through the blogging-about-blogging, welcome! Those posts were not all that typical, though, and I hope you'll enjoy this return to my normal form.

This time I'm covering section 3.4, "Implementing self-attention with trainable weights". How do we create a system that can learn how to interpret how much attention to pay to words in a sentence, when looking at other words -- for example, that learns that in "the fat cat sat on the mat", when you're looking at "cat", the word "fat" is important, but when you're looking at "mat", "fat" doesn't matter as much?

Before diving into that, especially given the amount of time since the last post, let's start with the 1,000-foot view of how the GPT-type decoder-only transformer-based LLMs (hereafter "LLMs" to save me from RSI) work. For each step I've linked to the posts where I went throught the details.

*   You start off with a string, presumably of words. ([Part 2](https://www.gilesthomas.com/2024/12/llm-from-scratch-2))
*   You split it up into tokens (words like "the", or chunks like "semi"). ([Part 2](https://www.gilesthomas.com/2024/12/llm-from-scratch-2))
*   The job of the LLM is to predict the next token, given all of the tokens in the string so far. ([Part 1](https://www.gilesthomas.com/2024/12/llm-from-scratch-1))
*   Step 1: map the tokens to a sequence of vectors called _token embeddings_. A particular token, say, "the", will have a specific embedding -- these start out random but the LLM works out useful embeddings as it's trained. ([Part 3](https://www.gilesthomas.com/2024/12/llm-from-scratch-3))
*   Step 2: generate another sequence of _position embeddings_ -- vectors of the same size as the token embeddings, also starting random but trained, that represent "this is the first token", "this is the second token", and so on. ([Part 3](https://www.gilesthomas.com/2024/12/llm-from-scratch-3). [1](https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention#fn-1))
*   Step 3: add the two sequences to generate a new sequence of _input embeddings_. The first input embedding is the first token embedding plus the first position embedding (added element-wise), the second is the second token embedding plus the second position embedding, and so on. ([Part 3](https://www.gilesthomas.com/2024/12/llm-from-scratch-3))
*   Step 4: self-attention. Take the input embeddings and for each one, generate a list of _attention scores_. These are numbers that represent how much attention to pay to each other token when considering the token in question. So (assuming one token per word) in "the fat cat sat on the mat", the token "cat" would need a list of 7 attention scores -- how much attention to pay to the first "the", how much to pay to "fat", how much to pay to itself, "cat", how much to pay to "sat", and so on. Exactly how it does that is what this section of the book covers -- up until now we've been using a "toy" example calculation. ([Part 4](https://www.gilesthomas.com/2024/12/llm-from-scratch-4), [Part 5](https://www.gilesthomas.com/2025/01/llm-from-scratch-5-self-attention), [Part 6](https://www.gilesthomas.com/2025/01/llm-from-scratch-6-coding-self-attention-part-1), [Part 7](https://www.gilesthomas.com/2025/02/llm-from-scratch-7-coding-self-attention-part-2)).
*   Step 5: normalise the attention scores to _attention weights_. We want each token's list of attention weights to add up to one -- we do this by running each list through the [softmax](https://en.wikipedia.org/wiki/Softmax_function) function. ([Part 4](https://www.gilesthomas.com/2024/12/llm-from-scratch-4), [Part 5](https://www.gilesthomas.com/2025/01/llm-from-scratch-5-self-attention), [Part 6](https://www.gilesthomas.com/2025/01/llm-from-scratch-6-coding-self-attention-part-1), [Part 7](https://www.gilesthomas.com/2025/02/llm-from-scratch-7-coding-self-attention-part-2)).
*   Step 6: generate a new sequence of _context vectors_. In the system that we've built so far, this contains, for each token, the sum of multiplying all of the input embeddings by their respective attention weights and adding the results together. So in that example above, the context vector for "cat" would be the input embedding for the first "the" times "cat"'s attention score for that "the", plus the input embedding for "fat" times "cat"'s attention score for "fat", and so on for every other token in the sequence. ([Part 4](https://www.gilesthomas.com/2024/12/llm-from-scratch-4), [Part 5](https://www.gilesthomas.com/2025/01/llm-from-scratch-5-self-attention), [Part 6](https://www.gilesthomas.com/2025/01/llm-from-scratch-6-coding-self-attention-part-1), [Part 7](https://www.gilesthomas.com/2025/02/llm-from-scratch-7-coding-self-attention-part-2)).

After all of this is done, we have a sequence of context vectors, each of which should in some way represent the meaning of its respective token in the input, including those bits of meaning it gets from all of the other tokens. So the context vector for "cat" will include some hint of its fatness, for example.

What happens with those context vectors that allows the LLM to use them to predict what the next token might be? That bit is still to be explained, so we'll have to wait and see. But the first thing to learn is how we create a trainable attention mechanism that can take the input vectors and generate the attention scores so that we can work out those context vectors in the first place.

The answer Raschka gives in this section is called _scaled dot product attention_. He gives a crystal-clear runthrough of the code to do it, but I had to bang my head against it for a weekend to get to a solid mental model. So, instead of going through the section bit-by-bit, I'll present my own explanation of how it works -- to save me from future head-banging when trying to remember it, and perhaps to save other people's foreheads from the same fate.

### The summary, ahead of time

I'm a [long-time fan](https://www.gilesthomas.com/2011/10/teaching-programming) of the Pimsleur style of language course, where they start each tutorial with minute or so of conversation in the language you're trying to learn, then say "in 30 minutes, you'll hear that again and you'll understand it". You go through the lession, they play the conversation again, and you do indeed understand it.

So here is a compressed summary of how self-attention works, in my own words, based on Raschka's explanation. It might look like a wall of jargon now, but (hopefully) by the time you've finished reading this blog post, you'll be able to re-read it and it will all make sense.

We have an input sequence of length n, of tokens. We have converted it to a sequence of input embeddings, each of which is a vector of length d -- each of these can be treated as a point in d\-dimensional space. Let's represent that sequence of embeddings with values like this: x1,x2,x3,...xn. Our goal is to produce a sequence of length n made up of context vectors, each of which represents the the meaning of the respective input token in the context of the input as a whole. These context vectors will each be of length c (which in practice is often equal to d, but could in theory be of any length).

We define three matrices, the _query weights matrix_ Wq, the _key weights matrix_ Wk, and the _value weights matrix_ Wv. These are made up of trainable weights; each one of them is sized d×c. Because of those dimensions, we can treat them as operations that project a vector of length d -- a point in d\-dimensonal space -- to a vector of length c -- a point in a c\-dimensional space. We will call these projected spaces _key space_, _query space_ and _value space_. To convert an input vector xm into query space, for example, we just multiply it by Wq, like this qm\=xmWq.

When we are considering input xm, we want to work out its _attention weights_ for every input in the sequence (including itself). The first step is to work out the _attention score_, which, when considering another input xp, is calculated by taking the dot product of the projection of xm into query space, and the projection of xp into key space. Doing this across all inputs provides us with an attention score for every other token for xm. We then divide these by the square root of the dimensionality of the spaces we are projecting into, c, and run the resulting list through the softmax function to make them all add up to one. This list is the attention weights for xm. This process is called _scaled dot product attention_.

The next step is to generate a context vector for xm. This is simply the sum of the projections of all of the inputs into the value space, each one multiplied by its associated attention weight.

By performing these operations for each of the input vectors, we can generate a list of length n made up of context vectors of length c, each of which represents the meaning of a input token in the context of the input as a whole.

Importantly, with clever use of matrix multiplication, all of this can be done for all inputs in the sequence, producing a context vector for every one of them, with just five matrix multiplications and a transpose.

### Now let's explain it

First things first, if there's anyone there that understood all of that without already knowing how attention mechanisms work, then I salute you! It was pretty dense, and I hope it didn't read like my friend Jonathan's [parody of incomprehensible guides to using git](https://www.tartley.com/posts/a-guide-to-git-using-spatial-analogies/). For me, it took eight re-reads of Raschka's (emininently clear and readable) explanation to get to a level where I felt I understood it. I think it's also worth noting that it's very much a "mechanistic" explanation -- it says how we do these calculations without saying why. I think that the "why" is actually out of scope for this book, but it's something that fascinates me, and I'll blog about it soon. But, in order to understand the "why", I think we need to have a solid grounding in the "how", so let's dig into that for this post.

Up until this section of the book, we have been working out the attention scores by taking the dot product of the input embeddings against each other -- that is, when you're looking at xm, the attention score for xp is just xm·xp. I suspected earlier that the reason that Raschka was using that specific operation for his "toy" self-attention was that the real implementation is similar, and that has turned out right, as we're doing scaled dot products here. But what we do is adjust them first -- xm, the one that we're considering, is multiplied by the query weights matrix Wq first, and the other one xp is multiplied by the key weights matrix Wk. Raschka refers to this as a projection, which for me is a really nice way to look at it. But his reference is just in passing, and for me it needed a bit more digging in.

### Matrices as projections between spaces

> If your matrix maths is a bit rusty -- like mine was -- and you haven't read the [primer I posted the other week](https://www.gilesthomas.com/2025/02/basic-neural-network-matrix-maths-part-1), then you might want to check it out now.

From your schooldays, you might remember that matrices can be used to apply geometric transformations. For example, if you take a vector representing a point, you can multiply it by a matrix to rotate that point about the origin. You can use a matrix like this to rotate things anti-clockwise by θ degrees:

\[xy\]\[cosθ−sinθsinθcosθ\]\=\[x.cosθ+y.sinθx.−sinθ+y.cosθ\]This being matrix multiplication, you could add on more points -- that is, if the first matrix had more rows, each of which was a point you wanted to rotate, the same multiplication would rotate them all by θ. So you can see that matrix as being a function that maps sets of points to their rotated equivalents. This works in higher dimensions, too -- a 2×2 matrix like this can represent transformations in 2 dimensions, but, for example, in 3d graphics, people use 3×3 matrices to do similar transformations to the points that make up 3d objects. [2](https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention#fn-2)

An alternative way of looking at this 2×2 matrix is that it's a function that projects points from one 2-dimensional space to another, the target space being the first space rotated by θ degrees anti-clockwise. For a simple 2d example like this, or even the 3d ones, that's not necessarily a better way of seeing it. It's a philosophical difference rather than a practical one.

But imagine if the matrix wasn't square -- that is, it had a different number of rows to the number of columns. If you had a 3×2 matrix, it could be used to multiply a matrix of vectors in 3d space and produce a matrix in 2d space. Remember the rule for matrix multiplication: a n×3 matrix times a 3×2 matrix will give you a n×2 one.

That is actually super-useful; if you've done any 3d graphics, you might remember the [frustum](https://en.wikipedia.org/wiki/Viewing_frustum) matrix which is used to convert the 3d points you're working with to 2d points on a screen. Without going into too much detail, it allows you to project those 3d points into a 2d space with a single matrix multiplication.

So: a d×c matrix can be seen as a way to project a vector that represents a point in d\-dimensional space into one that represents one in a different c\-dimensional space.

What we're doing in self-attention is taking our d\-dimensional vectors that make up the input embedding sequence, then projecting them into three different c\-dimensional spaces, and working with the projected versions. Why do we do this? That's the question I want to look into in my future post on the "why", but for now, I think one thing that is fairly clear is that because these projections are learned as part of the training (remember, the three matrices we're using for the projections are made up of trainable weights), it's putting some kind of indirection into the mix that the simple dot product attention that we were using before didn't have.

### How to do the dot products of the projected input embeddings

Sticking with this mechanistic view -- "how" rather than "why" -- for now, let's look at the calculations and how matrix multiplication makes them efficient. I'm going to loosely follow Raschka's explanation, but using mathematical notation rather than code, as (unusually for me as a career techie) I found it a bit easier to grasp what's going on that way.

We'll stick with the case where we're considering token xm and trying to work out its attention score for xp. The first thing we do is project xm into query space, which we do by multiplying it by the query weights matrix Wq:

qm\=xmWqNow, let's project xp into key space by multiplying it by the key weights matrix Wk:

kp\=xpWkOur attention score is defined as being the dot product of these two vectors:

ωm,p\=qm.kpSo we could write a simple loop that iterated over all of the inputs x1...xn once, generating the projections into query space for each one, and then inside that loop iterated over x1...xn a second time, projecting them into key space, doing the dot products, and storing those as attention scores.

But that would be wasteful! We're doing matrix multiplications, so we can batch things up. Let's consider the projections of the inputs into the key space first; those will always be the same, each time around our hypothetical loop. So we can do them in one shot. Let's treat our input sequence as a matrix X like this:

\[x1(1)x1(2)x1(3)x2(1)x2(2)x2(3)...xn(1)xn(2)xn(3)\]We have a row for every input embedding in our input sequence x1, x2, and so on, with the row being made up of the elements in that embedding. So it has n rows, one per element in the input sequence, and d columns, one for each dimension in the input embeddings, so it's n×d. (I'm using d\=3 as an example here, like Raschka does in the book.)

That's just like our matrix of points in the rotation matrix example above, so we can project it into key space in one go, just by multiplying it by Wk. Let's call the result of that K:

K\=XWkIt will look like this (again, like Raschka, I'm using a 2-dimensional key space -- that is, c\=2 -- so that it's easy to see whether a matrix is in the original 3d input embedding space or a 2d projected one):

\[k1(1)k1(2)k2(1)k2(2)...kn(1)k2(2)\]...where each of those rows is the projection of the input xn to key space. It's just all of the projections stacked on top of each other.

Now, let's think about that dot product -- this bit from earlier:

ωm,p\=qm.kpWe now have a matrix K containing all of our kn values. When you're doing a matrix multiplication, the value of Mi,j -- that is, the element at row i, column j in the output matrix -- is the dot product of row i in the first matrix, taken as a vector, with column j in the second matrix, also considered as a vector.

It sounds like we can make use of that to do all of our dot products in a batch. Let's treat qm, our projection of the mth input token into query space, as a single-row matrix. Can we multiply the key matrix by it, like this

qmK...?

Unfortunately not. qm is a one-row matrix (size 1×c) and K is our n×c key matrix. With matrix multiplication, the number of columns in the first matrix -- c in this case -- needs to match the number of rows in the second, which is n. But, if we transpose K, essentially swapping rows for columns:

qmKT...then we have a 1×c matrix times a c×n one, which does make sense -- and, even better, it's every dot product for every pair of (qm, kp) for all values of p -- that is, with two matrix multiplications -- the one to work out K and this one, and a transpose, we've worked out all of the attention scores for element xm in our input sequence.

But it gets better!

First, let's do the same thing as we did to project the input sequence into key space to project it all into query space as well. We calculated K\=XWk to work out the key matrix, so we can work out the query matrix the same way, Q\=XWq. Just like K was all of the input vectors projected into key space, "stacked" on top of each other, Q is all of the input vectors projected into query space.

Now, what happens if we multiply that by the transposed key matrix?

QKTWell, our Q matrix is one row per input, one column per dimension in our projected space, so it's n×c. And, as we know, the transposed K matrix is c×n. So our result is n×n -- and because matrix multiplication is defined in terms of dot products, what it contains is the dot product of every row in Q -- the inputs transformed into query space -- against every column in KT -- the inputs transformed into key space.

The plan was to generate attention scores by working out exactly those dot products!

So with three matrix multiplications, we've done that:

Q\=XWq K\=XWk Ω\=QKT...where I'm using the capital Ω to represent a matrix where each row represents an input in the sequence, and each column within the row represents an attention weight for that input. The element Ωm,p represents how much attention to pay to the input xp when you are trying to work out the context vector for xm. And it has done that by working out the dot product of xm projected into query space and xp projected into key space.

That's the "dot product" part of "scaled dot product attention" done and dusted :-)

### Normalising it

So we've worked out our attention scores. The next thing we need to do is normalise them; in the past we used the softmax function. This function takes a list and adjusts the values in it so that they all sum up to 1, but gives a boost to higher numbers and a deboost to smaller ones. I imagine it's named "soft" "max" because it's like finding the maximum, but in a sense softer because it's leaving the other smaller numbers in there deboosted.

Raschka explains that when we're working with large numbers of dimensions -- in real-world LLMs, d and c can easily be in the thousands -- using pure softmax can lead to small gradients -- he says that it can start acting "like a step function", which I read as meaning that you wind up with all but the largest number in the list being scaled to really tiny numbers and the largest one dominating. So, as a workaround, we divide the numbers by the square root of the number of dimensions in our projected space c, and then only then do we run the result through softmax. [3](https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention#fn-3)

Remember that Ω is a matrix of attention scores, with one row for each input token, so we need to apply the softmax function to each row separately. Here's what we wind up with:

A\=softmax(Ωc, axis\=1)(The axis\=1 isn't really proper mathematical notation, it's just something I've borrowed from PyTorch to say that we're applying softmax to a matrix on a per-row basis.)

Once we've done that, we have our normalised attention scores -- that is, the attention weights. The next, and final, step, is to use those to work out the context vectors.

### Creating the context vectors

Let's reiterate how we're working out the context vectors. In the previous toy example, for each token, we took the input embeddings, multiplied each one by its attention weight, summed the results element-wise, and that was the result. Now we're doing the same thing, but projecting the input embeddings into another space first -- the value space. So let's start off by doing that projection as a simple matrix multiplication, just like we did for the other spaces:

V\=XWvNow, from above we have our attention weights matrix A, which has in row m the attention weights for every token in the input sequence for input xm -- that is, at Am,p we have the attention weight for input p when we're working out the context vector for input m. That means that for our input sequence of length n, it's an n×n matrix.

In our value matrix V, we also have one row per input. The values in row m, treated as a vector, are the projection of the input xm into value space. So it's an n×c matrix.

What happens if we do the matrix multiplication

AV...? We'll get a n×c matrix of some kind, by the rules of matrix multiplication, but what will it mean?

To reiterate, the rule for matrix multiplication is that the value of Mi,j -- that is, the element at row i, column j in the output matrix -- is the dot product of row i in the first matrix, taken as a vector, with column j in the second matrix, also considered as a vector.

So, at position (1,1) -- first row, first column, we have the dot product of the first row in A -- the attention weight for every token in the input sequence when we're considering the first token -- and the first column in V, which is the first element of each input embedding, projected into the value space. So, that is the first element of each input embedding times the attention weights for the first token. Or, in other words, it's the first element of the context vector for the first token!

At position (1,2) -- first row, second column -- we'll have the same calculation, but for the second element of each input embedding. That is the second element of the context vector for the first token.

...and so on for the rest of the columns. By the end of the first row, we'll have something that (treated as a vector) is the sum of all of the input embeddings, multiplied by the weights for the first input. It's our context vector for that input!

The same, of course, repeats for each row. The result of that single matrix multiplication is a matrix where the row m is the context vector for input xm.

We're done!

### Bringing it all together

Let's put together those steps. We start with our input matrix X, which is the input embeddings we generated earlier for our sequence of tokens of length n. Each row is an embedding, and there are d columns, where d is the dimensionality of our embeddings.

We also have our weight matrices to map input embeddings into different spaces: the _query weights matrix_ Wq, the _key weights matrix_ Wk, and the _value weights matrix_ Wv.

So, we project our input matrix into those spaces with three matrix multiplications:

Q\=XWq K\=XWk V\=XWv...to get our query matrix, our key matrix, and our value matrix.

We then calculate our attention scores with one further matrix multiplication and a transpose to work out the dot products:

Ω\=QKTWe normalise those to attention weights by scaling them by the square root of c and then applying softmax:

A\=softmax(Ωc, axis\=1)...and then we use one final matrix multiplication to use that to work out the context vectors:

C\=AVAnd that's our self-attention mechanism :-)

Now, if you [go back to the explanation at the start](https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention#the-summary-ahead-of-time), then hopefully it will make sense.

### Back to the book

Section 3.4 in the book works through the above with PyTorch code, and comes out with a nice simple `nn.Module` subclass that does exactly those matrix operations. This is then improved -- the first version uses generic `nn.Parameter` objects for the three weight matrices, and the second uses `nn.Linear` for more effective training. That side of it was reasonably easy to understand. And so, we've wrapped up what I think is the hardest part of "Build a Large Language Model (from scratch)": implementing self-attention with trainable weights.

### Next steps

The remainder of chapter 3 is much easier now that we're over this hump. We'll be going through two things:

*   Causal self-attention (which means that when we are looking at a given token, we don't pay any attention to later ones, just like we humans do when reading -- our language is structured so that you don't normally need to read forward to understand what a word means \[except [in German](https://faculty.georgetown.edu/jod/texts/twain.german.html) ;-\]).
*   Multi-head attention (which isn't as complex an issue as I thought it was when I first read about it).

So I think I'll probably blog about those first, and then circle back to the "why" of this form of self-attention. It's pretty amazing that we can do all of this -- projecting into differently-dimensioned spaces, taking dot products between every token's input embeddings in those spaces, and weighting the projected input tokens by the weights we generate -- with just five matrix multiplications. But why do we do that specifically?

The names of the matrices used -- query, key and value -- hint at the roles they play in a metaphorical way; Raschka says in a sidebar that it's a nod to information retrieval systems like databases. However, it's different enough to how DBs actually work that I can't quite make the connection. I'm sure it will come with time, though.

I also want to, probably in a separate post, consider what batches do to all of this. With [normal neural networks](https://www.gilesthomas.com/2025/02/basic-neural-network-matrix-maths-part-1), all of our activations when considering a given input are single-row or -column matrices (depending on the ordering of our equations). Extending to batches just means moving to normal multi-row, multi-column matrices.

But ever since we introduced the matrix of attention scores [for the first time](https://www.gilesthomas.com/2025/01/llm-from-scratch-6-coding-self-attention-part-1), it's been clear that even with a single input sequence going through our LLM, we're already using full matrices. How do we handle batches where we're processing multiple input sequences in parallel? It seems that we're going to need to use some kind of higher-order tensors -- if scalars are order zero tensors, vectors are order one tensors, and matrices are order two tensors, we're going to need to start considering order three tensors at least. That will require a bit of thought!

But for now, that's all -- see you next time! And please do comment below -- any thoughts, questions or suggestions would be very welcome, of course, but even if you just found this post useful it would be great to know :-)
