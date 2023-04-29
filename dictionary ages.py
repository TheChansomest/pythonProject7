
def main():
    #create an empty dictionary
    # birthdays = {}
    # what we will do
    # make a dictionary like {1:2 , 2:5 , ...}
    # first digit equals the number, second number equal the
    # amount of time that number is repeated

    #        key  value   k   v
    ages = {'omar': 45, 'chan': 19}
    print(ages)
    print(ages['chan'])

    for key in ages:
        print(key)
    # ages['Tom2' = 88]
    for key in ages:
        print(key, ":", ages[key])

    lk = ages.keys()
    lvs = ages.values()
    print(lk)
    print(lvs)


main()



#pop method FIFO
# format    dictionary.pop(key, default)