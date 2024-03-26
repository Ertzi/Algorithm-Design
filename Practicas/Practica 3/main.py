import pygame
import numpy as np
from algoritmos_evaluacion import A_star


mapa_default = np.array([[]],dtype = int)
class PillaPilla:

    def __init__(self,funcion_evaluacion,profundidad_minmax,mapa):
        # Constantes durante la ejecucion: 
        self.funcion_evaluacion = funcion_evaluacion
        self.profundidad_minmax = profundidad_minmax
        self.mapa = mapa # Tiene que ser un array de NUMPY
        # Variables durante la ejecucion:
        self.posicion_perseguidor = None # Tiene que ser un array de NUMPY
        self.posicion_perseguido = None # Tiene que ser un array de NUMPY

    def minmax(self, turno_perseguidor,profundidad):
        """
        Sirve para saber cuál es la siguiente posición óptima para la máquina
        """
        if (profundidad == 0 or self.posicion_perseguido == self.posicion_perseguidor):
            return self.funcion_evaluacion(self.mapa)
        
        elif turno_perseguidor: # Turno_perseguidor == nodo min
            min = float("inf")
            caminos = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in caminos:
                turno_anterior = self.posicion_perseguidor
                self.posicion_perseguidor = self.posicion_perseguidor + np.array((dx,dy))
                valor = self.minmax(turno_perseguidor = False, profundidad=profundidad-1)  
                if valor < min:
                    min = valor
                    if profundidad == self.profundidad_minmax:
                        mejor_posicion = self.posicion_perseguidor
                self.posicion_perseguidor = turno_anterior
        elif not turno_perseguidor:
            max = float("-inf")
            caminos = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in caminos:
                turno_anterior = self.posicion_perseguido
                self.posicion_perseguido = self.posicion_perseguido + np.array((dx,dy))
                valor = self.minmax(turno_perseguidor = False, profundidad=profundidad-1)
                self.posicion_perseguido = turno_anterior





