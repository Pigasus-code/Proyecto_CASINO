from back.src.CuadreMaquina.CuadreMaquina import CuadreMaquina

class GestorCuadreMaquina:
    
    def __init__(self):
        self.__cuadre_maquina=[]
    

    def calculo_total_contadores(self,fecha_inicio,fecha_fin,asset_maquina,lista_contadores)->tuple:
        """
        se debe retornar una tupla con el calculo de los contadores (in,out,jackpot,billetero)
        de una maquina en una rango de fechas. La formula para este calculo se encuentra
        en el documento del proyecto
        """
        pass
    
    def calculo_utilidad_maquina(self,fecha_inicio,fecha_fin,asset_maquina,lista_contadores)->float:
        """
        se debe retornar el calculo de la utilidad de una mquina en una rango de fecha,
        formula para realizar este calculo se encuentra en el documento del proyecto
        """
        pass

    def guardar_resultados(self,contadores:tuple,utilidad:float,maquina:object):
        """
        se debe agregar a la lista cuedre_maquina un objeto de tipo cuadre maquina
        y mandarle los atributos de cada contador (in,out,jackpot,billetero) que se resiven
        en tupla, la utilidad de la maquina y el objeto. Tambien se debe agregar esta 
        informacion en el archivo csv para que quede un registro en la base de datos
        """
        pass
    
    def lista_cuadre_quina(self)->list:
        return self.__cuadre_maquina
    