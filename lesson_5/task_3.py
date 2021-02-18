with open('task_3.txt', 'r') as my_file:
    task_3 = []
    zp = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            zp.append(i[0])
        task_3.append(i[1])

print(f'Оклад меньше 20.000 {zp}, средний оклад {sum(map(int, task_3)) / len(task_3)}')
