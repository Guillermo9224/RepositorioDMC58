# TelcoCustomerChurn — 

> Caso de Estudio N°2 · Especialización Python for Analytics  
> Autor: **Guillermo Carrasco** · Año: 2026

## Descripción del proyecto

Aplicación interactiva construida con **Streamlit** para el Análisis Exploratorio
de Datos (EDA) del dataset `TelcoCustomerChurn.csv`.

El objetivo es identificar los **patrones y factores asociados a la fuga de clientes**
(*churn*) de una empresa de telecomunicaciones, aplicando de manera integrada
los conceptos de la especialización: Python, Pandas, NumPy, Matplotlib, Seaborn,
estadística descriptiva y Programación Orientada a Objetos.

## Estructura de la aplicación

| Módulo | Descripción |
|---|---|
| 🏠 Home | Presentación del proyecto, autor y dataset |
| 📂 Carga del Dataset | `st.file_uploader`, vista previa, dimensiones |
| 🔍 EDA — Exploración | info general, clasificación, estadísticas, nulos, distribuciones |
| 📊 EDA — Visualizaciones | categóricas, bivariados, hallazgos clave |
| 🎛️ Análisis Dinámico | Ítem 9: selectbox, multiselect, slider, filtros interactivos |
| 🏁 Conclusiones | 5 conclusiones orientadas a decisiones de retención |

## Tecnologías utilizadas

- **Python**
- **Streamlit** — interfaz web interactiva
- **Pandas** — manipulación y análisis de datos
- **NumPy** — cálculo numérico
- **Matplotlib / Seaborn** — visualización
- **SciPy** — KDE y estadística

## Instrucciones de ejecución

### 1. Ejecutar la aplicación
```
streamlit run app.py
```

### 2. Cargar el dataset
En el módulo **"📂 Carga del Dataset"**, usa el uploader para cargar
`TelcoCustomerChurn.csv`.

## Dataset

El archivo `TelcoCustomerChurn.csv` contiene **7,043 registros** y **21 variables**
sobre clientes de una empresa de telecomunicaciones:
perfil demográfico, servicios contratados, facturación y estado de churn.


## 🔗 Links

- 🌐 App desplegada: `https://repositoriodmc58-jgca.streamlit.app/`
- 📁 Repositorio: `https://github.com/Guillermo9224/RepositorioDMC58/edit/main/README.md`

