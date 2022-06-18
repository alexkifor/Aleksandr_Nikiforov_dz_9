class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f'{self.name} поехала')
        else:
            exit(1)

    def stop(self):
        if self.speed == 0:
            print(f'{self.name} остановилась')
        else:
            exit(1)

    def turn(self, direction):
        if self.speed > 0:
            print(f'{self.name} повернула на {direction}')
        else:
            exit(1)

    def show_speed(self):
        print(f'текущая скорость {self.name}:{self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('превышение скорости')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('превышение скорости')

class PoliceCar(Car):
    pass
town_car = TownCar(70, 'желтая', 'городская машина', False)
sport_car = SportCar(200, 'красная', 'спортивная машина', False)
work_car = WorkCar(60, 'ораньжевая', 'рабочая машина', False)
police_car = PoliceCar(0, 'бело-синяя', 'полицейская машина', True)
town_car.show_speed()
sport_car.go()
work_car.turn('право')
police_car.go()