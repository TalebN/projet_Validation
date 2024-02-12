

from RootedGraph import RootedGraph


class ParentTraceur(RootedGraph):
    def __init__(self, rgraph):
        self.rgraph = rgraph  # Operand representation le graphe racine.
        self.parents = {}  # Dictionnaire pour stocker les parents de chaque nœud

    def getRoots(self):
        roots = self.rgraph.getRoots()  # Obtenir les racines du graphe

        # Initialiser les entrées du dictionnaire 'parents' pour chaque racine
        root_index = 0
        for r in roots:
            self.parents[r] = []
        return roots

    def getNeighbors(self, node):
        neighbors = self.rgraph.getNeighbors(node)  # Obtenir les voisins d'un nœud

        # Mettre à jour les parents des voisins dans le dictionnaire 'parents'
        neighbor_index = 0
        while neighbor_index < len(neighbors):
            neighbor_node = neighbors[neighbor_index]
            if self.parents.get(neighbor_node) is None:
                self.parents[neighbor_node] = [node]
            neighbor_index += 1
        return neighbors

    def get_trace(self, node):
        trace = []
        current = node
        while current is not None:
            trace.append(current)
            parents = self.parents.get(current)
            if len(parents) > 0:
                current = parents[0]
            else:
                current = None
        return trace[::-1]

    def printParentsABSoup(self, last):
        print("Trace:\n")
        lap = last
        value = self.parents[last]
        while value is not None and len(value)  != 0:
            print(f"{lap}: {value[0]}")
            lap = value[0]
            value = self.parents[lap]

