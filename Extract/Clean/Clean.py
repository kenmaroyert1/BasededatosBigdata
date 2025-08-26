import pandas as pd
import numpy as np

class DataCleaner:
    """
    Clase genérica para limpiar y analizar datasets (CSV o Excel).
    """

    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()
        self._original_shape = data.shape

    # ----------- ANÁLISIS -----------
    def missing_report(self) -> pd.DataFrame:
        """
        Devuelve un reporte de los valores faltantes por columna.
        """
        report = pd.DataFrame({
            "Nulos": self.data.isnull().sum(),
            "Porcentaje": (self.data.isnull().mean() * 100).round(2)
        })
        return report[report["Nulos"] > 0].sort_values(by="Nulos", ascending=False)

    def duplicates_report(self) -> int:
        """
        Devuelve el número de filas duplicadas.
        """
        return self.data.duplicated().sum()

    # ----------- ESTRATEGIAS DE LIMPIEZA -----------
    def handle_missing(self, method: str = "drop_rows", threshold: float = 0.5):
        """
        Maneja los valores nulos según la estrategia seleccionada.

        method:
            - drop_rows: elimina filas con nulos
            - drop_cols: elimina columnas con demasiados nulos
            - fill_mean: reemplaza numéricas con media, categóricas con moda
            - fill_const: rellena con un valor constante (ej: 0, "Desconocido")
        """
        if method == "drop_rows":
            self.data.dropna(inplace=True)

        elif method == "drop_cols":
            limit = int(len(self.data) * threshold)
            self.data.dropna(axis=1, thresh=limit, inplace=True)

        elif method == "fill_mean":
            num_cols = self.data.select_dtypes(include=[np.number]).columns
            cat_cols = self.data.select_dtypes(exclude=[np.number]).columns

            for col in num_cols:
                self.data[col].fillna(self.data[col].mean(), inplace=True)

            for col in cat_cols:
                if not self.data[col].mode().empty:
                    self.data[col].fillna(self.data[col].mode()[0], inplace=True)

        elif method == "fill_const":
            self.data.fillna(0, inplace=True)

        return self.data

    def remove_duplicates(self):
        """
        Elimina filas duplicadas del dataset.
        """
        self.data.drop_duplicates(inplace=True)
        return self.data

    # ----------- RESUMEN -----------
    def summary(self) -> dict:
        """
        Resumen del proceso de limpieza.
        """
        current_shape = self.data.shape
        return {
            "Filas iniciales": self._original_shape[0],
            "Columnas iniciales": self._original_shape[1],
            "Filas actuales": current_shape[0],
            "Columnas actuales": current_shape[1],
            "Duplicados restantes": self.duplicates_report(),
            "Nulos restantes": int(self.data.isnull().sum().sum())
        }

    def get_data(self) -> pd.DataFrame:
        """
        Retorna el dataset ya procesado.
        """
        return self.data
