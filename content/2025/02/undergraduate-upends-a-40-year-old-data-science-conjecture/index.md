---
title: Undergraduate Upends a 40-Year-Old Data Science Conjecture
date: 2025-02-12
extra:
  source: https://www.quantamagazine.org/undergraduate-upends-a-40-year-old-data-science-conjecture-20250210/
  original_title: Undergraduate Upends a 40-Year-Old Data Science Conjecture
---
## Summary
**摘要**:
通过一篇关于微软博客的文章,讲述了年轻计算机科学家安德鲁·克拉皮文在“小指针”论文的启发下,发现了改变数据存储方式的新方法。从2021年在拉特格斯大学遇到论文开始,并在毕业后、成为牛津大学剑桥分校研究生期间,克拉皮文教授自己的发现,改进了哈希表的核心结构,实现了数据查找效率的显著提升。此次发现克服了一个公认的难题——常规下存储数据所形成的哈希表中寻找元素最坏情况下的时间复杂度是线性增长的。克拉皮文围绕散列表进行了创新,创造了“快速定位”哈希表,优化了最坏情况下查找和插入元素的效率,达到了理论上的最佳状态。团队成功揭示了40年来被广泛接受但未能被彻底验证的数据科学假设——“元雅的散列运动”理论的局限性,展示了与其计算预测大相径庭的启发。

**要点总结**:
- **问题与挑战**:以前的数据结构设计规则,尤其是在哈希表中查找特定元素效率方面,表现出时间复杂度为线性增长,随着数据量的增加而变慢。
- **发现**:克拉皮文及其老师的合作揭示了“小指针”论文中提到的有效策略,付诸实践并取得了突破性成果,优化了数据结构和数据查找过程。
- **理论推进**:证实了40年前元雅关于散列表效率的猜测存在质疑,揭示了散列表最佳效率值的理论上限(\(log_{2}x^{2}\)),挑战了过去40年中最常使用的数据结构模式。
- **创新构思**:克拉皮文创造了新型哈希表,开启了在无可比拟的低时间复杂度下进行查询和插入操作的新篇章,突破了传统数据科学的瓶颈。
- **领域影响**:这一突破预示着对数据存储、数据科学以及计算机科学理论的可能进展,对提升计算效率和新应用的挖掘具有重要意义。这一发现不仅回应了先前的理论课题,还主动提出了一个实际且独立的挑战问题,即根基性的计算效率探索中尚未发现的理想解决方案。

## Full Content
Title: Undergraduate Upends a 40-Year-Old Data Science Conjecture

URL Source: https://www.quantamagazine.org/undergraduate-upends-a-40-year-old-data-science-conjecture-20250210/

Published Time: 2025-02-10T15:17:37+00:00

Markdown Content:
A young computer scientist and two colleagues show that searches within data structures called hash tables can be much faster than previously deemed possible.

Introduction
------------

Sometime in the fall of 2021, Andrew Krapivin, an undergraduate at Rutgers University, encountered a paper that would change his life. At the time, Krapivin didn’t give it much thought. But two years later, when he finally set aside time to go through the paper (“just for fun,” as he put it), his efforts would lead to a rethinking of a widely used tool in computer science.

