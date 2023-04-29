


class SolarSystem:
    def __init__(self, iName, iStar, iPlanetsDict={}):
        self.__iName = iName
        self.__iStar = iStar
        self.__iPlanetsDict = iPlanetsDict

    def addPlanet(self, aPlanet):
        self.__iPlanetsDict[aPlanet.getName()] = aPlanet

    def getPlanet(self, name):
        return self.__iPlanetsDict[name]

    def showPlanet(self):
        for planet in self.__iPlanetsDict.values():
            print(planet)

    def getPlanetsDict(self):
        return self.__iPlanetsDict

    def __str__(self):
        return f"Solar System: {self.__iName}\nStar: {self.__iStar}\nNumber of Planets: {len(self.__iPlanetsDict)}"

    def draw(self):
        win = GraphWin("Solar System", 800, 600)
        x = 400  # center x-coordinate
        y = 300  # center y-coordinate
        radius_factor = 0.1  # scale factor for planet radius

        # draw the sun
        self.__iStar.draw(win, x, y)

        # draw each planet and its moons
        for planet in self.__iPlanetsDict.values():
            planet.draw(win, x, y)
            radius = planet.getRadius() * radius_factor
            x += 30 * radius  # space planets evenly along x-axis

        # wait for user to close window
        win.getMouse()
        win.close()


"""
Our solar system consists of:
 1. our star, the Sun, and everything bound to it by gravity – 
 2. the planets Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune; 
 3. dwarf planets such as Pluto; Dwarf Plants live inside a belt (Asteriod or Kuiper).
 4. moons; planets might have 1 or more moons orbiting around them
 5. millions of asteroids, comets, and meteoroids.
 6. Galaxy
    Our solar system is just one specific planetary system—a star with planets orbiting around it. 
    Our planetary system is the only one officially called “solar system,” 
    but astronomers have discovered more than 3,200 other stars with planets orbiting them in our galaxy. 
    
    Our Sun is just one of about 200 billion stars in our galaxy. 
    Exoplanets are planets outside outside our solar system.

"""
