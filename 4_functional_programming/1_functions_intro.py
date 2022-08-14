"""
introduction to functions
Built-in function
https://docs.python.org/3/library/functions.html

We have run functions such as print() and range()
now we get to create our own functions

parameters are like placeholders for real values you will
pass to your function

"""

# defining a function


def multiply(x, y):
    result = x * y
    return result  # to find out what the function calculated
                   # and print it out later


# use the function
answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()
# can use our function in a for loop also
for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

