import streamlit as st
from src.InterfazUsuario.interfazModuloUsuario import login,crear_cuenta

def inicio():
    login()
    crear_cuenta()