class CuadreMaquina:
    
    def __init__(self,in_:float,out:float,jackpot:float,billetero:float,utilidad:float,maquina:object):
        self.__in_=in_
        self.__out=out
        self.__jackpot=jackpot
        self.__billetero=billetero
        self.__utilidad=utilidad
        self.__maquina=maquina
    
    @property
    def in_(self):
        return self.__in_

    @in_.setter
    def in_(self, in_):
        self.__in_ = in_

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
    def billetero(self, biletero):
        self.__billetero = biletero

    @property
    def utilidad(self):
        return self.__utilidad

    @utilidad.setter
    def utilidad(self, utilidad):
        self.__utilidad = utilidad

    @property
    def maquina(self):
        return self.__maquina

    @maquina.setter
    def maquina(self, maquina):
        self.__maquina = maquina
    
    def __str__(self):
        return "In: {}\nOut :{}\nJackpot: {}\nBilletero: {}\nUtilidad: {}\nMaquina: {}".format(
            self.__in_,self.__out,self.__jackpot,self.__billetero,self.__utilidad,self.__maquina)
    