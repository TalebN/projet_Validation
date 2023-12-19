from collections import deque
from RootedGraph import RootedGraph
from HanoiConfig import HanoiConfig, isFinal
from ParentTracer import ParentTraceur
from BFS import bfs_search

# Implémentation du graphe avec des nœuds représentant des configurations de Hanoi
class HanoiRG(RootedGraph):
    def __init__(self):
        self.graph = dict()  # Dictionnaire pour stocker les voisins de chaque nœud
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

def main():
    #graph = HanoiRG()
    #result, visited_nodes = bfs_search(graph,isFinal, inTrace=True)
    #print("\nNodes visited:")

    #for node in visited_nodes:
       # print(node.towers)

    #if result is not None:
     #   print("Result found:", result.towers)
    #else:
     #   print("Result not found.")






   graph = HanoiRG()  # Créer un graphe de tours de Hanoi
   parentracer = ParentTraceur(graph)  # Créer un traceur de parents
   result, visited_nodes = bfs_search(parentracer, isFinal)
   print("\nNodes visited:")
   for node in visited_nodes:
    print(node.towers)

   if result is not None:
    print("Result found:", result.towers)
   else:
    print("Result not found.")


# Fonction principale qui affiche la trace.
if __name__ == "__main__":
    main()
