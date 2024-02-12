
from souplanguage import SoupConfiguration


class AliceBobConfV1(SoupConfiguration):
    def __init__(self):
        self.EtatALICE = 0
        self.EtatBOB = 0
        self.flagAlice = 0
        self.flagBob = 0

    def __hash__(self):
        return hash(self.EtatALICE + self.EtatBOB + self.flagAlice + self.flagBob)

    def __eq__(self, other):
        return self.EtatALICE == other.EtatALICE and self.EtatBOB == other.EtatBOB and self.flagAlice == other.flagAlice and self.flagBob == other.flagBob

    def __str__(self):
        return "Alice: " + str(self.EtatALICE) + " flag alice: " + str(self.flagAlice) + " Bob: " + str(
            self.EtatBOB) + " flag Bob: " + str(self.flagBob)


def funct1(x, op):
    if op == 0:  # for alice
        if x.EtatALICE == 0:
            x.flagAlice = 1
        x.EtatALICE = (x.EtatALICE + 1) % 3
        if x.EtatALICE == 0:
            x.flagAlice = 0
        return x
    else:  # for bob
        if x.EtatBOB == 0:
            x.flagBob = 1
        x.EtatBOB = (x.EtatBOB + 1) % 3
        if x.EtatBOB == 0:
            x.flagBob = 0
        return x


