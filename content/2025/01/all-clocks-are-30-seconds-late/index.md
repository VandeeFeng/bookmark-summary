---
title: All clocks are 30 seconds late
date: 2025-01-08
extra:
  source: https://victorpoughon.fr/all-clocks-are-30-seconds-late/
  original_title: All clocks are 30 seconds late
---
## Summary
**摘要**：
这篇文章探讨了一个理论观点：无论是日常的壁挂钟还是智能手机上的时钟，它们实际上都比准确的时间慢了30秒。作者提出这种观点的原因是现有时钟只显示整分钟，不显示秒数，而它们显示的时间实际上是当前时间的前一分钟的结束时刻。例如，如果当前时间是14:15:59，时钟只会显示14:15。所以平均而言，大多数时钟显示的时间要比正点慢30秒。

**要点总结**：
1. **时钟的显示行为**：大多数时钟使用四舍五入的方式显示时间，将时间四舍五入到最近的整分钟，而不是将秒数舍去跳跃至下一分钟。以当前时间14:15:59为例，时钟将显示14:16，但实际上只过了15分钟，距离真正14:16还差一秒。这种行为意味着这些时钟在总的平均时间上滞后了30秒。

   **(解析)：** 秒数被四舍五入意味着从大多数时间到下一个整分钟的转换会在后一分钟的开始小于一秒的地方发生。例如，从14:15:59跳转到14:16不考虑秒数，只显示一个整数分钟。换言之，14:15:59到14:16之间只经历了不足一秒的时间差，这表明所有使用这样机制显示时间的设备实际上在平均时间上滞后30秒。

2. **建议更正的显示方式**：如果时钟显示时间时采用四舍而不是五入的方式来解决时间设置所导致的平均滞后问题。这样，当前时间14:15实际上应该在一个人的观念中表示为14:15:30。因此，当时间显示为14:15+（直到14:16-1），总平均时间将比实际情况提前30秒。

   **(解析)：** 通过将时间精确到最近的秒级，时钟将能正确传达当前精确时间和观察者的预期时间，避免了以整分钟跳跃所导致的平均滞后。如果时间表显示将每隔秒数视为一个整数单位，每个整数单位将涵盖半秒的真实时间变化，有效地解决了时钟平均滞后问题。

3. **时间显示的理解问题**：作者质疑了将时间是以整数形式表示的时间段的观念，强调了小时、分钟和秒连续并且连续考虑的重要性。作者认为在分钟、小时和基于它们的更长的时间间隔上，人们更倾向于采用四舍的方式而不是像其他分钟周期那样直接取整。

   **(解析)：** 此观点提出了一种对时间表示方式的重新思考，从而认识到当前对于时钟的设计是基于由整数分钟拟合成的便利性进行的。然而，它也可能引发关于时间连续性和表示时钟方式的更深层次的讨论，强调精度与便利性的权衡在实用性和抽象思考之间的体现。

4. **对比传统与预期的时间刻度**：文章讨论了不同时间尺度上人们出于习惯或便利性如何在思维上对时间的表示方式进行了调整。作者举例说明小时每当接近整点之前都会被四舍而不是五入的情况，但也提出在分钟单位上人们对时间进行四舍的方式，从而反映出不同时间刻度的影响与人们对精确度与便利性的权衡。

   **(解析)：** 时间显示与概念的重新审视推动了对时钟交互与时间感知方法的反思。揭示了在不同时间范围内如何接受、理解和预设时间的不同表示方式，形成了对于传统的指定时间机制以及个人时间观念的深层次疑问。

5. **文化的多样性与时间表达**：作者对不同文化间对于时间的表达及理解进行了概述，强调了时间表示的多样性。其中包含“下午2点15分钟和双12小时制时间”差异的举例，强调不同文化的传统与习惯如何影响对于一天的刻分解读和时间论述。

   **(解析)：** 文章通过介绍不同时间表达方式的辨识，探讨了时间概念在文化和传统方面表现出的深刻差异，突出了对于时间表述及其在不同文化背景下所具有的独特内涵的洞察。这一部分不仅强调了对于时间模型的理解与实用性层面的考虑，也展现了跨文化时间实践的丰富性。
## Full Content
Title: All clocks are 30 seconds late

URL Source: https://victorpoughon.fr/all-clocks-are-30-seconds-late/

Markdown Content:
_06 Jan, 2025_

OK, this is going to sound crazy: I believe all clocks are 30 seconds late.

Let's get a few things out of the way: this is neither about time zones, nor leap seconds. It's not about synchronization of clocks, and it's not about relativity or any obscure corner of physics. I'm talking about everyday clocks. The ones that you might have around in your house, like this one that sits on my desk:

