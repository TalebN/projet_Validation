from BFS import bfs_search
from RootedGraph import RootedGraph

#L'intégration d'un graphe basé sur un dictionnaire.
class DictRootedGraph(RootedGraph):
    def __init__(self):
        self.graph = dict()
        self.roots = []

    def getRoots(self):
        return self.roots

    def getNeighbors(self, node):
        return self.graph.get(node,[])

    def add_new_one(self, u, v):
        self.graph.setdefault(u, []).append(v)  # Ajoute une arête entre u et v dans le graphe
        # Vérifie si u n'existe pas, on l'initialise avec une liste vide avant d'ajouter v

    def __eq__(self, other):
        is_same_type = type(other) is DictRootedGraph  # Vérifie si other est une instance du DictRootedGraph
        same_graph = self.graph == other.graph
        same_roots = self.roots == other.roots
        return is_same_type and same_graph and same_roots  # Renvoie True si other est du même type et les attributs graph et roots sont égaux

    def __hash__(self):
        return 1


if __name__ == '__main__':
    print("#################################### Test le class DictRootedGraph ################################")
    g = DictRootedGraph()
    g.add_new_one(1, 2)
    g.add_new_one(1, 3)
    g.add_new_one(1, 4)
    g.add_new_one(2, 5)
    g.add_new_one(2, 6)
    g.add_new_one(2, 7)
    g.add_new_one(3, 8)
    print("Les neighbors du 1:", g.getNeighbors(1))

    # Set roots as a list containing the single root node 0
    g.roots = [1]
    print("Le Root:", g.getRoots())
    r, k = bfs_search(g, lambda n: n > 7)
    print("Result du test:", r)
    print("//////////////////////////////////////////////////////////////////////////////////////////////////")