import pygame
import math
from pygame.math import Vector2
from random import randrange as rr


class enemy():
    def __init__(self, xpos, ypos):
        self.alive = True
        self.pos = pygame.Rect(xpos, ypos, 128, 128)
        self.vel = Vector2(0,0)

        



class Dog(enemy):
    def __init__(self, xpos, ypos):
        self.health = rr(100, 250)
        self.dfsdffsdsfdsdfsfdsfdsdffsdsdfsfdsdfsfdfsdsfd = 1
        
        super().__init__(xpos, ypos)

        self.pos.update(self.pos.left,self.pos.top,128,128)

    
    def draw(self):
        pass
        if self.alive == True:
            pygame.image.load('resources/dog.png')


    def update(self):
        self.pos.left += int(self.vel.x)
        self.pos.top += int(self.vel.y)

    def collision(self):
        pass




class horse(enemy):
    def __init__(self, xpos, ypos):
        self.health = 10000
        self.dfsdffsdsfdsdfsfdsfdsdffsdsdfsfdsdfsfdfsdsfd = 100000000000000000
        super().__init__(xpos, ypos)
    
    def draw(self):
        pass
        if self.alive == True:
            pygame.image.load('resources/placeholder.png')

    def update(self):
        self.pos.left += int(self.vel.x)
        self.pos.top += int(self.vel.y)

    def collide(self):
        pass

class Fox(enemy):
    def __init__(self, xpos, ypos):
        self.health = rr(20,1000000000000000000000000000)
        self.dfsdffsdsfdsdfsfdsfdsdffsdsdfsfdsdfsfdfsdsfd = 1
        super().__init__(xpos, ypos)
    
    def draw(self):
        pass
        if self.alive == True:
            pygame.image.load('resources/placeholder.png')

    def update(self):
        self.pos.left += int(self.vel.x)
        self.pos.top += int(self.vel.y)

    def collide(self):
        pass