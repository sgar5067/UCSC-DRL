import gym
from gym import error, spaces, utils
from gym.utils import seeding

class MyEnv(gym.Env):
  metadata = {'render.modes': ['human', 'rgb_array']}

  def __init__(self):
    pass

  def step(self, u):
   pass   

  def reset(self, **kwargs):
    pass   

  def render(self, mode='human'):
    pass   
#     if mode == 'human':
#       pass
#     elif mode == 'rgb_array':
#       pass
			
  def close(self):
    pass
