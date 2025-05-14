from back.src.GestorPrincipal import GestorPrincipal

gestor = GestorPrincipal()

# -------------------- Métodos para Casinos --------------------

def agregar_casino(nombre: str, direccion: str, codigo: int) -> str:
    try:
        gestor.agregar_casino(nombre, direccion, codigo)
        return "Casino agregado correctamente."
    except Exception as e:
        return f"Error al agregar el casino: {str(e)}"

def modificar_casino(codigo: int, atributo: str, nuevo_dato: any) -> str:
    try:
        gestor.mosdificar_casino(codigo, atributo, nuevo_dato)
        return "Casino modificado correctamente."
    except Exception as e:
        return f"Error al modificar el casino: {str(e)}"

def activar_casino(codigo: int) -> str:
    if gestor.activar_casino(codigo):
        return "Casino activado correctamente."
    return "Error al activar el casino."

def desactivar_casino(codigo: int) -> str:
    if gestor.desactivar_casino(codigo):
        return "Casino desactivado correctamente."
    return "Error al desactivar el casino."

def filtrar_casinos(filtro: str) -> list:
    return gestor.filtrar_casinos(filtro)

def listar_casinos() -> list:
    return gestor.lista_casinos()

# -------------------- Métodos para Máquinas --------------------

def agregar_maquina(marca: str, modelo: str, serial: str, asset: int, codigo_casino: int, denominacion: float) -> str:
    try:
        gestor.agregar_maquina(marca, modelo, serial, asset, codigo_casino, denominacion)
        return "Máquina agregada correctamente."
    except Exception as e:
        return f"Error al agregar la máquina {str(e)}"

def modificar_maquina(asset: int, atributo: str, nuevo_dato: any) -> str:
    try:
        gestor.modificar_maquina(asset, atributo, nuevo_dato)
        return "Máquina modificada correctamente."
    except Exception as e:
        return f"Error al modificar la máquina {str(e)}"

def activar_maquina(asset: int) -> str:
    if gestor.activar_maquina(asset):
        return "Máquina activada correctamente."
    return "Error al activar la máquina."

def desactivar_maquina(asset: int) -> str:
    if gestor.desactivar_maquina(asset):
        return "Máquina desactivada correctamente."
    return "Error al desactivar la máquina."

def listar_maquinas(casino_codigo: int) -> list:
    return gestor.lista_maquinas(casino_codigo)

# -------------------- Métodos para Contadores --------------------

def agregar_registro_contador(fecha: str, maquina_asset: int, casino_codigo: int, in_: float, out: float, jackpot: float, billetero: float) -> str:
    try:
        gestor.agregar_registro_contador(fecha, maquina_asset, casino_codigo, in_, out, jackpot, billetero)
        return "Registro de contador agregado correctamente."
    except Exception as e:
        return f"Error al agregar el registro de contador: {str(e)}"

def modificar_contador(casino_codigo: int, fecha: str, atributo: str, nuevo_dato: any) -> str:
    try:
        gestor.modificar_contador(casino_codigo, fecha, atributo, nuevo_dato)
        return "Registro de contador modificado correctamente."
    except Exception as e:
        return f"Error al modificar el registro de contador: {str(e)}"

def mostrar_contadores(fecha_inicio: str, fecha_fin: str) -> tuple: #retorna una tupla con dos objetos tipo contador
    return gestor.mostrar_contadores(fecha_inicio, fecha_fin)

def listar_contadores()->list:
    return gestor.lista_contadores()

# -------------------- Métodos para Cuadre por Máquina --------------------

def calculo_total_contadores(fecha_inicio: str, fecha_fin: str, asset_maquina: str) -> tuple:
    return gestor.calculo_total_contadores(fecha_inicio, fecha_fin, asset_maquina)

def calculo_utilidad_maquina(fecha_inicio: str, fecha_fin: str, asset_maquina: str) -> float:
    return gestor.calculo_utilidad_maquina(fecha_inicio, fecha_fin, asset_maquina)

def guardar_resultados_maquina(contadores: tuple, utilidad:float, asset_maquina: int) -> str:
    try:
        gestor.guardar_resultados_maquina(contadores, utilidad, asset_maquina)
        return "Resultados de máquina guardados correctamente."
    except Exception as e:
        return f"Error al guardar los resultados de máquina: {str(e)}"

# -------------------- Métodos para Cuadre por Casino --------------------

def total_contadores_por_casino(fecha_inicio: str, fecha_fin: str, codigo_casino: int) -> tuple:
    return gestor.total_contadores_por_casino(fecha_inicio, fecha_fin, codigo_casino)

def calculo_utilidad_por_casino(fecha_inicio: str, fecha_fin: str, codigo_casino: int) -> float:
    return gestor.calculo_utilidad_por_casino(fecha_inicio, fecha_fin, codigo_casino)

def guardar_resultados_casino(contadores: tuple, utilidad:float, codigo_casino: int) -> str:
    try:
        gestor.guardar_resultados_casino(contadores, utilidad, codigo_casino)
        return "Resultados de casino guardados correctamente."
    except Exception as e:
        return f"Error al guardar los resultados de casino: {str(e)}"

# -------------------- Métodos para Reportes --------------------

def generar_reporte_personalizado(filtros_maquina, filtros_casino, fecha_inicio, fecha_fin, formato)->object:
    try:
        return gestor.generar_reporte_personalizado(filtros_maquina, filtros_casino, fecha_inicio, fecha_fin, formato)
    except Exception as e:
        return f"Error al generar el reporte personalizado: {str(e)}"

def generar_reporte_individual_maquina(asset_maquina, formato)->object:
    try:
        return gestor.generar_reporte_individual_maquina(asset_maquina, formato)
    except Exception as e:
        return f"Error al generar el reporte individual de máquina: {str(e)}"

def generar_reporte_individual_casino(codigo_casino, formato)->object:
    try:
        return gestor.generar_reporte_individual_casino(codigo_casino,  formato)
    except Exception as e:
        return f"Error al generar el reporte individual de casino: {str(e)}"

def generar_reporte_consolidado( fecha_inicio, fecha_fin, formato)->object:
    try:
        return gestor.generar_reporte_consolidado( fecha_inicio, fecha_fin, formato)
    except Exception as e:
        return f"Error al generar el reporte consolidado: {str(e)}"

def generar_reporte_especial(codigo_casino, asset_maquinas, porcentaje, formato)->object:
    try:
        return gestor.generar_reporte_especial(codigo_casino, asset_maquinas, porcentaje, formato)
    except Exception as e:
        return f"Error al generar el reporte especial: {str(e)}"

# -------------------- Métodos para Usuarios --------------------

def crear_usuario(usuario: str, contraseña: str, tipo: str, nombre: str ,telefono:str) -> str:
    try:
        gestor.crear_usuario(usuario, contraseña, tipo)
        return "Usuario creado correctamente."
    except Exception as e:
        return f"Error al crear el usuario: {str(e)}"

def modificar_usuario(usuario:str ,atributo:str ,nuevo_dato:any):
    try:
        gestor.modificar_usuario(usuario,atributo,nuevo_dato)
        return "Usuario modificado correctamente"
    except Exception as e:
        return f"Error al modificar el usuario: {str(e)}"

def activar_maquina(usuario: int) -> str:
    if gestor.activar_usuario(usuario):
        return "Usuario activado correctamente"
    return "Error al activar el usuario"

def desactivar_maquina(usuario: int) -> str:
    if gestor.desactivar_usuario(usuario):
        return "Usuario desactivado correctamente"
    return "Error al desactivar el usuario"