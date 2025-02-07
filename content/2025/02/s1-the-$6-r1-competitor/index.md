---
title: S1- The $6 R1 Competitor-
date: 2025-02-07
extra:
  source: https://simonwillison.net/2025/Feb/5/s1-the-6-r1-competitor/
  original_title: S1- The $6 R1 Competitor-
---
## Summary
**摘要**:
这篇文章讨论了一篇题为《s1: Simple test-time scaling》的论文,文章描述了在Qwen2.5-32B-Instruct顶上进行调优的推理尺度化模型,仅需$6的预算,就能够实现对32B模型的性能提升。作者Tim Kellogg分享了这个实验的重点成果:经过削减后的56000个例子中最好的1000个就足够实现与32B模型相媲美的o1-preview性能。论文中提到的技术叫做“Budget forcing”,旨在通过抑制思考结束符的生成并增加等效的“Wait”字符串来鼓励模型自我反思。作者自建了一个Hugging Face上s1-32B模型以及配套的1000个样本数据集,并通过利用工具(如Ollama和DuckDB)进行数据处理和分析,最终体现出该模型在数学和科学领域的应用,其中包括15个作为示例的填字游戏题目。

**要点总结**:
- **成本效益:** 研究通过低成本($6)覆盖16个NVIDIA H100 GPU小时,展示了构建高性能推理模型的可能性。
- **简单训练数据集:** 通过对大量数据集的削减(56K到K级),模型仍能获取关键信息并达到显著性能。
- **Budget forcing技术:** 提出的策略利用自省机制来优化模型性能,通过抑制某特定标记符的生成,增加鼓励深思熟虑的信息。
- **案例验证:** 包含数学、科学领域的具体应用实例(例如填字游戏题目),展示模型在不同任务上的适应性与效果。
- **数据资源的获取与分析:** 整体流程从论文到模型资源、数据集的获取,及通过编程工具(DuckDB、sqlite-utils或Ollama)实现的数据处理和可视化分析,充分展现了跨领域数据应用的可行性。
## Full Content
Title: S1: The $6 R1 Competitor?

URL Source: https://simonwillison.net/2025/Feb/5/s1-the-6-r1-competitor/

Markdown Content:
**[S1: The $6 R1 Competitor?](https://timkellogg.me/blog/2025/02/03/s1)** Tim Kellogg shares his notes on a new paper, [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393), which describes an inference-scaling model fine-tuned on top of Qwen2.5-32B-Instruct for just $6 - the cost for 26 minutes on 16 NVIDIA H100 GPUs.

Tim highlight the most exciting result:

> After sifting their dataset of 56K examples down to just the best 1K, they found that the core 1K is all that's needed to achieve o1-preview performance on a 32B model.

The paper describes a technique called "Budget forcing":

> To enforce a minimum, we suppress the generation of the end-of-thinking token delimiter and optionally append the string “Wait” to the model’s current reasoning trace to encourage the model to reflect on its current generation

That's the same trick Theia Vogel described [a few weeks ago](https://simonwillison.net/2025/Jan/22/r1py/).

Here's the `s1-32B` model [on Hugging Face](https://huggingface.co/simplescaling/s1-32B). I found a GGUF version of it at [brittlewis12/s1-32B-GGUF](https://huggingface.co/brittlewis12/s1-32B-GGUF), which I ran using [Ollama](https://ollama.com/) like so:

```
ollama run hf.co/brittlewis12/s1-32B-GGUF:Q4_0
```

I also found those 1,000 samples on Hugging Face in the [simplescaling/s1K](https://huggingface.co/datasets/simplescaling/s1K) data repository there.

I used DuckDB to convert the parquet file to CSV (and turn one `VARCHAR[]` column into JSON):

```
COPY (
    SELECT 
      solution,
      question,
      cot_type,
      source_type,
      metadata,
      cot,
      json_array(thinking_trajectories) as thinking_trajectories,
      attempt
    FROM 's1k-00001.parquet'
) TO 'output.csv' (HEADER, DELIMITER ',');
```

Then I loaded that CSV into [sqlite-utils](https://sqlite-utils.datasette.io/) so I could use the `convert` command to turn a Python data structure into JSON using `json.dumps()` and `eval()`:

```
# Load into SQLite
sqlite-utils insert s1k.db s1k output.csv --csv
# Fix that column
sqlite-utils convert s1k.db s1u metadata 'json.dumps(eval(value))' --import json
# Dump that back out to CSV
sqlite-utils rows s1k.db s1k --csv > s1k.csv
```

Here's that CSV [in a Gist](https://gist.github.com/simonw/048385f27e351c11b488bd9737452fa7), which means I can [load it into Datasette Lite](https://lite.datasette.io/?install=datasette-pretty-json&csv=https://gist.githubusercontent.com/simonw/048385f27e351c11b488bd9737452fa7/raw/5270dacc5aa4a7385f9a6e3d691c81cf3595abc9/s1k.csv#/data/s1k?_facet=cot_type).

![Image 3: Screenshot of Datasette Lite showing cot_type 1, crossword 15, Link: 93, rowid: 93, solution: "### Answer: INCIDENT ROOM ### Explanation: Definition: investigators' facility **Anagram of**(... changes) NOTICED MINOR. Defn: ... in a police station." Question text: "Solve the crossword puzzle. You are presented with a clue as input and the number of letters in brackets." Clue: "Noticed minor changes in investigators' facility (8,4)" cot_type: crossword, source_type: 0xharib/xword1, metadata: { "instruction": "You are an expert level solver of cryptic crosswords. You are presented with a clue as input. Respond with the answer and explanation." }](https://static.simonwillison.net/static/2025/s1k.jpg)

It really is a tiny amount of training data. It's mostly math and science, but there are also [15 cryptic crossword examples](https://lite.datasette.io/?install=datasette-pretty-json&csv=https://gist.githubusercontent.com/simonw/048385f27e351c11b488bd9737452fa7/raw/5270dacc5aa4a7385f9a6e3d691c81cf3595abc9/s1k.csv#/data/s1k?_facet=cot_type&cot_type=crossword).

