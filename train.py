from env import DeliveryEnv
from agent import QAgent

env = DeliveryEnv()
agent = QAgent(actions=[0,1,2,3])

episodes = 500

for episode in range(episodes):
    state = env.reset()

    while True:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)

        agent.update(state, action, reward, next_state)
        state = next_state

        if done:
            break

print("Training Completed ")
env.render()