import pandas as pd

class BigDataTransform:
    @staticmethod
    def normalize_numeric(df: pd.DataFrame):
        """
        Normaliza columnas numéricas entre 0 y 1
        """
        numeric_cols = df.select_dtypes(include="number").columns
        df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].min()) / (df[numeric_cols].max() - df[numeric_cols].min())
        return df

    @staticmethod
    def rename_columns(df: pd.DataFrame, mapping: dict):
        """
        Renombra columnas con un diccionario
        """
        return df.rename(columns=mapping)
