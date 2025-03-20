import pandas as pd
from time import perf_counter_ns

df = pd.read_csv('/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip')
print('Dataframe loaded successfully')

def total_precip_apply(df):
    # Sample 5% of the data
    df = df.sample(frac=0.05)
    
    # Start the timer
    start = perf_counter_ns()
    
    # Define a function to apply to each row
    def process_row(row):
        if row['parameterId'] == 'precip_past10min':
            return row['value']
        return 0.0
    
    # Apply the function to each row and sum the results
    total = df.apply(process_row, axis=1).sum()
    
    # End the timer
    end = perf_counter_ns()
    
    # Return the total and the elapsed time in milliseconds
    return total, (end - start) / 1e9

if __name__=='__main__':
    print(total_precip_apply(df))