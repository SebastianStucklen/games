import pygame
from pygame.math import Vector2
import math
import random

from pygame import Rect
from pygame import draw
from globals import SCREEN_RECT, TextDisplay

class FishingHole:
	def __init__(self):
		self.rect = Rect(50,400,700,400)
		self.text: list[TextDisplay] = []
	
	def draw(self,screen):
		draw.rect(screen, (0, 162, 232), self.rect)

	def collide(self,coord: Vector2):
		if self.rect.collidepoint(coord):
			return True


	def quicktime(self,screen,delta,len) -> bool:
		fish = []
		player = []
		timer = 0
		screen.fill((0,0,0))
		for i in range(len):
			prompt = str(random.randint(0,9))
			if i > 0:
				while prompt == fish[i-1]:
					prompt = str(random.randint(0,9))
			fish.append(prompt)
			self.text.append(TextDisplay(fish[i], SCREEN_RECT.x + i * ((SCREEN_RECT.width - 100) / len), SCREEN_RECT.centery, 200))
			print(SCREEN_RECT.x + i * ((SCREEN_RECT.width - 100) / len))
			self.text[i].update(screen,fish[i],200)
			print(fish, self.text[i].x)
		for j in range(len):
			IPUT = 'void'
			while True:
				maxtime = len*0.7

				for event in pygame.event.get():
					pass

				IPUT = self.inputs()

				timer += delta/15

				draw.rect(screen, (255,0,0), ((0 + SCREEN_RECT.width / 4), (SCREEN_RECT.centery - 100), (SCREEN_RECT.width / 2), 50))
				draw.rect(screen, (255,255,255), ((0 + SCREEN_RECT.width / 4 +timer * ((SCREEN_RECT.width / 2)/maxtime)), (SCREEN_RECT.centery - 100), (SCREEN_RECT.width / 2 - timer * ((SCREEN_RECT.width / 2)/maxtime)), 50))

				pygame.display.flip()

				if IPUT == fish[j]:
					self.text[j].update(screen,fish[j],200,(100,100,100))
					break
				if timer >= maxtime:
					# print("FAIL")
					pass

			player.append(IPUT)

		if player == fish:
			return True
		else:
			print(fish, player)
			return False
				
		
	def inputs(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_0] or keys[pygame.K_KP0]:
			return "0"
		elif keys[pygame.K_1] or keys[pygame.K_KP1]:
			return "1"
		elif keys[pygame.K_2] or keys[pygame.K_KP2]:
			return "2"
		elif keys[pygame.K_3] or keys[pygame.K_KP3]:
			return "3"
		elif keys[pygame.K_4] or keys[pygame.K_KP4]:
			return "4"
		elif keys[pygame.K_5] or keys[pygame.K_KP5]:
			return "5"
		elif keys[pygame.K_6] or keys[pygame.K_KP6]:
			return "6"
		elif keys[pygame.K_7] or keys[pygame.K_KP7]:
			return "7"
		elif keys[pygame.K_8] or keys[pygame.K_KP8]:
			return "8"
		elif keys[pygame.K_9] or keys[pygame.K_KP9]:
			return "9"
		else:
			return "void"
	
