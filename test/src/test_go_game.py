import unittest

from src import GoGame


class TestGoGame(unittest.TestCase):
    def setUp(self):
        self.go_game = GoGame()

    def test_is_valid_move_ok(self):
        self.assertTrue(self.go_game.is_valid_move(0, 0))

    def test_is_valid_move_nok(self):
        self.go_game.board[0][0] = 1
        self.assertFalse(self.go_game.is_valid_move(0, 0))

    def test_place_stone_ok(self):
        self.assertTrue(self.go_game.place_stone(0, 0))
        self.assertEqual(self.go_game.board[0][0], 1)
        self.assertEqual(self.go_game.current_player, -1)
        self.assertEqual(self.go_game.opponent, 1)
        self.assertEqual(self.go_game.last_action, (0, 0))

    def test_place_stone_nok(self):
        self.assertTrue(self.go_game.place_stone(0, 0))
        self.assertFalse(self.go_game.place_stone(0, 0))

    def test_no_empty_positions(self):
        self.assertFalse(self.go_game.no_empty_positions())
        for i in range(self.go_game.size):
            for j in range(self.go_game.size):
                self.go_game.place_stone(i, j)
        self.assertTrue(self.go_game.no_empty_positions())

    def test_is_game_over(self):
        self.assertFalse(self.go_game.is_game_over())
        self.go_game.pass_count = 2
        self.assertTrue(self.go_game.is_game_over())
        self.go_game.pass_count = 0
        for i in range(self.go_game.size):
            for j in range(self.go_game.size):
                self.go_game.place_stone(i, j)
        self.assertTrue(self.go_game.is_game_over())

    def test_get_possible_actions(self):
        for i in range(self.go_game.size):
            for j in range(self.go_game.size):
                self.assertTrue((i, j) in self.go_game.get_possible_actions())


if __name__ == "__main__":
    unittest.main()
