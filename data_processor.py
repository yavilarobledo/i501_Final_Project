import pandas as pd
from data_utility import load_cached_data, apply_filters

class DataProcessor:
    def __init__(self, df):
        self.df = df

    def get_unique_cities(self):
        return self.df['cityname'].unique()

    def get_price_range(self):
        return int(self.df['price'].min()), int(self.df['price'].max())

    def get_square_feet_range(self):
        return int(self.df['square_feet'].min()), int(self.df['square_feet'].max())

    def get_unique_amenities(self):
        return self.df['amenities'].str.split(',').explode().unique()


    def filter_data(self, cityname, pets, min_price, max_price, min_square_feet, max_square_feet, amenities):
        # Basic filtering based on city name and price range
        filtered_data = self.df[
            (self.df['cityname'] == cityname) &
            (self.df['price'] >= min_price) &
            (self.df['price'] <= max_price) &
            (self.df['square_feet'] >= min_square_feet) &
            (self.df['square_feet'] <= max_square_feet)
        ]

        # filtering based on 'pets_allowed'
        if pets != 'All':
            if pets == 'None':
                # No pets allowed
                filtered_data = filtered_data[filtered_data['pets_allowed'].isnull() | (filtered_data['pets_allowed'] == 'no')]
            else:
                # Specific pet type (like 'cats' or 'dogs')
                filtered_data = filtered_data[filtered_data['pets_allowed'].str.lower() == pets.lower()]

        # If interested in specific amenities , filter by those as well
        if amenities:
            filtered_data = filtered_data[
                filtered_data['amenities'].str.contains('|'.join(amenities), case=False, na=False)
            ]

        return filtered_data

