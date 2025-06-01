from back.src.Contador.Contador import Contador
from util import GestorArchivos
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PATH_FILE=os.path.join(BASE_DIR,"Data","Contadores.csv")

class GestorContador:
    
    def __init__(self):
        self.__contadores=[]
    
    def set_contadores(self,lista_contadores):
        self.__contadores=lista_contadores
        
    def buscar_contador(self,codigo)->object:
        contadores={contador.codigo:contador for contador in self.__contadores}
        return contadores.get(codigo,None)
    
    def agregar_registro_contador(self,fecha,maquina,casino,in_,out,jackpot,billetero)->bool:
        try:
            codigo=max([c.codigo for c in self.__contadores])+1
            GestorArchivos.escribir_csv(PATH_FILE,[{"codigo":codigo,"fecha":fecha,"maquina":maquina.asset,"casino":casino.codigo,"in":in_,"out":out,"jackpot":jackpot,"billetero":billetero}])
            self.__contadores.append(Contador(codigo,fecha,maquina,casino,in_,out,jackpot,billetero))
            return True
        except Exception:
            return False   
    
    def modificar_contador(self,codigo,atributo,nuevo_dato)->bool:
        contador=self.buscar_contador(codigo)
        if not contador:
            return False
        try:
            if atributo=="in":
                contador.in_=nuevo_dato
            elif atributo=="out":
                contador.out=nuevo_dato
            elif atributo=="jackpot":
                contador.jackpot=nuevo_dato
            elif atributo=="billetero":
                contador.billetero=nuevo_dato
            else:
                return False
            GestorArchivos.modificar(PATH_FILE,"codigo",str(codigo),atributo,nuevo_dato)
            return True
        except Exception:
            return False
    
    def mostrar_contadores_por_rango(self,fecha_inicio,fecha_fin)->tuple:
        contadores=tuple(filter(lambda contador: contador.fecha>=fecha_inicio and contador.fecha<=fecha_fin,self.__contadores))
        return contadores
    
    def lista_contadores(self)->list:
        return self.__contadores
