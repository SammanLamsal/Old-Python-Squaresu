#imports
import pygame
import random
import sys
from pygame.locals import *

pygame.init()

#variables

width = 800
height = 600

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
background_color = (0, 0, 0)
myFont = pygame.font.SysFont("monospace", 35)

speed = 3
score = 0  

asteroid_size = 50
astrd = pygame.Rect(random.randint(0, width - asteroid_size), 0, asteroid_size, asteroid_size)
asteroid_list = [astrd]

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
game_over = False

# functions
def set_level(score, speed):
    if score <= 5:
        speed = 3
    elif score <= 15:
        speed = 5
    elif score <= 25:
        speed = 7
    elif score <= 35:
        speed = 9
    elif score <= 45:
        speed = 11
    elif score <= 50:
        speed = 13
    elif score <= 60:
        speed = 15
    elif score <= 70:
        speed = 20
    return speed

def update_asteroid_pos(asteroid_list):
    for idx, asteroid in enumerate(asteroid_list):
        if 0 <= asteroid.y < height:
            asteroid.y += speed
        else:
            asteroid_list.pop(idx)


def draw_asteroids(asteroid_list):
    for asteroid in asteroid_list:
        pygame.draw.rect(screen, blue, asteroid)


#while loop running part
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for asteroid in asteroid_list:
                if asteroid.collidepoint(mouse_pos):
                    score += 1
                    asteroid_list.pop(asteroid_list.index(asteroid))
                    asteroid_list.append(pygame.Rect(random.randint(0, width - asteroid_size), 0, asteroid_size, asteroid_size))

        if astrd.y == height:
            game_over = True

    update_asteroid_pos(asteroid_list)
    screen.fill(background_color)

    speed = set_level(score, speed)

    text = "Score: " + str(score)
    label = myFont.render(text, 1, green)
    screen.blit(label, (width - 200, height - 40))

    draw_asteroids(asteroid_list)

    clock.tick(30)
    pygame.display.update()
