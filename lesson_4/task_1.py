def my_zp():
    try:
        name = input('Имя сотрудника - ')
        hour = float(input('Выработка в часах - '))
        rate = int(input('Ставка за час - '))
        bonus = int(input('Премия в процентах от выработки - '))
        check = (hour * rate) + ((hour * rate) * (bonus / 100))
        print(f'Заработная плата сотрудника {name} - {check}')
    except ValueError:
        return print('Not a number')
my_zp()

# не получилось сделать скриптом... =(