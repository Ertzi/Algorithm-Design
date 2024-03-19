import pygame
import numpy as np

# Dimensiones de la cuadrícula
n = 30  # Tamaño de la cuadrícula (nxn)
grid_size = 20  # Tamaño de cada cuadrado en píxeles
width, height = n * grid_size, n * grid_size

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dibujar Cuadrícula")

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
            if (i == 0 and j == 0):
                color = MARKED_COLOR_START
            elif (i == n - 1 and j == n - 1):
                color = MARKED_COLOR_END
            else:
                color = BLACK if grid_state[i][j] == 1 else WHITE
            pygame.draw.rect(screen, color, (j * grid_size, i * grid_size, grid_size, grid_size))
            pygame.draw.rect(screen, GRID_COLOR, (j * grid_size, i * grid_size, grid_size, grid_size), 1)

def generate_matrix():
    running = True
    drawing = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botón izquierdo del ratón
                    drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Botón izquierdo del ratón
                    drawing = False
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    x, y = event.pos
                    col = x // grid_size
                    row = y // grid_size
                    if 0 <= row < n and 0 <= col < n:
                        grid_state[row][col] = 1

        draw_grid()
        pygame.display.flip()

    pygame.quit()

    # Devolver la matriz de estado final
    return grid_state

M = generate_matrix()















# Ejemplo y ALGORITMO:

# M = [ [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
#     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]]

print(np.array(M))

def heuristico(posicion,n):
    return (n-posicion[0]) + (n-posicion[1])

def calcular_f(c,n):
    return (len(c)-1) + heuristico(c[-1],n)

def esta_dentro_del_tablero(posicion,n):
    return ( 0 <= posicion[0] ) and (posicion[0] < n) and ( 0 <= posicion[1] ) and (posicion[1] < n)

def no_choca_con_borde(nuevo_movimiento,mapa):
    x,y = nuevo_movimiento
    return mapa[x][y] != 1

def sucesores(c_min,mapa,visitados,g_visitados,A,f,n):
    movimientos = [(1,0),(0,1),(-1,0),(0,-1)]
    x,y = c_min[-1]
    for dx,dy in movimientos:
        nuevo_movimiento = (x+dx,y+dy)
        if esta_dentro_del_tablero(nuevo_movimiento,n) and no_choca_con_borde(nuevo_movimiento,mapa) and nuevo_movimiento not in c_min and nuevo_movimiento not in visitados:
            A.append(c_min + [nuevo_movimiento])
            visitados.append(nuevo_movimiento)
            g_visitados.append(len(c_min)-1)
            f.append(calcular_f(c_min + [nuevo_movimiento],n))
        
        elif esta_dentro_del_tablero(nuevo_movimiento,n) and no_choca_con_borde(nuevo_movimiento,mapa) and nuevo_movimiento not in c_min and nuevo_movimiento in visitados:
            indice_visitados = visitados.index(nuevo_movimiento)
            if len(c_min) < g_visitados[indice_visitados]:
                g_visitados[indice_visitados] = len(c_min)
                A.append(c_min + [nuevo_movimiento])
                f.append(calcular_f(c_min + [nuevo_movimiento],n))
            
def A_star(mapa,n):
    
    visitados = [(0,0)] # Importa el orden
    g_visitados = [0] # Importa el orden
    A = [ [(0,0)] ] # Lista de listas (caminos), importa el orden
    f = [ calcular_f(A[0],n) ]
    sol = None # Solucion temporal
    f_sol = float("inf") # Distancia de la mejor solucion hasta el momento (como no
    # tenemos soluciones lo definiremos como infinito)
    
    while A != []:
        min_index = np.argmin(f)
        c_min = A[min_index]
        f_c_min = f[min_index]
        A.pop(min_index)
        f.pop(min_index)
        if c_min[-1] == (n-1,n-1) and f_c_min < f_sol: # Si es una solución mejor a la que ya tenemos
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
            sucesores(c_min,mapa,visitados,g_visitados,A,f,n) # La función modificará las listas A, visitados y g_visitados
    

    return sol, f_sol


sol, f = A_star(M,len(M[0]))
print(f"Solucion: {sol}")
print(f"f = {f}")


for x,y in sol:
    M[x][y] = 2


M = np.array(M)
print(M)












# Dibujar

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dibujar Cuadrícula")

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
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (j * grid_size, i * grid_size, grid_size, grid_size))
            pygame.draw.rect(screen, GRID_COLOR, (j * grid_size, i * grid_size, grid_size, grid_size), 1)

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid(M)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
