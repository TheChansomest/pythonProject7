class Jungle:
    def __init__(self, j_name: object = "unknown", j_true_hero: object = "OmarZan") -> object:
        self.__j_name = j_name
        self.__j_true_hero = j_true_hero

    def __str__(self):
        return f"{self.__j_name}:({self.__j_true_hero})"

    # setters
    def set_j_name(self, newName):
        self.__j_name = newName

    def set_j_name(self, new_true_hero):
        self.__j_name = new_true_hero

    # getters
    def get_j_name(self):
        return self.__j_name

    def j_true_hero(self):
        return self.__j_true_hero

    def welcomeToMyJungle(self, vName):
        print("Welcome to my Jungle, ", vName, " I am Omarzan the TRUE master of the Jungle, ready to serve!")
#class AfricanJungle(Jungle):
#    def __init__(self, j_name="unknown", j_true_hero="OmarZan", ):
#        Jungle.__init__(self, j_name="unknown", j_true_hero="OmarZan"):


#class SouthAmericanJungle(Jungle):
 #   def __init__(self, j_name="unknown", j_true_hero="OmarZan")
  #      Jungle.__init__(self, j_name="unknown", j_true_hero="OmarZan"):
