import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__))))))


class GestorConfiguracion:
    
    def modificar_token(self,token:str) -> bool:
        try:
            with open(os.path.join(BASE_DIR,"Data","token_acceso.txt"),"w") as archivo:
                archivo.write(token)
            return True
        except:
            return False
    
    def modificar_datos_empresa(self,nombre: str,telefono: str,nit: str,direccion: str) -> bool:
        try:
            with open(os.path.join(BASE_DIR,"Data","datos_empresa.txt"),"w") as archivo:
                archivo.write(f"{nombre}\n{telefono}\n{nit}\n{direccion}")
            return True
        except:
            return False