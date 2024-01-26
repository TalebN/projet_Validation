import random

from BFS import bfs_search
from ParentTracer import ParentTraceur
from Semantics2RG import Semantics2RG
from souplanguage import SoupConfiguration, Piece, SoupSemantics, SoupSpecification


class AliceBobConfV1(SoupConfiguration):
    def __init__(self):
        self.state_Alice = 0   #0,1,2
        self.state_Bob = 0
        self.flag_Alice = 0
        self.flag_Bob = 0

    def __hash__(self):
        return hash(self.state_Alice + self.state_Bob+ self.flag_Alice +self.flag_Bob )

    def __eq__(self, other):
        return self.state_Alice == other.state_Alice and self.state_Bob == other.state_Bob and self.flag_Alice == other.flag_Alice and self.flag_Bob == other.flag_Bob

    def __str__(self):
        return "Alice: "+str(self.state_Alice)+" flag alice: "+str(self.flag_Alice) +" Bob: "+ str(self.state_Bob)+" flag Bob: "+str(self.flag_Bob)

def p1a_a(x, op):
        if op == 0:  # for alice
            if x.state_Alice == 0:
                x.flag_Alice = 1
            x.state_Alice = (x.state_Alice + 1) % 3
            if x.state_Alice == 0:
                x.flag_Alice = 0
            return x
        else:  # for bob
            if x.state_Bob == 0:
                x.flag_Bob = 1
            x.state_Bob = (x.state_Bob + 1) % 3
            if x.state_Bob == 0:
                x.flag_Bob = 0
            return x
if __name__ == '__main__':
    p1a = Piece("Alice veux", lambda x: x.state_Alice == 0, lambda x: p1a_a(x, 0))
    p2a = Piece("Alice entre", lambda x: x.flag_Bob == 0, lambda x: p1a_a(x, 0))
    p3a = Piece("Alice sort", lambda x: x.state_Alice == 2, lambda x: p1a_a(x, 0))
    p1b = Piece("Bob veux", lambda x: x.state_Bob == 0, lambda x: p1a_a(x, 1))
    p2b = Piece("Bob entre", lambda x: x.flag_Alice == 0, lambda x: p1a_a(x, 1))
    p3b = Piece("Bob sort", lambda x: x.state_Bob == 2, lambda x: p1a_a(x, 1))
    Lp = [p1a, p2a, p3a, p1b, p2b, p3b]
   # random.shuffle(Lp)

    initials = [AliceBobConfV1()]
    soup = SoupSpecification(initials, Lp)
    soupSem = SoupSemantics(soup)
    s = Semantics2RG(soupSem)
    pr = ParentTraceur(s)
    R = bfs_search(pr, lambda n: not (s.getNeighbors(n)))

    print("------------")
    print("---- chemin BFS----")
    print()

    for e in R[1]:
        print(e)

    print("------------")
    print("---- Trace ----")
    print()

    pr.printParentsABSoup(R[0])








