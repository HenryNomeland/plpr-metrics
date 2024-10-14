import pandas as pd

input_csv = "Z:\ASUTransfer\FullCorpus\distilled_mfa_framewise_corpus.csv"
output_csv = ".\\testing2.csv"
chunk_size = 1000
df_chunk = pd.read_csv(input_csv, nrows=chunk_size)
df_chunk.to_csv(output_csv, index=False)
print(f"First {chunk_size} rows have been saved to {output_csv}")
