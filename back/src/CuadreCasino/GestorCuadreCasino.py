from back.src.CuadreCasino.CuadreCasino import CuadreCasino
from util import GestorArchivos
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PATH_FILE=os.path.join(BASE_DIR,"Data","CuadrePorCasino.csv")

class GestorCuadreCasino:
    
    def __init__(self):
        self.__cuadre_casino=[]
        
    def set_cuadre_casinos(self,lista_cuadre_casinos):
        self.__cuadre_casino=lista_cuadre_casinos  
    
    
    def sumar_contadores(self,contadores):
        suma = {"in_": 0, "out": 0, "jackpot": 0, "billetero": 0}
        for c in contadores:
            suma["in_"] += c.in_
            suma["out"] += c.out
            suma["jackpot"] += c.jackpot
            suma["billetero"] += c.billetero
        return suma
    
    def total_contadores_por_casino(self,fecha_inicio,fecha_fin,codigo_casino,lista_contadores)->tuple:
        inicicial=list(filter(lambda contador: contador.casino.codigo==codigo_casino and contador.fecha==fecha_inicio,lista_contadores))
        final=list(filter(lambda contador: contador.casino.codigo==codigo_casino and contador.fecha==fecha_fin,lista_contadores))
        if not inicicial or not final:
            return None
        contadores_iniciales=self.sumar_contadores(inicicial)
        contadores_finales=self.sumar_contadores(final)
        contadores=(
            contadores_finales["in_"]-contadores_iniciales["in_"],
            contadores_finales["out"]-contadores_iniciales["out"],
            contadores_finales["jackpot"]-contadores_iniciales["jackpot"],
            contadores_finales["billetero"]-contadores_iniciales["billetero"]
        )
        return tuple(map(lambda x: abs(round(x,1)),contadores))
        
    
    def calculo_utilidad_por_casino(self,fecha_inicio,fecha_fin,codigo_casino,lista_contadores)->float:
        inicicial=list(filter(lambda contador: contador.casino.codigo==codigo_casino and contador.fecha==fecha_inicio,lista_contadores))
        final=list(filter(lambda contador: contador.casino.codigo==codigo_casino and contador.fecha==fecha_fin,lista_contadores))
        if not inicicial or not final:
            return None
        contadores_iniciales=self.sumar_contadores(inicicial)
        contadores_finales=self.sumar_contadores(final)
        total_in_=contadores_finales["in_"]-contadores_iniciales["in_"]
        total_out=contadores_finales["out"]-contadores_iniciales["out"]
        total_jackpot=contadores_finales["jackpot"]-contadores_iniciales["jackpot"]
        utilidad=(total_in_)-(total_out + total_jackpot)
        return round(utilidad,1)
    
    def guardar_resultados(self,contadores:tuple,utilidad,casino:object,fecha:str):
        if not contadores or not utilidad:
            return False
        try:
            in_,out,jackpot,billetero=contadores
            GestorArchivos.escribir_csv(PATH_FILE,[{"in":in_,"out":out,"jackpot":jackpot,"billetero":billetero,"utilidad":utilidad,"casino":casino.codigo,"fecha":fecha}])
            self.__cuadre_casino.append(CuadreCasino(in_,out,jackpot,billetero,utilidad,casino,fecha))
            return True
        except:
            return False

    def lista_cuadre_casino(self)->list:
        return self.__cuadre_casino