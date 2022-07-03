"""
The random module and importing
improving our guessing game
We want to use the randint function from the random module
"""
import random

highest = 1000
# dot notation module.function
answer = random.randint(1, highest)
guess = 0  # initialize to any number that does not equal the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
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

