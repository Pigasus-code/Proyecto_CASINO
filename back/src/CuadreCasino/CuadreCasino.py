class CuadreCasino:
    
    def __init__(self,in_:float,out:float,jackpot:float,billetero:float,utilidad:float,casino:object,fecha:str):
        self.__in_=in_
        self.__out=out
        self.__jackpot=jackpot
        self.__billetero=billetero
        self.__utilidad=utilidad
        self.__casino=casino
        self.__fecha=fecha
    
    @property
    def in_(self):
        return self.__in_

    @property
    def out(self):
        return self.__out

    @property
    def jackpot(self):
        return self.__jackpot

    @property
    def billetero(self):
        return self.__billetero

    @property
    def utilidad(self):
        return self.__utilidad

    @property
    def casino(self):
        return self.__casino
    
    @property
    def fecha(self):
        return self.__fecha
    
    def __str__(self):
        return "In: {}\nOut :{}\nJackpot: {}\nBilletero: {}\nUtilidad: {}\nMaquina: {}".format(
            self.__in_,self.__out,self.__jackpot,self.__billetero,self.__utilidad,self.__casino)
    
    def to_dict(self):
        return {
            "codigo": self.casino.codigo,  
            "in": self.in_,
            "out": self.out,
            "jackpot": self.jackpot,
            "billetero": self.billetero,
            "utilidad": self.utilidad,
            "fecha":self.fecha
        }