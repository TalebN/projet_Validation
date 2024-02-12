import unittest
from AliceEtBobPeterson import State, action

class TestStateAndAction(unittest.TestCase):
    def setUp(self):
        self.initial_state = State()

    def test_initial_state(self):
        """teste l'état initial"""
        self.assertEqual(self.initial_state.Alice_state, 0)
        self.assertEqual(self.initial_state.Bob_state, 0)
        self.assertEqual(self.initial_state.Alice_flag, 0)
        self.assertEqual(self.initial_state.Bob_flag, 0)
        self.assertEqual(self.initial_state.turn, -1)

    def test_action_alice(self):
        """teste les actions d'Alice"""
        updated_state = action(self.initial_state, 0)
        self.assertEqual(updated_state.Alice_state, 1)
        self.assertEqual(updated_state.Alice_flag, 1)
        self.assertEqual(updated_state.turn, 1)

    def test_action_bob(self):
        """teste les actions de Bob après Alice"""
        # Après que Alice a joué
        state_after_alice = action(self.initial_state, 0)
        updated_state = action(state_after_alice, 1)
        self.assertEqual(updated_state.Bob_state, 1)
        self.assertEqual(updated_state.Bob_flag, 1)
        self.assertEqual(updated_state.turn, 0)

    def test_full_cycle(self):
        """teste un cycle complet d'actions pour Alice et Bob"""
        state = self.initial_state
        for _ in range(3):
            state = action(state, 0)
            state = action(state, 1)
        self.assertEqual(state.Alice_state, 0)
        self.assertEqual(state.Bob_state, 0)
        self.assertTrue(state.Alice_flag in [0, 1])
        self.assertTrue(state.Bob_flag in [0, 1])
        self.assertEqual(state.Alice_flag, 0)
        self.assertEqual(state.Bob_flag, 0)



if __name__ == '__main__':
    unittest.main()
