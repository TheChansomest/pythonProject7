# Exam stuff
#
#
# UML diagram: standard diagrams for graphically
# depicting object-orientated systems
#   stands for Unified Modeling Language
# General layout
#   top section: name fo the class   ex.    coin
#   middle: list of data attributes         __sideup
#   bottom: list of class methods           __init__()
#       toss()
#       get_sideup()
#
# mainly object-oriented programing on quiz


# about collections
# tuple can't be changed, are safer and faster because they
# can't be changed, making them immutable

# lists, dictionaries, and sets
# list
mList = [1, 2, 3, 4, 5, 9, 10, 'a', 'chan', [1, 2, 3]]
# Can have anything in a list, even another list
# lists are mutable
# Can append to the list. append(8) would add 8
mList.append(8)
# to the end of the list
print(mList)
# % returns the remainder after division
# this slice method [:] can be used to capy a list
copyList = mList[:]
print(copyList)
# Quiz potentials
# list.append(item) new items are added to the end of the list
# most important function of a list
# len(mylist)

# List can be  indexed mList[3] gets fourth element
print(mList[3])

# , sliced    mList[1:3] gets first but not last
# , trimmed
# , checked -- in or not in
# , inserted    mList = (1,2,3)
# ,    mList.append(8)
# ,         won't work because the list is a tuple

# del mList gets rid of the list
# loop through list elements:
#  for x in mList:
#       print(x)

mList = [1, 2, 3, 4]
# for i in range(len(mList)):     len(mList) = 4
#       print(mList[i])

[print(x) for x in mList]

# comprehended
newList = [x for x in mList if int(x) > 3]
print(newList)

# tuples can't be updated
# What operations tuples do not support? any methods that would change them,
# because they are immutable
# Why tuples?   They are safe and are the fastest to run
# Tuples can have duplicates in them
#
# Dictionary are sometimes referred to as maps

#
# for key,value in phonebook.items():
# ,      print(key, value)
#for key in phonebook.items():
# ,      print(key)      returns keys of a dictionary

# noooo duplicates in sets. it is unchangeable (immutable)
# you can still add to the set though
# set is a class
# myset = set()
# myset = set (['a', 'b', 'c')]
# myset = set('abc')
# print(myset)

# myset = set([1, 2, 3, 4, 5,])

# intersection, union, and minus methods of sets
# read book maybe or review w3schools to recap and do well on quiz