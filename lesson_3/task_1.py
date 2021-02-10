def division(divisible, divisor):
    while divisor == 0:
        print('На ноль делить нельзя!')
        divisor = (int(input('Введите делитель - ')))
    return divisible / divisor

result = division(int(input('Введите делимое - ')), int(input('Введите делитель - ')))

print(result)
