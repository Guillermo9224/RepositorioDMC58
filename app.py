
"""
Caso de Estudio N°2 - EDA TelcoCustomerChurn
Especialización Python for Analytics
Autor: Guillermo
Año: 2025
"""
 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
 
st.set_page_config(page_title="TelcoChurn EDA", layout="wide")
 
 
# ─────────────────────────────────────────────
# CLASE DataAnalyzer (POO)
# ─────────────────────────────────────────────
class DataAnalyzer:
    """Clase que encapsula el análisis del dataset de churn."""
 
    def __init__(self, df):
        self.df = df.copy()
        # Limpiar TotalCharges que puede venir como string
        self.df["TotalCharges"] = pd.to_numeric(self.df["TotalCharges"], errors="coerce")
 
    def get_numericas(self):
        return self.df.select_dtypes(include=[np.number]).columns.tolist()
 
    def get_categoricas(self):
        return self.df.select_dtypes(include=["object"]).columns.tolist()
 
    def estadisticas_descriptivas(self):
        cols = self.get_numericas()
        desc = self.df[cols].describe().T
        desc["mediana"] = self.df[cols].median()
        return desc.round(2)
 
    def valores_faltantes(self):
        missing = self.df.isnull().sum()
        pct = (missing / len(self.df) * 100).round(2)
        return pd.DataFrame({"Faltantes": missing, "Porcentaje (%)": pct})
 
    def plot_histograma(self, col):
        fig, ax = plt.subplots()
        ax.hist(self.df[self.df["Churn"] == "No"][col].dropna(),
                bins=30, alpha=0.6, label="No Churn", color="steelblue")
        ax.hist(self.df[self.df["Churn"] == "Yes"][col].dropna(),
                bins=30, alpha=0.6, label="Churn", color="tomato")
        ax.set_title(f"Distribución de {col}")
        ax.set_xlabel(col)
        ax.set_ylabel("Frecuencia")
        ax.legend()
        return fig
 
    def plot_barras_churn(self, col):
        conteo = self.df.groupby([col, "Churn"]).size().unstack(fill_value=0)
        fig, ax = plt.subplots()
        conteo.plot(kind="bar", ax=ax, color=["steelblue", "tomato"], alpha=0.8)
        ax.set_title(f"{col} vs Churn")
        ax.set_xlabel(col)
        ax.set_ylabel("Cantidad")
        ax.tick_params(axis="x", rotation=30)
        ax.legend(title="Churn")
        return fig
 
    def plot_boxplot(self, col):
        fig, ax = plt.subplots()
        data_no  = self.df[self.df["Churn"] == "No"][col].dropna()
        data_yes = self.df[self.df["Churn"] == "Yes"][col].dropna()
        ax.boxplot([data_no, data_yes], labels=["No Churn", "Churn"],
                   patch_artist=True,
                   boxprops=dict(facecolor="steelblue", alpha=0.6))
        ax.set_title(f"{col} por Churn")
        ax.set_ylabel(col)
        return fig
 
 
# ─────────────────────────────────────────────
# SIDEBAR - MENÚ
# ─────────────────────────────────────────────
MODULOS = [
    "🏠 Home",
    "📂 Carga del Dataset",
    "🔍 EDA",
    "🎛️ Análisis Dinámico",
    "🏁 Conclusiones",
]
 
# Inicializar índice de módulo si no existe (arranca en Home)
if "modulo_idx" not in st.session_state:
    st.session_state["modulo_idx"] = 0
 
st.sidebar.title("📡 TelcoChurn EDA")
st.sidebar.markdown("---")
modulo = st.sidebar.radio(
    "Menú principal",
    MODULOS,
    index=st.session_state["modulo_idx"],
    key="sidebar_radio",
)
# Sincronizar índice cuando el usuario cambia en el sidebar
st.session_state["modulo_idx"] = MODULOS.index(modulo)
st.sidebar.markdown("---")
st.sidebar.write("**Autor:** Guillermo")
st.sidebar.write("**Curso:** Python for Analytics")
st.sidebar.write("**Año:** 2025")
 
 
# ─────────────────────────────────────────────
# ESTADO GLOBAL
# ─────────────────────────────────────────────
if "analyzer" not in st.session_state:
    st.session_state["analyzer"] = None
 
 
 
 
