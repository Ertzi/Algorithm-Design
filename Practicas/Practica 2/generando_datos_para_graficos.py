import time
from algoritmos import caballo_en_anchura, caballo_profundidad_1, caballo_profundidad_2, caballo_en_anchura_nodos_visitados, profund_1_nodos_visitados, profund_2_nodos_visitados
from collections import deque
from graficos import graficar_matriz
import numpy as np

# En VSCode, ctrl + k + c para comentar varias lineas, ctrl + k + u para descomentarlas

# Graficos del número de soluciones y tiempos de ejecución por casilla para n = 5

# Variables que usaremos:
n = 5
numero_de_soluciones1 = []
numero_de_soluciones2 = []
numero_de_soluciones3 = []
tiempos_de_ejecucion_prof1 = []
tiempos_de_ejecucion_prof2 = []
tiempos_de_ejecucion_anch = []

# Ejecutar los algoritmos para todas las casillas:
for x in range(5):
    lista_tiempo1 = []
    lista_tiempo2 = []
    lista_tiempo3 = []
    lista_sol1 =[]
    lista_sol2 =[]
    lista_sol3 =[]
    for y in range(5):
        # Profundidad 1
        start_time = time.time()
        lista_sol1.append(len(caballo_profundidad_1(n,deque([(x,y)]),deque([]))))
        end_time = time.time()
        lista_tiempo1.append(end_time - start_time)
        # Profundidad 2
        start_time = time.time()
        lista_sol2.append(len(caballo_profundidad_2(n,deque([(x,y)]),deque([]))))
        end_time = time.time()
        lista_tiempo2.append(end_time - start_time)
        # Anchura
        start_time = time.time()
        lista_sol3.append(len(caballo_en_anchura(n,x,y)))
        end_time = time.time()
        lista_tiempo3.append(end_time - start_time)

    numero_de_soluciones1.append(lista_sol1)
    numero_de_soluciones2.append(lista_sol2)
    numero_de_soluciones3.append(lista_sol3)

    tiempos_de_ejecucion_prof1.append(lista_tiempo1)
    tiempos_de_ejecucion_prof2.append(lista_tiempo2)
    tiempos_de_ejecucion_anch.append(lista_tiempo3)

# Redondear los tiempos:
for x in range(len(tiempos_de_ejecucion_prof1)):
    for y in range(len(tiempos_de_ejecucion_prof1[0])):
        tiempos_de_ejecucion_prof1[x][y] = round(tiempos_de_ejecucion_prof1[x][y],3)
        tiempos_de_ejecucion_prof2[x][y] = round(tiempos_de_ejecucion_prof2[x][y],3)
        tiempos_de_ejecucion_anch[x][y] = round(tiempos_de_ejecucion_anch[x][y],3)

# Hacemos print de las listas obtenidas:
print(numero_de_soluciones1)
print(numero_de_soluciones2)
print(numero_de_soluciones3)        

print(tiempos_de_ejecucion_prof1)
print(tiempos_de_ejecucion_prof2)
print(tiempos_de_ejecucion_anch)

# Calcular la cantidad de nodos a los que se llega para cada casilla

# Variables que usaremos:
n = 5
nodos1 = []
nodos2 = []
nodos3 = []

# Calcular la cantidad de nodos visitados:
for x in range(n):
    lista1 = []
    lista2 = []
    lista3 = []
    for y in range(n):
        lista1.append(profund_1_nodos_visitados(n,[1],deque([(x,y)])))
        lista2.append(profund_2_nodos_visitados(n,[1],deque([(x,y)])))
        lista3.append(caballo_en_anchura_nodos_visitados(n,x,y))
    nodos1.append(lista1)
    nodos2.append(lista2)
    nodos3.append(lista3)

# Ver los resultados para guardarlos:
print(nodos1)
print(nodos2)
print(nodos3)

