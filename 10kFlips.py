import random
import pygame
from pygame import draw
pygame.init()
screen = pygame.display.mode((500,500))
pygame.display.caption("10 thousand flips")

heads = 0
tails = 0

for i in range(10000):
    screen.fill(0,0,0)
    coin = random.random()
    if coin <= 0.5:
        heads += 1
        draw.rect(screen, (255,110,0), (120, 500, 50, heads/20))
    if coin > 0.5:
        tails += 1
        draw.rect(screen, (0,110,255), (380, 500, 50, tails/20))
    print("Flips[ ", i, " ], ", "Heads[ ", heads, " ], ", "Tails[ ", tails, " ]")

print("Percent of heads: ", heads/10000)
print("Percent of tails: ", tails/10000)

