import pygame
from random import randrange as rr
import math
from pygame.math import Vector2

screen = pygame.display.set_mode((800, 800))  # creates game screen

global plat
plat = 0

class platform():
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
        self.type = "normal"

    def draw(self):
        pygame.draw.rect(screen, (100, 50, 100), (self.pos.x, self.pos.y, 80, 30))
    
    def move(self):
        pass
    def collide(self):
        return self.type

class mblock(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
        self.startx = self.pos.x
        self.starty = self.pos.y
        self.direction = 1
        self.type = "Moveblock"
    def collision(self):
        return self.type

class trampoline(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
        self.type = "trampoline"
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, 80, 30))
    def move(self):
        pass
    def collision(self):
        return self.type
        
class ice_block(platform):
    def __init__(self, xpos, ypos):
        self.pos = Vector2(xpos, ypos)
        self.type = "Ice"
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 105), (self.pos.x, self.pos.y, 80, 30))
    def move(self):
        pass
    def collision(self):
        return self.type
    