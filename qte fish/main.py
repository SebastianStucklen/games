import pygame
from pygame import Vector2
from globals import FPS, SCREEN_SIZE, interact, TextDisplay
from player import Player
from interactables import FishingHole
from fishgen import fishgen
pygame.init()

doExit = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_SIZE))

guy = Player(1)
lake = FishingHole()
deltalist = []
inv = TextDisplay(guy.inventory,5,5,32)
while not doExit:
	delta = clock.tick(FPS) / 1000
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			doExit = True #lets you quit parogram
	screen.fill((0, 0, 0))
	lake.draw(screen)
	if lake.collide(guy.centerpos) and interact():
		fish = fishgen()
		print(fish)
		if lake.quicktime(screen,delta,fish[1]):
			guy.inventory.append(fish[0])
			print(guy.inventory)
	guy.update(delta,screen)
	
	inv.update(screen,guy.inventory,32)
	pygame.display.flip()
pygame.quit()