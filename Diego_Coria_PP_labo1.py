from biblioteca_diego_coria import *
from biblioteca_PP import *


"""El programa contará con el siguiente menú: 
1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos del mismo. 
2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los servicios. 
3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el total calculado (totalServicio) de la siguiente forma: cantidad x  precioUnitario. 
4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan servicios del tipo seleccionado. 
5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por descripción de manera ascendente. 
6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json. 
7) Salir."""

while True:
    opcion = menu()
    if opcion == "1":
        nombre_archivo = input("por favor ingrese el nombre del archivo: ")#se debe ingresar el nombre con la extension: data.json
        servicios = cargar_archivo(nombre_archivo)
    if opcion =="2":
        imprimir_lista(servicios)
    if opcion =="3":
        calcular_totales(servicios)
        print(servicios)
    if opcion =="5":
      lista_ordenada = mostrar_servicios(servicios)
    if opcion =="6":
        nombre = input("ingrese nombre del archivo ")
        guardar_archivo(nombre+".json",lista_ordenada)
    if opcion=="7":
        break