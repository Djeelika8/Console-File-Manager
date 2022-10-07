# НЕ ЧИСТАЯ функция
def CheckedNumber(money):
    while not money.isdigit():
        money = input('Внесите корректную сумму: ')
    return float(money)

# НЕ ЧИСТАЯ функция
def shopping_hist(hist):
    for shop in hist:
        print(shop[0], '  стоимостью  ', shop[1])


def bank():
    money = 0.00
    hist = []
    while True:
        print('0. выход')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. текущий баланс')

        ch = input('Выберите пункт меню: ')

        if ch == '0':
            print('Выход из Игры "Мой банковский счет"')
            break

        elif ch == '1':
            input_money = input('Введите сумму пополнения: ')
            money += CheckedNumber(input_money)

        elif ch == '2':
            input_money = input('Введите сумму покупки: ')
            deb = CheckedNumber(input_money)
            if deb > money:
                print('Сумма покупки больше доступного остатка')
            else:
                s = input('Введите название покупки: ')
                money = money - deb
                hist.append([s, deb])

        elif ch == '3':
            shopping_hist(hist)

        elif ch == '4':
            print(f'Ваш остаток = {money}')
        else:
            print('Неверный пункт меню')
