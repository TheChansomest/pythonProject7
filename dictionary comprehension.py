

numbers = [1,2,3,4,5,6,7,8]
squares = {}
for item in numbers:
    squares[item] = item**2

print(squares)
#or

squares = {item:item**2 for item in numbers}
print("2nd time")
print(squares)