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
		self.text = TextDisplay("",SCREEN_RECT.centerx,SCREEN_RECT.centery)
	
	def draw(self,screen):
		draw.rect(screen, (0, 162, 232), self.rect)
		
	def quicktime(self,screen,delta):
		fish = []
		player = []
		for i in range(5):
			timer = 0
			prompt = str(random.randint(0,9))
			fish.append(prompt)
			screen.fill((0,0,0))
			self.text.update(screen,prompt)
			IPUT = 'void'
			while True:
				for event in pygame.event.get():
					pass
				IPUT = self.inputs()
				timer += delta/100
				screen.fill((0,0,0))
				self.text.update(screen,prompt)
				draw.rect(screen, (255,255,255), ((0+timer*800), (SCREEN_RECT.centery-100), (SCREEN_RECT.width-timer*1600), 50))
				pygame.display.flip()
				if IPUT == prompt:
					break
				if timer >= 1:
					print("FAIL")
			player.append(IPUT)
		if player == fish:
			return True
				
		
	def inputs(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_0]:
			return "0"
		elif keys[pygame.K_1]:
			return "1"
		elif keys[pygame.K_2]:
			return "2"
		elif keys[pygame.K_3]:
			return "3"
		elif keys[pygame.K_4]:
			return "4"
		elif keys[pygame.K_5]:
			return "5"
		elif keys[pygame.K_6]:
			return "6"
		elif keys[pygame.K_7]:
			return "7"
		elif keys[pygame.K_8]:
			return "8"
		elif keys[pygame.K_9]:
			return "9"
		else:
			return "void"
	
