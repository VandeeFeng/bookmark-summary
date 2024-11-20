---
title: Reactive HTML notebooks
date: 2024-11-20
extra:
  source: https://maxbo.me/a-html-file-is-all-you-need.html
  original_title: Reactive HTML notebooks
---
## Summary
**摘要**：
这篇文章探讨了HTML作为科学出版平台的潜力，重点介绍使用HTML实现数据探索、分析、可视化以及文档编排的综合功能。首先，文章演示了如何利用HTML的特性，如内容可编辑和快取更新，创建可交互的笔记，特别是使用了支持动态内容更新的`script`元素。文章进一步展示了如何编写能自增时间的`counter`细胞，并通过引入`Hypertext Literal (htl)`库进行格式化输出，并提供直观数值滚动的可视化。另外，文章还说明HTML匹配或类似LaTeX、Markdown的文本渲染能力，并展示了通过细胞返回不同DOM元素（如`span`、`table`、`svg`等）。通过引入`Pyodide`和`WebR`，HTML进一步展示了支持Python和R语言环境的能力，实现复杂数据分析与绘图功能。最后，文章提出可能开发一个集成了上述特性的HTML库以简化科学出版流程，并给予简要提及将该库如何应用于幻灯片展示的使用情境。

**要点总结**：

1. **HTML作为科学出版平台的潜力**：通过利用HTML的编辑性和动态重载特性，HTML可以无缝承担数据探索、分析、可视化以及最终版本格式化的工作，减少第三方工具和平台的依赖。

2. **动态细胞与实时更新**：展示了如何在HTML中构建动态代码单元（细胞），实现类型添加、数据计算和状态更新，将HTML作为一种现代的交互式计算和文档编辑开发环境。

3. **格式化与渲染**：利用HTML和JavaScript特性，如通过`Hypertext Literal (htl)`库实现高级文本格式化和解析，展示了HTML在构建复杂文档结构和渲染中的应用。

4. **多级语言集成**：证明了Python (`Pyodide`)和R语言环境的集成可能，展示了通过HTML可以在Web端执行和展示图形化分析。

5. **细胞的进阶功能**：探索HTML细胞的多重用途，如互相关联的多个输出、数据存储、中间结果保留和依赖性细胞，以及通过细胞实现的数据交互与用户界面的集成。

**综上所述**，HTML不仅具有强大的文本和数据展示能力，还能通过构建动态计算环境和交互式笔记应用，成为科学出版和数据探索的一个多功能平台。然而，要全面发挥这些功能的潜力，还需不断地开发和完善库和其他辅助工具，使之成为一个更高效、易用的出版和数据分析生态系统。
## Full Content
Title: Reactive HTML notebooks

URL Source: https://maxbo.me/a-html-file-is-all-you-need.html

Published Time: 2024-05-06T00:00:00Z

Markdown Content:
I've packaged this article up and released a library, [@celine/celine](https://maxbo.me/celine). It has a nicer API too. Check it out! (o˘◡˘o)

