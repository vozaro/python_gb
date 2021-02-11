def my_func(x, y):
    while x <= 0:
        x = float(input('Введите действительное положительное число - '))
    while y >= 0:
        y = int(float(input('Введите отрицательное целое число - ')))
    for i in range(abs(y)):
        x = x * i
    return 1 / x

print(my_func(float(input('Введите действительное положительное число - ')),
                 int(float(input('Введите отрицательное целое число - ')))))
