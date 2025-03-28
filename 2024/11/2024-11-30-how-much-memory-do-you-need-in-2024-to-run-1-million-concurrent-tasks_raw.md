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
