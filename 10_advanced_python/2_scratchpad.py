"""
Official way to swap two values in Python

This technique relies on the fact the right side of an
assignment is evaluated first, then the result is assigned
to the variable(s) on the left

We'll be using this technique in our generator

See the next python file
"""
a = 2
b = 3
print("a is {}, b is {}".format(a, b))

a, b = b, a
print("a is {}, b is {}".format(a, b))
