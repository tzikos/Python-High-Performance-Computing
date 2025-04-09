import sys
import pyarrow.parquet as pq

def precip(df):
    precip = float(df[df['parameterId'] == 'precip_past10min']['value'].sum())
    return precip

if __name__ == '__main__':
    fname = sys.argv[1]
    ver = sys.argv[2] if len(sys.argv) > 2 else 'chunks'
    assert ver in ['chunks', 'all']

    if ver == 'chunks':
        total = 0
        pf = pq.ParquetFile(fname)
        for i in range(pf.num_row_groups):
            group = pf.read_row_group(i)
            #group = pf.read_row_group(i, columns=['parameterId', 'value'])
            total += precip(group.to_pandas())
    else:
        df = pq.read_table(fname).to_pandas()
        #df = pq.read_table(fname,
        #                   columns=['parameterId', 'value']).to_pandas()
        total = precip(df)

    print(total)
