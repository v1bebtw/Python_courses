name = input('Привет! Напиши своё имя: ')
age = int(input('Введи количество прожитых лет: '))
weight = int(input('Введи количество килограммов в твоей оболочке (вес): '))

named = name * 5
print(f'\nЗаика назвал бы тебя: {named}')

sec = age * 365 * 24 * 60 * 60
print(f'\nТвой возраст в секундах: {sec} секунд')

moon_weight = int(weight / 6)
print(f'\nТвой вес на луне составит: {moon_weight} килограмм')