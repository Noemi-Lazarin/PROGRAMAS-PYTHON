"""Programa que se repite hasta que ingrese la palabra ´salir´"""

#Inicializacion de variables 
palabra = ""
while palabra != "salir":
    palabra = input("Ingresa una palabra o 'salir' para terminar: ")
    palabra = palabra.lower() # Convierte la palabra a minusculas 
    print("Usted ingreso:",palabra)
print("Fin del programa")
