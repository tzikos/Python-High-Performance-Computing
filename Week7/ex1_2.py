import pandas as pd

df = pd.read_csv('/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip')

def df_memsize(df: pd.DataFrame) -> int:
    """
    Arguments: df
    
    Returns: size in bytes
    """

    mem = df.memory_usage(deep=True).sum()

    return mem


if __name__ == '__main__':
    print(df_memsize(df))
    print(df.head())
    
