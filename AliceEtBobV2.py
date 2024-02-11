import random
from AliceEtBobSoup1 import AliceBobConfV1
from ParentTracer import ParentTraceur
from Semantics2RG import Semantics2RG
from souplanguage import Piece, SoupSpecification, SoupSemantics
from BFS import bfs_search

def process_alicePriori__bob(x, operator):
    if operator == 0:  # ALICE
        if x.EtatALICE == 0:
            x.flagAlice = 1
        x.EtatALICE = (x.EtatALICE + 1) % 3
        if x.EtatALICE == 0:
            x.flagAlice = 0
    else:  # BOB
        if x.EtatBOB == 0:
            x.flagBob = 1
        x.EtatBOB = (x.EtatBOB + 1) % 3
        if x.EtatBOB == 0:
            x.flagBob = 0
    return x

def reset_flag(x):
    x.flagBob = 0
    x.EtatBOB = 1
    return x



