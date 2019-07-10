#####################################################################################################################
# Below example opens a file, writes content in the, file and comes out gracefully because there is no problem at all
#####################################################################################################################

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()


   '''
   A single try statement can have multiple except statements.
   After the except clause(s), you can include an else-clause.
    The code in the else-block executes if the code in the try: block does not raise an exception.
   '''
##############################################################################################################
# Below example tries to open a file where you do not have the write permission, so it raises an exception
##############################################################################################################

try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")

##############################################################################################################
# Below example tries to catch the nested exceptions
##############################################################################################################

try: 
   num = int(raw_input("Enter the number ")) 
   re = 100/num
except NameError:
   print("Name is not specified")
except ValueError:
   print("Value is not int type")
except ZeroDivisionError: 
   print("Don't use zero")
else:
   print("result is ",re)

##############################################################################################################
# Below example tries to catch the multiple exceptions in one go
##############################################################################################################

try: 
   num = int(raw_input("Enter the number ")) 
   re = 100/num
# An except clause may name multiple exceptions as a parenthesized tuple, for example
except (NameError, ValueError, ZeroDivisionError) as e:
   print("Anyone of above exception occured")
else:
   print("result is ",re)

###############################################################################################################
#The try-finally Clause
#You can use a finally: block along with a try: block. The finally: block is a place to put any code that must execute,
#whether the try-block raised an exception or not.
###############################################################################################################

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print ("Error: can\'t find file or read data")
   fh.close()
###############################################################################################################
try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print ("Error: can\'t find file or read data")

###############################################################################################################
# Throw an Exception using raise keyword
###############################################################################################################

def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
   return level
