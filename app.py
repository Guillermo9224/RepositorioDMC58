import streamlit as st

st.title ("Mi primera aplicacion en python")

st.sidebar.title ("Parametros")

st.write("Elaborado por : Guillermo Carrasco")

sesion = st.selectbox("Seleccione una sesion",["Sesion 1","Sesion 2","Sesion 3","Sesion 4"])
