from src.Maquina.Maquina import Maquina

class GestorMaquina:
    
    def __init__(self):
        self.__maquinas=[]
    
    def buscar_maquina(self,asset)->object:
        """
        se debe buscar en la lista de maquinas el objeto con el asset recivido,
        retornar el objeto. Este metodo se usara para reutilizacion de codigo
        en funciones donde se deba bucar un objeto tipo maquina y modificarlo 
        """
        pass
    
    def agregar_maquina(self,marca,modelo,serial,asset,casino,denominacion)->bool:
        """
        se debe agrgar a la lista de maquinas un objeto tipo maquina con los atributos
        recividos, ademas debe escribir los datos en el archivo casino.csv para que este 
        en la base de datos para futuras consultas y reportes. se retorna true si se pudo
        agregar exitosamente y false sino
        """
        pass
    
    def modificar_maquina(self,asset,atributo,nuevo_dato)->bool:
        """
        se debe buscar el objeto tipo maquina con el asset recivido y modificar
        su atributo con la nueva informacion. Ademas en la base de datos tambien
        debe quedar el cambio registrado. se retorna true si la modificacion fue exitosa
        de lo contrario false
        """
        pass
    
    def activar_maquina(self,asset)->bool:
        """
        se debe buscar el objeto tipo maquina con el asset recivido y modificar
        su estado haciendo uso del metodo de la calse maquina. se retorna true si la activacion
        fue exitosa de lo contrario false
        """
        pass
    
    def desactivar_maquina(self,asset)->bool:
        """
        se debe buscar el objeto tipo maquina con el asset recivido y modificar
        su estado haciendo uso del metodo de la calse maquina. se retorna true si la inactivacion
        fue exitosa de lo contrario false
        """
        pass

    #metodo para el gestor contador
    def lista_maquinas(self)->list:
        return self.__maquinas