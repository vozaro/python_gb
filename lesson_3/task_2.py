def user_data(name, surname, birthday, city, email, tel):
    print(name, surname, birthday, city, email, tel)

user_data(
    name = input('Введите имя - '),
    surname = input('Введите фамилию - '),
    birthday = input('Введите год рождения - '),
    city = input('Введите город проживания - '),
    email = input('Введите email - '),
    tel = input('Введите номер телефона - '),
)