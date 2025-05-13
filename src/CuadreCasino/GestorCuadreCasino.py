from src.CuadreCasino.CuadreCasino import CuadreCasino

class GestorCuadreCasino:
    
    def __init__(self):
        self.__cuadre_casino=[]
        
    def total_contadores_por_casino(self,fecha_inicio,fecha_fin,codigo_casino,lista_contadores)->tuple:
        """
        se debe calcular el total de los contadores de todas las maquina de un casino.
        debe retornar una tupla con el valor de cada contador despues de hacer el calculo
        
        """
        pass
    
    def calculo_utilidad_por_casino(self,fecha_inicio,fecha_fin,codigo_casino,lista_contadores)->float:
        """
        se debe calcular la utilidad total de un casino, esto se hace sumando las utilidades
        de cada maquina, debe retornar la utilidad
        """
        pass
    
    def guardar_resultados(self,contadores:tuple,utilidad,casino:object):
        """
        se debe agregar a la lista cuedre_casino un objeto de tipo cuadre casino
        y mandarle los atributos de cada contador (in,out,jackpot,billetero) que se resiven
        en tupla, la utilidad total del casino y el objeto casino. Tambien se debe agregar esta 
        informacion en el archivo csv para que quede un registro en la base de datos
        """
        pass

    def lista_cuadre_casino(self)->list:
        return self.__cuadre_casino