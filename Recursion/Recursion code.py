def message(times):
    if times>0:
        print("e", times)
        message(times-1)

times = 5
message(times)


def main():
    print("10")
    print("fibonacci")

    for number in range(1,11):
        print(fib(number))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: return fib(n-1) + fib(n-2)

main()

