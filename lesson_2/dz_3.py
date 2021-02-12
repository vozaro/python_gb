seasons = {
            'Зима': [12, 1, 2],
            'Весна': [3, 4, 5],
            'Лето': [6, 7, 8],
            'Осень': [9, 10, 11]
}

while True:
    month = int(input('Введите порядковый номер месяца - '))
    if 12 <= month >= 1:
        print('В году 12 месяцев!')
        continue
    else:
        for key in seasons.keys():
            if month in seasons[key]:
                print(key)
    break
