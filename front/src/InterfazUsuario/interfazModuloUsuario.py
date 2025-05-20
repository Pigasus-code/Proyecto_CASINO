from front.src import controlador
import streamlit as st

def login():
    """
    crear un login con los atributos de un usuario y segun su tipo deplegar
    un menu de permisos
    administrador: tiene acceso a todos los modulos
    soporte: tiene acceso a todos los modulos de cuadre por maquina o casino , contadores y reportes
    operador: tiene accceso solo al modulo de reportes
    """
    pass

def crear_cuenta():
    with st.form(key="Crear cuenta",clear_on_submit=True):
        tipo=st.selectbox("Tipo",["Administrador","Operador","Soporte"])
        usuario=st.text_input("Usuario")
        contraseña=st.text_input("Contraseña")
        nombre=st.text_input("Nombre")
        telefono=st.text_input("telefono")
        boton_enviar=st.form_submit_button(label="Enviar")
    if boton_enviar:
        mensaje=controlador.crear_usuario(usuario,contraseña,tipo,nombre,telefono)
        if mensaje:
            st.success("Cuenta creada exitosamente")
        else:
            st.error("Error al crear la cuenta")
        