import copy


class HanoiConfig:

    def __init__(self, n):
        tower1 = list(range(n, 0, -1))
        tower2 = list()
        tower3 = list()
        self.towers = [tower1, tower2, tower3]

    def is_valid_move(self, source_index, destination_index):
        source_tower = self.towers[source_index]
        destination_tower = self.towers[destination_index]

        if not source_tower:

            return False
        else:
            if not destination_tower or source_tower[-1] < destination_tower[-1]:

                return True
            else:
                return False

    def move_disk_and_get_next_state(self, source_index, destination_index):

        next_state = copy.deepcopy(self)
        next_state.towers[destination_index].append(next_state.towers[source_index].pop())
        return next_state

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.towers == other.towers


def is_empty_towers(towers):
    return all(len(tower) == 0 for tower in towers)


def is_sorted_descending(tower):
    return all(tower[i] > tower[i + 1] for i in range(len(tower) - 1))


def isFinal(node):
    return is_empty_towers(node.towers[:2]) and is_sorted_descending(node.towers[2])
