import pandas as pd

# pd.read_csv('2023_01.csv') # approx 4.3s for unzipping plus 18s for reading
# pd.read_csv('/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip') # approx 11.3s for reading directly
pd.read_csv('./2023_01.csv')
