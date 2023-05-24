# Punto 3
# Pedir al usuario que ingrese el número de filas y columnas de la matriz
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))
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