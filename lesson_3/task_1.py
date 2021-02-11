def division(divisible, divisor):
    while divisor == 0:
        divisor = (int(input('На ноль делить нельзя! Введите делитель - ')))
    return divisible / divisor

print(division(int(input('Введите делимое - ')), int(input('Введите делитель - '))))


