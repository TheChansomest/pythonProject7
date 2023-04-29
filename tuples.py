

# Queue first in first out
# Stack- First in Last out
# Tuple: an immutable sequence (cant be changed)
# Dont have to worry about insertions
# cant use append, pop or other similar functions to it
thistuple = ("a", "b", "c")
# tuiples do not use the following methods
# -append, remove, insert, reverse, sort
# tupile() function: converts list to tuple

#operations for lists
# [] indexing: name=[2]
# len(str)
# [:] string[start : end] #slicing
# * repetation *: "hello"*25

#function methods
# str.count(item)
#ord('a') --> 97    (ASCII)
#char(97) --> 'a'
#str(197) --> '197'

name = "Chandler Wuchter"
space_position = name.index(" ")

first = name[0:space_position]
last = name[space_position + 1:]
print("Your name is")
print(first)
print(last)

print("{0} is a lot of {1}".format("Python", "fun!"))

sales = 3.123456
print("Sales:", format(sales, '10,.2f'))

message = "hi "
name = "     chan    "
name = name.strip().capitalize()
message += name +"!"
print(message)

