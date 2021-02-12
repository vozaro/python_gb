def my_sum():
    sum_result = 0
    fix = False
    while not fix:
        number = input('Введите числа или E для выхода - ').split()
        result = 0
        for el in range(len(number)):
            if number[el] == 'e' or number[el] == 'E':
                fix = True
                break
            else:
                result = result + int(number[el])
        sum_result = sum_result + result
        print('Текущая сумма - ', sum_result)
    print('Финальная сумма - ', sum_result)


my_sum()
