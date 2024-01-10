from BFS import bfs_search
from ParentTracer import ParentTraceur
from Semantics import SemanticRelation
from Semantics2RG import Semantics2RG


class AliceetBobV1(SemanticRelation):
    def __init__(self):
        self.flage_Alice = 0
        self.flage_Bob = 0

    def initial(self):
        return [("Home_Alice", "Home_Bob")]

    def actions(self, conf):
        actions = []
        if conf == "Home_Alice":
            actions.append(lambda x: ["Wait_Alice"])
            self.flage_Alice = 1
        elif self.flage_Bob == 0 and conf == "Wait_Alice":
            actions.append(lambda x: ["SC_Alice"])
        elif conf == "SC_Alice":
            actions.append(lambda x: ["Home_Alice"])
            self.flage_Alice = 0

        elif conf == "Home_Bob":
            actions.append(lambda x: ["Wait_Bob"])
            self.flage_Bob = 1
        elif self.flage_Alice == 0 and conf == "Wait_Bob":
            actions.append(lambda x: ["SC_Bob"])
        elif conf == "SC_Bob":
            actions.append(lambda x: ["Home_Bob"])
            self.flage_Bob = 0

        return actions

    def execute(self, action, conf):
        return action(conf)
