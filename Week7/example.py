import pandas as pd

df = pd.read_csv('/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip')

def summarize_columns(df):
    summary = pd.DataFrame([
        (col, df[col].dtype, df[col].nunique(dropna=True), df[col].memory_usage(deep=True) / (1024**2))
        for col in df.columns
    ], columns=['name', 'dtype', 'unique', 'size (MB)'])

    summary['size (MB)'] = summary['size (MB)'].round(3)  # Round for better readability

    total_size = df.memory_usage(deep=True).sum() / (1024**2)  # Convert to MB
    print(summary)
    print(f"Total size: {total_size:.3f} MB")

    return summary  # Return summary DataFrame for further analysis

if __name__ == '__main__':
    summarize_columns(df)