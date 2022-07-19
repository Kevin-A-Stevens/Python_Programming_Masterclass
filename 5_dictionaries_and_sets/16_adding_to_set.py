"""
Adding items to a set

you cannot create an empty set with {}
This would actually create an empty dictionary

You can create an empty set with a literal
but do not do this

A better way to create an empty set is with set()

functions uses
set()
print()

methods used
.add()

"""
numbers = {}
print(numbers, type(numbers))

# creates an empty set but don't do this
numbers_set = {*""}
another_numbers_set = {*{}}

# the set() function creates an empty set
numbers2 = set()
print(numbers2, type(numbers2))

numbers2.add(1)
print(numbers2)

while len(numbers2) < 4:
    next_value = int(input("Please enter your next value: "))
    numbers2.add(next_value)
print(numbers2)

