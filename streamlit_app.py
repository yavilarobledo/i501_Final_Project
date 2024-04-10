import streamlit as st
import pandas as pd

# Attempt to read the CSV file with specified encoding
try:
    df = pd.read_csv("data/apartments_for_rent_classified_100K.csv", encoding='latin1')
    st.write("Successfully loaded the dataset.")
    st.write(df.head())  # Print first few rows for debugging
except Exception as e:
    st.write("Error:", e)  # Print any errors that occur during reading
