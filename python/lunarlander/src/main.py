###############################################################################
# Lunar Lander Step 0 - The final game
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
#screen_size = (screen_columns * Settings.BLOCK_SIZE * Settings.SCALE, screen_rows * Settings.BLOCK_SIZE * Settings.SCALE)
pygame.init()
screen_width = Settings.SCREEN_WIDTH
screen_height = Settings.SCREEN_HEIGHT
screen_size = (screen_width, screen_height)
#screen_size = (screen_width * Settings.SCALE, screen_height * Settings.SCALE)
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
#scene = titlescreen_scene
scenemanager = SceneManager(titlescreen_scene, lander_scene)
scenemanager.switch_to(EventNames.EVENT_SWITCH_SCENE_TITLESCREEN)

# Let the titlescreen scene notify the main.py when to switch to the lander_scene
def switch_to_lander_screen(scene_name):
	#if scene_name == EventNames.EVENT_SWITCH_SCENE_LANDER:
	#	scene = lander_scene
	#elif scene_name == EventNames.EVENT_SWITCH_SCENE_TITLESCREEN:
	#	scene = titlescreen_scene
	#print("Switched to new scene!")
	#print(scene)
	scenemanager.switch_to(scene_name)

scene_listener = Listener(switch_to_lander_screen)
scene_observer.add_listener(scene_listener)

#print("This is the console output!")
#value = input("Press ENTER key to continue...")


###############################################################################
# Main Game Loop
###############################################################################
while True:
	# Wait until time has passed before drawing the screen again.
	pygame.time.Clock().tick(fps)

	# Look for user input in case they want to quit the game.
	#events : List[Event] = pygame.event.get()
	#for event in pygame.event.get():
	#	e: pygame.event.Event = event
	#	# Pay attention if the user clicks the X to quit.
	#	if event.type == pygame.QUIT:
	#		sys.exit()

	#	# Check the keyboard for keypresses. 
	#	if event.type == pygame.KEYDOWN:
	#		if event.key == K_ESCAPE:
	#			sys.exit()
	#		if event.key == K_UP:
	#			pass
	#		if event.key == K_DOWN:
	#			pass
	#		if event.key == K_LEFT:
	#			pass
	#		if event.key == K_RIGHT:
	#			pass
	#		if event.key == K_RETURN or event.key == K_KP_ENTER:
	#			pass

	# Read the keyboard.  Find out which buttons are pressed.
	kbd.update(pygame.event.get())

	# If the player has quit the game, close the program now.
	if (kbd.esc_key_down):
		sys.exit()

	scene = scenemanager.scene
	scene.update(kbd)
	scene.draw(graphics, sounds, fonts, screen)

	pygame.display.update()
	