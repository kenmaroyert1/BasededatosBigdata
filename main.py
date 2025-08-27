from Extract.BigDataExtract import BigDataExtract
from Extract.Clean.Clean import DataCleaner
from Transform.BigDataTransform import BigDataTransform
from Load.BigDataLoad import BigDataLoad

def main():
    # 1) EXTRACT
    extractor = BigDataExtract()  # usa Config.DATA_PATH por defecto
    df_raw = extractor.queries()
    print("📥 Datos extraídos. Vista previa:")
    print(extractor.response())

    # 2) CLEAN
    cleaner = DataCleaner(df_raw)
    df_clean = cleaner.universal_clean()
    print("\n🧹 Datos limpios. Vista previa:")
    print(df_clean.head())

    # 3) TRANSFORM
    df_trans = BigDataTransform.rename_columns(df_clean)
    df_trans = BigDataTransform.normalize_stats(df_trans)
    # Si quieres codificar tipos a dummies, descomenta:
    # df_trans = BigDataTransform.one_hot_types(df_trans)

    print("\n🔧 Datos transformados. Vista previa:")
    print(df_trans.head())

    # 4) LOAD
    BigDataLoad.save_csv(df_trans, "cleaned_pokemon.csv")
    # BigDataLoad.save_excel(df_trans, "cleaned_pokemon.xlsx")

if __name__ == "__main__":
    main()
