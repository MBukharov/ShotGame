import pygame
import random
import time
import threading

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
screen_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
screen.fill(screen_color)


icon = pygame.image.load("img/cartoon-weapon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Игра тир")

target_img = pygame.image.load("img/target.png")  # мишень
target_width = 80
target_height = 80
target_got = pygame.image.load("img/smile.png")   # картинка после попадания

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGTH-target_height)

count = 0           # количество очков
complexity = 1      # сложность игры

# Определяем кнопки
button_width, button_height = 15, 15
increase_button = pygame.Rect(181, 33, button_width, button_height) # кнопка увеличения сложности
decrease_button = pygame.Rect(135, 33, button_width, button_height) # кнопка уменьшения сложности

def draw_button(rect, text):                # функция отрисовки кнопок
    pygame.draw.rect(screen, "GRAY", rect)
    text_surf = font.render(text, True, "BLACK")
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def move_target():                  # функция смены координат мишени от времени
    global complexity, target_y,target_x
    while True:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGTH - target_height)
        time.sleep((1500-100*complexity)/1000)  # после смены координат делаем паузу в выполнении потока

running = True

font = pygame.font.SysFont('couriernew', 20)  # шрифт для очков

# создаем поток для смены координат мишени
targetmove_thread = threading.Thread(target = move_target,)
targetmove_thread.start()

while running:
    screen.fill(screen_color)
    text = font.render("Счет: " + str(count), True, "black") # отображаем счет
    screen.blit(text, (10, 10))

    # Рисуем кнопки
    draw_button(increase_button, "+")
    draw_button(decrease_button, "-")

    # Отображаем значение сложности
    text2 = font.render(f"Сложность:  {complexity}", True, "black")
    screen.blit(text2, (10, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                screen.blit(target_got, (target_x, target_y)) # если попали, меняем картинку
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(40, SCREEN_HEIGTH - target_height)
                count += 1*complexity   # увеличиваем количество очков в зависимости от сложности
                pygame.display.update()
                pygame.time.delay(300)  # делаем паузу на 300 мс
            elif increase_button.collidepoint(event.pos):   # нажатие кнопки увеличение сложности
                complexity += 1 if complexity < 10 else 0   #
            elif decrease_button.collidepoint(event.pos):   # нажатие кнопки уменьшения сложности
                complexity -= 1 if complexity > 1 else 0


    screen.blit(target_img, (target_x,target_y))
    pygame.display.update()

pygame.quit()