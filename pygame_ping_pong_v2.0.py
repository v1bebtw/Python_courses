import pygame as pg
import sys


pg.init()  # Инициализация

pg.display.set_caption('Ping-pong')
img = pg.image.load('andr.png')  # Получение изображения и присваивание его переменной
pg.display.set_icon(img)  # Отрисовка иконки приложения

FPS = 120  
window_width = 600  
window_height = 400  

width_rect_1 = 10  
height_rect_1 = 100  

width_rect_2 = 10  
height_rect_2 = 100  

blue = (12, 56, 84)  # Создаем цвета фона RGB-раскладкой
white = (255, 255, 255)
red = (255, 0, 0)

r = 15  # Радиус шарика
x, y = 100, 300  
direct_x, direct_y = 1, 1  

x_rect_1 = (window_width - width_rect_1)  
y_rect_1 = window_height // 2 - height_rect_1 // 2  
direct_y_rect_1 = 3  

x_rect_2 = 0  
y_rect_2 = window_height // 2 - height_rect_1 // 2  
direct_y_rect_2 = 3  

screen = pg.display.set_mode((window_width, window_height))  # Создание переменной отрисовки экрана
clock = pg.time.Clock()  # Создание переменной времени

bg = pg.image.load('bg.png').convert()  # Создание фона картинки

count_user_1 = 0  
count_user_2 = 0  

while True:  # Цикл событий
    for event in pg.event.get():  # Цикл, отслеживающий события
        if event.type == pg.QUIT:  # Отслеживание закрытия окна приложения
            sys.exit()  # Прерывание выполнения скрипта

    clock.tick(FPS)  # Инициализация частоты кадров/сек
    pg.event.pump()  # Функция, позволяющая реагировать на зажатие клавиш

    screen.blit(bg, (0,0))

    pg.draw.line(screen, red, (window_width // 2, 0), (window_width // 2, window_height), 8)  
    pg.draw.line(screen, red, (0, window_height // 2), (window_width, window_height // 2), 4)  

    font_ = pg.font.SysFont('tahoma', 32)  # Создание шрифта
    text = font_.render(f'{count_user_2} : {count_user_1}' , True, (255, 0, 0))  # Создание текста счета
    screen.blit(text, (window_width // 2 - 32, 0))  # Отрисовка счета

    ball_1 = pg.draw.circle(screen, white, (x, y), r)  

    pg.draw.rect(screen, black,  
                 (x_rect_1, y_rect_1, width_rect_1, height_rect_1)
                 )

    pg.draw.rect(screen, black,  
                 (x_rect_2, y_rect_2, width_rect_2, height_rect_2)
                 )

    if pg.key.get_pressed()[pg.K_DOWN]:  # Обработка перемещения платформы 1 вниз
        if y_rect_1 + height_rect_1 >= window_height:  
            y_rect_1 = window_height - height_rect_1
        y_rect_1 += direct_y_rect_1  

    if pg.key.get_pressed()[pg.K_UP]:  # Обработка перемещения платформы 1 вверх
        if y_rect_1 <= 0: 
            y_rect_1 = 0
        y_rect_1 -= direct_y_rect_1  

    if pg.key.get_pressed()[pg.K_s]:  # Обработка перемещения платформы 2 вниз
        if y_rect_2 + height_rect_2 >= window_height: 
            y_rect_2 = window_height - height_rect_2
        y_rect_2 += direct_y_rect_2 

    if pg.key.get_pressed()[pg.K_w]:  # Обработка перемещения платформы 2 вверх
        if y_rect_2 <= 0:  
            y_rect_2 = 0
        y_rect_2 -= direct_y_rect_2  

    x += direct_x  # Перемещение шарика по Ox
    y += direct_y  # Перемещение шарика по Oy

    if y < 0 + r or y + r >= window_height:  # Отталкивание шарика от краев экрана
        direct_y = -direct_y

    if x - r >= window_width:  # Проверка вылета шарика за половину 2 игрока
        count_user_2 += 1 
        x, y, = window_width // 2, window_height // 2  
        FPS = 120  # Возврат FPS в исходное состояние

    if x <= 0:  # Проверка вылета шарика за половину 1 игрока
        count_user_1 += 1 
        x, y = window_width // 2, window_height // 2  
        FPS = 120  

    if x - r in range(x_rect_2, x_rect_2 + width_rect_2) and y - r in range(y_rect_2, y_rect_2 + height_rect_2):  # Отталкивание от 2 платформы
        direct_x = -direct_x  # Изменение направления движения шарика
        FPS += 10  # Увеличение скорости движения шарика

    if x + r in range(x_rect_1, x_rect_1 + width_rect_1) and y + r in range(y_rect_1, y_rect_1 + height_rect_1):  # Отталкивание от 1 платформы
        direct_x = -direct_x  # Изменение направления движения шарика
        FPS += 10  # Увеличение скорости движения шарика


    pg.display.update()  # Обновление экрана

