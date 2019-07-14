'''
We can use assert statement in two ways as mentioned above.

assert statement has a condition and if the condition is not satisfied the program will stop and give AssertionError.
assert statement can also have a condition and a optional error message.
If the condition is not satisfied assert stops the program and gives AssertionError along with the error message.

'''

def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))