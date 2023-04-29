

def main():
    print("Enter the names of three friends.")
    name1 = input("Friend #1: ")
    name2 = input("Friend #2: ")
    name3 = input("Friend #3: ")

    myfile = open("friends.txt", 'w')

    myfile.write(name1)
    myfile.write(name1)
    myfile.write(name1)
