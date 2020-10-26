import maze_world as mzw 
from maze_world import Point, MazeWorld

def ejecutar_a_star():
    cola = [posicion_actual]
    while cola:
        proximo_punto = cola.pop()
        if laberinto.get_current_point_value(proximo_punto) == '*':
            return proximo_punto
        else:
            puntos_alrededores = laberinto.get_neighbors(proximo_punto)
            for punto_alrededor in puntos_alrededores:
                punto_alrededor.set_parent(proximo_punto)
                punto_alrededor.cost = determinar_coste(proximo_punto, punto_alrededor)
        cola.extend(puntos_alrededores)
        cola.sort(key=lambda x: x.cost, reverse=True)
    return "No hay camino"


def determinar_coste(origen, punto_objetivo):
    distancia_objetivo = mzw.get_path_length(punto_objetivo)
    coste = mzw.get_move_cost(origen, punto_objetivo)
    coste_calculado = distancia_objetivo + coste
    return coste_calculado

laberinto = MazeWorld()
posicion_actual = Point(2, 2) 
salida = ejecutar_a_star()
print(salida)
path = mzw.get_path(salida)
print(path)
tamanio = mzw.get_path_length(salida)
print(f"Tamanio: {tamanio}")
x = laberinto.overlay_points_on_map(path)
coste = mzw.get_path_cost(salida)
print(f"Coste: {coste}")
for i in path:
    i.print()
    print(f"x: {i.x}")
    print(f"y: {i.y}")
    print("------------")