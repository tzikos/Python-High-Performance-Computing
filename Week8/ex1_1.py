import sys
import pandas as pd
from tqdm import tqdm

def load_calc_precip(data_path: str, chunk_size: int) -> None:

    dfc = pd.read_csv(data_path, chunksize=chunk_size)

    total_precip = 0.0
    for df in dfc:
        total_precip += df.loc[df['parameterId'] == 'precip_past10min','value'].sum()

    print(total_precip)

    return None

if __name__=='__main__':

    data_path = sys.argv[1]
    chunk_size = int(sys.argv[2])

    load_calc_precip(data_path=data_path, chunk_size=chunk_size)