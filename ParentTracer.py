from RootedGraph import RootedGraph


class ParentTraceur(RootedGraph):
    def __init__(self, rg):
        self.rg = rg  # Operand representation le graphe racine.
        self.parents = {}  # Dictionnaire pour stocker les parents de chaque nœud

    def getRoots(self):
        roots = self.rg.getRoots()  # Obtenir les racines du graphe

        # Initialiser les entrées du dictionnaire 'parents' pour chaque racine
        root_index = 0
        while root_index < len(roots):
            root_node = roots[root_index]
            self.parents[root_node] = []
            root_index += 1
        return roots

    def getNeighbors(self, node):
        neighbors = self.rg.getNeighbors(node)  # Obtenir les voisins d'un nœud

        # Mettre à jour les parents des voisins dans le dictionnaire 'parents'
        neighbor_index = 0
        while neighbor_index < len(neighbors):
            neighbor_node = neighbors[neighbor_index]
            if self.parents.get(neighbor_node) is None:
                self.parents[neighbor_node] = [node]
            neighbor_index += 1
        return neighbors

    def get_trace(self, last):
            print("Trace:\n")
            lap = last
            value = self.parents[last]
            while value is not None and len(value) !=0:
                if isinstance(lap, str):
                    print(f"{lap}: {value[0]}")
                else:
                    print(f"{lap.towers}: {value[0].towers}")

                lap = value[0]
                value = self.parents[lap]


