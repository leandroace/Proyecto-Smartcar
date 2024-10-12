
import time
from .SmartCar import SmartCar

def GreedySearch(world):
    root = SmartCar(world, None, None, 0, 0, None)
    tree = []
    tree.append(root)
    explored = set()
    tree_nodes = 1
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        tree.sort(key=lambda x: x.heuristic())
        current = tree.pop(0)
        expanded_nodes += 1
        if current.is_at_destination():
            compute_time = time.time() - start_time
            solution = current.solution()
            return solution, tree_nodes, expanded_nodes, current.depth, compute_time, current.cost
        else:
            for next_node in current.expand('greedy'):
                if next_node not in explored:
                    tree_nodes += 1
                    tree.append(next_node)
                    explored.add(next_node)

def AStarSearch(world):
    root = SmartCar(world, None, None, 0, 0, None)
    tree = []
    tree.append(root)
    explored = set()
    tree_nodes = 1
    expanded_nodes = 0
    start_time = time.time()
    while tree:
        tree.sort(key=lambda x: x.heuristic() + x.cost)
        current = tree.pop(0)
        expanded_nodes += 1
        if current.is_at_destination():
            compute_time = time.time() - start_time
            return current.solution(), tree_nodes, expanded_nodes, current.depth, compute_time, current.cost
        else:
            for next_node in current.expand('a_star'):
                if next_node not in explored:
                    tree_nodes += 1
                    tree.append(next_node)
                    explored.add(next_node)
