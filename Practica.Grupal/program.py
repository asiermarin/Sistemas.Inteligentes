from collections import deque
import math 

mat = [
    [-1, -9, 0, -1, 0],
    [-8, -3, -2, 9, -7],
    [2, 0, 0, -6, 0],
    [0, -7, -3, 5, -4]
]


print(mat)
print(mat[0][0])

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
    
    _mat = None

    def ejecutar_bfs(self, mat):
        pasos = 0
        _mat = mat

        q1 = deque()
        q1.append(positivo1)
        q1.append(positivo2)
        q1.append(positivo3)

        q2 = deque()
        q2.append(positivo1)
        q2.append(positivo2)
        q2.append(positivo3)

        while q1:
            posicion_actual = None
            pasos = pasos + 1
  
            posicion_actual = q1.popleft()     
            puntos_alrededores = self.obtener_alrededores(posicion_actual)   
        
            q2.copy(q1)
            q1.clear()
            for punto in q2:
                puntos_alrededores = obtener_alrededores(punto)
                if (not self.es_positivo(punto, q2)):
                    punto = q2.popleft()

                    # En caso de no haber sido visitado, establecemos que el padre del nodo es la posici�n actual.
                    vecino.set_parent(posicion_actual)          
                    # TODO Lo a�adimos a la cola_fifo para procesar sus vecinos con posterioridad.
                    cola_fifo.append(vecino)
                    # TODO Lo a�adimos a la posiciones_visitadas para procesar sus vecinos con posterioridad.
                    posiciones_visitadas.append(vecino)
                    # De acuerdo con el modelado del mundo, * es la meta, en ese caso devolvemos vecino
                    if laberinto.get_current_point_value(vecino) == '*':
                        return vecino
        # Si recorremos todo el laberinto y no encontramos soluci�n, devolvemos el siguiente mensaje:
            return pasos
    
    def es_positivo(self, punto, q2):
        for posicion_visitada in q2:
            if ((punto.x == posicion_visitada.x) and (punto.y == posicion_visitada.y) and (self._mat[punto.x, punto.y] > 0)):
                return True
        return False

    def obtener_alrededores(self, current_point):
            neighbors = []
            potential_neighbors = [[NORTH.x, NORTH.y], [SOUTH.x, SOUTH.y], [EAST.x, EAST.y], [WEST.x, WEST.y]]
            for neighbor in potential_neighbors:
                target_point = Point(current_point.x + neighbor[0], current_point.y + neighbor[1])
                if 0 <= target_point.x < self.maze_size_x and 0 <= target_point.y < self.maze_size_y:
                    if self.get_current_point_value(target_point) != '#':
                        neighbors.append(target_point)
            return neighbors

positivo1 = Point(0, 2)
positivo2 = Point(1, 3)
positivo3 = Point(3, 3)

comenzar_teorema = Aplicar_teorema()
salida = ejecutar_bfs(mat)