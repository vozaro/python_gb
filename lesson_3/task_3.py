def my_func(a, b, c):
    if a < b:
        min = a
    else:
        min = b
    if c < min:
        min = c
    return a + b + c - min

sum = my_func(int(input('Введите первое число - ')),
               int(input('Введите второе число - ')),
               int(input('Введите третье число - ')))

print(sum)
