import pygame
from random import randrange as rr
import math
from pygame.math import Vector2
from pygame.rect import Rect


screen = pygame.display.set_mode((1600, 800))  # creates game screen

_floorsprite = pygame.image.load('resources/grass.jpg')
_floorsprite = pygame.transform.smoothscale(_floorsprite,(50,50))
_spawnsprite = pygame.image.load('resources/placeholder.png')
_spawnsprite = pygame.transform.smoothscale(_spawnsprite,(50,50))

global plat
plat = 0

class Platform:
    image: pygame.Surface
    hitbox: Rect
    type: str
    velChange: Vector2
    flooroffset: int

    def __init__(self, xpos, ypos):
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

class spawn(Platform):
    image = _spawnsprite

    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 50, 50)
        self.type = "normal"
    
    def draw(self):
        
        #pygame.draw.rect(screen, (180,190,180), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
        screen.blit(self.image, self.hitbox)
class Floor(Platform):
    image = _floorsprite

    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 50, 50)
        self.type = "normal"
        self.floors = []
    
    def draw(self):
        
        #pygame.draw.rect(screen, (180,190,180), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
        screen.blit(self.image, self.hitbox)


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

#Walls
class map_bound_walls(Platform):
    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 30, 100)
        self.type = "normal"
    def draw(self):
        pygame.draw.rect(screen, (90, 50, 20), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
        
    def returnType(self):
        return self.type
    
class goal(Platform):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos)
        self.hitbox = Rect(xpos, ypos, 50, 50)
        self.type = 'goal'
    
    def draw(self):
        pygame.draw.rect(screen, (255,0,0), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))

