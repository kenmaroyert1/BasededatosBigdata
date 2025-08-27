import pandas as pd
from Config.ConfigBig import Config

class BigDataTransform:
    """
    Transformaciones genéricas y específicas de Pokémon.
    """

    @staticmethod
    def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
        """
        Renombra columnas comunes en el dataset de Pokémon para evitar espacios.
        (Se aplica solo si existen)
        """
        mapping = {
            "Sp. Atk": "Sp_Atk",
            "Sp. Def": "Sp_Def",
            "Type 1": "Type_1",
            "Type 2": "Type_2"
        }
        return df.rename(columns={k: v for k, v in mapping.items() if k in df.columns})

    @staticmethod
    def normalize_stats(df: pd.DataFrame) -> pd.DataFrame:
        """
        Normaliza stats [0,1] si la opción está activa.
        """
        if not Config.NORMALIZE_STATS:
            return df

        stats_cols = [c for c in ["Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Sp_Atk", "Sp_Def"] if c in df.columns]
        for col in stats_cols:
            col_min = df[col].min()
            col_max = df[col].max()
            # Evitar división por cero
            if pd.notna(col_min) and pd.notna(col_max) and col_max != col_min:
                df[col] = (df[col] - col_min) / (col_max - col_min)
        return df

    @staticmethod
    def one_hot_types(df: pd.DataFrame) -> pd.DataFrame:
        """
        (Opcional) Codifica tipos a variables dummies si las columnas existen.
        """
        for type_col in ["Type 1", "Type 2", "Type_1", "Type_2"]:
            if type_col in df.columns:
                dummies = pd.get_dummies(df[type_col], prefix=type_col.replace(" ", "_"))
                df = pd.concat([df.drop(columns=[type_col]), dummies], axis=1)
        return df
