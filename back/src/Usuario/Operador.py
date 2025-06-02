from back.src.Usuario.Usuario import Usuario

class Operador(Usuario):
    
    def __init__(self,usuario:str,contraseña:str,nombre:str,telefono:str,estado:str):
        super().__init__(usuario,contraseña,nombre,telefono,estado=estado,tipo="Operador")
    
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.usuario,self.contraseña,self.nombre,self.telefono,self.tipo,self.estado)
    