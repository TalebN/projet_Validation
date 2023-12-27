from Semantics import SemanticRelation


class OneBitClock(SemanticRelation):
    def __init__(self):
        super().__init__()  # Appel du constructeur de la classe de base

    def initial(self):
        return [0]

    def actions(self, conf):
        actions = []
        if conf == 1:
            actions.append(lambda _: [0])  # Utilisation de _ comme argument non utilisé
        elif conf == 0:
            actions.append(lambda _: [1])
        return actions

    def execute(self, action, conf):
        return action(conf)
