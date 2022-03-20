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

# top = ""
# list = []
#
# while True:
#     top = input("Что вы хотите добавить в пиццу?")
#     if top == "quit":
#         print("Ваш заказ принят")
#         break
#     if top != "quit":
#         print(f"{top} добавили в пиццу")
#     list.append(top)
#
# print(list)

"""************   Цикл for и функция range   ************"""

# numbers = 1, 2, 3, 4
#
# for i in numbers:
#     print(i)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# for i in range(a, b):
#     if i % 2 !=0:
#         print(i)


# c = int(input("Введите первое число: "))
# d = int(input("Введите второе число: "))
#
# if c > d:
#     for i in range(c, d, -1):
#         if i % 5 == 0:
#             if i % 2 != 0:
#                 print(i)
# elif c < d:
#     for i in range(d, c, -1):
#         if i % 5 == 0:
#             if i % 2 != 0:
#                 print(i)


# e = str(input("Введите слово: "))
#
# for i in e:
#     print(i)

# for i in range(0, 6):
#     if i !=3 and i != 6:
#         print(i)

# a = 1
# b = 0
# c = 0
#
# while a != 0:
#     a = int(input("Введите число: "))
#     if a > 0:
#         b += a
#     elif a < 0:
#         c += a
#
# print("Сумма положительных чисел:", b)
# print("Сумма отрицательных чисел:", c)

# n = int(input("Введите натуральное число: "))
#
# if n > 0:
#     for i in range(1, 11):
#         print(f"{n} * {i} = ", n * i)

"""************   Списки, множества, кортежи и словари   ************"""

# Список - это изменяемая упорядоченная последовательность элементов

# list_ = ['Egor', 'Berdnik', 16, True]

# print(list_)
#
# for i in list_:
#     print(i)
#
# list_1 = list(range(1, 5))
# print(list_1)
#
# a = 1, 2, 3, 4
# list_2 = list(a)
# print(list_2)

# names = ['Egor', 'Nikita', 'Artem', 'John']
# surnames = ['Berdnik', 'Ivanov', 'Troshkin', 'Petrov']

# # print(names[0])
#
# count = 0
# for name in names:
#     print(f'Hello, {name}!')
#     count += 1
#     if count == 2:
#         break

# print(names[-1])
#
# print(names[1:4:1])

# print(names + surnames)

# names[2] = 'Vlad'
# print(names[2])

# a = ['Irina', 'Gleb']
# names.append(a)
# print(names)

# names += ['Anastasiya', 'Boris']
# print(names)

# names.insert(1, 'Ivan')
# print(names)

# names.remove('John')
# print(names)

# del names[0]
# print(names)

# names.pop(0)
# print(names)

# if 'Nikita' in names:
#     print('Никита на месте!')

# index = names.index('Egor')
# print(index)

# list_2 = [i for i in range(1,10)]
# print(list_2)

# list_3 = [1, 5, 4, 2, 8, 7]

# list_3.sort()

# print(list_3)
#
# names.sort(reverse=True)
# print(names)

# print(max(list_3))

# print(list_3)
# list_3.reverse()
# print(list_3)

# list_4 = list(list_3)
# print(list_4)

# list_4 = [int(i) for i in input().split()]
# print(list_4)

# list_5 = []
#
# while True:
#     number = int(input('Введите 0 для завершения ввода \nВведите число: '))
#     list_5.append(number)
#     if number == 0:
#         break
# if 777 in list_5:
#     print('True')
# else:
#     print('False')

# list_ = [x for x in range(-5, 5)]
# print(list_)

# list_generator = [x**2
#                   for x in list_
#                   if x % 2 == 0]
# print(list_generator)

# list_4 = []
# for x in list_:
#     if x % 2 == 0:
#         list_4.append(x**2)
# print(list_4)

# tuple_ = (1, 2, 3, 4, 5, 2, 2, 4)
# print(tuple_)
# print(len(tuple_))
#
# a = set(tuple_)
# print(a)

