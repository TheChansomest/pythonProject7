

class Time:
    def __init__(self, h, m , s, h2):
        self.__h = h  # the __ gives data integrity
        self.__m = m
        self.__s = s

        self.h2 = h2

    def get_hours(self):
        return self.__h
    def set_hours(self, newh):
        if newh <= 24:      #checks to se if number is valid
            self.__h = newh
        else:
            print("Errororroro Invalid vlue for Hours")
def main():
    class_time = Time(13, 20, 0, 23)
    print(class_time.get_hours())

    class_time.__h = 15         # just to show you can't change the time like this
    print(class_time.get_hours())

    class_time.set_hours(15)
    print(class_time.get_hours())

    class_time.set_hours(899)
    print(class_time.get_hours())

    class_time.h2 = 987645
    print(class_time.h2)
main()