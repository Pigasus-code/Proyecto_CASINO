from back.src.Casino.Casino import Casino
from util import GestorArchivos

class GestorCasino:
    
    def __init__(self):
        self.__casinos=[]
        
    def buscar_casino(self,codigo)->object:
        casinos={casino.codigo:casino for casino in self.__casinos}
        return casinos.get(codigo,None)
    
    def agregar_casino(self,nombre,direccion,codigo)->bool:
        if self.buscar_casino(codigo):
            return False
        try:
            GestorArchivos.escribir_csv("CASINO/Data/Casinos.csv",[{"nombre":nombre,"direccion":direccion,"codigo":codigo,"estado":"Activo"}])
            self.__casinos.append(Casino(nombre,direccion,codigo))
            return True
        except Exception:
            return False   
    
    def modificar_casino(self,codigo,atributo,nuevo_dato)->bool:
        casino=self.buscar_casino(codigo)
        if not casino :
            return False
        try:
            if atributo=="nombre":
                casino.nombre=nuevo_dato
            elif atributo=="direccion":
                casino.direccion=nuevo_dato
            elif atributo=="codigo":
                if self.buscar_casino(nuevo_dato):
                    return False
                casino.codigo=nuevo_dato
            else:
                return False
            GestorArchivos.modificar("CASINO/Data/Casinos.csv","codigo",str(codigo),atributo,nuevo_dato)
            return True
        except Exception:
            return False
    
    def activar_casino(self,codigo)->bool:
        casino=self.buscar_casino(codigo) 
        if not casino :
            return False
        if casino.activar():
            try:
                GestorArchivos.modificar("CASINO/Data/Casinos.csv","codigo",str(codigo),"Estado","Activo")
                return True
            except Exception:
                return False
        else:
            return False
        
    def desactivar_casino(self,codigo)->bool:
        casino=self.buscar_casino(codigo) 
        if not casino :
            return False
        if casino.desactivar():
            try:
                GestorArchivos.modificar("CASINO/Data/Casinos.csv","codigo",str(codigo),"Estado","Inactivo")
                return True
            except Exception:
                return False
        else:
            return False
    
    def filtro_por_activos(self)->list:
        activos=list(filter(lambda casino:casino.estado=="Activo",self.__casinos))
        return activos
    
    def filtro_por_inactivos(self)->list:
        inactivos=list(filter(lambda casino:casino.estado=="Inactivo",self.__casinos))
        return inactivos
    
    def lista_casinos(self)->list:
        return self.__casinos