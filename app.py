import streamlit as st

st.title("Presentacion Modulo 01")


st.sidebar.title("Parámetros")

 

st.write("Elaborado por: Guillermo Carrasco")

 

st.sidebar.image("DMC.png")

 

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"] )

 

if sesion == "Sesión 1":

  st.write("Bienvenido la sesión 1")

  st.image("Python_logo.png" )

 

elif sesion == "Sesión 2":

  st.write("Bienvenido la sesión 2")

 

  precio = st.number_input("Ingrese el precio del producto", min_value = 0 , max_value = 5000 , value = 1200)

  descuento = st.number_input("Ingrese el descuento del producto del 0 al 100% ", min_value = 0 , max_value = 100 )

 

  precio_final_producto = precio - (precio*(descuento/100))

 

  st.write("El precio final del producto es: ", precio_final_producto  )

 
elif sesion == "Sesión 3":

  st.write("Bienvenido la sesión 3")

 

else:

  st.write("Bienvenido la sesión 4")



