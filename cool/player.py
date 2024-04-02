import pygame
from pygame.math import Vector2
import math
from pygame import Rect
pygame.init()

#screensize = pygame.display.get_window_size()

class Player:

	def __init__(self):
		self.pos = Vector2(0,0)
		self.rel = Vector2(0,0)
		self.vel = Vector2(0,0)
		self.centerpos = Vector2(0,0)
		self.image = pygame.image.load('resources/placeholder.png')
		self.transformed_image = pygame.transform.rotate(self.image, 0)
		self.offset = Vector2(self.image.get_rect().topleft) - Vector2(self.image.get_rect().midtop)

		self.newMousePos = Vector2(0,0)
		self.oldMousePos = Vector2(0,0)

		self.correctionangle = 90

		self.mouseVels: list[Vector2] = []

	def atan2(self, y, x):
		num = math.atan2(y, x) * (180/math.pi)
		if num > 0:
			return num
		else:
			return 180 + (180 - abs(num))
		
	def mouseMove(self,delta):
		self.newMousePos = Vector2(pygame.mouse.get_pos())

		rel = (self.newMousePos - self.oldMousePos) / delta
		if len(self.mouseVels) < 8:
			self.mouseVels.append(rel)
		else:
			self.mouseVels.pop(0)
			self.mouseVels.append(rel)
		
		avgVel = Vector2(0, 0)
		for vel in self.mouseVels:
			avgVel += vel
		avgVel /= len(self.mouseVels)
		self.oldMousePos = self.newMousePos
		return avgVel


	def update(self,delta: float):
		
		self.vel = self.mouseMove(delta)
		
		self.pos += self.vel * delta 
		self.centerpos.x = self.newMousePos.x
		self.centerpos.y = self.newMousePos.y

		#self.draw()

		
	#def draw(self):
#
	#	angle = math.degrees(math.atan2(-self.vel.y,self.vel.x)) - self.correctionangle
	#	
	#	if abs(self.vel.x) > 1 and abs(self.vel.y) > 1:
	#		self.transformed_image = pygame.transform.rotate(self.image, angle)
	#	
	#	screen.blit(self.transformed_image, self.newMousePos)
	#	#pygame.draw.circle(screen, (255,255,240),self.pos,50)


#guy = Player()
#clock = pygame.time.Clock()
#bye = False
#
#while bye == False:
#	delta = clock.tick(60) / 1000
#	screen.fill((0,0,0))
#	for event in pygame.event.get():
#			if event.type == pygame.QUIT:
#				bye = True
#
#	guy.update(delta)
#
#
#	pygame.display.flip()
#
#pygame.quit()