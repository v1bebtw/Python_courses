# f = open('test.txt')
# a = f.read()
# print(a)
# f.close()

# with open('C:\\Users\\IT-Academy-Gomel\\Desktop\\test_text\\test.txt', 'r') as file_object:
#     lines = file_object.readlines()
#     print(type(lines))
#     print(lines, '\n')

# pi_string = ''
#
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)

# file_path = 'C:\\Users\\IT-Academy-Gomel\\Desktop\\test_text\\test.txt'
#
# with open(file_path, 'a') as file_object:
#     for i in range(5):
#         file_object.write('\nI love Python!')
#
# with open(file_path, 'a') as file_object:
#     lines = file_object.read()
#
# print(lines)

#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# # print(pi_string[0:12])
#
# print(pi_string)
#
# if '1802' in pi_string:
#     print('Yes')
# else:
#     print('No')

while True:
    with open('C:\\Users\\IT-Academy-Gomel\\Desktop\\test_text\\names.txt', 'a') as file_object:
        question = input('Введите clear для отчистки файла или 0 для завершения: ')

    if question == 'clear':
        with open('C:\\Users\\IT-Academy-Gomel\\Desktop\\test_text\\names.txt', 'w') as file_object:
            print('Файл очищен')

    if question == '0':
        break

    with open('C:\\Users\\IT-Academy-Gomel\\Desktop\\test_text\\names.txt', 'a') as file_object:
        first_name = str(input('Введите имя: '))
        last_name = str(input('Введите фамилию: '))
        file_object.write(f'{first_name} ')
        file_object.write(f'{last_name} \n')



