# ----------------------------Import class--------------------------------------------------
import random

from AliceEtBob0 import AliceetBob
from AliceEtBobPeterson import State, action
from AliceEtBobSoup0 import AliceBobConfVersion0, funct
from AliceEtBobSoup1 import  AliceBobConfV1, funct1
from AliceEtBobV1 import AliceetBobV1
from AliceEtBobV2 import process_alicePriori__bob, reset_flag
from AliceEtBob_WITH_lhs import func2, buchi_action, PropBucchi
from BFS import bfs_search
from DetectionCycle import restate, ConfSpeci, detect_cycle
from DictRootedGraph import DictRootedGraph
from HanoiConfig import isFinal
from HanoiRG import HanoiRG
from OneBitClock import OneBitClock
from ParentTracer import ParentTraceur
from Semantics2RG import Semantics2RG
from Step import DependantSoupSemantics, StepSyncComposition
from souplanguage import Piece, SoupSpecification, SoupSemantics

# -----------------------------Test Du Class DictRootedGraaph-----------------------------
print("#################################### Test le class DictRootedGraph ################################")
g = DictRootedGraph()
g.add_new_one(1, 2)
g.add_new_one(1, 3)
g.add_new_one(1, 4)
g.add_new_one(2, 5)
g.add_new_one(2, 6)
g.add_new_one(2, 7)
g.add_new_one(3, 8)
print("Les neighbors du 1:", g.getNeighbors(1))

# Set roots as a list containing the single root node 0
g.roots = [1]
print("Le Root:",g.getRoots())
r, k = bfs_search(g, lambda n: n > 4)
print("Result du test:",r)
print("//////////////////////////////////////////////////////////////////////////////////////////////////")




print("############################################### Test du HanoiRG  ##################################")
graph = HanoiRG()  # Créer un graphe de tours de Hanoi
result, visited_nodes = bfs_search(graph, isFinal)
print("\nNodes visited:")
for node in visited_nodes:
    print(node.towers)

if result is not None:
    print("Result found:", result.towers)
else:
    print("Result not found.")
print("//////////////////////////////////////////////////////////////////////////////////////////////////")



print("############################################### Test du ParentTracer ##################################")
graph = HanoiRG()  # Créer un graphe de tours de Hanoi
parentracer = ParentTraceur(graph)  # Créer un traceur de parents
result, visited_nodes = bfs_search(parentracer, isFinal)
print("\nNodes visited:")
for node in visited_nodes:
    print(node.towers)

if result is not None:
    print("Result found:", result.towers)
    parentracer.get_trace(result)  # Appeler la méthode get_trace avec le résultat trouvé
else:
    print("Result not found.")
print("//////////////////////////////////////////////////////////////////////////////////////////////////")



print("############################################### Test du OnebitClock ##################################")
onebit = OneBitClock()
semantics2RG = Semantics2RG(onebit)
print("Roots:",semantics2RG.getRoots())
print("Neighbors:",semantics2RG.getNeighbors(0))
print("//////////////////////////////////////////////////////////////////////////////////////////////////")



print("############################################### Test du AliceETBob Version 0 ##################################")
AliceBob = AliceetBob()
semantics2RG = Semantics2RG(AliceBob)
# print("-------------------------------")
# print(semantics2RG.getRoots())
# print("-------------------------------")
# print(semantics2RG.getNeighbors("Home_Alice"))
pr = ParentTraceur(semantics2RG)
t, k = bfs_search(pr, lambda x: x[0] == "SC_Alice" and x[1] == "SC_Bob")

print(t, k)
trace = pr.get_trace(t)
print(trace)
print("//////////////////////////////////////////////////////////////////////////////////////////////////")



print("############################################### Test du AliceETBob Version 1 ##################################")
coordinator = AliceetBobV1()
rg = Semantics2RG(coordinator)
traceur = ParentTraceur(rg)
w, k = bfs_search(traceur, lambda x: x[0] == "SC_Alice" and x[1] == "SC_Bob")
trace = traceur.get_trace(w)
print(trace)
print("//////////////////////////////////////////////////////////////////////////////////////////////////")



