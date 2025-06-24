Title: Paper: Empirically derived evaluation requirements for responsible deployments of AI

URL Source: https://ferd.ca/notes/paper-empirically-derived-evaluation-requirements-for-responsible-deployments-of-ai.html

Markdown Content:
As if we weren't talking about AI enough these days, I've tripped upon this new paper by Dane A. Morey, Michael F. Rayo, and David D. Woods, titled [Empirically derived evaluation requirements for responsible deployments of AI in safety-critical settings](https://www.nature.com/articles/s41746-025-01784-y).

The paper covers a study where they ran experiments replicating the impact of AI augmentation nurses and nursing students' performances when doing remote monitoring of patients' vitals. I found this one interesting both on the results it got, but also on the experiment design and rationale they had for it all. I'm going to play around with the order a bit and start by covering the experiment and its results, some of the design elements I found compelling, and then their conclusions.

The charts used to do remote monitoring looked like the following:

![Image 1: Example patient case with AI recommendations and explanations. The display is split in 3 main areas, over a slider to select a time window to explore within the last 24h. On the left, there's a large red bar that shows an algorithmic prediction of emergency events predicted from 0 to 100% in the next 5 minutes. The central part is an oxygen saturation chart above a heart rate chart. On the right a series of smaller charts show patient information, labs, medication levels, blood saturation, blood pressure, respiration, and heart rate. As an AI explanation for the emergency percentage prediction, significant charts are overlaid with red color.](https://s3.us-east-2.amazonaws.com/ferd.ca/cohost/hbIJP82.png)

This variant is the one showing the basic data available to nurses, an AI's prediction, and the explanation of the AI's algorithmic choice. The big red bar on the left showing the AI's prediction of some emergency event happening in the next few minutes. The areas of the patient's health charts highlighted in red represent which data contributed to the AI predictions.

Other variants were used: without the explanations (only the prediction and chart), without the prediction (only red highlight explanations and chart), and the un-augmented approach (only basic charts).

These were shown to 450 nursing students and 12 licensed nurses, each seeing 10 randomized historical patient cases with randomized variants of charts. They had to score their own level of concern for the patients developing issues in the next five minutes, as quickly as possible, and then the authors analyzed the results to see the impact of AI augmentation on the final judgments. They specifically chose their 10 cases to cover a breadth of behaviors ranging from "the AI is very right" to "the AI is very wrong" to cover the whole spectrum.

![Image 2: Figure 2. Impacts of AI augmentation on human-AI performance. The magnitude of AI error was calculated as the absolute difference between AI recommendations and ground truth (0% for non-emergency patients or 100% for emergency patients). The impact of AI augmentation in the three AI-augmented conditions was calculated as the percentage difference between nurses’ concern with and without AI augmentation divided by the extent to which nurses differentiated emergency from non-emergency patients without AI augmentation. Positive and negative values correspond to changes in nurses’ concern which increased and decreased nurses’ differentiation of patient types, respectively. For emergency patients, results are separated by experimental condition: AI recommendation only (a), AI recommendation and explanation (b), and AI explanation only (c). For non emergency patients, results are similarly separated by experimental condition: AI recommendation only (d), AI recommendation and explanation (e), and AI explanation only (f). Each line represents the estimated marginal means from the generalized linear mixed effects model for nurses’ reported concern with 95% confidence intervals. Circles represent the mean of nurses’ concern in each case calculated from the unmodeled data, transformed with the same percentage difference calculation. Error bars correspond to 95% confidence intervals. Solid lines and closed circles represent the results of nurses using one of the three AI-augmented experimental conditions. Dashed lines and open circles represent the results of nurses using the baseline experimental condition without AI augmentation.](https://s3.us-east-2.amazonaws.com/ferd.ca/cohost/sTlZZFP.png)

They found multiple things. First, neither the nurses nor the AI were universally superior to the other. There were some cases where each did better or worse than the other. More significantly though, when the AI was right, the joint system where nurses were augmented by AI did better. When the AI was wrong, they did far worse.

> The magnitude of maximum degradation was nearly twice the magnitude of maximum improvement. When AI recommendations were most misleading, nurses’ reports of concern for emergency patients were indistinguishable from non-emergency patients, and vice versa. We observed a similar effect of lesser magnitude when nurses were presented with only AI explanations. These results suggest all forms of AI augmentation significantly influenced nurses’ perceptions of patient risk.

The authors particularly emphasize this aspect of risk:

> the strong influence of AI recommendations appeared to propagate AI vulnerabilities and induce dangerous confusions in cases which were otherwise routine for nurses.

They point out that a better algorithm does not necessarily yield better results. The critical part is how the nurses and the AI interact as a _joint system_. Optimizing algorithms may not optimize the joint system, and might instead harm it. They add that "human supervision may not fully mitigate the risk of all AI errors, even when provided with explanations".

Basically, if the AI recommendations can be persuasive and subject to error, so are the explanations. This is interesting because the theory generally goes that if AI can provide explanation behind its algorithms, then people can better audit and double-check them. Empirically, this does not seem to happen, and explanations may just make the recommendations sound more credible, and degrade overall system performance.

Now the 12 licensed nurses may have seemed like a low count out of the 450 students, but another finding here is that there was seemingly no strong relationships between nurse experience and the join human-AI performance. The authors also point out [a study done with radiologists](https://www.nature.com/articles/s41591-024-02850-w) that similarly found no reliable effect of experience (years of experience, subspecialty, or familiarity with AI tools) on the impact of AI assistance. The authors caution that some smaller differences may exist but may not be detectable to their study.

This is something I find interesting because there are direct parallels between these ideas and things we generally take for granted in software, such as people hoping to get better results out of [chain-of-thought prompts](https://en.wikipedia.org/wiki/Prompt_engineering#Chain-of-thought) or other model reasoning output to provide a similar "explainable AI" sort of mechanism. There's also a wildly repeated belief that risks of clumsy LLM results best prevented/handled by senior engineers and that junior engineers could be more error-prone with AI tools. Based on these studies, we should verify these claims for software, because neither might live up to expectations.

As the authors state:

> These risks are not unique to AI algorithms but rather fundamental risks of misleading information. Our findings add to growing concerns about the effectiveness of explainable AI to reliably help people recognize and recover from AI errors.
> 
> 
> Although different AI algorithms may produce different results, similar findings suggest susceptibility to AI errors might be a common feature of recommendation-centric human-AI architectures.

Put another way, if your AI interaction model is focused on recommendations, you may be stuck into this sort of joint performance pitfalls where AI errors are not corrected as much as amplified.

This brings us to one of my favorite parts of how they designed the experiment. The way they set it up meant to cover very good to very bad results for the AI. A common objection to this design is that we should also care for the frequency of events and errors seen to match reality. If you expect to be right 95% of the time, then it feels disingenuous to spend 50% of your scenarios on the 5% of cases that are wrong!

There's a two-part counter to that. First, they state:

> Improving the AI algorithm will likely reduce the _frequency_ of poor performance but it may not reduce the _range_ of possible performance or the consequences of poor performance. Therefore, improving the AI algorithm does not necessarily lessen the impact of AI errors. On the contrary, prior research has suggested recognizing and recovering from errors might be _more_ difficult if the frequency of error is rare.

Or put another way: if you want to look at error recovery, you have to look at errors, and the rarer the errors in the fields, the harder recovery ought to be for practitioners who encounter them less. The second part of the counter-argument is that aggregating the values in the overall accuracy rate ignores the weight of the consequences:

> If we had representatively sampled from the distribution of AI outputs or computed a weighted average of our results based on the probability of occurrence, the frequent but smaller benefits from correct AI recommendations might have outweighed the rare but larger costs from misleading AI recommendations. However, this aggregation misrepresents how healthcare practitioners are held accountable. Nurses are responsible for patients individually, not in the aggregate. Major harms are not excused by the accumulation of minor benefits.

Practitioners can be sued, may be penalized, have their license revoked, or [end up jailed](https://www.npr.org/sections/health-shots/2022/04/05/1090915329/why-nurses-are-raging-and-quitting-after-the-radonda-vaught-verdict) because of errors they are involved with. They are judged on the worst outcomes, in isolation. We should not, then, relax the criteria used for an AI to paper over that sort of responsibility, especially in a joint system where the human will likely _still_ get to pay for these errors.

I initially thought this was a bit of a weird study design, less realistic or relevant than it could be, but in the end I really, really appreciate this argument that aims to maintain proper alignment of real-world accountability and tool evaluation criteria.

This lines up with what their main points and conclusions are: AI capabilities alone do not guarantee a safe and effective joint human-AI system. To know if it is safe and effective, the two criteria they identify are:

1.   empirically measure the performance of people and AI together
2.   examine a range of challenging cases which produce a range of strong, mediocre, and poor AI performance.

As a conclusion, I like this little summary they had in the text:

> The goal of developing augmentative AI technologies should not be to improve AI algorithm performance, but rather to enable people to effectively accomplish cognitive work.

Isolated benchmarks might show the AI doing great, but it doesn't mean that the end result, where people use or are guided by AI as a joint system, are actually going to match the improvements seen in AI itself.
