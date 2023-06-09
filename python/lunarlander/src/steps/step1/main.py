###############################################################################
# Lunar Lander Step 1 - Main game loop
###############################################################################
# To run, type:
# python lander.py
###############################################################################

# PyGame imports
import pygame
from pygame.locals import *
import sys

# Lander game imports
from settings import *
from graphics import *
from sounds import *
from fonts import *
from lander import Lander
from titlescreen import TitleScreen
from keyboardstate import KeyboardState
from observer import EventNames, Listener, Observer
from scenemanager import SceneManager
from game import Game

###############################################################################
# PyGame Setup
###############################################################################
# Create a screen that we can draw on.
pygame.init()
screen_width = Settings.SCREEN_WIDTH
screen_height = Settings.SCREEN_HEIGHT
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode([screen_size[0], screen_size[1]])
pygame.display.set_caption("Lunar Lander")
fps = 60

###############################################################################
# Lander Game Setup
###############################################################################
settings = Settings()
graphics = Graphics()
sounds = Sounds()
fonts = Fonts()

scene_observer = Observer()
kbd_observer = Observer()
kbd = KeyboardState()

g = Game(fps, graphics, sounds, fonts, scene_observer, kbd)

lander_scene = Lander(g, scene_observer)
titlescreen_scene = TitleScreen(scene_observer)
scenemanager = SceneManager(titlescreen_scene, lander_scene)
scenemanager.switch_to(EventNames.EVENT_SWITCH_SCENE_TITLESCREEN)

# Let the titlescreen scene notify the main.py when to switch to the lander_scene
def switch_to_lander_screen(scene_name):
	scenemanager.switch_to(scene_name)

scene_listener = Listener(switch_to_lander_screen)
scene_observer.add_listener(scene_listener)

###############################################################################
# Main Game Loop
###############################################################################
while True:
	# Wait until time has passed before drawing the screen again.
	pygame.time.Clock().tick(fps)

	# Read the keyboard.  Find out which buttons are pressed.
	kbd.update(pygame.event.get())

	# If the player has quit the game, close the program now.
	if (kbd.esc_key_down):
		sys.exit()

	scene = scenemanager.scene
	# Step 1, uncomment these lines.  They are where the magic happens!
	#scene.update(kbd)
	#scene.draw(graphics, sounds, fonts, screen)

	pygame.display.update()
	