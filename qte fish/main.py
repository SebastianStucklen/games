import pygame
from pygame import Vector2
from globals import FPS, SCREEN_SIZE
from player import Player
from minigame import FishingHole
from fishgen import fishgen
pygame.init()

doExit = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_SIZE))

guy = Player(1)
lake = FishingHole()
deltalist = []
while not doExit:
	delta = clock.tick(FPS) / 1000
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			doExit = True #lets you quit parogram
	screen.fill((0, 0, 0))
	lake.draw(screen)
	if lake.quicktime(screen,delta):
		guy.inventory.append(fishgen())
		print(guy.inventory)
	# print(lake.inputs())
	guy.update(delta,screen)
	pygame.display.flip()
pygame.quit()