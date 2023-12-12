import copy


class HanoiConfiguration(list):
    def __init__(self, nbStacks, nbDisks):
        list.__init__(self, [[(nbDisks - i) for i in range(nbDisks)]] + [[] for _ in range(nbStacks - 1)])

    def __hash__(self):
        return 1

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if len(self[i]) != len(other[i]):
                return False
            for j in range(len(self[i])):
                if other[i][j] != self[i][j]:
                    return False
        return True


class HanoiRG:
    def __init__(self, nbStacks, nbDisks):
        self.nbStacks = nbStacks
        self.nbDisks = nbDisks

    def root(self):
        return HanoiConfiguration(self.nbStacks, self.nbDisks)

    def neighbors(self, state):
        voisins = []
        for i in range(self.nbStacks):
            new_state = copy.deepcopy(state)
            if new_state[i]:
                disk = new_state[i].pop()
                for j in range(self.nbStacks):
                    if i != j and (not new_state[j] or new_state[j][-1] > disk):
                        temp = copy.deepcopy(new_state)
                        temp[j].append(disk)
                        voisins.append(temp)
        return voisins

    def is_final_state(self, state):
        return state[-1] == list(range(1, self.nbDisks + 1))

####   Fonction qui nous permet de visualiser le comportement de Hanoi  #####
    def print_hanoi_state(self, state):
        for i, tower in enumerate(state):
            print(f"Tour {i + 1}: {tower}")

    def print_results(self, result_states):
        print("Résultats de la recherche :")
        if not result_states:
            print("Aucun état exploré.")
        else:
            for i, state in enumerate(result_states):
                print(f"\nÉtat {i + 1}:")
                self.print_hanoi_state(state)
                print("-" * 20)
