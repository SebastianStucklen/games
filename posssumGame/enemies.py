import pygame
import math
from pygame.math import Vector2
from random import randrange as rr
from pygame.rect import Rect
WIDTH = 1600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # creates game screen


class enemy():
	def __init__(self, xpos, ypos):
		self.alive = True
		self.hitbox = pygame.Rect(xpos, ypos, 128, 128)
		self.vel = Vector2(0,0)
		self.health = 0
		self.isOnGround = False
		self.platList = []
		self.objPos = Rect(-10000,-10000,-10000,-10000)


	def movement(self):
		pass

	def getPlatty(self,num:int):
		for i in range(num):
			self.platList.append(False)

	def collision(self, objPos:Rect, groundType:str,num:int):

		if self.hitbox.colliderect(objPos):
			self.groundType = groundType
			self.objPos.update(objPos.left, objPos.top, objPos.width, objPos.height)
			self.platList[num] = True
			
		else:
			self.platList[num] = False
	def update(self,type,playerDam):
		groundNum = 0
		if type == 0:
			for i in range(len(self.platList)):
				if self.platList[i] == True:
						groundNum += 1
				if groundNum > 0:
					self.isOnGround = True
				else:
					self.isOnGround = False
			if self.isOnGround == True:

				self.hitbox.bottom = self.objPos.top
				self.vel.y = 0
				self.fastfall = 0

			if self.isOnGround == False:
				self.whatdoing = "jump"
				self.vel.y += 0.4
		if type == 1:
			#self.hitbox.left+=int(self.vel.x) 
			#self.hitbox.bottom+=int(self.vel.y+self.fastfall)
			#self.pos.x += self.vel.x
			self.hitbox.bottom += int(self.vel.y)
			self.hitbox.centerx += int(self.vel.x)
			self.health -= playerDam
			
		
		#if type == 3:
		#	self.hitbox.update(self.pos.x+5, self.pos.y+15, self.frameWidth-5, self.frameHeight-15)
	


class Dog(enemy):
	def __init__(self, xpos, ypos):
		self.health = rr(100, 230)
		self.dfsdffsdsfdsdfsfdsfdsdffsdsdfsfdsdfsfdfsdsfd = 1
		super().__init__(xpos, ypos)
		self.hitbox.update(self.hitbox.left,self.hitbox.top,128,128)
		self.dog = pygame.image.load('resources/dog.png')
		self.offset = Vector2(0,0)
		self.pos = Vector2(0,0)
        #self.dog2 = pygame.transform.smoothscale(self.dog,(200,200))
	
	#def draw(self):
	#	if self.alive == True:
	#		screen.blit(self.dog, self.hitbox,(self.pos.x + self.offset.x, self.pos.y + self.offset.y))

	def movement(self):
		if self.alive == True:
			self.hitbox.centerx += 2
			
    
        

		
			


class Horse(enemy):
	def __init__(self, xpos, ypos):
		self.health = 10000
		self.dfsdffsdsfdsdfsfdsfdsdffsdsdfsfdsdfsfdfsdsfd = 100000000000000000
		super().__init__(xpos, ypos)
		self.horse = pygame.image.load('resources/horse.png')
		self.horse2 = pygame.transform.smoothscale(self.horse,(250,250))
	def draw(self):
		if self.alive == True:
			screen.blit(self.horse, self.hitbox)

class Fox(enemy):
	def __init__(self, xpos, ypos):
		self.health = rr(20,1000000000000000000000000000)
		self.dfsdffsdsfdsdfsfdsfdsdffsdsdfsfdsdfsfdfsdsfd = 1
		super().__init__(xpos, ypos)
		self.fox = pygame.image.load('resources/fox.png')
	def draw(self):
		if self.alive == True:
			screen.blit(self.fox, self.hitbox)

class Eagle(enemy):
	def __init__(self, xpos, ypos):
		self.health = 100
		self.dfsdffsdsfdsdfsfdsfdsdffsdsdfsfdsdfsfdfsdsfd = 1
		self.fox = pygame.image.load('resources/fox.png')
		super().__init__(xpos, ypos)

	def draw(self):
		if self.alive == True:
			screen.blit(self.fox, self.hitbox)

	