from functools import reduce


def my_func(prev_el, el):
    return prev_el * el

print(f'Список чётных чисел списка {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат умножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')