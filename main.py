from back.src.GestorPrincipal import GestorPrincipal
from back.src.Casino.Casino import Casino
from back.src.Maquina.Maquina import Maquina
from back.src.Contador.Contador import Contador
from back.src.CuadreCasino.CuadreCasino import CuadreCasino
from back.src.CuadreMaquina.CuadreMaquina import CuadreMaquina
from back.src.Usuario.Administrador import Administrador
from back.src.Usuario.Operador import Operador
from back.src.Usuario.Soporte import Soporte
from front.src.InterfazUsuario.web import app
from util.GestorArchivos import leer_csv
from datetime import date
import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))


def cargar_datos():
    
    def llenar_listas(casinos,maquinas,contadores,usuarios,cuadre_maquina,cuadre_casino):
        gestor=GestorPrincipal()
        gestor.gestor_casino.set_casinos(casinos)
        gestor.gestor_maquina.set_maquinas(maquinas)
        gestor.gestor_contador.set_contadores(contadores)
        gestor.gestor_usuario.set_usuarios(usuarios)
        gestor.gestor_cuadre_maquina.set_cuadre_maquinas(cuadre_maquina)
        gestor.gestor_cuadre_casino.set_cuadre_casinos(cuadre_casino)
        return gestor
        
    def _casinos():
        lista_casinos=[]
        casinos=leer_csv(os.path.join(BASE_DIR,"Data","Casinos.csv"))
        for casino in casinos:
            lista_casinos.append(Casino(casino["nombre"],casino["direccion"],int(casino["codigo"])))
        return lista_casinos    
    
    def _maquinas():
        lista_maquinas=[]
        maquinas=leer_csv(os.path.join(BASE_DIR,"Data","Maquinas.csv"))
        casinos=_casinos()
        for maquina in maquinas:
            codigo_casino=int(maquina["casino"])
            for casino in casinos:
                if casino.codigo==codigo_casino:
                    lista_maquinas.append(
                        Maquina(
                            maquina["marca"],maquina["modelo"],maquina["serial"],
                            int(maquina["asset"]),casino,float(maquina["denominacion"])
                        )
                    )
        return lista_maquinas
    
    def _contadores():
        lista_contadores=[]
        contadores=leer_csv(os.path.join(BASE_DIR,"Data","Contadores.csv"))
        maquinas=_maquinas()
        casinos=_casinos()
        for contador in contadores:
            codigo_casino=int(contador["casino"])
            asset_maquina=int(contador["maquina"])
            año,mes,dia=tuple(map(int,contador["fecha"].split("-")))
            fecha=date(año,mes,dia)
            for casino in casinos:
                if casino.codigo==codigo_casino:
                    for maquina in maquinas:
                        if maquina.asset==asset_maquina:
                            lista_contadores.append(
                                Contador(
                                    int(contador["codigo"]),fecha,maquina,casino,
                                    float(contador["in"]),float(contador["out"]),
                                    float(contador["jackpot"]),float(contador["billetero"])
                                )
                            )
        return lista_contadores
    
    def _cuadre_maquina():
        lista_cuadre_maquina=[]
        cuadre_maquinas=leer_csv(os.path.join(BASE_DIR,"Data","CuadrePorMaquina.csv"))
        maquinas=_maquinas()
        for cuadre in cuadre_maquinas:
            asset_maquina=int(cuadre["maquina"])
            for maquina in maquinas:
                if maquina.asset==asset_maquina:
                    lista_cuadre_maquina.append(
                        CuadreMaquina(
                            float(cuadre["in"]),float(cuadre["out"]),float(cuadre["jackpot"]),
                            float(cuadre["billetero"]),float(cuadre["utilidad"]),maquina,cuadre["fecha"]
                        )
                    )
        return lista_cuadre_maquina
    
    def _cuadre_casino():
        lista_cuadre_casino=[]
        cuadre_casinos=leer_csv(os.path.join(BASE_DIR,"Data","CuadrePorCasino.csv"))
        casinos=_casinos()
        for cuadre in cuadre_casinos:
            codigo_casino=int(cuadre["casino"])
            for casino in casinos:
                if casino.codigo==codigo_casino:
                    lista_cuadre_casino.append(
                        CuadreCasino(
                            float(cuadre["in"]),float(cuadre["out"]),float(cuadre["jackpot"]),
                            float(cuadre["billetero"]),float(cuadre["utilidad"]),casino,cuadre["fecha"]
                        )
                    )
        return lista_cuadre_casino
    
    def _usuarios():
        lista_usuarios=[]
        usuarios=leer_csv(os.path.join(BASE_DIR,"Data","Users.csv"))
        for usuario in usuarios:
            if usuario["tipo"]=="Administrador":
                lista_usuarios.append(Administrador(usuario["usuario"],usuario["contraseña"],usuario["nombre"],usuario["telefono"],usuario["estado"]))
            elif usuario["tipo"]=="Operador":
                lista_usuarios.append(Operador(usuario["usuario"],usuario["contraseña"],usuario["nombre"],usuario["telefono"],usuario["estado"]))
            elif usuario["tipo"]=="Soporte":
                lista_usuarios.append(Soporte(usuario["usuario"],usuario["contraseña"],usuario["nombre"],usuario["telefono"],usuario["estado"]))
        return lista_usuarios
    
    lista_casinos = _casinos()
    lista_maquinas = _maquinas()
    lista_contadores = _contadores()
    lista_usuarios = _usuarios()
    lista_cuadre_maquina = _cuadre_maquina()
    lista_cuadre_casino = _cuadre_casino()
    return llenar_listas(lista_casinos, lista_maquinas, lista_contadores, lista_usuarios, lista_cuadre_maquina, lista_cuadre_casino)

if __name__=="__main__":
    gestor=cargar_datos()
    app(gestor)       