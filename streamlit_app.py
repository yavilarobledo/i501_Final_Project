import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('cleaned_sample.csv')

# Title of the app
st.title('Apartments for Rent Analysis')

# Display the dataset
st.write('## Dataset')
st.write(df)

# Sidebar filters
st.sidebar.title('Filters')

# Filter by cityname
cityname_filter = st.sidebar.selectbox('Select City', df['cityname'].unique())

# Filter by pets_allowed
pets_filter = st.sidebar.selectbox('Pets Allowed?', ['All', 'Yes', 'No'])

# Filter by price
price_min = st.sidebar.slider('Minimum Price', int(df['price'].min()), int(df['price'].max()), int(df['price'].min()))
price_max = st.sidebar.slider('Maximum Price', int(df['price'].min()), int(df['price'].max()), int(df['price'].max()))

# Apply filters
filtered_df = df[(df['cityname'] == cityname_filter) & 
                 ((pets_filter == 'All') | (df['pets_allowed'] == pets_filter.lower())) &
                 (df['price'] >= price_min) & 
                 (df['price'] <= price_max)]

# Display filtered results
st.write('## Filtered Results')
st.write(filtered_df)
