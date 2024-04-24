# data_utils.py

import pandas as pd
import os

# Load data from a CSV file with error handling
def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    return pd.read_csv(file_path)

# Apply filters to the dataframe
def apply_filters(df, cityname, pets_allowed, price_min, price_max):
    return df[
        (df['cityname'] == cityname) &
        ((pets_allowed == 'All') | (df['pets_allowed'] == pets_allowed.lower())) &
        (df['price'] >= price_min) &
        (df['price'] <= price_max)
    ]
