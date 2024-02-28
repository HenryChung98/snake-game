import pygame
import sys
import time
from snake_class import Snake
from food_class import Food
from variables import *



def show_score():
    
    # create font(font, font-size)
    font = pygame.font.SysFont("Copperplate Gothic Bold", 30)
    
    # render font(text, anti-aliasing enabled, color)
    text = font.render("Score: " + str(food.score), True, (255, 255, 255))
    
    # draw text surface(text, (pos.x, pos.y))
    display.blit(text, (10, 10))


def show_best_score(b_score):
    font = pygame.font.SysFont("Copperplate Gothic Bold", 30)
    text = font.render("Best Score: " + str(b_score), True, (255, 255, 255))
    display.blit(text, (10, 30))


def game_over(b_score):
    font = pygame.font.SysFont("Copperplate Gothic Bold", 50)
    text = font.render("Game Over", True, (255, 255, 255))
    text_width, text_height = text.get_size()
    display.blit(text, (screen_width / 2 - (text_width / 2), screen_height / 2 - (text_height / 2)))
    
    # best score
    if int(b_score) < food.score:
        with open('best-score.txt', 'w') as file:
            file.write(str(food.score))


    #update the contents of the entire display
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()
    
pygame.init()

pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock() # similar to delta time
    
# create snake object
snake = Snake(screen_width / 2, screen_height / 2)

# create food object
food = Food(screen_width / 2, screen_height / 4, 0)
    

def gameLoop():
    running = True
    game_speed = 15
    is_increase = False
    best_score = 0

    while running:

        # best score
        try:
            with open('best-score.txt', 'r') as file:
                best_score = int(file.read())
        except:
            with open('best-score.txt', 'w') as file:
                file.write("0")

        # keydown event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP:
                    if not(snake.x_dir == 0 and snake.y_dir == 1):
                        snake.x_dir = 0
                        snake.y_dir = -1
                        
                if event.key == pygame.K_DOWN:
                    if not(snake.x_dir == 0 and snake.y_dir == -1):
                        snake.x_dir = 0
                        snake.y_dir = 1
                        
                if event.key == pygame.K_LEFT:
                    if not(snake.x_dir == 1 and snake.y_dir == 0):
                        snake.x_dir = -1
                        snake.y_dir = 0
                    
                if event.key == pygame.K_RIGHT:
                    if not(snake.x_dir == -1 and snake.y_dir == 0):
                        snake.x_dir = 1
                        snake.y_dir = 0
                
        # clear the surface
        display.fill(background)
        
        # show score
        show_score()
        show_best_score(best_score)
        # show objects
        snake.show()
        food.show()
        snake.update()
        
        # ---collision detection---
        
        # food
        if abs(snake.body[0][0] - food.x) < scale and abs(snake.body[0][1] - food.y) < scale:
            food.new_location()
            snake.grow()
            food.score +=  1
            if food.score % 5 == 0:
                is_increase = True
        
        # wall
        if snake.body[0][0] < -10 or snake.body[0][1] < -10:
            game_over(best_score)
        if snake.body[0][0] > screen_width or snake.body[0][1] > screen_height:
            game_over(best_score)
        
        
        # body
        
        if snake.death():
            game_over(best_score)
        
        # ---collision detection---
        
        # difficulty
        if is_increase == True and food.score % 5 == 0:
            game_speed += 5
            is_increase = False

        # update screen
        pygame.display.update()

        # 10frames per a second
        clock.tick(game_speed)
        
        
gameLoop()
    
