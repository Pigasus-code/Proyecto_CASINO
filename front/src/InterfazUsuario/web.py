import streamlit as st
from front.src import controlador
import os
import toml
import pandas as pd

# Ruta del archivo de configuración

BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CONFIG_PATH = os.path.join(BASE_DIR,"Util",".streamlit","config_usuario.tolm")

# Función para guardar la configuración del tema en archivo TOML
def guardar_configuracion_tema(primary: str,  background: str, secondary: str):
    config = {
        "theme": {
            "primaryColor": primary,
            "backgroundColor": background,
            "secondaryBackgroundColor": secondary
        }
    }
    os.makedirs(os.path.join(BASE_DIR,"util",".streamlit"), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        toml.dump(config, f)

# Función para cargar la configuración del tema desde archivo TOML
def cargar_configuracion_tema():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            config = toml.load(f)
            return (
                config.get("theme", {}).get("primaryColor", "#FF4B4B"),
                config.get("theme", {}).get("backgroundColor", "#0E1117"),
                config.get("theme", {}).get("secondaryBackgroundColor", "#262730")
            )
    return ("#FF4B4B", "#0E1117", "#262730")

# Función para aplicar los cambios
def apply_custom_theme(primary: str, background: str, secondary: str):
    custom_css = f"""
        <style>
        /* Botones (normales, formularios, sidebar) */
        button[kind="primary"], button:has(svg) {{
            background-color: {primary} !important;
            color: white !important;
            border: none !important;
        }}

        /* Fondo general */
        .stApp {{
            background-color: {background} !important;
        }}

        /* Sidebar */
        [data-testid='stSidebar'] {{
            background-color: {secondary} !important;
        }}

        /* Círculo del ítem seleccionado en st.sidebar.radio */
        .stRadio [role="radiogroup"] > label[data-baseweb="radio"] > div:first-child svg {{
            fill: {primary} !important;
        }}

        /* Texto del ítem seleccionado */
        .stRadio [aria-checked="true"] > div {{
            color: {primary} !important;
            font-weight: bold;
        }}
        </style>
        """
    st.markdown(custom_css, unsafe_allow_html=True)

def app(gestor: object):
    
    # Configuración inicial de la página (título e icono por defecto)
    st.set_page_config(page_title="Cuadre Casino", page_icon="🎲")
    
    # Inicialización del gestor
    if "gestor" not in st.session_state:
        st.session_state["gestor"] = gestor
        controlador.set_gestor(gestor)

    # Estado de navegación
    if "pantalla" not in st.session_state:
        st.session_state["pantalla"] = "inicio"
        
    # Inicializar valores de tema en Session State (desde archivo TOML si existe)
    if not all(k in st.session_state for k in ("theme_primary", "theme_background", "theme_secondary")):
        primary, background, secondary = cargar_configuracion_tema()
        st.session_state["theme_primary"] = primary
        st.session_state["theme_background"] = background
        st.session_state["theme_secondary"] = secondary

    # Aplicar tema actual
    apply_custom_theme(
        st.session_state["theme_primary"],
        st.session_state["theme_background"],
        st.session_state["theme_secondary"]
    )
    


    # Funciones de vista
    def mostrar_login():
        ruta_logo = os.path.join(BASE_DIR,"Data","logo_casino.png")
        if os.path.exists(ruta_logo):
            st.image(ruta_logo, width=200)
        st.header("Iniciar sesión")
        with st.form(key="form_login", clear_on_submit=True):
            usuario = st.text_input("Usuario")
            contraseña = st.text_input("Contraseña", type="password")
            enviar = st.form_submit_button("Entrar")

        if enviar:
            tipo_usuario = controlador.login_usuario(usuario, contraseña)
            if tipo_usuario:
                st.session_state["tipo_usuario"] = tipo_usuario
                st.session_state["pantalla"] = "menu"
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")

        if st.button("Crear una cuenta"):
            st.session_state["pantalla"] = "crear_cuenta"
            st.rerun()
            

    def mostrar_crear_cuenta():
        st.header("Crear cuenta")
        tipo = st.selectbox("Tipo de usuario", ["Administrador", "Operador", "Soporte"])
        token=None
        with st.form(key="form_crear_cuenta", clear_on_submit=True):
            if tipo == "Administrador":
                token = st.text_input("Token de seguridad")
            usuario = st.text_input("Usuario")
            contraseña = st.text_input("Contraseña", type="password")
            nombre = st.text_input("Nombre")
            telefono = st.text_input("Teléfono")
            enviar = st.form_submit_button("Crear")

        if enviar:
            exito = controlador.crear_usuario(usuario, contraseña, tipo, nombre, telefono,token)
            if exito:
                st.success("Cuenta creada exitosamente")
            else:
                st.error("No se pudo crear la cuenta")

        if st.button("Volver al inicio"):
            st.session_state["pantalla"] = "inicio"
            st.rerun()

    def mostrar_menu():
        tipo = st.session_state.get("tipo_usuario", "")
        # Definición de opciones según tipo de usuario
        if tipo == "Administrador":
            opciones = ["Inicio", "Casinos", "Máquinas", "Contadores", "Cuadre Casino", "Cuadre Máquina","Reportes","Usuarios","Configuracion"]
        elif tipo == "Soporte":
            opciones = ["Inicio", "Casinos", "Máquinas"]
        elif tipo == "Operador":
            opciones = ["Inicio", "Contadores", "Cuadre Casino", "Cuadre Máquina","reportes"]
        else:
            st.error("Tipo de usuario inválido")
            return

        opcion = st.sidebar.radio("Menú", opciones)
        st.session_state["vista_actual"] = opcion

        # Redirección a la vista seleccionada
        if opcion == "Inicio":
            vista_inicio()
        elif opcion == "Casinos":
            vista_casinos()
        elif opcion == "Máquinas":
            vista_maquinas()
        elif opcion == "Contadores":
            vista_contadores()
        elif opcion == "Cuadre Casino":
            vista_cuadre_casino()
        elif opcion == "Cuadre Máquina":
            vista_cuadre_maquina()
        elif opcion == "Reportes":
            vista_reportes()
        elif opcion == "Usuarios":
            vista_usuarios()
        elif opcion == "Configuracion":
            vista_configuracion()
            
    def vista_inicio():
        st.title("🎲 Sistema Automatizado de Cuadre de Casino")
        st.markdown("""
        Bienvenido al sistema integral para la **gestión y control de casinos**.

        ---
        ### ¿Qué puedes hacer en este sistema?
        - **Administrar casinos:** Creacion, modificación y consulta de casinos registrados.
        - **Gestionar máquinas:** Registro, modificación y control de máquinas por casino.
        - **Control de usuarios:** Crear, modificar y gestionar permisos de acceso.
        - **Registrar contadores:** Llevar el control diario de ingresos, egresos, jackpots y billeteros.
        - **Cuadre de máquinas y casinos:** Calcular utilidades y guardar resultados históricos.
        - **Generar reportes:** Descarga informes personalizados, globales y consolidados en PDF o Excel.
        - **Configuración:** Personaliza la interfaz y los datos de la empresa.

        ---
        > Utiliza el menú lateral para navegar por los diferentes módulos del sistema.
        """)
        st.info("Para comenzar, selecciona una opción en el menú de la izquierda.")
        if st.button("cerrar sesion"):
            st.session_state["pantalla"] = "inicio"
            if "gestor" in st.session_state:
                del st.session_state["gestor"]
            st.rerun()

    # Módulos específicos
    def vista_casinos():
        st.header("Agregar Casino")
        # Crear Casino
        with st.form(key="form_agregar_casino", clear_on_submit=True):
            nombre = st.text_input("Nombre del casino")
            direccion = st.text_input("Dirección")
            codigo = st.number_input("Código", min_value=0, step=1)
            enviar = st.form_submit_button("Registrar Casino")
        if enviar:
            ok = controlador.agregar_casino(nombre, direccion, int(codigo))
            if ok :
                st.rerun()
            else:
                st.error("Error al registrar casino")

        # Modificar Casino
        casinos = controlador.listar_casinos()
        if casinos:
            st.subheader("Lista Casinos")
            df = pd.DataFrame([c.to_dict() for c in casinos])
            st.dataframe(df)
            cods = [c.codigo for c in casinos]
            st.header("Modificar Casino")
            with st.form(key="form_modificar_casino", clear_on_submit=True):
                sel = st.selectbox("Selecciona código", cods)
                attr = st.selectbox("Atributo a modificar", ["nombre", "direccion"])
                nuevo = st.text_input("Nuevo valor")
                enviar_mod = st.form_submit_button("Modificar Casino")
            if enviar_mod:
                ok = controlador.modificar_casino(int(sel), attr, nuevo)
                if ok:
                    st.rerun()
                else:
                    st.error("Error al modificar casino")
                
            st.header("Activar/Desactivar Casino")
            with st.form(key="form_modificar_estado_casino",clear_on_submit=True):
                sel2 = st.selectbox("Selecciona código", cods)
                boton_activar=st.form_submit_button("Activar")
                boton_desactivar=st.form_submit_button("desactivar")
            if boton_activar:      
                if controlador.activar_casino(int(sel2)) :
                    st.rerun()
                else:
                    st.error("Error al activar el casino")
                    
            if boton_desactivar:
                if controlador.desactivar_casino(int(sel2)) :
                    st.rerun()    
                else:
                    st.error("Error al desactivar el casino")
        else:
            st.warning("No hay casinos registardos")
        
        
    def vista_maquinas():
        st.header("Agregar Maquina")
        # Crear Máquina
        with st.form(key="form_agregar_maquina", clear_on_submit=True):
            marca = st.text_input("Marca")
            modelo = st.text_input("Modelo")
            serial = st.text_input("Serial")
            asset = st.number_input("Asset", min_value=0, step=1)
            codigo_casino = st.number_input("Código Casino", min_value=0, step=1)
            denominacion = st.number_input("Denominación", min_value=0.0, step=0.01)
            enviar = st.form_submit_button("Registrar Máquina")
        if enviar:
            ok = controlador.agregar_maquina(marca, modelo, serial, int(asset), int(codigo_casino), float(denominacion))
            if ok:
                st.rerun()
            else:
                st.error("Error al registrar máquina")

        # Modificar Máquina
        # Pedimos primero el casino para listar
        maquinas = controlador.lista_maquinas()
        if maquinas:
            st.subheader("Lista Maquinas")
            df = pd.DataFrame([m.to_dict() for m in maquinas])
            st.dataframe(df)
            st.header("Modificar Maquina")
            assets = [m.asset for m in maquinas]
            with st.form(key="form_modificar_maquina", clear_on_submit=True):
                sel = st.selectbox("Selecciona Asset", assets)
                attr = st.selectbox("Atributo a modificar", ["marca", "modelo", "serial", "asset","casino"])
                nuevo = st.text_input("Nuevo valor")
                enviar_mod = st.form_submit_button("Modificar Máquina")
            if enviar_mod:
                # Conversión de tipo
                if attr in ["asset","casino"]:
                    val = int(nuevo)
                else:
                    val = nuevo
                ok = controlador.modificar_maquina(int(sel), attr, val)
                if ok:
                    st.rerun()    
                else:
                    st.error("Error al modificar máquina")
            st.header("Activar/Desactivar Maquina")
            with st.form(key="form_modificar_estado_maquina",clear_on_submit=True):
                sel2 = st.selectbox("Selecciona Asset", assets)
                boton_activar=st.form_submit_button("Activar")
                boton_desactivar=st.form_submit_button("desactivar")
            if boton_activar:
                if controlador.activar_maquina(int(sel2)):
                    st.rerun()    
                else:
                    st.error("Error al activar la maquina")
            if boton_desactivar:
                if controlador.desactivar_maquina(int(sel2)) :
                    st.rerun()    
                else:
                    st.error("Error al desactivar la maquina")    
        else:
            st.warning("No hay maquinas registradas")

    def vista_contadores():
        st.header("Agregar Contador")
        casinos = controlador.listar_casinos()
        if casinos:
            codigos = [c.codigo for c in casinos]
            cas_cod = st.selectbox("Filtrar por casino", codigos)  
            maquinas= controlador.listar_maquinas(cas_cod)  
            assets=[m.asset for m in maquinas] 
            if maquinas: 
                with st.form(key="form_agregar_contador", clear_on_submit=True):
                    fecha = st.date_input("Fecha")
                    asset = st.selectbox("Asset Máquina",assets)
                    in_ = st.number_input("In", min_value=0.0, step=0.01)
                    out = st.number_input("Out", min_value=0.0, step=0.01)
                    jackpot = st.number_input("Jackpot", min_value=0.0, step=0.01)
                    billetero = st.number_input("Billetero", min_value=0.0, step=0.01)
                    enviar = st.form_submit_button("Agregar Registro")
                if enviar:
                    ok = controlador.agregar_registro_contador( fecha, int(asset), int(cas_cod), float(in_), float(out), float(jackpot), float(billetero))
                    st.success("Registro agregado") if ok else st.error("Error al agregar registro")
            else:
                st.warning("No hay maquinas registradas en el casino")
        else:
            st.warning("No hay casinos agregados")

        # Modificar Contador
        registros = controlador.listar_contadores()
        codigos_contadores={r.codigo: r for r in registros}
        if registros:
            cods = [(r.codigo,str(r.fecha)) for r in registros]
            st.header("Modificar Contador")
            sel = st.selectbox("Selecciona el codigo", cods)
            contador=codigos_contadores[int(sel[0])]
            actuales={"in":contador.in_,"out":contador.out,"jackpot":contador.jackpot,"billetero":contador.billetero}
            with st.form(key="form_modificar_contador", clear_on_submit=True):
                attr = st.selectbox("Atributo a modificar", ["in", "out", "jackpot", "billetero"])
                st.write(f"Contadores actuales:")
                st.write(f"in: {actuales["in"]}")
                st.write(f"out: {actuales["out"]}")
                st.write(f"jackpot: {actuales["jackpot"]}") 
                st.write(f"billetero: {actuales["billetero"]}")
                nuevo = st.number_input("Nuevo valor", min_value=0.0, step=0.01)
                enviar_mod = st.form_submit_button("Modificar Contador")
            if enviar_mod:
                val = float(nuevo)
                if val<actuales[attr]:
                    st.error("Nuevo valor menor al actual")
                else:
                    val = float(nuevo)
                    ok = controlador.modificar_contador(sel[0], attr, val)
                    if ok:
                        st.rerun()    
                    else:
                        st.error("Error al modificar contador")
        else:
            st.warning("No hay contadores registrados")

    def vista_cuadre_maquina():
        st.header("Cuadre por Máquina")
        casinos = controlador.listar_casinos()
        if casinos:
            maquinas = controlador.lista_maquinas()
            if maquinas:
                assets=[maquina.asset for maquina in maquinas]
                with st.form(key="form_cuadre_maquina", clear_on_submit=True):
                    inicio = st.date_input("Fecha inicio")
                    fin = st.date_input("Fecha fin")
                    asset = st.selectbox("Asset Máquina", assets)
                    enviar = st.form_submit_button("Calcular Cuadre")
                if enviar:
                    if inicio>fin or inicio==fin:
                        st.error("Fechas no validas")
                    else:         
                        contadores = controlador.calculo_total_contadores(inicio, fin, int(asset))
                        utilidad= controlador.calculo_utilidad_maquina(inicio,fin,int(asset))
                        ok = controlador.guardar_resultados_maquina(contadores, utilidad, int(asset),f"{str(inicio)}/{str(fin)}")
                        if ok:
                            st.write(f"Contadores totales:")
                            st.write(f"in: {contadores[0]}")
                            st.write(f"out: {contadores[1]}")
                            st.write(f"jackpot: {contadores[2]}")
                            st.write(f"billetero: {contadores[3]}")
                            st.write(f"Utilidad: {utilidad}")
                            st.success("Resultados guardados") 
                        else:
                            st.error("Error al guardar resultados")
            else:
                st.warning("No hay maquinas registradas en este casino")
        else:
            st.warning("No hay casinos agregados")

    def vista_cuadre_casino():
        st.header("Cuadre por Casino")
        casinos = controlador.listar_casinos()
        codigos = [c.codigo for c in casinos]
        if casinos:
            cas_cod = st.selectbox("Código Casino", codigos)
            maquinas = controlador.listar_maquinas(int(cas_cod)) if cas_cod else []
            if maquinas:
                with st.form(key="form_cuadre_casino", clear_on_submit=True):
                    inicio = st.date_input("Fecha inicio")
                    fin = st.date_input("Fecha fin")
                    enviar = st.form_submit_button("Calcular Cuadre")
                if enviar:
                    if inicio>fin or inicio==fin:
                        st.error("Fechas no validas")
                    else:
                        contadores=controlador.total_contadores_por_casino(inicio, fin, int(cas_cod))
                        utilidad = controlador.calculo_utilidad_por_casino(inicio, fin, int(cas_cod))
                        ok = controlador.guardar_resultados_casino(contadores, utilidad, int(cas_cod),f"{str(inicio)}/{str(fin)}")
                        if ok:    
                            st.write(f"Contadores totales:")
                            st.write(f"in: {contadores[0]}")
                            st.write(f"out: {contadores[1]}")
                            st.write(f"jackpot: {contadores[2]}")
                            st.write(f"billetero: {contadores[3]}")
                            st.write(f"Utilidad: {utilidad}")
                            st.success("Resultados guardados")
                        else:
                            st.error("Error al guardar resultados")
            else:
                st.warning("No hay maquinas registradas en este casino")
        else:
            st.warning("No hay casinos agregados")

    def vista_reportes():
        st.header("Generar Reporte")
        tipo_reporte = st.selectbox("Tipo de reporte", [
            "Personalizado", "Global Máquina", "Global Casino", "Consolidado", "Especial"
        ])
        formato = st.selectbox("Formato", ["PDF", "Excel"])
        nombre = st.text_input("Nombre archivo")
        casinos = controlador.listar_casinos()  
        
        if tipo_reporte == "Personalizado":
            if casinos:
                st.subheader("Filtros para máquinas")
                filtros_maquina = st.multiselect("Campos de máquina", ["serial", "asset", "marca", "modelo", "denominacion"])
                st.subheader("Filtros para casinos")
                filtros_casino = st.multiselect("Campos de casino", ["nombre", "codigo", "direccion"])
                fecha_inicio = st.date_input("Fecha inicio")
                fecha_fin = st.date_input("Fecha fin")
                if st.button("Generar reporte"):
                    if fecha_inicio>fecha_fin or fecha_inicio==fecha_fin:
                        st.error("Fechas no validas")
                    else:
                        archivo = controlador.generar_reporte_personalizado(
                            filtros_maquina, filtros_casino, fecha_inicio, fecha_fin, formato.lower(),nombre
                        )
                        if archivo:
                            with open(archivo, "rb") as f:
                                bytes_data = f.read()
                            st.download_button(
                                label=f"Descargar reporte {formato}",
                                data=bytes_data,
                                file_name=f"{nombre}.{ 'pdf' if formato=='PDF' else 'xlsx'}",
                                mime="application/pdf" if formato=="PDF" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )
                        else:
                            st.error("No se pudo generar el reporte.")
            else:
                st.warning("No hay casinos agregados")
        elif tipo_reporte == "Global Máquina":
            if casinos:
                st.subheader("Seleccion Maquina")
                todas_maquinas = []
                for casino in casinos:
                    todas_maquinas.extend(controlador.listar_maquinas(casino.codigo))
                # Crear lista de opciones: (asset y casino)
                opciones = [f"{m.asset} (Casino {m.casino.codigo})" for m in todas_maquinas]
                asset_map = {f"{m.asset} (Casino {m.casino.codigo})": m.asset for m in todas_maquinas}
                seleccion = st.multiselect("Assets disponibles", opciones)
                assets_maquinas = [asset_map[op] for op in seleccion]
                if st.button("Generar reporte"):
                    archivo = controlador.generar_reporte_individual_maquina(list(map(int,assets_maquinas)),formato.lower(),nombre)
                    if archivo:
                        with open(archivo, "rb") as f:
                            bytes_data = f.read()
                        st.download_button(
                            label=f"Descargar reporte {formato}",
                            data=bytes_data,
                            file_name=f"{nombre}.{ 'pdf' if formato=='PDF' else 'xlsx'}",
                            mime="application/pdf" if formato=="PDF" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                    else:
                        st.error("No se pudo generar el reporte")
            else:
                st.warning("No hay casinos agregados") 
                
        elif tipo_reporte == "Global Casino":
            st.subheader("Seleccion Casino")
            if casinos:
                codigos = [c.codigo for c in casinos]
                casinos_codigos = st.multiselect("Codigo",codigos)
                if st.button("Generar reporte"):
                    archivo = controlador.generar_reporte_individual_casino(list(map(int,casinos_codigos)),formato.lower(),nombre)
                    if archivo:
                        with open(archivo, "rb") as f:
                            bytes_data = f.read()
                        st.download_button(
                            label=f"Descargar reporte {formato}",
                            data=bytes_data,
                            file_name=f"{nombre}.{ 'pdf' if formato=='PDF' else 'xlsx'}",
                            mime="application/pdf" if formato=="PDF" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                    else:
                        st.error("No se pudo generar el reporte")
            else:
                st.warning("No hay casinos agregados")
        elif tipo_reporte == "Consolidado":
            if casinos:
                st.subheader("Seleccion Fechas")
                fecha_inicio = st.date_input("Fecha inicio")
                fecha_fin = st.date_input("Fecha fin")
                if st.button("Generar reporte"):
                    if fecha_inicio>fecha_fin or fecha_inicio==fecha_fin:
                        st.error("Fechas no validas")
                    else:
                        archivo = controlador.generar_reporte_consolidado(
                            fecha_inicio, fecha_fin, formato.lower(),nombre
                        )
                        if archivo:
                            with open(archivo, "rb") as f:
                                bytes_data = f.read()
                            st.download_button(
                                label=f"Descargar reporte {formato}",
                                data=bytes_data,
                                file_name=f"{nombre}.{ 'pdf' if formato=='PDF' else 'xlsx'}",
                                mime="application/pdf" if formato=="PDF" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )
                        else:
                            st.error("No se pudo generar el reporte.")
            else:
                st.warning("No hay casinos agregados")
        elif tipo_reporte == "Especial":
            if casinos:
                st.subheader("Seleccion de maquinas")
                codigos = [c.codigo for c in casinos]
                casino_codigo = st.selectbox("Filtrar por casino",codigos)
                maquinas= controlador.listar_maquinas(casino_codigo)
                if maquinas:
                    assets=[m.asset for m in maquinas]
                    assets_maquinas=st.multiselect("Assets",assets)
                    porcentaje = st.number_input("Porcentaje participacion",min_value=0.0, step=0.01)
                    inico=st.date_input("Fecha incio")
                    fin=st.date_input("Fecha fin")
                    if st.button("Generar reporte"):
                        archivo = controlador.generar_reporte_especial(inico,fin,int(casino_codigo),list(map(int,assets_maquinas)),float(porcentaje),formato.lower(),nombre)
                        #mirar de que tipo se necesitan los assets
                        if archivo:
                            with open(archivo, "rb") as f:
                                bytes_data = f.read()
                            st.download_button(
                                label=f"Descargar reporte {formato}",
                                data=bytes_data,
                                file_name=f"{nombre}.{ 'pdf' if formato=='PDF' else 'xlsx'}",
                                mime="application/pdf" if formato=="PDF" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )
                        else:
                            st.error("No se pudo generar el reporte")
                else:
                    st.warning("No hay maquinas asociadas al casino")
            else:
                st.warning("No hay casinos agregados")
        else:
            st.error("Tipo de reporte invalido")

    def vista_usuarios():
        st.subheader("Lista usuarios")
        df=pd.DataFrame([u.to_dict() for u in controlador.lista_usuarios()])
        st.dataframe(df)
        st.header("Modificar usuario")
        with st.form(key="form_modificar_user"):
            atributo = st.selectbox("Atributo a modificar", ["usuario", "contraseña", "nombre", "telefono"])
            usuario = st.text_input("Usuario")
            nuevo_dato= st.text_input("Nuevo valor")
            modificar=st.form_submit_button("Modificar usuario")
        if modificar:
            ok=controlador.modificar_usuario(usuario,atributo,nuevo_dato)
            if ok:
                st.rerun()    
            else:
                st.error("Error al modificar el usuario")
        
        st.header("Activar/Desactivar Usuario")
        with st.form(key="form_modificar_estado_usuario",clear_on_submit=True):
            name_user=st.text_input("Usuario")
            boton_activar=st.form_submit_button("Activar")
            boton_desactivar=st.form_submit_button("desactivar")
            if boton_activar:
                if controlador.activar_usuario(name_user):
                    st.rerun()
                else:
                    st.error("Error al activar el usuario")
            if boton_desactivar:
                if controlador.desactivar_usuario(name_user):
                    st.rerun()
                else:
                    st.error("Error al desactivar el usuario")
        

    def vista_configuracion():
        st.header("Configuración de la interfaz")
        with st.form(key="form_tema"):
            primary = st.color_picker("Color de botones", st.session_state["theme_primary"])
            background = st.color_picker("Color de fondo", st.session_state["theme_background"])
            secondary = st.color_picker("Color de menu", st.session_state["theme_secondary"])
            aplicar = st.form_submit_button("Aplicar cambios")
        if aplicar:
            st.session_state["theme_primary"] = primary
            st.session_state["theme_background"] = background
            st.session_state["theme_secondary"] = secondary
            guardar_configuracion_tema(primary, background, secondary)
            st.rerun()
            
        st.header("Configuracion Token")
        with st.form(key="form_token",clear_on_submit=True):
            token = st.text_input("Nuevo token")
            cambiar = st.form_submit_button("Cambiar token")
        if cambiar:
            ok = controlador.modificar_token(token)
            st.success("Token modificado exitosamente") if ok else st.error("Error al modificar el token")
            
        st.header("Configuracion datos de la empresa")
        with st.form(key="form_company_data",clear_on_submit=True):
            nombre=st.text_input("Nombre")
            telefono=st.text_input("Telefono")
            nit=st.text_input("NIT")
            direccion=st.text_input("Direccion")
            enviar=st.form_submit_button("Enviar")
        if enviar:
            respuesta=controlador.modificar_datos_empresa(nombre,telefono,nit,direccion)
            st.success("Datos modificados exitosamente") if respuesta else st.error("Error al modificar los datos")
         
        st.header("Logo de la empresa")
        with st.form(key="form_logo", clear_on_submit=True):
            imagen = st.file_uploader("Selecciona una imagen para la empresa", type=["png", "jpg", "jpeg"])
            subir = st.form_submit_button("Subir imagen")
        if subir and imagen:
            ruta_logo = os.path.join(BASE_DIR,"Data","logo_casino.png")
            with open(ruta_logo, "wb") as f:
                f.write(imagen.read())
            st.success("Logo actualizado exitosamente")
            
    
    # Enrutamiento final
    if st.session_state["pantalla"] == "inicio":
        mostrar_login()
    elif st.session_state["pantalla"] == "crear_cuenta":
        mostrar_crear_cuenta()
    elif st.session_state["pantalla"] == "menu":
        mostrar_menu()
