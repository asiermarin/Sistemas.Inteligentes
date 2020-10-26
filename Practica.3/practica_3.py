import maze_world as mzw 
from maze_world import Point, MazeWorld

def ejecutar_dfs(laberinto, posicion_actual, posiciones_visitadas):
    posiciones_visitadas = []
    cola = [posicion_actual]
    while cola:
        proximo_punto = cola.pop()
        if not es_visitado(proximo_punto, posiciones_visitadas):
            posiciones_visitadas.append(proximo_punto)
            if laberinto.get_current_point_value(proximo_punto) == '*':
                return proximo_punto
            else:
                puntos_alrededores = laberinto.get_neighbors(proximo_punto)
                for punto_alrededor in puntos_alrededores:
                    punto_alrededor.set_parent(proximo_punto)
                    cola.append(punto_alrededor)
    return 'No se ha encontrado ninguna soluci�n.'


def es_visitado(posicion_actual, posiciones_visitadas):
    # TODO recorremos cada elemento en la lista de posiciones_vistadas
    for posicion_visitada in posiciones_visitadas:
        # TODO Si el argumento x e y de la posici�n es el mismo que para la posicion_actual, devolvemos True
        if ((posicion_actual.x == posicion_visitada.x) and (posicion_actual.y == posicion_visitada.y)):
            return True
    # En caso contrario devolvemos False
    return False

laberinto = MazeWorld()
posicion = Point(2, 2) 
posiciones_visitadas = []
salida = ejecutar_dfs(laberinto, posicion, posiciones_visitadas)
print(salida)
path = mzw.get_path(salida)
print(path)
len(path)
x = laberinto.overlay_points_on_map(path)
camino = mzw.get_path_cost(salida)
for i in path:
    i.print()
    print(f"x: {i.x}")
    print(f"y: {i.y}")
    print("------------")