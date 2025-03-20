import pandas as pd
import sys

def total_precip(path):
    df = pd.read_csv(path)
    # print('Dataframe loaded successfully')
    
    total = df[df['parameterId']=='precip_past10min']['value'].sum()
    
    # Return the total and the elapsed time in milliseconds
    return total

if __name__=='__main__':
    path = sys.argv[1]
    print(total_precip(path))