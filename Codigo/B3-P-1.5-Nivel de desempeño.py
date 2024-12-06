# programa 5: calcule el nivel de sus desmepeño descrito con su calificacion dada por el usuario, dada con la siguiente tabla 
#Fecha de elaboracion: 30/10/2024
#Elaborado por: Noemi Lazarin Rosas 

```
calificaciones = int(input("Ingresa tu calificacion para evaluar tu desempeño:"))

if calificaciones <= 60:
    print("Insuficiente")

elif calificaciones >= 70 and calificaciones <= 89: 
    print("Muy bien!")
    
elif calificaciones >= 90 and calificaciones <= 95:
    print("Notable!")
    
else:
    print("Exelente")
    
print("¡Gracias por usar mi sistema de evaluacion!")
```
