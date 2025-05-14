class Contador:
    
    def __init__(self,fecha:str,maquina:object,casino:object,in_:float,out:float,jackpot:float,billetero:float):
        self.__fecha=fecha
        self.__maquina=maquina
        self.__casino=casino
        self.__in=in_
        self.__out=out
        self.__jackpot=jackpot
        self.__billetero=billetero
    
    
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha
        
    @property
    def maquina(self):
        return self.__maquina
    
    @property
    def casino(self):
        return self.__casino

    @property
    def in_(self):
        return self.__in

    @in_.setter
    def in_(self, in_):
        self.__in = in_

    @property
    def out(self):
        return self.__out

    @out.setter
    def out(self, out):
        self.__out = out

    @property
    def jackpot(self):
        return self.__jackpot

    @jackpot.setter
    def jackpot(self, jackpot):
        self.__jackpot = jackpot

    @property
    def billetero(self):
        return self.__billetero

    @billetero.setter
    def billetero(self, billetero):
        self.__billetero = billetero
    
    def __str__(self):
        return "Fecha: {}\nMauina: {}\nCasino : {}\nIn: {}\nOut :{}\nJackpot: {}\nBilletero: {}".format(
            self.__fecha,self.__maquina,self.__casino,self.__in,self.__out,self.__jackpot,self.__billetero)
    