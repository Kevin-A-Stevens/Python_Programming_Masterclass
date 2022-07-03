"""
for loops
an iterable objects is anything that can be iterated over
If you can use it with a for loop, it is iterable

for variable_name in iterable_object:

functions used
print()
isnumeric() = True of character is numeric
sum() = adds numbers
"""
parrot = "Norwegian Blue"

for character in parrot:
    print(character)

number = "9,223;372:036 854,775;807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

print("*" * 80)

# Extracting values from user input

user_number = input("Please enter a series of numbers using any separators: ")
separators = ""

for char in user_number:
    if not char.isnumeric():
        separators = separators + char

values = "".join(char if char not in separators else " " for char in user_number).split()
print(sum([int(val) for val in values]))


