class Soporte:
    
    def __init__(self,usuario,contraseña,nombre,telefono):
        self.__usuario=usuario
        self.__contraseña=contraseña
        self.__nombre=nombre
        self.__telefono=telefono
        self.__tipo="Soporte"
        self.__estado="Activo"
        
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
    
    def __str__(self):
        return "{} {} {} {} {} {}".format(self,self.usuario,self.contraseña,self.nombre,self.telefono,self.tipo,self.estado)
    
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