import streamlit as st

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
        concepto=st.text_input("Ingrese concepto")

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

 

elif Opcion == "Sesión 2":

  st.write("Bienvenido la sesión 2")

 

  precio = st.number_input("Ingrese el precio del producto", min_value = 0 , max_value = 5000 , value = 1200)

  descuento = st.number_input("Ingrese el descuento del producto del 0 al 100% ", min_value = 0 , max_value = 100 )

 

  precio_final_producto = precio - (precio*(descuento/100))

 

  st.write("El precio final del producto es: ", precio_final_producto  )

 
elif Opcion == "Sesión 3":

  st.write("Bienvenido la sesión 3")

 

else:

  st.write("Bienvenido la sesión 4")



