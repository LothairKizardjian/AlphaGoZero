class GoGame:
    def __init__(self, size=19):
        self._size = size
        self._board = [[0 for _ in range(size)] for _ in range(size)]
        self._current_player = 1
        self._opponent = -1
        self._pass_count = 0  # Track consecutive passes
        self._last_action = None

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, s):
        self._size = s

    @property
    def board(self):
        return self._board

    @property
    def current_player(self):
        return self._current_player

    @current_player.setter
    def current_player(self, val):
        self._current_player = val

    @property
    def opponent(self):
        return self._opponent

    @opponent.setter
    def opponent(self, val):
        self._opponent = val

    @property
    def pass_count(self):
        return self._pass_count

    @pass_count.setter
    def pass_count(self, val):
        self._pass_count = val

    @property
    def last_action(self):
        return self._last_action

    @last_action.setter
    def last_action(self, val):
        self._last_action = val

    def is_valid_move(self, row, col):
        return self.board[row][col] == 0

    def place_stone(self, row, col):
        if not self.is_valid_move(row, col):
            return False
        self.board[row][col] = self.current_player
        self.current_player, self.opponent = self.opponent, self.current_player
        self.last_action = (row, col)  # Update last action
        return True

    def no_empty_positions(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    return False
        return True

    def is_game_over(self):
        if self.pass_count >= 2:
            return True  # Both players passed consecutively
        if self.no_empty_positions():
            return True  # No more empty positions on the board
        return False

    def get_possible_actions(self):
        actions = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    actions.append((row, col))
        return actions

    def get_next_state(self, action):
        row, col = action
        next_state = GoGame(size=self.size)
        next_state.board = [row[:] for row in self.board]
        next_state.place_stone(row, col)
        return next_state
