import streamlit as st

st.title ("Mi primera aplicacion en python")

st.sidebar.title ("Parametros")

st.write("Elaborado por : Guillermo Carrasco")
st.sidebar.image ("DMC.png")


sesion = st.sidebar.selectbox("Seleccione una sesion",["Sesion 1","Sesion 2","Sesion 3","Sesion 4"])

if sesion == "Sesion 1":
  st.write("Bienvenido a la sesion 1")
  st.image("Python_logo.png")


elif sesion =="Sesion 2":
  st.write("Bienvenido a la sesion 2")
  Precio=st.number_input("Ingrese el precio del producto",min_value=0,max_value=5000,value=1200)
  descuento=st.number_input("Ingrese el descuento del producto del 0 al 100% ", min_value = 0 , max_value = 100)

precio_final_producto= precio - (precio*descuento)
st.write("El precio final del producto es: ",precio_fninal_producto)

elif sesion =="Sesion 3":
  st.write("Bienvenido a la sesion 3")

else :
  st.write("Bienvenido a la sesion 4")



