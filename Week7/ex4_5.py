import pandas as pd
from time import perf_counter_ns

def total_precip(path):
    df = pd.read_csv(path)
    print('Dataframe loaded successfully')
    df = df.sample(frac=0.05)

    df.set_index('parameterId', inplace=True)
    start = perf_counter_ns()
    total = df.loc['precip_past10min','value'].sum()
    end = perf_counter_ns()
    # Return the total and the elapsed time in milliseconds
    return total, (end-start)/1e9

if __name__=='__main__':
    path = '/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip'
    print(total_precip(path))