from BFS import bfs_search
from ParentTracer import ParentTraceur
from Semantics import SemanticRelation
from Semantics2RG import Semantics2RG


class AliceetBobV1(SemanticRelation):
    def __init__(self):
        super().__init__()
        self.flagAlice = 0
        self.flagBob = 0

    def initial(self):
        return [("Home_Alice", "Home_Bob")]


    def actions(self, conf):
        actions = []
        confAlice, confBob = conf

        #Alice
        if confAlice == "Home_Alice":
            actions.append(lambda state: [("Wait_Alice", state[1])])
        elif confAlice == "Wait_Alice" and confBob != "SC_Bob":
            actions.append(lambda state: [("SC_Alice", state[1])])
        elif confAlice == "SC_Alice":
            actions.append(lambda state: [("Home_Alice", state[1])])

        #Bob
        if confBob == "Home_Bob":
            actions.append(lambda state: [(state[0], "Wait_Bob")])
        elif confBob == "Wait_Bob" and confAlice != "SC_Alice":
            actions.append(lambda state: [(state[0], "SC_Bob")])
        elif confBob == "Wait_Bob":
            actions.append(lambda state: [(state[0], "Home_Bob")])

        print(f"Conf: {conf}")
        return actions


    def execute(self, action, conf):
        return action(conf)


if __name__ == '__main__':
    coordinator = AliceetBobV1()
    rg = Semantics2RG(coordinator)
    traceur = ParentTraceur(rg)
    w, k = bfs_search(traceur, lambda x: x[0] == "SC_Alice" and x[1] == "SC_Bob")
    trace = traceur.get_trace(w)
    print(trace)