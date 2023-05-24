# Punto 2
# Pedimos al usuario el número de filas y columnas de ambas matrices
fila_matriz1 = int(input("Ingrese el número de filas de la matriz 1: "))
columna_matriz1 = int(input("Ingrese el número de columnas de la matriz 1: "))
fila_matriz2 = int(input("Ingrese el número de filas de la matriz 2: "))
columna_matriz2 = int(input("Ingrese el número de columnas de la matriz 2: "))
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