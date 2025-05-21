from back.src.Usuario.Administrador import Administrador
from back.src.Usuario.Operador import Operador
from back.src.Usuario.Soporte import Soporte
from util import GestorArchivos

class GestorUsuario:
    
    def __init__(self):
        self.__usuarios=[]
        
    def buscar_usuario(self,name_usuario):
        usuarios={u.usuario:u for u in self.__usuarios }
        return usuarios.get(name_usuario,None)
        
    def crear_usuario(self,usuario,contraseña,nombre,telefono,tipo):
        if self.buscar_usuario(usuario):
            return False
        try:
            GestorArchivos.escribir_csv("CASINO/Data/Users.csv",[{"usuario":usuario,"contraseña":contraseña,"nombre":nombre,"telefono":telefono,"tipo":tipo,"estado":"Activo"}])
            if tipo=="Administrador":
                self.__usuarios.append(Administrador(usuario,contraseña,nombre,telefono))
            elif tipo=="Operador":
                self.__usuarios.append(Operador(usuario,contraseña,nombre,telefono))
            elif tipo=="Soporte":
                self.__usuarios.append(Soporte(usuario,contraseña,nombre,telefono))
            return True
        except:
            return False
    
    def modificar_usuario(self,name_usuario,atributo,nuevo_dato)->bool:
        usuario=self.buscar_usuario(name_usuario)
        if not usuario :
            return False
        try:
            if atributo=="usuario":
                if self.buscar_usuario(nuevo_dato):
                    return False
                usuario.usuario=nuevo_dato
            elif atributo=="contraseña":
                usuario.contraseña=nuevo_dato
            elif atributo=="nombre":
                usuario.nombre=nuevo_dato
            elif atributo=="telefono":
                usuario.telefono=nuevo_dato
            else:
                return False
            GestorArchivos.modificar("CASINO/Data/Users.csv","usuario",name_usuario,atributo,nuevo_dato)
            return True
        except Exception:
            return False
    
    def activar_usuario(self,name_usuario:str)->bool:
        usuario=self.buscar_usuario(name_usuario)
        if not usuario :
            return False
        if usuario.activar():
            try:
                GestorArchivos.modificar("CASINO/Data/Users.csv","usuario",name_usuario,"estado","Activo")
                return True
            except Exception:
                return False
        else:
            return False
    
    def desactivar_usuario(self,name_usuario:str)->bool:
        usuario=self.buscar_usuario(name_usuario)
        if not usuario :
            return False
        if usuario.desactivar():
            try:
                GestorArchivos.modificar("CASINO/Data/Users.csv","usuario",name_usuario,"estado","Inactivo")
                return True
            except Exception:
                return False
        else:
            return False
    