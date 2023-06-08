import pygame
import graphics
from settings import Settings
import sounds
import fonts
import game
import scenemanager


class Lander:
	def __init__(self, game: game.Game, scene_manager):
		self.game = game
		self.scene_manager = scene_manager

		self.game.reset()
	def update(self, keyboard_state):
		self.keyboard_state = keyboard_state

		self.game.tick(keyboard_state)

		self.lander_rect = (self.game.position[0], self.game.position[1], Settings.LANDER_WIDTH, Settings.LANDER_HEIGHT)
		(lander_left, lander_top, lander_width, lander_height) = self.lander_rect

		self.burner_left_rect = (
			lander_left + Settings.BURNER_SECONDARY_LEFT_XOFFSET, 
			lander_top + Settings.BURNER_SECONDARY_LEFT_YOFFSET, 
			Settings.BURNER_SECONDARY_SIZE,
			Settings.BURNER_SECONDARY_SIZE)

		self.burner_right_rect = (
			lander_left + Settings.BURNER_SECONDARY_RIGHT_XOFFSET, 
			lander_top + Settings.BURNER_SECONDARY_RIGHT_YOFFSET, 
			Settings.BURNER_SECONDARY_SIZE,
			Settings.BURNER_SECONDARY_SIZE)
		
		self.burner_primary_rect = (
			lander_left + Settings.BURNER_PRIMARY_XOFFSET,
			lander_top + Settings.BURNER_PRIMARY_yOFFSET,
			Settings.BURNER_PRIMARY_SIZE,
			Settings.BURNER_PRIMARY_SIZE)
		
		self.hud_height = 150 * Settings.SCALE
		self.hud_width = 600 * Settings.SCALE
		self.hud_rect = (0, Settings.SCREEN_HEIGHT - self.hud_height, self.hud_width, self.hud_height)
		self.hud_background_surface = pygame.Surface((self.hud_width, self.hud_height))
		self.hud_background_surface.set_alpha(128)
		
	def draw(self, graphics: graphics.Graphics, sounds: sounds.Sounds, fonts: fonts.Fonts, screen : pygame.Surface):
		# Draw a black background to fill any voids from previous frames.
		screen.fill((0, 0, 0))

		# Draw the background
		screen.blit(graphics.background, (0,0, Settings.SCREEN_HEIGHT, Settings.SCREEN_HEIGHT))

		# Draw background rectangles to help visualize boundaries while determining the best position of each sprite.
		if Settings.DEBUG:
			screen.fill("green", (self.lander_rect))
			screen.fill("blue", (self.burner_left_rect))
			screen.fill("cyan", (self.burner_primary_rect))
			screen.fill("purple", (self.burner_right_rect))

		screen.blit(graphics.landingpad, Settings.LANDINGPAD_RECT)

		if (self.game.burning_left):
			screen.blit(graphics.burner_left, self.burner_left_rect)

		if (self.game.burning_right):
			screen.blit(graphics.burner_right, self.burner_right_rect)

		if (self.game.burning_primary):
			screen.blit(graphics.burner_primary, self.burner_primary_rect)

		if (Settings.DEBUG):
			pass

		# Draw the lander
		if (not self.game.is_crashing):
			screen.blit(graphics.lander, self.lander_rect)

		# Draw the HUD
		screen.blit(self.hud_background_surface, self.hud_rect)

		padding = 15 * Settings.SCALE
		white = (255, 255, 255)
		score_text = "Score: 123456789"
		score_surface = fonts.default_font.render(score_text, True, white, None)
		score_coords = (padding, Settings.SCREEN_HEIGHT - score_surface.get_height() * Settings.SCALE - padding)
		screen.blit(
			pygame.transform.scale(score_surface, (score_surface.get_width() * Settings.SCALE, score_surface.get_height() * Settings.SCALE)), 
			(score_coords)
		)

		velocity_value = round(self.game.velocity[1], 2)
		velocity_text = f"Velocity: {velocity_value}"
		velocity_surface = fonts.default_font.render(velocity_text, True, white, None)
		velocity_coords = (padding, score_coords[1] - velocity_surface.get_height() * Settings.SCALE - padding)
		screen.blit(
			pygame.transform.scale(velocity_surface, (velocity_surface.get_width() * Settings.SCALE, velocity_surface.get_height() * Settings.SCALE)),
			(velocity_coords)
		)

		# Draw shards of shrapnel that look like the lander has been destroyed
		if self.game.is_crashing:
			for shard in self.game.shrapnel:
				# Reposition the shard to avoid "jitter" by compensating for the new size after rotation.
				rotated = pygame.transform.rotate(graphics.shrapnel, shard.angle)
				original_width = graphics.shrapnel.get_width()
				original_height = graphics.shrapnel.get_height()
				origin_x = shard.xpos + original_width / 2.0
				origin_y = shard.ypos + original_height / 2.0
				new_x = origin_x - rotated.get_width() / 2.0
				new_y = origin_y - rotated.get_height() / 2.0

				screen.blit(rotated, (new_x, new_y))
		