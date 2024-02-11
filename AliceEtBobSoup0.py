from BFS import bfs_search
from ParentTracer import ParentTraceur
from Semantics2RG import Semantics2RG
from souplanguage import SoupConfiguration, SoupSemantics, SoupSpecification
import random


class AliceBobConfVersion0(SoupConfiguration):
    def __init__(self):
        super().__init__()
        self.EtatALICE = 0
        self.EtatBOB = 0

    def __hash__(self):
        return hash((self.EtatALICE, self.EtatBOB))

    def __eq__(self, other):
        return self.EtatALICE == other.EtatALICE and self.EtatBOB == other.EtatBOB

    def __str__(self):
        return "Alice: " + str(self.EtatALICE) + " Bob: " + str(self.EtatBOB)


class Piece:
    def __init__(self, name, condition, action):
        self.name = name
        self.condition = condition
        self.action = action

    def enabled(self, c):
        return self.condition(c)


def p1a_a(x, op):
    if op == 0:
        x.EtatALICE = (x.EtatALICE + 1) % 3
    else:
        x.EtatBOB = (x.EtatBOB + 1) % 3
    return x


if __name__ == '__main__':

    Lp = [
        Piece("Alice souahite", lambda x: True, lambda x: p1a_a(x, 0)),
        Piece("Bob souahite", lambda x: True, lambda x: p1a_a(x, 1)),
        Piece("Alice entre", lambda x: True, lambda x: p1a_a(x, 0)),
        Piece("Bob entre", lambda x: True, lambda x: p1a_a(x, 1)),
        Piece("Alice sort", lambda x: True, lambda x: p1a_a(x, 0)),
        Piece("Bob sort", lambda x: True, lambda x: p1a_a(x, 1)),
    ]

    initials = [AliceBobConfVersion0()]

    soup = SoupSpecification(initials, Lp)

    soupSem = SoupSemantics(soup)
    s = Semantics2RG(soupSem)
    pr = ParentTraceur(s)
    R = bfs_search(pr, lambda n: n.EtatBOB == 2)

    print("------------")
    print("---- chemin BFS----")
    print()

    for e in R[1]:
        print(e)

    print("------------")
    print("---- Trace ----")
    print()
    pr.printParentsABSoup(R[0])