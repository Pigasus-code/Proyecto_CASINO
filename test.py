from datetime import date
from back.src.GestorPrincipal import GestorPrincipal

gestor=GestorPrincipal()

gestor.agregar_casino("juan","calle 23",1)
gestor.agregar_casino("samuel","calle 13",2)
gestor.agregar_casino("esteban","calle 33",3)


gestor.agregar_maquina("macvc","hdfd","2113",1,3,230.3)
gestor.agregar_maquina("maaa","hdasa","13",2,3,230.3)
gestor.agregar_maquina("masas","haaad","2",3,3,230.3)


gestor.agregar_registro_contador(1,date(2025,5,16),1,3,232.3,23.3,233.4,322323.7)
gestor.agregar_registro_contador(2,date(2025,5,17),1,3,300.3,27.3,700.4,322323444.7)
gestor.agregar_registro_contador(3,date(2025,5,18),2,3,500.3,80.3,800.4,322323335555.7)
gestor.agregar_registro_contador(4,date(2025,5,20),2,3,600.3,100.3,1000.4,3223230000999.7)


contadores1=gestor.calculo_total_contadores(date(2025,5,16),date(2025,5,17),1)
utilidad1=gestor.calculo_utilidad_maquina(date(2025,5,16),date(2025,5,17),1)
gestor.guardar_resultados_maquina(contadores1,utilidad1,1)

contadores2=gestor.calculo_total_contadores(date(2025,5,18),date(2025,5,20),2)
utilidad2=gestor.calculo_utilidad_maquina(date(2025,5,18),date(2025,5,20),2)
gestor.guardar_resultados_maquina(contadores2,utilidad2,2)


conts1=gestor.total_contadores_por_casino(date(2025,5,16),date(2025,5,20),3)
util1=gestor.calculo_utilidad_por_casino(date(2025,5,16),date(2025,5,20),3)
gestor.guardar_resultados_casino(conts1,util1,3)

conts2=gestor.total_contadores_por_casino(date(2025,5,16),date(2025,5,17),3)
util2=gestor.calculo_utilidad_por_casino(date(2025,5,16),date(2025,5,17),3)
gestor.guardar_resultados_casino(conts2,util2,3)


gestor.crear_usuario("juanjo2007","1623+","juan jose ramirez","1029283","Administrador")
gestor.crear_usuario("sandra23","propr++","sandra vents","1034343","Operador")
gestor.crear_usuario("andres_mel","jjime3","andres bulg","121283","Soporte")

