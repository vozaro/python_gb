def my_func(x, y):
    while x <= 0:
        x = float(input('Введите действительное положительное число - '))
    while y >= 0:
        y = int(float(input('Введите отрицательное целое число - ')))
    r = 1
    for i in range(-y):
        r /= x
    print(r)


my_func(float(input('Введите действительное положительное число - ')),
                 int(float(input('Введите отрицательное целое число - '))))
