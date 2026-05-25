import streamlit as st
import pandas as pd
import numpy as np
import math

st.title("Presentacion Modulo 01")


st.sidebar.title("Opciones")

 

st.write("Elaborado por: Guillermo Carrasco")

 

st.sidebar.image("DMC.png")

 

Opcion = st.sidebar.selectbox("Seleccione una opcion", ["Home","Opcion 1","Opcion 2","Opcion 3","Opcion 4"] )

if Opcion == "Home":

  st.write("Bienvenido a la Presentacion del Modulo 01")
  st.image("IA2.jpg")
  st.markdown("""
  Realizado por Juan Guillermo Carrasco Ancajima
              
  Python Fundamentals
              
  2026
              
  Aplicacion interactica en streamlit
              
  Para esta aplicacion se uso chatgpt IA asi como API reference 
  """)
 
if Opcion == "Opcion 1":

    st.header("Modulo Flujo de Caja")

    st.markdown("""
    ### Descripcion

    Esta aplicacion permite registrar:

    - Ingresos
    - Gastos

    y mostrar el saldo final.
    """)

    # LISTA VACIA
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # INPUTS
    concepto = st.text_input("Ingrese concepto")

    tipo = st.selectbox(
        "Tipo de movimiento",
        ["Ingreso", "Gasto"]
    )

    valor = st.number_input(
        "Ingrese valor",
        min_value=0
    )

    # BOTON
    if st.button("Agregar movimiento"):

        nuevo = {
            "Concepto": concepto,
            "Tipo": tipo,
            "Valor": valor
        }

        st.session_state.movimientos.append(nuevo)

        st.success("Movimiento agregado correctamente")

    # TABLA
    if len(st.session_state.movimientos) > 0:

        df = pd.DataFrame(st.session_state.movimientos)

        st.subheader("Lista de movimientos")

        st.dataframe(df)

        # TOTALES
        ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()

        gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()

        saldo = ingresos - gastos

        # METRICAS
        st.metric("Total ingresos", ingresos)

        st.metric("Total gastos", gastos)

        st.metric("Saldo final", saldo)

        # RESULTADO FINAL
        if saldo >= 0:
            st.success("Flujo de caja a favor")

        else:
            st.error("Flujo de caja en contra")


if Opcion == "Opcion 2":

    st.header("Registro de Productos")

    st.markdown("""
    ### Descripcion

    Esta aplicacion permite registrar productos usando NumPy.

    Se registran:

    - Nombre del producto
    - Categoria
    - Precio
    - Cantidad
    - Total
    """)

    # LISTAS VACIAS
    if "productos" not in st.session_state:

        st.session_state.productos = []
        st.session_state.categorias = []
        st.session_state.precios = []
        st.session_state.cantidades = []
        st.session_state.totales = []

    # FORMULARIO

    producto = st.text_input("Ingrese producto")

    categoria = st.selectbox(
        "Seleccione categoria",
        ["Tecnologia", "Ropa", "Alimentos", "Otros"]
    )

    precio = st.number_input(
        "Ingrese precio",
        min_value=0.0
    )

    cantidad = st.number_input(
        "Ingrese cantidad",
        min_value=1
    )

    # BOTON
    if st.button("Agregar producto"):

        total = precio * cantidad

        # GUARDAR DATOS
        st.session_state.productos.append(producto)

        st.session_state.categorias.append(categoria)

        st.session_state.precios.append(precio)

        st.session_state.cantidades.append(cantidad)

        st.session_state.totales.append(total)

        st.success("Producto agregado correctamente")

    # MOSTRAR TABLA
    if len(st.session_state.productos) > 0:

        # ARRAYS NUMPY
        productos_np = np.array(st.session_state.productos)

        categorias_np = np.array(st.session_state.categorias)

        precios_np = np.array(st.session_state.precios)

        cantidades_np = np.array(st.session_state.cantidades)

        totales_np = np.array(st.session_state.totales)

        # DATAFRAME
        df = pd.DataFrame({
            "Producto": productos_np,
            "Categoria": categorias_np,
            "Precio": precios_np,
            "Cantidad": cantidades_np,
            "Total": totales_np
        })

        st.subheader("Lista de productos")

        st.dataframe(df)

        # TOTAL GENERAL
        suma_total = totales_np.sum()

        st.metric("Venta total", suma_total)

