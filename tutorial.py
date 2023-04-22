import gymnasium as gym
import random
import numpy as np


env = gym.make('CartPole-v1', )

# Initial state of env
observation, info = env.reset()

epochs = 100
for epoch in range(epochs):

    sample_state = env.action_space.sample()

    observation, reward, turncate, info, done = env.step(sample_state)
    print(f'Epoch {epoch}/{epochs}, reward:{reward}')

    env.render()

env.close()