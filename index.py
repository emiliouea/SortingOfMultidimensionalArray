def ordenacion_bubble_sort(lista):
    """
    Ordena una lista utilizando el algoritmo de Bubble Sort.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def imprimir_matriz(matriz):
    """
    Imprime la matriz en un formato legible.
    """
    for fila in matriz:
        print(fila)

def ordenar_fila(matriz, indice_fila):
    """
    Ordena una fila específica de la matriz utilizando Bubble Sort.
    """
    if 0 <= indice_fila < len(matriz):
        ordenacion_bubble_sort(matriz[indice_fila])
    else:
        print("Índice de fila fuera de rango.")

# Matriz original
matriz = [
    [3, 1, 2],
    [9, 7, 8],
    [6, 4, 5]
]

# Mostrar matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Ordenar la fila 1 (segunda fila)
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)



# Mostrar matriz con la fila ordenada
print(f"\nMatriz después de ordenar la fila {fila_a_ordenar}:")
imprimir_matriz(matriz)
