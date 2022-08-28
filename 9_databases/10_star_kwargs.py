"""
*kwargs = allows a function to take a variable number of keyword arguments
"""


def print_backwards(*args, **kwargs):
    print(kwargs)  # kwargs is a dictionary
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


with open("backwards.txt", "w") as backwards:
    print_backwards("hello", "planet", "earth", file=backwards)

