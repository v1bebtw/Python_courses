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

string = 'Сидел барсук в своей норе и ел картошечку пюре'
a = '!'
c = 'ре'

print(len(string))
print(string + a)

if c in string:
    print(f'{c} есть!')
else:
    print(f'{c} нет!')
