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
