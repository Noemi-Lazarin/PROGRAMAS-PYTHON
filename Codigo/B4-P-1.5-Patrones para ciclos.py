# Programa 5: Patrones para ciclos (Loops Patterns)
# Fecha de elaboracion: 05/11/2024
#Elaborado por: Noemi Lazarin Rosas 

#The count pattern 
letras = ["a","b","c","d","e"]
contador = 0 #Inicializa variable 
for letra in letras: 
    contador = contador + 1 
print("La lista\"letras\"tiene",contador,"letras") 

#
print("The sum pattern") 
numeros = [100,200,300,400]
sumatoria = 0 #Inicializacion 
for numero in numeros: 
    sumatoria = sumatoria + numero  
print("La sumatoria es", sumatoria)
("\n")
#
print("The acomulation pattern") 
palabras= ["Hoy", " ","hace", " ","frio"]
mensaje = " "
for palabra in palabras:
    mensaje=mensaje + palabra 
    print (mensaje) 
       
print("The map pattern")
lista_anterior = ["Manzana", "Piña","Uva"]
lista_nueva = []
print("La lista vacia, lista_nueva")
for fruta in lista_anterior:
    lista_nueva.append(fruta)
print("La lista copiada es",lista_nueva)
