from abc import ABC, abstractmethod
from typing import List

from Semantics import SemanticRelation


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
    def __init__(self, name: str, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def enabled(self, config):
        return self.guard(config)

    def execute(self, config):
        return [self.action(config)]


class SoupSpec:

    def __init__(self, pieces, initials):
        self.initials = initials
        self.pieces_list = pieces  # liste de pieces

    def initial(self):  # list de SoupConfiguration
        return self.initials

    def pieces(self):  # liste de pieces  #utilisé ou?
        return []

    def enabledPieces(self, c):  # faux
        filtered_pieces = list(filter(lambda p: p.enabled(c), self.pieces))
        return filtered_pieces

    def pieces(self) -> List[Piece]:
        return []


class SoupSemantics(SemanticRelation):
    def _init_(self, spec):
        self.spec = spec

    def initial(self):
        return self.spec.initial()

    def actions(self, config):
        return self.spec.enabledPieces(config.garde)

    def execute(self, action, config):
        return action(config)
