'''
Variables and Types

Python is completely object oriented, and not "statically typed".
You do not need to declare variables before using them, or declare their type. 

Every variable in Python is an object.
'''
###################################################################################################
#                                          Numbers                                                #
###################################################################################################

# Python supports two types of numbers - integers and floating point numbers. (It also supports complex numbers)

# Define an integer
myint = 7
print(myint)

# Define a Floating point number
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

###################################################################################################
#                                          Strings                                                #
###################################################################################################

# Strings are defined either with a single quote or a double quotes.
mystring = 'hello'
print(mystring)

mystring = "hello"
print(mystring)

# Simple operators can be executed on numbers and strings.
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Assignments can be done on more than one variable "simultaneously" on the same line
a, b = 3, 4
print(a,b)

# Mixing operators between numbers and strings is not supported.
one = 1
two = 2
hello = "hello"

print(one + two + hello)




