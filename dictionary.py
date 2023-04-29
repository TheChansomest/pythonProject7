

#nonsequential collections --> Dictionaries

#Dictionary - most important data structure
# for big corporations (elastic computing). Very efficient
#
#sets

# finding a mod of a list
def main():
    list1 = [1, 1, 2, 3, 4, 5, ]
    print(mode(list1))
    list2 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6]
    print(mode(list2))


def mode(alist):
    countDict = {}

    for item in alist:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1
    countList = countDict.values()
    maxcount = max(countList)


main()