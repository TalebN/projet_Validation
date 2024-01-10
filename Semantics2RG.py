from RootedGraph import RootedGraph


class Semantics2RG(RootedGraph):
    def __init__(self, sem):
        self.sem=sem

    def getRoots(self):
        roots = self.sem.initial()
        return roots

    def getNeighbors(self, n):
        actions = self.sem.actions(n)
        neighbors = []
        for act in actions:
            targets = self.sem.execute(act, n)
            neighbors.extend(targets)
        return neighbors
