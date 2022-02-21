import gym
from gym import error, spaces, utils
from gym.utils import seeding

class MyEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array']}

    def __init__(self):
        # TODO

    def step(self, u):
        # TODO   
		
	def reset(self):
        # TODO   

	def render(self, mode='human'):
        # TODO   
        if mode == 'human':
		    # Do something
		elif mode == 'rgb_array':
		    # raw image
			# numpy image
			
    def close(self):
        # TODO