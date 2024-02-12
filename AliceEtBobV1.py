from BFS import bfs_search

from Semantics import SemanticRelation


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

        # Alice
        if confAlice == "Home_Alice":
            actions.append(lambda state: [("Wait_Alice", state[1])])
        elif confAlice == "Wait_Alice" and confBob != "SC_Bob":
            actions.append(lambda state: [("SC_Alice", state[1])])
        elif confAlice == "SC_Alice":
            actions.append(lambda state: [("Home_Alice", state[1])])

        # Bob
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
