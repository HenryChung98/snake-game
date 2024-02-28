import random
import pygame
from variables import *


class Food:
    def __init__(self, food_x, food_y, score):
        self.x = food_x
        self.y = food_y
        self.score = score
    def new_location(self):

        self.x = random.randrange(1, screen_width - scale)
        self.y = random.randrange(1, screen_height - scale)
    
    def show(self):
        pygame.draw.rect(display, food_color, (self.x, self.y, scale, scale))
