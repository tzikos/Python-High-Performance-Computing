import pandas as pd

dfc = pd.read_csv('/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip',chunksize=100)

for df in dfc:
    print(df.columns)
    break