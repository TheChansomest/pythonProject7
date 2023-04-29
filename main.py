# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def sumToNum(num):
    acc = 0
    for x in range(1, num+1):
        acc = acc + x

    return acc

def getAvg(num):
    acc = sumToNum(num)
    avg = acc / num
    return avg
def sumB2Numbers(num, num1):
    adder = num + num1
    return adder
def main():
    x = int(input("give me a number"))
    y = int(input("give me a another number"))
    print("The sum of numbers between", x, "and", y, "is:", sumToNum(x))
    print("The avg is: ", getAvg(x))
    print("The sum between x and y is", sumB2Numbers(x,y))


main()