print("############################################### Test du AliceETBobSoup0  ##################################")
pieces = [
        Piece("Alice souahite", lambda x: True, lambda x: funct(x, 0)),
        Piece("Alice entre", lambda x: True, lambda x: funct(x, 0)),
        Piece("Alice sort", lambda x: True, lambda x: funct(x, 0)),
        Piece("Bob souahite", lambda x: True, lambda x: funct(x, 1)),
        Piece("Bob entre", lambda x: True, lambda x: funct(x, 1)),
        Piece("Bob sort", lambda x: True, lambda x: funct(x, 1)),
    ]
random.shuffle(pieces)
initials = [AliceBobConfVersion0()]

soup = SoupSpecification(initials, pieces)

soupSem = SoupSemantics(soup)
s = Semantics2RG(soupSem)
pr = ParentTraceur(s)
R = bfs_search(pr, lambda n: n.EtatBOB == 2)
print(" chemin BFS")
print()

for e in R[1]:
    print(e)
print("---- Trace ----")
print()
pr.printParentsABSoup(R[0])
print("//////////////////////////////////////////////////////////////////////////////////////////////////")







print("############################################### Test du AliceETBobSoup1 ##################################")
p1a = Piece("Alice souhaite", lambda x: x.EtatALICE == 0, lambda x: funct1(x, 0))
p2a = Piece("Alice entre", lambda x: x.flagBob == 0, lambda x: funct1(x, 0))
p3a = Piece("Alice sort", lambda x: x.EtatALICE == 2, lambda x: funct1(x, 0))
p1b = Piece("Bob souhaite", lambda x: x.EtatBOB == 0, lambda x: funct1(x, 1))
p2b = Piece("Bob entre", lambda x: x.flagAlice == 0, lambda x: funct1(x, 1))
p3b = Piece("Bob sort", lambda x: x.EtatBOB == 2, lambda x: funct1(x, 1))
Lp = [p1a, p2a, p3a, p1b, p2b, p3b]
# random.shuffle(Lp)
initials = [AliceBobConfV1()]
soup = SoupSpecification(initials, Lp)
soupSem = SoupSemantics(soup)
s = Semantics2RG(soupSem)
pr = ParentTraceur(s)
R = bfs_search(pr, lambda n: not (s.getNeighbors(n)))
print("chemin BFS")
print()
for e in R[1]:
    print(e)
print("---- Trace ----")
print()
pr.printParentsABSoup(R[0])
print("//////////////////////////////////////////////////////////////////////////////////////////////////")




print("############################################### Test du AliceETBobPeterson ##################################")
pieces = [
    Piece("Alice souahite", lambda x: x.Alice_state == 0, lambda x: action(x, 0)),
    Piece("Alice entre", lambda x: x.Bob_flag == 0 or x.turn == 0, lambda x: action(x,0)),
    Piece("Alice sort", lambda x: x.Alice_state == 2, lambda x: action(x, 0)),
    Piece("Bob souahite", lambda x: x.Bob_state == 0, lambda x: action(x, 1)),
    Piece("Bob entre", lambda x: x.Alice_flag == 0 or x.turn == 1, lambda x: action(x, 1)),
    Piece("Bob sort", lambda x: x.Bob_state == 2, lambda x: action(x, 1))
]

random.shuffle(pieces)
initial_state = State()
initial_spec = SoupSpecification([initial_state], pieces)
semantics = SoupSemantics(initial_spec)
rg = Semantics2RG(semantics)
parent_tracer = ParentTraceur(rg)
result = bfs_search(parent_tracer, lambda n: not (rg.getNeighbors(n)))


print("BFS Path ")
print()

for e in result[1]:
    print(e)
print("//////////////////////////////////////////////////////////////////////////////////////////////////")




