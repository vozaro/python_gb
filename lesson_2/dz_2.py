data = ['name', 'surname', 'age', 'city']

data[0] = input('Введите ваше имя - ')
data[1] = input('Введите вашу фамилию - ')
data[2] = int(input('Введите ваш возраст - '))
data[3] = input('Введите город проживания - ')

print(data)

data.insert(1, data.pop(0))
data.insert(2, data.pop(3))

print(data)
