import os
import pandas as pd
from Config.ConfigBig import Config

class BigDataLoad:
    @staticmethod
    def save_csv(df: pd.DataFrame, filename="cleaned_output.csv"):
        """
        Guarda el DataFrame como CSV en la carpeta de salida
        """
        os.makedirs(Config.OUTPUT_PATH, exist_ok=True)
        file_path = os.path.join(Config.OUTPUT_PATH, filename)
        df.to_csv(file_path, index=False)
        print(f"✅ Archivo guardado en: {file_path}")
