import tkinter as tk

from .go_game import GoGame
from .go_nn import GoNeuralNetwork
from .mcts import MCTS

class GoGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        
        # Create Go board
        self.board_size = 19
        self.cell_size = 20
        self.draw_board()

        self.go_game = GoGame(self.board_size)
        self.neural_network_B = GoNeuralNetwork(self.board_size)
        self.neural_network_W = GoNeuralNetwork(self.board_size)
        self.agent_B = MCTS(self.go_game, self.neural_network_B)
        self.agent_W = MCTS(self.go_game, self.neural_network_W)

    def draw_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                x0, y0 = j * self.cell_size, i * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black")

    def draw_move(self, row, col, color):
        x0, y0 = col * self.cell_size, row * self.cell_size
        x1, y1 = x0 + self.cell_size, y0 + self.cell_size
        self.canvas.create_oval(x0, y0, x1, y1, fill=color)

    def run_game_loop(self):
        while not self.go_game.is_game_over():
            self.agent_B.search(num_iterations=10)
            best_action_B = self.agent_B.get_best_action()
            if best_action_B is not None and self.go_game.is_valid_move(*best_action_B):
                self.go_game.place_stone(best_action_B[0], best_action_B[1])
            self.draw_move(best_action_B[0], best_action_B[1], "black" if self.go_game.current_player == 'B' else "white")
            self.master.update()
            if self.go_game.is_game_over():
                break

            self.agent_W.search(num_iterations=10)
            best_action_W = self.agent_W.get_best_action()
            if best_action_W is not None and self.go_game.is_valid_move(*best_action_B):
                self.go_game.place_stone(best_action_W[0], best_action_W[1])
            self.draw_move(best_action_W[0], best_action_W[1], "black" if self.go_game.current_player == 'B' else "white")
            self.master.update()
