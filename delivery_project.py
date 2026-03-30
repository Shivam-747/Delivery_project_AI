import numpy as np
import random

# ENVIRONMENT
class DeliveryEnv:
    def __init__(self, grid_size=5):
        self.grid_size = grid_size

    def reset(self):
        self.agent_pos = [0, 0]
        self.delivery_points = [[4,4], [2,2], [1,3]]
        self.done = False
        return self.state()

    def state(self):
        return tuple(self.agent_pos + sum(self.delivery_points, []))

    def step(self, action):
        if action == 0: self.agent_pos[0] -= 1
        elif action == 1: self.agent_pos[0] += 1
        elif action == 2: self.agent_pos[1] -= 1
        elif action == 3: self.agent_pos[1] += 1

        self.agent_pos[0] = max(0, min(self.grid_size-1, self.agent_pos[0]))
        self.agent_pos[1] = max(0, min(self.grid_size-1, self.agent_pos[1]))

        reward = -1

        if self.agent_pos in self.delivery_points:
            self.delivery_points.remove(self.agent_pos)
            reward += 10

        if len(self.delivery_points) == 0:
            self.done = True
            reward += 20

        return self.state(), reward, self.done


# AGENT (Q-learning)
env = DeliveryEnv()
q_table = {}
actions = [0,1,2,3]

def get_q(state, action):
    return q_table.get((state, action), 0)

def update_q(state, action, reward, next_state):
    lr = 0.1
    gamma = 0.9
    max_next = max([get_q(next_state, a) for a in actions])
    old = get_q(state, action)
    q_table[(state, action)] = old + lr * (reward + gamma * max_next - old)


# TRAINING
for episode in range(500):
    state = env.reset()

    while True:
        action = random.choice(actions)
        next_state, reward, done = env.step(action)
        update_q(state, action, reward, next_state)
        state = next_state

        if done:
            break

print("Training Complete ")