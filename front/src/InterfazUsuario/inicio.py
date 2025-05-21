import streamlit as st
from front.src.InterfazUsuario.interfazModuloUsuario import login,crear_cuenta

def inicio():
    st.header("Bienvenido al sistema automatizo cuadre casino")
    st.write("este software tiene como proposito\nautomatizar la gestion de un casino")
    opcion=st.sidebar.selectbox("Menu",["login","crear cuenta"])
    if opcion=="login":
        login()
    elif opcion=="crear cuenta":
        crear_cuenta()