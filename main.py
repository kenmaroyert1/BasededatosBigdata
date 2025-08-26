from BigDataExtract import BigDataExtract

response1 = BigDataExtract("csv")
response1.queries()
print(response1.response())

from Extract.BigDataExtract import BigDataExtract
from Extract.Clean.DataCleaner import DataCleaner
from Load.BigDataLoad import BigDataLoad

def main():
    # Extraer CSV
    extractor = BigDataExtract("Pokemon.csv")
    df = extractor.extract()

    # Instanciar limpiador
    cleaner = DataCleaner(df)

    print("\n=== Reporte de nulos ===")
    print(cleaner.missing_report())

    print("\n=== Duplicados encontrados ===")
    print(cleaner.duplicates_report())

    # Aplicar estrategias
    cleaner.handle_missing(method="fill_mean")
    cleaner.remove_duplicates()

    print("\n=== Resumen final ===")
    print(cleaner.summary())

    # Guardar limpio
    loader = BigDataLoad("Pokemon_clean.csv")
    loader.load(cleaner.get_data())

if __name__ == "__main__":
    main()
