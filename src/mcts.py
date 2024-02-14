import numpy as np

from .node import Node

class MCTS:
    def __init__(self, root_state, neural_network):
        self.root = Node(root_state)
        self.neural_network = neural_network

    def search(self, num_iterations):
        for _ in range(num_iterations):
            node = self.select_node()
            node.expand()
            child_node = node.select_child()
            value = child_node.rollout(self.neural_network, n_steps=5) # Adjust n_steps as needed
            child_node.backpropagate(value)

    def select_node(self):
        current_node = self.root
        while len(current_node.children) > 0:
            if np.random.uniform(0, 1) < 0.1:  # Exploration probability
                return current_node
            current_node = current_node.select_child()
        return current_node

    def get_action_probs(self, temperature=1):
        visits = [child.visits for child in self.root.children]
        if temperature == 0:
            # If temperature is 0, return a one-hot vector for the best action
            best_action_index = np.argmax(visits)
            action_probs = np.zeros(len(visits))
            action_probs[best_action_index] = 1
        else:
            # Apply softmax with temperature scaling
            visits = np.array(visits)
            action_probs = np.exp(visits / temperature) / np.sum(np.exp(visits / temperature))
        return action_probs

    def get_best_action(self):
        best_child = max(self.root.children, key=lambda child: child.visits)
        action_index = best_child.state.get_last_action()  # Get the last action from the best child state
        if action_index is None:
            return None  # No action taken yet
        row, col = action_index
        return row, col