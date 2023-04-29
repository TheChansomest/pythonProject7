
class Point:
    def __init__(self, x1, y1):
        self.__x = x1
        self.__y = y1

class Shape:
    def __init__(self, newx):
        self.__x = newx
        self.point = Point(3,4)

    def getX(self):
        return self.__x

    def setX(self, newx):
        if newx > 0:
            self.__x = newx
        else:
            print("Error x Shall be >= 0")


    def getArea(self):
        return 0

class Square(Shape):
    def __init__(self, newx):
        Shape.__init__(self, newx)

    def getArea(self):
        return self.getX()**2

class Rectangle(Shape):
    def __init__(self, newx, newy):
        Shape.__init__(self, newx)
        self.__y = newy

    def getY(self):
        return self.__y
    def setY(self, newy):
        if self.__y >= 0:
            self.__y = newy
        else:
            print("Error y must be greater than or equal to zero")

    def getArea(self):
        return self.getX() * self.getY()

def main():
    so1 = Shape(7)
    so2 = Shape(9)

    so1.getArea()
    so2.getArea()

    sqo = Square(6)
    ro = Rectangle(7, 8)

    print("Shape Objects Area: so1 area = ", so1.getArea(), "\tso2 area = ", so2.getArea())

    print("Square Object sqo Area = ", sqo.getArea())
    print("Rectangle Object ro Area = ",ro.getArea())

    print("-" * 55)
    shape_list = [so1, sqo, ro, Shape(9), Square(10), Rectangle(8, 12)]
    # isinstance(object, type)
    print("\nisinstance?\tObject Area")
    print("-----------\t------ ----")
    for s in shape_list:
        print(isinstance(s, Shape), "\t\t", s.getArea())  # polymorphic call to getArea() method

    print("\nEnd Main\n")

main()