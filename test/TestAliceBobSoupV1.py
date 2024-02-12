import unittest
from AliceEtBobSoup1 import AliceBobConfV1, p1a_a


class TestAliceBobConfV1(unittest.TestCase):
    def setUp(self):
        self.conf = AliceBobConfV1()

    def test_initial_state(self):
        self.assertEqual(self.conf.EtatALICE, 0)
        self.assertEqual(self.conf.EtatBOB, 0)
        self.assertEqual(self.conf.flagAlice, 0)
        self.assertEqual(self.conf.flagBob, 0)

    def test_alice_state_transitions(self):
        initial_state = self.conf.__str__()
        p1a_a(self.conf, 0)  # Apply Alice operation
        self.assertNotEqual(initial_state, self.conf.__str__())
        self.assertTrue(self.conf.flagAlice in [0, 1])
        self.assertTrue(self.conf.EtatALICE in range(3))

    def test_bob_state_transitions(self):
        initial_state = self.conf.__str__()
        p1a_a(self.conf, 1)  # Apply Bob operation
        self.assertNotEqual(initial_state, self.conf.__str__())
        self.assertTrue(self.conf.flagBob in [0, 1])
        self.assertTrue(self.conf.EtatBOB in range(3))

    def test_equality_and_hash(self):
        conf1 = AliceBobConfV1()
        conf2 = AliceBobConfV1()
        self.assertEqual(conf1, conf2)
        self.assertEqual(hash(conf1), hash(conf2))
        p1a_a(conf1, 0)  # Modify conf1
        self.assertNotEqual(conf1, conf2)
        self.assertNotEqual(hash(conf1), hash(conf2))

    def test_sequence_operations(self):
        """Teste une séquence d'opérations pour Alice et Bob"""
        sequence = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for op, actor in sequence:
            p1a_a(self.conf, actor)
        self.assertNotEqual(self.conf.EtatALICE, 0)
        self.assertNotEqual(self.conf.EtatBOB, 0)

    def test_random_operations(self):
        """Exécute un nombre aléatoire d'opérations pour Alice et Bob et vérifie la cohérence"""
        import random
        for _ in range(10):  # 10 opérations aléatoires
            actor = random.choice([0, 1])
            p1a_a(self.conf, actor)
        # assertions sur l'état après les opérations aléatoires
        self.assertTrue(self.conf.EtatALICE in range(3), "EtatALICE devrait être entre 0 et 2 inclus")
        self.assertTrue(self.conf.EtatBOB in range(3), "EtatBOB devrait être entre 0 et 2 inclus")

        # vérifiez les flags en fonction des états finaux
        if self.conf.EtatALICE == 0:
            self.assertEqual(self.conf.flagAlice, 0, "FlagAlice devrait être 0 quand EtatALICE est 0")
        else:
            self.assertEqual(self.conf.flagAlice, 1, "FlagAlice devrait être 1 quand EtatALICE n'est pas 0")

        if self.conf.EtatBOB == 0:
            self.assertEqual(self.conf.flagBob, 0, "FlagBob devrait être 0 quand EtatBOB est 0")
        else:
            self.assertEqual(self.conf.flagBob, 1, "FlagBob devrait être 1 quand EtatBOB n'est pas 0")




if __name__ == '__main__':
    unittest.main()
