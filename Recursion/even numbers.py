


def even(num):
    num = int(num)
    if num % 2 == 1:
        num = num +1


    elif num < lim:
        return even(num+1,lim)
        num = num + 1



def main():
    print("First")
    print("couple of even numbers")
    number = 0
    lim= int(input("Give me a number"))
    for number in range(number, lim):
        print(even(number, lim))

main()
