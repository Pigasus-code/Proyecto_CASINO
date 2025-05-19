
class Maquina:
    
    def __init__(self,marca:str,modelo:str,serial:str,asset:int,casino:object,denominacion:float):
        self.__marca=marca
        self.__modelo=modelo
        self.__serial=serial
        self.__asset=asset
        self.__casino=casino
        self.__denominacion=denominacion
        self.__estado="Activa"
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,marca):
        self.__marca=marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo=modelo
        
    @property
    def serial(self):
        return self.__serial
    
    @serial.setter
    def serial(self,serial):
        self.__serial=serial
        
    @property
    def asset(self):
        return self.__asset
    
    @asset.setter
    def asset(self,asset):
        self.__asset=asset
        
    @property
    def casino(self):
        return self.__casino
    
    @casino.setter
    def casino(self,casino):
        self.__casino=casino
        
    @property
    def denominacion(self):
        return self.__denominacion
    
    @property
    def estado(self):
        return self.__estado
    
    def __str__(self):
        return "Marca: {}\nModelo: {}\nSerial: {}\nAsset: {}\nCasino: {}\nDenominacion: {}\nEstado: {}\n".format(
            self.__marca,self.__modelo,self.__serial,self.__asset,self.__casino,self.__denominacion,self.__estado)
    
    def activar(self)->bool:
        if self.__estado=="Inactiva":
            self.__estado="Activa"
            return True
        else:
            return False
    
    def desactivar(self)->bool:
        if self.__estado=="Activa":
            self.__estado="Inactiva"
            return True
        else:
            return False