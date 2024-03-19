def numero_mochilas_vacias(M):
    return M.count([])

def volumen(mochila):
    vol =sum(mochila)
    return vol

def es_posible_insertar(elemento,M,i,S,capacidad_mochila):
    if volumen(M[i]) + elemento > capacidad_mochila:
        return False
    copia = []
    for mochila in M:
        copia.append(mochila.copy())
    copia[i] = copia[i] + [elemento]
    if len(S) > 0 and (numero_mochilas_vacias(S[0]) > numero_mochilas_vacias(copia)):
        return False
    return True

def es_posible_insertar_2(elemento,M,i,S,capacidad_mochila):
    return not (volumen(M[i]) + elemento > capacidad_mochila)

def Mochilas(M,V,capacidad_mochila,S = [],iteraciones = [0]):
    # print(f"{S}")
    iteraciones[0]+=1
    if V == []:
        if len(S) > 0 and numero_mochilas_vacias(S[0]) < numero_mochilas_vacias(M):
            lista = []
            for mochila in M:
                lista.append(mochila.copy())
            S[0] = lista
        elif len(S) == 0:
            lista = []
            for mochila in M:
                lista.append(mochila.copy())
            S.append(lista)
    else:
        elemento = V[0]
        for i,mochila in enumerate(M):
            if es_posible_insertar(elemento,M,i,S,capacidad_mochila):
                mochila.append(elemento)
                Mochilas(M,V[1:],capacidad_mochila,S)
                mochila.pop()
    return S,iteraciones[0]


def Mochilas_2(M,V,capacidad_mochila,S = [],iteraciones = [0]):
    # print(f"{S}")
    iteraciones[0]+=1
    if V == []:
        if len(S) > 0 and numero_mochilas_vacias(S[0]) < numero_mochilas_vacias(M):
            lista = []
            for mochila in M:
                lista.append(mochila.copy())
            S[0] = lista
        elif len(S) == 0:
            lista = []
            for mochila in M:
                lista.append(mochila.copy())
            S.append(lista)
    else:
        elemento = V[0]
        for i,mochila in enumerate(M):
            if es_posible_insertar_2(elemento,M,i,S,capacidad_mochila):
                mochila.append(elemento)
                Mochilas_2(M,V[1:],capacidad_mochila,S)
                mochila.pop()
    return S,iteraciones[0]




# Ejemplo:

m = 8 # Numero de mochilas disponibles
V = [2,8,3,4,7,3] # n = 6: numero de objetos
capacidad_mochila = 12
M = [[] for _ in range(m)] # Mochilas vacías

solucion,iter = Mochilas(M,V,capacidad_mochila) # Con poda
print(solucion,iter)

solucion,iter = Mochilas_2(M,V,capacidad_mochila) # Sin poda
print(solucion,iter)

