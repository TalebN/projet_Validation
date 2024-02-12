import unittest
from AliceEtBobV1 import AliceetBobV1


class TestAliceetBobV1(unittest.TestCase):
    def setUp(self):
        self.model = AliceetBobV1()

    def test_initial_state(self):
        expected_initial_state = [("Home_Alice", "Home_Bob")]
        self.assertEqual(self.model.initial(), expected_initial_state)

    def test_actions_from_initial_state(self):
        initial_state = self.model.initial()[0]
        actions = self.model.actions(initial_state)
        self.assertTrue(len(actions) > 0)

    def test_action_execution(self):
        initial_state = self.model.initial()[0]
        actions = self.model.actions(initial_state)
        for action in actions:
            new_state = self.model.execute(action, initial_state)
            self.assertIsNotNone(new_state)

    #  tests pour les transitions connues
    def test_transition_to_wait_alice_from_home(self):
        initial_state = ("Home_Alice", "Home_Bob")
        actions = self.model.actions(initial_state)
        for action in actions:
            new_state = action(initial_state)
            if new_state[0][0] == "Wait_Alice":
                self.assertEqual(new_state, [("Wait_Alice", "Home_Bob")])

    def test_transition_to_sc_alice_when_bob_not_sc(self):
        state = ("Wait_Alice", "Home_Bob")
        actions = self.model.actions(state)
        for action in actions:
            new_state = action(state)
            if new_state[0][0] == "SC_Alice":
                self.assertEqual(new_state, [("SC_Alice", "Home_Bob")])

    def test_transition_to_home_alice_from_sc(self):
        state = ("SC_Alice", "Wait_Bob")
        actions = self.model.actions(state)
        for action in actions:
            new_state = action(state)
            if new_state[0][0] == "Home_Alice":
                self.assertEqual(new_state, [("Home_Alice", "Wait_Bob")])


if __name__ == '__main__':
    unittest.main()