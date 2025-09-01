# Programa 1: Búsqueda en Arreglo Multidimensional

def buscar_en_matriz(matriz, valor):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == valor:
                return True, (i, j)  # Retorna True y la posición (fila, columna)
    return False, None  # No se encontró


# Matriz bidimensional 3x3
matriz = [
    [1, 5, 9],
    [4, 2, 6],
    [7, 8, 3]
]

# Valor a buscar
valor_buscar = 5

# Realizar búsqueda
encontrado, posicion = buscar_en_matriz(matriz, valor_buscar)

# Mostrar resultados
if encontrado:
    print(" El valor {valor_buscar} fue encontrado en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(" El valor {valor_buscar} no se encontró en la matriz.")