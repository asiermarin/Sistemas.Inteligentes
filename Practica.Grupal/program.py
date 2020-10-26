from collections import deque
import math
import numpy as np

mat = [
    [-1, -9, 0, -1, 0],
    [-8, -3, -2, 9, -7],
    [2, 0, 0, -6, 0],
    [0, -7, -3, 5, -4]
]
rows = len(mat)
columns = len(mat[0])

print(rows)
print(columns)
print(np.matrix(mat))

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.cost = math.inf

    def set_parent(self, p):
        self.parent = p

    def set_cost(self, c):
        self.cost = c

    def print(self):
        print(self.x, ',', self.y)

NORTH = Point(0, 1)
SOUTH = Point(0, -1)
EAST = Point(1, 0)
WEST = Point(-1, 0)

class Aplicar_teorema:

    def __init__(self, anchura_matriz, altura_matriz, mat):
        self.anchura_matriz = anchura_matriz
        self.altura_matriz = altura_matriz
        self._mat = mat
        self.ejercutar_busqueda_dfs()

    def ejercutar_busqueda_dfs(self):
        pasos = 0
        cola_puntos = deque()
        cola_puntos.append(positivo1)
        cola_puntos.append(positivo2)
        cola_puntos.append(positivo3)

        cola_puntos_intento = deque()
        while cola_puntos:
            pasos = pasos + 1
            cola_puntos_intento = cola_puntos.copy()
            cola_puntos.clear()
            puntos_alrededores_positivos = []
            for punto in cola_puntos_intento:    
                puntos_alrededores_positivos = self.devolver_puntos_alrededores_positivos(punto)
            for punto_alrededor in puntos_alrededores_positivos:
                cola_puntos_intento.append(punto_alrededor)
            cola_puntos.copy(cola_puntos_intento)
            pasos = pasos + 1
            print(pasos)
            print(np.matrix(self._mat))
            return pasos


    def devolver_puntos_alrededores_positivos(self, punto_actual):
        posiciones_alrededores = []
        posibles_alrededores = [[NORTH.x, NORTH.y], [SOUTH.x, SOUTH.y], [EAST.x, EAST.y], [WEST.x, WEST.y]]
        for punto_alrededor in posibles_alrededores:
            punto_cardinal = Point(punto_actual.x + punto_alrededor[0], punto_actual.y + punto_alrededor[1])
            if (0 <= punto_cardinal.x < self.anchura_matriz and 0 <= punto_cardinal.y < self.altura_matriz):
                if (self.obtener_posicion_matriz(punto_cardinal) < 0):
                    self.sustituir_valor_matriz(punto_cardinal)
                    posiciones_alrededores.append(punto_cardinal)
        return posiciones_alrededores


    def obtener_posicion_matriz(self, current_point):
        return self._mat[current_point.x][current_point.y]
    
    def sustituir_valor_matriz(self, punto_cardinal):
            self._mat[punto_cardinal.x][punto_cardinal.y] = abs(self._mat[punto_cardinal.x][punto_cardinal.y])

print(mat[4][3])

positivo1 = Point(0, 2)
positivo2 = Point(1, 3)
positivo3 = Point(3, 3)

aplicar_dfs = Aplicar_teorema(5, 4, mat)