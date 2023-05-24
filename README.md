# Reto 11

En este reto use mayormente ciclos for y condicionales ya que son mas practicos a la hora de hacer operaciones con matrices ya que estas tienen ciertas restricciones como lo son la multiplicacion entre matrices.

## Punto 1

Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
# Punto 1
# Pedir la dimension de las matrices al usuario
fila = int(input("Ingrese el numero de filas para las matrices: "))
columna = int(input("Ingrese el numero de columnas para las matrices: "))
# Crear la primera matriz
print("Ingrese los valores de la primera matriz:")
matriz1 = []
for i in range(fila):
    fila_matriz1 = []
    for j in range(columna):
        fila_matriz1.append(int(input()))
    matriz1.append(fila_matriz1)
# Crear la segunda matriz
print("Ingrese los valores de la segunda matriz:")
matriz2 = []
for i in range(fila):
    fila_matriz2 = []
    for j in range(columna):
        fila_matriz2.append(int(input()))
    matriz2.append(fila_matriz2)
# Sumar o restar las matrices
operacion = input("¿Desea sumar o restar las matrices? ")
if operacion == "sumar":
    resultado = []
    for i in range(fila):
        fila_resultado = []
        for j in range(columna):
            fila_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila_resultado)
    print("El resultado de la suma de las matrices es:")
    for i in range(fila):
        print(resultado[i])
elif operacion == "restar":
    resultado = []
    for i in range(fila):
        fila_resultado = []
        for j in range(columna):
            fila_resultado.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila_resultado)
    print("El resultado de la resta de las matrices es:")
    for i in range(fila):
        print(resultado[i])
else:
    print("Operacion no valida. Por favor, ingrese 'sumar' o 'restar'.")
```

## Punto 2

Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
# Punto 2
# Pedimos al usuario el numero de filas y columnas de ambas matrices
fila_matriz1 = int(input("Ingrese el numero de filas de la matriz 1: "))
columna_matriz1 = int(input("Ingrese el numero de columnas de la matriz 1: "))
fila_matriz2 = int(input("Ingrese el numero de filas de la matriz 2: "))
columna_matriz2 = int(input("Ingrese el numero de columnas de la matriz 2: "))
# Verificamos si las matrices se pueden multiplicar
if columna_matriz1 != fila_matriz2:
    print("Error: las matrices no se pueden multiplicar")
else:
    # Pedimos al usuario los valores de las matrices
    print("Ingrese los valores de la matriz 1:")
    matriz1 = [[int(input()) for j in range(columna_matriz1)] for i in range(fila_matriz1)]
    print("Ingrese los valores de la matriz 2:")
    matriz2 = [[int(input()) for j in range(columna_matriz2)] for i in range(fila_matriz2)]
    
    # Creamos una matriz resultado con las dimensiones adecuadas
    matriz_resultado = [[0 for j in range(columna_matriz2)] for i in range(fila_matriz1)]
    
    # Realizamos el producto de las matrices y almacenamos el resultado en la matriz resultado
    for i in range(fila_matriz1):
        for j in range(columna_matriz2):
            for k in range(columna_matriz1):
                matriz_resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    # Mostramos el resultado al usuario
    print("El producto de las matrices es:")
    for i in range(fila_matriz1):
        for j in range(columna_matriz2):
            print(matriz_resultado[i][j], end=" ")
        print()
```
## Punto 3

Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```Pynthon
# Punto 3
# Pedir al usuario que ingrese el numero de filas y columnas de la matriz
filas = int(input("Ingrese el numero de filas de la matriz: "))
columnas = int(input("Ingrese el numero de columnas de la matriz: "))
# Inicializar la matriz con ceros
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(0)
    matriz.append(fila)
# Pedir al usuario que ingrese los valores de la matriz
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = int(input("Ingrese el valor de la celda [" + str(i) + "][" + str(j) + "]: "))
# Imprimir la matriz original
print("\nMatriz original:")
for fila in matriz:
    print(fila)
# Calcular la matriz transpuesta
transpuesta = []
for j in range(columnas):
    fila = []
    for i in range(filas):
        fila.append(matriz[i][j])
    transpuesta.append(fila)
# Imprimir la matriz transpuesta
print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)
```

## Punto 4

Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
# Punto 4
# Pedir al usuario que ingrese el numero de filas y columnas de la matriz
filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))
# Crear una matriz vacia con los valores ingresados
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input("Ingrese el valor para la fila {} y columna {}: ".format(i+1, j+1)))
        fila.append(valor)
    matriz.append(fila)
# Pedir al usuario que ingrese el numero de la columna que desea sumar
columna_sumar = int(input("Ingrese el numero de la columna que desea sumar (1 a {}): ".format(columnas)))
# Verificar que la columna ingresada este dentro del rango de columnas de la matriz
if columna_sumar < 1 or columna_sumar > columnas:
    print("El numero de columna ingresado no es valido")
else:
    # Sumar los elementos de la columna seleccionada
    suma = 0
    for fila in matriz:
        suma += fila[columna_sumar-1]
    # Mostrar la suma de los elementos de la columna seleccionada
    print("La suma de los elementos de la columna {} es {}".format(columna_sumar, suma))
```

## Punto 5

Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python
# Punto 5
# Pedir al usuario el numero de filas y columnas de la matriz
num_filas = int(input("Ingrese el numero de filas: "))
num_columnas = int(input("Ingrese el numero de columnas: "))
# Crear la matriz vacia
matriz = []
# Pedir al usuario los valores de la matriz
for i in range(num_filas):
    fila = []
    for j in range(num_columnas):
        valor = int(input(f"Ingrese el valor para la fila {i+1}, columna {j+1}: "))
        fila.append(valor)
    matriz.append(fila)
# Imprimir la matriz para verificar que se ingresaron correctamente los valores
print("Matriz ingresada:")
for fila in matriz:
    print(fila)
# Pedir al usuario el numero de fila a sumar
num_fila_sumar = int(input("Ingrese el numero de fila que desea sumar: "))
# Verificar que el numero de fila ingresado sea valido
if num_fila_sumar > num_filas or num_fila_sumar < 1:
    print("Numero de fila invalido.")
else:
    # Sumar los elementos de la fila seleccionada
    suma = sum(matriz[num_fila_sumar-1])
    # Imprimir la suma de la fila seleccionada
    print(f"La suma de los elementos de la fila {num_fila_sumar} es: {suma}")
```
