import pygame
from random import randrange as rr
import math
from pygame.math import Vector2
from pygame.rect import Rect

screen = pygame.display.set_mode((800, 800))  # creates game screen

global plat
plat = 0

class platform():
    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 0, 0)
        self.type = "normal"
        self.velChange = Vector2 (10,0)
    def draw(self):
        pygame.draw.rect(screen, (100, 50, 100), (self.hitbox.left, self.hitbox.top, 80, 30))
    
    def move(self):
        pass
    def collision(self):
        return self.type

class mblock(platform):
    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 20, 50)
        self.startx = xpos
        self.starty = ypos
        self.direction = 1
        self.type = "Moveblock"
    def collision(self):
        return self.type

class trampoline(platform):
    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 20, 50)
        self.type = "trampoline"
        self.velChange = Vector2 (0,10)
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.hitbox.left, self.hitbox.top, 80, 30))
    def move(self):
        pass
    def collision(self):
        return self.type
        
class ice_block(platform):
    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 20, 50)
        self.type = "Ice"
        self.velChange = Vector2 (10,0)
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 105), (self.hitbox.left, self.hitbox.top, 80, 30))
    def move(self):
        pass
    def collision(self):
        return self.type
    