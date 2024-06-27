import pandas as pd
df = pd.read_parquet('/Users/tanaynagar/Documents/commonsense_qa/data')
df.to_csv('filename.csv')