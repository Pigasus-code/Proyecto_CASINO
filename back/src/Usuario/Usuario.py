from abc import ABC, abstractmethod

class Usuario(ABC):
    
    def __init__(self,usuario:str,contraseña:str,nombre:str,telefono:str,tipo:str,estado:str):
        self.__usuario=usuario
        self.__contraseña=contraseña
        self.__nombre=nombre
        self.__telefono=telefono
        self.__tipo=tipo
        self.__estado=estado
        
    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self,usuario):
        self.__usuario=usuario
    
    @property
    def contraseña(self):
        return self.__contraseña
    
    @contraseña.setter
    def contraseña(self,contraseña):
        self.__contraseña=contraseña
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
        
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,telefono):
        self.__telefono=telefono
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def estado(self):
        return self.__estado
        
    @abstractmethod
    def __str__(self):
        pass
    
    def activar(self)->bool:
        if self.__estado=="Inactivo":
            self.__estado="Activo"
            return True
        else:
            return False
    
    def desactivar(self)->bool:
        if self.__estado=="Activo":
            self.__estado="Inactivo"
            return True
        else:
            return False
    
    def to_dict(self):
        return {
            "usuario":self.usuario,
            "contraseña":self.contraseña,
            "nombre":self.nombre,
            "telefono":self.telefono,
            "tipo":self.tipo,
            "estado":self.estado
        }