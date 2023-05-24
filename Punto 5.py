# Punto 5
# Pedir al usuario el número de filas y columnas de la matriz
num_filas = int(input("Ingrese el número de filas: "))
num_columnas = int(input("Ingrese el número de columnas: "))
# Crear la matriz vacía
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
# Pedir al usuario el número de fila a sumar
num_fila_sumar = int(input("Ingrese el número de fila que desea sumar: "))
# Verificar que el número de fila ingresado sea válido
if num_fila_sumar > num_filas or num_fila_sumar < 1:
    print("Número de fila inválido.")
else:
    # Sumar los elementos de la fila seleccionada
    suma = sum(matriz[num_fila_sumar-1])
    # Imprimir la suma de la fila seleccionada
    print(f"La suma de los elementos de la fila {num_fila_sumar} es: {suma}")