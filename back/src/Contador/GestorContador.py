from back.src.Contador.Contador import Contador
from util import GestorArchivos


class GestorContador:
    
    def __init__(self):
        self.__contadores=[]
        
    def buscar_contador(self,codigo)->object:
        contadores={contador.codigo:contador for contador in self.__contadores}
        return contadores.get(codigo,None)
    
    def agregar_registro_contador(self,codigo,fecha,maquina,casino,in_,out,jackpot,billetero)->bool:
        try:
            GestorArchivos.escribir_csv("CASINO/Data/Contadores.csv",[{"codigo":codigo,"fecha":fecha,"maquina":maquina.asset,"casino":casino.codigo,"in":in_,"out":out,"jackpot":jackpot,"billetero":billetero}])
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
            GestorArchivos.modificar("CASINO/Data/Contadores.csv","codigo",str(codigo),atributo,nuevo_dato)
            return True
        except Exception:
            return False
    
    def mostrar_contadores_por_rango(self,fecha_inicio,fecha_fin)->tuple:
        contadores=tuple(filter(lambda contador: contador.fecha>=fecha_inicio and contador.fecha<=fecha_fin,self.__contadores))
        return contadores
    
    def lista_contadores(self)->list:
        return self.__contadores
