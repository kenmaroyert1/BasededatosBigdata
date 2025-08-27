# 📌 Proyecto ETL Universal con Python

Este proyecto lo realicé con el objetivo de crear un **pipeline ETL (Extract, Transform, Load)** totalmente modular y universal, que pueda trabajar con cualquier archivo CSV o Excel sin importar su estructura.

La idea principal fue organizar el código en diferentes módulos que representen cada fase del proceso: **Extracción, Limpieza, Transformación y Carga**, además de un archivo de configuración que permite cambiar parámetros sin necesidad de modificar el código principal.

---

## 🚀 Funcionalidades principales

✅ **Extract**

* Permite leer cualquier archivo `.csv` o `.xlsx`.
* Se puede configurar la ruta del archivo desde `Config/ConfigBig.py`.

✅ **Clean**

* Elimina duplicados en el dataset.
* Maneja valores nulos (`mean`, `median`, `mode` o ignorar).
* Limpia espacios innecesarios en columnas de texto.
* Todo esto se aplica de forma **universal a cualquier dataset**.

✅ **Transform**

* Normaliza todas las columnas numéricas en valores entre `0 y 1`.
* Permite renombrar columnas de manera sencilla.

✅ **Load**

* Guarda los datos procesados en un nuevo archivo CSV dentro de la carpeta `output/`.

✅ **main.py**

* Orquesta todo el proceso ETL.
* Se ejecuta en 4 pasos: **Extract → Clean → Transform → Load**.

---

## 📂 Estructura del proyecto

```
BASEDEDATOSBIGDATA/
│── Config/
│   └── ConfigBig.py
│
│── Extract/
│   ├── BigDataExtract.py
│   └── Clean/
│       └── Clean.py
│
│── Transform/
│   └── BigDataTransform.py
│
│── Load/
│   └── BigDataLoad.py
│
│── main.py
│── Pokemon.csv        # Dataset de prueba
│── requirements.txt
│── README.md
```

---

## ⚙️ Instalación y requisitos

1. Clonar este repositorio o copiar la estructura.
2. Crear un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

📌 `requirements.txt` contiene:

```txt
pandas
numpy
```

---

## ▶️ Uso

1. Coloca tu archivo `.csv` o `.xlsx` en la carpeta principal.
2. Ajusta la ruta en `Config/ConfigBig.py` si quieres usar otro archivo distinto a `Pokemon.csv`.
3. Ejecuta el flujo ETL:

```bash
python main.py
```

4. El resultado se guardará automáticamente en la carpeta `output/` como `cleaned_output.csv`.

---

## 📊 Ejemplo de salida

Si usamos el dataset de prueba `Pokemon.csv`, el flujo hará lo siguiente:

* Cargará todos los registros.
* Limpiará duplicados, valores faltantes y espacios.
* Normalizará las estadísticas (`HP`, `Attack`, `Defense`, etc.) entre 0 y 1.
* Guardará un archivo final en `output/cleaned_output.csv`.

---

## 🔮 Conclusión

Este proyecto me permitió practicar la **arquitectura de un ETL real**, modularizar el código en Python y crear un sistema **universal** que pueda trabajar con cualquier dataset.
En el futuro se le pueden agregar más transformaciones y hasta conexión con bases de datos para automatizar todo el proceso.

