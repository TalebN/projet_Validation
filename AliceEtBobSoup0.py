from BFS import bfs_search
from ParentTracer import ParentTraceur
from Semantics2RG import Semantics2RG
from souplanguage import SoupConfiguration, SoupSemantics, SoupSpecification
import random


class AliceBobConfVersion0(SoupConfiguration):
    def __init__(self):

        self.EtatALICE = 0
        self.EtatBOB = 0

    def __hash__(self):
        return hash((self.EtatALICE + self.EtatBOB))

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
        return x
    else:
        x.EtatBOB = (x.EtatBOB + 1) % 3
        return x



