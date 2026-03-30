from env import DeliveryEnv

env = DeliveryEnv()
state = env.reset()

for _ in range(10):
    env.render()
    