from RootedGraph import RootedGraph

class ParentTraceur(RootedGraph):
    def __init__(self, rg):
        self.rg = rg  # Opérande représentant le graphe raciné
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

    def printParents(self, last):
        current_node = last

        # Afficher les parents de chaque nœud jusqu'à la racine
        while current_node is not None and len(self.parents[current_node]) != 0:
            print(f"{current_node.towers}: {self.parents[current_node][0].towers}")
            current_node = self.parents[current_node][0]
