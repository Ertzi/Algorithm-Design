import pygame
import numpy as np

# Dimensiones de la cuadrícula
n = 30  # Tamaño de la cuadrícula (nxn)
grid_size = 20  # Tamaño de cada cuadrado en píxeles
width, height = n * grid_size, n * grid_size

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dibujar Mapa: click izq = bordes; click drch = posiciones; click rueda = limpiar")

# Colores
WHITE = (238,238,210)
BLACK = (186,202,68)
GRID_COLOR = (200, 200, 200) # Color de fondo de la cuadrícula
MARKED_COLOR_START = (255, 255, 255) # Color para las posiciones marcadas
MARKED_COLOR_END = (255, 0, 0) 

# Crear matriz para almacenar el estado de los cuadrados
grid_state = np.zeros((n, n), dtype=int)

def draw_grid():
    screen.fill(GRID_COLOR)  # Rellenar el fondo con el color de la cuadrícula
    for i in range(n):
        for j in range(n):
            if grid_state[i][j] == 3:
                color = MARKED_COLOR_START
            elif grid_state[i][j] == 4:
                color = MARKED_COLOR_END
            else:
                color = BLACK if grid_state[i][j] == 1 else WHITE
            pygame.draw.rect(screen, color, (j * grid_size, i * grid_size, grid_size, grid_size))
            pygame.draw.rect(screen, GRID_COLOR, (j * grid_size, i * grid_size, grid_size, grid_size), 1)

def generate_matrix():
    running = True
    drawing = False
    cleaning = False
    timer = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1:  # Botón izquierdo del ratón
                    drawing = True
                    x, y = event.pos
                    col = x // grid_size
                    row = y // grid_size
                    if 0 <= row < n and 0 <= col < n:
                        grid_state[row][col] = 1

                elif event.button == 3 and timer == 0: # Boton derecho del raton
                    timer +=1
                    x, y = event.pos
                    col = x // grid_size
                    row = y // grid_size
                    if 0 <= row < n and 0 <= col < n:
                        grid_state[row][col] = 3 # == 3 is INITIAL POINT (WHITE)
                    
                elif event.button == 3 and timer == 1:
                    timer -= 1
                    x, y = event.pos
                    col = x // grid_size
                    row = y // grid_size
                    if 0 <= row < n and 0 <= col < n:
                        grid_state[row][col] = 4 # == 4 is END POINT (RED)
                
                elif event.button == 2:
                    x, y = event.pos
                    col = x // grid_size
                    row = y // grid_size
                    if 0 <= row < n and 0 <= col < n:
                        grid_state[row][col] = 0 # Clean wrong cells
                    cleaning = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Botón izquierdo del ratón
                    drawing = False
                if event.button == 2:
                    cleaning = False
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    x, y = event.pos
                    col = x // grid_size
                    row = y // grid_size
                    if 0 <= row < n and 0 <= col < n:
                        grid_state[row][col] = 1
                if cleaning:
                    x, y = event.pos
                    col = x // grid_size
                    row = y // grid_size
                    if 0 <= row < n and 0 <= col < n:
                        grid_state[row][col] = 0

        draw_grid()
        pygame.display.flip()

    pygame.quit()

    # Devolver la matriz de estado final
    return grid_state

M = generate_matrix()













# Ejemplo y ALGORITMO:

# Para ejecutar el ejemplo siguiente, poner n = 15

# M = [ [3, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 4]]












# ---------------------------------------------------------------
# ---------------------INICIO ALGORITMO--------------------------
# ---------------------------------------------------------------
def heuristico(posicion,posicion_final):
    return abs(posicion_final[0]-posicion[0]) + abs(posicion_final[1]-posicion[1])

def calcular_f(c,posicion_final):
    return (len(c)-1) + heuristico(c[-1],posicion_final)

def esta_dentro_del_tablero(posicion,n):
    return ( 0 <= posicion[0] ) and (posicion[0] < n) and ( 0 <= posicion[1] ) and (posicion[1] < n)

def no_choca_con_borde(nuevo_movimiento,mapa):
    x,y = nuevo_movimiento
    return mapa[x][y] != 1

