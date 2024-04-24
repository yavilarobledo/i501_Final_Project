import streamlit as st
import pydeck as pdk
from data_utility import load_cached_data
from data_processor import DataProcessor

# Load data with caching
df = load_cached_data('cleaned_sample.csv')

# Initialize DataProcessor
processor = DataProcessor(df)

st.title('Apartments for Rent Analysis')

st.write('This project aims to analyze the ongoing apartment rent crisis by providing a Streamlit-based application that allows users to explore rental data with various filters. The primary focus is on affordability and desired amenities, offering a tool for stakeholders interested in the housing crisis and those seeking to understand the rental market dynamics. Through this app, users can gain insights into rental trends and identify factors contributing to the current crisis.')

#filters
st.sidebar.title('Filters')
cityname_filter = st.sidebar.selectbox('Select City', processor.get_unique_cities())
pets_filter = st.sidebar.selectbox('Pets Allowed?', ['All', 'Cats', 'Dogs', 'None'])

#square footage
square_feet_min, square_feet_max = processor.get_square_feet_range()
square_feet_min = st.sidebar.slider(
    'Minimum Square Footage', 
    square_feet_min, 
    square_feet_max, 
    square_feet_min
)
square_feet_max = st.sidebar.slider(
    'Maximum Square Footage', 
    square_feet_min, 
    square_feet_max, 
    square_feet_max
)

# Price filter
min_price, max_price = processor.get_price_range()
min_price = st.sidebar.slider('Minimum Price', min_price, max_price, min_price)
max_price = st.sidebar.slider('Maximum Price', min_price, max_price, max_price)

# Amenities filter
unique_amenities = processor.get_unique_amenities()
amenities_filter = st.sidebar.multiselect('Select Amenities', unique_amenities)

# Apply all filters
filtered_data = processor.filter_data(
    cityname_filter,
    pets_filter,
    min_price,
    max_price,
    square_feet_min,
    square_feet_max,
    amenities_filter
)

# Display filtered results
st.write('## Filtered Results')
st.write(filtered_data)

# Visualization Requirement: Price distribution
st.write('### Price Distribution')
st.bar_chart(filtered_data['price'])

# Visualization Suggestion from TA: Apartment locations map
locations = filtered_data[['latitude_deg', 'longitude_deg']]
layer = pdk.Layer(
    'ScatterplotLayer',
    data=locations,
    get_position=['longitude_deg', 'latitude_deg'],
    get_radius=100,
    get_fill_color=[255, 0, 0],
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=locations['latitude_deg'].mean(),
    longitude=locations['longitude_deg'].mean(),
    zoom=10,
    pitch=50,
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
