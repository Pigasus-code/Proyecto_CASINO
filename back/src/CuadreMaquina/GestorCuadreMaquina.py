from back.src.CuadreMaquina.CuadreMaquina import CuadreMaquina
from util import GestorArchivos
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PATH_FILE=os.path.join(BASE_DIR,"Data","CuadrePorMaquina.csv")

class GestorCuadreMaquina:
    
    def __init__(self):
        self.__cuadre_maquina=[]
    
    def set_cuadre_maquinas(self,lista_cuadre_maquinas):
        self.__cuadre_maquina=lista_cuadre_maquinas
            
    def calculo_total_contadores(self,fecha_inicio,fecha_fin,asset_maquina,lista_contadores,para_utilidad=False)->tuple:
        contadores_mquina=list(filter(lambda contador:contador.maquina.asset==asset_maquina,lista_contadores))
        if not contadores_mquina:
            return None
        contadores_mquina.sort(key=lambda contador:contador.fecha)
        indices_contadores=[]
        for index,contador in enumerate(contadores_mquina):
            if contador.fecha==fecha_inicio or contador.fecha == fecha_fin:
                indices_contadores.append(index)
        if len(indices_contadores) != 2:
            return None
        denominacion=contadores_mquina[0].maquina.denominacion
        if contadores_mquina[indices_contadores[0]].in_==0: #reinicio en la fecha inicial
            indices_contadores[0]+=1
        elif contadores_mquina[indices_contadores[1]].in_==0: #reinicio en la fecha final
            indices_contadores[1]-=1
        
        index_reinicio=None
        reinicio=False
        for i in range(indices_contadores[0],indices_contadores[1]+1):
            if contadores_mquina[i].in_==0:
                index_reinicio=i
                reinicio=True
                break
        if reinicio: #hay un reinicio entre las fechas
            inicial=contadores_mquina[indices_contadores[0]]
            final=contadores_mquina[indices_contadores[1]]
            reinicio_antes=contadores_mquina[index_reinicio-1]
            lista1=[inicial.in_,inicial.out,inicial.jackpot,inicial.billetero]
            lista2=[final.in_,final.out,final.jackpot,final.billetero]
            lista3=[reinicio_antes.in_,reinicio_antes.out,reinicio_antes.jackpot,reinicio_antes.billetero]
            lista4=[j-i for i,j in zip(lista1,lista3)]
            ans=[(j-i)*denominacion for i,j in zip(lista4,lista2)]
            if para_utilidad:
                return (lista4,lista2)
            else:
                return tuple(map(lambda x: abs(round(x,1)),ans))
        
        inicial,final=contadores_mquina[indices_contadores[0]],contadores_mquina[indices_contadores[1]]
        lista1=[inicial.in_,inicial.out,inicial.jackpot,inicial.billetero]
        lista2=[final.in_,final.out,final.jackpot,final.billetero]
        ans=[(j-i)*denominacion for i,j in zip(lista1,lista2)]
        if para_utilidad:
                return (lista2,lista1)
        else:
            return tuple(map(lambda x: abs(round(x,1)),ans))
                
    def calculo_utilidad_maquina(self,fecha_inicio,fecha_fin,asset_maquina,lista_contadores)->float:
        contadores=self.calculo_total_contadores(fecha_inicio,fecha_fin,asset_maquina,lista_contadores,para_utilidad=True)
        if not contadores:
            return None
        inicial,final=contadores
        if not inicial or not final:
            return None
        utilidad = (final[0]-inicial[0]) - ((final[1] -inicial[1])+ ( final[2]-inicial[2]))
        return round(utilidad,1)

    def guardar_resultados(self,contadores:tuple,utilidad:float,maquina:object,fecha:str)->bool:
        if not contadores or not utilidad:
            return False
        try:
            in_,out,jackpot,billetero=contadores
            GestorArchivos.escribir_csv(PATH_FILE,[{"in":in_,"out":out,"jackpot":jackpot,"billetero":billetero,"utilidad":utilidad,"maquina":maquina.asset,"fecha":fecha}])
            self.__cuadre_maquina.append(CuadreMaquina(in_,out,jackpot,billetero,utilidad,maquina,fecha))
            return True
        except:
            return False
    
    def lista_cuadre_quina(self)->list:
        return self.__cuadre_maquina
    