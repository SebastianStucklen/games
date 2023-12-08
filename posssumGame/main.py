import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from BETTERSPRITE import Possum
import time
#from random import randrange as rr

#Platforms
from platforms import Platform
from platforms import Trampoline
from platforms import Ice_block
from platforms import Floor
from platforms import spike
from platforms import goal
from platforms import water
from platforms import Sidetramp
from platforms import topSpike


#Enemies
from enemies import Dog
from enemies import Horse
from enemies import Fox
from enemies import Eagle

import levels.maps




pygame.init() 
pygame.mixer.init()
ouch = pygame.mixer.Sound("resources/ouwie.mp3")
haha = pygame.mixer.Sound("resources/haha.mp3")
loser = pygame.image.load("resources/lose.jpg")
loser = pygame.transform.smoothscale_by(loser,0.5)
WIDTH = 1600
HEIGHT = 900

pygame.display.set_caption("platformer")  # sets the window title
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#map1: 1 is grass
Map = levels.maps.room_four

tramp = Trampoline(100, 100)

character = Possum()

plats1 = []

for i in range(len(Map)):
	plats1.append([])


platNum = 0
whatPlat = 0
#floor = Floor(100,800)
width = 0

#plats.append(mblock(rr(0,700), rr(100,600)))
#plats.append(platform(rr(0,700), rr(100,600)))
#plats.append(ice_block(rr(0,700), rr(100,600)))

#GROUND
#for i in range(800//50):
#	plats.append(floor(-50+50*(i+1),750))

for i in range (len(Map)):
		for j in range(len(Map[i])):
			if Map[i][j]!=0:
				if Map[i][j] == 5:
					plats1[i].append(spike(j*50,(i*50)))
					ouch.play()
					ouch.stop()
				elif Map[i][j] == 4:
					plats1[i].append(goal(i*50, j*50))
				elif Map[i][j] == 3:
					plats1[i].append(Trampoline(j*50, i*50))
				elif Map[i][j] == 2:
					plats1[i].append(Ice_block(j*50, i*50))
				elif Map[i][j] == 6:
					plats1[i].append(water(j*50, i*50))
				elif Map[i][j] == 8:
					plats1[i].append(Sidetramp(j*50, i*50))
				elif Map[i][j] == 7:
					plats1[i].append(topSpike(j*50, i*50))
				else:
					plats1[i].append(Floor(j*50,i*50))
				#map(lambda x:Floor(i*50,j*50) if x== 0 else x,plats)
			else:
				plats1[i].append(0)
			if Map[i][j] != 0:
				platNum +=1
			width = len(Map[i])

character.getSpawn(width,len(Map))
	


character.getPlatty(platNum)

#eagle = Eagle(100,100)
dog = Dog(100, 100)
horse = Horse(0,0) 
fox = Fox(0, 0)
eagle = Eagle(0,0)

eagle.getPlatty(platNum)
dog.getPlatty(platNum)
horse.getPlatty(platNum)
fox.getPlatty(platNum)

#PLACE HOLDER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


while not gameover:
	
	print(character.health)
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover = True
	
	keys = pygame.key.get_pressed()


	character.update(3) #update hitbox
	dog.update(0,1000000)

	for i in range (len(Map)):
		for j in range(len(Map[i])):
			if Map[i][j]!=0:
				character.collision(plats1[i][j].hitbox, plats1[i][j].type,whatPlat)
				dog.collision(plats1[i][j].hitbox, plats1[i][j].type,whatPlat)
				whatPlat+=1
	whatPlat = 0
	character.gouds()
	
	character.update(0) #ground, gravity, etc
	
	character.getKeyPressed() #get keystrokes
	dog.movement()

 
	character.update(3) 
	character.actions() #actions



	character.update(1) # add vel to pos
	dog.update(1,1000000)


	
	screen.fill((0,19,23))
	#dog.draw()
	#horse.draw()
	#fox.draw()
	#Trampoline.draw()
	
	
	#for i in range(len(plats1)):
	#	plats1[i].returnType()
	

	#pygame.draw.line(screen, (180,190,180),(0,ground.y),(800,ground.y),1)
	for i in range (len(Map)):
		for j in range(len(Map[i])):
			if Map[i][j]!=0:
				if Map[i][j] == 7:
					plats1[i][j].updatePos(j*50+character.offset.x, (i*50+character.offset.y))
				else:
					plats1[i][j].updatePos(j*50+character.offset.x, i*50+character.offset.y)
				if plats1[i][j].hitbox.left < 1650 and plats1[i][j].hitbox.right > -50 and plats1[i][j].hitbox.bottom > -50 and plats1[i][j].hitbox.top < 950:
					plats1[i][j].draw()

	#for i in range (16):
	#	for j in range(42):
	#		if map1[i][j]==2:
	#			screen.blit(plats[i].Trampoline, (j*50+character.offset, i*50), (0, 0, 50, 50))
	character.draw()#drawing
	if character.health <= 0.1:
		haha.play()
		screen.blit(loser, (0,0))
		character.pos.y = -1000
	pygame.display.flip()


pygame.quit()

