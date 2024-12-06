#Programa 12: 
#Fecha de elaboracion:8/11/2024
#Elaborado por: Noemi Lazarin Rosas 

"""Programa que se repite indefinidamente, hasta que se ingrese la palabra 'salir' """

#Inializacion de variables 
palabra = " "
while True: 
    palabra = input("Ingresa una palabra o 'salir' para terminar: ")
    palabra = palabra.lower() #Convierte la palabra a minusculas 
    print("Utsed ingreso:", palabra)
    if palabra == "Salir":
        break 
    
print("Fin del programa \U0001F601 \n \n") #Imprime un emoji feliz 
print("¡Hasta luego! \U0001F44B \n") #Imprime un emoji de saludo 
