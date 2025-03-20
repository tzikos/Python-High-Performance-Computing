import pandas as pd

df = pd.read_csv('/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip')

def reduce_dmi_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function that takes a df and returns a transformed df, optimized in terms of memory

    Arguments: df

    Returns: transformed_df
    """ 

    df['created'] = pd.to_datetime(df['created'], dayfirst=False, format="mixed")
    df['observed'] = pd.to_datetime(df['observed'], dayfirst=False, format='mixed')
    df['parameterId'] = df['parameterId'].astype('category')

    return df 

if __name__ == '__main__':
    print(reduce_dmi_df(df))
