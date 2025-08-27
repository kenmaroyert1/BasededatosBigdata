import os

class ConfigBig:
    """
    Configuración global del ETL.
    """
    # Archivo por defecto (cámbialo si usas otro dataset)
    DATA_PATH = os.path.join(os.getcwd(), "Pokemon.csv")

    # Carpeta de salida
    OUTPUT_PATH = os.path.join(os.getcwd(), "output")

    # Opciones de limpieza
    DROP_DUPLICATES = True          # Eliminación de duplicados
    FILL_TEXT_DEFAULT = "Unknown"   # Texto por defecto para NA en columnas string
    TYPE2_DEFAULT = "None"          # Valor por defecto para 'Type 2' si existe
    NUMERIC_MISSING_STRATEGY = "zero"  # "zero" | "mean" | "median" | "mode"

    # Valores no deseados (se limpiarán de columnas de texto)
    UNWANTED_PATTERN = r"[^a-zA-Z0-9\s\-\.\']"  # elimina caracteres raros

    # Normalización de estadísticas en Transform
    NORMALIZE_STATS = True
