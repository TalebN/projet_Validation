from abc import ABC,abstractmethod


class RootedGraph(ABC):

    @abstractmethod
    def getRoots(self):
        pass  # Méthode pour retourner une liste des racines noeuds du graph.

    @abstractmethod
    def getNeighbors(self, node):
        pass  # Méthode pour obtenir une liste des noeuds voisins d'une noeud spécifiée

