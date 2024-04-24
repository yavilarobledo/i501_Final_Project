# data_processor.py

import pandas as pd
from data_utility import apply_filters

class DataProcessor:
    def __init__(self, df):
        self.df = df

    def filter_data(self, cityname, pets_allowed, price_min, price_max):
        return apply_filters(self.df, cityname, pets_allowed, price_min, price_max)

    def get_unique_cities(self):
        return self.df['cityname'].unique()

    def get_price_range(self):
        return int(self.df['price'].min()), int(self.df['price'].max())
