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

# Определяем кнопки
button_width, button_height = 15, 15
increase_button = pygame.Rect(181, 33, button_width, button_height)
decrease_button = pygame.Rect(135, 33, button_width, button_height)

def draw_button(rect, text):
    pygame.draw.rect(screen, "GRAY", rect)
    text_surf = font.render(text, True, "BLACK")
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

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
            elif increase_button.collidepoint(event.pos):
                complexity += 1
            elif decrease_button.collidepoint(event.pos):
                complexity -= 1
    font = pygame.font.SysFont('couriernew', 20)
    text = font.render("Счет: "+str(count), True, "black")
    screen.blit(text, (10, 10))
    screen.blit(target_img, (target_x, target_y))

    # Рисуем кнопки
    draw_button(increase_button, "+")
    draw_button(decrease_button, "-")

    # Отображаем текущее значение счетчика
    text2 = font.render(f"Сложность:  {complexity}", True, "black")
    screen.blit(text2, (10, 30))

    pygame.display.update()


pygame.quit()