from back.src.GestorPrincipal import GestorPrincipal

gestor = None

def set_gestor(global_gestor:GestorPrincipal):
    global gestor
    gestor = global_gestor

# -------------------- Métodos para Casinos --------------------

def agregar_casino(nombre: str, direccion: str, codigo: int) -> bool:
    return gestor.agregar_casino(nombre, direccion, codigo)

def modificar_casino(codigo: int, atributo: str, nuevo_dato: any) -> bool:
    return gestor.mosdificar_casino(codigo, atributo, nuevo_dato)

def activar_casino(codigo: int) -> bool:
    return gestor.activar_casino(codigo)

def desactivar_casino(codigo: int) -> bool:
    return gestor.desactivar_casino(codigo)

def filtrar_casinos(filtro: str) -> list:
    return gestor.filtrar_casinos(filtro)

def listar_casinos() -> list:
    return gestor.lista_casinos()

# -------------------- Métodos para Máquinas --------------------

def agregar_maquina(marca: str, modelo: str, serial: str, asset: int, codigo_casino: int, denominacion: float) -> bool:
    return gestor.agregar_maquina(marca, modelo, serial, asset, codigo_casino, denominacion)

def modificar_maquina(asset: int, atributo: str, nuevo_dato: any) -> bool:
    return gestor.modificar_maquina(asset, atributo, nuevo_dato)

def activar_maquina(asset: int) -> bool:
    return gestor.activar_maquina(asset)

def desactivar_maquina(asset: int) -> bool:
    return gestor.desactivar_maquina(asset)

def listar_maquinas(casino_codigo: int) -> list:
    return gestor.lista_maquinas_por_casino(casino_codigo)

def lista_maquinas():
    return gestor.lista_maquinas()

# -------------------- Métodos para Contadores --------------------

def agregar_registro_contador( fecha: str, maquina_asset: int, casino_codigo: int, in_: float, out: float, jackpot: float, billetero: float) -> bool:
    return gestor.agregar_registro_contador(fecha, maquina_asset, casino_codigo, in_, out, jackpot, billetero)

def modificar_contador(codigo:int, atributo: str, nuevo_dato: any) -> bool:
    return gestor.modificar_contador(codigo, atributo, nuevo_dato)

def mostrar_contadores(fecha_inicio: str, fecha_fin: str) -> tuple:
    return gestor.mostrar_contadores(fecha_inicio, fecha_fin)

def listar_contadores() -> list:
    return gestor.lista_contadores()

# -------------------- Métodos para Cuadre por Máquina --------------------

def calculo_total_contadores(fecha_inicio: str, fecha_fin: str, asset_maquina: int) -> tuple:
    return gestor.calculo_total_contadores(fecha_inicio, fecha_fin, asset_maquina)

def calculo_utilidad_maquina(fecha_inicio: str, fecha_fin: str, asset_maquina: int) -> float:
    return gestor.calculo_utilidad_maquina(fecha_inicio, fecha_fin, asset_maquina)

def guardar_resultados_maquina(contadores: tuple, utilidad: float, asset_maquina: int) -> bool:
    return  gestor.guardar_resultados_maquina(contadores, utilidad, asset_maquina)

# -------------------- Métodos para Cuadre por Casino --------------------

def total_contadores_por_casino(fecha_inicio: str, fecha_fin: str, codigo_casino: int) -> tuple:
    return gestor.total_contadores_por_casino(fecha_inicio, fecha_fin, codigo_casino)

def calculo_utilidad_por_casino(fecha_inicio: str, fecha_fin: str, codigo_casino: int) -> float:
    return gestor.calculo_utilidad_por_casino(fecha_inicio, fecha_fin, codigo_casino)

def guardar_resultados_casino(contadores: tuple, utilidad: float, codigo_casino: int) -> bool:
    return gestor.guardar_resultados_casino(contadores, utilidad, codigo_casino)

# -------------------- Métodos para Reportes --------------------

def generar_reporte_personalizado(filtros_maquina, filtros_casino, fecha_inicio, fecha_fin, formato,nombre) -> object:
    resultado = gestor.generar_reporte_personalizado(filtros_maquina, filtros_casino, fecha_inicio, fecha_fin, formato,nombre)
    if resultado:
        return resultado
    return None

def generar_reporte_individual_maquina(asset_maquina, formato,nombre) -> object:
    resultado = gestor.generar_reporte_individual_maquina(asset_maquina, formato,nombre)
    if resultado:
        return resultado
    return None

def generar_reporte_individual_casino(codigos_casinos, formato,nombre) -> object:
    resultado = gestor.generar_reporte_individual_casino(codigos_casinos, formato,nombre)
    if resultado:
        return resultado
    return None

def generar_reporte_consolidado(fecha_inicio, fecha_fin, formato,nombre) -> object:
    resultado = gestor.generar_reporte_consolidado(fecha_inicio, fecha_fin, formato,nombre)
    if resultado:
        return resultado
    return None

def generar_reporte_especial(codigo_casino, asset_maquinas, porcentaje, formato,nombre) -> object:
    resultado = gestor.generar_reporte_especial(codigo_casino, asset_maquinas, porcentaje, formato,nombre)
    if resultado:
        return resultado
    return None

# -------------------- Métodos para Usuarios --------------------

def crear_usuario(usuario: str, contraseña: str, tipo: str, nombre: str, telefono: str, token: str) -> bool:
    return gestor.crear_usuario(usuario, contraseña, nombre, telefono,tipo,token)

def login_usuario(usuario:str,contraseña:str):
    return gestor.login_usuario(usuario,contraseña)

def modificar_usuario(usuario: str, atributo: str, nuevo_dato: any)-> bool:
    return gestor.modificar_usuario(usuario, atributo, nuevo_dato)

def activar_usuario(usuario: int) -> bool:
    return gestor.activar_usuario(usuario)

def desactivar_usuario(usuario: int) -> bool:
    return gestor.desactivar_usuario(usuario)

def lista_usuarios():
    return gestor.lista_usuarios()

# -------------------- Métodos para Configuracion --------------------

def modificar_token(token):
    return gestor.modificar_token(token)

def modificar_datos_empresa(nombre,telefono,nit,direccion):
    return gestor.modificar_datos_empresa(nombre,telefono,nit,direccion)