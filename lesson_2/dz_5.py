reit = [7, 5, 3, 3, 2]
new = int(input('Введите любое натуральное число - '))
i = [i for i, ltr in enumerate(reit) if ltr == new]

print(i)
