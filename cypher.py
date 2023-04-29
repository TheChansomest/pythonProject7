
def main():
    phrase = input("put in a name to be decifered: ")
    even_character = ""
    odd_character = ""
    for i in range(len(phrase)):
        if i % 2 == 0:
            even_character += phrase[i]
        else:
            odd_character += phrase[i]
    print(odd_character + even_character)



main()