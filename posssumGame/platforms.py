from cmath import rect
import pygame
from random import randrange as rr
import math
from pygame.math import Vector2
from pygame.rect import Rect


screen = pygame.display.set_mode((1600, 900))  # creates game screen

_floorsprite = pygame.image.load('resources/grass.jpg')
_floorsprite = pygame.transform.smoothscale(_floorsprite,(50,50))
_spikesprite = pygame.image.load('resources/spikeman.png')
_spikesprite = pygame.transform.smoothscale(_spikesprite,(50,50))
_trampolinesprite = pygame.image.load('resources/aaa6fd39badef20.png')
_trampolinesprite = pygame.transform.smoothscale(_trampolinesprite,(50,50))
global plat
plat = 0

class Platform:
	image: pygame.Surface
	hitbox: Rect
	type: str
	velChange: Vector2
	flooroffset: int

	def __init__(self, xpos, ypos):
		self.velChange = Vector2 (10,0)
		self.flooroffset = 0
	def draw(self):
		pygame.draw.rect(screen, (100, 50, 100), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
	
	def move(self):
		pass
	def returnType(self):
		return self.type
	
	def updatePos(self,x,y):
		self.hitbox.update(x,y,self.hitbox.width,self.hitbox.height)

class spike(Platform):
	image = _spikesprite

	def __init__(self, xpos, ypos):
		self.hitbox = Rect(xpos, ypos, 50, 50)
		self.type = "spike"
		super().__init__(xpos, ypos)
	
	def draw(self):
		screen.blit(self.image, self.hitbox)
class topSpike(Platform):
	image = _spikesprite

	def __init__(self, xpos, ypos):
		self.hitbox = Rect(xpos, ypos, 50, 50)
		self.type = "spike"
		super().__init__(xpos, ypos)
	
	def draw(self):
		screen.blit(self.image, self.hitbox)
class Floor(Platform):
	image = _floorsprite

	def __init__(self, xpos, ypos):
		self.hitbox = Rect(xpos, ypos, 50, 50)
		self.type = "normal"
		self.floors = []
		super().__init__(xpos, ypos)
	
	def draw(self):

		screen.blit(self.image, self.hitbox)

class Trampoline(Platform):
	image = _trampolinesprite
	def __init__(self, xpos, ypos):
		self.hitbox = Rect(xpos, ypos, 50, 50)
		self.type = "trampoline"
		self.velChange = Vector2 (0,10)
		super().__init__(xpos, ypos)
		
		
	def draw(self):
	
		screen.blit(self.image, self.hitbox)
class Ice_block(Platform):
	def __init__(self, xpos, ypos):
		self.hitbox = Rect(xpos, ypos, 50, 50)
		super().__init__(xpos, ypos)
		self.type = "Ice"
		self.velChange = Vector2 (10,0)
	def draw(self):
		pygame.draw.rect(screen, (0, 0, 105), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))

#Walls
class map_bound_walls(Platform):
	def __init__(self, xpos, ypos):
		self.hitbox = Rect(xpos, ypos, 30, 100)
		super().__init__(xpos, ypos)
		self.type = "normal"
	def draw(self):
		pygame.draw.rect(screen, (90, 50, 20), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
		
	def returnType(self):
		return self.type
	
class goal(Platform):
	def __init__(self, xpos, ypos):
		super().__init__(xpos, ypos)
		self.hitbox = Rect(xpos, ypos, 50, 50)
		self.type = 'Goal'
	
	def draw(self):
		pygame.draw.rect(screen, (255,0,0), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))

class water(Platform):
	def __init__(self, xpos, ypos):
		self.type = 'Water'
		self.hitbox = Rect(xpos,ypos, 50, 50)
		super().__init__(xpos, ypos)

	def draw(self):
		pygame.draw.rect(screen, (0,255,255), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))


class Breakblock(Platform):
	def __init__(self, xpos, ypos):
		self.hitbox = Rect(xpos, ypos, 50,50)
		super().__init__(xpos, ypos)
		self.type = "break"
	
	def draw(self):
		pygame.draw.rect(screen, (255,0,255), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))

class Sidetramp(Platform):
	def __init__(self, xpos, ypos):
		self.hitbox = Rect(xpos, ypos, 50, 50)
		super().__init__(xpos, ypos)
		self.type = "sideT"
	
	def draw(self):
		pygame.draw.rect(screen, (255,255,255), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))