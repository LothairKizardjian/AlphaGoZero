import torch
import torch.nn as nn

from .go_game import GoGame

class GoNeuralNetwork(nn.Module):
    def __init__(self, board_size):
        super(GoNeuralNetwork, self).__init__()
        self.board_size = board_size
        self.conv1 = nn.Conv2d(in_channels=2, out_channels=64, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64 * board_size * board_size, board_size * board_size)
        self.fc2 = nn.Linear(64 * board_size * board_size, 1)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = torch.relu(self.conv3(x))
        x = x.view(-1, 64 * self.board_size * self.board_size)
        
        # Output for move probabilities
        move_probs = torch.softmax(self.fc1(x), dim=1)
        
        # Output for game state estimation
        state_value = torch.tanh(self.fc2(x))
        
        return move_probs, state_value

    def predict(self, state):
        # Preprocess the board state
        state_tensor = self.preprocess_state(state)
        
        # Pass the preprocessed state tensor through the neural network
        move_probs, state_value = self.forward(state_tensor)
        
        # Convert tensors to numpy arrays and return
        return move_probs.squeeze().detach().numpy(), state_value.item()

    def preprocess_state(self, state: GoGame):
        # Convert the state (board) to a tensor
        tensor_board = torch.zeros(2, self.board_size, self.board_size, dtype=torch.float32)
        for i in range(self.board_size):
            for j in range(self.board_size):
                if state.board[i][j] == 'B':
                    tensor_board[0, i, j] = 1
                elif state.board[i][j] == 'W':
                    tensor_board[1, i, j] = 1
        return tensor_board.unsqueeze(0)  # Add batch dimension
    