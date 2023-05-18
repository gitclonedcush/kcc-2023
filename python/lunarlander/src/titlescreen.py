# PyGame imports
import pygame
import keyboardstate
import settings
import graphics
import sounds
import fonts
import observer

class TitleScreen:
	def __init__(self, scene_observer):
		self.scene_observer = scene_observer
	def update(self, keyboard_state: keyboardstate.KeyboardState):
		self.keyboard_state = keyboard_state
		# If ENTER is pressed, we switch to the game scene.
		# Really, we tell the main.py method to do it.  This class was provided 
		# with a function to do this for us when it was created!
		#print("From TitleScreen: ")
		#keyboard_state.show_state()
		if (keyboard_state.enter_down):
			self.scene_observer.trigger(observer.EventNames.EVENT_SWITCH_SCENE_LANDER)
	def draw(self, graphics: graphics.Graphics, sounds: sounds.Sounds, fonts: fonts.Fonts, screen : pygame.Surface):
		# Draw a black background, just to make sure there is nothing visible in any gaps.
		screen.fill((0, 0, 0))
		# Draw the title screen background.
		screen.blit(graphics.titlescreen, (0,0, 640, 480))
