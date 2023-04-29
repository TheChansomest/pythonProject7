#  Program 1 – Planets and Moons made by Chandler Wuchter
#  The goal is to gather data from an outside file, turn the file into
#  a dictionary, and then use that dictionary to complete other tasks

def readPlanetData(planetFile):
    planet_dict = {}

    with open(planetFile, 'r') as f:
        lines = f.readlines()

    for line in lines:
        # Split the line into its components
        components = line.strip().split(',')
        # Use the first component as the key, and the remaining components as the values
        key = components[0]
        values = [float(v) if '.' in v else v for v in components[1:]]
        planet_dict[key] = values
    return planet_dict


def processPlanetData(planet_dict):
    for key, values in planet_dict.items():
        new_values = [int(v) if isinstance(v, str) and v.isnumeric() else v for v in values]
        planet_dict[key] = new_values
    return planet_dict

    # display in format
    # planet Name, Radius, Mass, Dis.From Sun, Color, is Dwarf, No.Of Moons
    # Mercury        1       516       3.285     red      False      0
    # printData(pList) #helper function
    # which generate the above output
    # Is right below this one


def print_data(dictionary):  # prints the data from the dictionary into a more
                             #  readable format
    fmt = "{:<12}: {:<7}, {:<6}, {:^17}, {:^7}, {:^9}, {:^11}"
    print(fmt.format("PLANET NAME", "RADIUS", "MASS", "DISTANCE_FROM_SUN", "COLOR", "IS_Dwarf", "NO_OF_MOONS"))

    iter_dict = iter(dictionary.items())
    next(iter_dict)
    for key, values in iter_dict:
        print(fmt.format(key, *values))


def getPlanetsAsSet(planet_dict_names):  # puts the planets names' into a set
    planet_set = set(planet_dict_names.keys())
    planet_set.discard("NAME")
    print(planet_set)


def buildPlanetMap(planet_dict):
    planet_dict.pop("NAME")  # the dictionary without the NAME, radius
    print(planet_dict)  # and such, get rid of .pop
    # function if I want to keep those details


def getMoons(planet_dict):
    while True:
        planet_moons = str(input("""Give me a planet name and I'll
give you its number of moons, or type 'quit' :""").capitalize())
        if planet_moons == "Quit":
            break
        elif planet_moons not in planet_dict:
            print("Invalid planet name. Please try again.")
        else:
            num_moons = planet_dict[planet_moons][-1]
            print(f"{planet_moons} has {num_moons} moon(s).")


def getDwarfs(planet_dict):
    print("All of the dwarf planets are as follows: ")
    dwarf_planets = []
    for planet_name, planet_data in planet_dict.items():
        if planet_data[4] == "True":
            dwarf_planets.append(planet_name)
    print(dwarf_planets)


def main():
    planetFile = "planet data"
    read_dict = readPlanetData(planetFile)  # This function reads a file
    # passed as a parameter
    # and returns a reference to
    # that file.
    planet_dict = processPlanetData(read_dict)  # The function accepts 2
    # parameters
    # and return the list of
    # planets in the list that was
    # passed empty to it.
    print_data(planet_dict)
    getPlanetsAsSet(planet_dict)  # The function accepts 2
    # parameters a list contains
    # all planet data and return
    # a set contains planet
    # names only.
    buildPlanetMap(planet_dict)  # I might have mistakenly done
    # Populate a dictionary of       #this one in readPlanetData
    # planets and their data as a
    # key-value pair where key
    # is the planet name and value
    # is the list of planet data.
    getMoons(planet_dict)
    getDwarfs(planet_dict)  # runs after you type quit into last function


main()
