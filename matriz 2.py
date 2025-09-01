# Programa 2: Ordenación de Arreglo Multidimensional

def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio

# Matriz bidimensional 3x3
matriz = [
    [1, 5, 9],
    [4, 2, 6],
    [7, 8, 3]
]

# Mostrar matriz original
print(" Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (por ejemplo, la fila 1, índice 1)
fila_a_ordenar = 1

# Copia de la matriz para no modificar la original
matriz_ordenada = [fila.copy() for fila in matriz]

# Aplicar ordenamiento a la fila seleccionada
bubble_sort_fila(matriz_ordenada[fila_a_ordenar])

# Mostrar resultado
print("\n Matriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz_ordenada:
    print(fila)