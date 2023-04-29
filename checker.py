user_number = input("Give me a number: ")
try:
    int(user_number)
except:
    print("That's not an integer number.")
print(user_number)