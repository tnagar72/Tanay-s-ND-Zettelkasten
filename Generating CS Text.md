# Generating CS Text

There are three main ways to generate CS text:
### TCS Model

The Translation for Code-Switching (TCS) model[^1] generates high-quality code-switched text by adapting a state-of-the-art neural machine translation model. Starting from monolingual Hindi sentences, TCS uses a curriculum of pretraining steps, including synthetic code-switched text, to enhance the model's performance. The model relies on both supervised and unsupervised training objectives, utilizing monolingual text, parallel text, and synthetic code-switched sentences. TCS demonstrates significant improvements in tasks like language modeling and natural language inference by effectively capturing code-switching patterns​

![](Pasted%20image%2020240614171754.png)

`So TCS utilizes MT technqiues to capture CS patterns and create a hindi to hinglish model. It does not follow any explicit linguistic rules related to code-switching`

### GCM Toolkit

The GCM Toolkit[^2] is designed to generate synthetic code-mixed text by leveraging parallel data in two languages. It implements two linguistic theories of code-mixing: the Equivalence Constraint theory and the Matrix Language theory. The toolkit generates all possible code-mixed sentences for a given language pair and then samples the data to produce natural code-mixed sentences.

`So GCM relies on accepted linguistic theories to generate Code-Switched Data, not relying only on a learning model to`

### CoCoa

CoCoa builds on the TCS model by adding encode and decoder side control so once can have fine-grained control on the CS text generation. However, the CoCoa paper[^3] does not provide its code.

![](Pasted%20image%2020240614171727.png)

`So we can either communicate with the authors of CoCoa and try to obtain this code or go forward with one of the other two techniques. Currently, I have decided to go forward with GCM, while we attempt to get in touch with the authors of the CoCoa paper and get their code.`

[^1]: https://arxiv.org/abs/2107.06483
[^2]: Mohd Sanad Zaki Rizvi, Anirudh Srinivasan, Tanuja Ganu, Monojit Choudhury, and Sunayana Sitaram. 2021. [GCM: A Toolkit for Generating Synthetic Code-mixed Text](https://aclanthology.org/2021.eacl-demos.24). In _Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations_, pages 205–211, Online. Association for Computational Linguistics.
[^3]: Sneha Mondal, Ritika ., Shreya Pathak, Preethi Jyothi, and Aravindan Raghuveer. 2022. [CoCoa: An Encoder-Decoder Model for Controllable Code-switched Generation](https://aclanthology.org/2022.emnlp-main.158). In _Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing_, pages 2466–2479, Abu Dhabi, United Arab Emirates. Association for Computational Linguistics.