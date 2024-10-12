
import time
from .SmartCar import SmartCar

def BreadthFirstSearch(world):
    """
    Realiza una búsqueda por amplitud en un mundo dado.

    Parámetros:
    - world: El mundo en el que se realizará la búsqueda.

    Retorna:
    - path: El camino encontrado desde el estado inicial hasta el estado objetivo.
    - tree_nodes: El número de nodos en el árbol de búsqueda.
    - expanded_nodes: El número de nodos expandidos durante la búsqueda.
    - depth: La profundidad del camino encontrado.
    - computation_time: El tiempo de computación utilizado para realizar la búsqueda.
    - cost: El costo total del camino encontrado.
    """
    root = SmartCar(world, None, None, 0, 0, None)
    tree = []
    tree.append(root)
    explored = set()
    tree_nodes = 1
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        current = tree.pop(0)
        expanded_nodes += 1
        if current.is_at_destination():
            return current.solution(), tree_nodes, expanded_nodes, current.depth, time.time() - start_time, current.cost
        else:
            for next_node in current.expand('bfs'):
                if next_node not in explored:
                    tree_nodes += 1
                    tree.append(next_node)
                    explored.add(next_node)

def UniformCostSearch(world):
    """
    Realiza una búsqueda por costo uniforme en un mundo dado.

    Parámetros:
    - world: El mundo en el que se realizará la búsqueda.

    Retorna:
    - path: El camino encontrado desde el estado inicial hasta el estado objetivo.
    - tree_nodes: El número de nodos en el árbol de búsqueda.
    - expanded_nodes: El número de nodos expandidos durante la búsqueda.
    - depth: La profundidad del camino encontrado.
    - computation_time: El tiempo de computación utilizado para realizar la búsqueda.
    - cost: El costo total del camino encontrado.
    """
    root = SmartCar(world, None, None, 0, 0, None)
    tree = []
    tree.append(root)
    explored = set()
    tree_nodes = 1
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        tree.sort(key=lambda x: x.cost)
        current = tree.pop(0)
        expanded_nodes += 1
        if current.is_at_destination():
            return current.solution(), tree_nodes, expanded_nodes, current.depth, time.time() - start_time, current.cost
        else:
            for next_node in current.expand('ucs'):
                if next_node not in explored:
                    tree_nodes += 1
                    tree.append(next_node)
                    explored.add(next_node)

def DepthFirstSearch(world):
    """
    Realiza una búsqueda en profundidad evitando ciclos en un mundo dado.

    Parámetros:
    - world: El mundo en el que se realizará la búsqueda.

    Retorna:
    - path: El camino encontrado desde el estado inicial hasta el estado objetivo.
    - tree_nodes: El número de nodos en el árbol de búsqueda.
    - expanded_nodes: El número de nodos expandidos durante la búsqueda.
    - depth: La profundidad del camino encontrado.
    - computation_time: El tiempo de computación utilizado para realizar la búsqueda.
    - cost: El costo total del camino encontrado.
    """
    root = SmartCar(world, None, None, 0, 0, None)
    tree = []
    tree.append(root)
    explored = set()
    explored_in_branch = set()
    tree_nodes = 1
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        current = tree.pop()
        expanded_nodes += 1
        explored_in_branch = set()
        if current.is_at_destination():
            return current.solution(), tree_nodes, expanded_nodes, current.depth, time.time() - start_time, current.cost
        else:
            for next_node in current.expand('dfs'):
                if next_node not in explored and next_node not in explored_in_branch:
                    tree_nodes += 1
                    tree.append(next_node)
                    explored_in_branch.add(next_node)
            explored.add(current)
