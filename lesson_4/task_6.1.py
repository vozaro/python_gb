from itertools import cycle

my_list = ['Hello world', 123, 25.32, False]
for el in cycle(my_list):
    print(el)
