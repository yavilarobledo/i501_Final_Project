import streamlit as st
import pandas as pd


df = pd.read_csv("data/apartments_for_rent_classified_100K.csv")

# Sidebar title
st.sidebar.title("Filters")

# Filter by location
locations = df['Location'].unique()
selected_location = st.sidebar.selectbox("Select Location", locations)

# Filter by number of bedrooms
bedrooms = df['NumberOfBedrooms'].unique()
selected_bedrooms = st.sidebar.selectbox("Select Number of Bedrooms", bedrooms)

# Filter by number of bathrooms
bathrooms = df['NumberOfBathrooms'].unique()
selected_bathrooms = st.sidebar.selectbox("Select Number of Bathrooms", bathrooms)

# Filter data based on selected criteria
filtered_df = df[(df['Location'] == selected_location) &
                 (df['NumberOfBedrooms'] == selected_bedrooms) &
                 (df['NumberOfBathrooms'] == selected_bathrooms)]

# Display filtered data
st.write(filtered_df)
