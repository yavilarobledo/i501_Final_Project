import streamlit as st
import pandas as pd
from data_utility import load_data
from data_processor import DataProcessor

# Load data with error handling
try:
    df = load_data('cleaned_sample.csv')
except FileNotFoundError:
    st.error("Dataset not found. Please check the file path.")
    df = pd.DataFrame()  # fallback empty dataframe

# If data is loaded successfully, use the DataProcessor class to filter data
if not df.empty:
    processor = DataProcessor(df)

    # App title
    st.title('Apartments for Rent Analysis')

    # Sidebar filters
    st.sidebar.title('Filters')
    cityname_filter = st.sidebar.selectbox('Select City', processor.get_unique_cities())
    pets_filter = st.sidebar.selectbox('Pets Allowed?', ['All', 'Yes', 'No'])
    price_min, price_max = processor.get_price_range()

    min_price = st.sidebar.slider('Minimum Price', price_min, price_max, price_min)
    max_price = st.sidebar.slider('Maximum Price', price_min, price_max, price_max)

    # Apply filters
    filtered_data = processor.filter_data(cityname_filter, pets_filter, min_price, max_price)

    # Display filtered results
    st.write('## Filtered Results')
    st.write(filtered_data)
