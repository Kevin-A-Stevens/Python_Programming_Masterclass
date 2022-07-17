"""
documenting your code

To set docstring type
File > Settings > Tools > Python Integrated Tools
Select docstring format

writing a docstring
"""
import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


# get function details (docstring)
print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)

# Another way to get a docstring for a function
help(get_integer)

highest = 1000
# dot notation module.function
answer = random.randint(1, highest)
guess = 0  # initialize to any number that does not equal the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")

