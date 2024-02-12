import unittest
from HanoiConfigSoup import HanoiConfigSoup

class TestHanoiConfigSoup(unittest.TestCase):
    def setUp(self):
        self.config = HanoiConfigSoup(3)

    def test_initial_state(self):
        """vérifie l'état initial des tours"""
        expected = [[3, 2, 1], [], []]
        self.assertEqual(self.config.towers, expected)

    def test_can_move(self):
        """vérifie la possibilité de mouvement entre les tours"""
        self.assertTrue(self.config.can_move(0, 1))
        self.assertFalse(self.config.can_move(1, 0))

    def test_move_disk(self):
        """teste le déplacement d'un disque"""
        self.config.move_disk(0, 1)
        expected = [[3, 2], [1], []]
        self.assertEqual(self.config.towers, expected)

    def test_is_final(self):
        """vérifie si l'état final est correctement identifié"""
        # pour simuler un état final -> déplacez manuellement les disques
        self.config.towers = [[], [], [3, 2, 1]]
        self.assertTrue(self.config.isFinal())
        # réinitialiser et tester un état non final
        self.config.towers = [[3], [], [2, 1]]
        self.assertFalse(self.config.isFinal())

    def test_complete_solution(self):
        """simule une solution complète et valide les états intermédiaires"""
        moves = [
            (0, 2),
            (0, 1),
            (2, 1),
            (0, 2),
            (1, 0),
            (1, 2),
            (0, 2)
        ]
        for src, dest in moves:
            self.assertTrue(self.config.can_move(src, dest), f"Le mouvement de {src} à {dest} devrait être possible")
            self.config.move_disk(src, dest)
        # vérifie l'état final pour confirmer la réussite de la solution
        self.assertTrue(self.config.isFinal(), "L'état final n'est pas atteint après la séquence de mouvements")


if __name__ == '__main__':
    unittest.main()
