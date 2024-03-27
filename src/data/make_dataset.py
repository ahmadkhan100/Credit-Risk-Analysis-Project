
import pandas as pd

def load_data(path):
    """Function to load data from a CSV file."""
    return pd.read_csv(path)

def save_data(df, path):
    """Function to save DataFrame to a CSV file."""
    df.to_csv(path, index=False)
