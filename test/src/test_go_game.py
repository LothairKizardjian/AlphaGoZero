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
        self.go_game.place_stone(0, 0)
        self.assertEqual(self.go_game.board[0][0], 1)


if __name__ == "__main__":
    unittest.main()
