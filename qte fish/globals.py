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

	def update(self, screen, text, size, color: tuple = (255,255,255)):
		font = pygame.font.Font(None, size)
		text = font.render(str(text), 1, color)
		screen.blit(text, (self.x, self.y))

def interact():
	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		return True