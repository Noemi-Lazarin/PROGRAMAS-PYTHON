# Tipos de datos 

``` 
# Datos alfanuméricos
nombre = "Noemi"
apellido = "Lazarin"
nombre_completo = f"{nombre} {apellido}"

# Datos enteros
edad = 18

# Datos flotantes
altura = 1.63  # Altura en metros

# Datos binarios
numero_binario = 0b1010  # Esto es 10 en decimal

# Listas
notas = [8.5, 9.0, 7.5, 10.0]  # Notas de un estudiante

# Función para calcular el promedio de las notas
def calcular_promedio(notas):
    return sum(notas) / len(notas)

if __name__ == "__main__":
    # Imprimir los datos
    print("Nombre completo:", nombre_completo)
    print("Edad:", edad)
    print("Altura:", altura, "metros")
    print("Número binario (en decimal):", numero_binario)
    
    # Calcular y mostrar el promedio de las notas
    promedio_notas = calcular_promedio(notas)
    print("Promedio de notas:", promedio_notas)
  ``` 
