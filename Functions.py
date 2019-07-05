'''
This is a training material for Python 3
Functions
    How to define a function
    How to call a function
    Pass by Reference
    Types of arguments in function (Required, Keyword, Default, Variable length)
    Scope of variables (Global and Local)

'''

# How to define a function
#   Function blocks begin with the keyword def
#   followed by the function name and parentheses ( ( ) ).
#   The code block within every function starts with a colon (:)


# Function definition is here
def _printme( deptList ):
   "This prints a passed argument into this function"
   print (deptList)
   return

# Now you can call printme function
_printme("function provides modularity and code reusability !")


'''
PEP Conventions
Single and double underscores have a meaning in Python variable and method names.
    Single Leading Underscore: _var
    The underscore prefix is meant as a hint to another programmer that a variable or method starting with a single underscore is intended for internal use.
    E.g. from M import * does not import objects whose name starts with an underscore..

    Single Trailing Underscore: var_
    Sometimes the most fitting name for a variable is already taken by a keyword. Therefore names like class or def cannot be used as variable names in Python.
    In this case you can append a single underscore to break the naming conflict:

    Double Leading Underscore: __var
    With Python class attributes (variables and methods) that start with double underscores, things are a little different.
    A double underscore prefix causes the Python interpreter to rewrite the attribute name in order to avoid naming conflicts in subclasses.
    This is also called name mangling—the interpreter changes the name of the variable in a way that makes it harder to create collisions when the class is extended later.

    Double Leading and Trailing Underscore: __var__
    Perhaps surprisingly, name mangling is not applied if a name starts and ends with double underscores.
    Variables surrounded by a double underscore prefix and postfix are left unscathed by the Python interpeter.
    This rule covers things like __init__ for object constructors, or __call__ to make an object callable.

    Single Underscore: _
    Per convention, a single standalone underscore is sometimes used as a name to indicate that a variable is temporary or insignificant.

    For example, in the following loop we don’t need access to the running index 
    and we can use “_” to indicate that it is just a temporary value:

    >>> for _ in range(32):
    ...     print('Hello, World.')
'''
# Pass by Reference
# All parameters (arguments) in the Python language are passed by reference.

def _printme( deptList ):
   "Below deptList is a local variable"
   deptList = ["PCS","ADNS","MES"]
   print (deptList)
   return

# Below deptList is a global variable
deptList = ["Telecom","Banking","Aeroline"]
_printme (deptList)
print (deptList)

# In above example deptList is a required argument

def _print( deptList, deptHead ):
   print (deptList, deptHead)
   return

_print(deptHead = ["Murari","Manni"], deptList = ["Telecom","Banking","Aeroline"])

# When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.

def _print( deptList, deptHead = "Ankit"):
   print (deptList, deptHead)
   return

deptList = ["Telecom","Banking","Aeroline"]
_print(deptList)

# A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.

####################################################################################################################################
####################################################################################################################################

# Variable-length Arguments
def _printarg( *deptList):
    for var in deptList:
      print (var)
    return

deptList = ["Telecome","Banking","Aeroline"]
_printarg(deptList)