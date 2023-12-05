import pygame
from random import randrange as rr
import math
from pygame.math import Vector2
from pygame.rect import Rect
import levels.maps

room_one_settings = {
    'current room': levels.maps.room_one,
    'spawn_coords': Vector2(0, 0)
}

room_two_settings = {
    'current room': levels.maps.room_one,
    'spawn_coords': Vector2(0, 0)
}
room_three_settings = {
    'current room': levels.maps.room_one,
    'spawn_coords': Vector2(0, 0)
}