The paper’s title, “[Tiny Pointers](https://arxiv.org/abs/2111.12800),” referred to arrowlike entities that can direct you to a piece of information, or element, in a computer’s memory. Krapivin soon came up with a potential way to further miniaturize the pointers so they consumed less memory. However, to achieve that, he needed a better way of organizing the data that the pointers would point to.

He turned to a common approach for storing data known as a hash table. But in the midst of his tinkering, Krapivin realized that he had invented a new kind of hash table, one that worked faster than expected — taking less time and fewer steps to find specific elements.

[Martín Farach-Colton](https://engineering.nyu.edu/faculty/martin-farach-colton), a co-author of the “Tiny Pointers” paper and Krapivin’s former professor at Rutgers, was initially skeptical of Krapivin’s new design. Hash tables are among the most thoroughly studied data structures in all of computer science; the advance sounded too good to be true.  But just to be sure, he asked a frequent collaborator (and a “Tiny Pointers” co-author), [William Kuszmaul](https://csd.cmu.edu/people/faculty/william-kuszmaul) of Carnegie Mellon University, to check out his student’s invention. Kuszmaul had a different reaction. “You didn’t just come up with a cool hash table,” he remembers telling Krapivin. “You’ve actually completely wiped out a 40-year-old conjecture!”

Together, Krapivin (now a graduate student at the University of Cambridge), Farach-Colton (now at New York University) and Kuszmaul demonstrated in a [January 2025 paper](https://arxiv.org/abs/2501.02305) that this new hash table can indeed find elements faster than was considered possible. ln so doing, they had disproved a conjecture long held to be true.

“It’s an important paper,” said [Alex Conway](https://ajhconway.com/) of Cornell Tech in New York City. “Hash tables are among the oldest data structures we have. And they’re still one of the most efficient ways to store data.” Yet open questions remain about how they work, he said. “This paper answers a couple of them in surprising ways.”

Hash tables have become ubiquitous in computing, partly because of their simplicity and ease of use. They’re designed to allow users to do exactly three things: “query” (search for) an element, delete an element, or insert one into an empty slot. The first hash tables date back to the early 1950s, and computer scientists have studied and used them ever since. Among other things, researchers wanted to figure out the speed limits for some of these operations. How fast, for example, could a new search or insertion possibly be?

The answer generally depends on the amount of time it takes to find an empty spot in a hash table. This, in turn, typically depends on how full the hash table is. Fullness can be described in terms of an overall percentage — this table is 50% full, that one’s 90% — but researchers often deal with much fuller tables. So instead, they may use a whole number, denoted by _x_, to specify how close the hash table is to 100% full. If _x_ is 100, then the table is 99% full. If _x_ is 1,000, the table is 99.9% full. This measure of fullness offers a convenient way to evaluate how long it should take to perform actions like queries or insertions.

Researchers have long known that for certain common hash tables, the expected time required to make the worst possible insertion — putting an item into, say, the last remaining open spot — is proportional to _x_. “If your hash table is 99% full,” Kuszmaul said, “it makes sense that you would have to look at around 100 different positions to find a free slot.”

In a [1985 paper](https://dl.acm.org/doi/10.1145/3828.3836), the computer scientist [Andrew Yao](https://amturing.acm.org/award_winners/yao_1611524.cfm), who would go on to win the A.M. Turing Award, asserted that among hash tables with a specific set of properties, the best way to find an individual element or an empty spot is to just go through potential spots randomly — an approach known as uniform probing. He also stated that, in the worst-case scenario, where you’re searching for the last remaining open spot, you can never do better than _x_. for 40 years, most computer scientists assumed that Yao’s conjecture was true.

Krapivin was not held back by the conventional wisdom for the simple reason that he was unaware of it. “I did this without knowing about Yao’s conjecture,”  he said. His explorations with tiny pointers led to a new kind of hash table — one that did not rely on uniform probing. And for this new hash table, the time required for worst-case queries and insertions is proportional to (log _x_)2 — far faster than _x_. This result directly contradicted Yao’s conjecture. Farach-Colton and Kuszmaul helped Krapivin show that (log _x_)2 is the optimal, unbeatable bound for the popular class of hash tables Yao had written about.

“This result is beautiful in that it addresses and solves such a classic problem,” said [Guy Blelloch](http://www.cs.cmu.edu/~guyb/) of Carnegie Mellon.

“It’s not just that they disproved \[Yao’s conjecture\], they also found the best possible answer to his question,” said [Sepehr Assadi](https://cs.uwaterloo.ca/about/people/sassadi) of the University of Waterloo.  “We could have gone another 40 years before we knew the right answer.”

In addition to refuting Yao’s conjecture, the new paper also contains what many consider an even more astonishing result. It pertains to a related, though slightly different, situation: In 1985, Yao looked not only at the worst-case times for queries, but also at the average time taken across all possible queries. He proved that hash tables with certain properties — including those that are labeled “greedy,” which means that new elements must be placed in the first available spot — could never achieve an average time better than log _x_.

Farach-Colton, Krapivin and Kuszmaul wanted to see if that same limit also applied to non-greedy hash tables. They showed that it did not by providing a counterexample, a non-greedy hash table with an average query time that’s much, much better than log _x_. In fact, it doesn’t depend on _x_ at all. “You get a number,” Farach-Colton said, “something that is just a constant and doesn’t depend on how full the hash table is.” The fact that you can achieve a constant average query time, regardless of the hash table’s fullness, was wholly unexpected — even to the authors themselves.

The team’s results may not lead to any immediate applications, but that’s not all that matters, Conway said. “It’s important to understand these kinds of data structures better. You don’t know when a result like this will unlock something that lets you do better in practice.”

