import pygame
import sys

class KeyboardState:
	def __init__(self):
		self.reset()

	def equals(self, compare_to):
		if (self == compare_to):
			return True
		return \
			self.up_arrow_down == compare_to.up_arrow_down and \
			self.down_arrow_down == compare_to.down_arrow_down and \
			self.left_arrow_down == compare_to.left_arrow_down and \
			self.right_arrow_down == compare_to.right_arrow_down and \
			self.space_down == compare_to.space_down and \
			self.esc_key_down == compare_to.esc_key_down and \
			self.enter_down == compare_to.enter_down 

	def reset(self):
		self.esc_key_down = False
		self.left_arrow_down = False
		self.right_arrow_down = False
		self.up_arrow_down = False
		self.down_arrow_down = False
		self.space_down = False
		self.enter_down = False
	def update(self, events):
		for e in events:
			# Pay attention if the user clicks the X to quit.
			if e.type == pygame.QUIT:
				sys.exit()

			# Check the keyboard for keypresses.
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					self.esc_key_down = True
				if e.key == pygame.K_UP:
					self.up_arrow_down = True
				if e.key == pygame.K_DOWN:
					self.down_arrow_down = True
				if e.key == pygame.K_LEFT:
					self.left_arrow_down = True
				if e.key == pygame.K_RIGHT:
					self.right_arrow_down = True
				if e.key == pygame.K_SPACE:
					self.space_down = True
				if e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
					self.enter_down = True
			if e.type == pygame.KEYUP:
				if e.key == pygame.K_ESCAPE:
					self.esc_key_down = False
				if e.key == pygame.K_UP:
					self.up_arrow_down = False
				if e.key == pygame.K_DOWN:
					self.down_arrow_down = False
				if e.key == pygame.K_LEFT:
					self.left_arrow_down = False
				if e.key == pygame.K_RIGHT:
					self.right_arrow_down = False
				if e.key == pygame.K_SPACE:
					self.space_down = False
				if e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
					self.enter_down = False

	def clone(self):
		result = KeyboardState()
		result.up_arrow_down = self.up_arrow_down
		result.down_arrow_down = self.down_arrow_down
		result.left_arrow_down = self.left_arrow_down
		result.right_arrow_down = self.right_arrow_down
		result.space_down = self.space_down
		result.esc_key_down = self.esc_key_down
		result.enter_down = self.enter_down
		return result

	def show_state(self):
		escstring = "esc " if self.esc_key_down else ""
		upstring = "up " if self.up_arrow_down else ""
		downstring = "down " if self.down_arrow_down else ""
		leftstring = "left " if self.left_arrow_down else ""
		rightstring = "right " if self.right_arrow_down else ""
		spacestring = "space " if self.space_down else ""
		enterstring = "enter " if self.enter_down else ""

		tostring = "[ " + escstring + upstring + downstring + leftstring + rightstring + enterstring + spacestring + "]"
		print(tostring)