# users = {'name_1': 'Egor',
#          'surname_1': 'Berdnik'}
#
# users['name_2'] = 'Artem'
# users['name_1'] = 'Ivan'
#
# # print(users['name_1'])
# # print(users['surname_1'])
#
# del users['name_1']
# print(users)
# print(users['name_2'])

# favourite_food = {
#     'Иван': 'колбаса',
#     'Георгий': 'кукуруза',
#     'Василий': 'бураки',
#     'Андрей': 'колбаса',
# }

# food = favourite_food.get('Артём', 'картофель')
# print(f'Любимая еда Артёма - {food}')

# for key, value in favourite_food.items():
#     print(f'key: {key}, value: {value}')
#
# for key in favourite_food.keys():
#     print(f'Key: {key}')
#
# for value in favourite_food.values():
#     print(f'Value: {value}')

# N = int(input('Введите двухзначное число: '))
#
# list_5 = [int(a) for a in str(N)]
# print(sum(list_5))


# count = 0
#
# for number in str(N):
#     number = int(number)
#     count += number
# print(count)

# year = int(input('Введите год: '))
# if year % 100 == 0:
#     print('Yes')
# else:
#     print('No')

# import random
#
# n = int(input('Введите размер списка: '))
#
# list_6 = [random.randint(0, 100) for i in range(n)]
# print(list_6)
#
# # a = int(input('Введите индекс элемента: '))
# # list_6.pop(a)
# # print(list_6)
#
# for index in range(len(list_6)):
#     if index % 6 == 0:
#         list_6.pop(index)
#
# print(list_6)

"""************   Работа с файлами   ************"""

# test.txt
# file_reader.py
# names.txt

"""************   Функции   ************"""

# Создание функции
# def Имя функции(параметры):
#   Блок инструкции


# def user(username, password):
#     print(f'Привет {username}!\nПароль: {password}')
#
#
# name = str(input('Введите имя: '))
# pw = input('Введите пароль: ')
# user(name, pw)

# def get_name(first_name, last_name, middle_name=None):
#     """Возвращает аккуратно отформатированные имя и фамилию"""
#     if middle_name:
#         full_name = f'{last_name} {first_name} {middle_name} '
#     else:
#         full_name = f'{last_name} {first_name}`'
#     return full_name.title()
#
#
# user = get_name(first_name='Егор', last_name='Бердник', middle_name='Сергеевич')
# print(user)

# def build_user(first_name, last_name, age=None):
#     user = {'name': first_name, 'surname': last_name}
#     if age:
#         user['age'] = age
#     return user
#
#
# user_ = build_user('Egor', 'Berdnik', 16)
# print(user_)


# current_users = []
#
#
# def users(names):
#     global current_users
#     for name in names:
#         if name == 'джо':
#             continue
#         current_users.append(name)
#         print(f'Hello, {name.title()}')
#
#
# users(['егор', 'артем', 'назар', 'джо'])
# print(current_users)

# def fact(number):
#     if number == 0:
#         print('Так не пойдёт!')
#     elif number == 1:
#         return number
#     else:
#         return number * fact(number-1)
#
#
# print(fact(5))

# def print_scores(name, *scores):
#     print(f'Name: {name}')
#     for score in scores:
#         print(score)
#
#
# print_scores('Egor', 2, 10, 8, 9, 10, 2, 5)

# def print_pet_names(owner, **names):
#     print(f'Owner name: {owner}')
#     for pet, name in names.items():
#         print(f'{pet}: {name}')
#
#
# print_pet_names('Egor', dog='Bobik', fish=['Larry', 'Ben', 'Clary'], turtle='Shelldon')

# def draw_triangle(start, stop):
#     for i in range(start, stop + 1):
#         print('*' * i)
#
#
# draw_triangle(5, 10)

def make_pizza(size, *toppings):
    print(f"Пицца, диаметром {size} и с ингридиентами: {', '.join(toppings)}, готовится")


make_pizza(35, 'сыр', 'томаты', 'мясо')
