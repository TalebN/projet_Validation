
class State:
    def __init__(self, Alice_state=0, Bob_state=0, Alice_flag=0, Bob_flag=0, turn=-1):
        self.Alice_state = Alice_state
        self.Bob_state = Bob_state
        self.Alice_flag = Alice_flag
        self.Bob_flag = Bob_flag
        self.turn = turn

    def __hash__(self):
        return hash(self.Alice_state + self.Bob_state + self.Alice_flag + self.Bob_flag)

    def __eq__(self, other):
        return self.Alice_state == other.Alice_state and self.Bob_state == other.Bob_state and self.Alice_flag == other.Alice_flag and self.Bob_flag == other.Bob_flag and self.turn == other.turn

    def __str__(self):
        return f"Alice: {self.Alice_state} flag alice: {self.Alice_flag} Bob: {self.Bob_state} flag Bob: {self.Bob_flag}"

def action(state, player):
    if player == 0:
        if state.Alice_state == 0:
            state.Alice_flag = 1
            state.turn = 1
        state.Alice_state = (state.Alice_state + 1) % 3
        if state.Alice_state == 0:
            state.Alice_flag = 0
        return state
    else:
        if state.Bob_state == 0:
            state.Bob_flag = 1
            state.turn = 0
        state.Bob_state = (state.Bob_state + 1) % 3
        if state.Bob_state == 0:
            state.Bob_flag = 0
        return state




