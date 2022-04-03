import pygame as pg
import sys

pg.init()
FPS = 200
window_width = 600
window_height = 400

width_rect = 200
height_rect = 100

white = (255, 255, 255)
black = (0, 0, 0)
gray = (125, 125, 125)
yellow = (255, 255, 0)
red = (255, 0, 0)

r = 50

x, y = 100, 300
direct_x, direct_y = 1, 1

x1, y1 = 200, 150
direct_x1, direct_y1 = 1, 1

screen = pg.display.set_mode((window_width, window_height))
clock = pg.time.Clock()

pg.display.set_caption('Моя программа')
img = pg.image.load('c++.png')
pg.display.set_icon(img)

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    """Отрисовка прямоугольников"""
    # pg.draw.rect(screen, (255, 0, 20), (window_width // 2 - width_rect // 2, window_height // 2 - height_rect // 2, 200, 100))
    #
    #
    # pg.draw.rect(screen, (100, 200, 20), (window_width // 2 - width_rect // 2, window_height // 2 - height_rect // 2 + 110, 200, 100), 10)

    """Отрисовка линий"""
    # pg.draw.line(screen, white, (0, 0), (600, 400), 10)
    # pg.draw.line(screen, white, (0, 400), (600, 0), 10)

    # pg.draw.aaline(screen, white, (10, 70), (290, 255))

    # Если True, то ломаная замыкается, а если False, то не замыкается
    # pg.draw.lines(screen, white, False, ([10, 10], [140, 70], [240, 12]))

    """Отрисовка кругов"""
    # pg.draw.circle(screen, yellow, (window_width // 2, window_height // 2), r)

    """Отрисовка текста"""
    # font = pg.font.SysFont('tahoma', 32)
    # text = font.render('Привет', True, (255, 0, 0), (50, 100, 20))
    #
    # screen.blit(text, (x, y))

    """Анимация"""
    # clock.tick(FPS)
    # screen.fill(white)
    #
    # pg.draw.circle(screen, black, (x, y), r)
    # pg.draw.circle(screen, red, (x1, y1), r)
    #
    # x += direct_x
    # if x >= window_width - r or x < 0 + r:
    #     direct_x = -direct_x
    #
    # y += direct_y
    # if y >= window_height - r or y < 0 + r:
    #     direct_y = -direct_y
    #
    # x1 += direct_x1
    # if x1 >= window_width - r or x1 < 0 + r:
    #     direct_x1 = -direct_x1
    #
    # y1 += direct_y1
    # if y1 >= window_height - r or y1 < 0 + r:
    #     direct_y1 = -direct_y1

    pg.display.update()


