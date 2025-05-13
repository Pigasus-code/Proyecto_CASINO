from src.Usuario.Administrador import Administrador
from src.Usuario.Operador import Operador
from src.Usuario.Soporte import Soporte

class GestorUsuario:
    
    def __init__(self):
        self.__usuarios=[]
        
    def crear_usuario(self,usuario,contraseña,tipo)->bool:
        """
        se debe agregar a la lista de usurios un usuario del tipo que se recibe
        crrando el objeto con los atributos recividos, ademas se debe escribir en el 
        archivo usuarios.csv la informacion para que quede un registro en la base de datos.
        Se debe validar que no existan usuarios con el mismo nombre de usuario, debe retoran true
        si le creacion fue exitosa de lo contrario false
        """
        pass
    
    def modificar_usuario(self,usuario,atributo,nuevo_dato):
        """
        se debe buscar en la lista de usuarios y modificar el atributo, esto debe quedar
        registrado en el archivo usuarios.csv para que quede evidencia en la base de datos y 
        estar actualizada
        """
        pass

    