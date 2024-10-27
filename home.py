import streamlit as st
from pages import soy 

st.title("HOME🏡")

st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a:", ["Quien soy"])

# Lógica para mostrar cada página
if page == "Inicio":
    home.show()
elif page == "Quien soy":
    about.show()
