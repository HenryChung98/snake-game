import pygame

# screen width, height
screen_width = 500
screen_height = 500

# for collision detection
scale = 10


# colors
background = (23, 32, 42)
snake_head = (247, 220, 111)
snake_color = (236, 240, 241)
food_color = (148, 49, 38)

# to handle events, draw graphics, and manage the display within the window.
display = pygame.display.set_mode((screen_width, screen_height))