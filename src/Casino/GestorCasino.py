from src.Casino.Casino import Casino

class GestorCasino:
    
    def __init__(self):
        self.__casinos=[]
        
    def buscar_casino(self,codigo)->object:
        """
        se debe buscar en la lista de casinos el objeto con el codigo recivido,
        retornar el objeto. Este metodo se usara para reutilizacion de codigo
        en funciones donde se deba bucar un objeto tipo casino y modificarlo 
        """
        pass
    
    def agrgar_casino(self,nombre,direccion,codigo)->bool:
        """
        se debe agrgar a la lista de casinos un objeto tipo casino con los atributos
        recividos, ademas debe escribir los datos en el archivo casino.csv para que este 
        en la base de datos para futuras consultas y reportes. se retorna true si se pudo
        agregar exitosamente y false sino
        """
        pass
    
    def modificar_casino(self,codigo,atributo,nuevo_dato)->bool:
        """
        se debe buscar el objeto tipo casino con el codigo recivido y modificar
        su atributo con la nueva informacion. Ademas en la base de datos tambien
        debe quedar el cambio registrado. se retorna true si la modificacion fue exitosa
        de lo contrario false
        """
        pass
    
    def activar_casino(self,codigo)->bool:
        """
        se debe buscar el objeto tipo casino con el codigo recivido y modificar
        su estado haciendo uso del metodo de la calse casino. se retorna true si la activacion
        fue exitosa de lo contrario false
        """
        pass

    def desactivar_casino(self,codigo)->bool:
        """
        se debe buscar el objeto tipo casino con el codigo recivido y modificar
        su estado haciendo uso del metodo de la calse casino. se retorna true si la inactivacion
        fue exitosa de lo contrario false
        """
        pass
    
    def filtro_por_activos(self)->list:
        """
        se debe retornar una lista con los objetos tipo casino que esten activos
        """
        pass
    
    def filtro_por_inactivos(self)->list:
        """
        se debe retornar una lista con los objetos tipo casino que esten inactivos
        """
        pass
    
    #metodo para el gestor contador
    def lista_casinos(self)->list:
        return self.__casinos