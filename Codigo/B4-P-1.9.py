#Programa 9
# Fecha de elaboracion: 08/11/2024
#Elaborado por: Noemi Lazarin Rosas 

"""Pograma que demuestra el uso de los comandos \"break\" y \"continue\" """

#Ejemplo 1 - break 
#Imprimir los numeros del 1 al 10 
#Pero si el numero es 5, salir del ciclo while
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1 #Equivalente a i = i + 1
print("Fin del programa")

#Ejemplo 2 - contine 
#Imprimir los numeros del 1 al 10, pero si el numero es 5, omitirlo 
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue 
    print(i)
    1 += 1
print("Fin del rpograma")
