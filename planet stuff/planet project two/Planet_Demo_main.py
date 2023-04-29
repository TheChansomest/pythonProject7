from SolarSystem import *
from Planet import *
from Moon import *
from Sun import *
from graphics import *
import random

def printHeader(header):
    header = header.rstrip("\n")  # strip end of line "\n"
    header = header.split(',')

    # design you header to print the data as you wish
    print(header)

#
# readData() function reads planet data from a file
# it ignores the header line which contains titles of attributes
# returns a reference to file contents
#
def readData(radius_factor):
    f = open("planets_and_moons-All.txt", "r")
    headerLine = f.readline()  # read and ignore first line as it holds the header titles
    printHeader(headerLine)

    planets = {}
    for line in f:
        line = line.rstrip("\n")  # strip end of line "\n"
        planet_data = line.split(',')

        # create planet object using data from file
        pName = planet_data[0]
        pRadius = float(planet_data[1])
        pColor = planet_data[2]
        pNoOfMoons = int(planet_data[3])
        if pNoOfMoons > 0:
            pMoonsList = planet_data[4:]
        else:
            pMoonsList = []
        planet = Planet(pName, pRadius, pColor)
        if pNoOfMoons > 0:
            moons = [Moon(moon, pRadius * 0.1 * radius_factor, pColor,planet) for moon in pMoonsList]
            for moon in moons:
                moon.setPlanet(planet)
                planet.addMoon(moon)
        planets[pName] = planet

    f.close()
    return SolarSystem("Milky Way", Sun("Sun", 4), planets)

def drawStars(win):
    # draw stars
    for i in range(300):
        x = random.randint(0, 1000)
        y = random.randint(0, 600)
        size = random.uniform(0.5, 1.5)
        if i % 2 == 0:
            color = "yellow"
        else:
            color = "white"
        star = Circle(Point(x, y), size)
        star.setFill(color)
        star.setOutline(color)
        star.draw(win)

def main():
    # start drawing using the Graphics package
    win = GraphWin("Solar System", 1000, 600)
    win.setBackground("black")

    # add stars to the background
    drawStars(win)

    # get a_sun object
    our_sun = Sun('Sun', 5)
    our_sun.draw(win)

    # Load planets data
    ss = readData(radius_factor=0.1)

    # draw each planet in the solar system
    x = 350  # center x-coordinate
    y = 180  # center y-coordinate
    radius_factor = 0.001  # scale factor for planet radius
    for planet_name in ss.getPlanetsDict():
        planet = ss.getPlanet(planet_name)
        planet.draw(win, x, y, radius_factor)  # pass radius_factor to draw() method
        radius = planet.getRadius() * radius_factor
        x += (100/(radius*4))+60 # space planets evenly along x-axis
        y += 50

    time.sleep(0)
    # wait for user to close window
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
