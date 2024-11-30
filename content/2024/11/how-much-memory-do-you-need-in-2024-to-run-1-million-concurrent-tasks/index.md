---
title: How Much Memory Do You Need in 2024 to Run 1 Million Concurrent Tasks?
date: 2024-11-30
extra:
  source: https://hez2010.github.io/async-runtimes-benchmarks-2024/
  original_title: How Much Memory Do You Need in 2024 to Run 1 Million Concurrent Tasks?
---
## Summary
**摘要**：
这篇文章主要是关于比较不同编程语言在实现1百万个并发任务时的内存消耗。在2024年底，作者再次进行了基准测试，比较了不同语言在并发执行任务时的性能变化。测试环境包括最新的硬件设备（13th Gen Intel(R) Core(TM) i7-13700K）和操作系统（Debian GNU/Linux 12）等。

**要点总结**：
1. **静态编译语言**：在实现大量并发任务时，例如进程控制、协程等概念，协程的支持使得Rust和C# (使用NativeAOT)展现出了较小的内存消耗。这类语言静态编译成本机二进制，对自身实现有较好的内存控制。

2. **内存消耗**：在不同的并发任务数量下（比如10K、100K和100万个任务），内存消耗出现了显著变化。以Rust为代表的部分静态编译语言表现优势明显，而高级语言如Java（通过GraalVM运行）和C#表现出超越预期的内存效率，成本更加合理。

3. **性能超常**：当并发任务量增加到100万个时，C#显示出显著的优势，运行内存消耗较低且在所有测试语言中击败了其他语言，包括内存消耗通常被认为较高的Java版本（使用GraalVM运行）。C#已展现出极高的竞争力和出色的内存效率。

4. **Go的局限性**：尽管Go的协程最初被认为较为健壮且效率高，但其内存消耗远超过静态编译的语言。当并发任务量增大时，Go的表现不如Java与使用GraalVM运行的Java版本、C#和NodeJS。

5. **改进与发现**：在新测试中，加入了一个from `join_all`到使用循环遍历`Vec`的测试用例，这使得Rust实现了更小的内存消耗，并最终成为测试中的领导者。这种优化方式对于动态语言Rust来说是关键进步。

**关键发现**：
- 高并发任务执行时，选择语言对内存消耗有显著影响。适合瓶颈场景的语言表现出更好的内存控制性。
- 高级语言如C#和以静态编译为主的语言如Rust，在大规模并发任务的内存消耗上取得突破性成果，提高了市场整体性能表现。
- 经过性能优化后，选择不同的库和实现方式（如C++协程的Rust-to-vec迭代替代`join_all`）对于提高内存效率有显著帮助。
## Full Content
Title: How Much Memory Do You Need in 2024 to Run 1 Million Concurrent Tasks?

URL Source: https://hez2010.github.io/async-runtimes-benchmarks-2024/

