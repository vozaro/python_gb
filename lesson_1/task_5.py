a = int(input('Введите сумму выручки - '))
b = int(input('Введите сумму издержек - '))

if a > b:
    print('Ваша прибыль - ', a - b)

if a < b:
    print('Ваш убыток - ', b - a)

print('Рентабельность вашего бизнеса - ', '{0:.2f}'.format(a / b))

if a > b:
    c = int(input('Введите количество сотрудников - '))
    print('Прибыль фирмы в расчете на одного сотрудника - ', '{0:.2f}'.format((a - b) / c))
