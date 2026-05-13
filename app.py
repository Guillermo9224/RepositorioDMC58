import streamlit as st

st.title ("Mi primera aplicacion en python")

st.sidebar.title ("Parametros")

st.write("Elaborado por : Guillermo Carrasco")

sesion = st.sidebar.selectbox("Seleccione una sesion",["Sesion 1","Sesion 2","Sesion 3","Sesion 4"])

if sesion == "Sesion 1":
  st.write("Bienvenido a la sesion 1")

elif sesion =="Sesion 2":
  st.write("Bienvenido a la sesion 2")

elif sesion =="Sesion 3":
  st.write("Bienvenido a la sesion 3")

else ("Bienvenido a la sesion 3")
