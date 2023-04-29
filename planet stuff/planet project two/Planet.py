from graphics import *
import math

class Planet:
    def __init__(self, name, radius, color, moonsList=None):
        if moonsList is None:
            moonsList = []
        self.__name = name
        self.__radius = radius
        self.__color = color
        self.__moonsList = moonsList
        self.__x = 0
        self.__y = 0

    def getName(self):
        return self.__name

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def getMoonsList(self):
        return self.__moonsList

    def addMoon(self, aMoon):
        self.__moonsList.append(aMoon)

    def hasMoons(self):
        return len(self.__moonsList) > 0

    def __str__(self):
        return f"Planet Name: {self.__name}, Radius: {self.__radius}, Color: {self.__color}, Number of Moons: {len(self.__moonsList)}"

    def draw(self, win, x, y, radius_factor):
        planet_circle = Circle(Point(x, y), self.__radius * radius_factor)
        planet_circle.setFill(self.__color)
        planet_circle.draw(win)

        # Draw moons
        if self.hasMoons():
            moon_radius_factor = radius_factor / 0.02  # scale moons proportionally to planets
            moon_distance_factor = self.__radius * radius_factor + moon_radius_factor * self.__radius * radius_factor
            moon_x = x + moon_distance_factor
            moon_y = y
            moon_angle = 0
            for moon in self.__moonsList:
                moon_radius = moon.getRadius() * moon_radius_factor
                moon_xpos = moon_x + moon_distance_factor * math.cos(moon_angle)*2-15
                moon_ypos = moon_y + moon_distance_factor * math.sin(moon_angle)*1-5
                moon.draw(win, moon_xpos, moon_ypos, moon_radius_factor)
                moon_angle += 2 * math.pi / len(self.__moonsList)

    def setPosition(self, x, y):
        self.__x = x
        self.__y = y

    def getPosition(self):
        return self.__x, self.__y