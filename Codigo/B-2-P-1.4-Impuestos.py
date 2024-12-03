#Programa 4: Programa que calcula impuestos de un valor e imprime de la sig. manera 
#Fecha de elaboracion: 22/10/2024
#Elaborado por: Noemi Lazarin Rosas 

```
# Solicitamos que el usuario ingrese el valor y el porcentaje del impuesto
valor = float(input("Ingrese el valor sobre sobre el cual quieres calcular los impuestos: "))
porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto: "))

# Calculamos el impuesto
impuesto = (porcentaje_impuesto / 100) * valor

# Calculamos el total a pagar
total_a_pagar = valor + impuesto

# Resultados
print(f"El impuesto a pagar es: {impuesto:.2f}")
print(f"El total a pagar, incluyendo impuestos, es: {total_a_pagar:.2f}")
print("Gracias por usar nuestro sistema")
```