print("############################################### Test du AliceETBobVersion2 ##################################")
pieces = [
    Piece("Alice souhait", lambda x: x.EtatALICE == 0, lambda x: process_alicePriori__bob(x, 0)),
    Piece("Alice entre", lambda x: x.flagBob == 0, lambda x: process_alicePriori__bob(x, 0)),
    Piece("Alice sort", lambda x: x.EtatALICE == 2, lambda x: process_alicePriori__bob(x, 0)),
    Piece("Bob souhait", lambda x: x.EtatBOB == 0, lambda x: process_alicePriori__bob(x, 1)),
    Piece("Bob entre", lambda x: x.flagAlice == 0, lambda x: process_alicePriori__bob(x, 1)),
    Piece("Bob sort", lambda x: x.EtatBOB == 2, lambda x: process_alicePriori__bob(x, 1)),
    Piece("Bob descend flag", lambda x: x.flagAlice == 1 and x.flagBob == 1, lambda x: reset_flag(x))
]

random.shuffle(pieces)

initials = [AliceBobConfV1()]
soup_specification = SoupSpecification(initials, pieces)
soup_semantics = SoupSemantics(soup_specification)
semantics_rg = Semantics2RG(soup_semantics)
parent_tracer = ParentTraceur(semantics_rg)
result = bfs_search(parent_tracer, lambda n: not (semantics_rg.getNeighbors(n)))


print("Chemin BFS ")
print()

for element in result[1]:
    print(element)
print("//////////////////////////////////////////////////////////////////////////////////////////////////")



print("############################################### Test du Detection #################################")
pieces = [
    Piece("mvt", lambda x: x.state == 0, lambda x: restate(x, 1)),
    Piece("mvt", lambda x: x.state == 1, lambda x: restate(x, 2)),
    Piece("mvt", lambda x: x.state == 2, lambda x: restate(x, 0)),
    Piece("mvt", lambda x: x.state == 2, lambda x: restate(x, 2))
]

initials = ConfSpeci()
soup_spec = SoupSpecification([initials], pieces)
soup_semantics = SoupSemantics(soup_spec)
semantic_rg = Semantics2RG(soup_semantics)
parent_traceur = ParentTraceur(semantic_rg)

resultat = bfs_search(parent_traceur, lambda n: n in parent_traceur.getNeighbors(n))

print(resultat[0])

# Pour détecter un cycle :
detect_cycle(parent_traceur)

resultat_cycle = bfs_search(parent_traceur, lambda n: n in bfs_search(parent_traceur, lambda n: n)[1])



print("//////////////////////////////////////////////////////////////////////////////////////////////////")



print("############################################### Test du AliceETBobPeterson avec LHS ##################################")
pieces = [
    Piece("Alice souhait", lambda x: x.state_Alice == 0, lambda x: func2(x, 0)),
    Piece("Alice entre", lambda x: x.flag_Bob == 0 or x.turn == 0, lambda x: func2(x, 0)),
    Piece("Alice sort", lambda x: x.state_Alice == 2, lambda x: func2(x, 0)),
    Piece("Bob souhait", lambda x: x.state_Bob == 0, lambda x: func2(x, 1)),
    Piece("Bob entre", lambda x: x.flag_Alice == 0 or x.turn == 1, lambda x: func2(x, 1)),
    Piece("Bob sort", lambda x: x.state_Bob == 2, lambda x: func2(x, 1))
]

random.shuffle(pieces)

initials1 = [State()]

pieces1 = [
    Piece("bucchi piece", lambda y, x: not(y[2].state_Alice == 2 or y[2].state_Bob == 2), lambda y, x: buchi_action(x)),
    Piece("bucchi piece", lambda y, x: not(y[2].state_Alice == 2 or y[2].state_Bob == 2), lambda y, x: x),
    Piece("bucchi piece", lambda y, x: (y[2].state_Alice == 2 or y[2].state_Bob == 2), lambda y, x: x)
]

initials2 = [PropBucchi()]

lhsspe = SoupSpecification(initials1, pieces)
lhs = SoupSemantics(lhsspe)
rhs_soup = SoupSpecification(initials2, pieces1)
rhs = DependantSoupSemantics(rhs_soup)
dss = StepSyncComposition(lhs, rhs)
s = Semantics2RG(dss)
pr = ParentTraceur(s)
R = bfs_search(pr, lambda n: n[1].state == 1)
print("//////////////////////////////////////////////////////////////////////////////////////////////////")
