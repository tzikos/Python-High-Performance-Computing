from pyarrow import csv
import pyarrow.compute as pc
import pyarrow as pa

# def dict_encode_all_str_columns(table):
#     new_arrays = []
#     for index, field in enumerate(table.schema):
#         if field.type == pa.string():
#             new_arr = pc.dictionary_encode(table.column(index))
#             new_arrays.append(new_arr)
#         else:
#             new_arrays.append(table.column(index))
#     return pa.Table.from_arrays(new_arrays, names=table.column_names)

def dict_encode_str_column(table, colname):
    new_arrays = []
    for index, field in enumerate(table.schema):
        if field.type == pa.string() and field.name == colname:
            new_arr = pc.dictionary_encode(table.column(index))
            new_arrays.append(new_arr)
        else:
            new_arrays.append(table.column(index))
    return pa.Table.from_arrays(new_arrays, names=table.column_names)

def pyarrow_load(filepath: str):
    """
    Loads a csv file and outputs a pyarrow table

    Arguments: filepath

    Returns: pyarrow table
    """
    var = 'parameterId'
    df = csv.read_csv(filepath)
    # Encode column as dictionary (automatically assigns unique integers)
    df = dict_encode_str_column(df, var)

    return df.nbytes

if __name__ == '__main__':
    # print(pyarrow_load('2023_01.csv'))    
    print(pyarrow_load('2023_01.csv'))