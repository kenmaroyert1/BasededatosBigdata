from Extract.BigDataExtract import BigDataExtract
from Extract.Clean.Clean import DataCleaner
from Transform.BigDataTransform import BigDataTransform
from Load.BigDataLoad import BigDataLoad

def main():
    # 1. Extraer
    extractor = BigDataExtract()
    df = extractor.queries()
    print("📥 Datos cargados:")
    print(extractor.response())

    # 2. Limpiar
    cleaner = DataCleaner(df)
    df_clean = cleaner.universal_clean()
    print("\n🧹 Datos después de limpieza:")
    print(df_clean.head())

    # 3. Transformar (ejemplo: normalizar numéricos)
    df_transformed = BigDataTransform.normalize_numeric(df_clean)
    print("\n🔄 Datos transformados:")
    print(df_transformed.head())

    # 4. Cargar
    BigDataLoad.save_csv(df_transformed)

if __name__ == "__main__":
    main()
