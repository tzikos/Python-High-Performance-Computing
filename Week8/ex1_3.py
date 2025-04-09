import sys
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

infile = sys.argv[1]
outfile = sys.argv[2]

df_chunks = pd.read_csv(
    infile,
    dtype={
        'parameterId': 'category'
    },
    chunksize=100_000
)

first = True
writer = None
for chunk in df_chunks:
    chunk_table = pa.Table.from_pandas(chunk)
    schema = chunk_table.schema
    if first:
        first = False
        writer = pq.ParquetWriter(outfile, schema=schema)
    writer.write_table(chunk_table)
writer.close()