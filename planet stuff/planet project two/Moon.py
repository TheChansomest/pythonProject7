# 1. Complete the constructor __init__ method.
# 2. Encapsulate the Moon attributes: name, radius and color
# 3. complete the __str__ method
# 4. complete the draw method
#

from graphics import *
from Planet import *

class Moon:
    def __init__(self, name, radius, color, planet):
        self.__name = name
        self.__radius = radius
        self.__color = planet.getColor()
        self.__planet = None

    def getName(self):
        return self.__name

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def setPlanet(self, planet):
        self.__planet = planet

    def getPlanet(self):
        return self.__planet

    def __str__(self):
        return f"Moon Name: {self.__name}, Radius: {self.__radius}, Color: {self.__color}"

    def draw(self, win, x, y, planet_radius_factor):
        moon = Circle(Point(x, y), self.__radius * planet_radius_factor * 0.1)
        moon.setFill(self.__color)
        moon.draw(win)


