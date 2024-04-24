import pandas as pd
from data_utility import load_cached_data, apply_filters

class DataProcessor:
    def __init__(self, df):
        try:
            self.df = df
            if df.empty:
                raise ValueError("DataFrame is empty")
        except ValueError as ve:
            raise ve  # Re-raise ValueError if DataFrame is empty
        except Exception as e:
            raise RuntimeError(f"Error initializing DataProcessor: {e}")

    def filter_data(self, cityname, pets, min_price, max_price, min_square_feet, max_square_feet, amenities):
        try:
            filtered_data = self.df[
                (self.df['cityname'] == cityname) &
                ((pets == 'All') | (self.df['pets_allowed'].str.lower() == pets.lower())) &
                (self.df['price'] >= min_price) &
                (self.df['price'] <= max_price) &
                (self.df['square_feet'] >= min_square_feet) &
                (self.df['square_feet'] <= max_square_feet)
            ]

            # If amenities are given, ensure that they are present in the DataFrame
            if amenities:
                filtered_data = filtered_data[
                    filtered_data['amenities'].str.contains('|'.join(amenities), case=False, na=False)
                ]

            if filtered_data.empty:
                st.warning("No results found with the selected filters.")

            return filtered_data

        except KeyError as ke:
            raise RuntimeError(f"Missing key in DataFrame: {ke}")
        except Exception as e:
            raise RuntimeError(f"Error during data filtering: {e}")
