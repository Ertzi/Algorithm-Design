from collections import deque # Libreria de Python para usar colas

# Funciones auxiliares

def es_posible(n,tupla):
    x,y = tupla
    return (0 <= x) and (x < n) and (0 <= y) and (y < n)

def sucesores(A,n):
    """
    A : lista de tuplas que representan posiciones en los que el caballo ya ha estado
    Devuelve una lista de listas con todos los posibles caminos
    """
    movimientos = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
    sucesores_posibles = []
    x,y = A[-1]
    for (dx,dy) in movimientos:
       if (not ((x+dx,y+dy) in A)) and es_posible(n,(x+dx,y+dy)):
          sucesores_posibles.append(A+[(x+dx,y+dy)])
    return sucesores_posibles

# Algoritmos de profundidad

def caballo_profundidad_1(n,A,S = deque([]).copy()):
    """
    Toma como input un número entero n y un objeto tipo deque A (A = deque([x0,y0]))
    """
    x,y = A[-1]
    movimientos = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
    for dx,dy in movimientos:
        if (not ((x+dx,y+dy) in A)) and es_posible(n,(x+dx,y+dy)) and (len(A) < n**2):
            A.append((x+dx,y+dy))
            caballo_profundidad_1(n,A,S)
            A.pop()
    if len(A) == n**2:
       S.append(A.copy())
    return S

def caballo_profundidad_2(n,A,S = deque([]).copy()):
    """
    Toma como input un número entero n y un objeto tipo deque A (A = deque([x0,y0]))
    """
    x,y = A[-1] 
    movimientos = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
    for dx,dy in movimientos:
        if (not ((x+dx,y+dy) in A)) and es_posible(n,(x+dx,y+dy)) and (len(A) < n**2):
            caballo_profundidad_2(n,A + deque([(x+dx,y+dy)]),S)
    if len(A) == n**2:
       S.append(A.copy())
    return S

# Algoritmos de profundidad contando la cantidad de nodos visitados:

def profund_1_nodos_visitados(n,k,A,S = deque([]).copy()):
    """
    Toma como input un número entero n y un objeto tipo deque A (A = deque([x0,y0]))
    """
    x,y = A[-1]
    movimientos = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
    for dx,dy in movimientos:
        if (not ((x+dx,y+dy) in A)) and es_posible(n,(x+dx,y+dy)) and (len(A) < n**2):
            A.append((x+dx,y+dy))
            k[0] = k[0] + 1
            profund_1_nodos_visitados(n,k,A,S)
            A.pop()
    if len(A) == n**2:
       S.append(A.copy())
    return k[0]

def profund_2_nodos_visitados(n,k,A,S = deque([]).copy()):
    """
    Toma como input un número entero n y un objeto tipo deque A (A = deque([x0,y0]))
    """
    x,y = A[-1] 
    movimientos = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
    for dx,dy in movimientos:
        if (not ((x+dx,y+dy) in A)) and es_posible(n,(x+dx,y+dy)) and (len(A) < n**2):
            k[0] = k[0] + 1
            profund_2_nodos_visitados(n,k,A + deque([(x+dx,y+dy)]),S)
    if len(A) == n**2:
       S.append(A.copy())
    return k[0]

# Algoritmo en anchura

def caballo_en_anchura(n,x0,y0):
    S = []
    V = deque([[(x0,y0)]])
    while V != deque([]):
        X = V[0]
        if len(X) == n**2:
            S.append(X)
        else:
            sucesores_X = sucesores(X,n)
            if sucesores_X != []:
                V.extend(sucesores_X)
        V.popleft()    
    return S

# Algoritmo en anchura contando la cantidad de nodos visitados:

def caballo_en_anchura_nodos_visitados(n,x0,y0):
    S = []
    V = deque([[(x0,y0)]])
    i = 0
    while V != deque([]):
        X = V[0]
        i += 1
        if len(X) == n**2:
            S.append(X)
        else:
            sucesores_X = sucesores(X,n)
            if sucesores_X != []:
                V.extend(sucesores_X)
        V.popleft()
    return i

