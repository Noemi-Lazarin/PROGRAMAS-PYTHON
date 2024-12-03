#Programa 8: Programa que calcule el promedio de 5 unidades e indique si aprobo la materia 
#Fecha de elaboracion:24/10/2024
#Elaborado por: Noemi Lazarin rosas 

```
# Realizamos una lista para guardar las calificaciones
unidades = []

# Pedimos al usuario que ingrese las calificaciones de 5 unidades
for i in range(5):
    calificación = float(input("Ingresa la calificación de la unidad " + str(i + 1) + ": "))
    unidades.append(calificación)  # Agregamos la calificación a la lista

# Calculamos el promedio sumando todas las calificaciones y dividiendo por 5
promedio = sum(unidades) / 5

# Verificamos si el promedio es mayor o igual a 7
if promedio >= 70:
    print("Aprobaste la materia con un promedio de:", promedio)
else:
    print("Reprobaste la materia con un promedio de:", promedio)
```
