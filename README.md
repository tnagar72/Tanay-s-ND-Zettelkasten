### Links

[Relevant Research Papers](Relevant%20Research%20Papers)

### TL;DR Research Proposal

Give small explanation, and then include links to research proposal, research progress, proposed timeline, ongoing literature review

Language Models perform worse on the same subjective tasks([Zhang et al.](https://aclanthology.org/2023.emnlp-main.491.pdf)) when the prompted in different languages. This bias is primarily caused by an imbalance in language data use for pre-training/training i.e. LMs perform worse for low-resource languages on subjective tasks.

It is worth exploring whether finetuning such language models on code-switched data (multiple languages interspersed in one sentence) can help increase performance of LMs on low-resource languages, while preserving their performance on high-resource languages used in pre-training and training (like English).

If possible, it would help reduce language bias, and promote language equity. Since this kind of bias is further seen in smaller language models ([Li et al.](https://arxiv.org/html/2404.11553v1)), a small fine-tuning step can help unbiased user-specific language models that perform better in multilingual classrooms, and are also generally better at interacting multilingually.

 Currently, there are three main ways of generating code-switched data (more info [here](Generating%20CS%20Text)). More info on Benchmarks on which we will evaluate baseline and fine-tuned llama can be found [here](Benchmarks).