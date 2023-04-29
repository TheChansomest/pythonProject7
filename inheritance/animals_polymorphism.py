# The Mammal class represents a generic mammal.

class Mammal:
    def __init__(self, species):
        self.__species = species
    
    def show_species(self):
        print('I am a', self.__species)
    
    def make_sound(self):
        print('Grrrrr')

# The Dog class is a subclass of the Mammal class.

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    def make_sound(self):
        print('Woof! Woof!')

# The Cat class is a subclass of the Mammal class.
class Cat(Mammal):
    # The __init__ method calls the superclass's
    # __init__ method passing 'Cat' as the species.

    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # The make_sound method overrides the superclass's
    # make_sound method.
    def make_sound(self):
        print('Meow')