def sucesores(c_min,mapa,visitados,g_visitados,A,f,n,posicion_final):
    movimientos = [(1,0),(0,1),(-1,0),(0,-1)]
    x,y = c_min[-1]
    for dx,dy in movimientos:
        nuevo_movimiento = (x+dx,y+dy)
        if esta_dentro_del_tablero(nuevo_movimiento,n) and no_choca_con_borde(nuevo_movimiento,mapa) and nuevo_movimiento not in c_min and nuevo_movimiento not in visitados:
            A.append(c_min + [nuevo_movimiento])
            visitados.append(nuevo_movimiento)
            g_visitados.append(len(c_min)-1)
            f.append(calcular_f(c_min + [nuevo_movimiento],posicion_final))
        
        elif esta_dentro_del_tablero(nuevo_movimiento,n) and no_choca_con_borde(nuevo_movimiento,mapa) and nuevo_movimiento not in c_min and nuevo_movimiento in visitados:
            indice_visitados = visitados.index(nuevo_movimiento)
            if len(c_min) < g_visitados[indice_visitados]:
                g_visitados[indice_visitados] = len(c_min)
                A.append(c_min + [nuevo_movimiento])
                f.append(calcular_f(c_min + [nuevo_movimiento],posicion_final))
                print("AAAAAA")
            
def A_star(mapa,n):
    
    posicion_inicial = (0,0)
    posicion_final = (n-1,n-1)
    for i,fila in enumerate(mapa):
        for j,valor in enumerate(fila):
            if valor == 3:
                posicion_inicial = (i,j)
            elif valor == 4:
                posicion_final = (i,j)

    if posicion_inicial == (0,0):
        mapa[0][0] = 3
    if posicion_final == (n-1,n-1):
        mapa[n-1][n-1] = 4

    print(f"Posicion inicial = {posicion_inicial}")
    print(f"Posicion final = {posicion_final}")

    visitados = [posicion_inicial] # Importa el orden
    g_visitados = [0] # Importa el orden
    A = [ [posicion_inicial] ] # Lista de listas (caminos), importa el orden
    f = [ calcular_f(A[0],posicion_final) ]
    sol = None # Solucion temporal
    f_sol = float("inf") # Distancia de la mejor solucion hasta el momento (como no
    # tenemos soluciones lo definiremos como infinito)
    
    while A != []:
        min_index = np.argmin(f)
        c_min = A[min_index]
        f_c_min = f[min_index]
        A.pop(min_index)
        f.pop(min_index)
        if c_min[-1] == posicion_final and f_c_min < f_sol: # Si es una solución mejor a la que ya tenemos
            # Actualizar solucion y coste minimo:
            sol = c_min[:]
            f_sol = f_c_min
            # Podar:
            indices_para_podar = []
            for i,f_i in enumerate(f):
                if f_i > f_sol:
                    indices_para_podar.append(i)
            A = [camino for indice,camino in enumerate(A) if indice not in indices_para_podar]
            f = [valor_f for indice, valor_f in enumerate(f) if indice not in indices_para_podar]

        else: # Si no es solución o es peor que la que ya tenemos
            sucesores(c_min,mapa,visitados,g_visitados,A,f,n,posicion_final) # La función modificará las listas A, visitados y g_visitados
    

    return sol, f_sol


# ---------------------------------------------------------------
# ----------------------FINAL ALGORITMO--------------------------
# ---------------------------------------------------------------
















sol, f = A_star(M,len(M[0]))
print(f"Solucion: {sol}")
print(f"f = {f}")


for x,y in sol[1:-1]:
    M[x][y] = 2

M = np.array(M)













# Dibujar

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(f"Solucion, pasos necesarios = {f}")

# Colores
# Color de fondo de la cuadrícula
MARKED_COLOR = (65, 43,21)     # Color para las posiciones marcadas

def draw_grid(grid):
    screen.fill(GRID_COLOR)  # Rellenar el fondo con el color de la cuadrícula
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                color = BLACK
            elif grid[i][j] == 2:
                color = MARKED_COLOR
            elif grid[i][j] == 3:
                color = MARKED_COLOR_START
            elif grid[i][j] == 4:
                color = MARKED_COLOR_END
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (j * grid_size, i * grid_size, grid_size, grid_size))
            pygame.draw.rect(screen, GRID_COLOR, (j * grid_size, i * grid_size, grid_size, grid_size), 1)

def dibujar_solucion():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid(M)
        pygame.display.flip()

    pygame.quit()

dibujar_solucion()