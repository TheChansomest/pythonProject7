



def main():
    phrase = input("Put in a phrase to be deciphered: ")
    even_characters = ""
    odd_characters = ""
    for i in range(len(phrase)):
        if i % 2 == 0:
            even_characters += phrase[i]
        else:
            odd_characters += phrase[i]
    print(odd_characters + even_characters)
    return
    decipher()

def decipher(odd_characters, even_characters):
    phrase = ""
    for i in range(max(len(odd_characters), len(even_characters))):
        if i < len(odd_characters):
            phrase += odd_characters[i]
        if i < len(even_characters):
            phrase += even_characters[i]
    return phrase


main()