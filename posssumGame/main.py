import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from BETTERSPRITE import Possum
from platforms import platform
from platforms import trampoline
from platforms import mblock

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
global plat

#PLACE HOLDER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
global ground
ground = Vector2(0,700)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

while not gameover:

	clock.tick(60)

	character.update(3) #update hitbox

	character.collision(ground, "normal") #collision

	character.update(0) #ground, gravity, etc

	character.getKeyPressed() #get keystrokes

	character.playerInput() #connects keystrokes and actions
 
	character.actions() #actions

	character.update(1) # add vel to pos
	
    
	screen.fill((200,210,200))
	character.draw()#drawing
	pygame.draw.line(screen, (180,190,180),(0,ground.y),(800,ground.y),1)
	pygame.display.flip()

pygame.quit()