# ----------------------------Import class--------------------------------------------------
from AliceetBob0 import AliceetBob
from BFS import bfs_search
from DictRootedGraph import DictRootedGraph
from HanoiConfig import isFinal
from HanoiRG import HanoiRG
from OneBitClock import OneBitClock
from ParentTracer import ParentTraceur
from Semantics2RG import Semantics2RG

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
t, k = bfs_search(pr, lambda x: "Wait_Bob" in x)
print(t, k)
trace = pr.get_trace(t)
print("//////////////////////////////////////////////////////////////////////////////////////////////////")

