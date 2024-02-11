import copy

from BFS import bfs_search
from souplanguage import SoupConfiguration

from HanoiConfig import isFinal
from ParentTracer import ParentTraceur
from Semantics2RG import Semantics2RG
from souplanguage import Piece, SoupSpecification, SoupSemantics


class HanoiConfigSoup(SoupConfiguration):
    def __init__(self, n):
        self.towers = [list(range(n, 0, -1)), list(), list()]

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.towers == other.towers

    def __str__(self):
        return "numtowers " + str(self.towers)


    def can_move(self, source, destination):
        source_tower, destination_tower = self.towers[source], self.towers[destination]

        return bool(source_tower) and (not destination_tower or source_tower[-1] < destination_tower[-1])

    def move_disk(self, src, dest):
        if self.can_move(src, dest):
            self.towers[dest].append(self.towers[src].pop())
        return self

    def isFinal(self):
        return len(self.towers[0]) == 0 and len(self.towers[1]) == 0 and all(
            self.towers[2][i] > self.towers[2][i + 1] for i in range(len(self.towers[2]) - 1)
        )
def make_move(config, source, destination):
    return config.move_disk(source, destination)

def is_valid_move(config, source, destination):
    return source != destination and config.can_move(source, destination)


# Gardes
gardes = [(lambda x, i=i, j=j: is_valid_move(x, i, j)) for i in range(3) for j in range(3) if i != j]

# Actions
actions = [(lambda x, i=i, j=j: make_move(x, i, j)) for i in range(3) for j in range(3) if i != j]

# Initials
initials = [HanoiConfigSoup(3)]

# Liste Lp
Lp = [Piece("next: ", gardes[k], actions[k]) for k in range(len(actions))]

soup=SoupSpecification(initials,Lp)
soupSem=SoupSemantics(soup)
s=Semantics2RG(soupSem)
pr=ParentTraceur(s)
result, visited_nodes =bfs_search(pr,lambda n:isFinal(n))
print("\nNodes visited:")
for node in visited_nodes:
    print(node.towers)

if result is not None:
    print("Result found:", result.towers)
else:
    print("Result not found.")
print("//////////////////////////////////////////////////////////////////////////////////////////////////")
