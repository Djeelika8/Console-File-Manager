def input_money(text):
    money = input(text)
    while not money.isdigit():
        money = input('Внесите корректную сумму: ')
    return float(money)


def shopping_hist(hist):
    for shop in hist:
        print(shop[0], '  стоимостью  ', shop[1])


def bank():
    money = 0.00
    hist = []
    while True:
        print('0. текущий баланс')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        ch = input('Выберите пункт меню: ')

        if ch == '0':
            print(f'Ваш остаток = {money}')

        elif ch == '1':
            money += input_money('Введите сумму пополнения: ')

        elif ch == '2':
            deb = input_money('Введите сумму покупки: ')
            if deb > money:
                print('Сумма покупки больше доступного остатка')
            else:
                s = input('Введите название покупки: ')
                money = money - deb
                hist.append([s, deb])
            pass
        elif ch == '3':
            shopping_hist(hist)

        elif ch == '4':
            break
        else:
            print('Неверный пункт меню')
