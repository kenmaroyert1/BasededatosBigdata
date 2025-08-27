import pandas as pd
from Config.ConfigBig import Config

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def drop_duplicates(self):
        if Config.DROP_DUPLICATES:
            self.df = self.df.drop_duplicates()
        return self

    def handle_missing(self):
        if Config.FILL_MISSING == "mean":
            self.df = self.df.fillna(self.df.mean(numeric_only=True))
        elif Config.FILL_MISSING == "median":
            self.df = self.df.fillna(self.df.median(numeric_only=True))
        elif Config.FILL_MISSING == "mode":
            self.df = self.df.fillna(self.df.mode().iloc[0])
        return self

    def clean_whitespace(self):
        str_cols = self.df.select_dtypes(include="object").columns
        for col in str_cols:
            self.df[col] = self.df[col].str.strip()
        return self

    def universal_clean(self):
        """
        Aplica todos los pasos de limpieza universales
        """
        return (
            self.drop_duplicates()
                .handle_missing()
                .clean_whitespace()
                .df
        )
