# Generating CS Text

There are three main ways to generate CS text:

### TCS Model

The Translation for Code-Switching (TCS) model generates high-quality code-switched text by adapting a state-of-the-art neural machine translation model. Starting from monolingual Hindi sentences, TCS uses a curriculum of pretraining steps, including synthetic code-switched text, to enhance the model's performance. The model relies on both supervised and unsupervised training objectives, utilizing monolingual text, parallel text, and synthetic code-switched sentences. TCS demonstrates significant improvements in tasks like language modeling and natural language inference by effectively capturing code-switching patterns​

`So TCS utilizes MT technqiues to capture CS patterns and create a hindi to hinglish model. It does not follow any explicit linguistic rules related to code-switching`

### GCM Toolkit

The GCM Toolkit is designed to generate synthetic code-mixed text by leveraging parallel data in two languages. It implements two linguistic theories of code-mixing: the Equivalence Constraint theory and the Matrix Language theory. The toolkit generates all possible code-mixed sentences for a given language pair and then samples the data to produce natural code-mixed sentences.

`So GCM relies on accepted linguistic theories to generate Code-Switched Data, not relying only on a learning model to`

### CoCoa