**Attention mechanism:**

LSTM: [https://deeplearning.cs.cmu.edu/F23/document/readings/LSTM.pdf](https://www.google.com/url?q=https://deeplearning.cs.cmu.edu/F23/document/readings/LSTM.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2DrSsklmocweX6daK95TRj "https://www.google.com/url?q=https://deeplearning.cs.cmu.edu/F23/document/readings/LSTM.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2DrSsklmocweX6daK95TRj")   

Seq2Seq: [https://arxiv.org/pdf/1409.3215](https://www.google.com/url?q=https://arxiv.org/pdf/1409.3215&source=gmail-imap&ust=1718120964000000&usg=AOvVaw1eqM_nKSz9FoQXqdXyBUze "https://www.google.com/url?q=https://arxiv.org/pdf/1409.3215&source=gmail-imap&ust=1718120964000000&usg=AOvVaw1eqM_nKSz9FoQXqdXyBUze") (hey that's Ilya here, will go on to create OpenAI)

BiLSTM: [https://arxiv.org/pdf/1508.01991](https://www.google.com/url?q=https://arxiv.org/pdf/1508.01991&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2nEm5Ol6QiRHxZQOa4yK9q "https://www.google.com/url?q=https://arxiv.org/pdf/1508.01991&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2nEm5Ol6QiRHxZQOa4yK9q") (also see ELMo as an example application: [https://arxiv.org/pdf/1802.05365](https://www.google.com/url?q=https://arxiv.org/pdf/1802.05365&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2BDBLbofX-uCGwMwoWpcO- "https://www.google.com/url?q=https://arxiv.org/pdf/1802.05365&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2BDBLbofX-uCGwMwoWpcO-"))

Attention as an addon to BiLSTM (that's the paper that introduced attention as a concept for language modeling): [https://arxiv.org/pdf/1409.0473](https://www.google.com/url?q=https://arxiv.org/pdf/1409.0473&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3t1PlutQQqcg2QmOHmgjlS "https://www.google.com/url?q=https://arxiv.org/pdf/1409.0473&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3t1PlutQQqcg2QmOHmgjlS")

Attention is all you need (Transformer invented here): [https://arxiv.org/pdf/1706.03762](https://www.google.com/url?q=https://arxiv.org/pdf/1706.03762&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2CggG8iwEzzXFY8WoKWCMd "https://www.google.com/url?q=https://arxiv.org/pdf/1706.03762&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2CggG8iwEzzXFY8WoKWCMd")

**Encoder-only models:**

BERT (encoder only): [https://arxiv.org/pdf/1810.04805](https://www.google.com/url?q=https://arxiv.org/pdf/1810.04805&source=gmail-imap&ust=1718120964000000&usg=AOvVaw36-VfK0j6hMAyd5taO0iQA "https://www.google.com/url?q=https://arxiv.org/pdf/1810.04805&source=gmail-imap&ust=1718120964000000&usg=AOvVaw36-VfK0j6hMAyd5taO0iQA") - this one kinda started the whole thing  

There are architectural advancements made with this: [https://arxiv.org/pdf/2006.03654](https://www.google.com/url?q=https://arxiv.org/pdf/2006.03654&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3y6wz68ljlCl4dNhR1M2AZ "https://www.google.com/url?q=https://arxiv.org/pdf/2006.03654&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3y6wz68ljlCl4dNhR1M2AZ"), but a lot of work goes into domain specialization, e.g. [https://arxiv.org/pdf/1903.10676](https://www.google.com/url?q=https://arxiv.org/pdf/1903.10676&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3VXxA3ZzoqTOPPXvfQlGP0 "https://www.google.com/url?q=https://arxiv.org/pdf/1903.10676&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3VXxA3ZzoqTOPPXvfQlGP0") (SciBERT), [https://aclanthology.org/2022.naacl-main.400.pdf](https://www.google.com/url?q=https://aclanthology.org/2022.naacl-main.400.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw1GiWGwAPAUdjzdj_5GwrbV "https://www.google.com/url?q=https://aclanthology.org/2022.naacl-main.400.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw1GiWGwAPAUdjzdj_5GwrbV") (ConfliBERT), there's a lot more.

  

**Decoder-only models:**

The paper that introduced decoder only: [https://arxiv.org/pdf/1801.10198](https://www.google.com/url?q=https://arxiv.org/pdf/1801.10198&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2CjD0OYUr96VToElTwlODt "https://www.google.com/url?q=https://arxiv.org/pdf/1801.10198&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2CjD0OYUr96VToElTwlODt")

  

These are done by OpenAI and basically illustrate the growth of this decoder only architecture without big architectural changes:  
GPT-1 (decoder only): [https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf](https://www.google.com/url?q=https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw12dHXkd7s2IoMjv14IYyX9 "https://www.google.com/url?q=https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw12dHXkd7s2IoMjv14IYyX9")

GPT-2 (decoder only): [https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf](https://www.google.com/url?q=https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2UeruEMWLHoAnmzunw73Ti "https://www.google.com/url?q=https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2UeruEMWLHoAnmzunw73Ti")

GPT-3 (decoder only): [https://arxiv.org/pdf/2005.14165](https://www.google.com/url?q=https://arxiv.org/pdf/2005.14165&source=gmail-imap&ust=1718120964000000&usg=AOvVaw1rYlgb5xl2nz96rWxkzqCv "https://www.google.com/url?q=https://arxiv.org/pdf/2005.14165&source=gmail-imap&ust=1718120964000000&usg=AOvVaw1rYlgb5xl2nz96rWxkzqCv") (there are some changes in this one, they added residual connections a la ResNet)

There's an awesome video by Karpathy where he shows all this in code: [https://www.youtube.com/watch?v=kCc8FmEb1nY](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkCc8FmEb1nY&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0uM2Hpl9_p0FEIsVJ3Whzt "https://www.google.com/url?q=https://www.youtube.com/watch?v%3DkCc8FmEb1nY&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0uM2Hpl9_p0FEIsVJ3Whzt")

  

LLAMA papers are done by Meta and talk a lot about more advanced concepts for training/fine-tuning (also some architecture changes):

LLAMA 1: [https://arxiv.org/pdf/2302.13971](https://www.google.com/url?q=https://arxiv.org/pdf/2302.13971&source=gmail-imap&ust=1718120964000000&usg=AOvVaw32ECMIZ5Dqiz03-Fjzwb_T "https://www.google.com/url?q=https://arxiv.org/pdf/2302.13971&source=gmail-imap&ust=1718120964000000&usg=AOvVaw32ECMIZ5Dqiz03-Fjzwb_T")

LLAMA 2: [https://arxiv.org/pdf/2307.09288](https://www.google.com/url?q=https://arxiv.org/pdf/2307.09288&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2tdiaPUyr6_OU7eMhY4s4b "https://www.google.com/url?q=https://arxiv.org/pdf/2307.09288&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2tdiaPUyr6_OU7eMhY4s4b")

  

Instruction tuning (by giving specifically constructed prompts during fine-tuning we can improve performance): [https://arxiv.org/pdf/2109.01652](https://www.google.com/url?q=https://arxiv.org/pdf/2109.01652&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3YyBlOP9bnHLJXrbvR8lkw "https://www.google.com/url?q=https://arxiv.org/pdf/2109.01652&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3YyBlOP9bnHLJXrbvR8lkw")

RLHF (humans look at output and say good/bad, model learns from that): [https://arxiv.org/pdf/1706.03741](https://www.google.com/url?q=https://arxiv.org/pdf/1706.03741&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3hmLr3QjrXDZ76hfOsS4Pf "https://www.google.com/url?q=https://arxiv.org/pdf/1706.03741&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3hmLr3QjrXDZ76hfOsS4Pf"), [https://arxiv.org/pdf/2203.02155](https://www.google.com/url?q=https://arxiv.org/pdf/2203.02155&source=gmail-imap&ust=1718120964000000&usg=AOvVaw1JmUf4iKmSpjwoyJucpIz0 "https://www.google.com/url?q=https://arxiv.org/pdf/2203.02155&source=gmail-imap&ust=1718120964000000&usg=AOvVaw1JmUf4iKmSpjwoyJucpIz0")

  

**Fine-tuning:**

Model quantization (how to make LLMs smaller and useful on consumer-grada GPUs, is done a lot): [https://www.ijcai.org/Proceedings/2020/0520.pdf](https://www.google.com/url?q=https://www.ijcai.org/Proceedings/2020/0520.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2GTfl--kBVVM21wFrPaWwL "https://www.google.com/url?q=https://www.ijcai.org/Proceedings/2020/0520.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2GTfl--kBVVM21wFrPaWwL")

How fine-tuning is done in practice: [https://arxiv.org/pdf/2106.09685](https://www.google.com/url?q=https://arxiv.org/pdf/2106.09685&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0_1JNbofMGsY6_9JeKc7Dn "https://www.google.com/url?q=https://arxiv.org/pdf/2106.09685&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0_1JNbofMGsY6_9JeKc7Dn")

How we are doing it here, because we don't have a ton of compute: [https://arxiv.org/pdf/2305.14314](https://www.google.com/url?q=https://arxiv.org/pdf/2305.14314&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0RoHB1EaEuT8htuQVrXesU "https://www.google.com/url?q=https://arxiv.org/pdf/2305.14314&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0RoHB1EaEuT8htuQVrXesU")

  

**Other stuff (this is more for reference):**

Very large context transformers (something like this is probably done for newer Gemimis by Google): [https://arxiv.org/pdf/2203.08913](https://www.google.com/url?q=https://arxiv.org/pdf/2203.08913&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0nhPt97RzZFORsp2fyUKsk "https://www.google.com/url?q=https://arxiv.org/pdf/2203.08913&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0nhPt97RzZFORsp2fyUKsk"), [https://arxiv.org/pdf/2310.01889](https://www.google.com/url?q=https://arxiv.org/pdf/2310.01889&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0_KSG-qj04ejKpo_7W-qKG "https://www.google.com/url?q=https://arxiv.org/pdf/2310.01889&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0_KSG-qj04ejKpo_7W-qKG"), [https://arxiv.org/pdf/2109.00301](https://www.google.com/url?q=https://arxiv.org/pdf/2109.00301&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2J9juCGLkmIP9Ms5d7kFrj "https://www.google.com/url?q=https://arxiv.org/pdf/2109.00301&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2J9juCGLkmIP9Ms5d7kFrj"), [https://arxiv.org/pdf/2403.11901](https://www.google.com/url?q=https://arxiv.org/pdf/2403.11901&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3yR68WsM2ZF7LR949mHIew "https://www.google.com/url?q=https://arxiv.org/pdf/2403.11901&source=gmail-imap&ust=1718120964000000&usg=AOvVaw3yR68WsM2ZF7LR949mHIew")

MoE models (something like this was/is rumored to be used for GPT-4): [https://arxiv.org/pdf/2202.08906](https://www.google.com/url?q=https://arxiv.org/pdf/2202.08906&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0Hysr4tAiO14Bfx-eUIP5f "https://www.google.com/url?q=https://arxiv.org/pdf/2202.08906&source=gmail-imap&ust=1718120964000000&usg=AOvVaw0Hysr4tAiO14Bfx-eUIP5f"), [https://arxiv.org/pdf/2101.03961](https://www.google.com/url?q=https://arxiv.org/pdf/2101.03961&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2vv6Os7xIJFr1abMtJqJ7w "https://www.google.com/url?q=https://arxiv.org/pdf/2101.03961&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2vv6Os7xIJFr1abMtJqJ7w"), [https://aclanthology.org/2022.naacl-main.407.pdf](https://www.google.com/url?q=https://aclanthology.org/2022.naacl-main.407.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2eJvNuGJpvQaIBYqhxQL8I "https://www.google.com/url?q=https://aclanthology.org/2022.naacl-main.407.pdf&source=gmail-imap&ust=1718120964000000&usg=AOvVaw2eJvNuGJpvQaIBYqhxQL8I")

The overview: [https://arxiv.org/pdf/2307.06435](https://www.google.com/url?q=https://arxiv.org/pdf/2307.06435&source=gmail-imap&ust=1718120964000000&usg=AOvVaw13_tQRKq_lXtOnxcdYXCQR "https://www.google.com/url?q=https://arxiv.org/pdf/2307.06435&source=gmail-imap&ust=1718120964000000&usg=AOvVaw13_tQRKq_lXtOnxcdYXCQR")