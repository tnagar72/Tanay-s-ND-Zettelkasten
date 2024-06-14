# README
### Links :)

[Research Proposal](Research%20Proposal.md) | 
[Weekly Research Progress](Weekly%20Research%20Progress.md) | 
[Relevant Research Papers](Relevant%20Research%20Papers.md) | 
[Generating CS Text](Generating%20CS%20Text.md) | 
[Benchmarks](Benchmarks.md) | 
[TL;DR Research Proposal](#TL;DR%20Research%20Proposal)
### TL;DR Research Proposal

Language Models perform worse on the same subjective, translation-variant tasks([Zhang et al; 2023](https://aclanthology.org/2023.emnlp-main.491.pdf))(more info in [Benchmarks](Benchmarks.md)) when prompted in different languages. This bias is primarily caused by an imbalance in language data use for pre-training/training i.e. LMs perform worse for low-resource languages on subjective tasks.

It is worth exploring whether finetuning such language models on code-switched data (multiple languages interspersed in one sentence) can help increase performance of LMs on low-resource languages, while preserving their performance on high-resource languages used in pre-training and training (like English).

If done, it would help reduce language bias, and promote language equity. Since this kind of bias is further seen in smaller language models ([Li et al; 2024](https://arxiv.org/html/2404.11553v1)), a small fine-tuning step can help user-specific language models perform better in multilingual classrooms, and also generally, behave better multilingually.

 Currently, there are three main ways of generating code-switched data (more info [here](Generating%20CS%20Text.md)). More info on Benchmarks on which we will evaluate baseline and fine-tuned llama can be found [here](Benchmarks.md).