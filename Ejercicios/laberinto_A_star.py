import pygame
import numpy as np

# Dimensiones de la cuadrícula
n = 15  # Tamaño de la cuadrícula (nxn)
grid_size = 50  # Tamaño de cada cuadrado en píxeles
width, height = n * grid_size, n * grid_size

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dibujar Cuadrícula")

# Colores
WHITE = (238,238,210)
BLACK = (186,202,68)
GRID_COLOR = (200, 200, 200)  # Color de fondo de la cuadrícula
MARKED_COLOR_START = (255, 255, 255)     # Color para las posiciones marcadas
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

def main():
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

if __name__ == "__main__":
    final_grid_state = main()
    # print("Matriz final:")
    # print(final_grid_state)
    # print(final_grid_state.tolist())

M = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 
1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 1, 0, 1, 0, 
1, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]]

def heuristico(c,n):
    """
    El heuristico será la distancia de Manhattan
    """
    x,y = c[-1]
    return len(c)-1 + abs(n-1 - x) + abs(n-1 - y)

def dentro_del_tablero(posicion,n):
    return ( 0 <= posicion[0] ) and (posicion[0] < n) and ( 0 <= posicion[1] ) and (posicion[1] < n)

def sucesores(c,mapa,f_min):
    movimientos = [(0,1),(1,0),(0,-1),(-1,0)] # Para encontrar los sucesores
    sucesores = []
    x,y = c[-1]
    for dx,dy in movimientos:
        x_new, y_new = x + dx, y + dy
        if dentro_del_tablero((x_new,y_new),n) and not((x_new,y_new) in c) and mapa[x_new][y_new] != 1: # No dejamos al algoritmo volver atrás
            heur = heuristico(c + [(x_new,y_new)],n)
            if heur <= f_min:
                sucesores.append((c + [(x_new,y_new)],heur))
    print(f"c =\n [{c}, {f_min}]")
    print(f"sucesores = \n{sucesores}")
    print("\n")
    return sucesores

def argmin(A):
    c = []
    f_c = float("inf")
    for list,value in A:
        print(f"list = {list}")
        print(f"value = {value}")
        print(f"Desigualdad: {value < f_c}")
        if value < f_c:
            c = list
            f_c = value
    return c,f_c

def A_star(mapa):
    
    A = [ ( [(0,0)]  , abs(n-1 - 0) + abs(n-1 -0) ) ] # Lista de tuplas
    f_min = float("inf")

    while A != [] and len(A) <20:
        c,f_c = argmin(A)
        # print(f"c = {c}")
        # print(f"f_c = {f_c}")
        if c[-1] == (n-1,n-1) and f_c < f_min:
            sol = c
            f_min = f_c
            print("SOLUCION")
            indices_para_eliminar = []
            for i in range(len(A)):
                camino = A[i][0]
                f = A[i][1]
                if f > f_min:
                    indices_para_eliminar.append(i)
            indices_para_eliminar.sort(reverse=True)
            for indice in indices_para_eliminar:
                A.pop[indice]
        else:
            A = A + sucesores(c,mapa,f_min)
        
        i = A.index((c,f_c))
        A.pop(i)
        
    return sol, f_min
        

sol, f = A_star(M)
print(f"Solucion: {sol}")
print(f"f = {f}")