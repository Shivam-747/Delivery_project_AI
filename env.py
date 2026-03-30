import random
from typing import Self

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
        # actions: 0=up,1=down,2=left,3=right
        if action == 0: self.agent_pos[0] -= 1
        elif action == 1: self.agent_pos[0] += 1
        elif action == 2: self.agent_pos[1] -= 1
        elif action == 3: self.agent_pos[1] += 1

        # boundary check
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

    def render(self):
        grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for d in self.delivery_points:
            grid[d[0]][d[1]] = "D"

        grid[self.agent_pos[0]][self.agent_pos[1]] = "A"

        for row in grid:
            print(" ".join(row))
        print("\n")