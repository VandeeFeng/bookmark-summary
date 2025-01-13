# Why I Chose Common Lisp
- URL: https://blog.djhaskin.com/blog/why-i-chose-common-lisp/
- Added At: 2025-01-13 03:17:20
- [Link To Text](2025-01-13-why-i-chose-common-lisp_raw.md)

## Summary
**摘要**：
原作者Dan在他的文章《为什么我选择了Common Lisp——Dan的思考》中，详细阐述了他从Clojure转而选择Common Lisp的原因与经历。核心可总结为一系列转而采用新的LISP语言的驱动因素。在转投Common Lisp之前，Dan面临了Clojure中的多个挑战，如启动时间过长，社区对于这一问题的重视度不足，以及在实现快速原生执行文件时遇到的技术难度。这篇文章逻辑条理清晰，层层推进，阐述了每个标准要求以及是如何满足或超越自身过去的选择。

**要点总结**：
1. **满足快速启动需求的工具链**：
   - Common Lisp具备简洁且可行的方法来生成广泛应用程序的快速启动和独立执行文件，解决了启动时间太长的问题。

2. **跨平台兼容性**：
   - 包括Windows、Mac和Linux在内的多操作系统环境下的广泛支持，满足了Dan对于持久服务和跨平台应用开发的需求。

3. **连接到更大的声明式生态系统**：
   - Basic Foreign Function Interface (CFFI)的使用，使得它能够很好地与其他语言（如C）互动，特别是在发展基于大型社区的特定功能时。

4. **高性能运行时环境**：
   - SBCL作为最受欢迎的实现，提供了令人印象深刻的快速性能，满足Dan对执行效率的高要求。

5. **丰富的多线程支持**：
   - 通过Bordeaux-Threads、lparallel、cl-async和blackbird等多个库的支持，Common Lisp提供了强大的多线程能力，使得并发编程成为可能。

**摘录**主要内容依据逻辑顺序展开如下：

1. **与前一个项目Clojure的道别**：
   - 初期调用主要对Clojure启动费时的不满，以及后续尝试通过使用native-image方法加速启动，但最终仍未能实现快速的独立可执行文件，这一问题被认定为亲密编程语言的必要要求。在此背景下，Dan决定舍弃Clojure。

2. **转而探索新LISP语言的动机**：
   - 认出Clojure的欠缺后，Dan开始寻找新的LISP语言，列出了一系列所需特点，涵盖生成快速启动的可执行文件、兼容Vim和Emacs、支持多种操作系统、与广泛社区和生态系统相互融合，以及快速且高效运行的能力。

3. **Common Lisp的提出和使用**：
   - 经过Francky Pierret的链接介绍，以及自身对CLtLv2工具的学习和HyperSpec的深入阅读，Dan最终决定采用Common Lisp，特别是在了解其多编译器、快启动、以及社区活跃度后。

4. **探索Common Lisp的好奇心**：
   - 提供诸如JSON解析、SQLite支持、HTTP请求和功能性数据结构等实用功能的广泛库，以适应创建CLI工具的常见任务需求。同时，Dan提到在事件处理、/web开发、独立运行脚本、自动化和其他专有项目中使用的个案研究，阐明其使用范围和灵活性。

5. **喜悦和技术上的回报**：
   - 强烈的社区、活跃的用户、网络资源和其他社区提供的CLU和CL孤立模块，为开发者提供解决特定问题和挑战的途径。通过实践和应用，用户体验到了技术挑战被满足的喜悦，并在此过程期间，发现了关于标准、工具、技术和实践的独特见解。

**参考资料**：
- Clojure: [https://clojure.org/](https://clojure.org/)
- CLI: [https://github.com/djha-skin/degasolv](https://github.com/djha-skin/degasolv)
