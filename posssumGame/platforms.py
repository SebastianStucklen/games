import pygame
from random import randrange as rr
import math
from pygame.math import Vector2
from pygame.rect import Rect

screen = pygame.display.set_mode((800, 800))  # creates game screen

global plat
plat = 0

class Platform():
    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 0, 0)
        self.type = "normal"
        self.velChange = Vector2 (10,0)
        self.flooroffset = 0
    def draw(self):
        pygame.draw.rect(screen, (100, 50, 100), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
    
    def move(self):
        pass
    def returnType(self):
        return self.type
    
    def updatePos(self,x,y):
        self.hitbox.update(x,y,self.hitbox.width,self.hitbox.height)

class Floor(Platform):
    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 50, 50)
        self.type = "normal"
        self.dirt = pygame.image.load('resources/grass.jpg')
        self.dirt2 = pygame.transform.smoothscale(self.dirt,(50,50))
        self.floors = []
    
    def draw(self):
        
        #pygame.draw.rect(screen, (180,190,180), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
        screen.blit(self.dirt2, self.hitbox)


class Mblock(Platform):
    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 100, 30)
        self.startx = xpos
        self.starty = ypos
        self.direction = 1
        self.type = "Moveblock"
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))


class Trampoline(Platform):
    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 100, 30)
        self.type = "trampoline"
        self.velChange = Vector2 (0,10)
        
        
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
        
class Ice_block(Platform):
    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 100, 100)
        self.type = "Ice"
        self.velChange = Vector2 (10,0)
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 105), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
    
