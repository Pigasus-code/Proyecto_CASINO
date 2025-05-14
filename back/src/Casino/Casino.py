class Casino:
    
    def __init__(self,nombre:str,direccion:str,codigo:str):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__codigo=codigo
        self.__estado="Activo"
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
        
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self,direccion):
        self.__direccion=direccion
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo
    
    def __str__(self):
        return "{} {} {} {}".format(self.__nombre,self.__direccion,self.__codigo,self.__estado)
    
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
        
        
    