

class Car:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def __str__(self):
        return \
            self.__make + "\t"+ \
            self.__model  + "\t"+ \
            str(self.__mileage)  + "\t"+ \
            str(self.__price)
    def getMake(self):
        return self.__make

mycar = Car("Toyota", "Celica", 20000, 700)

print()
