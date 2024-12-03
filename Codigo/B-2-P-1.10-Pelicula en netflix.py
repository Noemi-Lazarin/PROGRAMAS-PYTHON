#Programa 10: Revisar si puedes ver una pelicula en netflix la condicion para esto es que seas mayor de edad y que hayas comprado la pelicula 
#fecha de elaboracion: 25/10/2024
#Elaborado por:Noemi Lazarin Rosas 

```
edad = int(input("¿Cuantos años tienes?"))

if edad>= 18:
    compra = int(input("¿Compraste la pelicula?\n0-NO\n1-SI\n"))
    if compra == 1:
        print("Puede ver la pelicula")
    
else:
    print("Vete a hacer la tarea")
    
print("¡Gracias por usar Netflix")
```
        
