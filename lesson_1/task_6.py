a = int(input('Введите количество километров, которое Вы пробежали сегодня - '))
b = int(input('Введите целевой километраж пробежки - '))
count = 1
if a > b:
    print('Ваша цель достигнута! =)')
else:
    while a <= b:
        a = a * 1.1
        count = count + 1
print('Вам потребуется -', count, 'дней')
