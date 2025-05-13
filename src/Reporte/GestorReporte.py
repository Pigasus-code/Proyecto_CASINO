from PIL import Image
import pandas as pd
from PyPDF2 import PdfReader
import os


class GestorReporte:
    
    def generar_reporte_personalisado(self,filtros_maquina:list,filtros_casino:list,contadores:list,fecha_inicio,fecha_fin,formato):
        """
        generar el reporte en el formato especificado filtrando la informacion, haciendo uso de
        la libreria pandas, se pueden tener varios filtros por maquina y casino y un rango de fechas
        """
        pass

    def generar_reporte_individual_maquina(self,asset_maquina,contadores:list,formato):
        """
        generar el reporte en el formato especificado de una maquina en especifico
        y los contadores que estan asociados a esta
        """
        pass
    
    def generar_reporte_individual_casino(self,codigo_casino,maquinas:list,contadores:list,formato):
        """
        generar el reporte en el formato especificado de una casino en en especifico, 
        se debe tener todas las maquinas asociadas a este casino y los contadores de estas
        """
        pass
    
    def generar_reporte_consolidado(self,contadores:list,fecha_inicio,fecha_fin,formato):
        """
        generar un reporte en el formato especificado de los contadores en un rango de fecha
        """
        pass
    
    def generar_reporte_especial(self,codigo_casino,maquinas:list,porcentaje,formato):
        """
        generar un reporte en el formato especificado de un casino y una seleccion
        de maquinas del mismo, tambien debe mostrar cual es la participacion
        de este grupo de maquinas en la utilidad total del casino haciendo uso de un 
        porcentaje (mirar especificacion del archivo del proyecto)
        """
        pass