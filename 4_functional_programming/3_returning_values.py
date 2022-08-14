"""
returning values

If you do not explicitly return something
your function will return None

functions used
print()

methods used
isnumeric()
"""
import random


def multiply(x, y):
    result = x * y
    # return result


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


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


answer = multiply(18, 3)
print(answer)

