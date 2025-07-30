import pandas as pd

def load_dataset(file):
    df = pd.read_csv(file)
    if 'title' not in df.columns or 'overview' not in df.columns:
        raise ValueError("CSV must contain 'title' and 'overview' columns.")
    df.dropna(subset=['title', 'overview'], inplace=True)
    return df