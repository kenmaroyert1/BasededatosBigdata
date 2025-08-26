# 📊 Proyecto BaseDatosBigData

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** en Python para trabajar con datos masivos. La arquitectura sigue un enfoque modular, separando la configuración, extracción, transformación y carga de datos en carpetas específicas.

## 📂 Estructura del Proyecto

```
BaseDatosBigData/
│
├── Config/                  # Configuración general
│   ├── __init__.py
│   └── ConfigBig.py
│
├── Extract/                 # Módulo de extracción de datos
│   ├── __init__.py
│   └── BigDataExtract.py
│
├── Load/                    # Módulo de carga de datos
│   ├── __init__.py
│   └── BigDataLoad.py
│
├── Transform/               # Módulo de transformación de datos
│   ├── __init__.py
│   └── BigDataTransform.py
│
├── Pokemon.csv              # Dataset de ejemplo
├── main.py                  # Script principal de ejecución del pipeline
├── requirements.txt         # Dependencias necesarias
└── README.md                # Documentación del proyecto
```

## 🚀 Flujo ETL

1. **Extract (`Extract/`)**
   Aquí se define la lógica para **leer los datos desde distintas fuentes** (archivos CSV, bases de datos, APIs, etc.).
   Ejemplo: en este proyecto se usa el archivo `Pokemon.csv`.

2. **Transform (`Transform/`)**
   Aquí se realizan las operaciones de **limpieza, validación y transformación de datos**:

   * Normalización de columnas.
   * Eliminación de valores nulos o duplicados.
   * Estandarización de tipos de datos.
   * Aplicación de reglas de negocio.

3. **Load (`Load/`)**
   Finalmente, los datos procesados se **cargan en un destino** (base de datos, otro archivo CSV/Excel, o incluso almacenamiento en la nube).

4. **Config (`Config/`)**
   Contiene parámetros de configuración globales (rutas de archivos, credenciales, conexiones, etc.).

5. **main.py**
   Es el **punto de entrada del pipeline**. Desde aquí se ejecuta el flujo completo: **Extract → Transform → Load**.

## ⚙️ Instalación

1. Clona el repositorio:

   ```bash
   git clone <url-del-repo>
   cd BaseDatosBigData
   ```

2. Crea un entorno virtual y activa:

   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate      # En Windows
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecución

Ejecuta el pipeline completo desde `main.py`:

```bash
python main.py
```

## 📌 Próximos pasos

* Implementar un módulo de **cleaning** dentro de `Transform/BigDataTransform.py` para limpiar datos de Excel o CSV (ejemplo: `Pokemon.csv`).
* Agregar logs para seguimiento de errores.
* Conectar con una base de datos real para la etapa de `Load`.

