# Punto 4
# Pedir al usuario que ingrese el número de filas y columnas de la matriz
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
# Crear una matriz vacía con los valores ingresados
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input("Ingrese el valor para la fila {} y columna {}: ".format(i+1, j+1)))
        fila.append(valor)
    matriz.append(fila)
# Pedir al usuario que ingrese el número de la columna que desea sumar
columna_sumar = int(input("Ingrese el número de la columna que desea sumar (1 a {}): ".format(columnas)))
# Verificar que la columna ingresada esté dentro del rango de columnas de la matriz
if columna_sumar < 1 or columna_sumar > columnas:
    print("El número de columna ingresado no es válido")
else:
    # Sumar los elementos de la columna seleccionada
    suma = 0
    for fila in matriz:
        suma += fila[columna_sumar-1]
    # Mostrar la suma de los elementos de la columna seleccionada
    print("La suma de los elementos de la columna {} es {}".format(columna_sumar, suma))