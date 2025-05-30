from back.src.Casino.GestorCasino import GestorCasino
from back.src.Maquina.GestorMaquina import GestorMaquina
from back.src.Contador.GestorContador import GestorContador
from back.src.CuadreCasino.GestorCuadreCasino import GestorCuadreCasino
from back.src.CuadreMaquina.GestorCuadreMaquina import GestorCuadreMaquina
from back.src.Reporte.GestorReporte import GestorReporte
from back.src.Usuario.GestorUsuario import GestorUsuario
from back.src.Configuracion.GestorConfiguracion import GestorConfiguracion

class GestorPrincipal:

    def __init__(self):
        self.__gestor_casino = GestorCasino()
        self.__gestor_maquina = GestorMaquina(self.__gestor_casino)
        self.__gestor_contador = GestorContador()
        self.__gestor_cuadre_maquina = GestorCuadreMaquina()
        self.__gestor_cuadre_casino = GestorCuadreCasino()
        self.__gestor_reporte = GestorReporte()
        self.__gestor_usuario = GestorUsuario()
        self.__gestor_configuracion=GestorConfiguracion()
    
    @property
    def gestor_casino(self):
        return self.__gestor_casino

    @property
    def gestor_maquina(self):
        return self.__gestor_maquina

    @property
    def gestor_contador(self):
        return self.__gestor_contador

    @property
    def gestor_cuadre_maquina(self):
        return self.__gestor_cuadre_maquina

    @property
    def gestor_cuadre_casino(self):
        return self.__gestor_cuadre_casino

    @property
    def gestor_reporte(self):
        return self.__gestor_reporte

    @property
    def gestor_usuario(self):
        return self.__gestor_usuario
    
    @property
    def gestor_configuracion(self):
        return self.__gestor_configuracion

    # MAQUINAS

    def agregar_maquina(self, marca: str, modelo: str, serial: str, asset: int, codigo_casino: int, denominacion: float) -> bool:
        casino = self.__gestor_casino.buscar_casino(codigo_casino)
        if not casino or not marca or not modelo or not serial or not isinstance(asset, int) or not isinstance(denominacion, float):
            return False
        return self.__gestor_maquina.agregar_maquina(marca, modelo, serial, asset, casino, denominacion)

    def modificar_maquina(self, asset: int, atributo: str, nuevo_dato: any) -> bool:
        if not atributo or not nuevo_dato or not isinstance(asset, int):
            return False
        return self.__gestor_maquina.modificar_maquina(asset, atributo, nuevo_dato)

    def activar_maquina(self, asset: int) -> bool:
        return self.__gestor_maquina.activar_maquina(asset)

    def desactivar_maquina(self, asset: int) -> bool:
        return self.__gestor_maquina.desactivar_maquina(asset)

    def lista_maquinas_por_casino(self,codigo_casino) -> list:
        return self.__gestor_maquina.lista_maquinas_por_casino(codigo_casino)
    
    def lista_maquinas(self):
        return self.__gestor_maquina.lista_maquinas()

    # CASINOS

    def agregar_casino(self, nombre: str, direccion: str, codigo: int) -> bool:
        if not nombre or not direccion or not isinstance(codigo, int):
            return False
        return self.__gestor_casino.agregar_casino(nombre, direccion, codigo)

    def mosdificar_casino(self, codigo: int, atributo: str, nuevo_dato: any) -> bool:
        if not atributo or not nuevo_dato or not isinstance(codigo, int):
            return False    
        return self.__gestor_casino.modificar_casino(codigo, atributo, nuevo_dato)

    def activar_casino(self, codigo: int) -> bool:
        return self.__gestor_casino.activar_casino(codigo)

    def desactivar_casino(self, codigo: int) -> bool:
        if self.__gestor_maquina.lista_maquinas_por_casino(codigo):
            return False
        return self.__gestor_casino.desactivar_casino(codigo)

    def filtrar_casinos(self, filtro: str) -> list:
        if filtro == "Activos":
            return self.__gestor_casino.filtro_por_activos()
        elif filtro == "Inactivos":
            return self.__gestor_casino.filtro_por_inactivos()
        elif filtro == "Todos":
            return self.__gestor_casino.filtro_por_activos() + self.__gestor_casino.filtro_por_inactivos()
        return []

    def lista_casinos(self) -> list:
        return self.__gestor_casino.lista_casinos()

    # CONTADORES

    def agregar_registro_contador(self, fecha: str, maquina_asset: int, casino_codigo: int, in_: float, out: float, jackpot: float, billetera: float) -> bool:
        if not fecha or not isinstance(maquina_asset, int) or not isinstance(casino_codigo, int) or not isinstance(in_, float)  or not isinstance(out, float) or not isinstance(jackpot, float) or not isinstance(billetera, float):
            return False
        maquina = self.__gestor_maquina.buscar_maquina(maquina_asset)
        casino = self.__gestor_casino.buscar_casino(casino_codigo)
        if not maquina or not casino:
            return False
        if maquina.casino.codigo!=casino_codigo:
            return False
        return self.__gestor_contador.agregar_registro_contador( fecha, maquina, casino, in_, out, jackpot, billetera)

    def modificar_contador(self, codigo: int, atributo: str, nuevo_dato: any) -> bool:
        if not isinstance(codigo,int) or not atributo or not nuevo_dato :
            return False
        return self.__gestor_contador.modificar_contador(codigo, atributo, nuevo_dato)

    def mostrar_contadores(self, fecha_inicio: str, fecha_fin: str) -> list:
        return self.__gestor_contador.mostrar_contadores_por_rango(fecha_inicio, fecha_fin)

    def lista_contadores(self) -> list:
        return self.__gestor_contador.lista_contadores()

    # CUADRE POR MAQUINA

    def calculo_total_contadores(self, fecha_inicio: str, fecha_fin: str, asset_maquina: int) -> tuple:
        lista_contadores = self.lista_contadores()
        return self.__gestor_cuadre_maquina.calculo_total_contadores(fecha_inicio, fecha_fin, asset_maquina, lista_contadores)

    def calculo_utilidad_maquina(self, fecha_inicio: str, fecha_fin: str, asset_maquina: int) -> float:
        lista_contadores = self.lista_contadores()
        return self.__gestor_cuadre_maquina.calculo_utilidad_maquina(fecha_inicio, fecha_fin, asset_maquina, lista_contadores)

    def guardar_resultados_maquina(self, contadores: tuple, utilidad: float, asset_maquina: int) -> bool:
        if not contadores or not isinstance(utilidad, float) or not isinstance(asset_maquina, int):
            return False
        maquina = self.__gestor_maquina.buscar_maquina(asset_maquina)
        if not maquina:
            return False
        return self.__gestor_cuadre_maquina.guardar_resultados(contadores, utilidad, maquina)

    # CUADRE POR CASINO

    def total_contadores_por_casino(self, fecha_inicio: str, fecha_fin: str, codigo_casino: int) -> tuple:
        lista_contadores = self.lista_contadores()
        return self.__gestor_cuadre_casino.total_contadores_por_casino(fecha_inicio, fecha_fin, codigo_casino, lista_contadores)

    def calculo_utilidad_por_casino(self, fecha_inicio: str, fecha_fin: str, codigo_casino: int) -> float:
        lista_contadores = self.lista_contadores()
        return self.__gestor_cuadre_casino.calculo_utilidad_por_casino(fecha_inicio, fecha_fin, codigo_casino, lista_contadores)

    def guardar_resultados_casino(self, contadores: tuple, utilidad: float, codigo_casino: int) -> bool:
        if not contadores or not isinstance(utilidad, float) or not isinstance(codigo_casino, int):
            return False
        casino = self.__gestor_casino.buscar_casino(codigo_casino)
        if not casino:
            return False
        return self.__gestor_cuadre_casino.guardar_resultados(contadores, utilidad, casino)

    # REPORTES

    def generar_reporte_personalizado(self, filtros_maquina: list, filtros_casino: list, fecha_inicio: str, fecha_fin: str, formato: str, nombre: str) -> str:
        contadores = self.__gestor_contador.lista_contadores()
        return self.__gestor_reporte.generar_reporte_personalizado(filtros_maquina, filtros_casino, contadores, fecha_inicio, fecha_fin, formato, nombre)

    def generar_reporte_individual_maquina(self, assets_maquinas: list, formato: str, nombre: str) -> str:
        maquinas= self.__gestor_maquina.lista_maquinas()
        return self.__gestor_reporte.generar_reporte_individual_maquina(assets_maquinas, maquinas, formato, nombre)

    def generar_reporte_individual_casino(self, codigos_casinos: list, formato: str, nombre: str) -> str:
        casinos = self.__gestor_casino.lista_casinos()
        maquinas = self.__gestor_maquina.lista_maquinas()
        return self.__gestor_reporte.generar_reporte_individual_casino(codigos_casinos, maquinas, casinos, formato, nombre)

    def generar_reporte_consolidado(self, fecha_inicio: str, fecha_fin: str, formato: str, nombre: str) -> str:
        contadores = self.__gestor_contador.lista_contadores()
        return self.__gestor_reporte.generar_reporte_consolidado(contadores, fecha_inicio, fecha_fin, formato, nombre)

    def generar_reporte_especial(self, codigo_casino: int, asset_maquinas: list, porcentaje: float, formato: str, nombre: str) -> str:
        contadores = self.__gestor_contador.lista_contadores()
        return self.__gestor_reporte.generar_reporte_especial(codigo_casino, asset_maquinas, contadores, porcentaje, formato, nombre)

    # USUARIO

    def crear_usuario(self, usuario: str, contraseña: str, nombre: str, telefono: str, tipo: str, token: str) -> bool:
        if not usuario or not contraseña or not nombre or not telefono or not tipo:
            return False
        return self.__gestor_usuario.crear_usuario(usuario, contraseña, nombre, telefono, tipo,token)
    
    def login_usuario(self,usuario:str,contraseña:str):
        if not usuario or not contraseña:
            return False
        return self.__gestor_usuario.login_usuario(usuario,contraseña)

    def modificar_usuario(self, usuario: str, atributo: str, nuevo_dato: any) -> bool:
        if not usuario or not atributo or not nuevo_dato:
            return False
        return self.__gestor_usuario.modificar_usuario(usuario, atributo, nuevo_dato)

    def activar_usuario(self, usuario: str) -> bool:
        return self.__gestor_usuario.activar_usuario(usuario)

    def desactivar_usuario(self, usuario: str) -> bool:
        return self.__gestor_usuario.desactivar_usuario(usuario)
    
    def lista_usuarios(self):
        return self.__gestor_usuario.lista_usuarios()
    
    #CONFIGURACION
    
    def modificar_token(self,token):
        if not token:
            return False
        return self.__gestor_configuracion.modificar_token(token)
    
    def modificar_datos_empresa(self,nombre,telefono,nit,direccion):
        if not nombre or not telefono or not nit or not direccion:
            return False
        return self.__gestor_configuracion.modificar_datos_empresa(nombre,telefono,nit,direccion)