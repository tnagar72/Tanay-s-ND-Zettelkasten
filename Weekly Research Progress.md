# Weekly Research Progress


### Week 1 and 2 Log

1. Initial meeting with Dr. Chawla and C-CAS REU Meeting(Wednesday)
2. Meet Dohoen and understand his work (Wednesday)
3. Meeting Deng and Anna (Thursday)
4. Explored Code-Switched Text Articles from [genta’s repo](https://github.com/gentaiscool/code-switching-papers)
5. Come up with initial idea: Creation of Spa-Eng Code-switched dataset and begin reading and replicating code from [Tarunesh et al; 2021](https://arxiv.org/abs/2107.06483)

1. Found a few relevant seed spanglish datasets to use as seed data; Learnt basics of RNNs and stacked RNNs;
2. Learnt basics of LSTM’s; Built on last week’s idea with Grigorii and came up with current research proposal; Found additional metrics/benchmarks to evaluate on ([MLQA](https://github.com/facebookresearch/MLQA) and [PAWS-X](https://arxiv.org/abs/1908.11828))
3. Learnt about bi-directional LSTMs and GRUs; Coded a small next word-predictor
4. Worked from home. Spent time completing CPT formalities and read read papers from [Grigorii's List of Papers](Grigorii's%20List%20of%20Papers.md)
5. Spent time understanding code from [Tarunesh et al; 2021](https://arxiv.org/abs/2107.06483) and running it

### Week 3

1. Found two new ways of generating CS-text that were already published ([GCM](https://aclanthology.org/2021.eacl-demos.24.pdf) and [CoCoa](https://aclanthology.org/2022.emnlp-main.158/)); Each have their respective advantages and disadvantages. Check [Generating CS Text](Generating%20CS%20Text.md) for more info
2. Met Deng to discuss LLM OCR project; Discussed obstacle about Spa-Eng CS generation with Anna. (Will need to email Author of CoCoa to possibly ask for the code)
3. Currently going with GCM toolkit to generate spa-eng code; Spent time reading through [Zhang et al; 2023](https://aclanthology.org/2023.emnlp-main.491.pdf) to better understand all benchmarks used and create more testing examples

### Week 4

1. Finished CPT credit assignments for work authorization
2. Read through Translation Variant tasks of the Zhang et al. paper and planned how they can be implemented in our project too
3. Discussed draft pipeline and all aspects of the project with Anna (in prep for meeting with Dr. Chawla)
4. Reached out to CoCoa model team for code
5. Tested TE tasks on Llama 3 to get some baseline scores (check [week4code_readme](Week4code%2Fweek4code_readme.md) for more info)
6. Read CoCoa paper to get better understanding how to adjust CMI index for CS text output