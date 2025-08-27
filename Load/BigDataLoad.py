import os
import pandas as pd
from Config.ConfigBig import Config

class BigDataLoad:
    """
    Módulo de carga: exporta DataFrames a archivos.
    """

    @staticmethod
    def save_csv(df: pd.DataFrame, filename: str = "cleaned_pokemon.csv") -> str:
        os.makedirs(Config.OUTPUT_PATH, exist_ok=True)
        path = os.path.join(Config.OUTPUT_PATH, filename)
        df.to_csv(path, index=False)
        print(f"✅ Archivo guardado en: {path}")
        return path

    @staticmethod
    def save_excel(df: pd.DataFrame, filename: str = "cleaned_pokemon.xlsx") -> str:
        os.makedirs(Config.OUTPUT_PATH, exist_ok=True)
        path = os.path.join(Config.OUTPUT_PATH, filename)
        df.to_excel(path, index=False)
        print(f"✅ Archivo guardado en: {path}")
        return path
