

names = ['Jim', 'Jill', 'John', 'Jasmine']
tm = 'Jasmine'
"""
if tm not in names: 
     print('Cannot find Jasmine.') 
else: 
    print("Jasmine's family:") 
    print(names)
    """
    #convert this code without using the "not in" operator,
    # and produce the same results
i = 0
while i < len(names):
    if tm == names[i]:
        print("Good its in")
    i +=1
# i = 0 code is the same as using the not in function
for n in names:   #iterator design pattern
    print(n)