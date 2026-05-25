import streamlit as st
import pandas as pd
import numpy as np
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


