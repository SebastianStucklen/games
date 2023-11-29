import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from BETTERSPRITE import Possum
from platforms import platform
from platforms import trampoline
from platforms import mblock
from platforms import ice_block
from platforms import floor
from enemies import Dog
from enemies import Horse
from enemies import Fox
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

character = Possum()

plats = []


plats.append(trampoline(rr(0,700), rr(100,600)))
plats.append(mblock(rr(0,700), rr(100,600)))
#plats.append(platform(rr(0,700), rr(100,600)))
plats.append(ice_block(rr(0,700), rr(100,600)))

#GROUND

plats.append(floor(-500, 700))

platpos = []

for i in range(len(plats)):
	platpos.append(plats[i].returnPos())


dog = Dog(100, 100)
horse = Horse(0,0) 
fox = Fox(0, 0)
global plat

#PLACE HOLDER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
global ground
ground = Rect(-500,700,1000,1000)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#MAP: 1 is grass
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0 ,0 ,0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0 ,0 ,2, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2 ,2 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0 ,2 ,0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0],
	   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1, 1]]

#dirt = pygame.image.load('resources/grass.png') #load your spritesheet

while not gameover:


	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover = False
	
	keys = pygame.key.get_pressed()

	character.update(3) #update hitbox
	
	for i in range(len(plats)):
		character.collision(plats[i].returnPos(), plats[i].returnType())
	

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
	#trampoline.draw()

	for i in range(len(plats)):
		plats[i].draw()
	
	for i in range(len(plats)):
		plats[i].returnType()
	
	character.draw()#drawing
	

	#pygame.draw.line(screen, (180,190,180),(0,ground.y),(800,ground.y),1)
	#for i in range (16):
	   #   for j in range(42):
	   #          if map[i][j]==1:
	   #                 screen.blit(dirt, (j*50+character.offset, i*50), (0, 0, 50, 50))
	pygame.display.flip()

pygame.quit()