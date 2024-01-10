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
        if conf == "Home_Alice":
            actions.append(lambda x: ["Wait_Alice"])
        elif conf == "Wait_Alice":
            actions.append(lambda x: ["SC_Alice"])
        elif conf == "Home_Bob":
            actions.append(lambda x: ["Wait_Bob"])
        elif conf == "Wait_Bob":
            actions.append(lambda x: ["SC_Bob"])

        return actions

    def execute(self, action, conf):
        return action(conf)
