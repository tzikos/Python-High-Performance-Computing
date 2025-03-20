from pyarrow import csv

def pyarrow_load(filepath: str):
    """
    Loads a csv file and outputs a pyarrow table

    Arguments: filepath

    Returns: pyarrow table
    """

    df = csv.read_csv(filepath)

    return df.to_pandas()

if __name__ == '__main__':
    print(pyarrow_load('2023_01.csv'))