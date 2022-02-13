# fname = 'Egor'
# lname = 'Berdnik'
#
# print("Hello ", fname, lname)
#
# input('Нажмите Enter')

# a = input('Введите свое имя: ')
# b = int(input('Введите ваш возраст: '))
#
# print(type(a))
# print(type(b))

# in
# s = 10, 20, 30
# x = 10
# print(x in s)
#
# list = ['Egor', 'Berdnik', 15]
# print(list)
#
# tuple = ('Egor', 'Berdnik', 15)
# print(tuple)

# string = "всем привет, я ЛЮБЛЮ python!"
#
# print(f'Исходная фраза: {string}')
#
# print(f'\nКогда я кричу: {string.upper()}')
#
# print(f'\nКогда я говорю шепотом: {string.lower()}')
#
# print(f'\nС заглавных букв: {string.title()}')
#
# print(f'\nС заменой: {string.replace("ЛЮБЛЮ", "ОБОЖАЮ")}')
#
# input('Нажмите Enter для завершения')

# string = 'egor', 'berdnik', 15
# print(string[0])
# print(string[1])
# print(string[2])

# print(string[-1])
# print(string[-2])
# print(string[-3])

# string = 'egor'
# print(string[0:3])
# print(string[-1])

# string = 'Сидел барсук в своей норе и ел картошечку пюре'
# a = '!'
# c = 'ре'
#
# print(len(string))
# print(string + a)
#
# if c in string:
#     print(f'{c} есть!')
# else:
#     print(f'{c} нет!')

"""************   Условные операторы   ************"""

# x = 0

# y = 5

# if x == 6:
#     print('Верно')
#
# elif x == 4:
#     print(4)
#
# elif x == 3:
#     print(3)
#
# else:
#     print('Ничего не верно')

# if x >= 0:
#     print('Число больше нуля')
#
# print('Едем дальше')
#
# if x >= 0 and y >= 0:
#     print('Оба числа больше 0')
#
# if x == 5 or y == 5:
#     print('Какое-то из чисел равно 5')
#
# if x != 5:
#     print('X не равно 5')
#
# health = int(input('Введите кол-во здоровья:'))
#
# if health <= 0:
#     health = False
#     print(health)
#
# else:
#     health = True
#     print(health)
#
# password = input('Введите пароль: ')
#
# if password == '777atom':
#     print('Доступ к компьютеру разрешён')
#
# else:
#     print('Пароль неверный. Доступ к компьютеру запрещён')

# x = 10
#
# if x % 2 == 0:
#     print('Число чётное')
# else:
#     print('Число нечётное')
#
# if x % 5 == 0:
#     print('Число делиться на 5')
# else:
#     print('Число не делиться на 5')
#
# print(len(str(x))

# year = int(input('Введите ваш год:'))
#
# if year % 4 == 0:
#     print('Yes')
# else:
#     print('No')

# x = int(input('Введите координату точки по оси OX:'))
# y = int(input('Введите координату точки по оси OY:'))
#
# if x > 0 and y > 0:
#     print('Точка находиться в первой четверти')
#
# elif x < 0 and y > 0:
#     print('Точка находиться во второй четверти')
#
# elif x < 0 and y < 0:
#     print('Точка находиться в третьей четверти')
#
# elif x > 0 and y < 0:
#     print('Точка находиться в четвёртой четверти')
#
# else:
#     print('Точка находиться на оси')
#
# month = int(input('Введите номер месяца вашего рождения:'))
#
# if 0 < month < 3 or month == 12:
#     print('За окном падал белый снег')
#
# elif 2 < month < 6:
#     print('Птицы пели прекрасные песни')
#
# elif 5 < month < 9:
#     print('Солнце светило ярче, чем когда-либо')
#
# elif 8 < month < 12:
#     print('Урожай был невероятным')
#
# else:
#     print('В году 12 месяцов')

"""************   Цикл while и модуль random   ************"""

#import random
#
#
# print(random.randint(1, 10))
# random.randint(start, stop, step(не всегда))
# print(random.randrange(10))
# random.randrange(10(10 не включая))

# import random
#
#
# kubik1 = random.randint(1, 6)
# kubik2 = random.randrange(6) + 1
# total = kubik1 + kubik2
#
# print(f"При вашем броске выпалоk {kubik1} и {kubik2} очков. \nВ сумме {total}")
# input("\n\nНажмите Enter, чтобы выйти ")

# a = 1
# while a != 10:
#     print(a)
#     a += 1
#
# print('Всё, конец программы, я сделал всё, что мог')

# otvet = ""
#
# while otvet.lower() != "Покупаю":
#     otvet = input("купи слона!\n")
#
#     if otvet.lower() == "покупаю":
#         break
#
#     if otvet.lower() == "покупаю":
#         print(f"Все говорят:{otvet}, а ты возьми и купи слона!")
#
# print("Цена на слона 1000$. Деньги вперед")
# input("Нажмите Enter, чтобы выйти")

# num = 0
# while num < 20:
#     num += 1
#     print(num)

# print("Вашего героя окружила огромная армия троллей. \nСмрадными зелеными трупами врагов устланы все окрестные поля. \nОдинокий герой достает меч из ножен, готовясь к последней битве в своей жизни\n")
#
# health = 100
# trolls = 0
# damage = 3
#
# while health > 0:
#     trolls = trolls + 1
#     health = health - damage
#     print(f"Взмахнув мечом, ваш герой истребляет злобного тролля, но сам получает повреждений на {damage} очков.\n")
#
# print(f"Ваш герой доблестно сражался и убил {trolls} троллей.")
# print("Но увы, он пол на поле боя.")
# print("F герою")
# input("\n\nНажмите Enter, чтобы выйти.")

# count = 0
#
# while True:
#     count += 1
#
#     if count > 10:
#         break
#
#     if count == 5:
#         print('Пропускаем пятерку')
#
#     print(count)

# print("\tЭксклюзивная компьютерная сеть")
# print("\tТолько для зарегистрированных пользователей!\n")
#
# security = 0
# username = ""
# password = ""
#
# while not username:
#     username = input("Логин:")
#
# while not password:
#     password = input("Пароль:")
#
# if username == "Egor" and password == "Egorik":
#     print("Здравствуй, Егор!")
#     security = 3
#
# elif username == "guest" and password == "guest":
#     print("Добро пожаловать к нам в гости.")
#     security = 1
#
# else:
#     print("Войти в систему не удалось. Должно быть, Вы не зарегистрированы. \n")
#
# input("\n\nНажмите Enter, чтобы выйти")

top = ""
list = []

while True:
    top = input("Что вы хотите добавить в пиццу?")
    if top == "quit":
        print("Ваш заказ принят")
        break
    if top != "quit":
        print(f"{top} добавили в пиццу")
    list.append(top)

print(list)
