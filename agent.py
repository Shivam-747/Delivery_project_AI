import random

class QAgent:
    def __init__(self, actions):
        self.q_table = {}
        self.actions = actions
        self.lr = 0.1
        self.gamma = 0.9

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0)

    def choose_action(self, state):
        return random.choice(self.actions)

    def update(self, state, action, reward, next_state):
        max_next = max([self.get_q(next_state, a) for a in self.actions])
        old = self.get_q(state, action)

        self.q_table[(state, action)] = old + self.lr * (reward + self.gamma * max_next - old)