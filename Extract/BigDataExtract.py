import pandas as pd
from Config.ConfigBig import Config

class BigDataExtract:
    """
    Módulo de extracción. Lee CSV o Excel y devuelve un DataFrame.
    """

    def __init__(self, path: str | None = None):
        self.path = path or Config.DATA_PATH
        self.data = None

    def queries(self) -> pd.DataFrame:
        """
        Lee el archivo completo (CSV o XLSX).
        """
        try:
            if self.path.lower().endswith(".csv"):
                self.data = pd.read_csv(self.path)
            elif self.path.lower().endswith((".xlsx", ".xls")):
                self.data = pd.read_excel(self.path)
            else:
                raise ValueError("Formato no soportado. Usa .csv o .xlsx")
            return self.data
        except Exception as e:
            raise RuntimeError(f"Error al leer '{self.path}': {e}") from e

    def response(self, rows: int = 5):
        """
        Vista previa de las primeras filas.
        """
        if self.data is None:
            raise ValueError("Primero ejecuta queries() para cargar los datos.")
        return self.data.head(rows)
