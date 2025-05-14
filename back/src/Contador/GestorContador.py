from back.src.Contador.Contador import Contador

class GestorContador:
    
    def __init__(self):
        self.__contadores=[]
    
    def agregar_registro_contador(self,fecha,maquina,casino,in_,out,jackpot,billetera):
        """
        se debe agregar a la lista de contadores un objeto de tipo contador con los atributos
        recibidos. Ademas se debe escribir todos los datos en el archivo contadores.csv 
        para que quede un registro en la base de datos. Tener en cuenta que los atributos
        maquina y casino son objetos de sus respectivas clases, por lo que al escribirlo se debe
        acceder a los atributos y separarlos por slash ejemplo: 
        casino.nombre/casino.direccion/casino.codigo ademas en maquina en el atributo casino
        se debe mostrar solo el asset. Debe retornar un true si fue exitosa la operacion
        de lo contrario un false
        """
        pass
    
    def modificar_contador(self,casino,fecha,atributo,nuevo_dato):
        """
        Se debe buscar en la lista de contadores el objeto con el casino recivido
        y modificarle un atributo, este cambio tambien debe quedar reflejado en la base de datos
        volviendo a escribir con la informacion actualizada
        """
        pass
    
    def mostrar_contadores_por_rango(self,fecha_inicio,fecha_fin,lista_contadores)->tuple:
        """
        se debe buscar en la lista de contadores los objetos con las fecha recividas
        y devolver una tupla con estos dos.
        """
        pass
    
    #metodo para el gestor de reportes
    def lista_contadores(self)->list:
        return self.__contadores
