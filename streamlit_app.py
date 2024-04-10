import os
import streamlit as st
from dotenv import load_dotenv
from b2 import B2



# ------------------------------------------------------
#                      APP CONSTANTS
# ------------------------------------------------------
REMOTE_DATA = 'apartments_for_rent_classified_100K.csv'


# ------------------------------------------------------
#                        CONFIG
# ------------------------------------------------------
load_dotenv()

# load Backblaze connection
b2 = B2(endpoint=os.environ['B2_ENDPOINT'],
        key_id=os.environ['B2_KEYID'],
        secret_key=os.environ['B2_APPKEY'])


# ------------------------------------------------------
#                        CACHING
# ------------------------------------------------------
@st.cache_data
def get_data():
    # collect data frame of reviews and their sentiment
    b2.set_bucket(os.environ['B2_BUCKETNAME'])
    df_apartment= b2.get_df(REMOTE_DATA)

    # average sentiment scores for the whole dataset
    benchmarks = df_coffee[['neg', 'neu', 'pos', 'compound']] \
                    .agg(['mean', 'median'])
    
    return df_coffee, benchmarks


@st.cache_resource



import streamlit as st
import pandas as pd


# Sidebar title
st.sidebar.title("Filters")

# Filter by location
locations = df_apartment['Location'].unique()
selected_location = st.sidebar.selectbox("Select Location", locations)

# Filter by number of bedrooms
bedrooms = df_apartment['NumberOfBedrooms'].unique()
selected_bedrooms = st.sidebar.selectbox("Select Number of Bedrooms", bedrooms)

# Filter by number of bathrooms
bathrooms = df_apartment['NumberOfBathrooms'].unique()
selected_bathrooms = st.sidebar.selectbox("Select Number of Bathrooms", bathrooms)

# Filter data based on selected criteria
filtered_df = df_apartment[(df_apartment['Location'] == selected_location) &
                 (df_apartment['NumberOfBedrooms'] == selected_bedrooms) &
                 (df_apartment['NumberOfBathrooms'] == selected_bathrooms)]

# Display filtered data
st.write(filtered_df)