# ═══════════════════════════════════
# MÓDULO 1 - HOME
# ═══════════════════════════════════
if modulo == "🏠 Home":
    st.title("📡 Análisis de Fuga de Clientes — TelcoCustomerChurn")
    st.markdown("**Caso de Estudio N°2 · Especialización Python for Analytics**")
    st.markdown("---")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.subheader("🎯 Objetivo")
        st.write("""
        Analizar de forma exploratoria el dataset TelcoCustomerChurn para
        identificar patrones asociados a la fuga de clientes (churn).
 
        El objetivo NO es predecir el churn, sino entender los datos
        y comunicar hallazgos útiles para la toma de decisiones.
        """)
 
        st.subheader("📁 Sobre el dataset")
        st.write("""
        Contiene información de clientes de una empresa de telecomunicaciones:
        servicios contratados, facturación, tiempo de permanencia y si
        el cliente abandonó o no la empresa.
 
        Durante el último mes, el ratio de churn subió de 2% a 2.5%
        por el impacto del COVID-19. Retener un cliente es 6–7 veces
        más barato que adquirir uno nuevo.
        """)
 
    with col2:
        st.subheader("👤 Datos del autor")
        st.info("**Nombre:** Guillermo\n\n**Curso:** Especialización Python for Analytics\n\n**Año:** 2025")
 
        st.subheader("🛠️ Tecnologías")
        st.write("- Python 3.11")
        st.write("- Pandas")
        st.write("- NumPy")
        st.write("- Matplotlib")
        st.write("- Seaborn")
        st.write("- Streamlit")
 
    st.markdown("---")
    st.subheader("📋 Variables del dataset")
    variables = pd.DataFrame({
        "Variable":    ["customerID","gender","SeniorCitizen","Partner","Dependents",
                        "tenure","PhoneService","MultipleLines","InternetService",
                        "OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport",
                        "StreamingTV","StreamingMovies","Contract","PaperlessBilling",
                        "PaymentMethod","MonthlyCharges","TotalCharges","Churn"],
        "Descripción": ["ID único del cliente","Género","¿Es adulto mayor?",
                        "¿Tiene pareja?","¿Tiene dependientes?","Meses de permanencia",
                        "¿Tiene telefonía?","¿Múltiples líneas?","Tipo de internet",
                        "¿Seguridad online?","¿Backup online?","¿Protección dispositivo?",
                        "¿Soporte técnico?","¿TV streaming?","¿Películas streaming?",
                        "Tipo de contrato","¿Facturación electrónica?","Método de pago",
                        "Cargo mensual (USD)","Cargo total (USD)","¿Abandonó la empresa?"],
    })
    st.dataframe(variables, use_container_width=True)
 
    st.markdown("---")
    if st.button("Siguiente: Carga del Dataset →"):
        st.session_state["modulo_idx"] = 1
        st.rerun()
 
 
