import pygame
from settings import Settings
from settings import Paths

class Graphics:
	"""A class which contains all of the graphics we will display in the game."""
	def __init__(self):
		"""Set up the Graphics class."""
		self.load_graphics()
	def load_graphics(self):
		"""Create, load and scale each of the graphics."""
		self.lander = pygame.transform.scale(pygame.image.load(Paths.GRAPHICS_LANDER), (Settings.LANDER_WIDTH, Settings.LANDER_HEIGHT))
		self.titlescreen = pygame.transform.scale(pygame.image.load(Paths.GRAPHICS_TITLESCREEN), (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
		self.background = pygame.transform.scale(pygame.image.load(Paths.GRAPHICS_BACKGROUND), (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
		self.burner_raw = pygame.image.load(Paths.GRAPHICS_BURNER)
		#self.burner_primary = pygame.transform.scale(self.burner_raw, (Settings.BURNER_PRIMARY_SIZE * Settings.SCALE, Settings.BURNER_PRIMARY_SIZE * Settings.SCALE))
		self.burner_primary = pygame.transform.scale(self.burner_raw, (Settings.BURNER_PRIMARY_SIZE, Settings.BURNER_PRIMARY_SIZE))
		#left_angle = 3.14 / 2
		#right_angle = 3.14 / 2 * 3

		# Angles are in DEGREES, not radians?! ???
		left_angle = 270
		right_angle = 90

		#self.burner_left = pygame.transform.rotate(pygame.transform.scale(self.burner_raw, (Settings.BURNER_SECONDARY_SIZE * Settings.SCALE, Settings.BURNER_SECONDARY_SIZE * Settings.SCALE)), left_angle)
		#self.burner_right = pygame.transform.rotate(pygame.transform.scale(self.burner_raw, (Settings.BURNER_SECONDARY_SIZE * Settings.SCALE, Settings.BURNER_SECONDARY_SIZE * Settings.SCALE)), right_angle)
		self.burner_left = pygame.transform.rotate(pygame.transform.scale(self.burner_raw, (Settings.BURNER_SECONDARY_SIZE, Settings.BURNER_SECONDARY_SIZE)), left_angle)
		self.burner_right = pygame.transform.rotate(pygame.transform.scale(self.burner_raw, (Settings.BURNER_SECONDARY_SIZE, Settings.BURNER_SECONDARY_SIZE)), right_angle)

		self.landingpad = pygame.transform.scale(pygame.image.load(Paths.GRAPHICS_LANDINGPAD), (Settings.LANDINGPAD_SIZE))
		self.shrapnel = pygame.transform.scale(pygame.image.load(Paths.GRAPHICS_SHRAPNEL), (Settings.SHRAPNEL_SIZE, Settings.SHRAPNEL_SIZE))
