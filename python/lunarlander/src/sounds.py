import pygame
from settings import Paths

class Sounds:
	"""A class which contains all the sounds that we can play in the game."""
	def __init__(self):
		self.load_sounds()
	def load_sounds(self):
		self.primaryburner = pygame.mixer.Sound(Paths.SOUND_BURNER)
		self.leftburner = pygame.mixer.Sound(Paths.SOUND_BURNER)
		self.rightburner = pygame.mixer.Sound(Paths.SOUND_BURNER)