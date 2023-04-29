def print_line(what):
    print("-" * 20, "\t", what, "\t", "-" * 20)


# Collections: 1. dictionaries
print_line("1. dictionaries")
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key, end=", ")

# Collections: 2. Lists
print_line("2. lists")


# Collections: 3. Sets
print_line("3. Sets")


# # Collections: 1. Tuples
print_line("4. Tuples")


# OO 1. Basics
print_line("Object-Oriented - 1. Basics")
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

# OO 2. __init__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
       return "Welcome " + self.name

    def myfunc(self):
        print("Hello my name is " , self.name, "you are ", self.age, " years old")

print_line("Object-Oriented - 2. __init__")
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1)

# OO 3.  methods myfunc()
print_line("Object-Oriented - 3.  methods myfunc() ...")
p2 = Person("Omar", 38)
p2.myfunc()

# OO 4.  Inheritance
class Person2:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person2):
    def __init__(self, fname, lname, year):
        self.graduationyear = year

        Person2.__init__(self, fname, lname)  # or use super().__init__(fname, lname)


    def welcome(self):
        print("Welcome", self.__fname, self.__lname, "to the class of", self.graduationyear)


#Use the Person class to create an object, and then execute the printname method:
x = Person2("John", "Doe")
x.printname()

s1 = Student("Omar", "Alzoubi", 2026)
s1.welcome()
s1.printname()

