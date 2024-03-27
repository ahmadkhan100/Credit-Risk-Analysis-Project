import pandas as pd

def encode_categorical_variables(df, categorical_columns):
    """Function to encode categorical variables."""
    return pd.get_dummies(df, columns=categorical_columns)

def scale_features(df, numeric_columns):
    """Function to scale numeric features."""
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df
