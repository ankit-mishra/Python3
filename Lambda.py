'''
    In this discussion we will cover below topics
    -   Lambda function
    -   Map function
    -   Filter function
'''

# Define Function
def add(x, y): 
    return x + y
  
# Call the function
add(2, 3)  # Output: 5

# Use of Lambda Function
add = lambda x, y : x + y 
  
print(add(2, 3)) # Output: 5

def multiply2(x):
  return x * 2
    
map(multiply2, [1, 2, 3, 4])  # Output [2, 4, 6, 8]
# print(map(multiply2, [1, 2, 3, 4]))

numlist = [1, 2, 3, 4, 5]

filter_obj = filter(lambda x: x % 2 == 0, numlist) # filter object <filter at 0x4e45890>

even_num = list(filter_obj) # Converts the filer obj to a list

print(even_num) # Output: [2, 4]