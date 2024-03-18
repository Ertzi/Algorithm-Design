import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Código para hacer gráficos:

def dibujar_solución(n,tuplas, titulo =""):
    matriz = []
    for i in range(n):
        lista = []
        for j in range(n):
            lista.append(0)
        matriz.append(lista)
    
    for i, (x,y) in enumerate(tuplas):
        matriz[x][y] = i+1


    # Crear una figura y un eje
    fig, ax = plt.subplots()

    # Dibujar cuadrícula en blanco y negro
    for i in range(n):
        for j in range(n):
            color = "palegoldenrod" if (i + j) % 2 == 0 else "yellowgreen"
            ax.add_patch(plt.Rectangle((j, n-i-1), 1, 1, fill=True, color=color))

            # Colocar el número en el centro de la casilla
            ax.text(j + 0.5, n - i - 0.5, str(matriz[i][j]), color='black',
                    size=12, va='center', ha='center')

    # Configurar límites y aspecto
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    # Mostrar el gráfico
    plt.title(titulo)
    plt.show()

def graficar_matriz(matriz,min, max,leyenda="",titulo = "",paleta = "seismic",text_color = "white"):
    """
    Grafica una matriz introducida con colores en base a los números de la matriz
    """
    n = len(matriz)
    # Crear una cuadrícula de subgráficos
    fig, ax = plt.subplots()

    # Crear una cuadrícula nxn con colores en las casillas equivalentes a los valores de la matriz
    cmap = plt.get_cmap(paleta)  # Puedes cambiar 'viridis' por otro mapa de colores
    cax = ax.matshow(matriz, cmap=cmap, vmin = min, vmax = max)

    # Mostrar los números en las casillas
    for i in range(n):
        for j in range(n):
            ax.text(j, i, str(matriz[i, j]), va='center', ha='center', color=text_color)

    # Ocultar los números en los ejes
    ax.set_xticks([])
    ax.set_yticks([])

    # Añadir una leyenda a la derecha
    cbar = fig.colorbar(cax)
    cbar.set_label(leyenda)
    plt.title(titulo)

    # Mostrar el gráfico
    plt.show()


# Graficos (las listas las hemos conseguido mediante el script "generando_datos_para_graficos.py"):
    
# Ejemplo de solución
solucion_ejemplo = deque([(0, 0), (1, 2), (2, 4), (4, 3), (3, 1), (1, 0), (2, 2), (0, 3), (1, 1), (3, 0), (4, 2), (3, 4), (1, 3), (0, 1), (2, 0), (4, 1), (3, 3), (1, 4), (0, 2), (2, 1), (4, 0), (3, 2), (4, 4), (2, 3), (0, 4)])
dibujar_solución(5,solucion_ejemplo,titulo = "Número de soluciones")

# Número de soluciones:
m4 = np.matrix([[304, 0, 56, 0, 304], [0, 56, 0, 56, 0], [56, 0, 64, 0, 56], [0, 56, 0, 56, 0], [304, 0, 56, 0, 304]])
m5 = np.matrix([[304, 0, 56, 0, 304], [0, 56, 0, 56, 0], [56, 0, 64, 0, 56], [0, 56, 0, 56, 0], [304, 0, 56, 0, 304]])
m6 = np.matrix([[304, 0, 56, 0, 304], [0, 56, 0, 56, 0], [56, 0, 64, 0, 56], [0, 56, 0, 56, 0], [304, 0, 56, 0, 304]])

graficar_matriz(m4,0,304,"Número de soluciones por casilla", "Número de soluciones algoritmo en profundidad 1")
graficar_matriz(m5,0,304,"Número de soluciones por casilla", "Número de soluciones algoritmo en profundidad 2")
graficar_matriz(m6,0,304,"Número de soluciones por casilla", "Número de soluciones algoritmo en anchura")

# Tiempos de ejecución:
m1 = np.matrix([[7.959, 7.68, 6.081, 7.703, 7.318], [7.661, 6.097, 4.233, 6.07, 7.691], [6.063, 4.233, 2.627, 4.22, 6.044], [7.733, 6.079, 4.277, 6.151, 7.675], [7.377, 7.673, 6.048, 7.702, 7.363]])
m2 = np.matrix([[7.993, 8.437, 6.497, 8.211, 7.916], [8.16, 6.501, 4.508, 6.543, 8.75], [6.449, 4.585, 2.827, 4.64, 6.522], [8.226, 6.527, 4.679, 6.603, 8.334], [7.834, 8.224, 6.471, 8.334, 7.839]])
m3 = np.matrix([[8.652, 9.363, 7.241, 9.531, 8.65], [9.218, 7.234, 4.876, 7.216, 9.276], [7.108, 4.921, 2.978, 4.848, 7.127], [9.234, 7.247, 5.137, 7.278, 9.627], [8.712, 9.38, 7.192, 9.327, 9.012]])

graficar_matriz(m1,0,10,"Segundos por casilla", "Tiempos de ejecución algoritmo en profundidad 1","viridis","black")
graficar_matriz(m2,0,10,"Segundos por casilla", "Tiempos de ejecución algoritmo en profundidad 2","viridis","black")
graficar_matriz(m3,0,10,"Segundos por casilla", "Tiempos de ejecución algoritmo en anchura","viridis","black")

# Número de nodos visitados:
nodos1 = np.matrix([[1735079, 1829421, 1453989, 1829421, 1735079], [1829421, 1465477, 1028893, 1465477, 1829421], [1453989, 1028893, 641577, 1028893, 1453989], [1829421, 1465477, 1028893, 1465477, 1829421], [1735079, 1829421, 1453989, 1829421, 1735079]])
nodos2 = np.matrix([[1735079, 1829421, 1453989, 1829421, 1735079], [1829421, 1465477, 1028893, 1465477, 1829421], [1453989, 1028893, 641577, 1028893, 1453989], [1829421, 1465477, 1028893, 1465477, 1829421], [1735079, 1829421, 1453989, 1829421, 1735079]])
nodos3 = np.matrix([[1735079, 1829421, 1453989, 1829421, 1735079], [1829421, 1465477, 1028893, 1465477, 1829421], [1453989, 1028893, 641577, 1028893, 1453989], [1829421, 1465477, 1028893, 1465477, 1829421], [1735079, 1829421, 1453989, 1829421, 1735079]])

min1 = np.min(nodos1)
max1 = np.max(nodos1)
min2 = np.min(nodos2)
max2 = np.max(nodos2)
min3 = np.min(nodos3)
max3 = np.max(nodos3)

graficar_matriz(nodos1,min1,max1,"Nodos visitados por casilla", "Nodos visitados algoritmo en profundidad 1","viridis","black")
graficar_matriz(nodos2,min2,max2,"Nodos visitados por casilla", "Nodos visitados algoritmo en profundidad 2","viridis","black")
graficar_matriz(nodos3,min3,max3,"Nodos visitados por casilla", "Nodos visitados algoritmo en anchura","viridis","black")


print(nodos1 == nodos2, nodos2 == nodos3, nodos3 == nodos1)