[← Max Bo](https://maxbo.me/index.html)
---------------------------------------

Published May 6, 2024  
Modified September 9, 2024  
[Hacker News discussion](https://news.ycombinator.com/item?id=42170740)  
[SydJS talk](https://www.youtube.com/watch?v=oMUt0PnKuyc)

Before I start, why am I doing this?

**I don't think HTML is being used enough as a platform for scientific publishing.**

Instead, people will:

1.  Use an interactive notebook like [Jupyter](https://jupyter.org/), [RStudio](https://rmarkdown.rstudio.com/lesson-10.html), [Pluto.jl](https://plutojl.org/) or [Observable](https://observablehq.com/) to do data exploration, analysis and visualisation,
2.  Move to a publishing platform like [Typst](https://typst.app/), [Overleaf](https://overleaf.com/), pure [LaTeX](https://www.latex-project.org/), or a [WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG) editor to typeset their work,
3.  Export to `.pdf` for distribution.

I think a HTML file can be used for all 3 of these stages, and prevent a lot of faffing around with manual processes, CLI tooling, CI steps and 3rd-party platforms.

HTML's typesetting capabilities are well documented, but its capabilities as a platform for data exploration, analysis and visualisation are not.

I'll try and demonstrate these capabilities, literate programming style.

![Image 1: A computer displays an open book](https://maxbo.me/img/document.png)

We also want `contenteditable` `script`s to be re-evaluated on blur by building a clone of the `script` and then removing the original.

Now we'll declare a cell called `counter` that emits a number every second. **The `script`'s `id` attribute is the same as the `name` parameter passed to `cell`**.

_Try changing the initial counter value `i` above to a much bigger number, and then defocus the `script`._

Now that we've created a our `counter` cell, we can create other cells that depend on it.  
We'll import [Hypertext Literal](https://observablehq.com/@observablehq/htl) and use it to format the `counter` value. `htl` implements a full-blown HTML5 parser that performs automatic escaping and interpolation of non-serializable values, such as event listeners, style objects, and other DOM nodes.

We can still observe the output of a cell without needing to show its definition. Just don't add the `echo` class. This makes them useful as a rendering primitive. _(There's a hidden cell above ^)_

Alternatively, we can create a cell type that doesn't display its output at all.  
We can use these cells to store intermediate values or datastructures. Also note that cells can be declared out of order.

We can use cell values in more complex outputs. We'll import [Observable Plot](https://observablehq.com/plot/what-is-plot) and use the `counter` value in a plot.

![Image 2: A computer displays a graph in the upward direction](https://maxbo.me/img/up.png)

TeX, Markdown, Graphviz
-----------------------

We can return any type of DOM element from a cell.  
In this case, the `tex`, `md`, and `dot` cells return `span`, `table` and `svg` elements respectively.

_Try editing any of the following cells._

![Image 3: A computer with an open CD tray is surrounded by data](https://maxbo.me/img/data.png)

Cell status
-----------

We can also return a `Promise`, or throw an `Error`, from a cell. Observable's `Inspector` will apply an `observablehq--running` or `observablehq--error` class to the cell's outer `div` element respectively. We'll style them appropriately:

Python
------

The [Pyodide](http://pyodide.org/) CPython WASM distribution includes [NumPy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), [scikit-learn](https://scikit-learn.org/), and [Scipy](https://scipy.org/). We'll rebuild the plot seen above, but using Matplotlib and Python's `sqlite3` module instead.

_Try editing one of the plot labels!_

R
-

You know the drill. It's R, using [WebR](https://docs.r-wasm.org/webr/latest/). I didn't figure out how to get [ggplot2](https://ggplot2.tidyverse.org/) [rendering](https://docs.r-wasm.org/webr/latest/plotting.html) working, but I assume it's possible. _I must disclose that this cell seems to be a bit flaky on iOS. I have not had a chance to investigate further, nor will I._

Inputs
------

We'll create a new cell type `viewof` that works specifically with [Observable Inputs](https://github.com/observablehq/inputs). It declares 2 reactive cells: `NAME` and `viewof NAME` - one for the value, and one for the DOM element itself.

To display the input above the cell, we set the cell `id` to `viewof NAME`.

_Wiggle the range input and see another dependent cell update._

_NB: The way Observable Inputs work is a bit arcane. This demo of [Synchronized Inputs](https://observablehq.com/@observablehq/synchronized-inputs) may shed some light._

Mutability
----------

Purely functional dataflow is great, but sometimes you just need to mutate state. We'll create a new helper function `mutable`. It registers a `Mutable` - an object that yields new [`Generator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator) values when the value is mutated - in the runtime.

_Try editing the initial state of the `mutable`._ _Try editing the button labels._

What's next?
------------

~I will try and cram all of this into a library with some proper documentation.~  
~I initially thought it should be called `incel` (short for _inline cell_), but I'll probably call it `celine` instead.~I've released a library! It's called [@celine/celine](https://maxbo.me/celine)!

![Image 4: A computer terminal receives text](https://maxbo.me/img/typing.gif)

Slide infrastructure
--------------------

I demo'd this article at [SydJS](https://www.youtube.com/@SydJSMeetup). This is the code I used to turn the article into a slideshow.

*   Shift + N - Start slideshow / next slide
*   Shift + B - Previous slide
*   Shift + E - End slideshow

