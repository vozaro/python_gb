data = input('Введите несколько слов - ')
data = data.split()

for i, data in enumerate(data):
    print(i + 1, data[:10])
