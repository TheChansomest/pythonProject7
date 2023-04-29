


def main():
    string = input_string()
    print_backwards(string)
def input_string():
    string = (input("Input a string to be printed backwords: "))
    return str(string)
def print_backwards(string):
    for i in range(len(string) - 1, -1, -1):
        print(string[i], end='')

main()