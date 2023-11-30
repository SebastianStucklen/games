import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from BETTERSPRITE import Possum

from platforms import Platform
from platforms import Trampoline
from platforms import Mblock
from platforms import Ice_block
from platforms import Floor

from enemies import Dog
from enemies import Horse
from enemies import Fox
from enemies import Eagle

import levels.maps

from random import randrange as rr


pygame.init() 
pygame.mixer.init()

WIDTH = 800
HEIGHT = 800

pygame.display.set_caption("platformer")  # sets the window title
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#map1: 1 is grass
map1 = levels.maps.room_one

tramp = Trampoline(100, 100)

character = Possum()

plats1 = [[],
	   [],
	   [],
	   [],
	   [],
	   [],
	   [],
	   [],
	   [],
	   [],
	   [],
	   [],
	   [],
	   [],
	   [],
	   []]
class dumb:
	def __init__(self):
		self.hitbox = Rect(0, 0, 0, 0)
		self.type = "normal"
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


platNum = 0
whatPlat = 0
#floor = Floor(100,800)


#plats.append(mblock(rr(0,700), rr(100,600)))
#plats.append(platform(rr(0,700), rr(100,600)))
#plats.append(ice_block(rr(0,700), rr(100,600)))

#GROUND
#for i in range(800//50):
#	plats.append(floor(-50+50*(i+1),750))

for i in range (16):
		for j in range(42):
			if map1[i][j]!=0:
				plats1[i].append(Floor(i*50,j*50))
				#map(lambda x:Floor(i*50,j*50) if x== 0 else x,plats)
			else:
				plats1[i].append(0)
			if map1[i][j] != 0:
				platNum +=1

character.getPlatty(platNum)


#eagle = Eagle(100,100)
dog = Dog(100, 100)
horse = Horse(0,0) 
fox = Fox(0, 0)


#PLACE HOLDER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



while not gameover:


	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover = False
	
	keys = pygame.key.get_pressed()

	character.update(3) #update hitbox
	for i in range (16):
		for j in range(42):
			if map1[i][j]!=0:
				character.collision(plats1[i][j].hitbox, plats1[i][j].type,whatPlat)
				whatPlat+=1
	whatPlat = 0

	character.update(0) #ground, gravity, etc
	
	character.getKeyPressed() #get keystrokes

	#character.playerInput() #connects keystrokes and actions
 
	character.actions() #actions

	character.update(1) # add vel to pos

	character.update(3)
	
	screen.fill((0,0,0))
	#dog.draw()
	#horse.draw()
	#fox.draw()
	#Trampoline.draw()

	
	#for i in range(len(plats)):
	#	plats[i].returnType()
	

	#pygame.draw.line(screen, (180,190,180),(0,ground.y),(800,ground.y),1)
	for i in range (16):
		for j in range(42):
			if map1[i][j]!=0:
				plats1[i][j].updatePos(j*50+character.offset, i*50)
				plats1[i][j].draw()


	#for i in range (16):
	#	for j in range(42):
	#		if map1[i][j]==2:
	#			screen.blit(plats[i].Trampoline, (j*50+character.offset, i*50), (0, 0, 50, 50))
	character.draw()#drawing
	pygame.display.flip()

pygame.quit()