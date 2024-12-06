#Programa 7: Programa que clasifica las edades de una lista de grupos 
#Fecha de elaboracion: 07/11/2024 
# Elaborado por: Noemi Lazarin Rosas 

"""P-7 Programa que clasifica las edades de una lista en los siguientes grupos menores de 18 """

edades = [10,15,18,8,36,25,67,89,95,43,26,10,65,55,81,90,]
menores_18 = [] #Lista para menores de 18 
adultos = [] # Lista vacia para adultos entre 18 y 65 
mayores_65 = [] #Lista vacia para mayores de 65 

#...Clasificar edades en las listas correspondientes...
for edad in edades: 
    if edad < 18: 
        menores_18.append(edad)
    elif edad >= 18 and edad < 65: 
        adultos.append(edad)
    else: 
        mayores_65.append(edad)
        
#...Imprimir resultados...
print("\n \\La lista de edades es:",edades)
print("\n \\La lista de menores es:",menores_18)
print("\n \\La lista de adultos:", adultos)
print("\n \\La lista de adultos mayores es:",mayores_65)
