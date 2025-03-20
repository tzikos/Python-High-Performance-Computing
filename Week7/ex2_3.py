from pyarrow import csv

def pyarrow_load(filepath: str):
    """
    Loads a csv file and outputs a pyarrow table

    Arguments: filepath

    Returns: pyarrow table
    """

    df = csv.read_csv(filepath)
    print(df.nbytes)
    pd_df = df.to_pandas()
    print(pd_df.memory_usage(deep=True).sum())
    return pd_df

if __name__ == '__main__':
    # print(pyarrow_load('2023_01.csv'))    
    pyarrow_load('2023_01.csv')