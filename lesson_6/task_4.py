class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} - поехала'

    def stop(self):
        return f'{self.name} - остановилась'

    def turn_right(self):
        return f'{self.name} - повернула направо'

    def turn_left(self):
        return f'{self.name} - повернула налево'

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость городского автомобиля {self.name} - превышена!'
        else:
            return f'{self.name} - скорость допустима для городского автомобиля'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочего автомобиля {self.name} - {self.speed}')

        if self.speed > 60:
            return f'{self.name} - скорость превышена для рабочего автомобиля!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} автомобиль полиции'
        else:
            return f'{self.name} автомобиль не принадлежит полиции'


porsche = SportCar(100, 'красный', 'Porsche', False)
peugeot = TownCar(30, 'белый', 'Peugeot', False)
lada = WorkCar(70, 'чёрный', 'Lada', True)
ford = PoliceCar(110, 'синий', 'Ford', True)
print(lada.turn_left())
print(f'{peugeot.turn_right()}, затем {porsche.stop()}')
print(f'{lada.show_speed()}')
print(f'{lada.name} - цвет {lada.color}')
print(f'{porsche.name} автомобиль полиции? {porsche.is_police}')
print(f'{lada.name}  автомобиль полиции? {lada.is_police}')
print(porsche.show_speed())
print(peugeot.show_speed())
print(ford.police())
print(ford.show_speed())
