# i501_Final_Project
# Apartment Rental Analysis Web App

## Abstract or Overview
The purpose of this web app is to shed light into the skyrocketing prices in rent. This app analyzes apartment rental prices across various locations, allowing users to filter by city, amentities, pets, square foot, and price range. There is a lack of bedroom/bathroom filter because this app aims at showing what is available based on user's affordability. For example, say I am someone needing an apartment in San Antonio that allows pets and is in the minimum pricing range and a max price of $1500, I only receive 34 apartments available. Another point I wish to make with this app is that as years go by everything racks up in price, so let's say I took my 34 apartments and clicked on the 'time' column and displayed the apartments from earliest posted to the latest apartment. The earliest apartment with those specified filters is a 2 bedroom, 2 bathroom apartment posted on December 9, 2018 that costs $1200, that includes the amenities of a fireplace, parking, pool, and a tennis court and is 1215 sq.ft. If I reclick the 'time' column I am then able to see the latest apartment posted that fits those filters. I browsed and found a similarly priced $1200 one bedroom one bathroom apartment recently posted on December 26, 2019 that only has the amenities of a pool and is 865 sq.ft. Therefore, we can see that today's apartment's are higher priced with less amenities and less square footage. 



## Audience
The main target audience for my streamlit project is for the general public to see how un-affordable housing is today, and how renters are not getting much bang for their buck. As a plus this app may benefit apartment hunters by easily being able to search for rentals that fit their needs. Another plus is that property managers can use the tool to analyze market trends, identify popular amenities, and set competitive prices.

## Data Description
The dataset used in this project contains information on various apartments, including location, amenities, rental price, square footage, and other key features. The data was cleaned and processed to ensure accuracy and remove inconsistencies.

### Data Fields
- **Location**: City, State, Address, Latitude, Longitude
- **Apartment Features**: Number of bedrooms, bathrooms, amenities
- **Rental Price**: Price, currency, fee, pets allowed
- **Other Details**: Time of data collection, source

## Algorithm Description
The app is filtering data based on user-selected criteria, including city, pets allowed, and price range. 

## Tools Used
- **Streamlit**: Used to create the web app, providing an easy way to build interactive user interfaces.
- **Pandas**: For data manipulation and filtering operations.
- **pydeck**: For map-based visualizations.
- **Python**: Primary programming language used for the backend logic.
- **GitHub**: Version control system used to track changes and collaborate.

## Ethical Concerns
Considering the sensitive nature of personal and location-based data, the following ethical considerations are addressed:
- **Privacy**: The data used does not contain personally identifiable information (PII) and respects user privacy.
- **Fairness**: The app does not discriminate against any group or individual based on their demographics.

