from back.src.Usuario.Usuario import Usuario

class Administrador(Usuario):
    
    def __init__(self,usuario,contraseña,nombre,telefono):
        super().__init__(usuario,contraseña,nombre,telefono,tipo="Administrador")
    
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.usuario,self.contraseña,self.nombre,self.telefono,self.tipo,self.estado)
    