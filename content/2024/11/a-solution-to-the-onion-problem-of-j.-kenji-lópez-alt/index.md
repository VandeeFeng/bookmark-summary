---
title: A solution to the Onion Problem of J. Kenji López-Alt
date: 2024-11-27
extra:
  source: https://medium.com/@drspoulsen/a-solution-to-the-onion-problem-of-j-kenji-l%C3%B3pez-alt-c3c4ab22e67c
  original_title: A solution to the Onion Problem of J. Kenji López-Alt
---
## Summary
**摘要**：
这篇文章围绕着如何通过更高效的切片方法减少切割洋葱时产生的碎末，提出了创新解决方案，并与数学中的波朗数 (Golden Ratio) 相关联。作者Dylan Poulsen 发现了一种简化该问题的办法，将其转化为连续数学领域中的问题，即在无限层动画中寻找最佳切割深度。研究过程涉及从实线坐标系到极坐标的转换、利用雅可比矩阵来量化每个部分体积的均匀程度，并最终发现了一种与波朗数无关的最优切割方式。

**要点总结**：
1. **问题起源**：文章以前列出了洋葱切割问题的引入，提出了如何在保证尽可能一致的切片同时减少废料的目标，这起始于切洋葱的朋友之间的数学讨论。
2. **简化问题**：作者将洋葱切割问题转化为连续数学中的极限问题，探索了无限层数的洋葱，并通过该思路找到了解决方案的核心。
3. **雅可比矩阵应用**：运用雅可比矩阵在不同坐标系统下的应用，作者分析了洋葱各个微小部分体积的均匀度，进而计算出优化切片位置的数学公式。
4. **创新切割深度**：文章最后指出了最优切割深度的位置，它位于中心点下方一个比例值下的深度，作者通过迭代计算出精确数值为约为55.73%的洋葱半径长度。
5. **解析与结论**：通过深入解析切割深度与洋葱层次的数量及最佳切割点位置的关系，作者不仅揭示了优化切片方法的理由，还指出这种方法自然且容易实施，为日常厨师提供了实用建议，同时展示了数学在日常问题解决中的潜在应用价值。
## Full Content
Title: A solution to the Onion Problem of J. Kenji López-Alt

URL Source: https://medium.com/@drspoulsen/a-solution-to-the-onion-problem-of-j-kenji-l%C3%B3pez-alt-c3c4ab22e67c

Published Time: 2021-11-14T03:06:28.668Z

