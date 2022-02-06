password = 'Qwerty1234'
treb_1 = 'QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
treb_2 = '123456789-=!@#$%^&*()_+'

if len(password) > 8:
    for i in treb_1:
        if i in password:
            print('Заглавные буквы есть')
            break
        else:
            print('Заглавные буквы отсутствую')

    for i in treb_2:
        if i in password:
            print('Спец. символы или цифры есть')
            break
        else:
            print('Спец. символы или цифры отсутствую')
            break

else:
    print('Пароль слишком короткий')

