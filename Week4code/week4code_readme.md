# Week 4 README

## Tasks that this folder is used for:

1. To evaluate commonSenseQA questions and knowledge access questions for Proof of Concept in Llama3:
	1. We use the 20 questions of the english version of the database as is
	2. We then use chatGPT api to translate to our target language (Hindi)
	3. We compare performance in both languages to see Llama performance. Previous Llama model did not work for certain tasks, so if this works, we can can set up baselines scores for our research with a bigger benchmark with more tasks, and then continue with generating CS and other parts of the research from there

2. English: Got 3 questions wrong out of 20.
3. Hindi: Got 5 questions wrong. So we still see the difference in performance here too. And we know that Llama is capable of performing this task too, unlike previous iterations.