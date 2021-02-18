my_func = open('task_1.txt', 'w')
line = input('Введите текст - \n')
while line:
    my_func.writelines(line)
    line = input('Введите текст - \n')
    if not line:
        break

my_func.close()
my_func = open('task_1.txt', 'r')
content = my_func.readlines()
print(content)

my_func.close()
