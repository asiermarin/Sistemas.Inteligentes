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
    NEGATIVO = -1

    def __init__(self, mat_size_x, mat_size_y, mat):
        self.mat_size_x = mat_size_x
        self.mat_size_y = mat_size_y
        _mat = mat

    def ejecutar_bfs(self):
        pasos = 0
        q1 = deque()
        q1.append(positivo1)
        q1.append(positivo2)
        q1.append(positivo3)

        q2 = deque()
        while q1:
            posicion_actual = None
            pasos = pasos + 1
            q2 = q1.copy()
            q1.clear()
            for punto in q2:    
                puntos_alrededores = self.obtener_alrededores_negativos(punto)
                for punto_alrededor in puntos_alrededores:
                    if (not self.es_positivo(punto, q2)):
                        # punto = q2.popleft()
                        punto_positivo = punto * (NEGATIVO)
                        q1.append(punto_positivo)
            pasos = pasos + 1
            print(pasos)
            return pasos
    
    def es_positivo(self, punto, q2):
        for posicion_visitada in q2:
            if ((punto.x == posicion_visitada.x) and (punto.y == posicion_visitada.y) and (self._mat[punto.x, punto.y] > 0)):
                return True
        return False

    def obtener_alrededores_negativos(self, current_point):
            neighbors = []
            potential_neighbors = [[NORTH.x, NORTH.y], [SOUTH.x, SOUTH.y], [EAST.x, EAST.y], [WEST.x, WEST.y]]
            for neighbor in potential_neighbors:
                target_point = Point(current_point.x + neighbor[0], current_point.y + neighbor[1])
                if 0 <= target_point.x < self.mat_size_x and 0 <= target_point.y < self.mat_size_y:
                    if self.get_current_point_value(target_point) != 0:
                        neighbors.append(target_point)
            return neighbors

    def get_current_point_value(self, current_point):
        return self._mat[current_point.x][current_point.y]

    def overlay_points_on_map(self, points):
        overlay_map = copy.deepcopy(self.maze)
        for point in points:
            # new_row = overlay_map[point.x][:point.y] + '@' + overlay_map[point.x][point.y + 1:]
            new_row = 1
            overlay_map[point.x] = new_row

    def get_path(point):
        path = []
        current_point = point
        while current_point.parent is not None:
            path.append(current_point)
            current_point = current_point.parent
        return path

positivo1 = Point(0, 2)
positivo2 = Point(1, 3)
positivo3 = Point(3, 3)

comenzar_teorema = Aplicar_teorema(5, 4, mat)
ejecutar = comenzar_teorema.ejecutar_bfs()
path = comenzar_teorema.get_path(ejecutar)
mostrar_matriz = comenzar_teorema.overlay_points_on_map(path)

print(mat)