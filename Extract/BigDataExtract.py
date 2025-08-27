import pandas as pd
from Config.ConfigBig import Config

class BigDataExtract:
    def __init__(self, csv_path: str = None):
        """
        Inicializa la clase con la ruta del archivo CSV
        """
        self.csv = csv_path if csv_path else Config.DATA_PATH
        self.data = None

    def queries(self):
        """
        Lee el archivo CSV y lo guarda en un DataFrame
        """
        try:
            self.data = pd.read_csv(self.csv)
            return self.data
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.csv}")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def response(self, rows: int = 5):
        """
        Devuelve las primeras filas del DataFrame cargado
        """
        if self.data is not None:
            return self.data.head(rows)
        else:
            print("Primero ejecuta queries() para cargar los datos.")
            return None
