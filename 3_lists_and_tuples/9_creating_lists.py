"""
creating lists

functions used
sorted()
print()
list()

methods used
.copy()
"""

empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# concatenate two or more lists
numbers = even + odd
print(numbers)

# using a function that returns a list
sorted_numbers = sorted(numbers)
print(sorted_numbers)

digits = sorted("432985617")
print(digits)

more_digits = list("678213493")
print(more_digits)

more_numbers = list(numbers)
print(more_numbers)

print(numbers is more_numbers)  # False = different lists
print(numbers == more_numbers)  # True = same items

more_numbers2 = numbers.copy()
print(more_numbers2)

