


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def __str__(self):
        return "Welcome " + self.name

    def myFunc(self):
        print("Hello my name is", self.name, ", I am", self.age, "Years old")

#print_line("object-orientated - 2 .__init__")
p1 = Person("john", 36)
print(p1.name)
print(p1.age)
print(p1)

p2 = Person("Omar", 38)
p2.myFunc()