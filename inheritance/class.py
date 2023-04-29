
#  class def-
#what's inside
#constructor- methods (methods are functions)
# that help me initialize the name
#Accessors / getters - set of methods that allows
# me to read out of the object ex. get Name
#mutators / setters -     ex. set Name
#inheritance- a heirarchy of classes ex in terms of cookies, using different fillings (vanilla, chocolate)
#construct
class Person: #in good practice, start a class
    # variable with a capital letter
              #needed  #parameters
    def __init__(self, name, age, fc):
        self.__name = name
        self.__age = age
        self.__fav_color = fc

    def __str__(self):         #hashtag to get instance b
        return f"{self.__name}:({self.__age})"

    def greeting(self):
        print("hello there, my name is", self.name)

    def setName(self, newName):
        self.__name = newName

    def getName(self):
        return self.__name

def main():
    chandler = Person("Chandler", 19, "blue-violet")
                        #parameters
   # print(chandler.getName())
    #print(chandler.__str__())
    #print(chandler) #prints "at" which refers to where it is stored in memory
    #print(chandler.greeting)
    #print(chandler.greeting())

    #chandler.setName("Dave")
    #print(chandler.getName())
    sal = Person("Sal", 29, "yellow")
    print(sal.getName())
    chandler = Person("Chandler", 19, "blue-violet")
    #print(chandler.__name)
    #print(chandler.__age)    - ---- wont work, instead use
    #print(chandler.__fav_color)
    print(chandler.getName())
    chandler.setName("john")
    print(chandler.getName())
    print(sal)   # change __str__ to get instance b (get object's location in memory
main()

# cookie cutter example
#cookies = object
#cookie cutter = class
#use cookie cutter to make cookies

# data encapsulation provides safety
# encapsulation are shielded from the outside
# world which use methods to interact with them

#inheritance is a powerful tool for reuseability in classes
#polymorphism means "many shapes" and is a greek word