###################################################################################################
#                                          String                                              #
###################################################################################################

'''
Basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)

'''

# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list)
# together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

name = "John"
print("Hello, %s!" % name)

# To use two or more argument specifiers, use a tuple (parentheses)
name = "John"
age = 23
print("%s is %d years old." % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

# Any object which is not a string can be formatted using the %s operator as well.

astring = "Hello world!"
print(len(astring))
print(astring.index("o"))
print(astring.count("l"))
print(astring[3:7])
print(astring[3:7:2]) # This prints the characters of string from 3 to 7 skipping one character. The general form is [start:stop:step].
print(astring[::-1]) # to reverse a string
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
afewwords = astring.split(" ")
print(afewwords)

