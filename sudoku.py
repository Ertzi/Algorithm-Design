import numpy as np


# Los huecos tienen que tener el numero 0.
# Supondremos se conocen las cifras correctas de 26 celdas, se pueden conocer menos,
# pero el algoritmo tarda más. Si se colocan puntos iniciales erroneos, no dará error.
tablero =[
    [0,0,0, 0,0,0, 0,4,5],
    [0,4,0, 0,0,9, 0,0,8],
    [0,0,1, 0,5,0, 9,0,0],

    [0,2,0, 1,0,0, 5,0,9],
    [0,0,0, 7,0,5, 0,0,0],
    [4,0,7, 0,0,2, 0,8,0],

    [0,0,6, 0,7,0, 8,0,0],
    [7,0,0, 3,0,0, 0,6,0],
    [8,3,0, 0,0,0, 0,0,0]
]

tablero_incorrecto = [
    [0,0,0, 0,0,0, 4,4,5],
    [0,4,0, 0,0,9, 0,0,8],
    [0,0,1, 0,5,0, 9,0,0],

    [0,2,0, 1,0,0, 5,0,9],
    [0,0,0, 7,0,5, 0,0,0],
    [4,0,7, 0,0,2, 0,8,0],

    [0,0,6, 0,7,0, 8,0,0],
    [7,0,0, 3,0,0, 0,6,0],
    [8,3,0, 0,0,0, 0,0,0]
]


def Sudoku(tablero,S = []):
    if es_solucion(tablero): S.append( [sublista.copy() for sublista in tablero] )
    else:
        for number in range(1,10):
            i,j = posicion_libre(tablero)
            if es_posible(tablero,number,(i,j)):
                tablero[i][j] = number
                Sudoku(tablero,S)
                tablero[i][j] = 0
    return S


def es_posible(tablero,numero,posicion):
    """
    Para comprobar si es posible añadir 'numero' en 'posicion' para 'tablero'.
    Es decir, solo comprueba una fila, una columna, y una subcuadrícula
    """
    i,j = posicion
    añadido = [sublista.copy() for sublista in tablero]
    añadido[i][j] = numero
    # Filas
    if len(lista_unica(tablero[i][:])) != (len(lista_unica(añadido[i][:])) - 1):
        return False
    # Columnas:
    traspuesta = [[fila[i] for fila in tablero] for i in range(len(tablero[0]))]
    traspuesta_añadida = [[fila[i] for fila in añadido] for i in range(len(añadido[0]))]
    if len(lista_unica(traspuesta[j][:])) != (len(lista_unica(traspuesta_añadida[j][:])) - 1):
        return False
    # Cuadricula:
    indices = [0,0,0,3,3,3,6,6,6]
    cuadricula = []
    cuadricula_añadido = []
    for k in range(indices[i],indices[i]+3):
        list = []
        list2 = []
        for l in range(indices[j],indices[j]+3):
            list.append(añadido[k][l])
            list2.append(tablero[k][l])
        cuadricula.append(list2)
        cuadricula_añadido.append(list)
    if len(lista_unica2(cuadricula)) != (len(lista_unica2(cuadricula_añadido)) - 1):
        return False
        
    # Else:
    return True

def lista_unica(lista):
    k = []
    for element in lista:
        if not(element in k) and element != 0:
            k.append(element)
    return k

def lista_unica2 (matriz):
    k = []
    for lista in matriz:
        for element in lista:
                if not(element in k) and element != 0:
                    k.append(element)
    return k

def es_solucion(tablero):
    """
    Para comprobar si es la solución, por cómo hemos hecho el código, solo hace falta comprobar
    si quedan posiciones libres en el tablero
    """
    return len(np.argwhere(np.array(tablero) == 0)) == 0

def posicion_libre(tablero):
    """
    Encuentra la primera posición libre y la devuelve.
    """
    return np.argwhere(np.array(tablero) == 0)[0]



soluciones = Sudoku(tablero)
solucion = soluciones[0]
print(f"La solución es: \n{np.array(solucion)}")

# Comprobacin (codigo chat GPT):
    
def es_solucion_sudoku(matriz):
    # Verificar filas
    for fila in matriz:
        if len(set(fila)) != 9 or any(x not in range(1, 10) for x in fila):
            return False
    
    # Verificar columnas
    for j in range(9):
        columna = [matriz[i][j] for i in range(9)]
        if len(set(columna)) != 9 or any(x not in range(1, 10) for x in columna):
            return False
    
    # Verificar subcuadros 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subcuadro = [matriz[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(subcuadro)) != 9 or any(x not in range(1, 10) for x in subcuadro):
                return False
    
    return True

for sol in soluciones:
    print(f"Es solucion?: {es_solucion_sudoku(sol)}\n")


print(f"La solución es: \n{np.array(Sudoku(tablero_incorrecto,[]))}\n")
