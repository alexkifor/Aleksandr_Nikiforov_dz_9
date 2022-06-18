from time import sleep
from itertools import cycle
class TrafficLight:

    def __init__(self):
        self.__color = (('red', 7), ('yellow', 3), ('green', 7))

    def running(self):
        for color, time in cycle(self.__color):
            print(color)
            sleep(time)


tl_1 = TrafficLight()
tl_1.running()