Markdown Content:
Did you still remember [the memory consumption comparison](https://pkolaczk.github.io/memory-consumption-of-async/) between asynchronous programming across popular languages in 2023?

Now at the end of 2024, I wonder how things changed in the span of one year, with the latest version of languages.

Let's do the benchmark again and see the results!

Benchmark
---------

The program to benchmark is the same with the one in the last year:

> Let's launch N concurrent tasks, where each task waits for 10 seconds and then the program exists after all tasks finish. The number of tasks is controlled by the command line argument.

This time, let's focus on coroutine instead of multiple threads.

All benchmark code can be accessed at [async-runtimes-benchmarks-2024](https://github.com/hez2010/async-runtimes-benchmarks-2024).

What is a coroutine?

> Coroutines are computer program components that allow execution to be suspended and resumed, generalizing subroutines for cooperative multitasking. Coroutines are well-suited for implementing familiar program components such as cooperative tasks, exceptions, event loops, iterators, infinite lists and pipes.

### Rust

I created 2 programs in Rust. One uses `tokio`:

```
use std::env;
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() {
    let args: Vec<String> = env::args().collect();
    let num_tasks = args[1].parse::<i32>().unwrap();
    let mut tasks = Vec::new();
    for _ in 0..num_tasks {
        tasks.push(sleep(Duration::from_secs(10)));
    }
    futures::future::join_all(tasks).await;
}
```

while another one uses `async_std`:

```
use std::env;
use async_std::task;
use futures::future::join_all;
use std::time::Duration;

#[async_std::main]
async fn main() {
    let args: Vec<String> = env::args().collect();
    let num_tasks = args[1].parse::<usize>().unwrap();
    
    let mut tasks = Vec::new();
    for _ in 0..num_tasks {
        tasks.push(task::sleep(Duration::from_secs(10)));
    }

    join_all(tasks).await;
}
```

Both are popular async runtime commonly used in Rust.

### C#

C#, similar to Rust, has first-class support for async/await:

```
int numTasks = int.Parse(args[0]);
List<Task> tasks = new List<Task>();

for (int i = 0; i < numTasks; i++)
{
    tasks.Add(Task.Delay(TimeSpan.FromSeconds(10)));
}

await Task.WhenAll(tasks);
```

.NET also offers NativeAOT compilation since .NET 7, which compiles the code to the final binary directly so that it no longer needs a VM to run managed code. So we added the benchmark for NativeAOT as well.

### NodeJS

So does NodeJS:

```
const util = require('util');
const delay = util.promisify(setTimeout);

async function runTasks(numTasks) {
  const tasks = [];

  for (let i = 0; i < numTasks; i++) {
    tasks.push(delay(10000));
  }

  await Promise.all(tasks);
}

const numTasks = parseInt(process.argv[2]);
runTasks(numTasks);
```

### Python

And Python, too:

```
import asyncio
import sys

async def main(num_tasks):
    tasks = []

    for task_id in range(num_tasks):
        tasks.append(asyncio.sleep(10))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    num_tasks = int(sys.argv[1])
    asyncio.run(main(num_tasks))
```

### Go

In Go, goroutines are the building block for concurrency. We don’t await them separately, but we use a `WaitGroup` instead:

```
package main

import (
    "fmt"
    "os"
    "strconv"
    "sync"
    "time"
)

func main() {
    numRoutines, _ := strconv.Atoi(os.Args[1])
    var wg sync.WaitGroup
    for i := 0; i < numRoutines; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            time.Sleep(10 * time.Second)
        }()
    }
    wg.Wait()
}
```

### Java

Java offers virtual threads since JDK 21, which are a similar concept to goroutines:

```
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;

public class VirtualThreads {

    public static void main(String[] args) throws InterruptedException {
	    int numTasks = Integer.parseInt(args[0]);
        List<Thread> threads = new ArrayList<>();

        for (int i = 0; i < numTasks; i++) {
            Thread thread = Thread.startVirtualThread(() -> {
                try {
                    Thread.sleep(Duration.ofSeconds(10));
                } catch (InterruptedException e) {
                    // Handle exception
                }
            });
            threads.add(thread);
        }

        for (Thread thread : threads) {
            thread.join();
        }
    }
}
```

While there's a new variant of JVM called GraalVM. GraalVM also offers native image, which is a similar concept to NativeAOT in .NET. So we added the benchmark for GraalVM as well.

Test Environment
----------------

*   Hardware: 13th Gen Intel(R) Core(TM) i7-13700K
*   OS: Debian GNU/Linux 12 (bookworm)
*   Rust: 1.82.0
*   .NET: 9.0.100
*   Go: 1.23.3
*   Java: openjdk 23.0.1 build 23.0.1+11-39
*   Java (GraalVM): java 23.0.1 build 23.0.1+11-jvmci-b01
*   NodeJS: v23.2.0
*   Python: 3.13.0

All programs were launched using the release mode if available, and support for internationalization and globalization was disabled as we did't have libicu in our test environment.

Results
-------

### Minimum Footprint

Let's start from something small, because some runtimes require some memory for themselves, let's first launch only one task.

We can see that Rust, C# (NativeAOT), and Go achieved similar results, as they were compiled statically to native binaries and needed very little memory. Java (GraalVM native-image) also did a great job but cost a bit more than the other statically compiled ones. The other programs running on managed platforms or through interpreters consume more memory.

Go seems to have the smallest footprint in this case.

Java with GraalVM is a bit surprising, as it cost far more memory than Java with OpenJDK, but I guess this can be tuned with some settings.

### 10K Tasks

A few surprises here! The two Rust benchmarks achieved very promising results: they both used very little memory, which didn't grow too much compared to minimal footprint results, even though there were 10K tasks running behind the scenes! C# (NativeAOT) followed closely behind, using only ~10MB of memory. We need more tasks to put more pressure on them!

The memory consumption grew dramatically in Go. Goroutines are supposed to be very lightweight, but they actually consumed far more RAM than Rust required. In this case, virtual threads in Java (GraalVM native image) seem to be more lightweight than Goroutines in Go. To my surprise, both Go and Java (GraalVM native image), which were compiled to native binaries statically, cost more RAM than the C# one running on a VM!

### 100K Tasks

After we increased the number of tasks to 100K, the memory consumption of all the languages started to grow significantly.

Both Rust and C# did a really good job in this case. A big surprise is that C# (NativeAOT) even cost less RAM than Rust and beat all other languages. Really impressive!

At this point, the Go program has been beaten not only by Rust but also by Java (except the one running on GraalVM), C#, and NodeJS.

### 1 Million Tasks

Let's go extreme now.

Finally, C# undoubtedly beat all other languages; it's very competitive and has really become a monster. And as expected, Rust continues to do a good job on memory efficiency.

The distance between Go and the others increased. Now Go loses by over 13 times to the winner. It also loses by over 2 times to Java, which contradicts the general perception of the JVM being a memory hog and Go being lightweight.

Final Word
----------

As we have observed, a high number of concurrent tasks can consume a significant amount of memory, even if they do not perform complex operations. Different language runtimes have varying trade-offs, with some being lightweight and efficient for a small number of tasks but scaling poorly with hundreds of thousands of tasks.

Many things have changed since last year. With the benchmark results on the latest compilers and runtimes, we see a huge improvement in .NET, and .NET with NativeAOT is really competitive with Rust. The native image of Java built with GraalVM also did a great job in terms of memory efficiency. However, goroutines continue to be inefficient in resource consumption.

Appendix
--------

Some folks pointed out that in Rust (tokio) it can use a loop iterating over the `Vec` instead of `join_all` to avoid the resize to the list introduced by `join_all`. So I added a new test case `Rust (tokio-for)` here:

```
use std::env;
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() {
    let args: Vec<String> = env::args().collect();
    let num_tasks = args[1].parse::<i32>().unwrap();
    let mut tasks = Vec::new();
    for _ in 0..num_tasks {
        tasks.push(sleep(Duration::from_secs(10)));
    }
    for task in tasks {
        task.await;
    }
}
```

Note that this won't work for `async_std` as it needs you to poll explicitly until the task being scheduled and executed, so switching to a loop will make it run the tasks sequentially.

Let's see what will happen with the new test code.

### Minimum Footprint

### 10K Tasks

### 100K Tasks

### 1M Tasks

This shrinks the cost of `Rust (tokio)` by about a half, which makes Rust the absolute lead in this benchmark. Good job, Rust.

