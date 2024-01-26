from BFS import bfs_search
from ParentTracer import ParentTraceur
from Semantics2RG import Semantics2RG
from souplanguage import SoupConfiguration, SoupSemantics, SoupSpecification
import random
class AliceBobConf(SoupConfiguration):
    def __init__(self):
        super().__init__()
        self.state_Alice = 0
        self.state_Bob = 0

    def __hash__(self):
        return hash((self.state_Alice, self.state_Bob))

    def __eq__(self, other):
        return self.state_Alice == other.state_Alice and self.state_Bob == other.state_Bob

    def __str__(self):
        return "Alice: " + str(self.state_Alice) + " Bob: " + str(self.state_Bob)

class Piece:
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action

    def enabled(self, c):
        return self.condition(c)


def p1a_a(x, op):
    if op == 0:
        x.state_Alice = (x.state_Alice + 1) % 3
    else:
        x.state_Bob = (x.state_Bob + 1) % 3
    return x

if __name__ == '__main__':
    # Fixer l'ordre des pièces pour correspondre au résultat attendu
    Lp = [
        Piece("Alice veux", lambda x: True, lambda x: p1a_a(x, 0)),
        Piece("Bob veux", lambda x: True, lambda x: p1a_a(x, 1)),
        Piece("Alice entre", lambda x: True, lambda x: p1a_a(x, 0)),
        Piece("Bob entre", lambda x: True, lambda x: p1a_a(x, 1)),
        Piece("Alice sort", lambda x: True, lambda x: p1a_a(x, 0)),
        Piece("Bob sort", lambda x: True, lambda x: p1a_a(x, 1)),
    ]


    initials = [AliceBobConf()]

    soup = SoupSpecification(initials, Lp)

    soupSem = SoupSemantics(soup)
    s = Semantics2RG(soupSem)
    pr = ParentTraceur(s)
    R = bfs_search(pr, lambda n: n.state_Bob == 2)

    print("------------")
    print("---- chemin BFS----")
    print()

    for e in R[1]:
        print(e)

    print("------------")
    print("---- Trace ----")
    print()
    pr.printParentsABSoup(R[0])






