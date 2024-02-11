from collections import deque
from RootedGraph import RootedGraph
from HanoiConfig import HanoiConfig, isFinal
from ParentTracer import ParentTraceur
from BFS import bfs_search


# Implémentation du graphe avec des nœuds représentant des configurations de Hanoi
class HanoiRG(RootedGraph):
    def __init__(self):

        self.graph = dict()
        self.roots = [HanoiConfig(3)]  # Racines du graphe

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)  # Ajouter une arête entre les nœuds u et v

    def getRoots(self):
        return self.roots  # Obtenir les racines du graphe

    def getNeighbors(self, n):
        neighbors = []

        # Déplacer un disque vers une autre tour
        for source in range(3):
            for destination in range(3):
                if source != destination and n.is_valid_move(source, destination):
                    new_config = n.move_disk_and_get_next_state(source, destination)
                    neighbors.append(new_config)

        return neighbors
