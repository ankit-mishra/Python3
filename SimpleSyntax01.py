

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