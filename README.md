# 📡 TelcoCustomerChurn — EDA App

> Caso de Estudio N°2 · Especialización Python for Analytics  
> Autor: **Guillermo** · Año: 2025

## 📋 Descripción del proyecto

Aplicación interactiva construida con **Streamlit** para el Análisis Exploratorio
de Datos (EDA) del dataset `TelcoCustomerChurn.csv`.

El objetivo es identificar los **patrones y factores asociados a la fuga de clientes**
(*churn*) de una empresa de telecomunicaciones, aplicando de manera integrada
los conceptos de la especialización: Python, Pandas, NumPy, Matplotlib, Seaborn,
estadística descriptiva y Programación Orientada a Objetos.

## 🏗️ Estructura de la aplicación

| Módulo | Descripción |
|---|---|
| 🏠 Home | Presentación del proyecto, autor y dataset |
| 📂 Carga del Dataset | `st.file_uploader`, vista previa, dimensiones |
| 🔍 EDA — Exploración | Ítems 1–5: info general, clasificación, estadísticas, nulos, distribuciones |
| 📊 EDA — Visualizaciones | Ítems 6–8 + 10: categóricas, bivariados, hallazgos clave |
| 🎛️ Análisis Dinámico | Ítem 9: selectbox, multiselect, slider, filtros interactivos |
| 🏁 Conclusiones | 5 conclusiones orientadas a decisiones de retención |

## 🛠️ Tecnologías utilizadas

- **Python 3.11**
- **Streamlit** — interfaz web interactiva
- **Pandas** — manipulación y análisis de datos
- **NumPy** — cálculo numérico
- **Matplotlib / Seaborn** — visualización
- **SciPy** — KDE y estadística

## 🚀 Instrucciones de ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/telco-churn-eda.git
cd telco-churn-eda
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
streamlit run app.py
```

### 5. Cargar el dataset
En el módulo **"📂 Carga del Dataset"**, usa el uploader para cargar
`TelcoCustomerChurn.csv`.

## 📊 Dataset

El archivo `TelcoCustomerChurn.csv` contiene **7,043 registros** y **21 variables**
sobre clientes de una empresa de telecomunicaciones:
perfil demográfico, servicios contratados, facturación y estado de churn.

## 🔑 Hallazgos principales

1. La tasa global de churn es ~**26.5%**
2. Contratos **Month-to-month** tienen churn ~**42%**
3. Clientes con churn permanecen en promedio solo **~18 meses**
4. **Fiber Optic** y **Electronic Check** correlacionan con mayor churn
5. Cargos mensuales altos + tenure bajo = mayor riesgo de abandono

## 🔗 Links

- 🌐 App desplegada: `https://tu-app.streamlit.app`
- 📁 Repositorio: `https://github.com/tu-usuario/telco-churn-eda`

## 📄 Licencia

MIT — libre uso educativo.