# ═══════════════════════════════════
# MÓDULO 2 - CARGA DEL DATASET
# ═══════════════════════════════════
elif modulo == "📂 Carga del Dataset":
    st.title("📂 Carga del Dataset")
    st.markdown("---")
 
    archivo = st.file_uploader("Sube el archivo TelcoCustomerChurn.csv", type=["csv"])
 
    if archivo is not None:
        df = pd.read_csv(archivo)
        st.session_state["analyzer"] = DataAnalyzer(df)
        st.success(f"✅ Archivo cargado: **{archivo.name}**")
 
        st.subheader("Vista previa (primeras 5 filas)")
        st.dataframe(df.head(), use_container_width=True)
 
        st.subheader("Dimensiones del dataset")
        col1, col2 = st.columns(2)
        col1.metric("Filas", df.shape[0])
        col2.metric("Columnas", df.shape[1])
 
        st.subheader("Tipos de datos")
        tipos = pd.DataFrame({
            "Columna": df.dtypes.index,
            "Tipo":    df.dtypes.values.astype(str),
            "Nulos":   df.isnull().sum().values,
        })
        st.dataframe(tipos, use_container_width=True)
 
        st.markdown("---")
        if st.button("Siguiente: EDA →"):
            st.session_state["modulo_idx"] = 2
            st.rerun()
 
    else:
        st.warning("⚠️ Debes cargar el archivo CSV para poder analizar los datos.")
 
 
