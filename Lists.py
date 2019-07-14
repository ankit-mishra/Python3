'''
Lists
'''

###################################################################################################
#                                          Lists                                                  #
###################################################################################################

# Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish.
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

# Accessing an index which does not exist generates an exception (IndexError: list index out of range).
mylist = [1,2,3]
print(mylist[10])

