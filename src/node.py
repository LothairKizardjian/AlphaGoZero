import math
import numpy as np

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

    def expand(self):
        possible_actions = self.state.get_possible_actions()
        for action in possible_actions:
            next_state = self.state.get_next_state(action)
            child_node = Node(next_state, parent=self)
            self.children.append(child_node)

    def select_child(self):
        # Select a child node based on UCT (Upper Confidence Bound applied to Trees) formula
        max_uct = -float('inf')
        selected_child = None
        for child in self.children:
            if child.visits == 0:
                return child
            uct = child.value / child.visits + math.sqrt(2 * math.log(self.visits) / child.visits)
            if uct > max_uct:
                max_uct = uct
                selected_child = child
        return selected_child

    def rollout(self, neural_network, n_steps):
        current_state = self.state
        for _ in range(n_steps):
            action_probs, _ = neural_network.predict(current_state)
            best_action_index = np.argmax(action_probs)
            row = best_action_index // current_state.size
            col = best_action_index % current_state.size
            current_state = current_state.get_next_state((row, col))
        _, state_value = neural_network.predict(current_state)
        return state_value

    def backpropagate(self, value):
        self.visits += 1
        self.value += value
        if self.parent is not None:
            self.parent.backpropagate(value)