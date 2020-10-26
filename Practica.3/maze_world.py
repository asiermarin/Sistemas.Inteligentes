import copy
import math


# Esta clase es empleada para definir la idea de cada casilla en el laberinto.
class Point:
    def __init__(self, x=0, y=0):
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


# Estas constantes son usadas como puntos de referencia en el laberinto.
NORTH = Point(0, 1)
SOUTH = Point(0, -1)
EAST = Point(1, 0)
WEST = Point(-1, 0)


# La clase MazeWorld incluye la mecánica del laberinto
class MazeWorld:

    WALL = '#'
    EMPTY = '_'
    GOAL = '*'

    # Inicializamos el mapa del laberinto ; * objetivo, 0 punto vacío inexplorado, y # pared

    def __init__(self, maze_size_x=5, maze_size_y=5):
        self.maze_size_x = maze_size_x
        self.maze_size_y = maze_size_y
        self.maze = ['*0000',
                     '0###0',
                     '0#0#0',
                     '0#000',
                     '00000']

    def get_current_point_value(self, current_point):
        return self.maze[current_point.x][current_point.y]

    # Devuelve todos los vecinos válidos alrredeods de un punto.
    def get_neighbors(self, current_point):
        neighbors = []
        # potential_neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        potential_neighbors = [[NORTH.x, NORTH.y], [SOUTH.x, SOUTH.y], [EAST.x, EAST.y], [WEST.x, WEST.y]]
        for neighbor in potential_neighbors:
            target_point = Point(current_point.x + neighbor[0], current_point.y + neighbor[1])
            if 0 <= target_point.x < self.maze_size_x and 0 <= target_point.y < self.maze_size_y:
                if self.get_current_point_value(target_point) != '#':
                    neighbors.append(target_point)
        return neighbors

    # Una función que mestra visualmente el conjutno de casillas visitadas en el laberinto
    def overlay_points_on_map(self, points):
        overlay_map = copy.deepcopy(self.maze)
        for point in points:
            new_row = overlay_map[point.x][:point.y] + '@' + overlay_map[point.x][point.y + 1:]
            overlay_map[point.x] = new_row

        result = ''
        for x in range(0, self.maze_size_x):
            for y in range(0, self.maze_size_y):
                result += overlay_map[x][y]
            result += '\n'
        print(result)

        return overlay_map

    def print_maze(self):
        result = ''
        for x in range(0, self.maze_size_x):
            for y in range(0, self.maze_size_y):
                result += self.maze[x][y]
            result += '\n'
        print(result)


# Utilidad para obtener la ruta como una lista de puntos atravesando los padres de los nodos hasta que la raíz es alcanzada.
def get_path(point):
    path = []
    current_point = point
    while current_point.parent is not None:
        path.append(current_point)
        current_point = current_point.parent
    return path


# Utilidad para encontrar la longitud de una ruta dado un punto.
def get_path_length(point):
    path = []
    current_point = point
    total_length = 0
    while current_point.parent is not None:
        path.append(current_point)
        total_length += 1
        current_point = current_point.parent
    return total_length


# Utilidad para calcular el coste de una ruta.
def get_path_cost(point):
    path = []
    current_point = point
    total_cost = 0
    while current_point.parent is not None:
        path.append(current_point)
        total_cost += get_cost(get_direction(current_point.parent, current_point))
        current_point = current_point.parent
    return total_cost


# Utilidad para calcular el coste de un movimiento.
def get_move_cost(origin, target):
    return get_cost(get_direction(origin, target))


# Utilidad para determinar el movimento dado un origen y un punto objetivo.
def get_direction(origin, target):
    if target.x == origin.x and target.y == origin.y - 1:
        return 'N'
    elif target.x == origin.x and target.y == origin.y + 1:
        return 'S'
    elif target.x == origin.x + 1 and target.y == origin.y:
        return 'E'
    elif target.x == origin.x - 1 and target.y == origin.y:
        return 'W'


# Utilidad para determinar el coste de un movimiento dada una dirección. En este caso Norte y Sur es 5, y Este y Oeste 1.
STANDARD_COST = 1
GRAVITY_COST = 5


def get_cost(direction):
    if direction == 'N' or direction == 'S':
        return GRAVITY_COST
    return STANDARD_COST
