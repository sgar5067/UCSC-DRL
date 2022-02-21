import gym
from gym import error, spaces, utils
from gym.utils import seeding

class MyEnv(gym.Env):
  metadata = {'render.modes': ['human', 'rgb_array']}

  def __init__(self):
    pass

  def step(self, u):
   pass   

  def reset(self):
    pass   

  def render(self, mode='human'):
    # pass   
    if mode == 'human':
      # Do something
    elif mode == 'rgb_array':
      # Do something else
			
  def close(self):
    pass
