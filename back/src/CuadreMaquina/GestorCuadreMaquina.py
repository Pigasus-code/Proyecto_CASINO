from back.src.CuadreMaquina.CuadreMaquina import CuadreMaquina
from util import GestorArchivos

class GestorCuadreMaquina:
    
    def __init__(self):
        self.__cuadre_maquina=[]
    

    def calculo_total_contadores(self,fecha_inicio,fecha_fin,asset_maquina,lista_contadores)->tuple:
        contadores=list(filter(lambda contador: contador.maquina.asset==asset_maquina and (contador.fecha==fecha_inicio or contador.fecha==fecha_fin),lista_contadores))
        if len(contadores)!=2:
            return None
        contadores.sort(key=lambda contador: contador.fecha)
        inicial,final=contadores
        denominacion=inicial.maquina.denominacion
        lista1=[inicial.in_,inicial.out,inicial.jackpot,inicial.billetero]
        lista2=[final.in_,final.out,final.jackpot,final.billetero]
        ans=[(j-i)*denominacion for i,j in zip(lista1,lista2)]
        return tuple(map(lambda x: round(x,1),ans))
        
    
    def calculo_utilidad_maquina(self,fecha_inicio,fecha_fin,asset_maquina,lista_contadores)->float:
        contadores=list(filter(lambda contador: contador.maquina.asset==asset_maquina and (contador.fecha==fecha_inicio or contador.fecha==fecha_fin),lista_contadores))
        if len(contadores)!=2:
            return None
        contadores.sort(key=lambda contador: contador.fecha)
        inicial,final=contadores
        utilidad = (final.in_-inicial.in_) - ((final.out -inicial.out)+ ( final.jackpot-inicial.jackpot))
        return round(utilidad,1)

    def guardar_resultados(self,contadores:tuple,utilidad:float,maquina:object)->bool:
        if not contadores or not utilidad:
            return False
        try:
            in_,out,jackpot,billetero=contadores
            GestorArchivos.escribir_csv("CASINO/Data/CuadrePorMaquina.csv",[{"in":in_,"out":out,"jackpot":jackpot,"billetero":billetero,"utilidad":utilidad,"maquina":maquina.asset}])
            self.__cuadre_maquina.append(CuadreMaquina(in_,out,jackpot,billetero,utilidad,maquina))
            return True
        except:
            return False
    
    def lista_cuadre_quina(self)->list:
        return self.__cuadre_maquina
    