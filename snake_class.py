import pygame
import copy
from variables import *



class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = 10
        self.h = 10
        self.x_dir = 0
        self.y_dir = 0
        self.body = [[self.x, self.y]]
        self.length = 1
        
    def reset(self):
        self.x = width / 2 - scale
        self.y = height / 2 - scale
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.body = [[self.x, self.y]]
        self.length = 1
    
    def show(self):
        for i in range(self.length):
            if i != 0:
                # Surface, color, rect, width, height
                pygame.draw.rect(display, snake_color,
                                 (self.body[i][0], self.body[i][1], self.w, self.h))
            else:
                # snake head
                pygame.draw.rect(display, snake_head,
                                 (self.body[i][0], self.body[i][1], self.w, self.h))
    
    
    def grow(self):
        self.length += 1
        self.body.append(self.body[self.length - 2])
    
    def update(self):
        i = self.length - 1
        while i > 0:
            # copy the body object located self.body[i - 1], so it seems like moving when head moves.
            self.body[i] = copy.deepcopy(self.body[i - 1])
            i -= 1
        
        # move the head according to its current direction and scale.
        self.body[0][0] += self.x_dir * scale
        self.body[0][1] += self.y_dir * scale
    
    def death(self):
        if self.length > 2:
            # if head collided to body, dead.
            for i in range(1, self.length - 1):
                if abs(self.body[0][0] - self.body[i][0]) < 1 and abs(self.body[0][1] - self.body[i][1]) < 1:
                    return True
            return False
            