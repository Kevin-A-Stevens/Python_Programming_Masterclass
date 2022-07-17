"""
functions with multiple arguments
using *args

note that *args, *values, *anything mean the same thing
*args is recommended though and that is what you
will most likely see being used in programs

using *args we can use a variable number
of arguments in our function (0 or more)

*args represents an unpacked tuple
"""
numbers = (0, 1, 2, 3, 4, 5)

print(numbers)
print(*numbers)  # unpacks the tuple

# can use * to unpack any sequence type


def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()  # ()



