import maze_world as mzw 
from maze_world import Point, MazeWorld


# Function to find a route using the Depth-first Search algorithm.

# Depth-first search is an algorithm used to traverse a tree or generate nodes and paths in a tree. This algorithm
# starts at a specific node and explores paths of connected nodes of the first child and does this recursively until
# it reaches the furthest leaf node before backtracking and exploring other paths to leaf nodes via other child nodes
# that have been visited.

# Although the Depth-first search algorithm van be implemented with a recursive function. This implementation is
# achieved using a cola to better represent the order of operations as to which nodes get visited and processed.
# It is important to keep track of the visited points so that the same nodes do not get visited unnecessarily and
# create cyclic loops.
def aplicar_dfs(mzw, posicion_actual):
    # Append the current node to the stack
    puntos_visitados = []
    cola = [posicion_actual]
    # Keep searching while there are nodes in the cola
    while cola:
        # Set the next node in the cola as the current node
        proximo_punto = cola.pop()
        # If the current node hasn't already been exploited, search it
        if not is_in_puntos_visitados(proximo_punto, puntos_visitados):
            puntos_visitados.append(proximo_punto)
            # Return the path to the current punto_alrededor if it is the goal
            if mzw.get_current_point_value(proximo_punto) == '*':
                return proximo_punto
            else:
                # Add the current node's puntos_alrededores� to the cola
                puntos_alrededores = mzw.get_path(proximo_punto)
                for punto_alrededor in puntos_alrededores:
                    punto_alrededor.set_parent(proximo_punto)
                    cola.append(punto_alrededor)
    return 'Direccion no encontrada'


# Function to determine if the point has already been visited
def is_in_puntos_visitados(posicion_actual, puntos_visitados):
    for punto_visitado in puntos_visitados:
        if posicion_actual.x == punto_visitado.x and posicion_actual.y == punto_visitado.y:
            return True
    return False


print('---Depth-first Search---')

# Initialize a MazePuzzle
mzw_main = mp.MazePuzzle()

# Run the depth first search algorithm with the initialized maze
starting_point = mp.Point(2, 2)
outcome = run_dfs(mzw_main, starting_point)

# Get the path found by the depth first search algorithm
dfs_path = mp.get_path(outcome)

# Print the results of the path found
print('Path Length: ', len(dfs_path))
mzw_main.overlay_points_on_map(dfs_path)
print('Path Cost: ', mp.get_path_cost(outcome))
for point in dfs_path:
    print('Point: ', point.x, ',', point.y)