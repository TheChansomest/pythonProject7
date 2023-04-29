


# class of insect
# use bumblebee as a guideline to make grasshopper

# "is-a" relationship
# exits when one object is a
# specialized version of another object
# -specialized object has all the characteristics of the general
# object plus unique characteristics

# multilevel inheritance -
# square-->rectangle-->polygon-->shape

class Automobile #parent class or superclass


class Car(Automobile) #subclass
    def __init__(self, doors):

        Automobile.__init__()
        self.__doors = doors