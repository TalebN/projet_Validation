from Semantics import SemanticRelation
from Semantics2RG import Semantics2RG


class OneBitClock(SemanticRelation):
    def initial(self):
        return [0]

    def actions(self, conf):
        actions = []
        if conf == 1:
            actions.append(lambda x: [0])
        elif conf == 0:
            actions.append(lambda x: [1])
        return actions

    def execute(self, action, conf):
        return action(conf)


def main():
    onebit=OneBitClock()
    semantics2RG=Semantics2RG(onebit)
    print("------------------Roots-------------")
    print(semantics2RG.getRoots())
    print("------------------Neighbors-------------")
    print(semantics2RG.getNeighbors(0))


if __name__ == "__main__":
    main()