
from graphics import *



class Sun:
    def __init__(self, iName, iRad):
        self.__star_name = iName
        self.__radius = iRad

    def getRadius(self):
        return self.__radius

    def getName(self):
        return self.__star_name

    # draw the sun
    def draw(self, win):
        center = Point(win.getWidth() / 2, win.getHeight() / 2)
        radius = self.__radius * win.getHeight() * 0.05  # scale radius based on window height
        sun = Circle(center, radius)
        sun.setFill('yellow')
        sun.draw(win)

    def __str__(self):
        return f"Sun with radius {self.__radius} and name {self.__star_name}"
