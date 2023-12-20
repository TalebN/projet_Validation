from abc import abstractmethod


class SemanticRelation:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self,src):
        pass

    @abstractmethod
    def execute(self,actions,src):
        pass
