usd = float(2.57)
euro = float(2.92)

money = int(input('Введите сумму, которую хотите обменять: '))
currency = int(input('1 - доллары, 2 - евро: '))

if currency == 1:
    cash = round(money / usd, 2)
    print(cash)
elif currency == 2:
    cash = round(money / euro, 2)
    print(cash)
else:
    print('Что-то пошло не так')


