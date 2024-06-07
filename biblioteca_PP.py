
import json
def menu():#genero el menu
    opcion = input("""------ Menu de opciones -----------
                1) Cargar archivo
                2) Imprimir lista
                3) Asignar totales
                4) Filtrar por tipo
                5) Mostrar servicios
                6) Guardar servicios
                7) Salir.
                   Opcion...""")
    return opcion

def cargar_archivo(nombre_archivo:str):
    #cargo el archivo ingresando el nombre por parametro
    try:
        with open(nombre_archivo, 'r') as archivo: #selecciono para que se abra en formato "read"
            servicios_taller = json.load(archivo) #lo cargo
        return servicios_taller
    except FileNotFoundError:
        print("El archivo no existe.")
        return None
    
def imprimir_lista(lista:list):
    print("id_servicio //descripcion // tipo  //precio unitario // cantidad //total servicio")
    for i in lista:
        print(f"{i["id_servicio"]}            {i["descripcion"]}   {i["tipo"]}     {i["precioUnitario"]}             {i["cantidad"]}    {i["totalServicio"]}")

def mostrar_servicios(servicios):
    servicios_ordenados = sorted(servicios, key=lambda x: x['descripcion'])#ordeno los servicios por descripcion
    for servicio in servicios_ordenados:#genero un for para q los vaya imprimiendo
        print(f"{servicio["descripcion"]}")
        
    return servicios_ordenados

def guardar_archivo(nombre_archivo:str,informacion):
    try:
        with open(nombre_archivo,"w+") as archivo:
            archivo.write(informacion)
        print(f"{nombre_archivo} creado con exito")
        return True
    except TypeError:
        return False

def calcular_totales(servicios):
    for servicio in servicios:
        
         servicio['totalServicio'] = (lambda cantidad, precio: cantidad * precio)(
            int(servicio['cantidad']),
            float(servicio['precioUnitario'])
        )
