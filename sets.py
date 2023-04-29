

#len function returns number of elements in set
# for item in set used to check if item is in set already
# use loop before ^
# dictionaries, sets, lists, data structures
#functional programming- break a problem into set functions
# that can use other functions
# divide and conquer

def main():
    set1 = {1,2,3,4,5,6,7}
    set2 = {4,5,6,7,8,9}
    print(set1 & set2)
    print(set1 - set2)
    print(set2 - set1)
    print(set1.union(set2))
    print(set1 | set2)
    set1 = set([1,2,3,4,5])
    print(set1)
    set2 = {item*2 for item in set1}
    print(set2)
    set3 = set([1,20,2,40,3,50])
    set4 = {item for item in set3 if item < 10}
    print(set4)
    set4 = {item for item in set3 if item > 100}
    print(set4)
    set4 = {item*20 for item in set3 if item <= 20}
    print(set4)
    # objective: print 100 elements
main()