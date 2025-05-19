import csv

def leer_csv(nombre_archivo):
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        return list(csv.DictReader(archivo))

def escribir_csv(nombre_archivo, datos:list):
    with open(nombre_archivo, mode='a', newline='', encoding='utf-8') as archivo:
        campos=datos[0].keys()
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writerows(datos)
    
def modificar(nombre_archivo,id_name,id,atributo,nueva_data):
    
    def sobreescribir_csv(nombre_archivo, datos):      
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            campos=datos[0].keys()
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(datos)
            
    datos=leer_csv(nombre_archivo)
    for objeto in datos:
        if objeto[id_name]==id:
            objeto[atributo]=nueva_data
            break
    sobreescribir_csv(nombre_archivo,datos)