import random
import graphics
import keyboardstate
import sounds
import fonts
from settings import Settings
from cooldown import Cooldown
from observer import Observer, EventNames
from pygametimefunction import pygame_time_function
from shard import Shard

class Game:
	"""Represents the state and behaviors of a game instance."""
	def __init__(
			self, 
			fps,
			graphics : graphics.Graphics, 
			sounds : sounds.Sounds, 
			fonts : fonts.Fonts, 
			scene_observer: Observer,
			kbd_state: keyboardstate.KeyboardState
			):
		"""Capture injected __init__ parameters."""
		self.fps = fps
		self.graphics = graphics
		self.sounds = sounds
		self.fonts = fonts
		self.scene_observer = scene_observer
		self.old_kbd_state = kbd_state.clone()
		self.random = random.Random()
		self.calc_everything()
		self.reset()
	def play_burner(self, kbdstate: keyboardstate.KeyboardState):
		self.sounds.burner.play()
	def stop_burner(self):
		self.sounds.burner.stop()
	def calc_everything(self):
		"""These are one-time calculations that are done on init."""
		pass
	def reset(self):
		"""Reset everything to start a new round (game)."""
		self.score = 0
		self.fuel = Settings.INITIAL_FUEL
		self.velocity = Settings.INITIAL_VELOCITY
		self.position = (self.random.random() * (Settings.SCREEN_WIDTH - Settings.LANDER_WIDTH), 0)
		self.burning_left = False
		self.burning_right = False
		self.burning_primary = False
		self.is_crashing = False
		self.is_landing = False
		self.is_playing = True
		self.reset_cooldown = None
		self.shrapnel: list[Shard] = []
		self.reset_sounds()
		self.reset_burners()
	def reset_sounds(self):
		self.sounds.primaryburner.stop()
		self.sounds.leftburner.stop()
		self.sounds.rightburner.stop()
	def reset_burners(self):
		self.burning_primary = False
		self.burning_left = False
		self.burning_right = False
	def start_landing(self):
		# Check the velocity and adjust the score.  Start a cooldown to pause gameplay for a moment, then start a new game.
		self.is_playing = False
		self.is_landing = True
		self.reset_cooldown = Cooldown(pygame_time_function, 3000)
		self.reset_sounds()
		self.reset_burners()
	def do_landing(self):
		if (self.reset_cooldown.expired()):
			self.reset()
	def start_crash(self):
		self.is_playing = False
		self.is_crashing = True
		self.reset_cooldown = Cooldown(pygame_time_function, 5000)
		self.shrapnel = self.create_shrapnel()
		self.reset_sounds()
		self.reset_burners()
	def do_crash(self):
		if (self.reset_cooldown.expired()):
			# Just switch to the game over screen.
			self.reset()
			self.scene_observer.trigger(EventNames.EVENT_SWITCH_SCENE_TITLESCREEN)
		else:
			# Still crashing! Adjust shrapnel images
			for shard in self.shrapnel:
				shard.xpos += shard.xvelocity
				shard.ypos += shard.yvelocity
				shard.angle = (shard.angle + shard.avelocity) % 360
	def create_shrapnel(self):
		result = []
		shard_count = 13
		(x, y) = self.position
		x += Settings.LANDER_WIDTH / 2.0 - Settings.SHRAPNEL_SIZE / 2.0
		y += Settings.LANDER_HEIGHT
		for n in range(shard_count):
			yvelocity = -1 * self.random.random() - 1
			xvelocity = (self.random.random() - 0.5) * 2
			avelocity = (self.random.random() * 6.0) - 3.0
			xpos = x
			ypos = y
			apos = self.random.random() * 360
			shard = Shard(xvelocity, yvelocity, avelocity, xpos, ypos, apos)
			result.append(shard)
		return result
	def check_for_landing(self):
		# If y is >= landingpad line and downward velocity < max landing velocity 
		# then you win!  Otherwise, you crash!
		
		(x, y) = self.position
		# Adjust the y value to be the bottom of the lander, not the top.
		y = y + Settings.LANDER_HEIGHT 
		landed = y > Settings.LANDINGPAD_LINE_Y
		on_the_pad = landed and x > Settings.LANDINGPAD_X_BOUNDS[0] and x < Settings.LANDINGPAD_X_BOUNDS[1]
		if landed:
			# We have landed or crashed on the pad or the surface.  Which was it?
			(xv, yv) = self.velocity
			too_fast = yv > Settings.MAX_LANDING_VELOCITY
			if on_the_pad and not too_fast:
				self.start_landing()
			else:
				self.start_crash()
	def apply_gravity(self):
		(x, y) = self.velocity
		self.velocity = (x, y + Settings.GRAVITY * Settings.GRAVITY_SCALE)
	def apply_primary_thrust(self):
		(x, y) = self.velocity
		self.velocity = (x, y - Settings.PRIMARY_THRUST * Settings.THRUST_SCALE)
	def apply_left_thrust(self):
		(x, y) = self.velocity
		self.velocity = (x + Settings.LEFT_THRUST * Settings.THRUST_SCALE, y)
	def apply_right_thrust(self):
		(x, y) = self.velocity
		self.velocity = (x - Settings.RIGHT_THRUST * Settings.THRUST_SCALE, y)
	def move_lander(self):
		(leftright, updown) = self.velocity
		(x, y) = self.position
		self.position = (x + leftright, y + updown)
	def tick(self, new_kbd_state: keyboardstate.KeyboardState):
		"""This executes every time a frame is processed (60 times per second).
		Here, we write code to adjust the state and position of everything in the game 
		before the next	screen is drawn."""
		if (self.is_landing):
			self.do_landing()

		if self.is_crashing:
			self.do_crash()
			
		if self.is_playing:
			self.check_for_landing()
			self.apply_gravity()

			if self.old_kbd_state.up_arrow_down != new_kbd_state.up_arrow_down:
				self.burning_primary = new_kbd_state.up_arrow_down
				if self.burning_primary:
					self.sounds.primaryburner.play()
				else:
					self.sounds.primaryburner.stop()

			if self.old_kbd_state.left_arrow_down != new_kbd_state.left_arrow_down:
				self.burning_right = new_kbd_state.left_arrow_down
				if self.burning_right:
					self.sounds.rightburner.play()
				else:
					self.sounds.rightburner.stop()

			if self.old_kbd_state.right_arrow_down != new_kbd_state.right_arrow_down:
				self.burning_left = new_kbd_state.right_arrow_down
				if self.burning_left:
					self.sounds. leftburner.play()
				else:
					self.sounds.leftburner.stop()

			if self.burning_primary:
				self.apply_primary_thrust()

			if self.burning_left:
				self.apply_left_thrust()

			if self.burning_right:
				self.apply_right_thrust()

			self.move_lander()

		# Store the new keyboard state for next time.
		self.old_kbd_state = new_kbd_state.clone()



