#Import the module
import Functions

deptList = {"Telecom","Banking"}
# Call the function in the Imported module
Functions._printme(deptList);

'''
When a module is imported for the first time a .pyc file containing the compiled code
should be created in a __pycache__ subdirectory of the directory containing the .py file.

'''