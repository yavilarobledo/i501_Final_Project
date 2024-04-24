import pandas as pd
import os
import streamlit as st

@st.cache
def load_cached_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    return pd.read_csv(file_path)
