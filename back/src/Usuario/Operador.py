from back.src.Usuario.Usuario import Usuario

class Operador(Usuario):
    
    def __init__(self,usuario,contraseña,nombre,telefono):
        super().__init__(usuario,contraseña,nombre,telefono,tipo="Operador")
    
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.usuario,self.contraseña,self.nombre,self.telefono,self.tipo,self.estado)
    