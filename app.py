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
              
              <i>Python Fundamentals</i>
              
              2026
              
              Aplicacion interactica en streamlit
              
              Para esta aplicacion se uso chatgpt IA asi como API reference 
              """)
 
if Opcion == "Sesión 1":

  st.write("Bienvenido la sesión 1")

  st.image("Python_logo.png" )

 

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



