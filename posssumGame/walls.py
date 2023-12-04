import pygame
from random import randrange as rr
import math
from pygame.math import Vector2
from pygame.rect import Rect

screen = pygame.display.set_mode((1600, 800))

class wall():
    image: pygame.Surface

    def __init__(self, xpos, ypos):
        self.hitbox = Rect(xpos, ypos, 0, 0)
        self.type = "normal"
        self.velChange = Vector2 (0,0)
    def draw(self):
        pygame.draw.rect(screen, (100, 50, 100), (self.hitbox.left, self.hitbox.top, self.hitbox.width, self.hitbox.height))
    
    def returnType(self):
        return self.type
    
    def updatePos(self,x,y):
        self.hitbox.update(x,y,self.hitbox.width,self.hitbox.height)
    

    