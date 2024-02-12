from BFS import bfs_search
from souplanguage import SoupConfiguration


class ConfSpeci(SoupConfiguration):
    def __init__(self):
        self.state = 0

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __str__(self):
        return "Etat" + str(self.state)


def restate(d, v):
    d.state = v
    return d


def detect_cycle(graph):
    cycle_elements = []
    result = bfs_search(graph, lambda node: node in graph.getNeighbors(node))
    while result[0] is not None:
        cycle_elements.append(result[0])
        result = bfs_search(graph, lambda node: node in graph.getNeighbors(node) and node not in cycle_elements)

    for element in cycle_elements:
        print(element)