Markdown Content:
[![Image 60: Dylan Poulsen](https://miro.medium.com/v2/resize:fill:44:44/1*AD1NwhAxmaukG2e7vrKUIg.jpeg)](https://medium.com/@drspoulsen?source=post_page---byline--c3c4ab22e67c--------------------------------)

Note: this post has a lot of background information, much like every recipe you find online. To see the solution, jump to the end of the post.

I first became interested in the the problem of cutting onions in a way to reduce the variance of the volumes of the slices at a gathering with friends. One of my friends and colleagues, Dr. Gabe Feinberg, also a mathematician, pointed me to the Youtube video below.

The origin of the onion problem.

In the video, Chef Kenji López-Alt says he has a friend who is a mathematician, who claims that you should cut radially towards a point 60% of the radius below the center of the onion, and claims that this is related to the reciprocal of golden ratio, 0.61803398875…

I was intrigued by this, and even began cutting onions at home with this technique, just because it made me happy.

![Image 61: A picture of an onion cut according to the optimal strategy, along with a text message from the author saying that he has been cutting onions this way ever since his conversation with Gabe.](https://miro.medium.com/v2/resize:fit:700/1*njf0KQvZwF_qK3ZNQfTDhw.png)

A post in the Washington College Mathematics and Computer Science Department Discord where I show the results of cutting onions in this manner.

Each time I cut an onion for dinner, my mind would wander. I would think about why this is true, and what techniques I could use to approach the problem. While this was meditative for me, these musings did not lead anywhere substantial over the span of two months.

Last weekend, my thoughts actually lead me towards a solution. Within two days I had found the “true onion constant”, which, spoiler alert, is not the reciprocal of the golden ratio. The depth to which you have to aim your knife for radial cuts depends on the number of layers. You can see this by thinking of how to cut an onion with one layer versus an onion with ten layers to keep the pieces as similar as possible. For one layer you would aim towards the center of the onion, but for ten layers you would aim somewhere below the center of the onion. To simplify matters, I therefore thought of an onion with infinitely many layers (or, as Gabe called it, “the great onion in the sky,” which I love). These kind of abstractions are common in mathematics, and make problems tractable. Once there are infinitely many layers, it makes sense to think of infinitely many cuts. This moves the problem into the realm of continuous mathematics, where calculus can be used to great effect.

![Image 62: Text Transcript. Dylan: I’m starting to envision a proof of this by taking the limit as the number of cuts goes to infinity, and looking at the infinitesimal volumes. Sort of like Jacobians. I’d really like to see if 1/phi comes out as the “true” best depth to cut towards. Gabe: Maybe there’s some other onion constant.](https://miro.medium.com/v2/resize:fit:700/1*SUG-DyIR3UdYhqVqd7ZZ8w.png)

![Image 63: Text transcript. Dylan:The constant might also be a function of the number of layers. The true onion constant would then be in the limit as the number of layers goes to infinity… Gabe: Ah the great onion in the sky. Dylan reacts to Gabe’s comment with the joy emoji.](https://miro.medium.com/v2/resize:fit:700/1*GZ_8IAHFRsj0VcEZ78l63w.png)

More discussion from the Departmental Discord about the problem. There is also proof that I’m a millennial with the use of the 😂 emoji.

Here’s the technical part of the post. You probably need to know multivariable calculus to follow from here. I’m going to switch to using “we” instead of “I” to match mathematical writing conventions, and to indicate that we (you, dear reader, and I) are walking down this mathematical path together.

First, we model the onion as half of a disc of radius one, with its center at the origin and existing entirely in the first two quadrants in a rectangular (Cartesian) coordinate system. This ignores a dimension, and perhaps also some geometry of actual onions (are cross sections actually circles?) but makes the problem tractable and is still a good approximation.

The insight that leads to a solution comes from the Jacobian. When we change from rectangular coordinates to polar coordinates in integration, small rectangular pieces of area _dx dy_ are transformed into small pieces of area _r dr dθ_, where _x = r_ cos_(θ)_ and _y = r_ sin_(θ)_. The idea of the Jacobian applies to all changes in coordinate systems. We can calculate the Jacobian as

![Image 64: Formula for the Jacobian.](https://miro.medium.com/v2/resize:fit:700/1*X3M2-8-MmpR1cAJuA2u-Nw.png)

Below is a diagram showing the change of coordinates and the Jacobian in this setting.

![Image 65](https://miro.medium.com/v2/resize:fit:700/1*WIspnbRuJTatxib7ltjDeg.png)

Notice that the coordinate system cuts the onion, much as usual grid lines cut the plane into rectangles in the Cartesian coordinate system. The radial part of the coordinate system cuts the onion radially (which of course nature does by default, but we need to model this mathematically), while the angular part of the coordinate system cuts the onion as our knife would if we were making straight cuts towards the center of the onion. Even though every piece of the onion is infinitely small (there are infinitely many layers, and infinitely many cuts) The Jacobian _r dr dθ_ gives a measure of how big the infinitely small pieces are relative to each other. Pieces near the center of the onion are smaller than pieces near the edge of the onion, as we can see that since _r_ is smaller towards the center of the onion and larger towards the edge of the onion.

We can find the average value of the function _f(r,θ) = r_ over the part of the plane that defines the onion to find the average weight of the infinitesimal area, _A_.

![Image 66: Equation for average infintesimal area](https://miro.medium.com/v2/resize:fit:514/1*gkxaMzRDw1IhfFtt6mCPIg.png)

Once we have the average, we can find the variance, _v_, of the weight of the infinitesimal area by calculating

![Image 67: Equation for infinitesimal variance](https://miro.medium.com/v2/resize:fit:682/1*1Mqp6Y-9Y75eyi_dLGxGPw.png)

The variance is a good measure of the uniformity of the pieces. If the variance is large, the pieces are not very uniform, and vice-versa.

The problem with this analysis, of course, is that we are cutting towards the center of the onion. We want to cut towards a point below the center of the onion. To accomplish this, we need a new coordinate system.

We make a coordinate system for cutting towards a point a distance _h\>0_ below the center of the onion. In this coordinate system, we measure the angle theta from the point _(0,-h)_, while we measure the radius from the origin _(0,0)_ (both points in the rectangular coordinate system). The radial part of the coordinate system cuts the onion radially from the origin as before, while the angular part of the coordinate system cuts the onion as our knife would if we were making straight cuts towards the point _(0,-h)_, below the onion.

![Image 68](https://miro.medium.com/v2/resize:fit:700/1*un-K3W8FI0nwnykyXOFiUQ.png)

The new coordinate system also cuts the onion, but in exactly the way we want it to in order to model the cutting of an onion radially towards a point beneath the cutting board.

This coordinate system only works for the upper half plane, as there are now technically two points in the plane for a given point _(r,θ)_. Luckily, our onion is entirely in the upper-half plane!

In this coordinate system, the region of the plane that we model as the onion is defined by _\-_arctan_(_1_/h) ≤ θ ≤_ arctan_(_1_/h)_, and _h |_tan_(θ)| ≤ r ≤1_. We can eliminate the absolute value by using symmetry. Since the left side of the onion is a mirror image of the right side of the onion, and therefore both sides would have the same variance in area, we can perform this analysis just in the first quadrant. So, the region is defined by 0_≤θ≤_arctan_(_1_/h)_, and _h_ tan_(θ) ≤r≤_1.

The relation between _(x,y)_ and _(r,θ)_ is less clear. Given we know _r, h_, and _θ_, we can draw the following triangle, with a new variable c which represents the distance from the point _(0,-h)_ to a given point _(x,y)_ (both in the rectangular coordinate system).

![Image 69](https://miro.medium.com/v2/resize:fit:700/1*PTy7BVXMxxdkYdxDqHyRRg.png)

First, using the law of cosines, we can calculate

![Image 70](https://miro.medium.com/v2/resize:fit:608/1*rfjhLXQGcByKRqIjZI-EPg.png)

Using this, we can find the relationship between _(x,y)_ and _(r,θ)_ as

![Image 71: equation for x and y in terms of h, r, and theta](https://miro.medium.com/v2/resize:fit:700/1*3Qc8k1sVXcJAdZVShfTISA.png)

From this, for a given depth _h_, we can calculate the Jacobian as

![Image 72: the Jacobian as a function of h, r, and theta. It is multiple lines and complicated.](https://miro.medium.com/v2/resize:fit:700/1*Do_rPsTnOKqukDVAzPSEJA.png)

This is, to put it mildly, complicated. Nevertheless, we have done fairly straightforward calculus computations to get here, which shows the power of making this problem continuous. Mimicking what we did before, given a depth _h_, we can find the average weight of the infinitesimal area, _A(h)_, by calculating the integral of the Jacobian over the onion region divided by the integral of 1 over the same region

![Image 73: Equation for average infintesimal area](https://miro.medium.com/v2/resize:fit:700/1*1SCPsG-RP4YgIFcOyBwdjA.png)

And the variance of the weight of the infinitesimal area, _v(h)_, is found by calculating the integral of the square of the Jacobian minus _A(h)_ over the onion region divided by the integral of 1 over the same region

![Image 74: Equation for variance of the infintesimal area](https://miro.medium.com/v2/resize:fit:700/1*hWL6XQXzbtw-SKF9y1QGKg.png)

Yikes! Integrating this by hand looks really difficult, if not impossible. We should use a computer to help us. Using the power of numerical integration in Mathematica, we can plot the variance versus _h_, the depth of the point we are cutting towards.

![Image 75: graph of variance versus h, the depth to which we cut the onion radially.](https://miro.medium.com/v2/resize:fit:700/1*HzWcOlCsDJOXswDJbo8s8Q.png)

We can see the minimum variance is around _h_\=.55. We can use a numerical minimization technique to find the _h_ that minimizes the variance.

I am only confident of this number to 7 decimal points, but the “true onion constant” for the “onion in the sky” is given by 0.5573066…

To get the most even cuts of an onion by making radial cuts, one should aim towards a point 55.73066% the radius of the onion below the center. This is close, but different from, the 61.803% claimed in the Youtube video at the top. Also, this number will be different for onions for finitely many layers (that is to say, all onions). Nevertheless, I find this answer to be beautiful, and I will forever treasure the true onion constant.

I think it would be interesting to consider the effect of the number of layers on this answer. Since with one layer the best strategy is to cut towards the center, I suspect that the best depth _h_ to cut towards increases from zero with one layer, with .5573066… as the upper bound on the depth. So, the best depth for an onion with ten layers would be somewhere between 0 and 0.5573066. I have not investigated this in depth, but this seems like a fun next step.

I hope we all now know enough about onions to object.

![Image 76](https://miro.medium.com/v2/resize:fit:700/1*dDbLMFoP869FOHDPJRFO-g.jpeg)

Comic from Li Chen [https://www.exocomics.com/685/](https://www.exocomics.com/685/)

Update: I actually was able to evaluate _v(h)_ in a closed form. The techniques used to do it are really fun, and I am hoping to write them up for a recreational mathematics journal.

As calculus students know, if you want to minimize a function, you should take the derivative and set it equal to zero. Here, the derivative of _v(h)_ is given by

![Image 77](https://miro.medium.com/v2/resize:fit:700/1*xYLwZzZqMcjRLTqOQexYsg.png)

The unique root of the above expression in the interval _(0,1)_ is the onion constant, since it is a critical point for the function _v(h)_ and the sign of _v’(h)_ changes from negative to positive at this point, as seen in the graph of _v’(h)_ below.

![Image 78](https://miro.medium.com/v2/resize:fit:700/1*SmkSWiXxsMs4J0N10mR9Kw.png)

The derivative of v with respect to h. Notice that the derivative crosses the horizontal axis around 0.55, which is the onion constant. The sign change from negative to positive means this is a minimum of the v function.

With this, I can calculate the onion constant to arbitrary precision. Here it is to 1000 decimal places: 0.5573066929856644788510930591459271808320003020727327593398292131946981351272104586975295563488927792384215157297641443660261449855854165046873271472618959107816152780606384065758548635804885244580180000739444280590673621405484408743288174143897178500658897679049099235460450539966379793582365697832234771908624791276216076862484729083731336235000704236891376747519710815301807822317779086701048122723023915093054323298702150340065450327186756623642052156098646912508581593702205375240220768344875026631985363470644632525528856220691258227307037720900190873707797080215945078389222941122441664099620992665469305266348508835318836823451849946341751553954012216070423374355399193069992187951842347509926071534835419058678494025712006870992663407278202945110198402208378584410140122892631419360798953694134222761038423480438048889054739124583187162972867878589998414926409519790844390232917730134252343064728228633559834886507214553757974736357343027167265972675903577598983959532796594227162648681839040…

Such a beautiful mathematical constant deserves a name. I choose to use the Hebrew character samekh, because it looks particularly like an onion.

![Image 79](https://miro.medium.com/v2/resize:fit:700/1*SmvcQdS5JCumMwT51JnhvQ.png)

