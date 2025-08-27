import os

class Config:
    # Ruta del dataset (cambia el nombre del CSV según corresponda)
    DATA_PATH = os.path.join(os.getcwd(), "Pokemon.csv")
    
    # Carpeta de salida
    OUTPUT_PATH = os.path.join(os.getcwd(), "output")

    # Opciones de limpieza
    DROP_DUPLICATES = True
    FILL_MISSING = "mean"  # opciones: "mean", "median", "mode", None
