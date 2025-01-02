import pandas as pd
import random
from constants import clickstream_data_headers

clickstream_data_path = "src/data-source/data/clickstream-enwiki-2024-10.tsv"
clickstream_sample_path = "src/data-source/data/clickstream-enwiki-2024-10_sample.csv"

n = 0
with open(clickstream_data_path, 'r') as f:
    row_count = sum(1 for _ in f) - 1  

sample_size = 10000

skip_rows = sorted(random.sample(range(1, row_count + 1), row_count - sample_size))

df_sampled = pd.read_csv(clickstream_data_path, 
                         skiprows=skip_rows,
                         sep='\t',
                         on_bad_lines='skip',
                         header=None,
                         names=clickstream_data_headers)

df_sampled.to_csv(clickstream_sample_path)

