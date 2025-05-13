from src.Casino.GestorCasino import GestorCasino
from src.Maquina.GestorMaquina import GestorMaquina
from src.Contador.GestorContador import GestorContador
from src.CuadreCasino.GestorCuadreCasino import GestorCuadreCasino
from src.CuadreMaquina.GestorCuadreMaquina import GestorCuadreMaquina
from src.Reporte.GestorReporte import GestorReporte
from src.Usuario.GestorUsuario import GestorUsuario

class GestorPrincipal:
    
    def __init__(self):
        self.__gestor_maquina=GestorMaquina()
        self.__gestor_casino=GestorCasino()
        self.__gestor_contador=GestorContador()
        self.__gestor_cuadre_maquina=GestorCuadreMaquina()
        self.__gestor_cuadre_casino=GestorCuadreCasino()
        self.__gestor_reporte=GestorReporte()
        self.__gestor_usuario=GestorUsuario()
    
    #MAQUINAS
    def agregar_maquina(self,marca,modelo,serial,asset,casino,denominacion):
        pass
    
    def modificar_maquina(self,asset,atributo,nuevo_dato):
        pass

    def activar_maquina(self,asset):
        pass
    
    def desactivar_maquina(self,asset):
        pass
    
    #CASINOS
    def agregar_casino(self,nombre,direccion,codigo):
        pass
    
    def mosdificar_casino(self,codigo,atributo,nuevo_dato):
        pass
    
    def activar_casino(self,codigo):
        pass
    
    def desactivar_casino(self,codigo):
        pass
    
    def filtrar_casinos(self,filtro): #el filtro puede ser Activos / Inactivos / Todos
        pass
    
    #CONTADORES
    def lista_casinos(self):
        pass
    
    def lista_maquinas(self,casino_codigo):
        pass
    
    def agregar_registro_contador(self,fecha,maquina_asset,casino_codigo,in_,out,jackpot,billetera):
        pass
    
    def modificar_contador(self,casino_codigo,fecha,atributo,nuevo_dato):
        pass
    
    def mostrar_contadores(self,fecha_inicio,fecha_fin):
        # se debe utilizar el metodo lista de contadores de la clase GestorContador
        pass
    
    #CUADRE POR MAQUINA
    
    #lista casinos
    #lista maquinas
    #mostrar contadores
    
    def calculo_total_contadores(self,fecha_inicio,fecha_fin,asset_maquina):
        # se debe utilizar el metodo lista de contadores de la clase GestorContador
        pass
    
    def calculo_utilidad_maquina(fecha_inicio,fecha_fin,asset_maquina):
        # se debe utilizar el metodo lista de contadores de la clase GestorContador
        pass
    
    def guardar_resultados_maquina(self):
        pass
    
    
    # CUADRE POR CASINO
    
    #lista casinos
    #lista maquinas
    # mostrar contadores
    
    def total_contadores_por_casino(self,fecha_inicio,fecha_fin,codigo_casino):
        # se debe utilizar el metodo lista de contadores de la clase GestorContador
        pass
    
    def calculo_utilidad_por_casino(self,fecha_inicio,fecha_fin,codigo_casino):
        #se debe utilizar el metodo lista de contadores de la clase GestorContador
        pass
    
    def guardar_resultados_casino(self):
        pass
    
    # REPORTES
    
    def generar_reporte(self,tipo,formato):
        pass
    
    # USUARIO
    
    def crear_usuario(self,usuario,contraseña,tipo):
        pass
    