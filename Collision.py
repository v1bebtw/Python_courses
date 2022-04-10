import pygame as pg
import sys


pg.init()

FPS = 120
window_width = 600
window_height = 400

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

r = 50
width_rect = 150
height_rect = 100

width_rect1 = 150
height_rect1 = 100

x, y = 300, 200
direct_x = 1
direct_y = 1

x1, y1 = 100, 200
direct_x1 = 1
direct_y1 = 1

x_rect = window_width // 2 - width_rect // 2
y_rect = window_height // 2 - height_rect // 2

x_rect1 = window_width // 2 - width_rect // 2 + 160
y_rect1 = window_height // 2 - height_rect // 2

screen = pg.display.set_mode((window_width, window_height))
clock = pg.time.Clock()

count_of_collision = 0

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            """Запись количества стокновений в файл"""
            with open('scores.txt', 'w', encoding='utf-8') as score:
                score.write(f'Количество столкновений: {count_of_collision}')
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                x_rect -= direct_x
            elif i.key == pg.K_RIGHT:
                x_rect += direct_x
            elif i.key == pg.K_UP:
                y_rect -= direct_y
            elif i.key == pg.K_DOWN:
                y_rect += direct_y


    clock.tick(FPS)
    screen.fill(white)

    # ball_1 = pg.draw.circle(screen, red, (x, y), r)
    # ball_2 = pg.draw.circle(screen, black, (x1, y1), r)

    """Столкновение прямоугольников по OX"""
    pg.draw.rect(screen, red, (x_rect, y_rect, width_rect, height_rect))
    pg.draw.rect(screen, black, (x_rect1, y_rect1, width_rect, height_rect))

    x_rect += direct_x
    if x_rect >= window_width - width_rect  or x_rect < 0:
        direct_x = -direct_x

    x_rect1 += -direct_x1
    if x_rect1 >= window_width - width_rect1 or x_rect1 < 0:
        direct_x1 = -direct_x1

    if x_rect1 == x_rect + width_rect:
        direct_x = -direct_x
        direct_x1 = -direct_x1
        count_of_collision += 1
        print(f'Количество столкновений: {count_of_collision}')

    """Перемещение с клавиатуры"""
    # pg.draw.rect(screen, red, (x_rect, y_rect, width_rect, height_rect))

    pg.display.update()


