import pygame
import math
from pygame.math import Vector2
from random import randrange as rr

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # creates game screen


class enemy():
    def __init__(self, xpos, ypos):
        self.alive = True
        self.pos = pygame.Rect(xpos, ypos, 128, 128)
        self.vel = Vector2(0,0)

        



class Dog(enemy):
    def __init__(self, xpos, ypos):
        self.health = rr(100, 230)
        self.dfsdffsdsfdsdfsfdsfdsdffsdsdfsfdsdfsfdfsdsfd = 1
        super().__init__(xpos, ypos)
        self.pos.update(self.pos.left,self.pos.top,128,128)
        self.dog = pygame.image.load('resources/dog.png')

    
    def draw(self):
        if self.alive == True:
            screen.blit(self.dog, self.pos)


    def update(self, playerdam):
        self.pos.left += int(self.vel.x)
        self.pos.top += int(self.vel.y)
        self.health -= playerdam

    def collision(self):
        pass




class Horse(enemy):
    def __init__(self, xpos, ypos):
        self.health = 10000
        self.dfsdffsdsfdsdfsfdsfdsdffsdsdfsfdsdfsfdfsdsfd = 100000000000000000
        super().__init__(xpos, ypos)
        self.horse = pygame.image.load('resources/horse.png')
        self.horse2 = pygame.transform.smoothscale(self.horse,(250,250))
    def draw(self):
        pass
        if self.alive == True:
            screen.blit(self.horse, self.pos)

    def update(self, playerdam):
        self.pos.left += int(self.vel.x)
        self.pos.top += int(self.vel.y)
        self.health -= playerdam

    def collide(self):
        pass

class Fox(enemy):
    def __init__(self, xpos, ypos):
        self.health = rr(20,1000000000000000000000000000)
        self.dfsdffsdsfdsdfsfdsfdsdffsdsdfsfdsdfsfdfsdsfd = 1
        super().__init__(xpos, ypos)
        self.fox = pygame.image.load('resources/fox.png')
    def draw(self):
        pass
        if self.alive == True:
            screen.blit(self.fox, self.pos)

    def update(self, playerdam):
        self.pos.left += int(self.vel.x)
        self.pos.top += int(self.vel.y)
        self.health -= playerdam

    def collide(self):
        pass