from back.src.Casino.GestorCasino import GestorCasino
from back.src.Maquina.GestorMaquina import GestorMaquina
from back.src.GestorPrincipal import GestorPrincipal

gestor=GestorPrincipal()
gestor_casino=GestorCasino()
gestor_maquina=GestorMaquina(gestor_casino)

gestor.agregar_casino("juan","calle 23",1)
gestor.agregar_casino("samuel","calle 13",2)
gestor.agregar_casino("esteban","calle 33",3)

gestor.agregar_maquina("macvc","hdfd","2113",1,3,230.3)
gestor.agregar_maquina("maaa","hdasa","13",2,3,230.3)
gestor.agregar_maquina("masas","haaad","2",3,3,230.3)

gestor.modificar_maquina(3,"casino",1)
gestor.desactivar_maquina(1)
gestor.desactivar_maquina(2)
gestor.desactivar_maquina(3000)

gestor.activar_maquina(2)
