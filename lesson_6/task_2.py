class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class MassCount(Road):
    def __init__(self, _length, _width, depth, mass):
        super().__init__(_length, _width)
        self.depth = depth
        self.mass = mass

    def mass_road(self):
        return self._length * self._width * ((self.depth * self.mass) / 1000)


v = MassCount(20, 5000, 25, 5)
print(v.mass_road())
