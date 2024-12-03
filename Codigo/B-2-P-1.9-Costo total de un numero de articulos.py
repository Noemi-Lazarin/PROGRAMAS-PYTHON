#Programa 9:  Programa que calcule el costo total de un número de artículos si: Son 3 artículos o menos precio unitario: $45.00. Más de 3 artículos precio unitario: $30. al final mostrar un mensaje 
#Fecha de elaboracion: 25/10/24
#Elaborado por: Noemi Lazarin Rosas 

```
cantidad=int(input("¿Cauntos articulos compro?"))
if cantidad>3:
    total=cantidad*30 
else:
    total=cantidad*45
print("El total a pagar es $" + str(total))
print("Que tenga bonito dia")
```
