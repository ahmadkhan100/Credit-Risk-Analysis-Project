
import pandas as pd

def clean_data(df):
    """Function to perform initial cleaning of the dataset."""
    # Example cleaning steps
    df.dropna(inplace=True)
    return df
