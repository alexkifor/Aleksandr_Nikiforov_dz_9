class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass_asphalt(self):
        mass = self._lenght * self._width * 25 * 5 / 1000
        return mass

road = Road(5000, 20)
print(road.mass_asphalt(), 'т')
