


# Open the file and read in the lines
def readPlanetData(planetFile):

    planet_dict = {}

    with open(planetFile, 'r') as f:
        lines = f.readlines()

    # Parse each line into a dictionary entry
    for line in lines:
        # Split the line into its components
        components = line.strip().split(',')
        # Use the first component as the key, and the remaining components as the values
        key = components[0]
        # Convert the numerical values to floats
        values = [float(v) if '.' in v else v for v in components[1:]]
        # Add the entry to the dictionary
        planet_dict[key] = values
    return planet_dict

def processPlanetData(planet_dict):

    for key, values in planet_dict.items():
        new_values = [int(v) if isinstance(v, str) and v.isnumeric() else v for v in values]
        planet_dict[key] = new_values
    return planet_dict

def print_data(dictionary):
    fmt = "{:<12}: {:<6}, {:<6}, {:^17}, {:^7}, {:^9}, {:^11}"
    print(fmt.format("PLANET NAME", "RADIUS", "MASS", "DISTANCE_FROM_SUN", "COLOR", "IS_Dwarf", "NO_OF_MOONS"))

    iter_dict = iter(dictionary.items())
    next(iter_dict)
    for key, values in iter_dict:
        print(fmt.format(key, *values))


def getPlanetsAsSet(planet_dict_names):
    planet_set = set(planet_dict_names.keys())
    planet_set.discard("NAME")
    print(planet_set)

def buildPlanetMap(planet_dict):
    planet_dict.pop("NAME")      #the dictionary without the NAME, radius
    print(planet_dict)

def getMoons(planet_dict):
    while True:
        planet_moons = str(input("Give me a planet name and I'll give you its number of moons, or type 'quit' :").capitalize())
        if planet_moons == "Quit":
            break
        elif planet_moons not in planet_dict:
            print("Invalid planet name. Please try again.")
        else:
            num_moons = planet_dict[planet_moons][-1]
            print(f"{planet_moons} has {num_moons} moon(s).")

def getDwarfs(planet_dict):
    dwarf_planets = []
    for planet_name, planet_data in planet_dict.items():
        if planet_data[4] == "True":
            dwarf_planets.append(planet_name)
    print(dwarf_planets)


def main():
    planetFile = "planet data"
    read_dict = readPlanetData(planetFile)
    planet_dict = processPlanetData(read_dict)
    print_data(planet_dict)
    getPlanetsAsSet(planet_dict)
    buildPlanetMap(planet_dict)
    getMoons(planet_dict)
    getDwarfs(planet_dict)
main()