def my_func(a, b, c):
    if a < b:
        min_numb = a
    else:
        min_numb = b
    if c < min_numb:
        min_numb = c
    return a + b + c - min_numb


sum_el = my_func(int(input('Введите первое число - ')),
                 int(input('Введите второе число - ')),
                 int(input('Введите третье число - ')))

print(sum_el)
