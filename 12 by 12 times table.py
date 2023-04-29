# A 12x12 multiplication table made with
# while statements that has user inputs made by Chandler Wuchter
print("This is a multiplication table where you choose the bounds")
horiz= int(input("Choose a whole number for the horizontal axis of the table: "))
verti = int(input("Choose a whole number for the vertical axis of the table: "))

print("     ", end=" ")
#for x in range(1,horiz + 1):
    #print(x.format, end=" ")
print("\n")
for x in range(1,horiz + 1):
    print("__________", end="")
for x in range(1,verti + 1):
    print("\n", x, " |", end=" ")
    for y in range(1,horiz + 1):
        print(x * y,"\t", end=" ")
        
