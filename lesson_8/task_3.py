class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажмите клавишу Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f'Недопустимое значение!')
                stop = input('Чтобы закончить введите слово - stop \n')

                if stop != 'stop':
                    print(f'Текущий список - {self.my_list} \n ')
                    print(try_except.my_input())
                else:
                    print()


try_except = Error()
print(try_except.my_input())
