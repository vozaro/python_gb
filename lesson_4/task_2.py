my_list = [20, 31, 2, 13, 16, 1, 9, 11, 7, 21]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')