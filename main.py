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
        
    def casinos():
        lista_casinos=[]
        casinos=leer_csv("CASINO/Data/Casinos.csv")
        for casino in casinos:
            lista_casinos.append(Casino(casino["nombre"],casino["direccion"],int(casino["codigo"])))
        return lista_casinos    
    
    def maquinas():
        lista_maquinas=[]
        maquinas=leer_csv("CASINO/Data/Maquinas.csv")
        casinos=casinos()
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
    
    def contadores():
        lista_contadores=[]
        contadores=leer_csv("CASINO/Data/Contadores.csv")
        maquinas=maquinas()
        casinos=casinos()
        for contador in contadores:
            codigo_casino=int(contador["casino"])
            asset_maquina=int(contador["maquina"])
            año,mes,dia=tuple(map(int,contador["fecha"].split("/")))
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
    
    def cuadre_maquina():
        lista_cuadre_maquina=[]
        cuadre_maquinas=leer_csv("CASINO/Data/CuadrePorMaquina.csv")
        maquinas=maquinas()
        for cuadre in cuadre_maquinas:
            asset_maquina=int(cuadre["maquina"])
            for maquina in maquinas:
                if maquina.asset==asset_maquina:
                    lista_cuadre_maquina.append(
                        CuadreMaquina(
                            float(cuadre["in"]),float(cuadre["out"]),float(cuadre["jackpot"]),
                            float(cuadre["billetero"]),float(cuadre["utilidad"]),maquina
                        )
                    )
        return lista_cuadre_maquina
    
    def cuadre_casino():
        lista_cuadre_casino=[]
        cuadre_casinos=leer_csv("CASINO/Data/CuadrePorCasino.csv")
        casinos=casinos()
        for cuadre in cuadre_casinos:
            codigo_casino=int(cuadre["casino"])
            for casino in casinos:
                if casino.codigo==codigo_casino:
                    lista_cuadre_casino.append(
                        CuadreCasino(
                            float(cuadre["in"]),float(cuadre["out"]),float(cuadre["jackpot"]),
                            float(cuadre["billetero"]),float(cuadre["utilidad"]),casino
                        )
                    )
        return lista_cuadre_casino
    
    def usuarios():
        lista_usuarios=[]
        usuarios=leer_csv("CASINO/Data/Users.csv")
        for usuario in usuarios:
            if usuario["tipo"]=="Administrador":
                lista_usuarios.append(Administrador(usuario["usuario"],usuario["contraseña"],usuario["nombre"],usuario["telefono"]))
            elif usuario["tipo"]=="Operador":
                lista_usuarios.append(Operador(usuario["usuario"],usuario["contraseña"],usuario["nombre"],usuario["telefono"]))
            elif usuario["tipo"]=="Soporte":
                lista_usuarios.append(Soporte(usuario["usuario"],usuario["contraseña"],usuario["nombre"],usuario["telefono"]))
        return lista_usuarios
    
    lista_casinos = casinos()
    lista_maquinas = maquinas()
    lista_contadores = contadores()
    lista_usuarios = usuarios()
    lista_cuadre_maquina = cuadre_maquina()
    lista_cuadre_casino = cuadre_casino()
    return llenar_listas(lista_casinos, lista_maquinas, lista_contadores, lista_usuarios, lista_cuadre_maquina, lista_cuadre_casino)

if __name__=="__main__":
    gestor=cargar_datos()
    app(gestor)
    