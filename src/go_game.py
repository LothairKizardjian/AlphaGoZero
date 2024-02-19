class GoGame:
    def __init__(self, size=19):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.current_player = 1
        self.opponent = -1
        self.pass_count = 0  # Track consecutive passes
        self.last_action = None

    def is_valid_move(self, row, col):
        return self.board[row][col] == 0

    def place_stone(self, row, col):
        if not self.is_valid_move:
            return False
        self.board[row][col] = self.current_player
        self.current_player, self.opponent = self.opponent, self.current_player
        self.last_action = (row, col)  # Update last action
        return True

    def get_last_action(self):
        return self.last_action

    def is_game_over(self):
        if self.pass_count >= 2:
            return True  # Both players passed consecutively
        if self.no_empty_positions():
            return True  # No more empty positions on the board
        return False

    def no_empty_positions(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == " ":
                    return False
        return True

    def get_possible_actions(self):
        actions = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == " ":
                    actions.append((row, col))
        return actions

    def get_next_state(self, action):
        row, col = action
        next_state = GoGame(size=self.size)
        next_state.board = [row[:] for row in self.board]
        next_state.place_stone(row, col)
        return next_state
