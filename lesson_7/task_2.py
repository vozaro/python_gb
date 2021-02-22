class Textiles:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_square_coat(self):
        return self.size / 6.5 + 0.5

    def get_square_costume(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани \n' 
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textiles):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто {self.square_coat}'


class Costume(Textiles):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_costume = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм {self.square_costume}'


coat = Coat(2, 4)
costume = Costume(1, 2)
print(coat)
print(costume)
print(coat.get_sq_full)
print(costume.get_sq_full)
print(costume.get_square_coat())
print(costume.get_square_costume())
