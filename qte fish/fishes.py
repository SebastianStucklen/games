import pygame
from pygame import image
from pygame import transform

placeholder = image.load('resources/placeholder.png')


class Fishes:
    def __init__(self):
        self.delta:float
        self.screen: pygame.Surface

        self.baseImg = placeholder
        self.caughtImg = transform.scale_by(self.baseImg,self.size)
        self.inventoryImg = transform.scale_by(self.baseImg,0.2)

        self.size = 1.00 #percent

        self.description = [
            "this is a placeholder fish",
            "if youve caught this something",
            "has gone wrong"
        ]


        