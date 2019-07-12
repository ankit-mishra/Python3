# Build and return a list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)

'''
The above code is simple and straightforward, but it builds the full list in memory.
This is clearly not acceptable, because we cannot afford to keep all n "10 megabyte" integers in memory.
'''

########################################################################################################################
# Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.#
########################################################################################################################

# Using the generator pattern (an iterable)
class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)

'''
This will perform as we expect, but we have the following issues:

    there is a lot of boilerplate
    the logic has to be expressed in a somewhat complex way
'''

########################################################################################################################
########################################################################################################################

# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)

'''
Note that the expression of the number generation logic is clear and natural.
It is very similar to the implementation that built a list in memory, but has the memory usage characteristic of the iterator implementation.
'''