'''
Copy an Object in Python

In Python, we use = operator to create a copy of an object.
You may think that this creates a new object; it doesn't.

It only creates a new variable that shares the reference of the original object.
'''

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

# As you can see from the output both variables old_list and new_list shares the same id.

############################################################################################################
# You may want to have the original values unchanged and only modify the new values or vice versa.
# In Python, there are two ways to create copies:
####                                            Shallow Copy
####                                            Deep Copy

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

# We use the copy module of Python for shallow and deep copy operations. Suppose, you need to copy the compound list say x.
# Here, the copy() return a shallow copy of x. Similarly, deepcopy() return a deep copy of x.