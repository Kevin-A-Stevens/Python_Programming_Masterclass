"""
*args = allows a function to take a variable number of arguments
"""


def average(*args):
    print(type(args))  # args is a tuple
    print("args is {}: ".format(args))  # args = a tuple
    print("*args is: ", *args)  # *args unpacks the tuple
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


print(average(1, 2, 3, 4))