![Image 7: post2image1](https://bear-images.sfo2.cdn.digitaloceanspaces.com/victorpoughon/post2image1-2.webp)

Or even the clock on your phone! Maybe they're all correctly set very precisely to a very accurate reference clock, but here I will argue that they are still exactly 30 seconds late. In other words:

> It would be more accurate if they were thirty seconds ahead.

What are you on about?
----------------------

All the above clocks have one thing in common: they don't show seconds. They truncate down to the nearest lower whole minute, right? So when it's actually `14:15:45`, they'll show `14:15`. And when the actual time goes from `14:15:59` to `14:16:00`, then that's when your clock changes from `14:15` to `14:16`.

They apply the [floor function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions)!

Ok great. Now hear me out! Let's compute the average error between a usual (truncating) clock, and the precise current time.

import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

\# A datetime array from 14:00:15pm for 300 seconds
true\_time \= np.array(\[datetime.datetime(2024, 12, 20, 14, 00, 15) + datetime.timedelta(seconds\=i) for i in range(300)\])

\# The clock truncates seconds
shown\_time \= \[t.replace(second\=0) for t in true\_time\]

\# The clock error is the shown time minus the true time
error \= \[dt.total\_seconds() for dt in (shown\_time \- true\_time)\]

fig, ax \= plt.subplots(figsize\=(10, 3.5))
ax.plot(true\_time, error, label\="clock error", color\="teal")
ax.hlines(np.mean(error), xmin\=true\_time\[0\], xmax\=true\_time\[\-1\], label\="average", linestyle\="--", color\="orange")
ax.xaxis.set\_major\_formatter(mdates.DateFormatter('%H:%M'))
ax.set\_ylim(\[\-60, 60\])
ax.set\_title("A normal clock")
ax.legend()

![Image 8: post2plot1](https://bear-images.sfo2.cdn.digitaloceanspaces.com/victorpoughon/post2plot1-1.webp)

*   Sometimes the error is 1 or 2 seconds, like when the clock shows `14:02` and it's actually `14:02:01`
*   Sometimes the error is almost 60 seconds, like when the clock shows `14:02` and it's actually `14:02:57`

So, the average error of a truncating clock is 30 seconds. Let that sink in for a moment: **the average error of a clock is 30 seconds**. If clocks [rounded](https://en.wikipedia.org/wiki/Rounding) to the nearest minute instead of truncating, the average error would be 0. Therefore all clocks are 30 seconds late!

Similarly of course, all clocks that show seconds but not milliseconds are half a second late.

\# The rounding clock! aka +30s
shown\_time \= \[(t + datetime.timedelta(seconds\=30)).replace(second\=0) for t in true\_time\]

\# The clock error is the shown time minus the true time
error \= \[dt.total\_seconds() for dt in (shown\_time \- true\_time)\]

fig, ax \= plt.subplots(figsize\=(10, 3.5))
ax.plot(true\_time, error, label\="clock error", color\="teal")
ax.hlines(np.mean(error), xmin\=true\_time\[0\], xmax\=true\_time\[\-1\], label\="average", linestyle\="--", color\="orange")
ax.xaxis.set\_major\_formatter(mdates.DateFormatter('%H:%M'))
ax.set\_ylim(\[\-60, 60\])
ax.set\_title("A rounding clock")
ax.legend()

![Image 9: post2plot2](https://bear-images.sfo2.cdn.digitaloceanspaces.com/victorpoughon/post2plot2-1.webp)

This is just a convention
-------------------------

> But this is just a convention! Truncating, rounding or even ceiling are all valid, as long as we pick one and stick to it. By your logic we should say that it's Tuesday as soon as it's one second past noon on Monday.

Well... kind of.

It would be weird if we rounded for years, months and days, that's for sure. I think most people think of those scales as intervals. In other words, July is a period of time, with a start and an end. So are years, centuries, seasons. We are inside of it or outside.

Is it the same for the current minute of the current hour ? I'm not so sure.

Basically I'm arguing that rounding for clocks would be more useful than flooring. This is especially apparent when you're trying to calculate "how much time until my next meeting?", and your next meeting is at noon. If it's 11:55, you would usually mentally subtract and conclude: the meeting is in 5 minutes. That's how I always do it myself anyway! But the most probable estimate given the available information is actually 4'30"!

If you had a rounding clock instead, 5 minutes would be the correct estimation.

In fact, as we go down the various scales of time all the way from years, months, days and we reach hours, that's when we start truncating! At hours! For example: if it's `10:43` and you are asked the time and (for some context appropriate reason) you reply with just hours, you would say it's 11! Personally, I would never say that it's 10 if the clock shows anything past `10:30`. I realize that's probably very different in other cultures, though! And I'd be interested to learn about how different cultures approximate time in language.

So, looking at the various scales of time and how I mentally view them:

*   **Years**: truncate. If the full date has `2019` in it, I'll say "the year is 2019" - all the way to the end. Saying "it's 2020" in September 2019 is super weird.
*   **Months**: truncate. It's January all the way until it's February.
*   **Days**: truncate. It gets a little weird if it's past midnight and I haven't slept yet. Is tomorrow today? Or is it the day after that? I think collectively we still haven't quite figured that one out yet. And that's ok. Kind of like how "next Friday" becomes ambiguous on Thursdays. Some cultures use times beyond 24:00, like 25:30 to indicate one hour and a half past midnight, and I think that's lovely!
*   **Hours**: That's when mentally, I switch to rounding! At `15:48` I definitely feel like it's pretty much `16:00`.
*   **Minutes**: At `15:48:57`, I definitely feel like it's `15:49`! But clocks switch back to flooring for for some reason! But mentally we round! This is why I feel like all clocks are 30 seconds late: because the truncating convention doesn't match my intuition at the minute scale.
*   **Seconds and below**: definitely rounding.

Please someone tell me I'm not crazy 🙃

**EDIT 2025-01-07**:

This kinda [blew up on HN](https://news.ycombinator.com/item?id=42612842) and I want to clarify something: This is a tongue-in-cheek article! It's fun to think about, but in the end, this IS a convention and the most important thing about conventions is that we all follow the same ones. I'm obviously not going to move all my clocks forwards by 30 seconds and neither should you! In many ways truncating is a much better convention and that's why we use it.

I've also been made aware that Big Ben is truly an analog clock and doesn't jump around every minute, so I've removed that example. My bad! The point still stands because some "analog" clocks actually jump every minute and are not truly analog, but I should have picked a better example photo.

