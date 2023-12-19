from RootedGraph import RootedGraph



class DictRootedGraph(RootedGraph):
    def __init__(self):
        super().__init__()  # Appeler le constructeur de la classe de base en utilisant super.

    def getRoots(self):
        return super().getRoots()  # Appeler la même méthode roots de la classe de base et renvoyer le résultat

    def getNeighbors(self, node):
        return super().getNeighbors(node)  # Appeler la même méthode neighbors de la classe de base et renvoyer le résultat

    def add_new_one(self, u, v):
        self.graph.setdefault(u, []).append(v)  # Ajoute une arête entre u et v dans le graphe
                                               # Vérifie si u n'existe pas, on l'initialise avec une liste vide avant d'ajouter v

    def __eq__(self, other):
        is_same_type = type(other) is DictRootedGraph  # Vérifie si other est une instance du DictRootedGraph
        same_graph = self.graph == other.graph
        same_roots = self.getRoots() == other.getRoots()  # Appeler la méthode roots pour comparer les racines
        return is_same_type and same_graph and same_roots  # Renvoie True si other est du même type et les attributs graph et roots sont égaux

    def __hash__(self):
        return 1




