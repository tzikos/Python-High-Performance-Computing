import sys
import pyarrow.parquet as pq
from pyarrow import csv

# table = csv.read_csv('')

# pq.write_table(table, '')

# pq.read_table('')

def load_csv_save_pq(path: str) -> None:
    
    table = csv.read_csv(path)
    pq.write_table(table, 'file.parquet')

    return None

if __name__=='__main__':
    path = sys.argv[1]
    load_csv_save_pq(path)