# ═══════════════════════════════════
# MÓDULO 3 - EDA (10 ítems)
# ═══════════════════════════════════
elif modulo == "🔍 EDA":
    st.title("🔍 Análisis Exploratorio de Datos")
 
    if st.session_state["analyzer"] is None:
        st.warning("⚠️ Primero carga el dataset en el módulo 'Carga del Dataset'.")
        st.stop()
 
    an = st.session_state["analyzer"]
    df = an.df
 
    tabs = st.tabs([
        "1 · Info General",
        "2 · Variables",
        "3 · Estadísticas",
        "4 · Nulos",
        "5 · Distribuciones",
        "6 · Categóricas",
        "7 · Bivariado Num",
        "8 · Bivariado Cat",
        "9 · Por parámetros",
        "10 · Hallazgos",
    ])
 
    # ── Ítem 1: Info general ──
    with tabs[0]:
        st.subheader("Ítem 1 — Información general del dataset")
 
        col1, col2, col3 = st.columns(3)
        col1.metric("Filas", df.shape[0])
        col2.metric("Columnas", df.shape[1])
        col3.metric("Nulos totales", df.isnull().sum().sum())
 
        st.markdown("**Tipos de datos y nulos por columna:**")
        info = pd.DataFrame({
            "Columna":        df.columns,
            "Tipo":           df.dtypes.astype(str).values,
            "Valores únicos": df.nunique().values,
            "Nulos":          df.isnull().sum().values,
        })
        st.dataframe(info, use_container_width=True)
        st.info("El dataset tiene 21 columnas. La variable objetivo es **Churn** (Yes / No).")
 
    # ── Ítem 2: Clasificación de variables ──
    with tabs[1]:
        st.subheader("Ítem 2 — Clasificación de variables")
 
        numericas   = an.get_numericas()
        categoricas = an.get_categoricas()
 
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**🔢 Variables numéricas ({len(numericas)}):**")
            for v in numericas:
                st.write(f"- {v}")
        with col2:
            st.markdown(f"**🔤 Variables categóricas ({len(categoricas)}):**")
            for v in categoricas:
                st.write(f"- {v}")
 
        st.markdown("**Cardinalidad de variables categóricas:**")
        cardinalidad = pd.DataFrame({
            "Variable":       categoricas,
            "Valores únicos": [df[c].nunique() for c in categoricas],
            "Ejemplo":        [str(df[c].unique()[:3].tolist()) for c in categoricas],
        })
        st.dataframe(cardinalidad, use_container_width=True)
        st.info("La mayoría de las variables categóricas son binarias (Yes/No).")
 
    # ── Ítem 3: Estadísticas descriptivas ──
    with tabs[2]:
        st.subheader("Ítem 3 — Estadísticas descriptivas")
        st.dataframe(an.estadisticas_descriptivas(), use_container_width=True)
 
        st.markdown("**Interpretación básica:**")
        for col in an.get_numericas():
            media   = df[col].mean()
            mediana = df[col].median()
            desvio  = df[col].std()
            st.write(f"- **{col}**: Media = {media:.2f} | Mediana = {mediana:.2f} | Desvío = {desvio:.2f}")
 
        st.info("TotalCharges tiene alta dispersión por clientes con contratos largos.")
 
    # ── Ítem 4: Valores faltantes ──
    with tabs[3]:
        st.subheader("Ítem 4 — Análisis de valores faltantes")
        faltantes = an.valores_faltantes()
        con_nulos = faltantes[faltantes["Faltantes"] > 0]
 
        if con_nulos.empty:
            st.success("✅ No hay valores nulos en el dataset.")
        else:
            st.dataframe(con_nulos, use_container_width=True)
            fig, ax = plt.subplots()
            con_nulos["Porcentaje (%)"].plot(kind="barh", ax=ax, color="tomato")
            ax.set_title("% de valores faltantes")
            ax.set_xlabel("%")
            st.pyplot(fig)
            plt.close()
 
        nulos_tc = df["TotalCharges"].isnull().sum()
        st.info(
            f"TotalCharges tiene {nulos_tc} nulos tras conversión numérica. "
            "Corresponden a clientes con tenure = 0 (sin cargos acumulados aún)."
        )
 
    # ── Ítem 5: Distribución de numéricas ──
    with tabs[4]:
        st.subheader("Ítem 5 — Distribución de variables numéricas")
        numericas = an.get_numericas()
        col_sel = st.selectbox("Selecciona una variable numérica", numericas, key="item5")
 
        col1, col2 = st.columns(2)
        with col1:
            fig = an.plot_histograma(col_sel)
            st.pyplot(fig)
            plt.close()
        with col2:
            fig2 = an.plot_boxplot(col_sel)
            st.pyplot(fig2)
            plt.close()
 
        st.info(
            "Los clientes con churn tienden a tener tenure bajo y MonthlyCharges altos."
        )
 
    # ── Ítem 6: Variables categóricas ──
    with tabs[5]:
        st.subheader("Ítem 6 — Análisis de variables categóricas")
        cat_cols = [c for c in an.get_categoricas() if c != "customerID"]
        col_cat = st.selectbox("Selecciona una variable categórica", cat_cols, key="item6")
 
        col1, col2 = st.columns(2)
        with col1:
            conteo = df[col_cat].value_counts()
            st.markdown(f"**Conteo — {col_cat}:**")
            st.dataframe(conteo.rename("Cantidad"), use_container_width=True)
        with col2:
            fig, ax = plt.subplots()
            conteo.plot(kind="bar", ax=ax, color="steelblue", alpha=0.8)
            ax.set_title(f"Distribución de {col_cat}")
            ax.set_ylabel("Cantidad")
            ax.tick_params(axis="x", rotation=30)
            st.pyplot(fig)
            plt.close()
 
        proporciones = (df[col_cat].value_counts(normalize=True) * 100).round(2)
        st.markdown("**Proporciones (%):**")
        st.dataframe(proporciones.rename("Porcentaje (%)"), use_container_width=True)
 
    # ── Ítem 7: Bivariado numérico vs categórico ──
    with tabs[6]:
        st.subheader("Ítem 7 — Bivariado: Numérico vs Churn")
        num_cols = an.get_numericas()
        col_num = st.selectbox("Selecciona variable numérica", num_cols, key="item7")
 
        col1, col2 = st.columns(2)
        with col1:
            fig = an.plot_boxplot(col_num)
            st.pyplot(fig)
            plt.close()
        with col2:
            fig = an.plot_histograma(col_num)
            st.pyplot(fig)
            plt.close()
 
        st.markdown("**Estadísticas por grupo:**")
        stats = df.groupby("Churn")[col_num].agg(["mean","median","std"]).round(2)
        st.dataframe(stats, use_container_width=True)
        st.info("Los clientes con churn tienen menor tenure y mayor MonthlyCharges en promedio.")
 
    # ── Ítem 8: Bivariado categórico vs categórico ──
    with tabs[7]:
        st.subheader("Ítem 8 — Bivariado: Categórico vs Churn")
        cat_options = [c for c in an.get_categoricas() if c not in ["customerID","Churn"]]
        col_cat2 = st.selectbox("Selecciona variable categórica", cat_options,
                                index=cat_options.index("Contract") if "Contract" in cat_options else 0,
                                key="item8")
 
        col1, col2 = st.columns(2)
        with col1:
            fig = an.plot_barras_churn(col_cat2)
            st.pyplot(fig)
            plt.close()
        with col2:
            tasa = df.groupby(col_cat2)["Churn"].apply(
                lambda x: (x == "Yes").mean() * 100
            ).round(2).rename("Churn Rate (%)")
            st.markdown("**Tasa de churn por categoría:**")
            st.dataframe(tasa, use_container_width=True)
 
            fig2, ax = plt.subplots()
            tasa.sort_values().plot(kind="barh", ax=ax, color="tomato", alpha=0.8)
            ax.set_title(f"Tasa de Churn (%) por {col_cat2}")
            ax.set_xlabel("%")
            st.pyplot(fig2)
            plt.close()
 
    # ── Ítem 9: Análisis por parámetros seleccionados ──
    with tabs[8]:
        st.subheader("Ítem 9 — Análisis por parámetros seleccionados")
 
        col1, col2 = st.columns(2)
        with col1:
            var_x = st.selectbox(
                "Variable X",
                an.get_numericas() + [c for c in an.get_categoricas() if c != "customerID"],
                key="item9_x"
            )
        with col2:
            contratos = st.multiselect(
                "Filtrar por tipo de contrato",
                df["Contract"].unique().tolist(),
                default=df["Contract"].unique().tolist(),
                key="item9_cont"
            )
 
        tenure_range = st.slider(
            "Filtrar por Tenure (meses)",
            int(df["tenure"].min()),
            int(df["tenure"].max()),
            (int(df["tenure"].min()), int(df["tenure"].max())),
            key="item9_slider"
        )
 
        mostrar_senior = st.checkbox("Solo adultos mayores (SeniorCitizen = 1)", key="item9_cb")
 
        df_filtrado = df[
            df["Contract"].isin(contratos) &
            (df["tenure"] >= tenure_range[0]) &
            (df["tenure"] <= tenure_range[1])
        ]
        if mostrar_senior:
            df_filtrado = df_filtrado[df_filtrado["SeniorCitizen"] == 1]
 
        st.write(f"**Registros con filtros aplicados:** {len(df_filtrado):,} de {len(df):,}")
 
        an_filtrado = DataAnalyzer(df_filtrado)
        if var_x in an.get_numericas():
            fig = an_filtrado.plot_histograma(var_x)
        else:
            fig = an_filtrado.plot_barras_churn(var_x)
        st.pyplot(fig)
        plt.close()
 
    # ── Ítem 10: Hallazgos clave ──
    with tabs[9]:
        st.subheader("Ítem 10 — Hallazgos clave")
 
        churn_rate   = (df["Churn"] == "Yes").mean() * 100
        m2m_rate     = df[df["Contract"]=="Month-to-month"]["Churn"].eq("Yes").mean()*100
        fiber_rate   = df[df["InternetService"]=="Fiber optic"]["Churn"].eq("Yes").mean()*100
        tenure_churn = df[df["Churn"]=="Yes"]["tenure"].mean()
        mc_churn     = df[df["Churn"]=="Yes"]["MonthlyCharges"].mean()
 
        col1, col2, col3 = st.columns(3)
        col1.metric("Tasa de Churn Global", f"{churn_rate:.1f}%")
        col2.metric("Churn en Month-to-month", f"{m2m_rate:.1f}%")
        col3.metric("Tenure promedio (Churn)", f"{tenure_churn:.0f} meses")
 
        st.markdown("---")
 
        # Dashboard resumen
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle("Resumen visual — Factores de Churn", fontsize=14)
 
        # Gráfico 1: Donut Churn
        churn_counts = df["Churn"].value_counts()
        axes[0,0].pie(churn_counts, labels=churn_counts.index, autopct="%1.1f%%",
                      colors=["steelblue","tomato"], startangle=90,
                      wedgeprops=dict(width=0.5))
        axes[0,0].set_title("Distribución de Churn")
 
        # Gráfico 2: Churn por Contract
        tasa_contrato = df.groupby("Contract")["Churn"].apply(
            lambda x: (x=="Yes").mean()*100
        )
        axes[0,1].bar(tasa_contrato.index, tasa_contrato.values,
                      color=["tomato","steelblue","green"], alpha=0.8)
        axes[0,1].set_title("Churn (%) por Tipo de Contrato")
        axes[0,1].set_ylabel("%")
        axes[0,1].tick_params(axis="x", rotation=15)
 
        # Gráfico 3: Tenure por Churn (histograma)
        axes[1,0].hist(df[df["Churn"]=="No"]["tenure"], bins=25,
                       alpha=0.6, color="steelblue", label="No Churn")
        axes[1,0].hist(df[df["Churn"]=="Yes"]["tenure"], bins=25,
                       alpha=0.6, color="tomato", label="Churn")
        axes[1,0].set_title("Distribución de Tenure por Churn")
        axes[1,0].set_xlabel("Meses")
        axes[1,0].legend()
 
        # Gráfico 4: MonthlyCharges por Churn
        axes[1,1].hist(df[df["Churn"]=="No"]["MonthlyCharges"], bins=25,
                       alpha=0.6, color="steelblue", label="No Churn")
        axes[1,1].hist(df[df["Churn"]=="Yes"]["MonthlyCharges"], bins=25,
                       alpha=0.6, color="tomato", label="Churn")
        axes[1,1].set_title("MonthlyCharges por Churn")
        axes[1,1].set_xlabel("USD")
        axes[1,1].legend()
 
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
 
 
# ═══════════════════════════════════
# MÓDULO 4 - ANÁLISIS DINÁMICO
# ═══════════════════════════════════
elif modulo == "🎛️ Análisis Dinámico":
    st.title("🎛️ Análisis Dinámico")
 
    if st.session_state["analyzer"] is None:
        st.warning("⚠️ Primero carga el dataset en el módulo 'Carga del Dataset'.")
        st.stop()
 
    an = st.session_state["analyzer"]
    df = an.df
 
    st.markdown("Filtra los datos y explora la variable que quieras.")
    st.markdown("---")
 
    col1, col2 = st.columns(2)
    with col1:
        todas_vars = [c for c in an.get_numericas() + an.get_categoricas()
                      if c != "customerID"]
        variable = st.selectbox("Variable a analizar", todas_vars)
    with col2:
        churn_filter = st.selectbox("Filtrar por Churn", ["Todos", "Yes", "No"])
 
    contratos_sel = st.multiselect(
        "Tipo de contrato",
        df["Contract"].unique().tolist(),
        default=df["Contract"].unique().tolist()
    )
 
    tenure_min, tenure_max = st.slider(
        "Rango de tenure (meses)",
        int(df["tenure"].min()), int(df["tenure"].max()),
        (int(df["tenure"].min()), int(df["tenure"].max()))
    )
 
    solo_senior = st.checkbox("Solo adultos mayores")
 
    # Aplicar filtros
    df_din = df[
        df["Contract"].isin(contratos_sel) &
        (df["tenure"] >= tenure_min) &
        (df["tenure"] <= tenure_max)
    ]
    if churn_filter != "Todos":
        df_din = df_din[df_din["Churn"] == churn_filter]
    if solo_senior:
        df_din = df_din[df_din["SeniorCitizen"] == 1]
 
    st.write(f"**Registros mostrados:** {len(df_din):,}")
 
    an_din = DataAnalyzer(df_din)
 
    if variable in an.get_numericas():
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(an_din.plot_histograma(variable))
            plt.close()
        with col2:
            st.pyplot(an_din.plot_boxplot(variable))
            plt.close()
        st.dataframe(df_din[variable].describe().round(2), use_container_width=True)
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(an_din.plot_barras_churn(variable))
            plt.close()
        with col2:
            conteo = df_din[variable].value_counts()
            st.dataframe(conteo.rename("Cantidad"), use_container_width=True)
 
    if st.checkbox("Ver tabla de datos filtrados (muestra de 20 filas)"):
        st.dataframe(df_din.sample(min(20, len(df_din))), use_container_width=True)
 
 
