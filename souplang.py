from abc import ABC, abstractmethod

class SoupConfiguration(ABC):
    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __eq__(self, other: object):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Piece:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def execute(self, config):
        return [self.action(config)]

# class SoupSpec:
    # def __init__(self, conf):
    #     self.initial = conf
    #     self.pieces = []