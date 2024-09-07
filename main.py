import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
screen_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
screen.fill(screen_color)

pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/cartoon-weapon.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")

count = 0
complexity = 1

running = True

while running:
    pass

pygame.quit()