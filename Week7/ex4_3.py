import pandas as pd
from time import perf_counter_ns

df = pd.read_csv('/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip')
print('Dataframe loaded successfully')

def total_precip_vec(df):
    # Sample 5% of the data
    df = df.sample(frac=0.05)
    
    start = perf_counter_ns()
    total = df.loc[df['parameterId']=='precip_past10min', 'value'].sum()
    end = perf_counter_ns()
    
    # Return the total and the elapsed time in milliseconds
    return total, (end - start) / 1e9

if __name__=='__main__':
    print(total_precip_vec(df))