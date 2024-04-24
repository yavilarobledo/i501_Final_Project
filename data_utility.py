import pandas as pd
import os
import streamlit as st

@st.cache
def load_cached_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    return pd.read_csv(file_path)


def apply_filters(df, filters):
    """
    Apply a set of filters to a DataFrame.

    :param df: DataFrame to apply filters to.
    :param filters: Dictionary with filter parameters.
    :return: Filtered DataFrame.
    """
    # Example filters
    if 'cityname' in filters:
        df = df[df['cityname'] == filters['cityname']]
    if 'pets_allowed' in filters:
        if filters['pets_allowed'] != 'All':
            df = df[df['pets_allowed'] == filters['pets_allowed'].lower()]
    if 'price_range' in filters:
        min_price, max_price = filters['price_range']
        df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]

    return df
