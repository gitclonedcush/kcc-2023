import pygame
from settings import Paths

class Fonts:
	"""A class which contains all the sounds that we can plan in the game."""
	def __init__(self):
		self.load_fonts()
	def load_fonts(self):
		self.default_font = pygame.font.Font(Paths.FONT_PATH, 48)