if Opcion == "Opcion 3":

 def calcular_metricas_clasificacion(tp: int, fp: int, fn: int) -> dict:
     """
     Calcula precisión, recall y F1-score.
     Fórmulas:
     - precisión = TP / (TP + FP)
     - recall = TP / (TP + FN)
     - F1 = 2 * (precisión * recall) / (precisión + recall)
     """
     validar_positivo(tp, "tp", permitir_cero=True)
     validar_positivo(fp, "fp", permitir_cero=True)
     validar_positivo(fn, "fn", permitir_cero=True)
 
     precision = tp / (tp + fp) if (tp + fp) > 0 else 0
     recall = tp / (tp + fn) if (tp + fn) > 0 else 0
     f1_score = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0
 
     return {
         "precision": round(precision, 4),
         "recall": round(recall, 4),
         "f1_score": round(f1_score, 4)
     }
 
 
 def calcular_disponibilidad_sistema(tiempo_total_horas: float, tiempo_caida_horas: float) -> dict:
     """
     Calcula la disponibilidad de un sistema.
     Fórmula:
     disponibilidad = ((tiempo_total - tiempo_caida) / tiempo_total) * 100
     """
     validar_positivo(tiempo_total_horas, "tiempo_total_horas")
     validar_positivo(tiempo_caida_horas, "tiempo_caida_horas", permitir_cero=True)
 
     if tiempo_caida_horas > tiempo_total_horas:
         raise ValueError("tiempo_caida_horas no puede ser mayor que tiempo_total_horas.")
 
     disponibilidad = (
         (tiempo_total_horas - tiempo_caida_horas) / tiempo_total_horas
     ) * 100
 
     return {
         "disponibilidad_pct": round(disponibilidad, 4)
     }
 
 
 def calcular_tiempo_transferencia_archivo(tamano_mb: float, velocidad_mbps: float) -> dict:
     """
     Calcula el tiempo estimado de transferencia de un archivo.
     Conversión:
     1 byte = 8 bits
     Fórmula:
     tiempo_segundos = (tamano_mb * 8) / velocidad_mbps
     """
     validar_positivo(tamano_mb, "tamano_mb")
     validar_positivo(velocidad_mbps, "velocidad_mbps")
 
     tiempo_segundos = (tamano_mb * 8) / velocidad_mbps
     tiempo_minutos = tiempo_segundos / 60
 
     return {
         "tiempo_segundos": round(tiempo_segundos, 2),
         "tiempo_minutos": round(tiempo_minutos, 2)
     }
 
 
 def calcular_tasa_error_transacciones(transacciones_fallidas: int, transacciones_totales: int) -> dict:
     """
     Calcula la tasa de error de transacciones.
     Fórmula:
     tasa_error = (fallidas / totales) * 100
     """
     validar_positivo(transacciones_fallidas, "transacciones_fallidas", permitir_cero=True)
     validar_positivo(transacciones_totales, "transacciones_totales")
 
     if transacciones_fallidas > transacciones_totales:
         raise ValueError("transacciones_fallidas no puede ser mayor que transacciones_totales.")
 
     tasa_error = (transacciones_fallidas / transacciones_totales) * 100
     tasa_exito = 100 - tasa_error
 
     return {
         "tasa_error_pct": round(tasa_error, 4),
         "tasa_exito_pct": round(tasa_exito, 4)
     }
 
 
 def calcular_almacenamiento_respaldo(
     numero_usuarios: int,
     archivos_por_usuario: int,
     tamano_promedio_mb: float,
     factor_respaldo: float
 ) -> dict:
     """
     Calcula el almacenamiento estimado necesario para respaldo.
     Fórmula:
     almacenamiento_total = usuarios * archivos_por_usuario * tamano_promedio_mb * factor_respaldo
     """
     validar_positivo(numero_usuarios, "numero_usuarios")
     validar_positivo(archivos_por_usuario, "archivos_por_usuario")
     validar_positivo(tamano_promedio_mb, "tamano_promedio_mb")
     validar_positivo(factor_respaldo, "factor_respaldo")
 
     almacenamiento_mb = (
         numero_usuarios * archivos_por_usuario * tamano_promedio_mb * factor_respaldo
     )
     almacenamiento_gb = almacenamiento_mb / 1024
 
     return {
         "almacenamiento_estimado_mb": round(almacenamiento_mb, 2),
         "almacenamiento_estimado_gb": round(almacenamiento_gb, 2)
     }