# ═══════════════════════════════════
# MÓDULO 5 - CONCLUSIONES
# ═══════════════════════════════════
elif modulo == "🏁 Conclusiones":
    st.title("🏁 Conclusiones Finales")
 
    if st.session_state["analyzer"] is None:
        st.warning("⚠️ Primero carga el dataset en el módulo 'Carga del Dataset'.")
        st.stop()
 
    an = st.session_state["analyzer"]
    df = an.df
 
    churn_rate   = (df["Churn"] == "Yes").mean() * 100
    m2m_rate     = df[df["Contract"]=="Month-to-month"]["Churn"].eq("Yes").mean()*100
    fiber_rate   = df[df["InternetService"]=="Fiber optic"]["Churn"].eq("Yes").mean()*100
    senior_rate  = df[df["SeniorCitizen"]==1]["Churn"].eq("Yes").mean()*100
    tenure_churn = df[df["Churn"]=="Yes"]["tenure"].mean()
    mc_churn     = df[df["Churn"]=="Yes"]["MonthlyCharges"].mean()
 
    st.markdown("---")
 
    st.subheader("📌 Conclusión 1 — El contrato mes a mes es el mayor factor de riesgo")
    st.write(
        f"Los clientes con contrato **Month-to-month** tienen una tasa de churn de "
        f"**{m2m_rate:.1f}%**, muy por encima de la tasa global de {churn_rate:.1f}%. "
        "Incentivar contratos anuales debería ser la principal palanca de retención."
    )
 
    st.subheader("📌 Conclusión 2 — Los primeros meses son los más críticos")
    st.write(
        f"Los clientes que hacen churn llevan en promedio solo **{tenure_churn:.0f} meses**. "
        "Un programa de seguimiento en los primeros 6 meses podría reducir la fuga."
    )
 
    st.subheader("📌 Conclusión 3 — Fiber Optic concentra el mayor churn por servicio")
    st.write(
        f"El **{fiber_rate:.1f}%** de los usuarios de Fiber Optic abandonan la empresa. "
        "Esto sugiere problemas de precio o calidad percibida en ese servicio."
    )
 
    st.subheader("📌 Conclusión 4 — Los adultos mayores son un segmento vulnerable")
    st.write(
        f"Los adultos mayores tienen una tasa de churn de **{senior_rate:.1f}%**. "
        "Requieren atención diferenciada, posiblemente con soporte más personalizado."
    )
 
    st.subheader("📌 Conclusión 5 — Cargos altos con poca permanencia = mayor riesgo")
    st.write(
        f"Los clientes con churn pagan en promedio **${mc_churn:.0f}/mes** con muy poco tiempo "
        "de permanencia. Ofrecer revisiones de plan en etapas tempranas podría mejorar "
        "la retención, especialmente considerando que adquirir un cliente nuevo cuesta "
        "6–7 veces más que retener uno existente."
    )
 
    st.markdown("---")
    st.success(
        "✅ Análisis completado. Los hallazgos apuntan a que el tipo de contrato, "
        "el tiempo de permanencia y el tipo de internet son los factores más relevantes "
        "para entender la fuga de clientes."
    )
