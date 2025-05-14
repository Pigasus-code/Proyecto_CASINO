import streamlit as st
from front.src.InterfazUsuario.interfazModuloUsuario import login,crear_cuenta

def inicio():
    login()
    crear_cuenta()