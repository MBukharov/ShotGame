import pygame
import random
import time

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
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGTH-target_height)

count = 0
complexity = 1

running = True

while running:
    screen.fill(screen_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGTH - target_height)
                count += 1
    font = pygame.font.SysFont('couriernew', 20)
    text = font.render("Счет: "+str(count), True, "black")
    screen.blit(text, (10, 10))
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()


pygame.quit()