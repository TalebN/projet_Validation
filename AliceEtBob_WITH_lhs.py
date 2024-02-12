def func2(x, op):
    alice_state_var = "state_Alice"
    bob_state_var = "state_Bob"
    alice_flag_var = "flag_Alice"
    bob_flag_var = "flag_Bob"
    turn_var = "turn"

    if op == 0:  # ALICE
        if getattr(x, alice_state_var) == 0:
            setattr(x, alice_flag_var, 1)
            setattr(x, turn_var, 1)
        setattr(x, alice_state_var, (getattr(x, alice_state_var) + 1) % 3)
        if getattr(x, alice_state_var) == 0:
            setattr(x, alice_flag_var, 0)
        return x
    else:  # BOB
        if getattr(x, bob_state_var) == 0:
            setattr(x, bob_flag_var, 1)
            setattr(x, turn_var, 0)
        setattr(x, bob_state_var, (getattr(x, bob_state_var) + 1) % 3)
        if getattr(x, bob_state_var) == 0:
            setattr(x, bob_flag_var, 0)
        return x
class PropBucchi:
    def __init__(self):
        self.state_variable = 0

    def __str__(self):
        return "bucchi state: " + str(self.state_variable)


def buchi_action(x):
    state_var = "state_variable"
    if getattr(x, state_var) == 1:
        setattr(x, state_var, 0)
    return x
