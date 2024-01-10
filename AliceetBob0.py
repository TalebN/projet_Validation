from BFS import bfs_search
from ParentTracer import ParentTraceur
from Semantics import SemanticRelation
from Semantics2RG import Semantics2RG


class AliceetBob(SemanticRelation):
    def __init__(self):
        # Call the __init__ method of the base class
        super().__init__()

    def initial(self):
        return [("Home_Alice", "Home_Bob")]

    def actions(self, conf):
        actions = []

        confAlice, confBob = conf

        if confAlice == "Home_Alice":
            actions.append(lambda x: [("Wait_Alice", confBob)])
        if confAlice == "Wait_Alice":
            actions.append(lambda x: [("SC_Alice", confBob)])
        if confAlice == "SC_Alice":
            actions.append(lambda x: [("Home_Alice", confBob)])
        if confBob == "Home_Bob":
            actions.append(lambda x: [(confAlice, "Wait_Bob")])
        if confBob == "Wait_Bob":
            actions.append(lambda x: [(confAlice, "SC_Bob")])
        if confBob == "SC_Bob":
            actions.append(lambda x: [(confAlice, "Home_Bob")])
        return actions

    def execute(self, action, conf):
        return action(conf)


if __name__ == "__main__":
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
