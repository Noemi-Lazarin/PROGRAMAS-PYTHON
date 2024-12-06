# Progrma 6: Progrma que permita crear una lista de todos los numeros menores a 50 
# Fecha de elaboracion: 06/11/2024
#Elaborado por: Noemi Lazarin Rosas 

numeros = [10,50,25,13,10,28,100,500,29,29]
menores_50 = []
for numero in numeros:
    if numero < 50:
        menores_50.append(numero) 
print ("La lista original es:",numeros)
print ("La nueva lista es:",menores_50)
