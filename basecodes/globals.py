from pygame.math import Vector2
from pygame import Rect
import pygame

SCREEN_SIZE = (1600, 900)
SCREEN_RECT = Rect(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1])
FPS = 60

class TextDisplay:
	def __init__(self, text, x, y,size):
		if text == None: text = ""
		self.text = text
		self.x = x
		self.y = y

	def update(self, screen, text,size):
		font = pygame.font.Font(None, 200)
		text = font.render(str(text), 1, (255, 255, 255))
		screen.blit(text, (self.x, self.y))