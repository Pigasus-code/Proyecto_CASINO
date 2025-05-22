import streamlit as st
from front.src import controlador


def app(gestor:object):
    
    st.session_state["gestor"] = gestor
    controlador.set_gestor(gestor)
    
    def inicio():
        st.header("Bienvenido al sistema automatizo cuadre casino")
        st.write("este software tiene como proposito\nautomatizar la gestion de un casino")
        opcion=st.sidebar.selectbox("Menu",["login","crear cuenta"])
        if opcion=="login":
            login()
        elif opcion=="crear cuenta":
            crear_cuenta()
    
    def Casinos():
        """
        crear la interfaz para que el usuarios pueda hacer uso de todas las funcionalidades
        de crear casinos, modificar,etc
        """
        pass

    def contadores():
        """
        crear la interfaz para que el usuarios pueda hacer uso de todas las funcionalidades
        de agregar contadores, modificar,etc
        """
        pass
    
    def cuadre_casino():
        """
        crear la interfaz para que el usuarios pueda hacer uso de todas las funcionalidades
        de crear hacer un cuadre por casino
        """
        pass

    def cuadre_maquina():
        """
        crear la interfaz para que el usuarios pueda hacer uso de todas las funcionalidades
        de crear hacer un cuadre por maquina
        """
        pass
    
    def maquinas():
        """
        crear la interfaz para que el usuarios pueda hacer uso de todas las funcionalidades
        de crear maquinas, modificar,etc
        """
        pass
    
    def reportes():
        """
        crear la interfaz para que el usuarios pueda crear reportes personalizados
        """
        pass
    
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
    inicio()