import pandas as pd
from time import perf_counter_ns
from tqdm import tqdm

df = pd.read_csv('/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip')
print('Dataframe loaded succesfully')

def total_precip(df):
    df = df.sample(frac=0.05)
    start = perf_counter_ns()
    total = 0.0
    for i in tqdm(range(len(df))):
        row = df.iloc[i]
        if row['parameterId'] == 'precip_past10min':
            total += row['value']
    end = perf_counter_ns()
    return total, (end-start)/1e9

if __name__=='__main__':
    print(total_precip(df))