from abc import ABC
import copy

from Semantics import SemanticRelation


class SoupConfiguration(ABC):
    def __hash__(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        pass


class Piece:  # (SoupConfiguration)
    def __init__(self, nom, garde, action):
        self.nom = nom
        self.garde = garde
        self.action = action

    def enabled(self, c):
        return self.garde(c)


class SoupSpecification:

    def __init__(self, initials, pieces):
        self.initials = initials
        self.pieces_list = pieces

    def initial(self):
        return self.initials

    def pieces(self):
        return self.pieces_list

    def enabledPieces(self, c):
        filtered_pieces = list(filter(lambda p: p.enabled(c), self.pieces_list))
        return filtered_pieces


class SoupSemantics(SemanticRelation):
    def __init__(self, spec):
        self.spec = spec

    def initial(self):
        return self.spec.initial()

    def actions(self, config):
        return self.spec.enabledPieces(config)

    def execute(self, piece, config):
        to_target = copy.deepcopy(config)
        return [piece.action(to_target)]
