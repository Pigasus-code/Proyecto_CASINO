from back.src.Maquina.Maquina import Maquina
from util import GestorArchivos

class GestorMaquina:
    
    def __init__(self, gestor_casino):
        self.__maquinas=[]
        self.__gestor_casino=gestor_casino
    
    def set_maquinas(self,lista_maquinas):
        self.__maquinas=lista_maquinas
    
    def buscar_maquina(self,asset)->object:
        maquinas={maquina.asset:maquina for maquina in self.__maquinas}
        return maquinas.get(asset,None)
    
    def agregar_maquina(self,marca,modelo,serial,asset,casino,denominacion)->bool:
        if self.buscar_maquina(asset):
            return False
        try:
            GestorArchivos.escribir_csv("CASINO/Data/Maquinas.csv",[{"marca":marca,"modelo":modelo,"serial":serial,"asset":asset,"casino":casino.codigo,"denominacion":denominacion,"estado":"Activa"}])
            self.__maquinas.append(Maquina(marca,modelo,serial,asset,casino,denominacion))
            return True
        except Exception:
            return False  
    
    def modificar_maquina(self,asset,atributo,nuevo_dato)->bool:
        maquina=self.buscar_maquina(asset)
        if not maquina :
            return False
        try:
            if atributo=="marca":
                maquina.marca=nuevo_dato
            elif atributo=="modelo":
                maquina.modelo=nuevo_dato
            elif atributo=="serial":
                maquina.serial=nuevo_dato
            elif atributo=="asset":
                if self.buscar_maquina(nuevo_dato):
                    return False
                maquina.asset=nuevo_dato
            elif atributo=="casino":
                casino = self.__gestor_casino.buscar_casino(nuevo_dato)
                if not casino:
                    return False
                maquina.casino=casino
            else:
                return False
            GestorArchivos.modificar("CASINO/Data/Maquinas.csv","asset",str(asset),str(atributo),nuevo_dato)
            return True
        except Exception:
            return False
    
    def activar_maquina(self,asset)->bool:
        maquina=self.buscar_maquina(asset) 
        if not maquina :
            return False
        if maquina.activar():
            try:
                GestorArchivos.modificar("CASINO/Data/Maquinas.csv","asset",str(asset),"estado","Activa")
                return True
            except Exception:
                return False
        else:
            return False
    
    def desactivar_maquina(self,asset)->bool:
        maquina=self.buscar_maquina(asset) 
        if not maquina :
            return False
        if maquina.desactivar():
            try:
                GestorArchivos.modificar("CASINO/Data/Maquinas.csv","asset",str(asset),"estado","Inactiva")
                return True
            except Exception:
                return False
        else:
            return False

    def lista_maquinas(self)->list:
        return self.__maquinas